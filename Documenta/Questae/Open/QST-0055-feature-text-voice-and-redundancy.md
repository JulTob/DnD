# QST-0055 — Feature text: passive voice, silent levels, no restating the rule

- **Type:** docs
- **Priority:** 🟠 high
- **Status:** Open
- **Related:** QST-0051 (Species voice sweep) · QST-0054

---

## 🔍 Diagnosis

Three related problems in how features print, all confirmed at the table.

**1. Present tense reads as an instruction.** New players read *"You choose one
Warlock spell"* and try to choose, now, at the table, in the wrong situations.
The sheet is a **record of a character already built**, not a rulebook. It
should say what happened: **"You learned"**, **"You gained access to"**, **"Your
Constitution was increased by 1."**

**2. Features announce their own level.** *"Gained at Level 5."* draws attention
to bookkeeping. A feature should simply appear on the sheet once earned.
Draconic Flight is **fixed**; Aasimar's Celestial Revelation and every
`Gained at Level N` in the Training maps are not.

**3. The generic rule is restated after the specific result.** Ability Score
Improvement prints the effect *and then* the whole rule:

	Your Constitution was increased by 1. Your Wisdom was increased by 1.
	Increase one ability score of your choice by 2, or increase two ability
	scores by 1. You can't increase a score above 20 this way. Repeatable.

The second half is dead text once the first half exists.

## 🎯 Desired outcome

Every feature entry: passive or past voice, no level announcement, no
restatement of a rule the sheet has already resolved. Numbers resolved.

## 🧭 Notes

`Aasimar/resolution.py` and `Dragonborn/resolution.py` are the closest
references but are still present tense; they solved attribution and filler, not
voice. Julio's rule: **"Mechanics should be hidden in narratives, but clear and
accessible as rules."**

Specific known offenders: Mystic Arcanum (*"You choose one Warlock spell"*),
Lessons of the First Ones, Ability Score Improvement, every
`Gained at Level N`.
