# QST-0029 — Arcane Trickster: max() crashes when no spell slots are unlocked yet

- **Type:** bug
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** —
- **Parent:** —
- **Sidequests:** —
- **Related:** AtlasLusoris/Grimoire_of_Spellcasters.py (`ArcaneTrickster.available_spells`)

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
- Trivial, mechanical fix (`max(..., default=0)` or an explicit empty check before the `max()` call) — shouldn't need a Dialog, but the second `NameError: 'char'` needs its own trace before closing this one out; don't assume it's fixed by the same one-line change.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
*(not yet convened)*
