# QST-0081 — Restore guilds, species, and backgrounds from vault (TOP)

- **Type:** chore/cleanup
- **Priority:** 🟠 high
- **Status:** Working
- **Owner:** Cursor (Grok)
- **Route to:** Julio · recovery board
- **Parent:** QST-0072
- **Sidequests:** —
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
- **Still open in this lane:** `Build_Guild` is still bytecode inside
  `Grimoire_of_Guilds`; `Load_Guild_Libraries` stays deferred; SpeciesKit
  trait/base/application/kinship/`__main__` shims are still vaulted;
  FighterKit and WarlockKit remain authored rebuilds, untouched.
- **Practice/preference to remember:** Catalogs are Pin Fields (`Available[:]`). Kit = spec; Grimoire = body. Do not `Load_Guild_Libraries` until GuildKit has re-exported the Tags the kits import.
