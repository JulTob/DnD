# 👑 Single Source of Truth

> This file is **Canon**. Agents and assistants **read** it. They do **not** edit it. Only Julio changes the Canon.

## The first law

**Julio is the single source of truth.** Every rule, preference, and final decision originates from him or is ratified by him. The Curia, the Agora, the Consuls, the Agentia — all exist to help Julio decide well and to remember what he decided. None of them may overrule him, and none may act as if they had.

## What this means in practice

- **Agents propose. The Agora deliberates. Julio decides.** No agent commits a decision to Canon or to the codebase's rules on its own authority.
- **Confirmation is required** before:
  - any non-trivial code change (new modules, refactors, interface changes, dependency changes, deletions);
  - any decision that touches rules, architecture, naming, IP, or design;
  - integrating any external content (a new D&D ruling, a design variation, a library).
- **Trivial, reversible, in-scope work** (fixing an obvious typo inside an already-approved Questa, formatting to the Code-Style) may proceed without a fresh confirmation, *if* it is already covered by an open Questa. When in doubt, ask.
- **Silence is not consent.** If Julio has not answered, the work waits. Agents may prepare and stage, but not merge.

## The chain of authority

```
                    JULIO  (single source of truth)
                      │  issues Decrees, sets Canon
                      ▼
                 The AGORA  (Consuls deliberate; Vox reports)
                      │  prepares reasoned choices
                      ▼
                The AGENTIA  (envoys: Scout, Legal, Design, Technical)
                      │  diagnose, propose, implement once approved
                      ▼
             The CODEBASE  (every tool and agent complies)
```

Any external agent framework sits at the **bottom** of this chain. It must comply with the Canon and the Decrees. It never sits above them. See `Agentia/Agents-Compliance.md`.

## The Julio-only documents

These are written and changed **only** by Julio (agents may draft *proposals* as Questae, but may not commit the change):

- everything in `Canon/`
- every ratified **Decree** in `Agora/Decrees/` (agents draft; Julio ratifies)

Agents freely create and edit: Questae, Dialog entries, Questions, and their own working notes — always subject to review.

## How to change the Canon

1. Mint a Questa proposing the change (what, why, tradeoffs).
2. If it is a real decision, take it through the Agora.
3. Vox presents to Julio.
4. **Julio edits the Canon himself**, or explicitly instructs an agent to apply an exact, quoted change.
5. A Decree records that the Canon changed and why.
