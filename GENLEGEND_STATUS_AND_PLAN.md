# GenLegend — Status, Cleanup & TOP Integration Plan

*Updated 2026-07-07 (session with Claude; prior assessment of 2026-06-30 superseded).
Priority unchanged: make it work first, then cut dead weight, then integrate TOP.*

---

## 1. Where it stands now

**Phase 0 (make it run for real) is done. The migration is committed.**

- Baseline commit `86ba494` snapshots the whole Flask→Shiny working tree; four
  follow-up commits fix the blockers (`92988d7`, `35031e6`, `d220d38`, `b4f0b90`).
- **Everything compiles.** Full-repo sweep clean on Python 3.10 (the promised
  floor in `requirements.txt`; 3.14 recommended).
- **Real generation verified end-to-end, no stubs:** NPC ("Lunerasia
  Stormwatcher — Fey Expert"), Character ("Finarion Zalaton, L3"), and the four
  repaired Races genera (Aberration / Celestial / Elf / Monstrosity) all load
  their real modules — 162 / 844 / 1591 / 318 names instead of the plantilla
  fallback.
- **The silent import shim is gone** (QST-0009 → Solved). Imports fail fast and
  loud; `summon_character` / `summon_npc` retry fresh seeds with every failed
  attempt reported through `@minion` into the `@chronicler` account. The user
  always gets a character; every error is on the record.
- **The Atlases are regular packages** (docstring `__init__.py`, pattern from
  AtlasVenustas). Imports no longer depend on the working directory.
- `npc_namer_legacy.py` deleted (5061 lines, superseded, unparseable) —
  recoverable from `86ba494` if ever needed.

Entry point unchanged: `shiny run shiny_app.py` (or `make run`, `app.py`).

## 2. What remains before "usable v1" (QST-0001 spine)

- **Front polish & flows** — QST-0001 (finish the Shiny front), QST-0002
  (character-sheet view), QST-0008 (NPC sheet still boxes), QST-0010
  (extract inline CSS/JS), QST-0011 (npc list dead links), QST-0012 (HTML
  escaping). The Shiny app itself boots; these are quality gaps, not blockers.
- **Flask removal** — QST-0003, *deferred by Julio 2026-07-07 (code fixes only
  that session)*. `app/routes.py`, templates, static and the R-era files still
  await the sweep; `app/character_url.py` and `app/random.py` stay (Shiny
  imports them).
- **Venv & deploy unification** — QST-0004 (ruled, awaiting go/no-go);
  deploy config still spans app.yaml / Dockerfile / Run_And_Deploy.sh —
  pick one target.
- **New:** QST-0021 — ~60 silent name fusions (missing commas) across the
  wider Races corpus, found by tokenizer sweep during the repair. Mechanical
  fix, per-file review.

## 3. TOP / TagKit integration (greenfield, unchanged plan)

TagKit is pinned in `requirements.txt` and imported **nowhere yet** — a clean
slate, as intended. AtlasTOP is gone from the tree (QST-0018; the fold-into-
Grimoires half is judged by Julio). With Phase 0 landed, tagging can start
without bugs hiding behind placeholder output:

1. **Conditions** (`Map_of_Conditions`) — overlay Tags on one creature-Agent.
2. **Species / Class / Background** — Tags layered on one stable identity
   (QST-0020 for Features; literally TOP's thesis).
3. **Resistances / Weaknesses / Senses** (AtlasPugna) as contributions.
4. **Spell effects / Enchantments** as Imprint/Rip duals.

Doctrine note: consult the pinned TagKit Guide before designing —
QST-0019 item 5 (Underlay, Conditions) still awaits the settled upstream text.

## 4. Practices ruled this session (remember these)

- **Import-time = fail fast. Generation-time = report loudly, recover with a
  fresh seed.** Never shadow real domain classes with placeholders.
- **Nothing is deleted until git can bring it back.** Baseline first, then cut;
  cite the recovering commit in the message.
- One concern per commit; the commit message carries the why.
