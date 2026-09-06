# QST-0087 — One door: land the pending work and make `app.main` the entry point

- **Type:** chore/cleanup · design
- **Priority:** 🔴 urgent
- **Status:** Working
- **Owner:** Claude (worktree `top-paradigm-status-plan-d41970`, branch `questa/QST-0087-one-door-land-pending-work`), started 2026-09-06 on Julio's word
- **Route to:** Safety (Paladin) · Architecture (Druid) · Workshop (Artificer) · Julio
- **Parent:** QST-0001
- **Sidequests:** —
- **Related:** REW-0001 · Decree 0004 · Decree 0006 · Decree 0007 · Decree 0008 · QST-0027 · QST-0073 · QST-0074 · QST-0016.6.1 · QST-0088 · Codex's QST-0084 (folded here, see below)

> Minted under `Documenta/` by Julio's direction (2026-09-06): `Documenta` is the
> coordination folder; `Curia/` is the older name and will be merged into it.

---

## 🔍 Diagnosis (what & where)

Two worktrees carry the most valuable pending work in the repository, and none of it is in history.

**Main checkout (`/Users/tbs/Desktop/DnD`, branch `main`), 13 modified files:**

- the launcher switch: `Makefile`, `app.py`, `app.yaml`, `run_shiny.sh`, `scripts/run_shiny_preview.sh`, `scripts/run_app_catch_errors.py`, `app/__init__.py` all point at `app.main:app`; `shiny_app.py` (1,233 lines) becomes an 8-line compatibility shim; `Curia/Current-State.md` says so;
- `app/shell.py` wires `eldritch_head_tags` into the head (the monolith had it, the modular shell did not);
- `app/components/character_sheet.py` flattens the Species section: description, extra Origin Feat and features render under the Species heading without their own sub-branches, and the self-test follows;
- prose: `AtlasActorLudi/SpeciesKit/Humans.py` (docstring plus "our people" first-person voice in the description, one word trimmed) and `AtlasLusoris/Map_of_Cleric_Prayers.py` (one paragraph of the Cleric description rewritten).

**Recovery worktree (`/Users/tbs/Desktop/DnD-recovery-player-composition`, branch `recovery/player-composition`, three commits behind `main`, none ahead):**

- `AtlasActorLudi/Map_of_Character_Generation.py`: `summon_player` no longer retries five fresh seeds on failure; a request either replays its seed or raises;
- `AtlasActorLudi/Tools_of_Legacy_RNG.py`: `Isolated_Legacy_RNG` now seeds and restores both stdlib `random` and the `app.random` singleton under a lock;
- `scripts/verify_player_replay.py`: the seeded-replay integration rite;
- three questae: QST-0016.6.1 (replay contract), QST-0085 (Fighter precondition), QST-0084 (composition boundary).

The recovery worktree's two source files were not touched by the three commits it is behind, so its diff applies to `main` cleanly.

## 🧾 Evidence

- `git -C /Users/tbs/Desktop/DnD status --short`: 13 `M` entries, plus eight untracked third-party books under `Documenta/Sources/` (about 510 MB) that must never be staged.
- `git -C /Users/tbs/Desktop/DnD-recovery-player-composition status --short`: 2 `M`, 4 `??`.
- Seeded replay on `main` before this work: Human Fighter Soldier L1 seed 42 twice gives the same name but 8 of 42 attributes differ (`skills`, `saving_throws`, `features`, `languages`, `attack_rolls`). The dual-RNG quarantine is the fix.
- REW-0001: for authored text, the gap between written and committed *is* the loss. Both trees are that gap today.
- Codex's QST-0084 (written 2026-09-02 in the recovery worktree) diagnosed the two composition roots and asked for `app.main:app` as the import-safe Player-only door. Its blocker (`alusoris_page_ui` called with three arguments) is already fixed on `main` (`2b44b2a`). Julio ruled on 2026-09-06: **one entry point, `app/` as the modular folder.** That ruling closes QST-0084's question; its remaining sidequest (launcher convergence) is this questa. QST-0084's file is not carried over because its id collides with `Documenta/Questae/Open/QST-0084-unhide-npc-generator.md`.
- Codex's QST-0085 (Fighter `target in Character`) is carried over as **QST-0088** for the same reason.

## 🎯 Desired outcome

1. Every pending change from both worktrees is in `main`'s history as reviewed commits, split so each commit has one purpose (Decree 0007).
2. `app.main:app` is the only entry point; `shiny_app.py` is a shim that imports it; every launcher, the deploy file and the preview script agree.
3. A seeded Player request replays exactly (`scripts/verify_player_replay.py` green).
4. The two other worktrees hold nothing that is not in history, and are retired (Decree 0008: close before you open).
5. Nothing from `Documenta/Sources/*.pdf|*.epub` enters the index; a `.gitignore` line makes that permanent.

## 🧭 Notes for the Agora / implementer

- The retry removal is a behaviour change: a request that fails now raises to the page instead of silently handing the user a different seed. That is the honest contract (Decree 0007), but until QST-0088 (Fighter L5) and the Monk/Ranger `random` import are fixed, two of the 78 sweep cells surface as errors. Julio decides whether those fixes ride separate questae immediately after this one, or whether the retry stays until they land.
- The prose edits (Humans, Cleric) and the sheet flattening are Julio's voice and presentation calls; they land in their own commit only on his word.
- Do not `git add -A` anywhere. Stage by path.
- Landing mechanics: commits are made on this questa branch in the `top-paradigm-status-plan` worktree; `main` fast-forwards from `/Users/tbs/Desktop/DnD` only after a backup ref of that checkout's dirty tree exists (`git stash create` → `refs/backup/…`, the QST-0080 pattern), then its working tree is reset to the new `main`. The recovery worktree and branch are removed once their diff is empty against `main`.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** Julio, 2026-09-06 ("one entry point, app as a modular folder")
- **What changed:** *(commits listed as they land)*
- **Practice/preference to remember:** *(pending)*

---

## 🏛️ Council

> Safety Consul (Paladin): Two dirty trees and one accident behind us. Bank first, argue about commit boundaries second; a red WIP commit is recoverable and an unsaved tree is not.
> Architecture Consul (Druid): The composition root is the one file that may not lie. With `app.main` the door, `shiny_app.py` must be a shim and nothing else, or the monolith grows back in the dark.
> Workshop Consul (Artificer): Every launcher names the same target, or the next hand that types "run" boots a ghost. Makefile, `app.py`, `app.yaml`, the two scripts: one string.
> Contracts Consul (Warlock): The replay verifier is the promise the share link makes. It rides with the RNG quarantine in the same commit, so the fix and its proof travel together.

**Weighting:** reach 3 × severity 3 = **9** · council leaning: `build`
