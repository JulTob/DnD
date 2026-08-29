# QST-0069 — Feat-granted spells print inside the feature, not in the magic section

- **Type:** design / presentation
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Julio (decision), then Technical Team
- **Related:** QST-0067 · `AtlasLusoris/AtlasOfFeatures/Map_of_Official_Origin_Feats.py`

---

## 🔍 Diagnosis (what & where)

Several Origin Feats embed a whole spell card inside their own Entry:

	f'<div class="spell">{SpeakwithAnimals}</div>'

Wildwarden does it with Speak with Animals; the same shape appears for Sacred
Flame, Augury, Message, Faerie Fire, Hex, Mage Hand, Chill Touch and Alter
Self. The spell therefore appears **in the Features list** rather than with the
Character's other magic, so a reader looking at the spellcasting section does
not see a spell the Character genuinely has.

Julio, 2026-08-24:

> Speak with animals is with the features, not at the end in the magic section.

## 🧾 Evidence

	localhost:8000/#/20/Goliath/Wildkeeper/Barbarian/World_Tree/He/2504349135602673103

Wildwarden's Entry carries the full card. The Character has no spellcasting
section entry for it. A Barbarian with a granted ritual is a real case, not an
edge one: the Wildkeeper background hands Wildwarden to anybody.

Note the same embedding was the vector for two rendering faults already fixed
in `AtlasMagia/SpellsKit.py` (an escaped `<br>` and an unclosed `<i>` that bled
italics into every later feature), and is the vector for the unresolved
`{dice}` placeholder tracked separately.

## 🎯 Desired outcome

A spell a Character actually has appears where a reader looks for spells.

## 🧭 Notes for the Agora / implementer

**This needs a decision before it needs code.** Two shapes, and they are not
equivalent:

1. **Register it as a spell.** The feat records the spell and its casting
   ability on the Character, and the magic section renders it beside the rest,
   flagged with its source. The Feature entry keeps the rule and drops the
   card. Most correct for a reader; requires the magic section to accept spells
   that come from no class and use their own ability.
2. **Leave it in the feature, drop the card.** The Entry names the spell and
   states the rule; no card anywhere. Cheapest, and it keeps the magic section
   purely about class spellcasting, but the spell is then only findable by
   reading every feature.

Related constraint from QST-0068: these feats choose the casting ability at a
moment when the scores do not exist yet. If option 1 is taken, the ability must
be **recorded**, not merely printed, so the magic section can read it. That
makes QST-0068 a prerequisite rather than a neighbour.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Moved to Solved:** —

---

## ⚗️ Reward (separate dialog — do not fill during implementation)

- **Reward file:** *(pending distillation dialog)*
- **Distilled:** *(pending)*

---

## 🏛️ Council
*(unheard — needs Julio's decision on shape before a seat can weigh in)*

**Weighting:** reach ⟨2⟩ × severity ⟨2⟩ = **4** · council leaning: `needs a Dialog`
