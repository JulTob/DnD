# QST-0030 — Minion.py's bug reports lose the signal they exist to carry

- **Type:** bug
- **Priority:** 🟠 high
- **Status:** Open — diagnosis only (do not patch piecemeal)
- **Owner:** unclaimed
- **Route to:** Flow Consul (Sorcerer), Repair Consul (Cleric), Barbarian, Lorekeeper
- **Parent:** —
- **Sidequests:** QST-0030.1 (duplicate/nested bug reports), QST-0030.2 (ANSI double-wrap), QST-0030.3 (call-tree blind outside app.py/shiny_app.py)
- **Related:** QST-0009 (Minions report, summoners recover), QST-0029 (a real crash this system was supposed to make legible)

---

## 🔍 Diagnosis (what & where)
`Minion.py` is the project's fail-reporting system — every generation attempt is wrapped in `@minion`/`@warden`/`@guardian`/`@watcher`, and `@chronicler` collects the account for one top-level job. It was live-tested against a real crash (a `TypeError` inside `Character.__init__`, reproduced with `char_class='Rogue', level=3, seed=3`) rather than only the self-test in `Minion.py`'s `__main__` block. Three independent, compounding defects surfaced, each recorded as its own sidequest so each can be fixed and verified on its own:

- **QST-0030.1** — one root-cause exception produces multiple, increasingly-redundant bug reports (one per nested `@minion`-decorated frame it passes through).
- **QST-0030.2** — the printed bug report's ANSI colors are double-wrapped and render broken.
- **QST-0030.3** — `get_call_tree()` is silently empty for any invocation that isn't through `app.py`/`shiny_app.py`.

## 🧾 Evidence
See each sidequest for its own captured output. Broadly: `AtlasLusoris/Grimoire_of_Characters.py` alone carries ~35 `@minion`/`@warden`/`@guardian` sites in one nested call chain (`__init__` → `set_char_features` → `apply_species_features` → …), which is exactly the shape that trips QST-0030.1.

## 🎯 Desired outcome
A single real failure produces **one** clean, correctly-colored report with full context — regardless of how many decorated frames it passes through on the way up, and regardless of whether the invocation came from the web app or a standalone script/test. See each sidequest for its specific target state.

## 🧭 Notes for the Agora / implementer
- These three are independent and separately fixable — don't bundle them into one patch.
- QST-0030.1 likely needs a design decision (how should `@chronicler` dedupe errors that share a root exception identity?) — probably wants a Dialog. QST-0030.2 and QST-0030.3 read as small, mechanical fixes that shouldn't need one.
- `Minion.py` is our own code (not TagKit-upstream) — fix it here directly once approved.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Repair Consul (Cleric): Three symptoms, one visit — good. I'd rather see each wound diagnosed on its own chart than one note that tries to cover all three.
> Flow Consul (Sorcerer): 0030.1 is mine to watch closely — it's a repetition-over-time bug wearing a logging costume.
> Readability Consul (Barbarian): A bug report nobody can read at 2am because the colors are garbled is worse than no color at all. 0030.2 is small; do it soon.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `needs a Dialog` (for 0030.1 only; .2 and .3 read as `build`)
