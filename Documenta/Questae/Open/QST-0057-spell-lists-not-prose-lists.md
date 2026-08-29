# QST-0057 — Granted spells belong in the Magic section, not in a paragraph

- **Type:** refactor
- **Priority:** 🟠 high
- **Status:** Open
- **Related:** QST-0056 · `AtlasLusoris/Grimoire_of_Spellcasters.py`

---

## 🔍 Diagnosis

Several features list spell **names** in their description. The names alone are
useless at the table: a player still has to look each one up.

- **Great Old One Spells** and the other three patron spell entries print a
  level-gated list of names.
- **Mystic Arcanum** prints its arcana as a **chip**, which reads badly beside
  Known Spells and gives no rules text.
- **Touch of Death** names a spell that is nowhere in the spell ledger.

## 🎯 Desired outcome

**Patron spells:** the feature says only that the patron taught you a set of
spells. The spells themselves appear as full entries in the Magic section, with
their descriptions, like any other prepared spell.

**Mystic Arcanum:** no chip. A structured entry naming the four chosen spells
by arcanum level, with the spells themselves in the Magic section. Julio's
shape:

	# Mystic Arcanum
	## 6th Level Arcanum
	* Tasha's Otherworldly Guise
	## 7th Level Arcanum
	* Plane Shift
	## 8th Level Arcanum
	* Glibness
	## 9th Level Arcanum
	* Astral Projection

	You regain all your Mystic Arcana on a Long Rest.

Note **Arcana** is the plural of arcanum.

## 🧭 Notes

Arcanum selection does not exist yet: nothing chooses a level 6, 7, 8 and 9
Warlock spell. It needs a drawn choice from the Warlock list at each tier,
seeded from a named level-free bag so it holds for the character's life.
