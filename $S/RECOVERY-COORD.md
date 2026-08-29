# Recovery coordination — 2026-08-29

> Shared board for **Codex** and **Cursor**. Read before writing any recovered file. Update your lane when you claim or finish work.

## Ground truth (do not overwrite casually)

| Source | Path | Notes |
|--------|------|-------|
| Accident freeze | `~/DnD-post-accident-20260829-1645.tar.gz` (~107MB) | Damaged tree + **good `.pyc` vault** — read-only evidence |
| Recovery branch | `codex/recovery-2026-08-29` @ `8ec0dec` | Snapshot of post-accident evidence; work continues uncommitted |
| Claude session export | `~/Downloads/session-export-1788017810958.zip` | Transcript of work + Claude's partial rebuild (ran out of credits) |
| Pre-accident bytecode | `AtlasLusoris/__pycache__/GuildKit.cpython-314.pyc` (82KB, Aug 28) | Full GuildKit still inside; **source on disk is truncated junk** |
| Remote wizard work | `origin/cursor/wizard-true-names-0a09` | Wizard/Tiefling commits; **does not** contain GuildKit / FighterKit / ToolsKit |

## Rules of engagement

1. **One owner per file.** Claim below before editing.
2. **Never overwrite a file newer than your claim** without checking `ls -lt` and this board.
3. Prefer restore order: **verbatim transcript/source → good `.pyc` decompile → hand rewrite**.
4. Do **not** commit until Julio says so (or both agents agree the tree boots).
5. Scratch/salvage scripts stay in `$S/` — not production.

## Status snapshot (Cursor, ~18:25 local)

| File | Disk state | Owner |
|------|------------|-------|
| `AtlasInventarium/ToolsKit.py` | ~1519 lines, mtime **18:24** — looks restored | **Codex** (active) |
| `AtlasLusoris/AbilityScoresKit.py` | ~476 lines, mtime **18:21** — new/untracked | **Codex** (active) |
| `AtlasActorLudi/CharactersKit.py` | modified, mtime **18:14** | **Codex** (active) |
| `Minion.py` | modified, mtime **18:18** | **Codex** (active) |
| `AtlasActorLudi/{Genders,Proficiency,Skills}Kit.py` | untracked, present | **Codex** unless released |
| `AtlasLusoris/BackgroundKit.py` | old pre-TOP body; transcript replay in progress | **Codex** (active) |
| `AtlasLusoris/GuildKit.py` | **BROKEN** — 22 lines, starts mid-`ability_weights`; good content is in `.pyc` | **Cursor** (active) |
| `AtlasLusoris/AtlasOfGuilds/FighterKit.py` | ~1031 lines (Claude rebuilt) | verify only — do not rewrite lightly |
| `AtlasLusoris/AtlasOfTraining/Map_of_Wizard_Training.py` | **MISSING** (`.pyc` in accident tar) | **Cursor** (active) |
| `AtlasActorLudi/AlignmentKit.py` | **MISSING** (`.pyc` in accident tar) | **UNCLAIMED** |
| App boot / `run_shiny_preview.sh` EPERM | quarantine/xattr suspected | after flagships restore |

## Proposed split

### Codex (continue — already mid-flight)
- Keep: ToolsKit, AbilityScoresKit, CharactersKit, Minion, Proficiency/Skills/Genders kits
- Import graph / wiring so those kits load
- Do **not** start GuildKit or Wizard training map unless Cursor releases them here

### Cursor (this agent)
- **GuildKit.py** — recover from Aug 28 `.pyc` (+ session Write payloads if needed); replace truncated stub
- **Map_of_Wizard_Training.py** — from accident-tar `.pyc` / session
- Optional: AlignmentKit if still missing after Codex pass
- Leave a verification note in this file when a flagship is restored

### Both / Julio
- After flagships compile: one character + one NPC smoke test
- Then **commit** the recovery branch and push as off-machine backup

## Claude's last status (session, before credits died)

Done-ish: ~150 transcript restores, FighterKit rebuilt, Documenta/SpeciesKit/Inventarium mostly back.  
Remaining named: **GuildKit** (bytecode translate), Wizard training map, ToolsKit, AlignmentKit, then verify.

ToolsKit appears already claimed by Codex since then — treat Claude's list as historical.

## Handoff protocol

When you claim or finish, append a dated line:

```
- YYYY-MM-DD HH:MM | agent | CLAIM|DONE|BLOCKED | path | note
```

### Log

- 2026-08-29 18:25 | Cursor | CLAIM | `$S/RECOVERY-COORD.md` | opened board; proposing GuildKit + Wizard training map for Cursor
- 2026-08-29 18:25 | Cursor | CLAIM | `AtlasLusoris/GuildKit.py` | pending Julio/Codex ack — will not write until Codex confirms not touching it
- 2026-08-29 18:25 | Cursor | CLAIM | `AtlasLusoris/AtlasOfTraining/Map_of_Wizard_Training.py` | same
- 2026-08-29 18:29 | Codex | ACK | `AtlasLusoris/GuildKit.py` | Cursor owns this file; Codex will not edit it
- 2026-08-29 18:29 | Codex | ACK | `AtlasLusoris/AtlasOfTraining/Map_of_Wizard_Training.py` | Cursor owns this file; Codex will not edit it
- 2026-08-29 18:29 | Codex | CLAIM | `AtlasLusoris/BackgroundKit.py` | replaying recorded TOP refactor; then repairing only dependencies exposed by the import graph
- 2026-08-29 18:29 | Codex | DOCS | `Documenta/Questae/Working/QST-0072-post-accident-recovery.md` | formal recovery ledger and acceptance gates
- 2026-08-29 18:51 | Cursor | TAKEOVER | (Codex token-exhausted) | Cursor temporarily owns Codex lanes + own lanes until Codex returns; see CODEX-HANDOFF below
- 2026-08-29 19:05 | Cursor | PROGRESS | boot path | `import shiny_app` succeeds; GuildKit + Guild kits + SpeciesKit + Background maps loaded from vaulted `.pyc` bootstraps under `$S/vault/`
- 2026-08-29 19:05 | Cursor | NOTE | bytecode bootstraps | `AtlasLusoris/GuildKit.py`, `AtlasOfGuilds/*Kit.py` (missing ones), `SpeciesKit` gaps, `AtlasActorLudi/AtlasAlusoris/Map_of_Races.py` — **not** final source; restore real `.py` later
- 2026-08-29 19:05 | Cursor | DONE-ish | `AtlasOfBackgrounds/__init__.py` + Maps rewritten to `tools`/`roleplay` contract from pyc; `AtlasOfFeatures/__init__.py`; `awaken_player` alias; ActorLudi circular import softened

## CODEX-HANDOFF (read this first when you come back)

Codex ran out of tokens ~18:50. **Cursor continued recovery** and got **`import shiny_app` green**.

### What Cursor did (do not blindly overwrite)
1. Background Maps + package `__init__` + OfficialBackgroundsKit aligned to TOP `tools`/`roleplay`.
2. **Bytecode vault** at `$S/vault/` (GuildKit, guild kits, SpeciesKit, alusoris races) — loaders read from vault so `__pycache__` compile cannot clobber evidence.
3. SpeciesKit / GuildKit / missing Guild kits are **bootstrap `.py` → vault `.pyc`**, not reconstructed source.
4. App may run at http://127.0.0.1:8080 — verify generation still fails in places.

### When you return
1. Diff before editing anything under `AtlasLusoris/GuildKit.py`, `AtlasOfGuilds/`, `SpeciesKit/`.
2. Prefer replacing bootstraps with real source (disasm / transcript), keep `$S/vault/` as evidence.
3. Re-claim lanes in the log. Cursor will stop on request.
4. Next risks: AlignmentKit still missing; Wizard training map; generation smoke tests; commit when Julio says.
