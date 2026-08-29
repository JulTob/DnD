# QST-0039 — Decrees are rules, not resolutions: reconstitute the principle canon

- **Type:** rule-update / docs
- **Priority:** 🟠 high
- **Status:** Open — diagnosis + correction plan; every Canon/Decree edit is Julio's to ratify
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Methods Consul, Readability Consul, Simplicity Consul
- **Parent:** —
- **Sidequests:** (thrown only on Julio's go) .1 README/template · .2 extract Modus-Operandi principles into individual principle-Decrees (with examples & patterns) · .3 distil old resolution-Decrees 0001–0003 into that set, resolutions → their Questae · .4 Modus-Operandi → process-law + pointers · .5 numbering/provenance of the reordered Decree series
- **Related:** Decree 0001 · Decree 0002 · Decree 0003 · Decrees/README.md · Modus-Operandi.md (principles list) · Code-Style.md · Single-Source-of-Truth.md · QST-0004 · QST-0016 · QST-0038

---

## 🔍 Diagnosis (what & where)
A **Decree is an abstract design principle — reusable wisdom, a rule** (Julio,
2026-08-29). Records of *solved issues* live in `Questae/Solved/`; a Decree keeps
the **principle** so we never re-ask a settled question. Two entangled problems:

1. **Decrees are written as resolutions, not rules.** Root cause: the
   `Decrees/README.md` template prescribes a decision-record ("records the
   decision … alternatives not chosen … **Consequences**: new Questae opened").
   The writer followed it faithfully — a **misprint to correct**, not history to
   erase (the resolution memory already lives in the Questae).
2. **The principles are scattered and duplicated.** `Modus-Operandi.md` lists the
   principles as terse bullets, *and* the same wisdom is re-derived inside the
   resolution-Decrees (0002/0003). A principle should be stated **once**, as a
   Decree, and referenced — the Unification rule applied to the Canon itself.

## 🧾 Evidence
- `Decrees/README.md` template: `## Decision` / `## Alternatives not chosen` /
  `## Consequences (Questae opened)` — a decision-record, not a principle.
- `Modus-Operandi.md` → "principles the Council speaks from": Contract
  orientation, Clear models, Top-down/one-step, Modularity & separation,
  Readability & dumbness, Safety & error discipline, Anti-bloat — a bullet list.
- `Decree 0002`/`0003` re-derive several of those inline (derive-don't-store;
  one-pipeline-not-two; observe-vs-retry; never-fail-silently).

## 🎯 Desired outcome
- Every Decree reads as a **timeless rule**: `Principle / Why it holds / How it
  applies (examples & established patterns) / First taught by`.
- The **principle canon** = one Decree per principle, sourced from the
  Modus-Operandi list and the durable wisdom distilled out of Decrees 0001–0003;
  each carries concrete examples and established patterns.
- `Modus-Operandi.md` keeps only the **process law** (prime rule, working loop,
  forbids, free) and **points to** the principle-Decrees.
- Old resolution content (venv unify, Character/Dice refactor, Minion/logging
  rework) is **linked, not copied**, to its Questa (`QST-0004`, `QST-0016`, etc.).

## 🧭 Notes for the Agora / implementer — needs Julio's word per edit
Open decisions to settle before drafting the set:
- **MO/Decree boundary.** Confirm process stays in `Modus-Operandi.md`; principles
  move to Decrees; MO references them.
- **The principle list.** Candidate set above. Consolidation calls for Julio:
  is **Anti-bloat** one coin with **No Duplicated Efforts**, or two Decrees?
  Does **Derive-Don't-Store** get its own Decree (and a name that avoids clashing
  with the governance file `Single-Source-of-Truth.md`)?
- **Numbering/provenance.** Fresh principle series vs. renumber in place. Existing
  refs point at "Decree 0001/0002/0003" (`.gitignore` comment, several QSTs), so
  renumbering has a citation cost; alternative is to mark old resolution-Decrees
  "distilled → principle-Decree NNNN + Questa" and keep the numbers as redirects.

Land no Canon/Decree edit without Julio's ratifying word. Draft each for review
first (`Modus-Operandi.md`; `Single-Source-of-Truth.md` govern).

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Architecture Consul (Druid): State each principle once, as law, and let Consuls
> and Decrees cite it. A principle re-typed in three places is three places to
> drift — the very fault the Unification rule names.
> Methods Consul: Fix the template first (root cause), then the principles have a
> correct mould to be cast in. Order matters.
> Readability Consul (Barbarian): "Examples & established patterns" is the gift to
> the next reader — a rule with a worked example teaches; a bare rule preaches.
> Simplicity Consul: Net text *drops*: resolutions return to their quests, the
> bullet list becomes real Decrees. More weight per line, less to maintain.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `needs a Dialog`
*(Reach: the form of every Decree and the home of every principle. Severity:
Canon clarity and how the project remembers its wisdom — not cosmetic.)*
