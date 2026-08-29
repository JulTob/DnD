# Quest: Superiority Dice chip is declared three times

**Status:** ✅ RESOLVED 2026-07-31 · **Scope:** Fighter + Paladin Training maps
**Found:** 2026-07-31, reported by the author, reproduced on a generated Battle Master.

---

## Symptom

A Battle Master's left rail shows **three** "Superiority Dice" chips, and they disagree:

```
Battle Master L20 chips:
   2nd Wind Uses            = 4
   Weapon Masteries         = 6
   Superiority Dice         = 6d12
   Superiority Dice         = 5d10     <-- stale
   Superiority Dice         = 6d12
```

Reproduce:

```bash
.venv/bin/python3 -c "
from AtlasActorLudi.Map_of_Character_Generation import summon_player
c = summon_player(guild='Fighter', level=20, seed=13)
print([ch for f in c.features for ch in getattr(f,'chips',())])
" 2>/dev/null
```

## Cause

The same chip label is emitted by three separate Trainings, each of which
independently restates the die size:

| Training | line | chip value |
|---|---|---|
| `Combat_Superiority` | [Map_of_Fighter_Training.py:386](../AtlasLusoris/AtlasOfTraining/Map_of_Fighter_Training.py:386) | callable → `4d8` / `5d10` / `6d12` by rank |
| `Improved_Combat_Superiority` | [:423](../AtlasLusoris/AtlasOfTraining/Map_of_Fighter_Training.py:423) | hardcoded `5d10` |
| `Ultimate_Combat_Superiority` | [:444](../AtlasLusoris/AtlasOfTraining/Map_of_Fighter_Training.py:444) | hardcoded `6d12` |

A level-18+ Battle Master has all three Trainings awake, so all three chips reach the
rail. The middle one is not merely duplicated but **wrong** at that level — it says
`5d10` when the character is on `6d12`.

`Combat_Superiority`'s callable already covers every tier on its own, so the other two
chips are pure redundancy.

## Fix

Drop the `chips=` from `Improved_Combat_Superiority` and `Ultimate_Combat_Superiority`
and let `Combat_Superiority`'s callable be the single owner of the number. Their prose
Entries still describe the upgrade, which is the part that belongs on the sheet.

This is the project's **one fact, one owner** rule: a value that can be derived should
have exactly one declaration site.

## A second instance, found by the new gate

Adding the duplicate-chip invariant to `scripts/verify_equipment.py` immediately caught
the same bug elsewhere, exactly as predicted:

```
Paladin L10 seed0: duplicate sheet chips ['Aura Range (ft)']
Paladin L20 seed0: duplicate sheet chips ['Aura Range (ft)']
```

`Aura Range (ft)` is declared twice in
[Map_of_Paladin_Training.py:329](../AtlasLusoris/AtlasOfTraining/Map_of_Paladin_Training.py:329)
and [:353](../AtlasLusoris/AtlasOfTraining/Map_of_Paladin_Training.py:353) — the
`Aura of Protection` and `Aura of Courage`/`Aura Expansion` Trainings each restate the
range. Same fix: one owner for the number.

## Resolution

Redundant chip declarations removed; the tier-aware callable on the first Training is
now the single owner of each number:

- `Improved_Combat_Superiority` and `Ultimate_Combat_Superiority` — `chips=` dropped
  (`Combat_Superiority`'s callable already returns 4d8 / 5d10 / 6d12 by rank).
- `Aura_of_Courage` — `chips=` dropped (`Aura_of_Protection` owns Aura Range).

The prose Entries still describe each upgrade; only the duplicated NUMBER was removed.

A **duplicate-chip invariant** now guards every guild and level, living in
`AtlasInventarium/GearKit._check_character` and running from that module's `__main__`
(the project keeps its tests in module mains, not a separate `scripts/` tree).

## Acceptance

- No duplicate chip labels on any generated character, at any level, for any guild.
- A Battle Master's Superiority Dice chip reads `4d8` (L3-9), `5d10` (L10-17),
  `6d12` (L18+).
- Add a duplicate-label invariant to `scripts/verify_equipment.py` (or a sibling
  training gate) so this class of bug is caught for every guild, not just this one —
  the same triple-declaration could exist elsewhere and is currently unguarded.
