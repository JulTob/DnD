# QST-0072 — Recover the pre-accident Shiny and TOP application

- **Type:** bug / recovery / tagkit
- **Priority:** 🔴 urgent
- **Status:** Working
- **Owner:** Codex and Cursor, with one owner per file
- **Route to:** Architecture, Workshop, TagKit, Lorekeeper
- **Parent:** —
- **Sidequests:** minted only when recovery reveals independent new work
- **Related:** QST-0001 · QST-0003 · QST-0016 · QST-0035 · QST-0047

---

## Diagnosis

The working tree was restored from an old Git state whose supported application
was Flask. Much of the later Shiny, TagKit, and Character-root work existed only
as uncommitted source, session transcripts, and Python bytecode.

The current tree therefore contains files from incompatible moments in the
migration. A single module may be intact while one of its imports is an older
contract or a truncated body.

## Evidence

- `app.main:app` is the intended Shiny composition root recorded by
  `Curia/Current-State.md`.
- The accident snapshot is preserved on recovery branch
  `codex/recovery-2026-08-29` at commit `8ec0dec`.
- The Claude export, prior Codex sessions, the accident archive, and recovered
  `.pyc` files preserve complementary parts of the lost work.
- The live ownership and handoff board is `$S/RECOVERY-COORD.md`.

## Desired outcome

1. Recover the last evidenced Shiny and TOP implementation without reviving
   Flask as the supported application.
2. Make `app.main` import cleanly.
3. Compile the recovered packages and pass their focused self-tests.
4. Start the Shiny application and verify one Player and one NonPlayer path.
5. Commit a coherent recovery checkpoint before resuming feature work.

## Recovery law

Evidence is preferred in this order:

1. exact source or patch payload from a recorded session;
2. source recovered from known-good bytecode;
3. a minimal reconstruction constrained by Canon and current callers.

One collaborator owns a file at a time. Ownership, completion, and blockers are
recorded in `$S/RECOVERY-COORD.md` before another collaborator crosses that
boundary.

## Active lanes

### Codex — foundation and import graph

- Character, Gender, Proficiency, Skill, Tool, Ability Score, and Minion
  foundations;
- `BackgroundKit.py` and its directly exposed dependencies;
- incremental import, compilation, and focused behavior checks.

### Cursor — damaged flagship recovery

- `AtlasLusoris/GuildKit.py`;
- `AtlasLusoris/AtlasOfTraining/Map_of_Wizard_Training.py`;
- `AlignmentKit.py` only after recording a separate claim.

### Claude — bootstrap exit and beta review (joined 2026-08-29 21:10)

- Replace every bytecode bootstrap with real source, prioritized by what the
  character generator imports: `GuildKit`, the vaulted `AtlasOfGuilds` kits,
  `AtlasOfTraining` maps, `SpeciesKit` gaps, `AlignmentKit`,
  `AtlasAlusoris/Map_of_Races`, `AtlasEpica` Titles and Stories,
  `AtlasInventarium/Map_of_Gear_Titles`, and the `Race_Ingredient` naming;
- evidence order per the recovery law: session-export transcript payloads
  first, vault `.pyc` reconstruction (disassembly-verified) second,
  Canon-constrained rewrite last;
- full review of the beta path (Decree 0006): generation, sheet, styles,
  shareable links;
- works only in worktree `sweet-mclean-44e50b`
  (branch `Julio_Cl/dnd-genlegend-recovery-ea160e`); merges via the board.

Neither lane edits the other lane's claimed files without a written handoff.

## Checkpoints

- [x] Preserve the post-accident tree in a recovery commit.
- [x] Locate the Claude export, Codex session patches, archive, and bytecode.
- [x] Reconstruct and isolate-test the Character and Gender foundation.
- [x] Reconstruct Proficiency, Skills, Tools, Ability Scores, and Minion.
- [ ] Restore Backgrounds and their registered catalogues.
- [ ] Restore Guilds, Wizard training, Alignment, and exposed dependencies.
- [x] Import and compile the supported Shiny application (`shiny_app`; the
      modular `app.main` root stays down, deferred to QST-0074 by Decree 0006).
- [x] Verify Player generation (`summon_player(seed=42, level=1)`, Cursor,
      2026-08-29 19:37). NonPlayer verification deferred to QST-0075.
- [ ] Exit bytecode-bootstrap mode: real `.py` for every vaulted module on the
      beta path (Claude lane). Landed so far: `Map_of_Gear_Titles` (gate
      PASS), `AlignmentKit` (gate PASS, self-test green), four SpeciesKit
      modules (gate PASS), and `GuildKit` itself: recovered as its authentic
      pre-wipe source from dangling git blob `62ece79e` plus two transcript
      edits, marshalling byte-identical to the vault bytecode. Five valuable
      dangling blobs are pinned against gc under `recovery-blob-*` tags,
      including the lost NonPlayer rites grimoire (QST-0075 evidence).
- [ ] Start and visually smoke-test Shiny (beta scope: character generator).
- [ ] Record a coherent recovery commit.

---

## Resolution

- **Decided by:** Julio, who explicitly approved reconstruction on 2026-08-29
- **What changed:** in progress
- **Practice/preference to remember:** do not rely on Git alone for valuable
  uncommitted work; preserve a coherent checkpoint before broad restoration.

---

## Council

> Architecture Consul (Druid): Restore contracts from their strongest evidence
> and advance through the import graph in small, testable slices.
>
> Workshop Consul (Artificer): Divide ownership by file and keep a common
> handoff ledger so concurrent recovery cannot overwrite recovered work.
>
> Lorekeeper Consul: Treat transcripts and documents as evidence of intent, not
> as new instructions that supersede Julio.

**Weighting:** reach 3 × severity 3 = **9** · council leaning: `build`
