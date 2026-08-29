# QST-0029 — Arcane Trickster: max() crashes when no spell slots are unlocked yet

- **Type:** bug
- **Priority:** 🟡 normal
- **Status:** Open — Agora converged, awaiting Julio (Dialog 0008)
- **Owner:** unclaimed
- **Route to:** Repair Consul (Cleric), Methods Consul (Wizard), Safety Consul (Paladin), Testing Consul (Rogue)
- **Parent:** —
- **Sidequests:** *(thrown if NameError still traces after the slot guard)* QST-0029.1
- **Related:** Dialog `0008-arcane-trickster-empty-slots.md` · Q-0011 · AtlasLusoris/Grimoire_of_Spellcasters.py (`ArcaneTrickster.available_spells`)

---

## 🔍 Diagnosis (what & where)
`ArcaneTrickster.available_spells` (`Grimoire_of_Spellcasters.py:1586`):
```python
max_slot = max(i+1 for i, n in enumerate(trickster.get_stats("slots").values()) if n > 0)
```
`max()` on a generator with no `default=` — if the character hasn't unlocked any Arcane Trickster spell slots yet (low level, before the subclass grants its first slot), every `n` is 0, the filtered generator is empty, and `max()` raises `ValueError: max() iterable argument is empty`. `summon_character`'s 5-attempt retry doesn't save it, because the failure is deterministic for that race/class/level/background combination — a fresh seed still rolls the same doomed shape.

## 🧾 Evidence
Surfaced incidentally during a 100-seed sweep verifying an unrelated change (spell-title fonts, 2026-07-11): seed 81 exhausted all 5 retries. Minion bug tree:
```
Grimoire_of_Characters.py:210 get_spellcaster
  Grimoire_of_Spellcasters.py:654 Spellcaster.__init__ (base __init__, called via the trickster path)
    Grimoire_of_Spellcasters.py:1586 available_spells
Bug: ValueError - max() iterable argument is empty
```
A second, likely related bug tree in the same failing seed: `NameError: name 'char' is not defined` directly inside `Grimoire_of_Characters.py.__init__` — not yet isolated to a line; may be a second, separate defect in the same code path and worth checking alongside this one rather than assuming it's the same root cause.

## 🎯 Desired outcome
An Arcane Trickster with zero unlocked spell slots gets an empty spell list (or is simply not offered spells yet), not a crash. `available_spells` returns `[]` when no slot is > 0, same contract as the early `if not source: return []` two lines above it.

## 🧭 Notes for the Agora / implementer
- Dialog 0008 is open and converged. Do **not** implement until Julio decrees.
- The questa's original sketch listed `max(..., default=0)` as a candidate. The council's objection: SPELL_LISTS key `0` is the cantrip list, so that one-liner would leak cantrips at levels 1–2. Leading recommendation is an explicit empty-slot guard that returns `[]`.
- The second `NameError: 'char'` stays isolated; throw QST-0029.1 only if it still traces after the slot guard.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
See Dialog 0008. Seats called: Cleric, Wizard, Paladin, Rogue. Converged on an empty-slot guard (`return []`); rejected `max(..., default=0)` because SPELL_LISTS key `0` would leak cantrips at levels 1–2. Awaiting Julio.

**Weighting:** reach 2 × severity 3 = **6** · council leaning: `needs a Dialog` → Dialog opened, `build` after Decree
