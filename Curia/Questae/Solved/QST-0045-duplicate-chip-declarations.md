# QST-0045 — One number, two chips: duplicated rail declarations

- **Type:** bug
- **Priority:** 🟡 normal
- **Status:** Solved (2026-07-31)
- **Owner:** Agent (Julio's report)
- **Route to:** Contracts Consul (Warlock), Readability Consul (Barbarian)
- **Parent:** —
- **Sidequests:** —
- **Related:** `Canon/Single-Source-of-Truth.md` · QST-0013 (modifier not single source)

---

## 🔍 Diagnosis (what & where)

A value that several Trainings all mention was **declared as a chip by each of them**,
so the left rail showed the same label two or three times — and the copies disagreed,
because the later ones hardcoded a tier while the first computed it.

- `Superiority Dice` — declared three times in
  `AtlasLusoris/AtlasOfTraining/Map_of_Fighter_Training.py`:
  `Combat_Superiority` (callable, correct at every rank),
  `Improved_Combat_Superiority` (hardcoded `5d10`),
  `Ultimate_Combat_Superiority` (hardcoded `6d12`).
- `Aura Range (ft)` — declared twice in
  `AtlasLusoris/AtlasOfTraining/Map_of_Paladin_Training.py`
  (`Aura_of_Protection` and `Aura_of_Courage`).

## 🧾 Evidence

Battle Master at level 20 — three chips, two different answers:

```
2nd Wind Uses            = 4
Weapon Masteries         = 6
Superiority Dice         = 6d12
Superiority Dice         = 5d10     <-- stale
Superiority Dice         = 6d12
```

Paladin, caught by the new invariant once it existed:

```
Paladin L10 seed0: duplicate sheet chips ['Aura Range (ft)']
Paladin L20 seed0: duplicate sheet chips ['Aura Range (ft)']
```

Julio reported the Superiority case; the Paladin case was found by adding the guard,
which is the argument for the guard.

## 🎯 Desired outcome

A derived number has exactly one declaration site. Later Trainings still describe their
upgrade in prose; they do not restate the value.

## 🧭 Notes for the Agora / implementer

This is `Single-Source-of-Truth` applied to the sheet: if a value can be computed from
rank, the callable that computes it is its owner, and no other Training may re-declare
the label. The prose is the place to say "your dice become d12s" — the chip is not.

---

## ✅ Resolution (filled when Solved)

- **Decided by:** Julio (reported the defect and asked for a Questa; fix applied because
  the new invariant left the module self-test red, and a permanently-failing gate trains
  people to ignore it).
- **What changed:** `chips=` removed from `Improved_Combat_Superiority`,
  `Ultimate_Combat_Superiority`, and `Aura_of_Courage`. The tier-aware callables on
  `Combat_Superiority` and `Aura_of_Protection` are now the sole owners.
  A duplicate-chip invariant was added to `AtlasInventarium/GearKit._check_character`
  and runs over every guild × level from that module's `__main__`.
- **Practice/preference to remember:** when a defect is reported in one place, add the
  invariant before fixing it — the guard found a second instance in a different Atlas
  that nobody had noticed.
- **Moved to Solved:** 2026-07-31

---

## ⚗️ Reward (separate dialog — do not fill during implementation)

- **Reward file:** *(pending distillation dialog)*
- **Distilled:** *(pending)*

---

## 🏛️ Council

> Contracts Consul (Warlock): Two declarations of one number is not a duplicate, it is a
> contradiction waiting for a level-up. The callable that knows every rank is the owner;
> everything else is prose.
> Readability Consul (Barbarian): The rail is a glance surface. A label appearing twice
> with different values costs the reader more than the feature was worth. No objection.

**Weighting:** reach 1 × severity 2 = **2** · council leaning: `build`
