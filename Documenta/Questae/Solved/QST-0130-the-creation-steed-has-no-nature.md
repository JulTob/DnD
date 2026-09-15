# QST-0130 — The Oath of Creation's drawn steed has no nature

- **Type:** design
- **Priority:** 🟢 low
- **Status:** Solved
- **Owner:** Claude
- **Route to:** Julio · Lorekeeper (Elf Sage) · Venustas (Bard)
- **Parent:** —
- **Sidequests:** —
- **Related:** PR #7 · `AtlasLusoris/AtlasOfTraining/Map_of_Paladin_Steeds.py`

---

## 🔍 Diagnosis (what & where)

Find Steed offers three natures, Celestial, Fey and Fiend. The generator draws
one per Character from the Oath: `OATH_NATURE` keys Devotion and Glory to
Celestial, Ancients to Fey, Vengeance to Fiendish. Creation, the fifth Oath,
is not keyed, so its steed is drawn evenly across the three. Nothing decided
that; the Oath arrived after the map.

## 🧾 Evidence

`OATH_NATURE` in `Map_of_Paladin_Steeds.py` has four keys. A level-5 Creation
Paladin on different seeds draws all three natures.

## 🎯 Desired outcome

A ruling, recorded and implemented: Creation keyed to one nature, or the even
draw kept on purpose with the steed's description reading as a made thing
rather than a summoned court's.

## 🧭 Notes for the Agora / implementer

Rules-bound: the three natures are the rules' and there is no fourth. The
maker's fantasy argues both ways: Fey for the wild elements, or no single
court because the maker answers to none. Julio's call; a Dialog only if he
wants one.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** Julio, in chat, 2026-09-15: "a demiurge would have a celestial steed if I had to choose, but we could change it to an elemental. It's our reflavour's kind anyway. We can personalize those things better than a printed book."
- **What changed:** `Map_of_Paladin_Steeds.py` gains a fourth kind, Elemental, keyed to Creation in `OATH_NATURE` at the same affinity weight as the other three pairings, with four forms, one per element (stone, wind, quiet flame, river water). The kind draw runs over four kinds; its Dice Bag is at version 2 because the candidate list changed. The module docstring records the ruling; the lesson comment in `Map_of_Paladin_Training.py` names the fourth kind as ours. Commit on PR #7.
- **Practice/preference to remember:** where the Oath is ours, its answer may be ours too. The book's list is a floor for a printed sheet, not a ceiling for a generated one; when the reflavour adds a kind, the module says so in its own voice and the sheet prints it without apology.

---

## 🏛️ Council

> Lorekeeper (Elf Sage): Three natures, by the book. The choice is which, or none by design.
> Venustas (Bard): If the draw stays even, the steed text must say why. An accident reads as one.

**Weighting:** reach 1 × severity 1 = **1** · council leaning: `defer` (to Julio)
