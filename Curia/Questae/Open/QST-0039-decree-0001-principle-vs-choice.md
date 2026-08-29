# QST-0039 — Decrees are rules, not resolutions: correct the misprint

- **Type:** rule-update / docs
- **Priority:** 🟠 high
- **Status:** Open — diagnosis + correction plan; every Canon/Decree edit is Julio's to ratify
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Methods Consul, Readability Consul, Simplicity Consul
- **Parent:** —
- **Sidequests:** (to throw on Julio's go) .1 README/template · .2 Decree 0001 · .3 Decree 0002 · .4 Decree 0003
- **Related:** Decree 0001 · Decree 0002 · Decree 0003 · Decrees/README.md · QST-0004 · QST-0038 · Modus-Operandi.md (principles list)

---

## 🔍 Diagnosis (what & where)
A **Decree is an abstract design principle — reusable wisdom, a rule** (Julio,
2026-08-29). The record of a *solved issue* belongs in `Questae/Solved/`. Once a
one-off decision is made we do not keep the decision as law; we keep the
**principle** so we never have to ask again.

The current Decrees are written as **resolutions** (specific choices + their
execution for this codebase), not as rules. The **root cause is the
`Decrees/README.md` template itself**, which instructs a resolution-shaped record:
"records the decision … including the alternatives not chosen" and "**Consequences**:
new Questae opened, Canon edits, agents affected." The writer followed the
template faithfully — so this is a **misprint to correct across the board**, not
history to erase (the resolution memory already lives in the Questae).

## 🧾 Evidence
- `Decrees/README.md` template fields: `## Decision`, `## Alternatives not chosen`,
  `## Consequences` (Questae opened) — a decision-record, not a principle.
- `Decree 0001` §3: "**Begin Track A now.**"; §2 "unify the virtualenvs into one" —
  execution/choice, not rule.
- `Decree 0002`: stores `name/title/scores/size/tier/seed`, `Roll(D=6)`, the
  `AtlasAlusoris→AtlasLusoris` merge — codebase-specific resolution.
- `Decree 0003`: "console handler local / file sink deployed", "keep
  `@minion/@watcher/…`" — implementation resolution.

## 🎯 Desired outcome
Decrees read as **timeless rules**. The README/template is principle-shaped. Each
existing Decree is **distilled to the principle(s) it embodies**, linking (not
copying) the Questa that first taught it. The durable principles land where
principles live (`Modus-Operandi.md`). The **unification principle — "no
duplicated efforts"** — is named there explicitly.

## 🧭 Notes for the Agora / implementer — needs Julio's word per edit
Correction plan (sidequests, thrown only on go):
- **.1 — `Decrees/README.md` + template (root fix).** Reframe a Decree as an
  abstract rule: `## Principle` / `## Why it holds` / `## How it applies` /
  `## First taught by` (link to the Questa/Dialog; memory lives there).
- **.2 — Decree 0001.** Holds *two* principles: **no-duplicated-efforts** and
  *diagnosis discipline*. The latter already lives in `Questae/README.md` +
  `QUESTA-template.md` — so 0001 becomes the **Unification** principle; the sweep
  execution stays in QST-0004/QST-0007 (Solved as they close).
- **.3 — Decree 0002.** Distill to: model-over-script; **derive-don't-store**
  (SSOT); variants-as-tags; instance-over-global + seed-reproducibility; refactor
  in place / no parallel skeleton. Specific Character/Dice work stays in QST-0016.
- **.4 — Decree 0003.** Distill to: one backbone, swappable coats (not parallel
  systems); observation vs behavior-change; never-fail-silently / idempotent
  retries; configure-once / concurrency-safe. Minion/logging work stays in its QST.

Do **not** erase the Questae the resolutions belong to; **link** them. Land no
Canon/Decree edit without Julio's ratifying word. `Single-Source-of-Truth.md`
and `Modus-Operandi.md` govern.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Architecture Consul (Druid): A Decree should survive the problem that birthed
> it. If deleting the venv mess would make the Decree meaningless, it was a
> resolution — lift the rule out, let the record rest in the quest.
> Methods Consul: The template *taught* the error; fix the template first or the
> next scribe repeats it. Root cause over symptom.
> Readability Consul (Barbarian): One shape for all law — principle, why, how,
> and a pointer to where it was learned. A stranger should read a Decree and
> know how to act, without needing the old battle it came from.
> Simplicity Consul: This mostly *removes* text — the one-off consequences go
> back to their quests. Less law, more weight per line. Anti-bloat approves.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `needs a Dialog`
*(Reach: the form of every Decree, present and future. Severity: Canon clarity
and how the project remembers its own wisdom — not cosmetic.)*
