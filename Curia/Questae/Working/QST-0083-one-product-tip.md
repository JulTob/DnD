# QST-0083 — One product tip; sessions do not share a checkout

- **Type:** rule-update / chore
- **Priority:** 🟠 high
- **Status:** Working
- **Owner:** Cursor (this session) — remote `product` branch landed; Decree still Julio's
- **Route to:** Paladin, Artificer, Julio
- **Parent:** QST-0052
- **Sidequests:** —
- **Related:** Dialog 0009 · QST-0072 · REW-0001 · `$S/RECOVERY-COORD.md`

---

## 🔍 Diagnosis (what & where)

Several agent sessions share `/Users/tbs/Desktop/DnD`. They force-move `main`,
stage hundreds of unrelated files, and leave Finder ` 2.py` copies. The
committed working generator and the dirty recovery dump live in the same
index. `origin/main` is a 2025 line (last commit 2025-08-07); local `main`
does not share history with it. A new session cannot tell which SHA is the
product.

## 🧾 Evidence

- 2026-08-31: `main` was force-moved off `24ee174` onto `d7845b0` (empty
  reflog). Cleric voice survived only because it had been pushed to
  `origin/cleric-voice-onto-d7845b0` and `origin/codex/recovery-2026-08-29`.
- Same checkout: 914 files staged (tree `e2440dec`), vault `.pyc` mixed with
  live source. `git add -A` would have published the dump.
- `main` tracks `origin/remove-npc-gen`, not a product tip.

## 🎯 Desired outcome

1. One remote ref is **the working product**: last commit that boots the
   Player generator (`import shiny_app` + `summon_player(seed=42, level=1)`).
2. Every new session starts from that ref, in **its own worktree**.
3. `origin/main` is not force-pushed until Julio retires the 2025 line.
4. In-flight recovery stays on session branches until Julio lands it.

## 🧭 Notes for the Agora / implementer

### The product tip (in force until Julio names something else)

| Ref | SHA (2026-08-31) | What it is |
|-----|------------------|------------|
| **`origin/product`** | `59c792d` | Working Player generator + Cleric voice |
| `origin/cleric-voice-onto-d7845b0` | `59c792d` | Same commit, named for the cherry-pick |
| `origin/codex/recovery-2026-08-29` | `24ee174` | Broader recovery line (not all of it is on product) |
| `origin/main` | 2025-08-07 tip | Stale. Do not force-push. |

### Session start (every agent)

```
git fetch origin
git worktree add /Users/tbs/Desktop/DnD-session-<short> origin/product
cd /Users/tbs/Desktop/DnD-session-<short>
git checkout -b session/<short>
```

Do **not** use `/Users/tbs/Desktop/DnD` if another session already has it
checked out. That directory is the collision surface.

### Landing on the product

1. Smoke: `import shiny_app` and `summon_player(seed=42, level=1)`.
2. Julio says land.
3. Fast-forward only: `git push origin HEAD:product`
4. Never `git branch -f main`. Never `git add -A` in a dirty recovery tree.

### Still Julio's (needs a Decree)

Whether `origin/main` is retired or reset onto `product`. This questa does
not force-push `origin/main`.

---

## ✅ Resolution (filled when Solved)

- **Decided by:** Julio asked to organize sessions around a consistent main
  (2026-08-31). Remote `product` is the mechanical answer pending a Decree
  about `origin/main`.
- **What changed:** `git push origin 59c792d:refs/heads/product` (this
  session). Local `main` set to track `origin/product`.
- **Practice/preference to remember:** the checkout is not the product; a
  named remote ref is. Uncommitted trees are other people's sessions.

---

## 🏛️ Council

> Safety Consul (Paladin): Shared checkouts plus `branch -f` is how the
> Cleric voice almost left history. Worktrees are the guard, not a courtesy.
>
> Workshop Consul (Artificer): `origin/product` is a fast-forward-only tip.
> Recovery dumps stay on disk until Julio lands them, never via `add -A`.

**Weighting:** reach ⟨2⟩ × severity ⟨3⟩ = **6** · council leaning: `build`
