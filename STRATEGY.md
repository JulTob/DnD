---
name: Gen Legend
last_updated: 2026-08-31
---

# Gen Legend Strategy

## Target problem

A table needs a legendary Player Character now — species, class, background, a sheet you can read and a link you can send — without waiting on a DM toolbox.

## Our approach

Ship one product: the Player Character generator. Park NPC, DM, and dungeon chrome in the tree. Perfect that one path before opening the next.

## Who it's for

**Primary:** the player (and the friend who hosts) — they're hiring Gen Legend to roll a 2024 Character they can show at the table.

## Key metrics

- **Player generate succeeds** — `summon_player` for a seed plus each selectable Guild; measured in the venv, then on the live Home button
- **Sheet is readable** — Julio's live-run sign-off on Home → Generate → sheet (QST-0001 / QST-0002)
- **Shareable Character URL** — reopen the same Character from the hash; already built, must stay green
- **No false Guilds** — the picker must not offer a class the generator cannot build (Artificer: QST-0050.2)

## Tracks

### Player generator

The only first-publish track: Home tablet, Character button, sheet, share link.

_Why it serves the approach:_ this is the product.

### Player correctness

Guilds, species, backgrounds, feats, and names that actually build a Character.

_Why it serves the approach:_ a pretty front over a crashing Artificer is not a ship.

### Presentation

Venustas sheet, type, and share chrome — QST-0002 and the remaining QST-0001 acceptance.

_Why it serves the approach:_ first users judge the sheet, not the Atlas.

## Milestones

- **First publish** — Player-only front; generate + sheet + share. Date when Julio accepts the live run.

## Not working on

- NPC generator, NPC list, DM Companion, dungeons, Epica (parked; restore via `PLAYER_ONLY_PUBLISH`)
- Merging live `AtlasAlusoris/` with `AtlasActorLudi/AtlasAlusoris/` (QST-0081.5)
- Finder ` 2.py` copies (QST-0081.3)

## Marketing

**One-liner:** Gen Legend rolls a legendary D&D Character — and gives you the sheet and the link.
