# QST-0001 — Finish the Shiny front so users can start

- **Type:** design/refactor
- **Priority:** 🔴 urgent  *(Julio's stated top priority: get the app working on the front for users)*
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Readability Consul (Barbarian), Flow Consul (Sorcerer)
- **Related:** QST-0002 (character-sheet view), QST-0003 (Flask removal), QST-0024, QST-0025, QST-0026, Q-0001, QST-0014 (stale migration doc)

---

## 🔍 Diagnosis (what & where)
The Shiny front implements core flows (home, character, NPC, NPC list) but is not yet **"done enough" for first users."** Phase 0 (make it run for real) is complete; the remaining gap is acceptance, in-flight UI decisions, and cleanup — not greenfield migration.

## 🧾 Evidence
- **Phase 0 done (2026-07-07):** real generation end-to-end, no import shim (QST-0009 Solved), Atlases are regular packages, `shiny_app.py` entry point stable (`shiny run shiny_app.py`, `make run`, `app.py`).
- **Refactor train landed (2026-07-09):** QST-0012, QST-0008, QST-0011, QST-0021.3–.6 Solved — `shiny_app.py` ~2100 → ~1230 lines; styles/scripts are Venustas static assets; share links live (QST-0021.6).
- **Still open on the spine:**
  - **Visual regression (Julio, live run)** — acceptance: home, character gen, NPC prose layout, NPC list click-through, share links (`make run`).
  - **Front decisions in flight** — Dialog 0005 → QST-0024 (reforge toolbar); Dialog 0006 → QST-0025 (characteristics grid, Working); QST-0026 spell prose (Working).
  - **Flask removal** — QST-0003 (deferred 2026-07-07); `app/routes.py`, templates, static still present; `app/character_url.py` and `app/random.py` stay (Shiny imports them).
  - **Venv & deploy** — QST-0004; deploy spans `app.yaml` / Dockerfile / `Run_And_Deploy.sh` — pick one target.
  - **Data quality** — QST-0023 (~60 silent name fusions in Races corpus).
- `app/routes.py` (Flask) still present and duplicates logic.

## 🎯 Desired outcome
A Shiny front a user can open and use end-to-end: generate a character and an NPC, view them well (see QST-0002), and navigate without dead ends. **"Good enough to ship to first users"** — with Julio's live-run sign-off as the acceptance gate.

## 🧭 Notes for the Agora / implementer
- This is the spine; QST-0002 (display), QST-0003 (Flask removal), QST-0024–0026 hang off it.
- Shareable URLs are **done** (QST-0021.6) — no longer a blocker here.
- About/Lore remain footer links (not panels) — post-v1 unless Julio promotes them.
- Confirm scope with Julio before each implementation step. Diagnose here; child questae carry the work.

---

## ✅ Resolution
*(pending — closes when Julio accepts live-run regression and remaining spine questae are Solved or explicitly deferred)*

---

## 🏛️ Council
> Flow Consul (Sorcerer): Phase 0 is behind us — the user path works; what remains is polish, acceptance, and dead-code removal.
> Readability Consul (Barbarian): Visual regression is the honest gate — the prose sheet and share links need Julio's eyes on a live run.
> Architecture Consul (Druid): Flask removal (QST-0003) is cleanup, not blocker — but it should follow v1 acceptance so we don't delete reference code mid-debug.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `build` (acceptance + in-flight UI questae)
