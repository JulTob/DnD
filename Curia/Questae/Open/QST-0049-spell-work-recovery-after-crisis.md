# QST-0049 — 🔴 RECOVERY BOARD: spell-work losses after the crisis

- **Type:** chore/cleanup (recovery)
- **Priority:** 🔴 urgent
- **Status:** Open — **coordination board for concurrent recovery agents**
- **Owner:** unclaimed — *claim one restoration below by writing your name on its line before applying; the three are independent, do not collide*
- **Route to:** any recovery agent, Cleric (Repair), Rogue (Testing), Julio
- **Parent:** —
- **Sidequests:** — (kept as one board on purpose during the live scramble; split into .1/.2/.3 only if recovery runs long)
- **Related:** QST-0031.* (the spell TOP arc these belong to), the reflog `reset`+`fdf3b08` crisis commit

---

## 🔍 Diagnosis (what & where)
An external agent ("Grok") reset and re-committed the working tree. HEAD is now `fdf3b08` ("Refactor module imports and update documentation") and the tree is **clean** — meaning every uncommitted piece of the spell-refactor session was frozen into that commit as a **partial, mixed snapshot**: some of the session work survived, three specific pieces were lost. This board is the authoritative forensic map so recovery agents do not duplicate effort or collide.

**Good news up front:** almost everything survived, and all three losses are **fully reconstructible** — two from verbatim content reproduced below, one deterministically from surviving data. Nothing needs to be re-derived from scratch.

## 🧾 Evidence (git forensics, read-only)
- `git reflog`: `4fa25dc HEAD@{1}: reset: moving to HEAD` then `fdf3b08 HEAD@{0}: commit` — the reset-then-commit that froze the mixed state.
- `git fsck`: 4 dangling commits (`81c66cf`, `6b24a1b`, `83abdcc`, `187f79c`) — all July/August, **none contain the Ledger or SpellsKit `__format__`**. The git object store has no copy of the two lost code pieces.
- `git stash@{0}` ("epitaxy: pre-switch") holds only `Documenta/Sources` deletions + `__init__` churn — **not** our work; leave it.
- `git log --all -- AtlasMagia/Ledger_of_Spell_Lists.py` → empty: the Ledger was never committed on any ref.
- `Documenta/Sources/{recovery_files,transcript_claude,transcript_claude_II}.txt` **do** mention both `Ledger_of_Spell` and `__format__` — a secondary text-recovery source if the appendices below are ever in doubt.

### Damage map
| Piece | State | Recovery source |
|---|---|---|
| Curia quests QST-0030…0039 | ✅ survived | — |
| `style.css` font work (`--font-spell-title`, `--font-magic-script`, `.magic-chip`, `.known-spells`) | ✅ survived | — |
| SpellsKit: `Legacy` tag, `Assign_Legacy`, `Spell_Level` family | ✅ survived | — |
| `Grimoire._bears` spellcaster dispatch fix | ✅ survived | — |
| shiny_app: `magic_chip`, French Canon font link, ritual/`level=` fix | ✅ survived (churning under concurrent edits) | — |
| **1. `AtlasMagia/Ledger_of_Spell_Lists.py`** | ❌ **deleted** (disk + git) | Reconstruct from surviving `Grimoire.SPELL_LISTS` literal (healthy, now 17 classes incl. Artificer line) + scaffold in Appendix A |
| **2. SpellsKit `__format__`/`html`/`md`/aliases/`_html_to_md_lite`** | ❌ **stripped** (only `def string` remains at ~L112) | Verbatim in Appendix B |
| **3. shiny_app `known-spells` class** on the Known Spells rail box | ❌ **reverted** (the `.known-spells` CSS rule is orphaned) | One-liner in Appendix C |

## 🎯 Desired outcome
The three lost pieces restored into a working tree that passes `python -m AtlasMagia.SpellsKit`, imports `shiny_app` clean, and renders a level-20 wizard with spell cards (`{spell:html}`) and a script-font Known Spells list. Then a single commit so this can never silently vanish again.

## 🧭 Notes for the Agora / recovery agents (coordination)
- **Claim before you apply.** Three independent restorations; write your handle on the piece you take (edit this file's Owner line or add a note) so two agents don't both patch SpellsKit.
- **Do not `git reset --hard`, `git checkout .`, or `git clean`** — the tree is the only live copy of the *surviving* work; a blunt reset would repeat the crisis.
- **Verify, don't assume.** Files are changing live under concurrent agents; re-grep before patching (`grep -c __format__ AtlasMagia/SpellsKit.py`), and if a piece is already restored by another agent, tick it here instead of re-applying.
- **Ledger placement:** `AtlasMagia/Ledger_of_Spell_Lists.py`; it imports spells from the Lodge and applies `Spell_List`/`Tradition` tags. Its data (`LEDGER` dict) is a mechanical transcription of `Grimoire.SPELL_LISTS` — same class→level→[names] shape. Regenerate it from that literal rather than hand-typing.
- **Commit when green** so the recovered state is durable — the root cause of this whole incident is that hours of work sat uncommitted.

---

## 📎 Appendix A — Ledger scaffold (reconstruct the `LEDGER` middle from `Grimoire.SPELL_LISTS`)
```python
'''
Ledger of Spell Lists — who may learn what.
Importing this file applies Spell_List + Tradition tags to every listed
spell and publishes SPELL_LISTS in the shape Grimoire_of_Spellcasters
consumes. List order is behavior (seeded draws), so preserve it.
Paladin's list (empty for the project's whole life) is filled here.
'''
from AtlasMagia.SpellsKit import (
	Spell, Spell_List, Wizard_List, SPELL_LISTS_TAGS, TRADITION_OF_LIST, Arcane,
)
import AtlasMagia.Lodge_of_Spells as _Lodge

# Subclass lists inherit the class list they draw from (interim home; their
# forever-home is each subclass file once the class system gets its TOP pass).
class Eldritch_Knight_List(Wizard_List):
	NAME = "Eldritch Knight"; DESCRIPTION = "On the Eldritch Knight (Fighter) subclass list."
class Arcane_Trickster_List(Wizard_List):
	NAME = "Arcane Trickster"; DESCRIPTION = "On the Arcane Trickster (Rogue) subclass list."

LIST_TAGS = dict(SPELL_LISTS_TAGS)
LIST_TAGS["Eldritch Knight"] = Eldritch_Knight_List
LIST_TAGS["Arcane Trickster"] = Arcane_Trickster_List
TRADITIONS_HERE = dict(TRADITION_OF_LIST)
TRADITIONS_HERE["Eldritch Knight"] = Arcane
TRADITIONS_HERE["Arcane Trickster"] = Arcane

LEDGER = {
	# ← transcribe Grimoire.SPELL_LISTS here: {class: {level: [spell names]}}
	# (mechanical copy of the surviving literal; keep list order intact)
}

# Build a name→Spell index from the Lodge, then tag + publish.
_INDEX = {s.name: s for s in vars(_Lodge).values() if isinstance(s, Spell)}
SPELL_LISTS = {}
for _cls, _levels in LEDGER.items():
	_tag = LIST_TAGS.get(_cls); _tradition = TRADITIONS_HERE.get(_cls)
	SPELL_LISTS[_cls] = {}
	for _lvl, _names in _levels.items():
		_pool = []
		for _nm in _names:
			_spell = _INDEX[_nm]              # loud KeyError: no list may name a ghost
			if _tag is not None: _tag(_spell)
			if _tradition is not None: _tradition(_spell)
			_pool.append(_spell)
		SPELL_LISTS[_cls][_lvl] = _pool

if __name__ == '__main__':
	assert SPELL_LISTS['Wizard'][3] and SPELL_LISTS['Paladin'][1]
	_fb = _INDEX['Fireball']; assert _fb in Wizard_List and _fb in Arcane
	print('Ledger_of_Spell_Lists self-test passed.')
```
Then Grimoire's own `SPELL_LISTS = {…literal…}` becomes `from AtlasMagia.Ledger_of_Spell_Lists import SPELL_LISTS` (the literal is the transcription source — copy it into `LEDGER` before deleting it from Grimoire).

## 📎 Appendix B — SpellsKit render block (verbatim; slot in place of the current `__str__`, before `@property def string`)
Requires `import re` at module top (already present). `def _html_to_md_lite` and the two module-level `as_html`/`as_md` functions go just after the `Spell` class.
```python
	def __str__(spell):
		"""Plain Entry form. f"{spell:html}" / f"{spell:md}" pick richer shapes."""
		return spell.string

	def __format__(spell, spec):
		"""Dispatch f"{spell:html}" / f"{spell:md}" / f"{spell}" (plain)."""
		spec = (spec or "").strip().lower()
		if spec in ("html", "card"):    return spell.html()
		if spec in ("md", "markdown"):  return spell.md()
		if spec in ("", "s", "str", "plain"): return str(spell)
		raise ValueError(f"Unknown Spell format spec {spec!r} — use html, md, or plain")

	def html(spell):
		"""HTML spell card. Aliases: as_html; f"{spell:html}"."""
		desc = ""
		if spell.casting_time:   desc += f"<i>⟨{spell.casting_time}⟩</i><br>"
		if spell.ritual:         desc += "<i>(Ritual)</i><br>"
		if spell.concentration:  desc += f"<i>({spell.concentration}: </i>"
		if spell.duration:       desc += f"<i>({spell.duration})</i>"
		if spell.ranges:         desc += f"<br><i>>{spell.ranges}></i>"
		if spell.components:     desc += f"<br><i>⦓{spell.components}⦔</i>"
		level_text = "<b><p>Cantrip</b></p>" if spell.level == 0 else f"<b><p> Level {spell.level} Spell </b></p>"
		return f'''
		<h4 class="spell-title"> {spell.name}</h4>
		{level_text}
		<p class="spell-meta">{desc}</p>
		<p>
		{spell.definition }
		</p>
		'''

	def md(spell):
		"""Markdown spell sheet. Aliases: markdown, as_md; f"{spell:md}"."""
		level_text = "Cantrip" if spell.level == 0 else f"Level {spell.level}"
		meta = [level_text]
		if spell.school:         meta.append(str(spell.school))
		if spell.ritual:         meta.append("Ritual")
		if spell.concentration:  meta.append(str(spell.concentration))
		lines = [f"### {spell.name}", f"*{' · '.join(meta)}*", ""]
		if spell.casting_time:   lines.append(f"- **Casting Time:** {spell.casting_time}")
		if spell.ranges:         lines.append(f"- **Range:** {spell.ranges}")
		if spell.components:     lines.append(f"- **Components:** {spell.components}")
		if spell.duration:       lines.append(f"- **Duration:** {spell.duration}")
		lines.append("")
		lines.append(_html_to_md_lite(spell.definition))
		return "\n".join(lines)

	# Aliases are good and free — each name reads best in its own context.
	as_html = html
	as_md = md
	markdown = md
```
Module-level (after the `Spell` class body):
```python
def _html_to_md_lite(text):
	"""Definitions carry light HTML (<br>, <b>, <i>); fold it into markdown."""
	text = re.sub(r"<br\s*/?>", "\n", str(text))
	text = re.sub(r"</?b>", "**", text)
	text = re.sub(r"</?i>", "*", text)
	text = re.sub(r"</?(p|ul|li|div|h[1-6])[^>]*>", "\n", text)
	return re.sub(r"\n{3,}", "\n\n", text).strip()

def as_html(spell): return spell.html()
def as_md(spell):   return spell.md()
```

## 📎 Appendix C — shiny_app Known Spells rail box (one-liner)
On the Known Spells rail box `ui.div`, change its class from `"npc-textbox"` to `"npc-textbox known-spells"` so the surviving `.known-spells li { font-family: var(--font-magic-script); … }` rule applies. Also confirm the spellbook cards use `f"{spell:html}"` (restored in Appendix B) rather than raw `{spell}`.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** commit spell-refactor work in small, frequent commits — the entire loss surface here was *uncommitted* working-tree state that a single external reset froze into a mixed snapshot.

---

## 🏛️ Council
> Repair Consul (Cleric): The wound is small and clean — three severed pieces, each with a graft ready. Don't reopen healthy tissue (no hard reset); suture the three and commit.
> Testing Consul (Rogue): The tripwire is a level-20 wizard with zero spell cards — that's the render that proves all three grafts took. Run it before declaring the recovery done.

**Weighting:** reach 2 × severity 3 = **6** · council leaning: `build` (apply the three grafts, verify the wizard renders, commit)
