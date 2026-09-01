# QST-0082 — Recovered source is still only on disk

- **Type:** recovery / chore
- **Priority:** 🔴 urgent
- **Status:** Working
- **Owner:** Cursor (Grok) — this session (18:15 2026-08-31)
- **Route to:** Julio, Paladin (Safety), Artificer (Workshop)
- **Parent:** QST-0072
- **Sidequests:** QST-0082.1 · QST-0082.2
- **Related:** REW-0001 · QST-0052 · Dialog 0009 · Dialog 0010 · `$S/RECOVERY-COORD.md`

---

## 🔍 Diagnosis (what & where)

The 2026-08-29 wipe is not the current loss window. Julio lifted recovery
rule 4 at 08:24 on 2026-08-31. Cleric voice landed on `main` as `59c792d`.
Everything restored *after* that — SpeciesKit bodies, training maps,
AlignmentKit, ActorLudi Alusoris, Grimoire_of_Guilds, app shims, InvocationKit,
general feats, epic boons — still lives only in the working tree.

`git status` at 18:15: **145 tracked files dirty**, ~30k insertions, plus
untracked recovered modules (`Grimoire_of_NPC.py`, RaceKit, Alusoris maps)
and the entire `.recovery-vault/` (747 `.pyc`). `main` is 30 commits ahead
of `origin/remove-npc-gen` (wrong upstream tracking), not pushed as this
tree.

A `git restore` / Finder copy / session end will repeat 08-29, this time
with no second bytecode chance for the reconstructed `.py`.

## 🧾 Evidence

- `$S/RECOVERY-COORD.md` log lines from 11:40 through 18:15 all say
  **Not committing**.
- REW-0001: for authored text, the gap between written and committed *is*
  the loss. Reconstructed source is the same class of object once the pyc
  has been transcribed.
- Backup ref from the 02:32 Grok session: `refs/backup/recovery-20260831-grok-session`
  (`d0cda34`). This session adds `refs/backup/recovery-20260831-1815-grok`
  (`d23a7d7`, 1618 files, Finder ` 2.py` excluded).

## 🎯 Desired outcome

Julio says whether to commit the recovered source onto `main` (or a recovery
branch) *without* the Finder ` 2.py` copies and without the 914-file staged
dump (`e2440dec`). The vault `.pyc` files are evidence and should ride with
that commit (`.gitignore` already un-ignores `.recovery-vault/`).

## 🧭 Notes for the Agora / implementer

Do not `git add -A`. Exclude `* 2.py` / `* 2.md`. Stay off FighterKit,
WarlockKit, live BackgroundKit, Map_of_Gear_Titles unless those diffs are
reviewed owner-by-owner.

The backup ref does **not** move `main`. It is the QST-0080 pattern until
Julio commits.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Recovery agent (Grok): The pyc lane on this checkout is empty of live
> bootstraps. The remaining failure is git, not marshal.
> Safety Consul (Paladin): A backup ref is cheaper than another tar.gz.
> Lorekeeper: REW-0001 already named this. Apply it to reconstructed source,
> not only to Cleric prose.

**Weighting:** reach 3 × severity 3 = **9** · council leaning: `build` (Julio's commit)
