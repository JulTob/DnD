# QST-0097 — Magic Initiate grants nothing, in all three versions

- **Type:** bug
- **Priority:** 🔴 urgent *(an Origin feat on the live draw grants no mechanics)*
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Technical Team · Lorekeeper
- **Related:** QST-0068 · QST-0069 · QST-0026.1 · `AtlasLusoris/FeaturesKit.py`

---

## 🔍 Diagnosis (what & where)

Magic Initiate (Cleric), (Druid) and (Wizard) are three of the twelve base
Origin feats, and all three carry prose only. Applying one leaves the Character
with no spellcaster, no `spells_known` and no tracked use. No cantrips, no
level-1 spell, no recharge.

Two published clauses are also missing from the text itself:

- *"You can also cast the spell using any spell slots you have."*
- The Spellcasting Ability clause, which lets the player choose Intelligence,
  Wisdom or Charisma for these spells.

The legacy twin in `Grimoire_of_Features` did more: it picked the spells,
printed them, and named the spellcasting ability. The live Tag is a regression
against the code it replaced.

## 🧾 Evidence

- Verified by applying each of the three to a fresh Character: no spellcaster,
  no spells, no uses.
- Three of the sixteen official backgrounds hand out a Magic Initiate as their
  Origin feat, so this reaches ordinary sheets.

## 🎯 Desired outcome

1. Each version grants its two cantrips and its level-1 spell, with the free
   cast per Long Rest tracked.
2. The spellcasting ability is resolved and printed, not left as a choice.
3. The two missing clauses are restored to the description.
4. The spells print in the Magic section (QST-0069).
