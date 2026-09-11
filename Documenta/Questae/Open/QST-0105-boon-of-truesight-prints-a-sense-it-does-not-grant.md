# QST-0105 — Boon of Truesight prints a sense it does not grant

- **Type:** bug
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Technical Team
- **Related:** QST-0102 · `AtlasLusoris/Grimoire_of_Features/__init__.py`

---

## 🔍 Diagnosis (what & where)

Boon of Truesight is the only boon whose working code was written and then
disabled. The line that would set the sense is commented out, so `_apply` raises
an ability score and returns. The sheet states Truesight 60 feet and the
Character object does not carry it.

## 🎯 Desired outcome

1. Either the sense is granted, or the text stops promising it.
2. A level-19 Character with this boon shows Truesight in its senses record, not
   only in the boon's prose.
3. Check the sibling boons for the same shape: Boon of Energy Resistance has a
   bare comment where its storage should be.
