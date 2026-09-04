# QST-0077 — The sheet reads in one decided order

- **Type:** design
- **Priority:** 🟠 high (beta path)
- **Status:** Solved
- **Owner:** Claude
- **Route to:** Venustas
- **Parent:** QST-0073
- **Sidequests:** —
- **Related:** Decree 0006 · QST-0060 · QST-0078

---

## 🔍 Diagnosis (what & where)

Julio fixed the character sheet's reading order (in chat, 2026-08-31):

1. Species: description, then Features
2. Background: description, then Features
3. Class and Subclass up to level: description, then Features
4. Tool proficiencies: description and Works of Wonder (the Practices section)
5. Equipment
6. Backstory
7. Magic / Focus / Special Resource: spell and resource descriptions

The modular renderer (`app/components/character_sheet.py`) already produced
exactly this order with titled blocks. The served beta root (`shiny_app.py`)
did not use it: it carried its own older duplicate with one flat "Features"
heading, so the reader could not tell Species from Background from Class.

## 🧾 Evidence

- `shiny_app.py:404` (before the fix): `prose_section("Features", *feature_items)`.
- `Character.to_dict()` already supplies every key the modular renderer reads
  (verified live: zero missing keys).

## 🎯 Desired outcome

One renderer, the decided order, on the served app.

---

## ✅ Resolution

- **Decided by:** Julio, in chat, 2026-08-31
- **What changed:** `shiny_app.py` now imports `build_character_sheet` from
  `app.components.character_sheet`; its 178-line local duplicate was removed.
  Verified in the browser: titled Species/Background/Class blocks with their
  descriptions and features, then Equipment, Backstory, Spells; Practices
  appear whenever the character has tool proficiencies.
- **Practice/preference to remember:** when the monolith and a module both
  render the same thing, the module is the truth and the monolith borrows it;
  a duplicate renderer is where design decisions go to be silently ignored.

---

## 🏛️ Council

> Venustas Consul (Bard): A sheet is read aloud at the table in exactly this
> order: who you are, where you come from, what you trained as, what your
> hands can do, what you carry, what you lived, and last the fire you bring.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `build`
