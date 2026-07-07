# QST-0017 — Detect orphan files (recurrent)

- **Type:** chore/cleanup
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Ecosystem Consul (Ranger), Workshop Consul (Artificer), Simplicity Consul (Monk), Architecture Consul (Druid)
- **Parent:** —
- **Sidequests:** one per confirmed orphan cluster, as found
- **Recurrence:** 🔁 **recurrent** — re-run each diagnostic sweep and periodically thereafter (candidate for a scheduled task once the sweep tooling exists).
- **Related:** QST-0007 (diagnostic sweep), QST-0004 (venv cleanup)

---

## 🔍 Diagnosis (what & where)
The project has accumulated files whose role is unclear. An **orphan** is a project file in one of two states:
- **Dead orphan** — present but **referenced by nothing** (no import, no route, no template include). Candidate to **clean** (delete/archive).
- **Ghost orphan** — **referenced but missing/empty**, or a stub imported somewhere it isn't fully implemented. Candidate to **implement**.

Neither should linger silently: dead files mislead readers; ghosts hide broken paths.

## 🧾 Evidence (initial signals)
- Many top-level dirs and loose files (e.g. `Enchantments/`, `SpellsEffects/*.p5js`, `docs/` R-site, `instance/`, `Users/`, scattered `*.svg`) whose live use is unverified.
- The Flask/Shiny split (QST-0003) leaves `app/routes.py` + `app/templates/*` possibly orphaned once Shiny is sole.
- Confirmed clean already: the six committed venvs (QST-0004).

## 🎯 Desired outcome
A repeatable pass that lists every project file as **live**, **dead orphan → clean**, or **ghost orphan → implement**, and mints a sidequest per cluster. Run it each sweep and on a cadence, so orphans never accumulate again.

## 🧭 Notes for the Agora / implementer
- **Diagnose, don't delete.** This quest only *classifies*; each removal/implementation is its own confirmed sidequest (deletions need Julio, per Canon).
- Method: build a reference graph from entrypoints (`shiny_app.py`, `app.yaml`) — reachable = live; unreachable = dead orphan; imported-but-absent = ghost.
- Exclude generated/ignored paths (venvs, `__pycache__`, `docs/site_libs`).
- Recurrence hook: once the reference-graph script exists, wire it to a scheduled task and let the **Ranger** report a short digest.

## ✅ Resolution
*(recurrent — never fully "Solved"; each pass links the sidequests it spawned)*

---

## 🏛️ Council
> Ecosystem Consul (Ranger): I own the terrain map — I'll build the reachability graph from the entrypoints. Reachable is live; the rest is suspect. I only *report*; I don't cut.
> Simplicity Consul (Monk): Dead code is the most seductive clutter — it looks like work. Finding it is half the battle to removing it. Endorsed.
> Architecture Consul (Druid): Distinguish dead from ghost carefully — a "missing" file may be an unfinished feature, not garbage. Ghosts route to *implement*, not delete.
> Workshop Consul (Artificer): Make it repeatable and scheduled, or it rots. A one-off cleanup is a Sisyphus quest; a recurring report is hygiene. No objection.

**Weighting:** reach 2 × severity 1 = **2** · council leaning: `build` (as a recurring report)
