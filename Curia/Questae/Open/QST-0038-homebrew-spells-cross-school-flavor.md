# QST-0038 — Homebrew spells that play in the seams between schools

- **Type:** design / question
- **Priority:** 🟢 low  *(flavor-forward, no system blocked on it)*
- **Status:** Open — idea capture, awaiting an Agora evaluation when Julio calls for it
- **Owner:** unclaimed
- **Route to:** Lorekeeper, Understanding Consul (Bard), Contracts Consul (Warlock)
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0031.1 (SpellsKit — where `School.Single_School` lives), QST-0031.6 (the HB purge that emptied the Lodge of homebrew)

---

## 🔍 Diagnosis (what & where)
SpellsKit enforces **one school per spell** (`School.Single_School`, a `@Pre` contract) — accurate to RAW, and Julio's own verdict while ratifying it: *"accurate to RAW but quite absurd"* at the edges. Is a shield of fire Abjuration or Evocation? The fuzziness at the seams is not a modeling failure — it's design space. Julio's sketches, captured verbatim in spirit:

- **Enchanting ice** — a freeze that leaves the target *suggestible* while frozen (Enchantment ↔ Evocation/Transmutation).
- **Divination of the past through bones** — scry a person's history through their remains (Divination ↔ Necromancy).
- **Stone into statue, statue into summons** — transmute stone to a creature's likeness and swap places with the real one (Transmutation ↔ Conjuration).

All homebrew was deliberately purged from the Lodge (2026-07-15, QST-0031.6's notes) — this Quest is the sanctioned door for it to come back *designed*, not smuggled.

## 🎯 Desired outcome
An evaluated batch of homebrew spells whose *flavor* deliberately crosses school boundaries — reflavored thematically, as Julio put it — each still **mechanically assigned one school** (the contract stands; the crossing lives in the prose, the name, and the effect's dressing). Each spell arrives with full rules text, clearly marked as homebrew (per QST-0031.6's practice note: never indistinguishable from published material), tagged through SpellsKit like any other spell.

## 🧭 Notes for the Agora / implementer
- **The Single_School contract is not the enemy here** — the cited examples all *have* a defensible primary school; the cross-school identity is flavor. If a design genuinely cannot pick one school, that's the moment to reopen the contract question with a concrete case in hand, not before.
- Wait for QST-0031.2/.3 to land first — homebrew entering a half-migrated Lodge doubles the migration surface for no gain.
- The (HB) marker convention from the purge stays: homebrew is always visibly homebrew.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Lorekeeper (Elf Sage): The schools were always a taxonomy of convenience — the Weave doesn't file paperwork. Flavor that crosses the lines while the mechanics stay filed is exactly how the good supplements do it.
> Understanding Consul (Bard): Capture the three sketches now, design them later — an idea written down survives; an idea "for later" evaporates.
> Contracts Consul (Warlock): One school per spell holds until a concrete design breaks it honestly. Then we renegotiate the pact with the case in front of us — not speculatively.

**Weighting:** reach 1 × severity 1 = **1** · council leaning: `defer` (by design — Julio summons it when ready)
