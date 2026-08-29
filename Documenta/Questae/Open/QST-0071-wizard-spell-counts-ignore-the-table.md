# QST-0071 — Wizard spell counts ignore the Wizard table

- **Type:** bug
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Consul-Wizard, Consul-Artificer
- **Related:** QST-0070

---

## 🔍 Diagnosis (what & where)

`Wizard.prepare_spells` in `AtlasLusoris/Grimoire_of_Spellcasters.py:995` sets the
number of spells from a hand-rolled formula:

```python
num_spells = caster.level * 2 + 4
```

The correct numbers are already in the same class, in the `table` dict a few
lines above, and that table is right: verified against the 2024 PHB at **20/20
rows** for cantrips, prepared spells and slots at every level.

Two consequences.

1. **The count is wrong at every level.** The formula gives a single total where
   the rules give two separate quotas.
2. **Cantrips and levelled spells are drawn from one mixed pool**, so the split
   between them is whatever the dice happen to produce. A level 6 Wizard was
   observed with **one** cantrip; a level 20 Wizard with eight.

`__str__` then does `prepared = other_spells[:n]` with `n` from the correct
table, so the rendered sheet is truncated to a plausible length while
`spells_known` underneath holds the wrong set. The defect is therefore invisible
on the page and visible only to anything reading the data.

## 🧾 Evidence

Generated Wizards, seed 13, against the PHB table:

```
 lvl  cantrips  want  prepared  want
   1         2     3         4     4   MISMATCH
   3         3     3         7     6   MISMATCH
   6         1     4        15    10   MISMATCH
  10         2     5        22    15   MISMATCH
  14         3     5        29    18   MISMATCH
  20         8     5        36    25   MISMATCH
 === 0/6 levels match ===
```

Every observed total equals `level * 2 + 4`, which confirms the formula rather
than the table is in control.

For contrast, the Eldritch Knight's third-caster progression **does** go through
its declared table and verifies at 6/6 levels on generated characters, so the
pattern for doing this correctly already exists in the codebase.

## 🎯 Desired outcome

A generated Wizard holds exactly the cantrips and prepared spells its own table
says it holds, drawn as two separate quotas, at every level from 1 to 20.

Whatever the fix, the check should be a test over generated characters rather
than over the table, since the table was already correct while every character
was wrong.

## 🧭 Notes for the Agora / implementer

- Do not fix the display. `other_spells[:n]` is a symptom; truncating output to
  hide a bad model is what made this invisible.
- Check the other casters in the same file before assuming this is Wizard-only:
  the same `prepare_spells` shape appears at lines 869, 1128 and 2143.
- This blocks the Spellbook entry rewrite requested on 2026-08-28, which drops
  the selection rules from the page on the grounds that **the generator chooses
  the spells and the sheet lists them**. That is only honest once the generator
  chooses the right number.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Moved to Solved:** —

---

## 🏛️ Council
*Pending.*
