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

- [x] **1. Checkpoint-before-destroy (recovery/migration branches).** Documented in Decree 0008; `make safepoint` implements the rolling anchor.
- [x] **2. Pre-reset safety anchor.** `scripts/safepoint.sh` tags `safepoint/latest` + dated tag + optional stash ref.
- [x] **3. Ignore scratch.** `.gitignore` adds `$S/`, `* 2.py`, `* 2.md`, `.safepoint/`. Untrack `$S/` from index: follow-up chore when recovery tree is triaged.
- [ ] **4. Pin-bump gate.** After any dependency re-pin (TagKit especially), the affected Kits' self-tests must pass before the pin stands. QST-0051 is the case this would have caught: TagKit `0.2.0a1` reserved `__contains__` and broke the Character/Role foundation unnoticed.
- [x] **5. Loss detector.** `scripts/loss_detector.py` + `make loss-check`; runs from `pre-commit` on staged `.py`.
- [x] **6. Boot-and-generate smoke gate.** `make smoke-player`; runs from `pre-push` and is required before questa commits (Decree 0008).
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
