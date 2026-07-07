# QST-0007 — Full file-by-file diagnostic sweep

- **Type:** docs/chore
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Curia (then Consuls per finding)
- **Related:** all questae; `Canon/`

---

## 🔍 Diagnosis (what & where)
The Curia was seeded from a **first-pass** evaluation (README, `routes.py`, `shiny_app.py` context, `Minion.py`, the TagKit Guide, legacy agent notes, and the migration doc). A **complete, file-by-file diagnostic** of the real source has not yet been done — the many Atlas packages, `shiny_app.py` in full, templates, `scripts/`, and assets remain to be read closely.

## 🧾 Evidence
Seed questae (QST-0001…0006) came from partial reading. The real source is currently buried under committed venvs (see QST-0004), which slowed a full sweep.

## 🎯 Desired outcome
Every real project file read and diagnosed; each issue (bug, refactor, design, naming, safety, TagKit-fit) minted as its own questa and routed to the right Consul. **Diagnose, not solve** — per Julio's instruction.

## 🧭 Notes for the Agora / implementer
- Suggested order: `shiny_app.py` (front is the priority) → the Atlas packages by domain → `scripts/` → templates/assets.
- Diagnose each file by **cycling through the Party roster** (`Agora/Consuls/`) — one lens per Consul, in turn. The lens set is the living roster, not a fixed list, so it grows as seats are added (Decree 0001).
- Produce a short digest of new questae, not a wall of text.
- This is the natural **next big step** after Julio blesses the Curia structure.
