# GenLegend — Status, Cleanup & TOP Integration Plan

*Top-down assessment. Priority: make it work first, then cut dead weight, then integrate Tag-Oriented Programming.*

---

## 1. Where it actually stands (the "halfway to Shiny" question)

The Shiny migration is **further than halfway — but none of it is committed.**

- The working tree already holds the new structure: `shiny_app.py` (the Shiny app) plus the Latin **Atlas\*** packages (ActorLudi, Alusoris, Inventarium, Ludus, Lusoris, Magia, Nomina, Pugna, Scriptum, WorldBuild).
- Git, however, still tracks the **old** flat Flask/R version. `git status` shows dozens of old modules (`NPCgen.py`, `abilities.py`, `magic.py`, `Procfile`, `index.Rmd`, `_includes/…`) as **deleted-but-not-committed**, and the entire new Atlas tree + `shiny_app.py` as **untracked**. Last real commit is "Add Heroku configuration files."
- So the refactor exists and largely boots, but it is (a) **uncommitted** and (b) **silently running on placeholder data** wherever a domain module is broken (see §2).

Entry point: `shiny run shiny_app.py` (wrapped by `app.py`; `run_shiny.sh` builds the venv). Deploy config is scattered across **four** targets — Cloud Run (README), App Engine (`app.yaml`, py3.14), Heroku (Procfile, now deleted), and `app/Dockerfile`.

---

## 2. What blocks "make it work" (critical path)

`shiny_app.py` wraps **every** Atlas import in one big `try/except` that, on any failure, swaps in dummy stubs and only prints to stderr. Result: the app *looks* like it runs while generating **placeholder characters**. The real blockers it's hiding:

**2a. Nine files don't compile**, and the damaging ones are on the generation path:

| File | Error | Impact |
|---|---|---|
| `AtlasNomina/Map_of_Titles.py` | TabError (line 757) | NPC **and** Character title generation |
| `AtlasNomina/Map_of_Names.py` → `Races/Aberration, Celestial, Elf, Monstrosity` | syntax / unclosed `[` / indent / stray chars | **name generation** (dynamically imports these) |
| `AtlasInventarium/Compass_of_Rarity.py` | TabError (line 26) | armor / loot rarity |
| `AtlasPugna/Map_of_Weakness.py` | dict key missing `:` (line 114) | monster weaknesses |
| `AtlasWorldBuild/AtlasOfMapmaking/Compass_of_Biomes.py` | nested-quote f-string (line 196) | maps — *valid on 3.12+/3.14, fails below* |
| `AtlasNomina/npc_namer_legacy.py` | invalid char `¡` (line 2068) | **legacy → delete** |

`Grimoire_of_NPC.py` (line 229/246) and `Grimoire_of_Characters.py` (line 347/357) both import `Map_of_Titles`/`Map_of_Names` *inside their methods*, so the top-level import succeeds but **name/title generation throws at call time** — straight into the silent fallback.

**2b. Inconsistent import paths.** Some modules use fully-qualified `AtlasX.Module`; others use **bare** names — `from Compass_of_Rarity import …` (`Ledger_of_Armors.py`), `from AtlasOfMapmaking.Compass_of_Biomes import …` (`Kit_of_ScalableVectorGraphics.py`). Bare imports only resolve when that *exact* directory is on `sys.path`; they break under `shiny run`, tests, and deploy.

**2c. No `__init__.py` in the Atlas packages.** They work only as *namespace packages* from the project root. Fragile for tooling and deploy — one wrong working directory and the imports vanish.

**2d. The silent `try/except` itself.** It converts every real bug above into invisible placeholder output. In development it should **fail loudly** so breakage is visible.

---

## 3. What we don't need anymore (delete candidates)

Verify each, then commit the removals.

- **R / GitHub-Pages era:** `.Rproj`, `DnD.Rproj`, `.Rproj.user/`, `.Rhistory`, `index.Rmd`, `_config.yml`, `_includes/`, `_navbar.yml`, `_site.yml`, `call.html`.
- **Old flat Python modules** already deleted in the tree (`NPCgen.py`, `abilities.py`, `magic.py`, …) — just commit the deletions.
- **Flask remnants under `app/`:** `routes.py`, `templates/`, `static/`, `app/Dockerfile`, `app/Wiki`. **Keep** `app/character_url.py` and `app/random.py` — `shiny_app.py` imports them (consider moving them out and deleting the Flask shell).
- **`AtlasNomina/npc_namer_legacy.py`** — superseded by `Map_of_Names.py`.
- **Cloud-sync conflict copies** in `.venv` (`.gitignore 2`, `bin 2/3/4`, `pyvenv 2.cfg`, …) — delete `.venv` entirely and rebuild; confirm it's gitignored.
- **Deploy sprawl** — pick one target; remove the rest.
- **Scratch files:** `test-write.txt`, stray `new_map_*.svg`.

---

## 4. TOP / TagKit integration (greenfield)

TagKit now comes from the external TOP GitHub package through `requirements.txt`; the local `TagKit/`, `tag-oriented-programming/`, and `TagRefactoring/` copies are removed. Nothing is tagged yet. Highest-value first targets (where tags beat the current class/dict model):

1. **Conditions** (`Map_of_Conditions`) — *poisoned, prone, stunned* are textbook **overlay Tags** on one creature-Agent: sticky marks, `Rip` = condition ends. Smallest, clearest win.
2. **Character/NPC composition** — Species + Class + Background as **Tags layered on one stable identity** — literally TOP's thesis.
3. **Resistances / Weaknesses / Senses** (AtlasPugna) as **contributions/Records**.
4. **Spell effects / Enchantments** as **Imprint/Rip** duals.

Recommendation: **don't start tagging until Phases 0–1 land.** Tagging a codebase that silently falls back to stubs would just hide tag bugs too.

---

## 5. Proposed order (make-it-work first)

**Phase 0 — Make it run for real (no placeholders)**
- 0.1 Make the import fallback **loud** in dev (log/raise) so breakage is visible.
- 0.2 Fix the compiling errors in §2a (delete the legacy one).
- 0.3 Normalize imports to fully-qualified `AtlasX.Module`; add `__init__.py` (or formally commit to namespace packages + a path shim).
- 0.4 Run `shiny_app.py`; generate an NPC, a Character, a spell, a map — confirm **real** (non-stub) output.

**Phase 1 — Commit the migration & cut dead weight**
- 1.1 Commit the working-tree refactor (currently all uncommitted). *(git runs on your machine.)*
- 1.2 Delete R/Flask/legacy (§3); pick one deploy target; rebuild `.venv`; fix `.gitignore`.

**Phase 2 — TOP integration, one Desk at a time** (mirrors your STEP "one topic" rule)
- 2.1 Conditions as overlay Tags.
- 2.2 Species/Class/Background as layered Tags on the character Agent.
- 2.3 Resistances/Weaknesses/Senses as contributions; spell effects as Imprint/Rip.

---

## Appendix — full list of non-compiling files

1. `AtlasInventarium/Compass_of_Rarity.py` — TabError, line 26
2. `AtlasNomina/Map_of_Titles.py` — TabError, line 757
3. `AtlasNomina/Races/Aberration.py` — collapsed/corrupted source, line 60
4. `AtlasNomina/Races/Celestial.py` — `[` never closed, line 48
5. `AtlasNomina/Races/Elf.py` — unexpected indent, line 351
6. `AtlasNomina/Races/Monstrosity.py` — invalid syntax, line 27
7. `AtlasNomina/npc_namer_legacy.py` — invalid char `¡`, line 2068 (legacy → delete)
8. `AtlasPugna/Map_of_Weakness.py` — `:` expected after dict key, line 114
9. `AtlasWorldBuild/AtlasOfMapmaking/Compass_of_Biomes.py` — nested-quote f-string, line 196 (3.10-only failure)
