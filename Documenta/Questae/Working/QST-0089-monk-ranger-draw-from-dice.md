# QST-0089 — Monk and Ranger training Maps call `random` they never imported

- **Type:** bug
- **Priority:** 🔴 urgent *(a selectable Guild crashes for a slice of seeds)*
- **Status:** Working (fix landed; awaiting Julio's closing word)
- **Owner:** Claude (branch `questa/QST-0089-monk-ranger-draw-from-dice`, 2026-09-06)
- **Route to:** Methods (Wizard) · Safety (Paladin) · Contracts (Warlock)
- **Parent:** QST-0016.2 (every Character rolls their own Dice)
- **Sidequests:** —
- **Related:** Decree 0002 §4 · QST-0016.6.1 · QST-0087 · QST-0088

> Minted under `Documenta/` (Julio, 2026-09-06).

---

## 🔍 Diagnosis (what & where)

Two legacy class-progression Maps reach for the global `random` module without importing it, so the line raises `NameError` the moment it runs.

- `AtlasLusoris/Map_of_Classes/Training/Monk.py`: the Elements and Open Hand feature text picks a decorative bullet emoji with `random.choice([...])` inside an f-string. A Monk who reaches level 3 in either Way crashes the whole generation.
- `AtlasLusoris/Map_of_Classes/Training/Ranger.py` line 23: `character.Subclass or random.choice(subclasses["Ranger"])`. Neither `random` nor `subclasses` is defined in the module. The fallback never fired on the Player path because the generator sets `Subclass` at level 1, which is the only reason Ranger stayed green.

Both are also Decree 0002 violations: a Character's draws go through its own Dice, never a process-global generator.

## 🧾 Evidence

- Strict sweep 2026-09-05 and 2026-09-06 (retries off): Monk level 5 seed 2 → `NameError: name 'random' is not defined`.
- `grep -n 'random\.' Training/Monk.py Training/Ranger.py` finds three call sites; `grep -n '^import\|^from'` in both files finds no `random` import.
- With `summon_player` no longer rerolling seeds (QST-0016.6.1), the crash reaches the page instead of hiding behind a different character.

## 🎯 Desired outcome

Every selectable Guild builds for every seed at levels 1 and 5 (78 of 78 in the sweep). The three draws are deterministic per Character: the bullet flair and the archetype fallback replay with the seed.

## 🧭 Notes for the Agora / implementer

- The bullet emoji is Julio's authored whimsy; keep it, make it replay.
- The Ranger fallback should draw from the Guild's real Specialization catalogue (`Specialization_Choices("Ranger")`), not from `Scroll_of_Constants.SUBCLASSES`, whose Ranger list is stale (it lacks Fey Wanderer and lists Horizon Walker).
- These Maps retire guild by guild once `training_covers()` reaches full coverage (TagKit 0.2 plan §5). This questa keeps them honest until then; it does not rewrite them.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** Julio, 2026-09-06 ("land it, fix both right after")
- **What changed:** Monk's two bullet draws and Ranger's archetype fallback go through `character.Pick(..., dice=character.Dice_Bag(purpose, version="2024", namespace=...))`, the same shape SpeciesKit and the Fighter training Map already use. Ranger's fallback draws from `Specialization_Choices("Ranger")`, imported locally to keep the legacy Map free of GuildKit at import time. No `random` remains in either file.
- **Practice/preference to remember:** a draw that only runs for some seeds is a crash that only some players see. The sweep with retries off is the gate that finds it; Dice Bags with a stable purpose string are how a draw stays a function of the seed.

---

## 🏛️ Council

> Methods Consul (Wizard): The bug is a missing import; the disease is a global draw. Fix the disease in the same line, through the Dice, and the import question disappears.
> Safety Consul (Paladin): With the retry gone this NameError is user-visible. It jumps the queue, and its proof is the sweep, not a unit test.
> Contracts Consul (Warlock): The fallback must draw from the catalogue the Guild actually declares, or a Ranger can be handed an archetype no Tag knows.

**Weighting:** reach 2 × severity 3 = **6** · council leaning: `build`
