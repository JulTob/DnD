# QST-0074 — Restore the modular composition root

- **Type:** refactor / recovery
- **Priority:** 🟡 normal (post-beta)
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture, Workshop
- **Parent:** QST-0027 (modularize the entrypoint)
- **Sidequests:** —
- **Related:** Decree 0006 · QST-0072 · QST-0073 · QST-0075

---

## 🔍 Diagnosis (what & where)

`app/main.py` survived the accident, but the modules it composes did not. Lost to the wipe:

- `app/navigation.py` (`Navigator`, `Page`)
- `app/session.py` (`Session_State`)
- `app/routing.py` (`Shareable_Path_Redirect`)
- `app/client.py` (`Client_Messages`)
- `app/pages/__init__.py` (the page-mount public surface)
- `app/pages/home.py` exists but must be re-verified against the lost siblings

`Curia/Current-State.md` records `app.main:app` as the approved destination. The beta ships from `shiny_app.py` instead (QST-0073).

## 🧾 Evidence

- `import app.main` fails in the recovered tree (see QST-0073 evidence).
- The accident tar (`~/DnD-post-accident-20260829-1645.tar.gz`) and the session export (`~/Downloads/session-export-1788017810958.zip`) may hold bytecode or transcript payloads for the lost modules. Nobody has swept them for `app/` composition files yet.

## 🎯 Desired outcome

1. The lost composition modules are restored (transcript payload first, bytecode second, constrained rewrite last, per QST-0072's recovery law).
2. `app.main:app` boots, serves the same beta scope as `shiny_app.py`, and the preview script switches back to it.
3. `shiny_app.py` is then retired page by page (the QST-0027 train resumes).

## 🧭 Notes for the Agora / implementer

- Do not rebuild these modules from imagination while evidence archives exist unswept.
- The restored root must respect Decree 0006 until Julio widens the scope: player wing lit, other wings dark.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Architecture Consul (Druid): The destination did not change; only the road washed out. Rebuild the bridge after the caravan ships.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `defer`
