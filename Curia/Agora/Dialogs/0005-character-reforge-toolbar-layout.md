# Dialog 0005 — Character sheet toolbar: layout model & Venustas ownership

- **Question (Q-0008):** How should the character sheet toolbar (`.character-reforge`) be structured so layout is stable — and where does the single source of truth live in AtlasVenustas?
- **Raised by:** Julio (via Agent)
- **Related Questae:** QST-0024 (flagship), QST-0021 (parent track), QST-0021.3, QST-0021.6
- **Consuls called:** Architecture (Druid), Workshop (Artificer), Simplicity (Monk), Flow (Sorcerer), Readability (Barbarian)
- **Status:** 🟡 open — deliberation started

---

## 🧭 Framing

The Character page opens with a **reforge toolbar**: species / class / background selects, level +/- , Generate, Share. It is implemented today as a CSS grid (`.character-reforge`) with markup and ~180 lines of CSS inline in `shiny_app.py`. Julio has tried many CSS tweaks; layout issues persist (column sizing, button alignment, responsive reflow).

**The question is architectural, not cosmetic:** what is the right *ownership model* for this widget so we stop fighting Shiny's DOM and duplicate CSS?

A good answer must:
- produce a **stable layout** at desktop and ≤900px breakpoints without selector whack-a-mole;
- establish **one source of truth** for control inventory, order, and styling contract;
- fit **AtlasVenustas** conventions (Kit + optional static assets) and the QST-0021 extraction sequence;
- keep **Shiny input IDs and handlers** unchanged (`char_sheet_species`, `btn_char_apply_selectors`, etc.) — this Dialog is presentation structure, not server logic;
- not regress **Share** behavior (coordinate with QST-0021.6).

Out of scope: Flask `character.html` retirement (QST-0003); character sheet body layout (QST-0002 / Dialog 0001); NPC toolbar (may reuse the chosen pattern later).

Constraints from Canon: propose, don't push; diagnose before prescribing in the Questa; Julio decides.

---

## 🗣️ Deliberation

Architecture Consul (Druid): The failure mode is clear — we have three authorities (markup in `character_panel`, layout CSS in `EXTRA_STYLE`, global `.fantasy-button` in `style.css`) and no published contract between them. Shiny wraps selects and buttons in its own divs; the grid assigns areas to our wrappers, not to Shiny's inner nodes. Every tweak changes one layer without updating the contract. I propose a **`Kit_of_Reforge`** (or similarly named) in `AtlasVenustas/` that exports `reforge_toolbar(*inputs)` — a function returning the toolbar `ui.div` tree from **declared slots**, plus a single CSS block (or BEM-scoped class prefix) co-located in the Kit. `shiny_app.py` passes the already-defined `ui.input_*` widgets into the Kit; the Kit owns structure and class names only.

Workshop Consul (Artificer): Seconding the Kit, with a practical split: **markup assembly in Python**, **styles in `app/static/css/reforge.css`** (or folded into `style.css` when QST-0021.3 lands). The Kit publishes `reforge_head_tags()` if we need a dedicated stylesheet. Match `Kit_of_Loader` / `Kit_of_Tablet` — one widget, one kit, one import in the head. Do *not* leave a second `.character-level-controls { display: grid }` block next to `display: contents`; pick one layout strategy and delete the other.

Simplicity Consul (Monk): The duplicate `.character-level-controls` rules are the smoking gun — we are layering hacks. Before any flex vs grid debate: **one layout mechanism**. My lean: a simple **two-column CSS grid on desktop** (left column = three stacked selects, right column = level + actions) implemented with **explicit wrapper divs per row**, not `display: contents` tricks. Fewer moving parts, easier to read in DevTools. If that cannot meet the aesthetic, say so with evidence — but do not add a third override block.

Flow Consul (Sorcerer): From the user's chair, the toolbar is the primary interaction on the Character page — misaligned +/- buttons and uneven select widths read as "broken app," not "CSS nit." Extraction must be **incremental and verifiable**: one PR that introduces the Kit with **pixel-parity or improvement**, app still boots, generate still works. Sequence matters — if we extract markup before styles move out of `EXTRA_STYLE`, we duplicate work. Prefer: **Kit markup first** (same CSS classes, zero visual change), then **move CSS** in QST-0021.3 or as part of QST-0024's implementation questa.

Readability Consul (Barbarian): Name the slots in the Kit docstring so the next reader sees the toolbar as a table — `species`, `class`, `background`, `level`, `generate`, `share` — not six anonymous `ui.div` calls buried in `shiny_app.py`. The Questa already describes the problem well; the Kit should make the solution obvious on first open.

Architecture Consul (Druid): On Shiny's `.action-button` vs `.fantasy-button`: the Kit should document that Shiny **always** adds `.action-button`. Styling should target `.reforge-toolbar .action-button` (scoped) rather than toggling between global class names. Optionally add `fantasy-button` for shared theme hooks, but the scoped selector is the contract.

Workshop Consul (Artificer): Extraction order proposal for Julio: **(A)** `Kit_of_Reforge.reforge_panel(...)` with current CSS unchanged; **(B)** consolidate CSS into one file, delete duplicate rules; **(C)** simplify layout per Monk if still brittle. Step C only if B does not fix it.

Simplicity Consul (Monk): Objection to doing (B) and (C) in one step — agree with Artificer's sequence. One objection remains open: should the level +/- be **native `ui.input_numeric`** instead of paired action buttons? That would shrink DOM and remove the 3-column grid inside the level box. Worth listing as an option, not decided here.

Flow Consul (Sorcerer): `input_numeric` changes handler wiring and may fight the golden fantasy chrome — keep it as an **option** in the Vox report, not the default path, unless Julio wants fewer moving parts over visual parity.

*(Deliberation continues — convergence not yet claimed.)*

---

## ✅ Convergence check
- [ ] Every called Consul has spoken.
- [ ] Every objection has been answered or conceded.
- [ ] At least one concrete proposal (with code sketch) is on the table.

---

## 🕊️ Vox report
*(pending — Vox reports after convergence)*

→ Awaiting council convergence, then Julio's decision. To be recorded as Decree NNNN.
