# QST-0031 — Redesign the spell system with TOP

- **Type:** tagkit / design
- **Priority:** 🟠 high
- **Status:** Open — diagnosis only (do not patch piecemeal)
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Contracts Consul (Warlock), Simplicity Consul (Monk), Testing Consul (Rogue), Lorekeeper
- **Parent:** —
- **Sidequests:** QST-0031.1 (SpellsKit — **Working**), QST-0031.2 (retire SPELL_DATA_2024 → Spell()), QST-0031.3 (apply Tags, dedupe the Lodge), QST-0031.4 (spell test suite), QST-0031.5 (`Spell.__format__`), QST-0031.6 (verify every definition)
- **Related:** QST-0016 (Character root, TOP flagship), QST-0020 (Features → TOP, sibling redesign), `Canon/TagKit-Doctrine.md`, `Canon/Conventions.md`

---

## 🔍 Diagnosis (what & where)
`AtlasMagia/Lodge_of_Spells.py` (5,284 lines) carries **two parallel, divergent representations of the same domain**:

1. `SPELL_DATA_2024` — a hand-maintained dict of 139 spells, each with a complete `definition`.
2. Hundreds of standalone `Spell(...)` constructor calls, one **re-declared per class/subclass spell list** — the same conceptual spell (e.g. "Misty Step") is built from scratch independently in the Wizard list, the Sorcerer list, the Warlock list, etc., with no shared identity between them.

This is a direct violation of TagKit Doctrine rule 3 ("One source of truth per type — shared types come from a single `Compass_of_*`"). It was live evidence, not theory: filling in missing spell descriptions (see QST-0026 lineage) required patching the **same** spell's text at 2–5+ separate call sites, because there is no single object that *is* "Misty Step" — only that many independent copies of it.

Discovered live, while doing that work: 463 `Spell(...)` call sites carried **no definition at all** (237 unique spell names), because the duplication makes it easy for one copy to get the fix and the others not to.

## 🎯 Desired outcome
One canonical `Spell` per name. Class/subclass membership, school, and casting tradition are **Tags** applied to that one object — not re-declarations of it. `Lodge_of_Spells.py` becomes what its own name already promises (per `Canon/Conventions.md`'s `Lodge_of_X` = "curated, closed sets"): a flat, closed *registry* of fully-defined `Spell` instances, with all classification logic living in the Tags, not in which list an object happens to sit in.

## 🧭 Notes for the Agora / implementer
- This is a whole-file redesign — **do not patch piecemeal.** Sequence per sidequest; each is independently reviewable.
- Uses **TagKit itself** (the real upstream, `github.com/JulTob/Tag_Oriented_Programming`, already pinned in `requirements.txt`) — not a local reimplementation of Tags.
- `AtlasTOP` was removed as unsanctioned bloat (Decree 0002 / QST-0018) — there is currently **no live TOP usage anywhere in this codebase**. This redesign would be the first real one. Worth being deliberate/exemplary about it, since whatever pattern lands here is likely the template QST-0016/QST-0020 (Character root, Features) will be compared against.
- Unlike QST-0020 (Features), this does **not** need to wait on the Character root (QST-0016) — a spell's Tags (school, class list, tradition) classify the spell itself; nothing here requires a Character to exist first. Can proceed independently and in parallel.
- **Naming: settled by Julio directly in Canon.** `Canon/Conventions.md` now defines `XKit` — "TOP implementation of a specific class and related Tags" — with `SpellsKit` listed as its own example, alongside `ClassKit`/`InvocationKit` for the same treatment elsewhere (QST-0020's Features redesign should reuse this pattern too, once it proceeds). Canon also adds `Tools_of_X` ("Context interfaces", example `Tools_of_Loader`) as where AtlasVenustas' `Kit_of_*` presentation modules are headed — so `XKit` (TOP) and `Kit_of_X`/`Tools_of_X` (presentation) no longer share a lane at all. No rename cascade forced by this Quest.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Architecture Consul (Druid): Two parallel representations of one domain is textbook rot — pick one, and let structure (Tags) carry what today lives in *which list you're in*.
> Contracts Consul (Warlock): Restricting the new Tags to `Spell` targets is a real obligation — use TagKit's own `Expectation` contract for it (QST-0031.1), not a hand-rolled `assert`.
> Simplicity Consul (Monk): One `Spell`, many Tags. The 463-site duplication this quest exists to kill is exactly the growth tax TOP is for.
> Testing Consul (Rogue): First real test suite in the repo rides along with this (QST-0031.4) — good moment to start, while the data model is being rebuilt anyway.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `needs a Dialog` (design shape), sidequests `build` once shape is confirmed
