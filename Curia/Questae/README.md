# ⚔️ Questae — the Quest Log

> *A questa is a quest: a task taken up, pursued, and seen through. Every unit of work — a bug, a refactor, a design, a question-made-actionable — is a quest on the board. Post it, take it up, complete it. Then keep it, as a chronicle of what was done and why.*

## The three states (folders)

```
Questae/
├── Open/       minted, awaiting the Agora or a hand
├── Working/    claimed and in progress
└── Solved/     closed — kept forever as memory of practice & preference
```

A questa moves by being **moved between folders**. Its status header is updated to match.

## The rules

1. **Nothing meaningful without a questa.** Work is distributed and remembered through them.
2. **Diagnose, don't pre-solve.** A questa describes the *problem* and its *evidence*. Solutions come from the Agora (for decisions) or from an approved implementation questa.
3. **One purpose per questa.** A questa is minimal and single-purpose. Never let it grow — when work branches, **throw a Sidequest** (see below).
4. **Confirmation before action.** A questa being *Open* is not permission to change code — non-trivial work waits for Julio (see `Canon/Single-Source-of-Truth.md`).
5. **Route to the right lens.** Tag which Consul(s)/Agent(s) should weigh in.
6. **`tagkit` = highest urgency.** If TagKit blocks a clean solution, that questa jumps the queue.
7. **Solved questae are never deleted.** They record *why* we did things — the project's long memory.

## 🌿 Sidequests (branching)

A questa must stay **minimal and one-purpose**. When acting on one reveals more work, do **not** widen the questa — **branch a Sidequest**: a child questa with its own single purpose. Sidequests may throw their own sidequests, without limit.

> *Example:* QST-0007 (diagnose the app) throws a sidequest to review dependencies → that sidequest throws one sidequest **per dependency** → any of those may throw its own. The tree stays legible because every node has exactly one purpose.

- **Id scheme:** a sidequest extends its parent's id with a dotted index — `QST-0007.1`, `QST-0007.2`, and nested `QST-0007.2.1`.
- **Links:** the child names its `Parent:`; the parent lists its `Sidequests:`. Follow the chain up or down at any time.
- **A parent is not "Solved" while an open sidequest remains** — unless the parent is explicitly closed as *superseded by its branches* (note it in the Resolution).

## Naming & id

`QST-####-short-slug.md` — zero-padded, incrementing. Sidequests use the dotted form `QST-####.N-short-slug.md`. The slug is human-readable and may be flavorful.

## Types (label in the header)
`bug` · `refactor` · `design` · `rule-update` · `docs` · `chore/cleanup` · `tagkit` · `tagkit-upstream` · `question`

> **`tagkit-upstream` = "Suggest to TagKit: X".** TagKit is an independent upstream project (pinned in `requirements.txt`), not local code. When TagKit itself is the blocker, mint a `tagkit-upstream` questa as a *proposal to that project* — we never patch a local copy; we bump the pin once a change lands. See `Canon/TagKit-Doctrine.md`.

## Priority
🔴 urgent · 🟠 high · 🟡 normal · 🟢 low   *(a `tagkit` blocker is always 🔴)*

## 🏛️ The Council section
Every questa ends with a **Council** section: a short, signed, Socratic weighing by the seats it was routed to, plus a light **reach × severity** weight. It records *why* the quest is worth doing and what the counselors advise — so the train of thought travels with the quest and survives into the `Solved/` archive. See `QUESTA-template.md`.

## How to work one
1. Pick from `Open/`. 2. Move it to `Working/`, set yourself as owner, update status. 3. If it needs a decision, open a Dialog in `Agora/`. 4. When done (and confirmed), move to `Solved/` with an outcome note and links to any Decree/commit.

See `QUESTA-template.md` to mint a new one.

---

## Register

### 🔴 / 🟠 Priority — Open
| ID | Title | Type | Priority | Route |
|----|-------|------|----------|-------|
| QST-0001 | Finish the Shiny front so users can start | design/refactor | 🔴 | Architecture, Readability, Flow |
| QST-0016 | **Flagship:** unify PC & NPC on one Character root (TOP tags) | tagkit | 🔴 | Druid, Warlock, Wizard, Monk, Bard, Lorekeeper → **Decree 0002** |
| QST-0018 | Remove AtlasTOP; fold composition into the Grimoires (first slice of 0016) | refactor | 🔴 | Monk, Druid, Warlock → Decree 0002 |
| QST-0002 | Character-sheet view (Markdown + CSS) instead of dynamic boxes for long text | design | 🔴 | Architecture, Understanding, Design-Team → Q-0001 |
| QST-0008 | NPC sheet still uses the box/masonry grid for long text | design | 🔴 | Architecture, Understanding, Readability, Flow → Q-0001 |
| QST-0021 | **AtlasVenustas** — presentation layer; slim `shiny_app.py` (6 sidequests) | refactor/design | 🟠 | Druid, Artificer, Barbarian, Monk → **Julio-approved** |
| QST-0003 | Decide & execute Flask removal; retire `app/routes.py` + templates | refactor | 🟠 | Architecture, Ecosystem, Workshop → Q-0004 |
| QST-0004 | Review, clean & unify the venvs — surface conflicts to Julio | chore/cleanup | 🟠 | Workshop, Ecosystem → Decree 0001 |
| QST-0011 | NPC-list entries are dead links (`href="#"`) | bug | 🟠 | Implementation, Understanding |
| QST-0012 | Inconsistent HTML escaping — NPC sheet injects raw model strings | bug | 🟠 | Safety, Contracts |

### 🟡 / 🟢 Priority — Open
| ID | Title | Type | Priority | Route |
|----|-------|------|----------|-------|
| QST-0005 | Resolve `AtlasLusoris` vs `AtlasAlusoris` near-collision | refactor | 🟡 | Architecture, Readability → Q-0002 |
| QST-0006 | Treat TagKit as settled upstream (retire local-convergence premise) | docs/chore | 🟢 | Architecture, Methods |
| QST-0010 | Extract inline CSS/JS from shiny_app.py *(superseded by QST-0021)* | refactor | 🟡 | Workshop, Readability, Simplicity |
| QST-0013 | Ability modifier recomputed inline instead of canonical `Modifier` | refactor | 🟡 | Contracts, Lorekeeper, Methods |
| QST-0017 | 🔁 Detect orphan files (recurrent) — clean dead, implement ghosts | chore/cleanup | 🟡 | Ecosystem, Workshop, Simplicity, Druid |
| QST-0023 | Silent name fusions (implicit string concat) across the Races | bug | 🟡 | Safety, Readability, Lorekeeper |

### 🟡 / 🟢 Priority — Open (QST-0021 sidequests)
| ID | Title | Type | Priority | Parent |
|----|-------|------|----------|--------|
| QST-0021.3 | Charts_of_Styles + fold EXTRA_STYLE → style.css | refactor | 🟡 | QST-0021 |
| QST-0021.4 | Kit_of_Masonry + `app/static/js/masonry.js` | refactor | 🟡 | QST-0021 |
| QST-0021.5 | Kit_of_Tablet + `app/static/js/tablet.js` | refactor | 🟡 | QST-0021 |
| QST-0021.6 | Kit_of_ShareableLinks + shiny_app.py close-out | refactor | 🟡 | QST-0021 |
| QST-0022 | Lodge symbol rationale review (species · class · element) | design | 🟡 | QST-0021 |

### ✅ Solved (recent)
| ID | Title |
|----|-------|
| QST-0009 | Silent import shim removed — Minions report, summoners recover (2026-07-07) |
| QST-0021.1 | Scaffold AtlasVenustas + Lodge_of_Symbols |
| QST-0021.2 | Kit_of_Loader + wire shiny_app.py |

### 🟢 Working
| ID | Title | Type | Priority | Route |
|----|-------|------|----------|-------|
| QST-0007 | Full file-by-file diagnostic sweep (Track A underway) | docs/chore | 🟠 | Curia (all Consuls per finding) |

### 🕵️ Pending to mint (Track A remainder)
- **QST-0014** — `docs/FLASK_TO_SHINY_MIGRATION.md` is stale (says "no shareable URL yet"; hash-URLs + `CharacterPathRedirectASGI` already exist). *(docs · Understanding, Workshop)*
- **QST-0015** — NPC level bounds: UI allows level → 100 while characters clamp 1–20; is uncapped legendary intended? *(rule-update · Lorekeeper, Contracts)*

### ✅ Solved
*(none yet — see `Solved/`)*
