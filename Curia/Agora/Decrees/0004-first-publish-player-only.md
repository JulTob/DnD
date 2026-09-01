# Decree 0004 — First publish is the Player Character generator

- **Ratified by:** Julio, 2026-08-31 (this session)
- **Source:** recovery close-out + Julio's first-publish cut
- **Status:** active
- **Related:** QST-0001 · QST-0002 · QST-0050.1 · QST-0050.2 · QST-0072 · QST-0082 · `STRATEGY.md`

## Decision

**The first public product is a Player Character generator.** Home, generate, sheet, and shareable Character URL. Nothing else is in the first-publish cut.

NonPlayer Characters, NPC lists, Dungeon Master Companions, dungeons, and Epica stay in the repository. They are **parked**, not deleted. Restore them later by flipping `PLAYER_ONLY_PUBLISH` in `app/publish_scope.py` (and re-showing the parked chrome). Do not merge the two Alusoris trees, and do not spend first-publish time on NPC summon, DM `bbeg` vs `dm_character`, or Finder ` 2.py` copies.

The long-term Character root (Decree 0002: one `Character`, Player and NonPlayer as Tags) is unchanged. First publish ships the **Player** face of that root. Unifying NPC onto it is work for a later cut.

## Reasoning

The vault restore recovered both Player and NonPlayer surfaces. Perfecting both at once keeps the first users waiting on forks that do not appear on the Player path (AbilityScores `character=`, dual Alusoris, Magistratum). Julio's cut: one goal, one button, one tablet face — then DM Characters, dungeons, and the rest.

A missing Guild in the picker is an honest decision. A Guild that always crashes is a bug report. Artificer is the known case (QST-0050.2).

## Alternatives not chosen

- **Ship Player + NPC together** — NPC generation is still red; the two Alusoris trees disagree. That is a second product.
- **Delete NPC / DM code** — recovery already paid for it. Park chrome; keep Atlas.
- **Hide Artificer without a record** — that is a scope call. Record it on QST-0050.2; do not silently drop a PHB Guild.

## Consequences

- Frontline chrome: Home + Character only. NPC, NPC List, and DM header buttons are `is-parked`. The home tablet shows only the Character generator; the NPC face stays in the markup, hidden.
- Navigation to `npc` / `npclist` / `dm` redirects to Home while the flag is on.
- Questae: Player-generator bugs jump the queue. NPC, DM, and Epica questae wait until after first publish unless they also break Player generate.
- Fast-publish path (ordered):
  1. This chrome park (QST-0082).
  2. Player generate stays green (seed 42 still Nikolas; sweep the selectable Guilds).
  3. QST-0050.2 — Artificer: **hide from the picker** for the cut, or implement progression. Do not ship a class that cannot build.
  4. QST-0050.1 — expertise draw that fails a slice of Characters.
  5. QST-0002 — the Character sheet reads as a sheet, not a debug dump.
  6. Live visual smoke: Home → Generate → sheet → Share link → reopen.
  7. Recovery checkpoint commit when Julio says so.

Parked until after first publish: QST-0037 (Epica / DM), QST-0041 (Magistratum), QST-0081.5–.9 (NPC/DM forks), QST-0050.4 (NPC/tests; Player summon does not pass `character=`), QST-0016's NPC-fold half, Finder duplicates (QST-0081.3).
