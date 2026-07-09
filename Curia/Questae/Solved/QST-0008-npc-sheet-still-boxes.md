# QST-0008 — NPC sheet still uses the box/masonry grid for long text

- **Type:** design
- **Priority:** 🔴 urgent  *(this is the still-open half of Q-0001)*
- **Status:** Solved (2026-07-09)
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Understanding Consul (Bard), Readability Consul (Barbarian), Flow Consul (Sorcerer) → **Q-0001 / Dialog 0001**
- **Parent:** QST-0007 (Track A / shiny_app.py)
- **Sidequests:** —
- **Related:** QST-0002, Dialog 0001

---

## 🔍 Diagnosis (what & where)
`build_character_sheet` (shiny_app.py ~L1197) **already** renders the modern "sheet" — a rail (scores/skills/saves) + stat-chips + markdown prose sections. But `build_npc_sheet` (~L1358) still uses the old `npc-grid` with `.npc-box`/`.npc-textbox` and a JS **masonry** packer, cramming long-form fields (Combat, Spellcasting, Legendary, Lair, Region, Story) into boxes. This is exactly Julio's "boxes break for long text" — now localized to the **NPC** panel.

## 🧾 Evidence
- Character panel: `sheet` / `sheet-rail` / `prose_section` (L1197–1355). Good.
- NPC panel: `npc-grid` + `prose_block` + `MASONRY_SCRIPT` (L1358–1471, L996). Long prose in a masonry grid.

## 🎯 Desired outcome
The NPC sheet reads like the character sheet: short stats in a tidy rail/header, long text as flowing prose. Retire the masonry grid for the NPC page (or keep it only for genuinely short chips).

## 🧭 Notes for the Agora / implementer
Decision belongs to **Dialog 0001** (character-sheet direction). This questa is the concrete NPC-side implementation once that's decreed. Reuse `prose_section`/`build_character_sheet`'s structure — don't invent a third layout.

## ✅ Resolution
- **Decided by:** Julio (refactor go, 2026-07-09; direction from Dialog 0001)
- **What changed:** commit `08e1eb5`. `build_npc_sheet` now mirrors `build_character_sheet`: npc-header, rail (stat-flow chips + scores/skills/saves/languages/movement/senses/resistances), main column of `prose_section` blocks (Personality, Combat, Spellcasting, Martial, Legendary, Lair, Region, Story). Masonry left the NPC page; `stat_chip` lifted to module level and shared; `prose_block` is caller-less, marked to retire with QST-0026.
- **Practice/preference to remember:** one sheet vocabulary for every being - when a second page needs a layout, it borrows the first page's helpers, never invents a third. Visual acceptance on a live run is Julio's step.

---

## 🏛️ Council
> Understanding Consul (Bard): The model is already proven on the character side — this is *apply the same shape*, not design a new one. Half the work is deletion.
> Architecture Consul (Druid): Agreed. Factor the character sheet's rail+prose into a shared builder both panels call; the NPC just supplies different fields. One layout, two feeders.
> Flow Consul (Sorcerer): And retiring masonry on this page removes a MutationObserver reflow loop — less churn, not more.
> Readability Consul (Barbarian): No objection; prose beats boxes for the reader here. Converged.

**Weighting:** reach 2 × severity 3 = **6** · council leaning: `needs a Dialog` (0001) then `build`
