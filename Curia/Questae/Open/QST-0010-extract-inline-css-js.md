# QST-0010 — Extract ~1000 lines of inline CSS/JS from shiny_app.py into static assets

- **Type:** refactor
- **Priority:** 🟡 normal
- **Status:** Open *(superseded by QST-0021 — do not implement standalone)*
- **Owner:** unclaimed
- **Route to:** Workshop Consul (Artificer), Readability Consul (Barbarian), Simplicity Consul (Monk)
- **Parent:** QST-0007 (Track A / shiny_app.py)
- **Sidequests:** —
- **Related:** **QST-0021** (replacement track) · QST-0008 (NPC sheet) · `app/static/style.css`

---

## 🔍 Diagnosis (what & where)
The 2336-line entrypoint embeds large asset blobs as Python string literals: `EXTRA_STYLE` (~570 lines of CSS, L159–726), `HOME_SCRIPT`, `LOADER_SCRIPT`, `MASONRY_SCRIPT`, and a ~200-line character-URL script (L1655–1862). `app/static/style.css` already exists and is loaded as `BASE_STYLE`, so the split is half-done.

**Update (Julio, 2026-07-07):** Superseded by **QST-0021 AtlasVenustas** — same goal, organized into six sidequests under a presentation Atlas with Kits and Lodges. Implement via QST-0021.1–0021.6 instead of this ticket standalone.

## 🧾 Evidence
- `EXTRA_STYLE = """ … """` L159–726; three `*_SCRIPT` blobs L728–1069; inline `ui.tags.script(ui.HTML(""" … """))` L1655–1862.
- Editors give no CSS/JS linting or highlighting inside Python strings.

## 🎯 Desired outcome
~~CSS moves into `app/static/style.css`…~~ **Handled by QST-0021.3–0021.6.** Close this questa when QST-0021 parent is Solved; reference QST-0021 in Resolution.

## 🧭 Notes for the Agora / implementer
Do **not** start this questa independently. Pick up **QST-0021.1** first.

## ✅ Resolution
*(pending — close when QST-0021 is Solved)*

---

## 🏛️ Council
> Workshop Consul (Artificer): Assets-as-Python-strings defeat caching and every editor tool. There's already a `style.css` — the pattern exists; we just finish it.
> Readability Consul (Barbarian): The file is 2336 lines mostly because of these blobs. Extracting them makes the real logic legible at last.
> Simplicity Consul (Monk): Agreed — this is subtraction from the entrypoint, my favorite kind. Just don't leave CSS in two places. Converged.

**Weighting:** reach 2 × severity 1 = **2** · council leaning: `build` (after QST-0008)
