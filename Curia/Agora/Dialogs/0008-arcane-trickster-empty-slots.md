# Dialog 0008 — Arcane Trickster with no spell slots yet

- **Question:** When a caster subclass has no spell slots unlocked yet, what should `available_spells` return — and is the companion `NameError: char` the same wound?
- **Raised by:** Julio (via Agent)
- **Related Questae:** QST-0029
- **Consuls called:** Repair (Cleric), Methods (Wizard), Safety (Paladin), Testing (Rogue)
- **Status:** 🟢 converged — awaiting Julio

---

## 🧭 Framing

QST-0029 is a live generation crash: an Arcane Trickster whose slot table is still `(0,0,0,0)` hits `max()` on an empty generator. `summon_character`'s five retries cannot save it — the race/class/level/background shape is deterministic. The questa already sketches `max(..., default=0)` or an empty check. That sketch is evidence of options, not a Decree.

Canon: fail loud on illegal states; do not invent machinery; one purpose per questa. Out of scope: rewriting SPELL_LISTS, TagKit spell redesign (QST-0031), Eldritch Knight unless it shares this empty-`max` wound.

A good answer must: (1) name the contract of `available_spells` when the subclass is not a caster yet, (2) keep a legal Character summoning, (3) say whether the untraced `NameError: name 'char' is not defined` rides this questa or a sidequest.

---

## 🗣️ Deliberation

Repair Consul (Cleric): The innermost frame is `ArcaneTrickster.available_spells` at `Grimoire_of_Spellcasters.py:1586`. Levels 1–2 of that table grant zero slots and zero cantrips. `max()` has no default, the filtered generator is empty, `ValueError`. That is the wound. The second tree — `NameError: name 'char' is not defined` inside `Grimoire_of_Characters.py.__init__` — has no line. Character methods already take `char` as `self`; a Minion report can make that look like a second bug when it is only the wrapper re-raising. Isolate it. Do not close QST-0029 by assuming one patch heals both.

Methods Consul (Wizard): Two methods look similar and are not. `max(..., default=0)` then `k <= max_slot` unlocks every list key at or below 0. The Arcane Trickster list **has key 0** (cantrips). Levels 1–2 would then receive the full cantrip pool while the progression table says `cantrips: 0`. That is the wrong method wearing a one-argument costume. The correct method is: if no slot count is positive, return `[]` — the same contract as `if not source: return []` two lines above. Then, and only then, take `max` of the positive slots.

```python
slots = trickster.get_stats("slots")
if not any(n > 0 for n in slots.values()):
    return []
max_slot = max(level for level, n in slots.items() if n > 0)
return [spell for level in source if level <= max_slot for spell in source[level]]
```

Safety Consul (Paladin): A level-1 Rogue Arcane Trickster is a legal Character. Crashing is not fail-loud; it is punishing a valid input. Empty list is the honest result: not a caster yet. Retry at the summoner (QST-0009) must not be the safety net for a deterministic catalogue shape — we just watched that hide the Gnome import. After the contract is set, a self-test on this module should pin levels 1–2 as `[]` and level 3 as non-empty.

Testing Consul (Rogue): What breaks this? (1) Rogue + Arcane Trickster + level 1 or 2 — must summon. (2) Level 3 — must learn cantrips, including Mage Hand. (3) `max(..., default=0)` as a "fix" — must *not* leak cantrips at level 1. I want that third case as a regression, or the wrong patch will look green. Eldritch Knight uses `lvl <= caster.level`, not empty-`max`; grep finds only this one site. Leave EK out. For the `NameError`: reproduce the original seed with the slot guard in place. If `char` still explodes, throw **QST-0029.1**. If it vanishes, it was the Minion tree of the same `ValueError`.

Repair Consul (Cleric): Concede the NameError stays a sidequest until a post-fix trace. QST-0029's purpose is the empty-slot contract only.

Methods Consul (Wizard): No objection. Prefer `slots.items()` over `enumerate(values())` so slot *level* is the dict key, not an assumed 1-based position — `get_stats("slots")` already returns `{1: n, 2: n, …}`.

Safety Consul (Paladin): Converged. Loud failure remains for a missing SPELL_LISTS source; silence is only for "zero slots means no list yet."

Testing Consul (Rogue): Converged. Proof lives in `Grimoire_of_Spellcasters.py`'s `__main__`, not a distant tests folder.

---

## ✅ Convergence check
- [x] Every called Consul has spoken.
- [x] Every objection has been answered or conceded.
- [x] At least one concrete proposal (with code sketch) is on the table.

---

## 🕊️ Vox report

Vox: Report on **Q-0011 — Arcane Trickster with no spell slots yet.**

**The question.** When a caster subclass has no spell slots unlocked yet, what should `available_spells` return — and is the companion `NameError: char` the same wound?

**Common ground (unanimous among seats called):**
- The crash is real; the shape is legal; retry cannot save it.
- `available_spells` should return `[]` when every slot count is 0.
- QST-0029 stays one purpose: that contract. The untraced `NameError` is a sidequest (QST-0029.1) if it still reproduces after the guard.
- Eldritch Knight is out of this questa.
- Pin the behavior with a module self-test (levels 1–2 empty; level 3 has spells).

**Options & tradeoffs:**
1. **Guard, then max of positive slots** *(council's lead)* — `if not any(n > 0): return []`. *Pro:* matches the progression table (`cantrips`/`prepared`/`slots` all 0 at levels 1–2); same shape as the existing `if not source` early return. *Con:* two extra lines, not one.
2. **`max(..., default=0)`** *(questa's first sketch)* — *Pro:* smallest diff. *Con:* SPELL_LISTS key `0` is the cantrip list, so levels 1–2 would unlock cantrips the table forbids. The council rejects this as the fix.
3. **Do not construct ArcaneTrickster until level 3** — *Pro:* avoids the method entirely. *Con:* `spellcaster(character)` already branches on subclass membership; delaying construction is a wider contract change and can hide other `__init__` work. Rejected as overreach for this questa.

**Consul positions:**
- Cleric: isolate the NameError; heal only the empty-`max` wound here.
- Wizard: option 1; use `slots.items()` so levels are keys.
- Paladin: legal input must not crash; self-test is the guardrail.
- Rogue: prove level 1–2 empty *and* that option 2 would leak cantrips.

**Code proposal (illustrative):**
```python
def available_spells(trickster):
    source = (
        SPELL_LISTS.get("Arcane Trickster")
        or SPELL_LISTS.get("Wizard")
    )
    if not source:
        return []
    slots = trickster.get_stats("slots")
    if not any(n > 0 for n in slots.values()):
        return []
    max_slot = max(level for level, n in slots.items() if n > 0)
    return [
        spell
        for level in source
        if level <= max_slot
        for spell in source[level]
    ]
```

**Vox's synthesis.** Leading recommendation: **option 1** (empty list when no slots), implemented locally in `ArcaneTrickster.available_spells`, with a `__main__` self-test, and a sidequest only if `NameError: char` still traces after that. Strongest alternative: option 2, which Julio may still pick for minimal diff — the council's objection is the cantrip leak, not taste.

→ Awaiting Julio's decision. To be recorded as Decree 0004 (next free) once ratified.
