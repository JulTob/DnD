# QST-0076 — Gear blurb self-test expects a folded AC the doctrine forbids

- **Type:** bug / question
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Workshop, Architecture
- **Parent:** QST-0072
- **Sidequests:** —
- **Related:** QST-0046 · Decree 0006

---

## 🔍 Diagnosis (what & where)

`AtlasInventarium/Map_of_Gear_Titles._self_test` (reconstructed 2026-08-31,
bytecode-equivalent to the 2026-08-05 pyc) asserts
`"AC 18" in mail.blurb()` for a forged Splint (+1). Today the blurb reads
`"AC 17, Heavy armour. +1 AC. …"`: base and bonus stated separately, never
folded.

This is a vintage seam, not a reconstruction error: the identical bytecode in
the vault pyc fails the same way in today's tree. Either the gear modules
changed blurb composition after 2026-08-05, or the blurb intentionally stopped
folding once the Canon ruled that AC is derived at read time and never stored
(`Curia/Current-State.md`, Gear and equipment).

## 🧾 Evidence

- `verify_equiv` PASS for the module (38 names, 19 functions) against
  `Map_of_Gear_Titles.cpython-314.pyc`, followed by the assert failing at
  runtime with `AC 17, Heavy armour. +1 AC. …`.
- Character generation and the GearKit import are unaffected.

## 🎯 Desired outcome

Julio rules which behavior is canon: a folded display total in blurbs, or the
current base-plus-bonus wording. The losing side (the assert, or the blurb)
is then updated in one commit.

## 🧭 Notes for the Agora / implementer

Do not edit the assert just to make the suite green: it encodes a real design
question about how much arithmetic a blurb performs for the reader.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Workshop Consul (Artificer): A blurb that folds the total does the reader's
> sum; a blurb that lists the parts shows its work. Both are defensible: only
> one is canon, and the test must agree with the canon, not enforce a memory.

**Weighting:** reach 1 × severity 2 = **2** · council leaning: `needs a Dialog`
