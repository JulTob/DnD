# QST-0026 — Spell definitions must render as prose (not boxed cells)

- **Type:** design
- **Priority:** 🔴 urgent
- **Status:** Working
- **Owner:** unclaimed
- **Route to:** Readability Consul (Barbarian), Architecture Consul (Druid), Flow Consul (Sorcerer)
- **Parent:** QST-0002
- **Sidequests:** QST-0026.1 · QST-0026.2 · QST-0026.3
- **Related:** QST-0002 · Dialog 0001 · QST-0008 · QST-0021

---

## 🔍 Diagnosis (what & where)
Long spell text (starting with `Friends` cantrip and likely others) is still appearing inside boxed/card-like containers instead of flowing as normal sheet prose. This contradicts the agreed character-sheet direction: short stats in compact boxes, long definitions in markdown-like prose sections.

Likely scope:
- Character spell sections in `build_character_sheet` (`shiny_app.py`)
- Any reusable spell formatting helpers used by character and NPC rendering paths

## 🧾 Evidence
- Julio report: `Friends` cantrip name + definition is still wrapped in a box.
- Existing Curia direction already settled this principle:
  - QST-0002: long text must not be boxed.
  - Dialog 0001 framing: dynamic boxes break for long prose.

## 🎯 Desired outcome
- All spell definitions (cantrips and leveled spells) render as readable prose blocks.
- No spell description is rendered in compact stat-box containers.
- The rule is applied systematically across all spell output paths, not as a one-off fix.

## 🧭 Notes for the Agora / implementer
- This is implementation alignment with settled direction; no new Dialog needed unless a conflict appears.
- Prefer a single formatting path for spell prose to avoid future drift.
- Keep character and NPC behavior coherent where spell text is presented.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** *(pending)*
- **What changed:** *(pending)*
- **Practice/preference to remember:** Long-form content (spell definitions, lore, features) belongs to prose sections, never compact stat boxes.
