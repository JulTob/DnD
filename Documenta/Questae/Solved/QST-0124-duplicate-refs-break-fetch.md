# QST-0124 — Finder duplicates of ref files break every fetch

- **Type:** chore / tooling
- **Priority:** 🟠 high
- **Status:** Solved
- **Owner:** Claude
- **Route to:** Julio
- **Parent:** —
- **Sidequests:** —
- **Related:** Decree 0008 · QST-0052 (the pre-commit Finder-duplicate refusal) · `scripts/git-hooks/pre-push`

---

## 🔍 Diagnosis (what & where)

macOS copied two remote-tracking ref files as `name 2`:

- `refs/remotes/origin/Julio_Cl/focused-hopper-d2xxs9 2`
- `refs/remotes/origin/Julio_Cl/funny-gauss-movzis 2`

Git cannot read a ref whose name contains a space. One such file is enough to
make every `git fetch` fail, even `git fetch origin main` with a narrowed
negotiation tip, because the connectivity check walks every ref:

```txt
fatal: bad object refs/remotes/origin/Julio_Cl/focused-hopper-d2xxs9 2
error: https://github.com/JulTob/GenLegend.git did not send all necessary objects
```

`main` could not be brought up to date, so no questa branch could start from it.

The two copies were not the same case. The first was identical to its original.
The second pointed at `172401d` ("The Paladin says the oath out loud") while its
original pointed at `3cb8e9a`, so deleting it blindly could have dropped the only
name for a commit.

A second defect in the same area: `scripts/install-git-hooks.sh` wrote to
`${ROOT}/.git/hooks`, which does not exist inside a worktree, where `.git` is a
file.

## 🧾 Evidence

Every fetch from a session worktree failed on 2026-09-14 with the error above,
while `origin/main` on GitHub had moved from `34992b6` to `cf14ec4`.

## 🎯 Desired outcome

A duplicated ref file never blocks a fetch for long, and repairing it never
loses a pointer.

## 🧭 Notes for the Agora / implementer

No decision needed: this repairs the tooling Decree 0008 already sets up.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** Julio, in chat, 2026-09-14 ("can you fix those files with a pre-push?")
- **What changed:**
  - `scripts/repair-duplicate-refs.sh` finds ref files named `name N` in the
    common git dir. An identical copy is removed. A copy that points elsewhere is
    kept under `refs/salvage/duplicate-refs/` (local, never pushed) and then
    removed. A copy that points at no object is removed. It can be run by hand.
  - `pre-push` runs it before the fast-forward check and the smoke.
  - `install-git-hooks.sh` installs into the common git dir, so it works from a
    worktree.
  - Run once on the repository: `focused-hopper-d2xxs9 2` removed (identical);
    `funny-gauss-movzis 2` kept as
    `refs/salvage/duplicate-refs/remotes/origin/Julio_Cl/funny-gauss-movzis-2`.
- **Practice/preference to remember:** a Finder duplicate is repaired, never
  simply deleted: keep what it points at under a valid name first.

---

## 🏛️ Council

> Repair Consul (Cleric): Three cases, three answers, and none of them loses a commit.
> Simplicity Consul (Monk): One script a person can run by hand, called from the hook that already exists.

**Weighting:** reach ⟨3⟩ × severity ⟨2⟩ = **6** · council leaning: `build`
