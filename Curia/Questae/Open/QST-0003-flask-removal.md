# QST-0003 — Decide & execute Flask removal

- **Type:** refactor
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Ecosystem Consul (Ranger), Workshop Consul (Artificer), Flow Consul (Sorcerer) → **Q-0004**
- **Related:** QST-0001, `docs/FLASK_TO_SHINY_MIGRATION.md`

---

## 🔍 Diagnosis (what & where)
Flask and Shiny currently coexist. `app/routes.py` (Flask) duplicates logic that now lives in `shiny_app.py`. The migration doc recommends removing Flask, `app/routes.py`, unused templates, and Flask-only dependencies (`Flask`, `Flask-SocketIO`, `gunicorn`, possibly `Jinja2`/`Werkzeug`).

## 🧾 Evidence
- `app/__init__.py`: "No Flask; use `shiny run shiny_app.py`."
- `app/routes.py`: full Flask route set still present.
- `docs/FLASK_TO_SHINY_MIGRATION.md` §3 "Remove Flask and related code" — an explicit checklist.
- Flask-SocketIO noted as "in requirements but not used."

## 🎯 Desired outcome
A single stack (Shiny only): Flask code removed or archived, dependencies trimmed, deploy config aligned to `shiny run`, nothing broken.

## 🧭 Notes for the Agora / implementer
- **Decide before deleting** (Q-0004): confirm no test/tool still needs `create_app()`; decide archive vs. delete for `app/templates/`.
- Preserve `app.random` and the Atlas modules (used by Shiny).
- Do it after QST-0001 scoping so we don't remove something the front still leans on.
