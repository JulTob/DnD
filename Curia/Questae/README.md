# ⚔️ Questae — the Quest Log

> *A questa is a quest: a task taken up, pursued, and seen through. Every unit of work — a bug, a refactor, a design, a question-made-actionable — is a quest on the board. Post it, take it up, complete it. Then keep it, as a chronicle of what was done and why.*

## The three states (folders)

```
Questae/
├── Open/       minted, awaiting the Agora or a hand
├── Working/    claimed and in progress
├── Solved/     closed — transit state while awaiting reward distillation
└── Rewards/    crystallized experience, one file per solved quest (REW-####)
```

A questa moves by being **moved between folders**. Its status header is updated to match.

## The rules

1. **Nothing meaningful without a questa.** Work is distributed and remembered through them.
2. **Diagnose, don't pre-solve.** A questa describes the *problem* and its *evidence*. Solutions come from the Agora (for decisions) or from an approved implementation questa.
3. **One purpose per questa.** A questa is minimal and single-purpose. Never let it grow — when work branches, **throw a Sidequest** (see below).
4. **Confirmation before action.** A questa being *Open* is not permission to change code — non-trivial work waits for Julio (see `Canon/Single-Source-of-Truth.md`).
5. **Route to the right lens.** Tag which Consul(s)/Agent(s) should weigh in.
6. **`tagkit` = highest urgency.** If TagKit blocks a clean solution, that questa jumps the queue.
7. **Solved questae yield a Reward, then are removed.** `Solved/` is a transit state — a quest stays there until a distillation dialog with Julio confirms the lesson, a `REW-####` file is written in `Rewards/`, and the questa file is deleted. See `Rewards/README.md`.

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
Every questa ends with a **Council** section: a socratic conversation, signed, with the core points briefly exposed, plus a light **reach × severity** weight. It also records *why* the quest is worth doing and what the counselors advise — so the train of thought travels with the quest and survives into the `Solved/` archive. See `QUESTA-template.md`.

## How to work one
1. Pick from `Open/`.
2. Move it to `Working/`, set yourself as main owner, update status.
3. If it needs a decision, open a Dialog in `Agora/`.
4. When done (and confirmed by Julio), move to `Solved/` with an outcome note and links to any Decree/commit.
5. **Separately, in a later step with Julio:** confirm the lesson — does the implementation fit the vision? is the TOP usage correct? is the pattern well-formulated? Then write `Rewards/REW-####.md` and delete the questa from `Solved/`.

See `QUESTA-template.md` to mint a new one.

---

## Register

### 🔴 / 🟠 Priority — Open
| ID | Title | Type | Priority | Route |
|----|-------|------|----------|-------|
| QST-0001 | Finish the Shiny front so users can start | design/refactor | 🔴 | Architecture, Readability, Flow |
| QST-0016 | **Flagship:** unify PC & NPC on one Character root (TOP tags) | tagkit | 🔴 | Druid, Warlock, Wizard, Monk, Bard, Lorekeeper → **Decree 0002** |
| QST-0002 | Character-sheet view (Markdown + CSS) instead of dynamic boxes for long text | design | 🔴 | Architecture, Understanding, Design-Team → Q-0001 |
| QST-0021 | **AtlasVenustas** — presentation layer; slim `shiny_app.py` (6 sidequests) | refactor/design | 🟠 | Druid, Artificer, Barbarian, Monk → **Julio-approved** |
| QST-0003 | Decide & execute Flask removal; retire `app/routes.py` + templates | refactor | 🟠 | Architecture, Ecosystem, Workshop → Q-0004 |
| QST-0004 | Review, clean & unify the venvs — surface conflicts to Julio | chore/cleanup | 🟠 | Workshop, Ecosystem → Decree 0001 |
| QST-0027 | Title map as narrative identity | design/refactor | 🟠 | Bard, Druid, Warlock, Wizard, Monk, Rogue, Lorekeeper → Q-0010 |
| QST-0030 | Minion.py's bug reports lose the signal they exist to carry (3 sidequests) | bug | 🟠 | Sorcerer, Cleric, Barbarian, Lorekeeper |
| QST-0030.1 | One exception, N bug reports: nested Minion decorators don't dedupe | bug | 🟠 | Sorcerer, Monk, Cleric → QST-0030 |
| QST-0031 | Redesign the spell system with TOP (6 sidequests) | tagkit/design | 🟠 | Druid, Warlock, Monk, Rogue, Lorekeeper |
| QST-0031.2 | Delete SPELL_DATA_2024; migrate every entry to Spell(), tagged | tagkit/refactor | 🟠 | Druid, Monk → QST-0031 |
| QST-0031.3 | Apply Compass_of_Spells Tags; collapse the Lodge to one entry per spell | tagkit/refactor | 🟠 | Druid, Monk, Rogue → QST-0031 |
| QST-0030 | Minion.py's bug reports lose the signal they exist to carry (3 sidequests) | bug | 🟠 | Sorcerer, Cleric, Barbarian, Lorekeeper |
| QST-0030.1 | One exception, N bug reports: nested Minion decorators don't dedupe | bug | 🟠 | Sorcerer, Monk, Cleric → QST-0030 |
| QST-0031 | Redesign the spell system with TOP (6 sidequests) | tagkit/design | 🟠 | Druid, Warlock, Monk, Rogue, Lorekeeper |
| QST-0031.2 | Delete SPELL_DATA_2024; migrate every entry to Spell(), tagged | tagkit/refactor | 🟠 | Druid, Monk → QST-0031 |
| QST-0031.3 | Apply Compass_of_Spells Tags; collapse the Lodge to one entry per spell | tagkit/refactor | 🟠 | Druid, Monk, Rogue → QST-0031 |
| QST-0035 | TagKit rollout sequence (after Phase 0) | tagkit/design | 🟠 | Druid, Wizard, Warlock, Lorekeeper → QST-0016 |
| QST-0037 | **AtlasEpica** — DM Character Oracle / epic forge (14 sidequests) | design/refactor | 🟠 | Druid, Bard, Lorekeeper, Artificer, Sorcerer, Wizard, Design-Team |
| QST-0040 | **Modularity law** — Ada ads/adb · TOP API; slim entrypoint (2 sidequests) | rule-update/refactor | 🟠 | Druid, Monk, Wizard, Warlock, Barbarian, Lorekeeper |
| QST-0042 | Review existing Kits against the current TOP Guide | tagkit/docs | 🟠 | Wizard, Warlock, Druid, Lorekeeper → QST-0036 |

### 🟡 / 🟢 Priority — Open
| ID | Title | Type | Priority | Route |
|----|-------|------|----------|-------|
| QST-0005 | Resolve `AtlasLusoris` vs `AtlasAlusoris` near-collision | refactor | 🟡 | Architecture, Readability → Q-0002 |
| QST-0006 | Treat TagKit as settled upstream (retire local-convergence premise) | docs/chore | 🟢 | Architecture, Methods |
| QST-0010 | Extract inline CSS/JS from shiny_app.py *(superseded by QST-0021)* | refactor | 🟡 | Workshop, Readability, Simplicity |
| QST-0013 | Ability modifier recomputed inline instead of canonical `Modifier` | refactor | 🟡 | Contracts, Lorekeeper, Methods |
| QST-0017 | 🔁 Detect orphan files (recurrent) — clean dead, implement ghosts | chore/cleanup | 🟡 | Ecosystem, Workshop, Simplicity, Druid |
| QST-0023 | Silent name fusions (implicit string concat) across the Races | bug | 🟡 | Safety, Readability, Lorekeeper |
| QST-0030.2 | Bug reports double-wrap their own ANSI colors | bug | 🟡 | Barbarian, Fighter → QST-0030 |
| QST-0030.3 | `get_call_tree()` blind outside `app.py`/`shiny_app.py` | bug | 🟡 | Paladin, Rogue, Druid → QST-0030 |
| QST-0032.1 | Sweep the rest of the codebase for the respecified Conventions | docs/chore | 🟢 | Barbarian, Ranger, Bard → QST-0032 |
| QST-0031.4 | First test suite: Compass_of_Spells and the Lodge registry | tagkit/chore | 🟡 | Rogue, Artificer → QST-0031 |
| QST-0031.5 | `Spell.__format__`: one canonical renderer, dispatched by format spec | refactor | 🟡 | Wizard, Monk, Barbarian → QST-0031 |
| QST-0031.6 | Verify and complete every spell's definition | bug/chore | 🟡 | Rogue, Cleric, Lorekeeper → QST-0031 |
| QST-0030.2 | Bug reports double-wrap their own ANSI colors | bug | 🟡 | Barbarian, Fighter → QST-0030 |
| QST-0030.3 | `get_call_tree()` blind outside `app.py`/`shiny_app.py` | bug | 🟡 | Paladin, Rogue, Druid → QST-0030 |
| QST-0032.1 | Sweep the rest of the codebase for the respecified Conventions | docs/chore | 🟢 | Barbarian, Ranger, Bard → QST-0032 |
| QST-0031.4 | First test suite: Compass_of_Spells and the Lodge registry | tagkit/chore | 🟡 | Rogue, Artificer → QST-0031 |
| QST-0031.5 | `Spell.__format__`: one canonical renderer, dispatched by format spec | refactor | 🟡 | Wizard, Monk, Barbarian → QST-0031 |
| QST-0031.6 | Verify and complete every spell's definition | bug/chore | 🟡 | Rogue, Cleric, Lorekeeper → QST-0031 |
| QST-0033 | Typographic system (fonts per element, class, race) | design | 🟡 | Barbarian, Bard, Artificer → QST-0021 |
| QST-0034 | Surface Minion dev log in browser (dev-only) | design | 🟢 | Artificer, Cleric, Sorcerer, Paladin → QST-0030 |
| QST-0036 | TagKit-Doctrine.md names contract primitives the pinned TagKit lacks | docs | 🟡 | Lorekeeper, Warlock, Bard |
| QST-0038 | Homebrew spells that play in the seams between schools | design/question | 🟢 | Lorekeeper, Bard, Warlock |
| QST-0039 | Arcane/Divine/Primal as a character axis (power origin) | tagkit/design | 🟡 | Druid, Lorekeeper, Bard, Warlock → QST-0016 |
| QST-0038 | Homebrew spells that play in the seams between schools | design/question | 🟢 | Lorekeeper, Bard, Warlock |
| QST-0039 | Arcane/Divine/Primal as a character axis (power origin) | tagkit/design | 🟡 | Druid, Lorekeeper, Bard, Warlock → QST-0016 |
| QST-0040.1 | 🔁 Recurrent modularity review (entrypoint & Atlas surfaces) | chore/docs | 🟡 | Druid, Monk, Ranger, Artificer → QST-0040 |
| QST-0040.2 | Canon: Ada ads/adb & TOP API as the modularity test | rule-update/docs | 🟡 | Lorekeeper, Druid, Wizard, Warlock, Bard → QST-0040 |
| QST-0080.1 | Cleric Domain openings still in the older, plainer register | design | 🟡 | Lorekeeper, Bard, Julio → QST-0080 / REW-0001 |

### 🟡 Priority — Open (QST-0037 AtlasEpica sidequests)
| ID | Title | Type | Priority | Parent |
|----|-------|------|----------|--------|
| QST-0037.1 | Vague DM guideline — victory / defeat / hanging resolution | design | 🟠 | QST-0037 |
| QST-0037.2 | Pointy Hat triple axes (martial / social / third TBD) | design | 🟠 | QST-0037 |
| QST-0037.3 | CYOA flow — adventure locus, not only literal dungeons | design | 🟠 | QST-0037 |
| QST-0037.4 | Integrate NPC generator into Epica encounters | design | 🟠 | QST-0037 |
| QST-0037.5 | Open Epica in a new browser tab | design | 🟡 | QST-0037 |
| QST-0037.6 | Collapse story possibility (wave-function metaphor → real API) | design/tagkit | 🟠 | QST-0037 |
| QST-0037.7 | Shareable URL: `/dungeon/<seed>/1/2/4` choice path | design | 🟠 | QST-0037 |
| QST-0037.9 | Self-tests for AtlasEpica modules | chore | 🟡 | QST-0037 |
| QST-0037.10 | Header **DM** → page **Dungeon Master Companion** | design | 🟡 | QST-0037 |
| QST-0037.11 | Character/NPC Tags Epica assumes *(Dialog with QST-0016)* | tagkit | 🟠 | QST-0037 |
| QST-0037.12 | Review findings: Map_of_Prose_Adventure | docs | 🟢 | QST-0037 |
| QST-0037.13 | Theme Tags (inherit / open-close); choices crystallize | tagkit | 🟠 | QST-0037 |
| QST-0037.14 | Titles moved to Epica; vocabulary Lodges still open | design/refactor | 🟠 | QST-0037 |
| QST-0037.15 | Scene box: Tag-gated encounter Lodge (not linear plot) | design/tagkit | 🟠 | QST-0037 |
| QST-0037.16 | **DM Character Oracle** — Companion inspiration cards (active product) | design/refactor/tagkit | 🟠 | QST-0037 |

### 🟡 / 🟢 Priority — Open (QST-0021 sidequests)
| ID | Title | Type | Priority | Parent |
|----|-------|------|----------|--------|
| QST-0022 | Lodge symbol rationale review (species · class · element) | design | 🟡 | QST-0021 |
| QST-0027.1 | Title selectors need a lusor membership protocol | refactor | 🟠 | QST-0027 |
| QST-0027.2 | Title generation needs an explicit RNG source | refactor | 🟠 | QST-0027 |
| QST-0027.3 | Title vocabulary needs thematic structure | design/refactor | 🟡 | QST-0027 |
| QST-0027.4 | Decide title return, yield, and cache strategy | design | 🟡 | QST-0027 |

### ✅ Solved (recent)
| ID | Title |
|----|-------|
| QST-0080 | Cleric voice — distilled to [REW-0001](Rewards/REW-0001-uncommitted-prose-is-already-lost.md); questa deleted (2026-08-31) |
| QST-0037.8 | Canonize **AtlasEpica** (renamed from Specus; Conventions row) (2026-07-15) |
| QST-0036 | TagKit-Doctrine resynced to GitHub Guide (`@Pre`/`@Post`, contributions, no fake orthogonality) (2026-07-17) |
| QST-0018 | Rogue parallel TOP package removed — role-tag half rides with QST-0016.3 (2026-07-15) |
| QST-0032 | Canon/Conventions.md respecified; renamed AtlasVenustas Kit_of_X → Tools_of_X (2026-07-15) |
| QST-0012 | One safe door for plain model text (`_text_html`) (2026-07-09) |
| QST-0008 | NPC sheet speaks the character sheet's vocabulary (2026-07-09) |
| QST-0011 | NPC-list entries open their NPC (2026-07-09) |
| QST-0021.3–.6 | Venustas train: Scroll_of_Styles, Kit_of_Masonry, Kit_of_Tablet, Kit_of_ShareableLinks (2026-07-09) |
| QST-0009 | Silent import shim removed — Minions report, summoners recover (2026-07-07) |
| QST-0021.1 | Scaffold AtlasVenustas + Lodge_of_Symbols |
| QST-0021.2 | Kit_of_Loader + wire shiny_app.py |

### 🟢 Working
| ID | Title | Type | Priority | Route |
|----|-------|------|----------|-------|
| QST-0007 | Full file-by-file diagnostic sweep (Track A underway) | docs/chore | 🟠 | Curia (all Consuls per finding) |
| QST-0031.1 | Build SpellsKit: Tags for school, class list, tradition (steps under Julio's review) | tagkit | 🟠 | Warlock, Druid, Lorekeeper → QST-0031 |
| QST-0031.1 | Build SpellsKit: Tags for school, class list, tradition (steps under Julio's review) | tagkit | 🟠 | Warlock, Druid, Lorekeeper → QST-0031 |
| QST-0041 | AtlasMagistratum — DM Companion extracted; closing dialog pending | design/refactor | 🟠 | Druid, Bard → QST-0040 · QST-0037 |

### 🕵️ Pending to mint (Track A remainder)
- **QST-0014** — `docs/FLASK_TO_SHINY_MIGRATION.md` is stale (says "no shareable URL yet"; hash-URLs + `CharacterPathRedirectASGI` already exist). *(docs · Understanding, Workshop)*
- **QST-0015** — NPC level bounds: UI allows level → 100 while characters clamp 1–20; is uncapped legendary intended? *(rule-update · Lorekeeper, Contracts)*

### 📜 Retired planning docs (integrated into Questae, 2026-07-15)
- `GENLEGEND_STATUS_AND_PLAN.md` → QST-0001 (v1 spine), QST-0016 + QST-0035 (TOP rollout), QST-0009 (import/generation practices)
- `GENLEGEND_TICKETS.md` → QST-0033 (typography), QST-0034 (Minion dev log)
