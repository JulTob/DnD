# QST-0039 — Refactor Modus-Operandi into principle-Decrees; delete the misinterpreted ones

- **Type:** rule-update / docs
- **Priority:** 🟠 high
- **Status:** Open — plan set; every Canon/Decree edit or deletion is Julio's to ratify
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Methods Consul, Readability Consul, Simplicity Consul
- **Parent:** —
- **Sidequests:** (thrown only on Julio's go) .1 rewrite `Decrees/README.md` template · .2 draft the principle-Decrees (one per principle) · .3 delete Decrees 0001–0003 + fix references · .4 `Modus-Operandi.md` → process-law + pointers
- **Related:** Decree 0001 · Decree 0002 · Decree 0003 · Decrees/README.md · Modus-Operandi.md · Code-Style.md · Single-Source-of-Truth.md · QST-0004 · QST-0016 · QST-0040

---

## 🔍 Diagnosis (what & where)
A **Decree is an abstract design principle — reusable wisdom, a rule** (Julio,
2026-08-29). The current Decrees are **misinterpretations**: they froze one-off
*resolutions* (unify the venvs; the Character/Dice refactor; the Minion/logging
rework) as if they were law. The root cause is the `Decrees/README.md` template,
which prescribes a decision-record. Separately, the project's **principles** live
only as a terse bullet list in `Modus-Operandi.md` and are re-derived inside those
resolution-Decrees — the very duplication the principles forbid.

## 🧾 Evidence
- `Decrees/README.md` template: `## Decision` / `## Alternatives not chosen` /
  `## Consequences (Questae opened)` — a resolution record, not a principle.
- `Modus-Operandi.md` → "principles the Council speaks from": a bullet list.
- Decrees 0001–0003 each encode codebase-specific execution + re-derived wisdom.

## 🎯 Desired outcome
- **Refactor `Modus-Operandi.md` into individual principle-Decrees** — clear design
  instructions, **no hacks, good TOP patterns**. MO keeps only the *process law*
  (prime rule, working loop, forbids, free) and **points to** the Decrees.
- **New Decree template** (design record that holds the *idea*, tied to real code):
  ```
  ## Principle        the rule, stated abstractly
  ## Why it holds     the reusable rationale
  ## How it applies   established patterns; no hacks; TOP shapes to reach for
  ## Where used       file/function identifiers where the pattern actually lives
  ## Toy examples     (optional) a minimal illustration
  ```
  (`Where used` replaces `First taught by`: a principle points at the code that
  embodies it — auditable, and it composes with the Rubrics of QST-0040.)
- **Delete the current Decrees 0001–0003** (misinterpretations). Their durable
  wisdom is re-expressed by the principle-Decrees; their resolution memory already
  lives in the Questae (`QST-0004`, `QST-0016`, the Minion/logging quest). The
  `Decrees/README.md` index keeps a short **Retired** note mapping old→new so
  citations resolve; references (`.gitignore` comment, QST cross-refs) are updated.

## 🧭 Notes for the Agora / implementer — needs Julio's word per edit/deletion
Candidate principle-Decree set (from the MO list; **anti-bloat is folded into
Unification** per Julio — "don't be redundant about not being redundant"):
1. **No Duplicated Efforts (Unification)** — *absorbs anti-bloat*: one canonical
   thing; diamond over fork; derive-don't-store; one backbone/swappable coats;
   delete before adding; refactor in place, no parallel codebase.
2. **Contract Orientation** — pre/post/invariants at the boundary; fail fast;
   observation vs behavior-change decorators; never fail silently.
3. **Clear Models** — model over script; variants as tags, not subclasses; the
   RNG *is* the Dice; build an algebra, not one solution.
4. **Top-down Design / One Line, One Step** — layers never mixed.
5. **Modularity & Separation of Concerns** — one purpose per Atlas/unit.
6. **Readability & Dumbness** — explicit over clever; no hacks; flavor never costs clarity.
7. **Safety & Error Discipline** — every error expected, handled, reported;
   idempotent retries; configure-once, concurrency-safe.

Open for Julio: is #1 the right consolidation (anti-bloat inside Unification —
yes per instruction); should derive-don't-store stay a *pattern under #1* or get
its own Decree; final ordering/numbering of the new series.

Land no Canon edit and **delete no Decree** without Julio's explicit word. Every
file touched follows the Rubrics (QST-0040): authored 🟡 → second-agent 🟢 → Julio ⚪️.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Architecture Consul (Druid): State each principle once, as a Decree, tied to the
> files that live it. `Where used` turns law into a map of the codebase — cite it,
> don't re-type it.
> Methods Consul: Delete the misread Decrees; keeping a wrong record "for memory"
> just re-teaches the error. The memory that matters is in the Questae.
> Readability Consul (Barbarian): "No hacks, TOP patterns, a toy example" — that
> is a Decree a newcomer can *act on*, not just nod at.
> Simplicity Consul: Folding anti-bloat into Unification is the principle applied
> to itself. Fewer Decrees, each heavier. Good.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `needs a Dialog`
*(Reach: the form of every Decree and the home of every principle. Severity:
Canon clarity and how the project remembers its wisdom — not cosmetic.)*
