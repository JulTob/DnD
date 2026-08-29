# QST-0039 — Arcane / Divine / Primal as a character axis: the origin of their power

- **Type:** tagkit / design
- **Priority:** 🟡 normal
- **Status:** Open — design capture, sequence with the Character root work
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Lorekeeper, Understanding Consul (Bard), Contracts Consul (Warlock)
- **Parent:** QST-0016 (Character root flagship)
- **Sidequests:** —
- **Related:** QST-0031.1 (SpellsKit's `Tradition` family — the model to mirror), QST-0035 (TagKit rollout sequence), QST-0020 (Features TOP)

---

## 🔍 Diagnosis (what & where)
SpellsKit's `Tradition` family (Arcane / Divine / Primal, the One D&D playtest grouping) landed as spell vocabulary — and Julio's read on it (2026-07-15): *"the division… is powerful. It would make for a great model for the characters. Like the origin of their powers… it simplifies so much."* Today the codebase has no notion of where a character's power comes from: class is a string, casting stat is per-subclass logic, and NPC archetypes (Cultist, Shaman, Priest, Mage…) encode their flavor only in prose tables. A character-level Tradition Tag would give PCs **and** NPCs one queryable axis for power origin.

## 🧾 Evidence
- SpellsKit already carries the mapping seed: `TRADITION_OF_LIST` (Bard/Sorcerer/Warlock/Wizard → Arcane; Cleric/Paladin → Divine; Druid/Ranger → Primal) — a character whose class grants a list has an obvious default tradition.
- The archetype tables in `AtlasAlusoris` (Priest, Shaman, Cultist, Mage, Druid, Warlock…) map naturally onto the same three — NPCs get the axis for free once it exists.
- What it buys, concretely: flavor selection (titles, stories, senses/regions already branch on race/archetype strings today), spell-pool filtering (a Primal NPC drawing only Primal-tagged spells — the two Tradition families, spell-side and character-side, compose), and one honest answer to "why can this creature do magic."

## 🎯 Desired outcome
A `Tradition` Tag family for **characters** (PC and NPC alike), mirroring SpellsKit's shape: three concrete Tags on one root, character-only `@Pre` contract, applied at composition time from class/archetype (with a deliberate door for exceptions — a Divine-powered warlock of a god-patron, an Arcane ranger). Where it lives (its own XKit? part of the future CharacterKit/ClassKit?) is the Agora's call inside QST-0016's architecture.

## 🧭 Notes for the Agora / implementer
- **Sequence behind the Character root (QST-0016.1)** — per QST-0035's own doctrine, overlays want a stable root to attach to. This quest captures the design so it's ready the moment the root exists; it does not jump the queue.
- Non-casters need a decision, not an accident: is a plain Fighter untagged (no power origin), or is there a fourth "Martial/Mundane" answer? The UA had spell lists only; characters are a bigger domain than spells. Leave it to the Dialog.
- Keep the two Tradition families **distinct Tags** (spell-side in SpellsKit, character-side wherever characters live) even though they share names — a spell being Arcane and a character being Arcane are different predicates that happen to rhyme. The bridge is composition ("this Arcane character draws from Arcane-tagged spells"), not a shared Tag.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Architecture Consul (Druid): This is the healthiest kind of growth — a proven shape (SpellsKit's Tradition) transplanted to a second domain, after the first one took root. But behind the Character root, not before.
> Lorekeeper (Elf Sage): Arcane/Divine/Primal for characters predates the UA — 4e organized its whole class roster by power source, and it *did* simplify so much. There's precedent worth reading before the Dialog.
> Understanding Consul (Bard): "The origin of their powers" is a story hook as much as a mechanic — titles, backstories, and regions can all branch on it. That's the simplification Julio smells.
> Contracts Consul (Warlock): Two Tag families sharing three names across two hosts — say loudly, in both files, that they are cousins and not the same Tag, or someone will import the wrong one within a month.

**Weighting:** reach 3 × severity 1 = **3** · council leaning: `needs a Dialog` (inside QST-0016's design pass)
