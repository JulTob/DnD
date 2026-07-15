# QST-0021 — AtlasVenustas: presentation layer (firmitas · utilitas · venustas)

- **Type:** refactor / design
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Workshop Consul (Artificer), Readability Consul (Barbarian), Simplicity Consul (Monk)
- **Parent:** QST-0007 (Track A / shiny_app.py)
- **Sidequests:** QST-0021.1 ✓, QST-0021.2 ✓, QST-0021.3 ✓, QST-0021.4 ✓, QST-0021.5 ✓, QST-0021.6 ✓ *(all landed 2026-07-09; parent stays Open for Julio’s visual regression + QST-0022/0024)*
- **Proposed for Canon (Julio to add):** Conventions table row — `AtlasVenustas` | UI presentation: styles, client chrome, loader/tablet/masonry/share Kits
- **Related:** QST-0010 (superseded by this track) · QST-0001 · QST-0008 · QST-0024 (character toolbar — Agora Q-0008) · QST-0033 (typography) · Decree 0001

---

## 🔍 Diagnosis (what & where)
`shiny_app.py` (~2380 lines) is the Shiny entrypoint **and** a warehouse for presentation: ~570 lines of `EXTRA_STYLE`, `LOADER_SCRIPT`, `HOME_SCRIPT`, `MASONRY_SCRIPT`, plus an inline character-URL/share script (~L1690–1896). That violates separation of concerns and makes the app hard to read, lint, or cache.

Julio approved extracting presentation into a new top-level Atlas — **`AtlasVenustas`** (Vitruvius: *firmitas, utilitas, venustas* — firmness, utility, beauty). Utility in organization beats rigid convention: assets stay must be organized on modular packages (kits, lodges, maps...); Python modules in the Atlas assemble and wire them.

## 🧾 Evidence
- `EXTRA_STYLE` L162–729; `HOME_SCRIPT` L731–848; `LOADER_SCRIPT` L849–1027; `MASONRY_SCRIPT` L1029–…; inline share/URL script L1690–1896.
- `BASE_STYLE` already reads `app/static/style.css` L159–160 — half-extracted.
- Loader logic is duplicated in legacy `app/templates/base.html` (Flask path); Flask retirement is QST-0003, not this track. Deletion of Flask code is a must, but the functionality and assets must be preserved on Shiny and Python modules. 
- `loaderMagic.js` removed (orphan p5 experiment); live loader is `LOADER_SCRIPT`.

## 🎯 Desired outcome
A thin, minimalist, `shiny_app.py` that imports presentation from `AtlasVenustas`, and other utilities from their corresponding Atlas:

A proposed organization is:
```
AtlasVenustas/
├── Lodge_of_Symbols.py      # rune pools — single source of truth
├── Kit_of_Loader.py         # loader markup + script wiring
├── Kit_of_Masonry.py        # NPC grid masonry script wiring
├── Kit_of_Tablet.py         # home generator tablet script wiring
├── Kit_of_ShareableLinks.py # character hash URL + copy-to-clipboard wiring
└── Scroll_of_Styles.py      # CSS load/merge for Shiny head
```
Individual components (kits, maps...) should be individual quests, with individual reviews. 

**Each sidequest leaves the app runnable.** No big-bang merge.

## 🧭 Notes for the Agora / implementer

### Design principles (Julio-approved)
1. **Firmitas** — each slice is independently verifiable; app boots and generates after every sidequest.
2. **Utilitas** — organization serves maintainability; pragmatic paths over dogma (assets may live in `app/static/`, and glue in Atlas, or be dynamically set by TOP).
3. **Venustas** — preserve the arcane golden loader, tablet UI, and typography; extraction must not regress aesthetics.

### Progression (strict order)
| Step | Questa | Purpose |
|------|--------|---------|
| 1 | QST-0021.1 | Scaffold Atlas + `Lodge_of_Symbols` (zero behavior change) |
| 2 | QST-0021.2 | `Kit_of_Loader` + `app/static/js/loader.js` |
| 3 | QST-0021.3 | `Scroll_of_Styles` + fold `EXTRA_STYLE` → `style.css` |
| 4 | QST-0021.4 | `Kit_of_Masonry` + `app/static/js/masonry.js` |
| 5 | QST-0021.5 | `Kit_of_Tablet` + `app/static/js/tablet.js` |
| 6 | QST-0021.6 | `Kit_of_ShareableLinks` + final `shiny_app.py` slim-down |
| — | QST-0024 | `Kit_of_Reforge` (or Agora-chosen shape) — character toolbar; **after Dialog 0005**; may slot after 0021.3 or parallel if hot |

### Constraints
- **Sequence QST-0021.3 after QST-0008** if NPC-sheet CSS is still in flux (same rule as old QST-0010).
- Do **not** move server logic, reactive handlers, or Atlas domain imports into `AtlasVenustas`.
- Do **not** edit `Canon/Conventions.md` directly — when the Atlas is settled, mint a proposal for Julio to add the row.
- Flask must go.
  - Flask funcitonality in `base.html` must be organized into Shiny. 
  - A loader may later import `Lodge_of_Symbols` via a thin bridge; out of scope until QST-0003.

### Verification (every sidequest)
- [ ] `python shiny_app.py` or project run script starts without error
- [ ] Home → generate character → loader shows → sheet renders
- [ ] NPC generate + NPC list still work
- [ ] Share/copy link on character page still works (from QST-0021.6 onward; N/A before)

## ✅ Resolution
*(pending — parent closes when all sidequests are Solved)*

---

## 🏛️ Council
> Architecture Consul (Druid): Presentation is a real domain — it deserves its own Atlas, not a junk drawer at the foot of the entrypoint. Six slices keep each PR reviewable.
> Workshop Consul (Artificer): Static assets in `app/static/`, Python assembly in `AtlasVenustas` — Shiny's file serving stays simple.
> Readability Consul (Barbarian): *Firmitas, utilitas, venustas* — good names for what we're optimizing. The entrypoint should read like an index, not an encyclopedia. 

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `build` (sequential sidequests)
