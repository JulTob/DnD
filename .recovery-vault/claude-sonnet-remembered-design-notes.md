# Remembered design notes — Claude (Sonnet 5), 2026-08-30

Not recovered *code* — recovered **intent**. This session has no memory of
`GuildKit.py`, `SpeciesKit`, or the Training maps; that work happened in
sessions after the one this conversation continued from, and the `.pyc`
vault + `~/Downloads/session-export-1788017810958/transcript.jsonl` are the
real evidence for those. What follows are two things this session *does* have
with certainty, dropped here as a reference sample for whoever reconstructs
the flagship files, so a rewrite stays faithful to already-ratified intent
instead of drifting into something merely plausible.

## 1. Decree 0002 — the Character root's original, ratified spec

Read directly from `Curia/Agora/Decrees/0002-character-root-and-dice.md`
earlier in this session (ratified by Julio, 2026-06-23). This is almost
certainly the founding spec that GuildKit/SpeciesKit/the TagKit rollout were
built to satisfy — worth checking any reconstruction against it line by line:

1. **One root: `Character`**, obtained by refactoring the existing
   `Grimoire_of_Characters.py` — never a parallel skeleton. PC and NPC are
   **tags** on that one root, never separate classes.
2. **Minimal stored substrate:** `name` and `title` (both required — the
   generator always produces a `Name, Title` pair as a narrative seed, title
   is not optional flavour), the six rolled `scores`, `size`, `tier` (level
   for PCs / CR·level for NPCs), `seed`, and the **Dice**.
3. **Everything else is computed or tagged.** Skills, HP, AC, proficiency
   bonus, modifier — computed/derived, never stored (a stored skill is a
   cache that drifts). Species, class, background, features, equipment,
   story — tags.
4. **The RNG *is* the Dice.** Each Character owns its own seeded RNG, named
   `Dice`: `Charlie.Roll(D=6)`. Every mechanism rolls through the
   Character's own Dice — no global `random`, no module-level seeding. A
   Character is a pure function of its seed.
5. **`AtlasAlusoris` merges into `AtlasLusoris`.** Non-player is a tag
   (`Non`/`Player`), not a parallel Atlas.
6. **`AtlasTOP` is removed.** Its composition (`compose_character`/
   `compose_npc`, the `kind` stamp) folds directly into the Grimoires using
   TagKit; `kind = character/npc` becomes the Player/Non role tag.

**Litmus test named in the source quest (QST-0016):** adding a PC-only
feature must never touch NPC code, and vice versa — no `if is_npc:`, anywhere.

## 2. Standing design feedback from this project's memory (cross-session)

These are Julio's own corrections from sessions this one has persistent
memory of (not this conversation) — the `originSessionId` on each matches
`f8071d5d-95c6-493d-bd1f-17c5c720e5a2`, the same session the transcript
export at `~/Downloads/session-export-1788017810958/` is from, so they're
independent confirmation of what that transcript contains, from a different
angle (distilled feedback rather than raw tool calls).

### TagKit: compose via bases, not imperative application
To have Tag A also confer Tag B, declare B as a **base** of A
(`class MyTag(Pretag, Pretag2): ...`) — TagKit applies bases first, in
declaration order. Applying a Tag imperatively from inside an `Imprint` on
the *same* target raises `TagCompositionError` (it works fine on a
*different* target — the two are different mechanisms). Prefer
`grants=SomeTag` spliced into the bases; write prerequisites against the
*capability* (`requires=Pact_Weapon`), not the specific thing that granted
it. Reserve imperative/deferred application for Tags chosen at runtime that
can't exist at class-creation time (an Origin feat picked per character).

### Species descriptions are identity, never mechanics restated
A species/background description must never narrate the traits already
printed as their own entries below it — that's duplication dressed as
flavour. It states the people's core drive (what moves them, what a player
could build a character out of), not their stat block in prose.

### A trait's inspiration line: taught/gifted/bestowed, never blood
Every species trait's one-sentence lead-in must frame the trait as
*transmitted* (learnt, gifted, bestowed, awakened, answered a call) — never
as something a people simply *has* by blood. This guards specifically
against **moral** determinism (courage, cunning, temperament, worth are
never innate); **physical** facts (darkvision, size, a breath weapon) may
still be stated as plainly inherited. Naming the source as a myth-figure or
title ("the Frost Fathers") over a taxonomy entry invites a bigger world
without resolving it on the sheet.

### An upgrade feature actualizes its parent — one number, one owner
A feature that resizes a pool another feature already prints (more
Superiority Dice, a bigger crit range, more Rage uses) states only what it
*changed* and stops. The live, resolved number stays in the single parent
entry that owns it — never spelled out as a total in the upgrade (goes
stale) and never re-derived live in both places (the two numbers will
eventually visibly contradict each other). The upgrade gets no flavour line
of its own; the parent already named the fantasy.

### Generated sheets omit player choices — the generator already chose
Rules text describing an election the player would make at level-up
("whenever you gain a level, you can replace one of these...") never
appears on a generated sheet, because in a generator that election already
happened, invisibly, in a Dice Bag. A standing condition (not an election)
still belongs on the sheet. Known inconsistent at last check: Warlock's
invocation-swap clause and Druid's known-form swap were still printing this
kind of text — those are lines to remove, not precedents to copy forward.

### Every module is its own API (Ada `.ads`/`.adb`, generalized)
Julio's general, cross-project design criterion: treat every module as if it
were its own API. A module's opening docstring is its **spec** — what it
owns, what it exposes, how callers use it (the `.ads`); the implementation
below is the **body**, free to change (the `.adb`). Public surface stays
explicit and minimal (`_`-prefixed = private = disposable); public aliases
are encouraged, used liberally; import contracts stay stable across
refactors (a moved symbol keeps a re-export at its old path) so consumers
never notice the move.

---

*Written by Claude (Sonnet 5) mid-recovery, alongside a confirmed-safe fix to
`AtlasEpica/Map_of_Stories.py` (see that file's own doc-comment) and
`Documenta/Questae/Open/QST-0076` (proposing a sweep for the same bug
pattern across the rest of the vault). Not claiming GuildKit/SpeciesKit/
Training — no memory of that code, only of what it was supposed to satisfy.*
