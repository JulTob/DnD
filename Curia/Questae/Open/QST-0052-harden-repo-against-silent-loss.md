# QST-0052 — 🟠 Harden the repo against silent loss

- **Type:** chore / infrastructure (prevention)
- **Priority:** 🟠 high — *do after the tree boots and a recovery checkpoint is committed; these stop the next accident, they do not fix this one*
- **Status:** Open — proposals converged in Agora Dialog 0009, awaiting Julio to adopt (as a Decree) and prioritize
- **Owner:** unclaimed
- **Route to:** Artificer (Workshop), Paladin (Safety), Rogue (Testing), Druid (Architecture), Julio
- **Parent:** —
- **Sidequests:** may split per item if any one runs long
- **Related:** Agora Dialog 0009 (the diagnosis) · QST-0072 (recovery ledger) · QST-0051 (the TagKit-pin regression this would have caught)

---

## Diagnosis

The 2026-08-29 accident (see Dialog 0009) was cheap to cause: uncommitted work erased by a restore to an old Git state, plus four footguns. The guards below are each small and independent. Adopt as a standing Decree.

## Desired outcome — seven guards

- [ ] **1. Checkpoint-before-destroy (recovery/migration branches).** A WIP commit is mandatory before any tree-altering Git command (`reset`, `restore`, `checkout <old>`, bulk revert), even when the tree is broken. A red commit is recoverable; an unsaved tree is not.
- [ ] **2. Pre-reset safety anchor.** Before a destructive Git verb: `git tag safety/pre-<op>-<YYYYMMDD-HHMM> HEAD` and capture the tree with `git stash create` (record the ref). Turns "gone" into "labeled."
- [ ] **3. Ignore scratch.** `.gitignore` `$S/`, `.recovery-vault/`, and `$*` literal-variable directories; move real scratch to an absolute path outside the repo. (`$S/` is currently *tracked* — remove it from the index as part of this.)
- [ ] **4. Pin-bump gate.** After any dependency re-pin (TagKit especially), the affected Kits' self-tests must pass before the pin stands. QST-0051 is the case this would have caught: TagKit `0.2.0a1` reserved `__contains__` and broke the Character/Role foundation unnoticed.
- [ ] **5. Loss detector.** A Make target / pre-commit check that flags any tracked `.py` that is near-empty while its `.pyc` is substantially larger, or that shrank > ~80% versus `HEAD`. The accident's "source truncated, bytecode intact" signature would have tripped it.
- [ ] **6. Boot-and-generate smoke gate.** One Make target: import the beta player root (`app.main` / `shiny_app`) and summon one Player (and one NonPlayer when in scope). "Done" for recovery = this passes, not "the file looks restored." (QST-0072 lists it; promote it to the acceptance definition.)
- [ ] **7. One module home.** Consolidate the duplicate trees (`AtlasLusoris/` vs `AtlasActorLudi/`, incl. the two differing `CharactersKit.py`) to a single home; make the other a shim or delete it, so a fix never has to be applied twice.

## Notes for the implementer

- Items 1, 2, 3, 7 are one-time or policy. Items 4, 5, 6 are small scripts (Make targets or `.git/hooks/pre-commit`), git-hook-friendly, no new dependencies.
- Keep it stdlib / shell: a `pre-commit` hook plus two or three Make targets covers 3–6.
- This questa is prevention only. It must not compete for attention with QST-0072 / QST-0049 / QST-0050.* until the tree boots and the recovery checkpoint is committed.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —
