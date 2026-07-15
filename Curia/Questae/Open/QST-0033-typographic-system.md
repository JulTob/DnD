# QST-0033 — Typographic system (fonts per element, class, and race)

- **Type:** design
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Readability Consul (Barbarian), Understanding Consul (Bard), Workshop Consul (Artificer)
- **Parent:** QST-0021 (AtlasVenustas)
- **Sidequests:** —
- **Related:** QST-0021.3 (Scroll_of_Styles), Dialog 0001 (sheet presentation)

---

## 🔍 Diagnosis (what & where)
Character and NPC sheets use a small set of IM Fell faces with gold rules between prose sections, but **one body font everywhere**. Identity, stats, magic, and lore do not yet read as distinct *syntactic layers* — and class/race flavour is not expressed typographically. We can ework on these aesthetics by providing type variation between IM Fell typografic (and alike).

## 🧾 Evidence
- Interim state (2026-07): IM Fell DW Pica + DW Pica SC + Great Primer + Great Primer SC are loaded; gold rules separate prose sections.
- Parked scope (formerly `GENLEGEND_TICKETS.md` TICKET-01): distinct faces were wanted per element — identity (display), headings (small-caps), body/lore, skills/stats (tabular legibility), magic (arcane), and optional per-class/race overrides.

## 🎯 Desired outcome
A **font map** keyed by section (`identity`, `skills`, `magic`, …) with optional class/race overrides, applied as CSS classes (`.syn-magic`, `.race-dwarf`, …). Faces defined once as CSS variables; class/race can re-point variables via a body-level class. **Done when:** changing one map flips fonts for that element everywhere, and a Dwarf wizard visibly reads different from an Elf bard.

## 🧭 Notes for the Agora / implementer
- Candidate faces (from parked notes): Cinzel / Cinzel Decorative or a vintage display face for identity; IM Fell SC for headings; DW Pica / Great Primer for body; a clean tabular face for stats; an arcane face for spells.
- Belongs in **Scroll_of_Styles** / Venustas — not inline in `shiny_app.py`.
- Open a Dialog if per-race font overrides conflict with performance or licensing constraints.

---

## ✅ Resolution
*(pending)*

---

## 🏛️ Council
> Readability Consul (Barbarian): Typography is part of the sheet contract — stats must stay scannable; lore can be expressive. One map, many surfaces.
> Understanding Consul (Bard): Class and race flavour through type is exactly the narrative-identity direction we're already pursuing with titles and symbols.
> Workshop Consul (Artificer): CSS variables + body-level class overrides keep this maintainable inside Venustas; don't scatter `@font-face` blocks.

**Weighting:** reach 2 × severity 1 = **2** · council leaning: `needs a Dialog` (scope vs. v1)
