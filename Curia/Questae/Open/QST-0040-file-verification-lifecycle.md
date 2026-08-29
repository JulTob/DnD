# QST-0040 — Adopt the file verification lifecycle (the Rubrics)

- **Type:** rule-update / docs
- **Priority:** 🟠 high
- **Status:** Open — rule recorded in Documenta; rollout & ratification are Julio's
- **Owner:** unclaimed
- **Route to:** Safety Consul (Paladin), Methods Consul, Readability Consul, Architecture Consul (Druid)
- **Parent:** —
- **Sidequests:** —
- **Related:** `Documenta/Verification-Lifecycle.md` · Modus-Operandi.md · Single-Source-of-Truth.md · QST-0039

---

## 🔍 Diagnosis (what & where)
Structural work currently lands on **one agent's word** — there is no verification
gate between "an agent wrote it" and "the project trusts it." Julio's new rule
(2026-08-29): every structural change is marked 🟡 by its author, verified by a
**second** agent (🟢) or flagged for revision (🔴, opening a Questa), and only then
confirmed by Julio (⚪️); files scheduled for rework are ⚫️. The rubric lives in
the file's docstring.

## 🧾 Evidence
- Julio's instruction (2026-08-29), recorded in `Documenta/Verification-Lifecycle.md`.
- Modus-Operandi already forbids "turning a report into a fait accompli"; this rule
  gives that principle teeth for files, with a second-agent check before Julio's word.

## 🎯 Desired outcome
Every file declares its trust state in its docstring; no 🟢 without a second
agent; no ⚪️ without Julio; every 🔴 opens a tracking Questa. The scheme is
documented in Documenta and cross-referenced from the process Canon.

## 🧭 Notes for the Agora / implementer — needs Julio's word
- **Docstring placement.** Python: module docstring (before `from __future__`);
  Markdown: `Status:` line under the H1. (Open question for Julio: should rubrics
  ever apply *below* file level — per function/class — or is file-level the rule?)
- **"Second agent" mechanism.** A review/compliance subagent, or another working
  agent — never the author. Tie into `Agentia/` (a verifier envoy?) — open a
  Dialog if it needs its own charter.
- **Rollout scope.** New/edited files carry rubrics immediately. Retro-labelling
  the existing tree is a separate, optional sweep (could ride QST-0017's orphan
  sweep) — decide whether/when.
- **Status change ≠ content edit** (or verification would loop). Stated in the doc.
- **Where the rule is *ruled*.** Recorded in Documenta now; if it should also be a
  process-Canon rule (Modus-Operandi) or a Decree, Julio decides.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Safety Consul (Paladin): A second set of eyes before trust is the whole of
> defense-in-depth. 🔴-opens-a-Questa means a flaw is never silently swallowed —
> the same law as "never fail silently," now applied to our own work.
> Methods Consul: The state machine is small and total — every file is in exactly
> one rubric, and every transition is named. That is a contract, not a vibe.
> Readability Consul (Barbarian): One colored mark in the docstring tells the next
> reader "trust me / check me / rework me" at a glance. Flavor (the Rubrics) that
> pays its way in clarity.
> Architecture Consul (Druid): Keep the mechanism cheap — a line of text, not a
> database. If it grows a tool later, that is a Questa, not a prerequisite.

**Weighting:** reach 3 × severity 3 = **9** · council leaning: `needs a Dialog`
*(Reach: every file in the project. Severity: it governs what we are allowed to
trust — correctness/process, not cosmetic.)*
