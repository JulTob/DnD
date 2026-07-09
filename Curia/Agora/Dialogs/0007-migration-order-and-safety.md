# Dialog 0007 — The migration: in what order, and how nothing breaks

- **Question (Q-0010):** Decree 0002 rules *what* the Character root is. In what **order** do QST-0027 and QST-0016.1–.6 land, and what **safety rail** guarantees the app works after every single step?
- **Raised by:** Julio ("How could we do that without breaking the app in every step?")
- **Related Questae:** QST-0016 (.1–.6) · QST-0027 · QST-0023
- **Consuls called:** Safety (Paladin), Architecture (Druid), Simplicity (Monk), Contracts (Cleric), Methods (Wizard)
- **Status:** 🟡 open — deliberating point by point **with Julio in chat** (per Canon/Modus-Operandi.md)

---

## 🧭 Framing

The destination is decreed; the road is not. Constraints from Canon and Julio:
the app must boot and generate after **every** step (no big-bang); we refactor
existing files, never build parallel ones; steps are small, shown, and
confirmed one at a time; contract orientation and clear models lead.

## 🗣️ Deliberation

*(recorded here as each point is raised with Julio in chat; his rulings drive
the next point)*

**Ground truth checked before speaking (2026-07-09):** `shiny_app.py` is 1265
lines. `build_character_sheet` (261-427) + `build_npc_sheet` (427-818) alone
span ~560 lines, over 40% of the file. `server()` (818-1213) is the second
mass. No `tests/` harness exists yet — QST-0016.6's diagnosis confirmed by
direct check, not assumption. The working tree also carries 8 files of
**unrelated, uncommitted** changes (Title/Name work, `AtlasActorLudi`
scores/saves, CSS) sitting alongside the two Grimoires this quest will touch.

> **Safety Consul (Paladin):** My principle is safety — a rail that exists
> *before* the first cut, not one promised for later. Two things follow:
> 1. **QST-0016.6 (the golden-master net) cannot be the last sidequest run —
>    it must be the first thing built**, before QST-0027 makes its first
>    move. "Behavior-neutral" is currently an assertion no one can check
>    automatically; even a small, deterministic rite (fixed-seed PC + fixed-
>    seed NPC, sheets rendered to text, diffed byte-for-byte) turns every
>    later step from "looks right" into "is right." This is cheap to build now
>    precisely because the root isn't touched yet — Character/NPC still exist
>    as today's two classes, so the rite has a stable target to snapshot
>    *before* anything moves.
> 2. **The uncommitted tree is a hazard to this quest, not to me to resolve.**
>    Refactor diffs are unreadable mixed with unrelated feature work, and a
>    bad step can't be isolated or reverted cleanly. I don't touch it — that's
>    your call — but I name it as a precondition question before the first
>    move.
>
> **Open questions for Julio:**
> - Do we build the golden-master rite (QST-0016.6) *first*, ahead of
>   QST-0027, as the safety rail the rest of the quest runs under?
> - What should happen to the 8 uncommitted files before refactor work
>   starts — commit them separately, stash, or are they fine to carry
>   alongside?

## ✅ Convergence check
- [ ] Every called Consul has spoken.
- [ ] Objections answered.
- [ ] An ordered plan with its safety rail, ready for Julio's decree.
