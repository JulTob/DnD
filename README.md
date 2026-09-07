# D&D — Gen Legend

Tools for Dungeon Masters: generate Player Characters and NPCs, and in time a companion for building worlds. The first public product is the Player Character generator (Decree 0004).

The living handbook is [Curia/Vademecum.md](Curia/Vademecum.md). Tickets (questae) live in `Documenta/Questae/` (new) and `Curia/Questae/` (older, being merged into Documenta). Decisions live in the Agora.

## Run

```bash
make run
```

`make setup` builds `.venv` from `requirements.txt` the first time (Python 3.10+, 3.14 recommended). `make dev` reloads on edits. The server is `app.main:app`; there is no other entry point.

## Prove

```bash
make smoke-player
```

Boot and generate seed 42. `make replay-player` proves a seeded request replays exactly; `make sweep-player` builds every Guild at levels 1 and 5 (`WIDE=1` builds every level, Species, Background and Specialization and renders every sheet, about nine minutes). The pre-push hook runs the smoke.

## One line: `main`

`origin/main` on GitHub is the product. There is no other remote branch. Local `main` tracks it and is never force-moved (Decree 0008).

Every piece of work is a questa branch, fast-forwarded into `main` when its gate passes:

```bash
git fetch origin
git worktree add ~/Desktop/DnD-session-<short> origin/main
cd ~/Desktop/DnD-session-<short>
git checkout -b questa/QST-####-short-slug
```

`make install-hooks` once per clone. Older lines from the 2026 recovery are local archive tags (`archive/*`, `salvage/*`, `safepoint/*`); they are evidence, not product, and are not pushed.

## Deploy

One container, one command:

```bash
docker build --build-arg BUILD_SHA=$(git rev-parse --short HEAD) -t gen-legend .
```

`gcloud run deploy gen-legend --source . --region us-central1 --allow-unauthenticated` builds the same Dockerfile on Cloud Run.
