# QST-0079 — Vault survey: what the 131 `.pyc` files actually hold, and a restoration order

- **Type:** docs / recovery
- **Priority:** 🟡 normal (informs QST-0072's remaining lanes; doesn't block the beta)
- **Status:** Open
- **Owner:** unclaimed — this is a reference for whoever picks up the next flagship, not a claim on any file
- **Route to:** Architecture, Workshop, whoever claims SpeciesKit/GuildKit next
- **Parent:** QST-0072 (post-accident recovery)
- **Sidequests:** —
- **Related:** QST-0076 (the bug-pattern method this reuses) · QST-0077 (the one confirmed instance) · `.recovery-vault/vault-survey-catalog.txt` (the full per-module raw data this Questa summarizes)

---

## 🔍 Diagnosis (what & where)

Nobody had gone through all 131 `.pyc` files in `.recovery-vault` systematically
— claims and restoration so far (BackgroundKit, FighterKit, ClericKit-in-
progress) worked file by file, from the transcript or by hand. This is a
mechanical survey instead: load every compiled module (`marshal.loads`), read
its own docstring (docstrings survive compilation intact — these are the
**original authored text**, not a guess), count its top-level definitions as
a size signal, and re-run the QST-0077 bug-shape heuristic across all of
them. Full per-file output: `.recovery-vault/vault-survey-catalog.txt`.

## 🧾 Evidence and findings

**1. SpeciesKit follows one consistent, repeatable shape across all ten
species** — `__init__` (Atlas declaration) → `base` (shared Shape) →
`traits` (trait Tags) → `resolution` (resolve rules onto the Character
sheet), with heritage/subrace variants as siblings (Elves ×5, Goliaths'
Giant Heritages ×6, Aasimar's Revelations ×3, Tieflings' legacies ×3). This
is good news for restoration: it's a template, not 55 unrelated files —
recovering the pattern once (from the richest example, e.g. Elves or
Goliaths) gives the shape for the rest.

**2. A pre-accident self-test module exists and is itself unrecovered:**
`species/__main__.cpython-314.pyc` — docstring *"Run the SpeciesKit contract
checks beside the package"*, 114 top-level defs. Per this project's own
Code-Style Canon (tests live beside the module, `if __name__ == "__main__"`),
this was SpeciesKit's built-in proof of correctness. Restoring it is worth
prioritizing **alongside** the species files it tests, not after — it's the
verification harness for everything else in this lane, and reconstructing
55 species files blind, without it, is much riskier than reconstructing
them against a real test.

**3. GuildKit's per-class kits are mostly trivial in the pre-accident
bytecode itself** — `ArtificerKit`, `BarbarianKit`, `BardKit`, `ClericKit`,
`DruidKit`, `MonkKit`, `PaladinKit`, `RangerKit`, `RogueKit`, `SorcererKit`,
`WizardKit` all show **0 top-level defs** (just inline class/Specialization
declarations, docstring `"<Class> Specializations."`). Only `FighterKit`
(54 defs, already the one confirmed real rebuild) and `WarlockKit` (2 defs)
carry real weight. This means the other 10 guild kits are a much smaller
lift than SpeciesKit — worth claiming as a fast batch, not feared as
individually as GuildKit's own size (147 defs) suggests.

**4. A real duplication risk, found by cross-checking the vault against the
live import graph, not just the vault alone:** the vault holds **both** a
flat `species/Dragonborn.cpython-314.pyc` (docstring *"The 2024 Dragonborn
Species Shape"*, 2 defs) **and** a full modular package
`species/Dragonborn/{__init__,base,resolution,traits,Map_of_Ancestors}.pyc`
— same for Dwarves. **`AtlasActorLudi/SpeciesKit/__init__.py` currently
imports the flat one** (`from AtlasActorLudi.SpeciesKit.Dragonborn import
Dragonborn`), while the fuller package sits on disk, unwired, next to it.
Every other species in the vault (Elves, Gnomes, Goliaths, Halflings, Orcs,
Tieflings) only exists as the package shape — Dragonborn/Dwarves are the
outliers, almost certainly because the vault caught them mid-migration from
flat file to package, same as every sibling species already finished. This
is exactly the "parallel codebase on top" smell Code-Style Canon warns
against (`Code-Style.md`: *"Refactor the existing filesystem; never build a
parallel codebase on top"*) — not something I'm fixing myself (SpeciesKit is
claimed territory), but worth surfacing before someone restores the flat
file believing it's the only version, or duplicates effort restoring both.

**5. Bug-shape re-scan (QST-0077's method, applied to all 131 files):** only
two files flagged — `epica/Map_of_Stories.pyc` (6 functions; 5 of the 6
verified live and work correctly, only `Name` was actually broken — already
fixed) and `epica/Map_of_Titles.pyc` (`_part`, **not yet live-verified** —
see Notes below). The pattern found in QST-0077 is not systemic; it does not
need a file-by-file dread sweep, just this one remaining check.

**6. Two near-duplicate snapshots of the same file:**
`inventarium/Map_of_Gear_Titles.cpython-314.pyc` (47 defs) and
`inventarium/__pycache__/Map_of_Gear_Titles.py.cpython-314.pyc` (45 defs) —
almost certainly the same module caught at two slightly different moments.
Diff them before restoring either; the smaller one may just be stale.

## 🎯 Desired outcome

Not a restoration itself — a map for whoever does the next lane:
1. `species/__main__` (the self-test) gets restored early, in the same pass
   as whichever species is restored first, so every subsequent species has
   something to verify against.
2. Guild kits other than Fighter/Warlock get claimed as one batch — they're
   small.
3. Before touching Dragonborn or Dwarves specifically: decide (or ask
   Julio) whether the unwired package versions are the intended destination
   and the flat files are meant to retire, per how every other species
   already resolved this exact fork.
4. `Map_of_Titles._part` gets the same live-verification `Map_of_Stories`'s
   five other flagged functions already got, before assuming it needs a fix
   at all.

## 🧭 Notes for the Agora / implementer

- This Questa claims nothing. No file listed here is mine to touch —
  SpeciesKit and GuildKit are already claimed lanes (see `$S/RECOVERY-COORD.md`).
- `Map_of_Titles._part` is the one open thread from this survey with no
  answer yet: I did not live-verify it the way I did `Map_of_Stories`'s five
  functions, and it's not the same file I already have context on. Whoever
  next imports `AtlasEpica.Map_of_Titles`, a one-line check
  (`from AtlasEpica import Map_of_Titles as M; <call _part with real args>`)
  answers it in under a minute — cheap enough to leave as a note rather than
  chase down myself right now.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
*(not convened — a findings survey, not a decision; the Dragonborn/Dwarves
fork in finding 4 may deserve one before it's resolved)*
