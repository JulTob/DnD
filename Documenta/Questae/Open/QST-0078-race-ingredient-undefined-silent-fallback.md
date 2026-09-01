# QST-0078 — `Race_Ingredient` is called but never defined; every character gets a fallback name

- **Type:** bug
- **Priority:** 🟠 high (degrades every single generated character's name, silently)
- **Status:** Open
- **Owner:** unclaimed — Codex's lane (`AtlasNomina/Map_of_Names.py` is part of "character generation foundation")
- **Route to:** Codex, or whoever owns `AtlasNomina/Map_of_Names.py` next
- **Parent:** QST-0072 (post-accident recovery)
- **Sidequests:** —
- **Related:** `.claude/worktrees/sweet-mclean-44e50b/AtlasNomina/Map_of_Names.py` (has a working definition, uncommitted, unmerged)

---

## 🔍 Diagnosis (what & where)

`AtlasNomina/Map_of_Names.py` calls `Race_Ingredient` four times from `NewName`.

**Update 2026-08-31 18:15 (Grok):** `def Race_Ingredient` is now on disk at
line 104 of the live file (uncommitted). The questa's original "never
defined" evidence is stale. Leave Open until Julio confirms the ladder
and a seeded summon no longer falls through to LastResort for a named
species. Do not restore this file from vault bytecode over the live body.

Introduced in commit `b4f7ce4` ("Enhance character generation and item
management", 2026-08-29 19:38) — the call sites landed; the function body
didn't.

## 🧾 Evidence

Live reproduction while verifying an unrelated fix (`summon_character(seed=1)`):
```
🐛 Bugs: ... NameError: name 'Race_Ingredient' is not defined
🧚 [changeling] NewName failed; LastResortName takes over.
🧚 [changeling] NewName answered by LastResortName: Lorn Marchwood
```
The comment already sitting above the call sites in `Map_of_Names.py`
describes the intended contract precisely ("Four ingredients, one ladder
each... a missing function and a bug inside a present one are the same
event here") — the design was thought through; only the function itself is
missing from this checkout.

**A working definition already exists**, uncommitted, in the other Claude
instance's worktree: `.claude/worktrees/sweet-mclean-44e50b/AtlasNomina/Map_of_Names.py:122`,
`def Race_Ingredient(race, ingredient, genus)` — a ladder (`[race,
_plantilla()]`) that asks each rung for the ingredient via `getattr`,
demoting on either a missing attribute or a bug inside a present one,
bottoming out at a constant "last-resort roster" rung with no failing path.
Matches the comment's stated contract exactly.

## 🎯 Desired outcome

`Race_Ingredient` exists on this checkout (ported from the worktree, or
independently written to the same contract if porting isn't clean) and
every character's name is drawn from its actual race module again, not the
generic fallback.

## 🧭 Notes for the Agora / implementer

- Not a design question — the contract is already documented in the
  comment and already implemented once. This is a port/merge, not a
  decision.
- **Do not just silence the `NameError`** — the fallback already does that
  gracefully. The actual defect is the missing function, not the missing
  guard.
- Worth a quick check once fixed: how many other calls in this file (or
  elsewhere) reference `Race_Ingredient` and would benefit from the same
  restoration — `grep -c` showed the 4 call sites plus references at lines
  531/547/555/567/568/576 in `Map_of_Names.py`, all downstream of the same
  fix.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
*(not convened — mechanical port, not a design question)*
