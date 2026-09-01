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
4. Start the Shiny application and verify the **Player** path (Decree 0004). NonPlayer verification waits until after first publish.
5. Commit a coherent recovery checkpoint when Julio says so.

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

Neither lane edits the other lane's claimed files without a written handoff.

## Checkpoints

- [x] Preserve the post-accident tree in a recovery commit.
- [x] Locate the Claude export, Codex session patches, archive, and bytecode.
- [x] Reconstruct and isolate-test the Character and Gender foundation.
- [x] Reconstruct Proficiency, Skills, Tools, Ability Scores, and Minion.
- [x] Restore Backgrounds and their registered catalogues (TOP `tools`/`roleplay`; verify fidelity).
- [~] Restore Guilds, Wizard training, Alignment — **runtime via vault bootstraps**; real `.py` still open.
- [x] Import and compile player path (`shiny_app`); `app.main` still fails NonPlayer imports.
- [~] Verify Player generation (green, with `Race_Ingredient` soft-fail). NonPlayer still open.
- [~] Start and visually smoke-test Shiny (player path).
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
