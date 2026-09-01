# QST-0081 — Restore guilds, species, and backgrounds from vault (TOP)

- **Type:** chore/cleanup
- **Priority:** 🟠 high
- **Status:** Working
- **Owner:** Cursor (Grok)
- **Route to:** Julio · recovery board
- **Parent:** QST-0072
- **Sidequests:** QST-0081.1 · QST-0081.2 · QST-0081.3 · QST-0081.4 · QST-0081.5 · QST-0081.6 · QST-0081.7 · QST-0081.8 · QST-0081.9
- **Related:** QST-0079 · QST-0036 · Dialog 0009 · TagKit Doctrine · Pin Guide

---

## 🔍 Diagnosis (what & where)

The 2026-08-29 wipe left Guild, Species, and some Background surfaces as vault `.pyc` loaders. Runtime works; the editable TOP source does not. Catalogs were rebuilt as parallel lists in some recovery drafts; the pin Guide says catalogs are Pin Fields (`Available[:]`, `Declared_Species[:]`).

## 🧾 Evidence

- Live `GuildKit.py` / most `AtlasOfGuilds/*Kit.py` / `SpeciesKit/{bases,catalog,physiology}.py` / species package `__init__.py` are `exec(marshal)` shims.
- `Playable_Species` disassembles to `tuple(Available[:])`.
- Flat `SpeciesKit/Dragonborn.py` and `Dwarves.py` are dead shims beside wired packages.
- `Declared_Species.DESCRIPTION` is tripled in source.
- Arcana Unleashed map is missing; two small prewipe pycs carry one Background (`Agent of the Ninth Quill`).

## 🎯 Desired outcome

Guilds, species Pins/catalog/physiology, and the missing Background map exist as readable source. Character remains the Target; Species/Guild/Heritage are Tags; catalogs read Pin Fields. FighterKit, WarlockKit, live BackgroundKit, and Map_of_Gear_Titles stay untouched. `Build_Guild` may remain bytecode in `Grimoire_of_Guilds` until it is rewritten.

## 🧭 Notes for the Agora / implementer

- TagKit pin `@c7bd376`: membership is `agent in Tag`, not `__contains__` overrides (QST-0051).
- Doctrine names Expectation/Exclusion/Augmentation do not match this pin (QST-0036); use `Pre`, `Record`, `Imprint`, `Pin` Fields.
- Vault `BackgroundKit.pyc` predates the Crafter/Musician fix — comparison copy only.
- Arcana pyc used `tool=`; live `Background` takes `tools=`.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** — (still Working; Julio released the commit gate on
  2026-08-31, but source restore is not finished)
- **Committed so far:** Julio lifted recovery rule 4 ("do not commit until
  Julio says so") at 08:24 on 2026-08-31. This lane's work is now in
  history rather than on disk only:
  - `4e2ad9a` — Guild spec/body split (`GuildKit` re-exports,
    `Grimoire_of_Guilds` holds the body) plus eleven specialization kits as
    `Build_Specialization` source; Arcana Unleashed map, unenrolled.
  - `27f4223` — Species Pins, `bases`, `catalog`, `physiology`, Elf line
    with Drow aliasing Dark_Elf; flat `Dragonborn.py` / `Dwarves.py`
    deleted; two duplicate `DESCRIPTION` declarations dropped.
  - Verified before committing: `import shiny_app`, `summon_player(seed=42,
    level=1)` → Nikolas Amexafa, and a Cleric summon for the voice path.
- **What changed so far:** Guild Ada spec/body; specialization kits as source; Species `bases`/`catalog`/`physiology` rewritten so catalogs are Pin Fields; species package Pins; Elf heritages; Drow alias; dead flat Dragonborn/Dwarves removed; Arcana Unleashed map recovered but not enrolled (missing Origin Feat).
- **Still open in this lane:** `Load_Guild_Libraries` stays deferred
  until Julio reviews; `app.main` NPC path still hits QST-0081.5
  (SavingThrows / Char_Skills arity). `Build_Guild` and
  `SpeciesKit/__main__.py` are source as of 2026-08-31 16:50–18:15.
  FighterKit and WarlockKit remain authored rebuilds, untouched.
  Later-session restores (not this file's original claim): InvocationKit,
  Map_of_General_Feats, Map_of_Epic_Boons, legacy Training/Artificer.py
  — see QST-0082. Conflict sidequests unchanged: QST-0081.1–.9.
  ActorLudi Alusoris contracts are source: FeaturesKit, Lodge, feature
  selection, RaceKit, Map_of_NPC, Archetypes, Projections, Generation,
  Map_of_Races, Grimoire_of_NPC. Do not overwrite live `AtlasAlusoris/`.
- **SpeciesKit bodies restored 2026-08-31 (this slice, uncommitted):**
  kinship, application, NonPlayer, kit-level resolution; Aasimar base/
  traits/Revelations; Gnome base/traits/Forest/Rock; Halfling base/traits/
  resolution; Orc base/traits/resolution; Tiefling base/Abyssal/Chthonic/
  Infernal; Goliath base/traits/Giant Heritages. `Resolve_Feature_Mechanics`
  is imported from live FeaturesKit, not duplicated. Duplicate
  `Grant_Resistance` import in Tiefling traits dropped (same name twice,
  not a design fork).
- **Training maps + AlignmentKit restored 2026-08-31 (uncommitted):**
  `Map_of_{Artificer,Bard,Monk,Sorcerer,Warlock,Wizard}_Training.py` from
  vault Tags; `AlignmentKit.py` as readable two-axis Geometry. TrainingKit
  self-test green. Artificer summon still hits QST-0050.2.
- **Chip rail + Alusoris contracts restored 2026-08-31 (uncommitted):**
  Six restored training maps declare `Chip(...)`. `FeaturesKit.Feature.chips`
  accepts Chip and still returns tuples when stored as tuples (QST-0081.4).
  Sheet normalizers accept Chip and NPC `Chip_Grant.icon`. Alusoris
  `FeaturesKit.py`, `Lodge_of_NonPlayer_Features.py` (17 `Feature_Spec`,
  was a garbled const dump), `Map_of_NonPlayer_Features.py`, `RaceKit.py`,
  and `Map_of_NPC.py` are source again. NPC catalogue chips stay
  `Chip_Spec` (template + icon), not Venustas Chip.
- **Map_of_Races + Grimoire_of_NPC restored 2026-08-31 (uncommitted):**
  ActorLudi `Map_of_Races` pickers take a Character and use `Pick`;
  catalogues match live `AtlasAlusoris` tables; `Creature_Type_For_Race`
  from vault. `Grimoire_of_NPC` is the Character awakener (`NPC` function
  + `NonPlayer` Tag), not the live class. `summon_nonplayer` still dies
  on QST-0050.4 (`AbilityScores(..., character=)`). Player path still
  Nikolas Amexafa.
- **Practice/preference to remember:** Catalogs are Pin Fields (`Available[:]`). Kit = spec; Grimoire = body. Do not `Load_Guild_Libraries` until GuildKit has re-exported the Tags the kits import.
