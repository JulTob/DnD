# QST-0036 — TagKit-Doctrine.md names contract primitives the pinned TagKit does not export

- **Type:** docs
- **Priority:** 🟡 normal
- **Status:** Open — diagnosis only
- **Owner:** unclaimed
- **Route to:** Lorekeeper, Contracts Consul (Warlock), Understanding Consul (Bard)
- **Parent:** —
- **Sidequests:** —
- **Related:** `Canon/TagKit-Doctrine.md`, QST-0031.1 (where the drift surfaced), QST-0019 item 5, QST-0006

---

## 🔍 Diagnosis (what & where)
`Canon/TagKit-Doctrine.md` rule 5 prescribes contract primitives by name: "`Expectation` (must hold before applying), `Condition` (must hold after), `Exclusion` (no invalid siblings), `Final`/`Sealed` where extension must stop." **None of those five names exist in the pinned TagKit** (v0.1.0, commit `c7bd376` per `requirements.txt`). Verified against the installed source (`TagKit/__init__.py` + `TagKit.py`, grep-confirmed zero occurrences): the real primitives are `@Precondition`/`@Pre` (before-apply predicate → `TagPreconditionError` + atomic rollback), `@Postcondition`/`@Post` (after-apply → `TagPostconditionError` + rollback, re-checked by `bool(agent)`), and the `Contract` namespace (`Contract.Preconditions/Postconditions/Conditions/Status/Display`). There is no exclusion primitive and no finality primitive; exclusivity is expressed as a Precondition (as QST-0031.1's `School.Single_School` now demonstrates in live code).

Rule 4's "composition modes" vocabulary (Augmentation/Extension/Mutation) also doesn't match the source's own terms (`@Underlay` extension, `TagOverwriteWarning` on independent replacement, `@Delete`) — same drift, softer form.

## 🧾 Evidence
Surfaced 2026-07-15 while building SpellsKit (QST-0031.1): the quest's Desired-outcome was written from the Doctrine and specified an `Expectation` contract; consulting the pinned source per that same quest's instructions revealed the name doesn't exist. Any implementer who trusts the Doctrine's vocabulary writes code that fails on import.

## 🎯 Desired outcome
The Doctrine's rules 4–5 speak the pinned commit's actual language (or explicitly mark aspirational/upstream-proposal vocabulary as such). Canon is read-only to agents — the fix is Julio's edit or a ratified update, not a drive-by patch.

## 🧭 Notes for the Agora / implementer
- QST-0019 item 5 already notes Underlay/Conditions doctrine "awaits settled upstream text" — this Quest is the concrete instance of that gap, now with a live-code counterexample to write from (SpellsKit).
- If the old names are *intended future TagKit API*, the right move per the Doctrine itself is a `tagkit-upstream` questa ("Suggest to TagKit: Expectation/Exclusion"), not local vocabulary that doesn't run.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Lorekeeper (Elf Sage): Canon that misquotes its own scripture breeds heresy in good faith — every future implementer will copy the wrong names from the most authoritative page we have.
> Contracts Consul (Warlock): The primitives that DO exist are strictly stronger than the prose suggests — atomic rollback on a failed Pre is a better promise than "must hold before applying". Document the real pact.
> Understanding Consul (Bard): Keep one line noting the aspirational names if Julio still wants them upstream — history of intent matters — but flagged as proposal, not API.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `build` (Julio's edit; agents don't touch Canon)
