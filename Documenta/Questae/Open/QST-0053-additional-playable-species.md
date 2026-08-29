# QST-0053 — Additional playable Species

- **Type:** design
- **Priority:** 🟢 low
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Design Team
- **Related:** QST-0051 · `AtlasLusoris/Map_of_Species.py` (retired catalogue)

---

## 🔍 Diagnosis (what & where)

Ten Species are playable and all ten now carry written descriptions, heritage
prose, kinship Tags and 2024-current rules. `Map_of_Species.py` still holds a
commented-out catalogue of roughly forty more (Goblin, Kobold, Lizardfolk,
Tabaxi, Genasi, Warforged, Changeling, Firbolg, Dhampir, Hexblood, Reborn,
Satyr, Minotaur, Shifter, Aarakocra, Owlin, Tortle, Triton, and others).

The setting brief in `Documenta/Canon/Cultural-Inspirations.md` already assigns
inspirations to several that do not exist yet: **Kobold** (Korea, a step aside
from the Dragonborn) and **Goblin** (ancient Indo-Israeli-Persian, marginalised
without a single real-world parallel).

## 🎯 Desired outcome

New Species added the way the current ten were finished: a Kit with real Tags
that *grant* rather than merely describe, a resolver in second person, kinship
Tags where the people resembles something, and a written description agreed
with Julio before it goes in.

## 🧭 Notes for the Agora / implementer

- **Do not bulk-add.** Each Species is a design conversation. The ten took a
  long collaboration each, and the value was in the collaboration.
- **Kinship first.** Dhampir is `Undead`, Genasi `Elemental`, Kobold `Dragon`,
  Fairy `Fae`. `AtlasActorLudi/SpeciesKit/kinship.py` already holds the
  vocabulary.
- **The metaphysics table** in `Documenta/Canon/Dragons-and-the-Overcoming.md`
  lists one organising principle per people. A new Species should either take
  an existing one or bring its own; it should not be metaphysically silent.
- Several of the retired names are Heritages rather than Species: Deep Gnome
  and Duergar belong under Gnome and Dwarf, Eladrin and Sea Elf and Shadar-Kai
  under Elf.
