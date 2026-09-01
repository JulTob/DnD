# QST-0016 — Unify PC & NPC on one Character root (TOP skeleton)

- **Type:** tagkit
- **Priority:** 🔴 urgent  *(flagship / main quest — the incremental TOP design for the generator)*
- **Status:** Open — **design decreed (Decree 0002)**; refactor pending
- **Owner:** unclaimed
- **Route to:** Architecture (Druid), Contracts (Warlock), Methods (Wizard), Flow (Sorcerer), Simplicity (Monk), Understanding (Bard), Lorekeeper → **Decree 0002**
- **Parent:** —
- **Sidequests:** QST-0018 (remove AtlasTOP) · then: `.1` Character root (name/title/scores/size/tier/seed) · `.2` Dice + `Roll(D=)` · `.3` Player/Non role tags · `.4` fold AtlasAlusoris→AtlasLusoris · `.5` one sheet renderer · `.6` reproducibility tests · QST-0035 (rollout sequence)
- **Related:** TagKit (upstream, pinned in `requirements.txt`), QST-0002 & QST-0008 (one sheet), QST-0005 (Atlas split), QST-0013 (Modifier one-source), QST-0035 (TOP rollout sequence), Decree 0004

---

## 🔍 Diagnosis (what & where)
Today PC and NPC are two parallel classes — `Character` (AtlasLusoris.Grimoire_of_Characters) and `NPC` (AtlasAlusoris.Grimoire_of_NPC) — that each re-implement the same substrate (ability scores, skills, saving throws, proficiency, HP/AC, size, alignment, story). That duplication is the core design debt.

## 🎯 Desired outcome (direction set by Julio)
One **Character** root — the umbrella for every generated being — carrying the minimal shared substrate. **PC** and **NPC** diverge as **TOP role-Tags** on that root, never as parallel classes. Shared axes (Species, Class/Archetype, Background, Scores, Skills, Equipment) are Tags; role-only concerns (PC: leveling, subclass, shareable build; NPC: legendary/lair/region, plot hook, light-list mode) are role-Tags. One sheet renderer reads the composed Character.

**First publish (Decree 0004):** ship the Player face. QST-0016.4 (fold Alusoris) and NPC-only sidequests wait. Player root / Dice / sheet work may still proceed when it makes generate better.

## 🧭 The design question (in the Agora now)
**What is the minimal expression of what the generator builds, and how are the RNG + core mechanisms instantiated into the root?** See `Agora/Dialogs/0003-minimal-character-and-rng.md`. Litmus test for the whole quest: adding a PC-only feature must never touch NPC code, and vice-versa (no `if is_npc:`).

## ✅ Decreed design (Decree 0002)
- **Refactor, not rebuild.** Make the *existing* `Grimoire_of_Characters` the root; fold NPC in. No parallel skeleton.
- **Root stores:** `name` + `title` (both required), `scores`, `size`, `tier`, `seed`, **Dice**. Skills/HP/AC/PB/modifier are **computed**. Species/class/background/features = tags.
- **Dice = the RNG**, per Character, seeded: `Charlie.Roll(D=6)`. All rolls go through it; no global random. Absorbs `AtlasLudus.Map_of_Dice`.
- **PC/NPC = tags** (Player/Non). **`AtlasAlusoris` folds into `AtlasLusoris`** (QST-0005). **`AtlasTOP` removed** (QST-0018).
- **Litmus:** adding a PC-only feature must never touch NPC code, and vice-versa (no `if is_npc:`).

## 🧭 Notes
- Built on the pinned TagKit API (`Tag`, `Imprint`) directly — **not** on a local composition layer (AtlasTOP is being removed).
- Sequence: QST-0018 first (it *is* the first slice — the `kind` flag becomes the role tag), then the `.1`–`.6` sidequests above.
- **Rollout order** for cross-Atlas TOP axes → see **QST-0035** (Conditions → Species/Class/Background → Pugna → Spells/Enchantments).
- **Engineering practices (Phase 0):** nothing deleted until git can bring it back (baseline commit cited in message); one concern per commit.

## ✅ Resolution
*(pending — execute the sidequests, refactoring existing files)*

---

## 🏛️ Council
*Full deliberation lives in Dialog 0003; summary weight here.*
> Architecture Consul (Druid): The debt is real and the composition-over-inheritance fix is the right shape. This is the spine everything hangs on.
> Lorekeeper (Elf Sage): "Character" is the correct umbrella — a PC and an NPC are both characters. Concur with Julio.
> Contracts Consul (Warlock): The prize is one invariant set for one skeleton (scores valid, seed reproducible) instead of two drifting copies.

**Weighting:** reach 3 × severity 3 = **9** · council leaning: `needs a Dialog` (0003) → then staged `build`
