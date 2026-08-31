# QST-0078 — Non-casters show an empty Spells section and casting chips

- **Type:** design / bug
- **Priority:** 🟡 normal (beta polish)
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Venustas, Architecture
- **Parent:** QST-0073
- **Sidequests:** —
- **Related:** QST-0077 · QST-0057 · QST-0069

---

## 🔍 Diagnosis (what & where)

A generated level 1 Monk (Orc Exorcist, no spellcasting) rendered:

- a "Spells" section containing only an em-dash placeholder;
- rail chips for "Spellcasting Ability: Wisdom" and "Spell Save DC: 13".

`_prose_sections` appends the Spells section whenever `data["Spellcaster"]`
is not None, and the chip builder reads the same object. Some non-casting
builds apparently carry a non-None Spellcaster with an empty book.

Julio's sheet order (QST-0077) names slot 7 "Magic / Focus / Special
Resource: spell and resource descriptions". An empty placeholder satisfies
none of those readings.

## 🧾 Evidence

Browser render of `seed` page, 2026-08-31: Spells section shows "—" for the
Monk above; chips visible in the rail.

## 🎯 Desired outcome

A decision, then one behavior: either the section and chips vanish when the
character has no spells and no special resource to describe, or the section
becomes the home of the class resource (Ki, Rage, Focus) whenever one exists.
The second reading matches Julio's slot 7 wording and deserves the Dialog.

## 🧭 Notes for the Agora / implementer

Find where a non-caster acquires a non-None Spellcaster first: hiding the
section may be masking a production bug rather than a presentation choice.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Venustas Consul (Bard): An empty section is a promise the sheet breaks at
> the last line. Either keep the promise with the character's true fire
> (their Focus, their Discipline), or do not make it.

**Weighting:** reach 2 × severity 1 = **2** · council leaning: `needs a Dialog`
