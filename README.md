# D&D — Gen Legend

Tools for Dungeon Masters: generate Player Characters and NPCs, and in time a companion for building worlds. The first public product is the Player Character generator (Decree 0004).

The living handbook is [Curia/Vademecum.md](Curia/Vademecum.md). Tickets (questae) live in `Documenta/Questae/` (new) and `Curia/Questae/` (older, being merged into Documenta). Decisions live in the Agora.

## One line: `main`

`origin/main` on GitHub is the product. There is no other remote branch. Local `main` tracks it and is never force-moved (Decree 0008).

Every piece of work is a questa branch, fast-forwarded into `main` when its gate passes:

```bash
git fetch origin
git worktree add ~/Desktop/DnD-session-<short> origin/main
cd ~/Desktop/DnD-session-<short>
git checkout -b questa/QST-####-short-slug
```

Before a commit: `make smoke-player`. Before a push: the pre-push hook runs it again (`make install-hooks` once per clone). The seeded-replay rite is `scripts/verify_player_replay.py`.

Older lines from the 2026 recovery are local archive tags (`archive/*`, `salvage/*`, `safepoint/*`); they are evidence, not product, and are not pushed.

## Run

```bash
./run_shiny.sh
```

The entry point is `app.main:app` (`make run`, `python app.py` and the deploy file agree). `shiny_app.py` is a compatibility shim.
