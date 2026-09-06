# QST-0088 — Fighter specialization rejects the Character Target

- **Type:** bug / tagkit
- **Priority:** 🔴 urgent
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** TagKit (Druid) · Contracts (Warlock) · Methods (Wizard)
- **Parent:** QST-0016.6.1
- **Sidequests:** —
- **Related:** Decree 0002 · Decree 0007 · QST-0016.6

---

## 🔍 Diagnosis (what & where)

A strict randomized Player sweep can select Fighter → Battle Master and then
fails while applying a maneuver Tag.  Its `Character_Only` precondition tests
membership against the `Character` type rather than the canonical Character
Target / TagKit field, producing a `TypeError` that TagKit reports as a
`TagPreconditionError`.

Normal generation may conceal this by retrying with a different seed.  That
makes a valid Player choice appear intermittent and violates the public seeded
request contract.

## 🧾 Evidence

- `scripts/verify_equipment.py` with `STRICT_GENERATION=1` fails during its
  first seed sweep.
- Call path: `summon_player` → `New_Player` → `Apply_Specialization` →
  `Apply_Battle_Master_Choices` → maneuver Tag precondition.
- The failing expression is `target in Character` in
  `AtlasLusoris/AtlasOfGuilds/FighterKit.py`, where `Character` is a type, not
  a container or TagKit Field.

## 🎯 Desired outcome

A valid Fighter specialization applies only to canonical Player Characters and
uses the native TagKit membership/contract vocabulary.  Strict generation
reports no precondition type error, and the repair is covered by a focused
Fighter regression plus the Player sweep.

## 🧭 Notes for the Agora / implementer

- Inspect the existing `CharactersKit` Target and pinned TagKit contract API
  before changing the predicate.
- Do not weaken or delete the precondition; express its real obligation with
  the correct semantic membership relation.
- Do not address retry behavior here; QST-0016.6.1 owns that public request
  contract.

---

## ✅ Resolution (filled when Solved)

- **Decided by:** pending
- **What changed:** pending
- **Practice/preference to remember:** a TagKit contract must name a Field or
  semantic Tag, never use Python containment against a Target type.

---

## 🏛️ Council

> TagKit Consul (Druid): The contract is right to protect the maneuver Tag;
> the relation has been expressed against the wrong kind of object.

> Contracts Consul (Warlock): A precondition that throws `TypeError` cannot
> communicate its domain obligation.  Keep the guard and make it truthful.

**Weighting:** reach 2 × severity 3 = **6** · council leaning: `build`
