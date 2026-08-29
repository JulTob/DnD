# QST-0058 — Apply @guardian at the generation seams so a failed draw recovers

- **Type:** design
- **Priority:** 🔴 urgent
- **Status:** Open
- **Route to:** Technical Team
- **Related:** `Minion.py` · `AtlasLusoris/InvocationKit.py`

---

## 🔍 Diagnosis

Generation can fail to the user with a bare precondition error. Observed:

	Character generation failed
	Precondition 'Ability_Met' failed
	localhost:8000/#/2/Dragonborn/Farmer/Warlock/Great_Old_One/She/16846665795940946129

The immediate cause is fixed: `invocation_eligible` now reads the same ability
table the `@Pre` enforces, so the selector no longer offers what the
precondition will refuse. But the **shape** of the failure is the real problem.
A precondition is a backstop against programmer error. When one fires, the
generator should recover, not hand the error to a player.

## 🧾 Evidence

**The machinery already exists.** `Minion.py` provides exactly this as a
decorator, and nothing needs building:

- `@minion` — report the bug tree, re-raise
- `@warden` — report the bug tree, retry **once**, return that
- `@guardian` — report the bug tree, retry until success or 100 attempts

`@guardian` is the pattern Julio described. And it works on a *draw* precisely
because `char.Pick` consumes from the dice bag: the retry is not the same roll
again, it is the next one. So a failed draw reports where it failed and then
recovers with a different element, which is the whole requirement.

## 🎯 Desired outcome

Every place the generator **draws from a pool** carries `@guardian`, so a bad
draw produces a located bug report in the log and a valid character on the
screen. The player never sees a precondition.

Seams to cover: invocation selection, species heritage selection, patron
feature application, background selection, gear outfitting, familiar drawing.

## 🧭 Notes

- **Do not weaken preconditions.** The Pre is what makes recovery possible: it
  is the signal that a draw was invalid. Catch it, never remove it.
- `@guardian`'s 100-attempt ceiling then raises, which is correct: an
  exhausted pool is a real bug and should surface in development.
- Prefer `@guardian` on the **draw**, not on the whole of `New_Player`.
  Retrying the entire character would re-roll everything and lose the seed's
  meaning; retrying one draw keeps the rest of the character intact.
- `bugged_tree` and `get_call_tree` are what produce the locator, and
  `set_log_file` decides where it lands.
