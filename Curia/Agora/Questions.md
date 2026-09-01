# ❓ Questions for the Agora

> The open queue. Anyone — Julio, a Consul, or an Agent — may add a question. Each becomes a Dialog in `Dialogs/` and, once settled, a Decree in `Decrees/`.

## How to add a question

Append a row. Keep it to one line; detail goes in the Dialog file.

| # | Question | Raised by | Consuls called | Dialog | Status |
|---|----------|-----------|----------------|--------|--------|

---

## Open

| # | Question | Raised by | Consuls called | Dialog | Status |
|---|----------|-----------|----------------|--------|--------|
| Q-0001 | Character display: keep dynamic boxes for Skills/Scores, or move to a 5e.tools-style Markdown "character sheet" styled by CSS? | Julio | Architecture (Druid), Understanding (Bard), Readability (Barbarian), Flow (Sorcerer); Design-Team + Lorekeeper advisory | `Dialogs/0001-character-sheet-vs-boxes.md` | 🟡 needs framing |
| Q-0002 | Resolve `AtlasLusoris` vs `AtlasAlusoris` near-collision — rename, alias, or leave documented? | Curia (eval) | Architecture (Druid), Readability (Barbarian) | — | 🕓 queued |
| Q-0003 | ~~TagKit paradigm: settle the decorator style / open questions~~ | Curia (eval) | — | — | 🔵 closed — invalid premise: TagKit is settled & upstream (see QST-0006) |
| Q-0004 | Flask → Shiny: confirm full removal of Flask and the retirement of `app/routes.py` and templates. | Curia (eval) | Architecture (Druid), Ecosystem (Ranger), Workshop (Artificer), Flow (Sorcerer) | — | 🕓 queued |
| Q-0005 | How should we run the QST-0007 file-by-file diagnostic sweep — order, method, and how findings branch into questae/sidequests? | Julio | Full council (Bard, Druid, Artificer, Ranger, Monk, Rogue, Sorcerer, Wizard, Lorekeeper) | `Dialogs/0002-how-to-run-the-diagnostic-sweep.md` | 🔵 settled → Decree 0001 |
| Q-0006 | What is the minimal Character the generator builds, and how are the RNG & core mechanisms instantiated so PC/NPC diverge by tags? | Julio | Bard, Lorekeeper, Druid, Wizard, Sorcerer, Paladin, Warlock, Monk, Rogue | `Dialogs/0003-minimal-character-and-rng.md` | 🔵 settled → Decree 0002 |
| Q-0007 | The Minions: are they sound, and where should they go — kept, evolved into a Log System, and/or deployment error reporting? | Julio | Full council | `Dialogs/0004-evaluate-the-minions.md` | 🔵 settled → Decree 0003 |
| Q-0008 | Character sheet toolbar (`.character-reforge`): how should layout be owned — inline CSS tweaks, Scroll_of_Styles only, or a Venustas Kit with a single contract? | Julio (via Agent) | Architecture (Druid), Workshop (Artificer), Simplicity (Monk), Flow (Sorcerer), Readability (Barbarian) | `Dialogs/0005-character-reforge-toolbar-layout.md` | 🟡 open |
| Q-0009 | Characteristics grid (`stat-flow`): uniform chips, thematic order, Level box — flex vs grid, label contract? | Julio (via Agent) | Readability (Barbarian), Architecture (Druid), Simplicity (Monk), Lorekeeper | `Dialogs/0006-characteristics-grid-layout.md` | 🟢 converged — awaiting Julio |
| Q-0010 | Title map: how should generated titles become thematic, deterministic narrative identity without leaking lusor internals? | Julio (via Agent) | Understanding (Bard), Architecture (Druid), Contracts (Warlock), Methods (Wizard), Simplicity (Monk), Testing (Rogue), Lorekeeper | `Dialogs/0007-title-map-as-narrative-identity.md` | 🟡 open |
| Q-0010 | Migration order & safety rail for the Character-root refactor (QST-0016.1–.6, QST-0027): what sequence, and what proves each step unbroken? | Julio | Safety (Paladin), Architecture (Druid), Simplicity (Monk), Contracts (Cleric), Methods (Wizard) | `Dialogs/0007-migration-order-and-safety.md` | 🟡 open |
| Q-0011 | When a caster subclass has no spell slots unlocked yet, what should `available_spells` return — and is the companion `NameError: char` the same wound? | Julio (via Agent) | Repair (Cleric), Methods (Wizard), Safety (Paladin), Testing (Rogue) | `Dialogs/0008-arcane-trickster-empty-slots.md` | 🟢 converged — awaiting Julio |
| Q-0012 | After two days of recovery, which failures can Agora + Questae not catch, and what Git/hook/ignore tools must sit beside the Curia? | Julio (via Grok) | Paladin, Druid, Artificer, Wizard, Monk, Lorekeeper, Rogue | `Dialogs/0010-beyond-agora-questae.md` | 🟡 open |

---

## Field notes for open threads

- **For Dialog 0003 / QST-0016 (RNG):** verified 2026-07-09 — `NPC(seed=7)` twice in one process yields *different* names. Mixed RNG sources (`app.random` in the Grimoires, stdlib `random` in `Map_of_Names`) defeat seed reproducibility today. Share-links and list-reopening now avoid regeneration because of this; the minimal-Character design should make the seed the single spine. *(Agent, session 2026-07-09)*

## Settled → see `Decrees/`

*(none yet)*
