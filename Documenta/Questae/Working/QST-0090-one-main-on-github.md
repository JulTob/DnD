# QST-0090 — One `main`, on GitHub: the product line is remote, sessions start from it

- **Type:** chore/cleanup · rule-update
- **Priority:** 🔴 urgent *(Julio, 2026-09-06: "that's priority now")*
- **Status:** Working
- **Owner:** Claude (branch `questa/QST-0090-one-main-on-github`, 2026-09-06)
- **Route to:** Safety (Paladin) · Workshop (Artificer) · Lorekeeper · Julio
- **Parent:** QST-0052 (harden the repo against silent loss)
- **Sidequests:** —
- **Related:** Decree 0008 · QST-0083 · QST-0087 · REW-0001

> Minted under `Documenta/` (Julio, 2026-09-06).

---

## 🔍 Diagnosis (what & where)

The product line exists only on this machine. `origin/main` on GitHub is nine commits behind local `main` (the 2026-09-06 landing: one door, exact replay, AtlasTOP cut, the two Guild fixes). Every session that wants to work remotely, or in its own worktree from a clean start, has nothing current to start from.

The documents also describe a remote that no longer exists:

- `README.md` says GitHub's `origin/main` is "an older public copy" and that work "lives on `origin/remove-npc-gen`". The remote has had only `main` since the 2026-09-02 consolidation; the transitional lines are archive tags.
- `QST-0083` still names `origin/product` as the product tip. Decree 0008 superseded that on 2026-09-01.
- A dead `heroku` remote (Flask era, no longer authenticates) still sits in the config beside `origin`.

## 🧾 Evidence

- `git rev-list --count origin/main..main` → 9; `git ls-remote --heads origin` → `main` only.
- `git remote -v` → `heroku` and `origin`; `git ls-remote heroku` → authentication failure.
- README paragraph three, verbatim, quoted above.
- Julio, 2026-09-06: "commit the project to the github folder so we have a proper development methodology and so we can work modularly and remotely. Cleanly keep only one main."

## 🎯 Desired outcome

1. `origin/main` equals local `main`; the pre-push smoke gate runs on the push.
2. The remote carries one branch, `main`. Archive and safepoint refs stay local tags.
3. The README states the branch model in a paragraph a remote session can follow: one `main`, questa branches, own worktree, the gates.
4. The Heroku remote is gone; its history remains at `archive/main-heroku-2025-08-07`.

## 🧭 Notes for the Agora / implementer

- Never force-push `main` (Decree 0008; the pre-push hook refuses it).
- Tags are not pushed: `safepoint/*`, `archive/*`, `salvage/*` and `recovery-blob-*` are local safeboxes and evidence, not product.
- A GitHub Actions gate (compile, smoke, URL suite, replay) is the natural next step for remote work; it is its own questa, proposed to Julio with the workflow file drafted, not landed by this one.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** Julio, 2026-09-06.
- **What changed:** `origin/main` fast-forwarded to this questa's tip on 2026-09-06 through the pre-push smoke gate; the remote carries `main` only; README rewritten around the one-line model and the session start; QST-0083's `origin/product` workaround closed out; the `heroku` remote removed (history at `archive/main-heroku-2025-08-07`). No tags pushed.
- **Practice/preference to remember:** the product is a remote ref, not a checkout. A session begins with `git fetch origin` and a worktree from `origin/main`.

---

## 🏛️ Council

> Safety Consul (Paladin): Nine commits that exist on one disk are nine commits away from the next accident. Push first; the hook already runs the smoke.
> Workshop Consul (Artificer): A README that names a branch the remote does not have sends every new hand to a ghost. Fix the paragraph in the same questa as the push, or the push teaches nothing.
> Lorekeeper (Elf Sage): Keep the archive tags local and named; they are the memory of the recovery, not a second product line.

**Weighting:** reach 3 × severity 3 = **9** · council leaning: `build`
