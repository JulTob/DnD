# QST-0100 — Dragon Cult Initiate's second language branch never fires

- **Type:** bug
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Technical Team
- **Related:** `AtlasLusoris/AtlasOfFeatures/Map_of_Official_Origin_Feats.py`

---

## 🔍 Diagnosis (what & where)

Dragon's Tongue promises: *"You know Draconic. If you already know Draconic,
you instead learn one language of your choice."*

`awaken` calls `_grant_language(char, "Draconic")` unconditionally, and
`_grant_language` de-duplicates silently. A Dragonborn, who already knows
Draconic, therefore gains nothing at all from that half of the feat, and the
sheet still promises the substitute language.

## 🧾 Evidence

The de-duplication is correct behaviour on its own; the missing part is the
branch that should notice and grant something else instead.

## 🎯 Desired outcome

1. The feat checks whether the Character already knows Draconic and grants a
   different language when it does.
2. A generated Dragonborn Dragon Cultist shows two languages from this feat's
   promise, not one.
