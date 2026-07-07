# QST-0004 — Review, clean & unify the venvs into one

- **Type:** chore/cleanup
- **Priority:** 🟠 high
- **Status:** Open — decisions ruled, execution awaiting go/no-go
- **Owner:** unclaimed
- **Route to:** Workshop Consul (Artificer), Ecosystem Consul (Ranger), Safety Consul (Paladin)
- **Parent:** —
- **Sidequests:** —
- **Related:** Decree 0001 (venv arbitration), QST-0003 (Flask→Shiny), QST-0009 (fallback shim)

---

## 🔍 Diagnosis (what & where)
**Seven** committed virtualenvs, across three Python versions and two machines, bury the real source and carry stale/duplicate dependencies:

| Env path | Python | Machine |
|----------|--------|---------|
| `.venv/` | 3.14.3 | this one (`/Users/tbs`) |
| `env/` | 3.12.6 | `/Users/julio` |
| `env/venv/` | 3.12.3 | `/Users/julio` |
| `DnD/` | 3.12.3 | `/Users/julio` |
| `adventurer/` | 3.10.2 | — |
| `Avatar/venv/` | 3.12.6 | `/Users/julio` |
| `AtlasWorldBuild/venv/` | 3.12.6 | `/Users/julio` |

## 🧾 Evidence
`pyvenv.cfg` files confirm the versions/paths above; `site-packages` trees (pip, numpy, flask, shiny…) are tracked alongside project code. One `requirements.txt`; deploy via `app.yaml` (`shiny run`).

## 🎯 Desired outcome (Julio's rulings — Decree 0001)
- **One** environment: a single **`.venv/` at the repo root**, gitignored, rebuilt from `requirements.txt`.
- **Python: always the newest** — currently **3.14** (standing preference, see below).
- **Fold in** the subproject envs (`AtlasWorldBuild/`, `Avatar/`) — no separate environments.
- A `.gitignore` excludes all venvs, `__pycache__`, build artifacts, editor state.

## 🧭 Standing preference to add to Canon (Julio to ratify)
> **Always target the newest stable Python.** Environments and CI track the latest release; dependencies are upgraded to follow. *(Draft for `Canon/` — Julio ratifies.)*

## 🗺️ Runbook (to run on Julio's Mac after go-ahead)
1. `.gitignore` added at repo root (done — non-destructive).
2. Remove the seven env directories from the working tree (destructive — **awaiting go/no-go**): `.venv env DnD adventurer Avatar/venv AtlasWorldBuild/venv env/venv`.
3. On the Mac: `python3.14 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` (regenerate `requirements.txt` first if it's Flask-era — coordinate with QST-0003).
4. Verify `shiny run shiny_app.py` boots against the new env.

## ✅ Resolution
*(pending execution — decisions ruled by Julio via Decree 0001; deletion awaits explicit go/no-go)*

---

## 🏛️ Council
> Workshop Consul (Artificer): One `.venv/` at root, gitignored, rebuilt from a lockfile — this is the standard workshop. The six strays are pure debt.
> Ecosystem Consul (Ranger): Fold the subprojects; I'll verify `AtlasWorldBuild`/`Avatar` don't need pinned-different deps before we drop their envs. Newest Python is fine *if* Shiny + numpy already ship 3.14 wheels — I'll check, else we pin one notch back.
> Safety Consul (Paladin): Before any delete, confirm no bespoke file hides inside a venv folder and no secret sits in a stray `.env`. Deletion is recoverable via git history, but confirm first — as the Canon requires.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `build` (execute on Julio's go/no-go)
