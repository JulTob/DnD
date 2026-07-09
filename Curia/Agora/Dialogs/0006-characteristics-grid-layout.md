# Dialog 0006 — Characteristics grid: systematic layout contract

- **Question (Q-0009):** How should the PC character sheet **Characteristics grid** (`stat-flow`) be structured so chips are uniform, thematically ordered, and include Level — without fighting flex-wrap and label-length variance?
- **Raised by:** Julio (via Agent)
- **Related Questae:** QST-0025, QST-0021, QST-0002, QST-0008
- **Consuls called:** Readability (Barbarian), Architecture (Druid), Simplicity (Monk), Lorekeeper
- **Status:** 🟢 converged — awaiting Julio's decree

---

## 🧭 Framing

Julio observed the Characteristics grid is **messy**: Speed too wide, PB too narrow, icons too large for their circle, Armor Class too wide, and stats not ordered thematically (HP and Hit Dice can split across lines). He also had a revelation: **Level belongs in the grid** as a chip, not only in the header line.

The grid lives in `build_character_sheet` (`shiny_app.py` ~L1094–1149): nine `stat_chip()` calls inside `.stat-flow`, styled by `EXTRA_STYLE` and global `.npc-box` / `.symbol` rules in `style.css`.

A good answer must:
- produce **uniform chip cells** regardless of value length (e.g. multi-mode Speed);
- use **short record labels** with full names still discoverable;
- keep **HP adjacent to Hit Dice** at all breakpoints;
- add **Level** as a chip and avoid redundant duplication in the header;
- reuse the **existing circle symbol** pattern from the ability-score rail;
- stay scoped to the PC sheet — NPC unification is QST-0008.

Out of scope: extracting CSS to `Charts_of_Styles` (QST-0021.3); NPC sheet migration.

---

## 🗣️ Deliberation

Readability Consul (Barbarian): The reader's eye wants a **stat block**, not a tag cloud. Flex-wrap sorts by leftover space, not meaning. I count nine chips — a **3×3 CSS grid** reads naturally: three rows of three equal columns. Order top-to-bottom, left-to-right:

| Level | PB | HP |
| HD | AC | Speed |
| Alignment | Size | Gender |

Row 1 is *who strong* (progression + current health). Row 2 is *how you endure and move in combat*. Row 3 is *identity*. HP and HD are adjacent in reading order (positions 3→4). Labels should be **short on the page, long on hover**: `PB` with `title="Proficiency Bonus"`, `HP` / `HD` / `AC` likewise. "Proficiency Bonus" and "Armor Class" spelled out are why PB feels cramped and AC feels wide — the label is doing layout work it shouldn't.

Architecture Consul (Druid): The structural bug is **two layout authorities**: `.npc-box { max-width: 180px }` in `style.css` and `.stat-flow > .npc-box { flex: 1 1 132px; max-width: 210px }` in `EXTRA_STYLE`, plus flex-grow letting Speed absorb slack. I propose a single contract:

1. `.stat-flow` → `display: grid; grid-template-columns: repeat(3, minmax(0, 1fr));`
2. `.stat-flow > .npc-box` → reset flex, `width: 100%; max-width: none; min-width: 0`
3. `.stat-chip` → fixed internal layout: circle symbol **centered top** (same 28px / 14px as scores), record label, value below
4. `stat_chip(emoji, short_label, value, title=full_name)` — Python owns order; CSS owns size

Level moves into `stat_chips`; header line drops the leading `Level N` and keeps `Class, Subclass` only — one source for level, in the grid.

Simplicity Consul (Monk): Delete the flex rules; don't add a fourth layout mechanism. The score rail already proves the circle symbol works — **stop overriding** `.stat-chip .symbol` to `1.7em`. One symbol style, centered for chips, top-left for score rows. No new Kit for nine boxes — that's QST-0021 scope creep. This is ~30 lines CSS + reorder the Python list.

Lorekeeper Consul (Elf Sage): On a 5e sheet, **Level** sits with proficiency bonus in the header block; **HP and Hit Dice** are paired; **AC and Speed** are combat essentials. The proposed order matches 2024 character sheet grouping well enough for our presentation layer. Abbreviations PB/HP/HD/AC are table-standard; full words on `title` satisfy accessibility without costing layout. No rules conflict.

Readability Consul (Barbarian): Conceding to Monk — no new Kit. One objection answered: at ≤560px, 3 columns may be tight; add `@media (max-width: 560px) { .stat-flow { grid-template-columns: repeat(2, 1fr); } }` so chips stay legible on phones. HP/HD may stack vertically on the narrowest view but remain **consecutive in DOM order**, which is the best we can do without 1-column (too tall).

Architecture Consul (Druid): Accepted. DOM order already guarantees HP before HD regardless of column wrap.

---

## ✅ Convergence check

- [x] Every called Consul has spoken.
- [x] Every objection answered or conceded.
- [x] A concrete proposal (grid + label contract + code sketch) is on the table.

---

## 🕊️ Vox report

Vox: The council agrees the Characteristics grid fails because **flex-wrap delegates layout to content length**, while **long record labels** amplify the mismatch. All Consuls converge on a **3-column CSS grid** (2 columns on very narrow screens), **short labels with `title` tooltips**, **Level as the first chip**, and **header trimmed** so class/subclass remain without repeating level.

### Common ground
- Nine chips → CSS grid, not flex-grow.
- Short labels: Level, PB, HP, HD, AC, Speed; identity row last.
- Reuse circle symbol sizing from score boxes; remove the 1.7em override.
- Level chip is new; remove `Level N` prefix from the header `h1`.

### Options

| Option | Summary | Tradeoffs |
|--------|---------|-----------|
| **A (recommended)** | 3×3 grid, short labels + `title`, thematic order above, symbol circles unified | Requires small CSS + Python reorder; header loses redundant level text |
| **B** | Keep flex but fixed `width: 140px` per chip | Simpler CSS diff, but ragged rows on wide screens; doesn't fix thematic order without manual row breaks |
| **C** | Move characteristics into the left rail below scores | Puts all numbers in one column; rail becomes very tall; fights current sheet-body layout |

### Consul recommendations
- **Barbarian, Druid, Monk, Lorekeeper** → Option A.

### Code sketch

```python
def stat_chip(emoji: str, label: str, value: str, *, title: str | None = None) -> ui.Tag:
    record = ui.div({"class": "record", "title": title or ""}, label)
    ...

stat_chips = [
    stat_chip("⬆️", "Level", str(data.get("Level", "-"))),
    stat_chip("⚜️", "PB", f"+{data.get('PB', '-')}", title="Proficiency Bonus"),
    stat_chip("💚", "HP", str(data.get("Health", "-")), title="Hit Points"),
    stat_chip("🎲", "HD", str(data.get("HPD", "-")), title="Hit Dice"),
    stat_chip("🛡️", "AC", str(data.get("AC", "-")), title="Armor Class"),
    stat_chip("👟", "Speed", str(data.get("Speed", "-"))),
    stat_chip("⚖️", "Alignment", ...),
    stat_chip("📏", "Size", ...),
    stat_chip("⚧", "Gender", ...),
]
```

```css
.stat-flow {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 8px;
}
.stat-flow > .npc-box { width: 100%; max-width: none; min-width: 0; flex: unset; }
.stat-chip { align-items: center; text-align: center; padding: 30px 6px 10px; position: relative; }
.stat-chip .symbol {
    position: absolute; top: 6px; left: 50%; transform: translateX(-50%);
    width: 28px; height: 28px; font-size: 14px; margin: 0;
}
@media (max-width: 560px) {
    .stat-flow { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
```

### Vox synthesis
**Lead recommendation: Option A.** Implement grid + short labels + Level chip + unified symbols as a focused change in `shiny_app.py` `EXTRA_STYLE` and `build_character_sheet`. Strongest alternative: Option C (rail consolidation) — defer unless Julio wants a larger sheet redesign.

→ Awaiting Julio's decision. If approved, record as Decree 0004 and close QST-0025.
