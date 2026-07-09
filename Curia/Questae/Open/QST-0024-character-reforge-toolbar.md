# QST-0024 — Character sheet toolbar grid (reforge controls)

- **Type:** bug / design
- **Priority:** 🟠 high
- **Status:** Open — needs Agora (Dialog 0005)
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Workshop Consul (Artificer), Simplicity Consul (Monk), Flow Consul (Sorcerer)
- **Parent:** QST-0021 (AtlasVenustas presentation layer)
- **Sidequests:** —
- **Related:** QST-0021.3 (Scroll_of_Styles) · QST-0021.6 (Kit_of_ShareableLinks) · Q-0008 · Dialog 0005

---

## 🔍 Diagnosis (what & where)

The **character sheet toolbar** — the control strip at the top of the Character page — does not lay out reliably. Julio has iterated on CSS many times; the grid still misbehaves (column widths, button sizing, level +/- alignment, responsive breakpoints).

The toolbar is the `.character-reforge` block in `shiny_app.py` (~L1354–1402): three `input_select` fields (species, class, background), a level box with `+`/`-` buttons, **Generate**, and **Share**. Its layout is driven by ~180 lines of CSS in `EXTRA_STYLE` (~L404–584).

There is **no single owner** for this widget. Markup, layout CSS, and button classes all live inline in `shiny_app.py`. A Flask-era duplicate still exists in `app/templates/character.html` (different structure, same intent). Nothing in `AtlasVenustas/` assembles or defines this control strip today.

## 🧾 Evidence

- **Competing CSS for the same selectors.** `.character-level-controls` is declared twice in `EXTRA_STYLE`: first as `display: grid` with fixed 2.8rem columns (L309–327), then overridden to `display: contents` with grid-column placement on children (L507–518). The second block exists to make the level box a 3-column grid; the first block is dead weight and signals layout-by-accumulation rather than one coherent model.
- **Shiny DOM vs hand-picked classes.** Buttons use `class_="fantasy-button"` but Shiny renders `input_action_button` as `.action-button`. Recent tweaks switched selectors between `.action-button` and `.fantasy-button` (see unstaged diff in `shiny_app.py`) — a symptom of fighting the framework rather than owning the contract.
- **Grid-area layout is brittle.** Six named areas (`species`, `class`, `background`, `level_block`, `generate`, `share`) with `minmax()` column tracks and a mobile reflow at 900px. Small changes to gap, `min-width`, or child `width: 100%` rules cascade unpredictably because children are heterogeneous (Shiny select wrappers vs bare divs vs action buttons).
- **Styles not yet in Scroll_of_Styles.** All `.character-reforge*` rules remain in `EXTRA_STYLE` inside `shiny_app.py`, not in `app/static/style.css` (QST-0021.3 not done). Every tweak edits the monolith.
- **Julio's report:** multiple fix attempts; problem persists. A structured, modular approach with one source of truth inside Venustas is preferred over more ad-hoc CSS patches.

## 🎯 Desired outcome

A **stable, responsive character toolbar** that:

- lays out correctly at desktop and mobile breakpoints without fragile selector overrides;
- has **one authoritative definition** of which controls exist, their order, and their styling contract;
- lives in the presentation layer (`AtlasVenustas`) per the QST-0021 direction, not scattered across `shiny_app.py` and legacy Flask templates;
- remains fully wired to existing Shiny inputs (`char_sheet_*`, `btn_char_*`) and handlers — behavior unchanged, structure improved.

*How* to achieve that (Kit name, declarative layout vs CSS grid, extraction order relative to QST-0021.3) is **for the Agora** — see Dialog 0005.

## 🧭 Notes for the Agora / implementer

- **Open a Dialog** — Q-0008 / `Dialogs/0005-character-reforge-toolbar-layout.md`.
- Julio's leaning (not a decision): single source of truth, modular Venustas kit — good SE practice; the council should evaluate concrete shapes.
- **Do not** keep patching `EXTRA_STYLE` piecemeal while this quest is open unless Julio explicitly asks for a hotfix.
- **Coordinate with QST-0021.3:** toolbar CSS may move with Scroll_of_Styles, or a dedicated Kit may own both markup and styles — the Agora should pick one path.
- **Share button** wiring overlaps QST-0021.6; extraction order matters — toolbar shell vs share script are separable concerns.
- Flask `character.html` duplicate is out of scope for implementation until QST-0003; note it as drift risk in the Dialog.

---

## ✅ Resolution
*(pending — awaits Dialog 0005 → Decree → implementation questa)*

---

## 🏛️ Council
> Architecture Consul (Druid): A widget with six grid areas, two CSS definitions for the same class, and markup in the entrypoint is not a toolbar — it is a drift magnet. It wants a Kit with a published contract.
> Simplicity Consul (Monk): Stop adding selectors. Either the layout model is one grid with one set of rules, or the toolbar is a single component with an explicit slot list — not both.
> Workshop Consul (Artificer): Venustas already has the Kit pattern (Loader, Tablet, Masonry). This strip is the same species of problem.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `needs a Dialog`
