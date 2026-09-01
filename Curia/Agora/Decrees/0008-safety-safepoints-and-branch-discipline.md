# Decree 0008 — Safety first, safepoints, and branch discipline

- **Ratified by:** Julio, in chat, 2026-09-01
- **Recorded by:** Cursor, same day
- **Status:** active
- **Source:** Dialog 0010 · QST-0052 · QST-0083 · Julio's direction to cure the illness, not rename it
- **Supersedes:** the temporary "use `origin/product` as the real main" workaround in QST-0083

---

## Decision

The project runs on **one tip: `main`**. That ref is the working Player generator line.
Recovery debris, Finder duplicates, and session scratch do not share its index.

Three layers enforce this — **doctrine**, **process**, and **mechanics** — in that order.
Markdown alone failed in August 2026; mechanics now back the law.

### 1. Safepoints (the safebox, not autosave)

We do not keep a constant save file. We keep **one rolling safepoint**: the last
known-good commit, tagged and recoverable.

- **`make safepoint`** (or `scripts/safepoint.sh`) moves `safepoint/latest` to
  `HEAD` and records the ref locally. Run it before any tree-altering Git verb
  (`reset`, `restore`, bulk revert, `checkout` of an old ref).
- Optional dated tags `safepoint/YYYYMMDD-HHMM` may be added for milestones.
- Destructive Git commands **require** a safepoint no older than the work they
  would erase, or they must create one first (QST-0052 items 1–2).
- The old 2025 Heroku line lives at **`archive/main-heroku-2025-08-07`**, not on
  `main`. Archive refs are read-only history, not the product.

### 2. Branch discipline

**Close before you open.** A subproject, session, or questa branch is not left
hanging when the next one starts.

| Scope | Branch name | Lifecycle |
|-------|-------------|-----------|
| Questa | `questa/QST-####-short-slug` | branch from `main` → implement → `make smoke-player` → commit → fast-forward merge to `main` → delete branch |
| Session / agent | `session/<short>` | own worktree under `~/Desktop/DnD-session-<short>`; merge or abandon before another session reuses the path |
| Recovery | `recovery/<topic>` | never force-moves `main`; lands only after smoke + Julio or Decree 0007 evaluation |

Rules:

- Never `git branch -f main`.
- Never `git add -A` in a tree that mixes recovery with product source.
- Never share one checkout between concurrent agent sessions.
- **`origin/main` is the product tip.** `origin/product` may track the same SHA
  during transition, then retires.

### 3. Questa workflow (branch → test → commit)

Every questa that touches code follows the same loop (Decree 0007 still applies
to *what* may land; this governs *how*):

1. `main` is current (`git fetch`, fast-forward pull).
2. `git checkout -b questa/QST-####-slug`.
3. Implement the smallest slice that closes the questa's single purpose.
4. **`make smoke-player`** must pass before commit.
5. Commit with evaluation in message or questa (Decree 0007).
6. Fast-forward merge to `main`, delete the questa branch, push `main`.
7. Move questa to `Solved/` with commit links.

Sidequests get their own branches (`questa/QST-####.N-slug`). A parent questa
is not Solved while an open sidequest branch exists.

### 4. Defensive coding and mechanical guards (QST-0052)

Adopted now, not "after recovery feels done":

| Guard | Mechanism |
|-------|-----------|
| Mass staging | `pre-commit` refuses >80 staged paths |
| Finder poison | `.gitignore` `* 2.py`, `* 2.md`; hook refuses if staged |
| Scratch dirs | `.gitignore` `$S/`; scratch outside repo |
| Silent truncation | `scripts/loss_detector.py` on staged `.py` |
| Boot gate | `make smoke-player` |
| Dangerous shell | Cursor `beforeShellExecution` hook blocks `-f main`, `reset --hard`, blind `add -A` |
| Hooks installed | `make install-hooks` copies `scripts/git-hooks/*` into `.git/hooks/` |

Item 7 of QST-0052 (one module home) remains open — a Decree cannot merge
`AtlasAlusoris/` and `AtlasActorLudi/` in one step.

---

## Reasoning

The August 2026 accidents (truncated source, 914-file staged dump, Grok recovery
junk on the wrong ref) shared one cause: **honor-system process on a shared,
dirty checkout with no Git refusal.**

Renaming the tip `product` changed which remote got hit; it did not stop the
verbs. Long-term health requires `main` to mean the generator **and** hooks that
make the dangerous verbs loud.

Safepoints replace anxiety-driven constant commits: one recoverable box, refreshed
at intentional boundaries, is enough.

Branch-per-questa keeps every change scoped, testable, and mergeable — the same
discipline Julio asked for when closing subprojects before opening new ones.

---

## Alternatives not chosen

- **Keep `product` as the canonical ref forever.** Rejected — two names trained
  agents to treat `main` as stale and invited the next collision.
- **Merge `origin/main` history into the generator line.** Rejected — unrelated
  2025 Heroku fork; archive tag preserves it without polluting product history.
- **Hooks only, no Decree.** Rejected — mechanics without written law drift when
  hooks are skipped or a new agent ignores `.git/hooks`.

---

## Consequences

- QST-0083 resolves: `main` repointed; `product` is transitional.
- QST-0052 items 1–6 have landing targets in `Makefile`, `scripts/`, hooks.
- Agents: read this Decree + Decree 0007 before any commit; run
  `make install-hooks` once per clone.
- Julio: change GitHub default branch to `main` after the repoint push lands
  (Settings → Branches).
