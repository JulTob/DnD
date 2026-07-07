# QST-0001 — Finish the Shiny front so users can start

- **Type:** design/refactor
- **Priority:** 🔴 urgent  *(Julio's stated top priority: get the app working on the front for users)*
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Readability Consul (Barbarian), Flow Consul (Sorcerer)
- **Related:** QST-0002 (character-sheet view), QST-0003 (Flask removal), Q-0001, `docs/FLASK_TO_SHINY_MIGRATION.md`

---

## 🔍 Diagnosis (what & where)
The web app is being moved from Flask to Shiny. `shiny_app.py` already implements the core flows (home, character, npc, npc list) per `docs/FLASK_TO_SHINY_MIGRATION.md`, but the front is not yet "done enough" for real users. Gaps noted in the migration doc: no shareable URLs yet; About/Lore are footer links, not panels; favicon/error pages not yet handled in Shiny.

## 🧾 Evidence
- `app/__init__.py` states the web app is Shiny (`shiny run shiny_app.py`), no Flask.
- `docs/FLASK_TO_SHINY_MIGRATION.md` lists an explicit, unfinished checklist.
- `app/routes.py` (Flask) still present and duplicates logic.

## 🎯 Desired outcome
A Shiny front a user can open and use end-to-end: generate a character and an NPC, view them well (see QST-0002), and navigate the app without dead ends. "Good enough to ship to first users."

## 🧭 Notes for the Agora / implementer
- This is the spine that QST-0002 (display), QST-0003 (Flask removal) hang off. Sequence them.
- Do a scoping pass first: list exactly what "usable v1" requires vs. what is post-launch (shareable URLs may be post-launch → its own Question).
- Confirm scope with Julio before building. Diagnose here; implementation questae to follow.
