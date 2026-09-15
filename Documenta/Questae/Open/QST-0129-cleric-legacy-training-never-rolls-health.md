# QST-0129 — The Cleric's legacy training never rolls health past level 1

- **Type:** bug
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Repair (Cleric) · Testing (Rogue)
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0091.2 (one kit declares the class) · `AtlasLusoris/Map_of_Classes/Training/Cleric.py` · `AtlasLusoris/Map_of_Classes/Training/Paladin.py` (the note in its docstring)

---

## 🔍 Diagnosis (what & where)

Health per level is rolled by the legacy 2014 training modules, not by the
2024 training maps. `Training/Fighter.py` calls `roll_health` at every level
and `Training/Paladin.py` keeps it as a named step, because removing it was
measured to cost a level-20 Paladin 96 Hit Points. `Training/Cleric.py` (72
lines) never calls it. A Cleric gains only its Constitution bonus after level
1.

## 🧾 Evidence

Seed 1, same session, same tree:

| Guild | Level | Health | Constitution |
|---|---|---|---|
| Cleric | 1 | 8 | 10 |
| Cleric | 20 | 48 | 14 |
| Paladin | 20 | 157 | 14 |
| Fighter | 20 | 217 | 20 |

48 is 8 plus 2 × 20: the level-1 die, then only the modifier, twenty times.
No die is rolled after level 1.

## 🎯 Desired outcome

A Cleric's Health grows by its hit die each level like every other Guild, on
the same seed. A check in the sweep flags any Guild whose level-20 Health is
below what one hit point per die would give, so the next silent loss is caught.

## 🧭 Notes for the Agora / implementer

The right home for the roll is the level-up step of the Guild kit
(QST-0091.2). Until that lands, add the named step to `Training/Cleric.py` the
way `Training/Paladin.py` does, and measure before and after on a fixed seed.
Walk every other legacy module for the same gap while there. No decision
needed.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Repair Consul (Cleric): The table is the diagnosis. Eight plus forty, and not one die. Restore the step, then measure the same seed again.
> Testing Consul (Rogue): A floor check per Guild costs one line in the sweep and would have caught this a year ago.

**Weighting:** reach 2 × severity 3 = **6** · council leaning: `build`
