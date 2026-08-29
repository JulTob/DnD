# QST-0051 — Species features still speak in the old third-person voice

- **Type:** docs
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Design Team
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0052 · `AtlasActorLudi/SpeciesKit/*/resolution.py`

---

## 🔍 Diagnosis (what & where)

Seven Species resolvers still print rules in a stock third-person past voice
with an invented attribution before the rule arrives:

- `Tieflings/resolution.py` — *"Fiendish legacy granted Darkvision…"*, *"was
  established as its spellcasting ability"*
- `Goliaths/resolution.py` — *"Giant heritage manifested as…"*, *"Giant descent
  granted Powerful Build…"*, *"treats this Character as one size larger"*
- `Elves/`, `Gnomes/`, `Halflings/`, `Orcs/`, `Dwarves/` — the same pattern

Two problems, both visible on one sheet:

1. **The attribution is filler.** The reader is under a heading naming the
   species and a heading naming the feature. *"Fiendish legacy granted…"* is
   six words before the rule starts, repeated on every entry.
2. **The voice does not match anything around it.** Species descriptions are
   second person present (*"You take after your mortal parents"*), Backgrounds
   are second person, and Class features are second person (*"As a Bonus
   Action, unleash the sorcerous power within"*). Only Species features use
   third person past passive.

## 🧾 Evidence

Aasimar and Dragonborn have already been converted and read correctly:

	You have Resistance to Necrotic damage and Radiant damage.
	As a Magic action, you touch a creature and roll 3d4.

The unconverted ones on the same sheet read:

	Fiendish legacy granted Darkvision with a range of 60 feet.
	Otherworldly Presence taught the Thaumaturgy cantrip.
	Intelligence was established as its spellcasting ability.

## 🎯 Desired outcome

Every Species feature reads as the rulebook writes it: second person, present
tense, no invented attribution, numbers resolved where the sheet knows them.
Aasimar (`Aasimar/resolution.py`) is the reference implementation.

## 🧭 Notes for the Agora / implementer

- **Rules as written.** Only deviate where Julio settled a rename (talaria and
  aureola for Aasimar, Talarian Wings for Heavenly Wings).
- **A chip is what you look up mid-combat.** Anything narrative stays prose.
  Darkvision is a record, not a paragraph: a Species Feature with chips and an
  empty description now renders as a chip only (see
  `app/components/character_sheet.py`).
- **Resolve numbers.** Print `3d4`, not "a number of d4s equal to your
  Proficiency Bonus".
- While in each resolver, check the trait actually *grants* what it claims.
  Dwarf and Dragonborn both described Resistances and Darkvision they never
  applied; both are fixed, the rest are unaudited.
