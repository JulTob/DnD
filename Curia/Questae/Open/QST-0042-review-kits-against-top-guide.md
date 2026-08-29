# QST-0042 — Review existing Kits against the current TOP Guide

- **Type:** tagkit / docs
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Methods Consul (Wizard), Contracts Consul (Warlock), Architecture Consul (Druid), Lorekeeper
- **Parent:** —
- **Sidequests:** —
- **Related:** `Canon/TagKit-Doctrine.md` · QST-0036 ✓ · QST-0031.1 (SpellsKit) · Guide `spec/SPECIFICATION.md` · Conventions `XKit`

---

## 🔍 Diagnosis (what & where)
Doctrine and the Guide were resynced (QST-0036). Live Kits may still carry pre-sync assumptions: wrong contract names, treating contribution modes as the paradigm, over-claiming orthogonality, or `Kit_of_*` modules that are not TOP `XKit`s at all.

Known surfaces to audit (not exhaustive — discover while reviewing):

| Module | Likely kind | Notes |
|--------|-------------|--------|
| `AtlasMagia/SpellsKit.py` | Real `XKit` (TOP) | First sanctioned TagKit usage; primary audit target |
| `AtlasMagia/Ledger_of_Spell_Lists.py` | Ledger + Tag applications | Must match SpellsKit / Guide membership idioms |
| `AtlasNomina/AtlasScriptum/Kit_of_Elvish.py`, `Kit_of_Dwarvish.py` | Legacy `Kit_of_*` name | Probably *not* TOP — confirm and rename or document |
| `AtlasWorldBuild/.../Kit_of_*.py` (WFC, SVG, HandDrawing) | Legacy `Kit_of_*` | Likely algorithms/tools, not TagKits |
| Any new `*Kit.py` since SpellsKit | TBD | Find via search |

## 🧾 Evidence
- Guide (2026 read): contributions = Action/Record/Imprint/Rip/Operation/Report; contracts = Pre/Post; Underlay extends; composition order-sensitive.
- Doctrine (2026-07-17): matches Guide; forbids catch-all parallel TOP packages.
- QST-0031.1 / SpellsKit already corrected `Expectation` → `@Pre` once; other Kits may not have been checked.

## 🎯 Desired outcome
A short audit report (in this questa's Resolution, or a linked Dialog note) that for each Kit:

1. States whether it is a true TOP `XKit` or a misnamed utility.
2. Lists concrete Guide/Doctrine mismatches (wrong primitives, missing contracts, tangled axes that should be Actions/Operations, etc.).
3. Throws sidequests for each material fix — this questa does not rewrite Kits itself unless Julio asks.

## 🧭 Notes for the Agora / implementer
- **Source of truth:** GitHub Guide at the pinned TagKit commit + installed TagKit — not memory, not old Doctrine wording.
- Prefer reading SpellsKit first as the project's reference pattern, then contrast others against it *and* the Guide (SpellsKit may itself still drift).
- Do not invent a new parallel TOP package while "fixing" Kits.
- Misnamed `Kit_of_*` that are not TOP belong under Conventions' other prefixes (`Tools_of_`, `Charts_of_`, …) — branch rename questae if needed (see QST-0032 / QST-0032.1).

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Methods Consul (Wizard): Audit against the Guide first, SpellsKit second — never against folklore from the deleted parallel package era.
> Contracts Consul (Warlock): Every `@Pre`/`@Post` claim in a Kit must match TagKit's real rollback semantics.
> Architecture Consul (Druid): Separate "is this TOP?" from "is this good TOP?" — rename non-Kits before polishing them as Tags.
> Lorekeeper (Elf Sage): Keep the audit short enough that the next Character Kit author can skim it in one sitting.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `build` (audit + branch fixes)
