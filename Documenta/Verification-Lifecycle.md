# 🎨 The Rubrics — the verification lifecycle of every file

Status: 🟢 verified by an independent review agent (2026-08-29) — awaiting Julio's ⚪️ confirmation.

> A *rubric* is a colored mark a scribe adds to a page to say what state it is in.
> Here, every file carries one in its docstring. It is the project's promise that
> **no structural work stands on one agent's word alone.**

## The rule

**Every structural work must be verified by another agent.** When a file is
written, rewritten, or edited *at all*, the authoring agent marks it **🟡**. A
**different** agent then verifies it — **🟢** if sound, or **🔴** if it needs
revision (which opens a Questa). Only after a file is 🟢 may **Julio** review it
and confirm it **⚪️**. This is the single source of truth for "is this file
trusted?" — one agent proposes, a second agent checks, Julio confirms.

## The five rubrics

| Rubric | State | Meaning | Set by |
|--------|-------|---------|--------|
| 🟡 | **Yellow** | Written/rewritten/edited; **unverified**. | the authoring agent, on any edit |
| 🟢 | **Green** | Verified sound by a **second** agent (not the author). | the verifying agent |
| 🔴 | **Red** | Verifier found problems — **revision required**; a Questa is opened. | the verifying agent |
| ⚪️ | **White** | Julio reviewed a 🟢 file and **confirmed it good**. | Julio only |
| ⚫️ | **Black** | **Marked for refactoring** — known to need rework. | any agent or Julio |

## The lifecycle

```
                 (any edit)
   any state ───────────────▶ 🟡  unverified
                               │
              second agent ────┤
                    verifies   │
                    ┌──────────┴───────────┐
                 sound                   flawed
                    │                       │
                    ▼                       ▼
                   🟢  verified           🔴  revision required
                    │                       │  └─▶ open a Questa (QST-####)
        Julio confirms                      │
                    │                 author reworks
                    ▼                       │
                   ⚪️  confirmed good        ▼
                    │                       🟡  (re-enters verification)
              (any edit)                    
                    └──────────▶ 🟡

   any state ──(scheduled for refactor)──▶ ⚫️  black
   ⚫️ ──(refactor written)──▶ 🟡  (re-enters verification)
```

Two invariants:
- **An edit invalidates trust.** Editing a 🟢 or ⚪️ file resets it to 🟡 — the
  verification described its *old* content.
- **Changing only the Status rubric is not a content edit.** Moving 🟡→🟢→⚪️ is
  the act of verification itself; it never resets the state (that would loop).

## Where the rubric lives

In the file's **docstring** (its own words about itself):

- **Python** — the module docstring, first statement in the file (before
  `from __future__ import …`).
  ```python
  """Map_of_Races — race weights and lookups.

  Status: 🟢 verified by <agent> on 2026-08-29.
  """
  from __future__ import annotations
  ```
- **Markdown / docs** — a `Status:` line directly under the H1 title (as this
  file does).

Format: `Status: <rubric> <state word> — <short provenance>`. Keep provenance
light: who acted and when, and the `QST-####` when 🔴 or ⚫️.

## What counts as "structural work"

Creating or rewriting a file; adding or removing a function, class, or module;
non-trivial edits that change behavior or shape. **Not** structural: fixing a
typo, updating this Status line, or reformatting whitespace — though when in
doubt, mark 🟡; a needless verification is cheap, an unverified change is not.

## Who the "second agent" is

Any agent that is **not the author** of the change: a review subagent, a
compliance agent, or another working agent. The verifier reads the file against
the Canon (`Curia/Canon/`) and the file's own contract, then sets 🟢 or 🔴. A 🔴
**must** name the defect and open a Questa so the fix is tracked, never lost.

---

*Recorded in `Documenta` per Julio's instruction (2026-08-29). This lifecycle is
itself subject to the rubrics: authored 🟡, verified 🟢 by an independent agent,
now awaiting Julio's ⚪️ confirmation.*
