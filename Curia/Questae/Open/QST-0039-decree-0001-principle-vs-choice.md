# QST-0039 — Decree 0001 conflates principle with choice: name the unification principle

- **Type:** rule-update / docs
- **Priority:** 🟠 high
- **Status:** Open — diagnosis only; the restatement is Julio's to ratify
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Methods Consul, Readability Consul, Simplicity Consul
- **Parent:** —
- **Sidequests:** —
- **Related:** Decree 0001 (venv arbitration) · Decree 0002 (no parallel skeleton) · Decree 0003 (one logging pipeline) · QST-0004 · QST-0038 · Code-Style.md (anti-bloat)

---

## 🔍 Diagnosis (what & where)
`Decree 0001` states its venv ruling as a **choice** — "unify the virtualenvs into
**one**." Julio's correction: that is not the principle. The principle is **"no
duplicated efforts"**; a single `.venv` is only *one application* of it. A Decree
should record the **design principle**, from which the concrete choice follows —
not the choice dressed as law.

The principle is already load-bearing across the Canon, but it is never named as
a principle — only re-derived locally each time:
- `Decree 0002`: one `Character` root; "refactor existing, never a parallel
  skeleton"; RNG unified into the Dice; `AtlasTOP` removed as a parallel layer.
- `Decree 0003`: "one logging pipeline … not two parallel systems (that would
  recreate the duplication we just cleared)."
- `Code-Style.md` (anti-bloat): "Delete before adding"; "never build a parallel
  codebase beside the one with the problem."

It has **no seat in the principles list** (`Modus-Operandi.md` → "principles the
Council speaks from"), even though that list is explicitly expandable and
Julio-ratified.

## 🧾 Evidence
- `Decree 0001` §2: "review, clean, and unify the virtualenvs into **one** —
  surfacing every conflict for Julio's decision." (choice-shaped; defers version)
- `Modus-Operandi.md`: "This list is expandable. When a new principle earns its
  place, Julio ratifies it here."
- The three Decrees + Code-Style quotes above all *apply* the same unnamed rule.

## 🎯 Desired outcome
"No duplicated efforts" (unification) sits **where principles live** (Canon), and
Decree 0001's venv section is **restated as an application** of it — without
losing Decree 0001's still-valid diagnostic-sweep method (part 1) and without
erasing settled memory (Decrees are kept forever).

## 🧭 Notes for the Agora / implementer — needs a Dialog
Two candidate shapes for the restatement (Julio picks; I draft the exact text):

- **Shape A — Canon principle + amend Decree 0001.** Add a "Unification / no
  duplicated efforts" seat to `Modus-Operandi.md`'s principles list; add a
  **Restated (2026-08-29)** note to Decree 0001 §2 reframing "one venv" as an
  *application* of the principle. Smallest footprint; keeps history in place.
- **Shape B — Canon principle + new Decree 0004.** Same Canon edit, plus a new
  Decree that *generalizes* the principle and explicitly notes it already governs
  Decrees 0001/0002/0003; Decree 0001 §2 gains a pointer. More ceremony, but the
  principle gets a first-class home and a clean provenance.

**Unification patterns Julio named to include** (as guidance, not mandates):
diamond modules (one shared dependency at the base of a diamond, depended on by
many, converging again), functional design, layering by abstraction. A git-like
mental model fits: store one canonical thing, reference it from many, **merge
diamonds instead of copying**.

**Also correct the record:** earlier agent notes (and `QST-0038`) implied
Decree 0001 *mandates* Python 3.14 + one venv. The Decree defers the version to
Julio; "3.14" is a standing preference from `QST-0004` / `.python-version`, not
ratified law. `QST-0038` wording corrected accordingly.

Do **not** overwrite Decree 0001 wholesale (its part-1 sweep method stands), and
do **not** land any Canon edit without Julio's ratifying word.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Architecture Consul (Druid): A principle names the *why*; a choice is a *what*.
> Decree 0001 froze a what. Lift the why into the principles list and every future
> Decree inherits it — the venv, the one root, the one log pipeline all become the
> same sentence spoken thrice.
> Methods Consul: Diamond over fork. Two modules that need the same thing should
> depend *down* onto one shared base, not each grow a copy — that is "no
> duplicated efforts" in code, and it is testable: count the definitions, there
> should be one.
> Readability Consul (Barbarian): Say it plainly so the next reader needs no
> archaeology — "we do a thing once, in one place, and point at it." Keep the
> flavor, but the meaning must survive a tired maintainer at midnight.
> Simplicity Consul: Anti-bloat and no-duplication are the same coin. Naming the
> principle lets us reject a parallel layer by *citing law*, not taste.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `needs a Dialog`
*(Reach: a founding principle touching every Atlas and every future Decree.
Severity: Canon clarity and how decisions are framed — not cosmetic.)*
