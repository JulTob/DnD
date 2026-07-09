# QST-0025 — Characteristics grid: uniform chips, thematic order, Level box

- **Type:** design
- **Priority:** 🟠 high
- **Status:** Working
- **Owner:** Agent (Julio's request)
- **Route to:** Readability (Barbarian), Architecture (Druid), Simplicity (Monk), Lorekeeper
- **Parent:** QST-0021 (Atlas Venustas presentation layer)
- **Sidequests:** —
- **Related:** Q-0009 · Dialog 0006 · QST-0002 · QST-0008

---

## 🔍 Diagnosis (what & where)

The **Characteristics grid** (`stat-flow` / `stat-chip` in `build_character_sheet`, `shiny_app.py` ~L1102–1149) packs identity and combat stats into flex-wrapped `.npc-box` cells. Layout is uneven and thematically scrambled:

- **Level** appears only in the sheet header, not as a chip — Julio's revelation: it belongs in the grid.
- **Speed** boxes grow too wide (long values like `30 ft., fly 60 ft.` + `flex: 1 1 132px` grow).
- **PB** is too narrow (`Proficiency Bonus` is the longest label, wraps badly).
- **AC** / **Armor Class** label causes width mismatch vs short chips.
- **Icons** in stat chips use `font-size: 1.7em` while score boxes use a 30px circle at 17px — chips look oversized and don't sit in the circle.
- **HP** and **Hit Dice** can land on different flex rows depending on viewport width.

Root cause: **content-driven flex** with no fixed grid, conflicting `max-width` rules (`.npc-box` 180px vs `.stat-flow > .npc-box` 210px), and inconsistent symbol styling between score rail and stat chips.

## 🧾 Evidence

```python
# shiny_app.py L1102–1111 — current chip order (identity before combat; no Level)
stat_chips = [
    stat_chip("⚖️", "Alignment", ...),
    stat_chip("📏", "Size", ...),
    stat_chip("⚧", "Gender", ...),
    stat_chip("⚜️", "Proficiency Bonus", ...),
    stat_chip("💚", "Health Points", ...),
    stat_chip("🎲", "Hit Dice", ...),
    stat_chip("🛡️", "Armor Class", ...),
    stat_chip("👟", "Speed", ...),
]
```

```css
/* shiny_app.py EXTRA_STYLE — flex grow causes uneven widths */
.stat-flow > .npc-box { flex: 1 1 132px; max-width: 210px; min-width: 120px; }
.stat-chip .symbol { font-size: 1.7em; }  /* vs style.css circle at 17px */
```

## 🎯 Desired outcome

- Level is a **stat chip** in the Characteristics grid.
- Chips live in the **left rail** (quick consultation reference), above scores/skills/saves.
- **2-column grid** with adjacent concept pairs:
  - Alignment · Gender
  - Size · Speed
  - Level · Proficiency Bonus
  - Hit Points · Hit Dice
  - Armor Class (full width)
- **Full record labels** — no abbreviations (Proficiency Bonus, not PB).
- Uniform cell sizing; icons in the same circle treatment as ability scores.

## 🧭 Notes for the Agora / implementer

- Scope: **PC character sheet** (`build_character_sheet`) only — NPC sheet unification remains QST-0008.
- Prefer CSS grid (`repeat(3, 1fr)`) over flex-wrap for the 9-chip layout (3×3).
- Do not start QST-0021.3 extraction in this slice — change `EXTRA_STYLE` inline block only.
- Open Dialog **0006** for the systematic layout contract; Julio decides before any Decree.

---

## ✅ Resolution (filled when Solved)

- **Decided by:** *(pending Julio)*
- **What changed:** *(pending)*
- **Practice/preference to remember:** *(pending)*
