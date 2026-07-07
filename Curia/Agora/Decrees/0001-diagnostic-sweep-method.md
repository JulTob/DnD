# Decree 0001 — The diagnostic sweep: method & venv arbitration

- **Ratified by:** Julio, 2026-06-23
- **Source:** Dialog 0002 (Q-0005), QST-0007
- **Status:** active

## Decision

**1. Method of the QST-0007 diagnostic sweep.**
- The sweep **diagnoses, never solves**; output is a **digest**, not a wall.
- Unit of output = a **finding** → exactly one **minimal, one-purpose Questa**. Larger work **branches a Sidequest** (`QST-####.N`); it never fattens the parent.
- Per file, **cycle through the Party roster** — each Consul reads the file through *its own lens* in turn (architecture, methods, contracts/safety, simplicity, readability, ecosystem, flow, testing, repair, implementation, workshop, game-canon, …). The set of lenses **is** the living roster in `Agora/Consuls/`: seat a new Consul (or a legend like Galadriel) and the analysis grows with it — there is no fixed list to maintain. *(Refines the council's original "seven lenses" framing in Dialog 0002 into a roster-driven cycle.)*
- Each finding carries a light **reach × severity** weight (two integers, 1–3) and a **Council** section.
- **Order:** two-track. **Track A (front-first)** walks the app's runtime path (`shiny_app.py` → its real imports) to unblock the Shiny front (QST-0001). **Track B (exhaustive)** then sweeps in boundary/dependency order (data & types → grimoires → Atlas packages → app/scripts), one sidequest per Atlas.

**2. Venv arbitration (the fork in Q-0005).**
Julio chose neither pure filter-now nor blind deletion, but: **review, clean, and unify the virtualenvs into one — surfacing every conflict for Julio's decision.** No environment is deleted or standardized without his ruling on the conflicts (Python version, Flask-vs-Shiny scope, dependency versions). This supersedes the council's "filter-now manifest" as the leading option.

**3. Kick-off.** **Begin Track A now.** Read `shiny_app.py` and its real imports; mint one diagnosis-only Questa per finding.

## Reasoning
The council reached unanimous common ground on the diagnose-only, one-purpose-questa, seven-lens, digest-not-wall shape. The only true fork was the venv clutter; Julio refined it into a review-and-unify with a decision gate, because the venvs mix machines and Python versions and must not be resolved by guesswork. Front-first ordering honors the standing priority: ship the app to first users.

## Alternatives not chosen
- **Filter-now (manifest only):** fast, but leaves the clutter in the repo; Julio preferred to actually unify the environments.
- **Clean-first by deletion:** would delete tracked venvs outright; rejected in favor of review + conflict-surfacing (nothing destroyed without a ruling).
- **Strict dependency order (leaves-first):** cleaner in theory, but would leave the front for last; rejected for front-first.

## Consequences
- **QST-0004** is reframed from "remove venvs" to **review → clean → unify → surface conflicts to Julio** (conflict decisions pending — see the quest and the questions put to Julio).
- **QST-0007** gains sidequests as the sweep proceeds (`QST-0007.1` = Track A / shiny_app.py, and so on).
- **Track A findings** are minted as **QST-0008 …** (this session's first batch).
- The **Council** section is now part of every questa (`QUESTA-template.md`), per Julio's review note.
