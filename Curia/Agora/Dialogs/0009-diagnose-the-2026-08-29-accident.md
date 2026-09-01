# Dialog 0009 — Diagnose the 2026-08-29 accident (beyond recovery)

- **Question:** Why did a large amount of work vanish on 2026-08-29, and what standing changes stop it recurring?
- **Raised by:** Julio (via the returning Claude session)
- **Related Questae:** QST-0072 (recovery ledger) · QST-0049 · QST-0050.* · QST-0051 (TagKit-resync regression) · QST-0052 (hardening, minted from this dialog)
- **Consuls called:** Architecture (Druid), Safety (Paladin), Methods (Wizard), Contracts (Warlock), Workshop (Artificer), Testing (Rogue), Simplicity (Monk), Lorekeeper
- **Status:** 🟡 open — awaiting Julio's decision

---

## 🧭 Framing

The recovery itself is tracked elsewhere (QST-0072 and the live board `$S/RECOVERY-COORD.md`). This dialog is only about the *causes and the prevention*: what made the loss possible, and what standing rule or guard makes the same mistake cheap next time instead of catastrophic. Evidence gathered this session:

- Git history is **intact**; reflog, stash, and the one dangling commit hold nothing from the lost span. The loss was **uncommitted working-tree work**, erased when the tree was restored to an **old (Flask-era) Git state**. `.pyc` bytecode survived, which is the only reason recovery is possible at all.
- A directory literally named **`$S/`** is tracked in the repo, full of forensic scripts. It is an unexpanded shell variable (a scratch path like `$SCRATCH` that never expanded) that got written into and then committed.
- Several source files came back **truncated to junk while their `.pyc` was intact** (per the board and QST-0072), meaning a bulk write or editor operation zeroed sources without touching bytecode.
- **TagKit was re-pinned mid-recovery** (to `0.2.0a1 @c7bd376`) without migrating consumers, which silently broke the Character/Role foundation (QST-0051).
- Two divergent module trees coexist (`AtlasLusoris/` and `AtlasActorLudi/`), including two differing `CharactersKit.py`.

Out of scope: the per-file restorations themselves.

---

## 🗣️ Deliberation
*Each Consul argues from their lens and ends with a concrete proposal.*

Architecture Consul (Druid): Name the single point of failure plainly: **advancement lived only in the working tree.** One `git restore`/`reset`/checkout to an old state, and months of it were gone because Git had never been told about it. Everything else is a contributing factor. The standing fix is not "be careful", it is "the working tree is never the only copy." Proposal: on any recovery or migration branch, a **checkpoint commit is mandatory before any tree-altering Git command**, even if the tree is broken. A red WIP commit is recoverable; an unsaved tree is not.

Safety Consul (Paladin): And guard the dangerous verbs. The accident verb was a restore to an old ref. Proposal: a **pre-reset safety tag** — before `reset --hard`, `restore`, `checkout <old>`, or a bulk revert, stamp `git tag safety/pre-<op>-<date> HEAD` and `git stash create` the tree into a ref. Cheap, and it turns "gone" into "tagged." Never run a destructive Git command on this project without leaving a labeled anchor first.

Methods Consul (Wizard): The `$S/` directory is a textbook footgun and it is still tracked. A quoted-nothing variable expanded to the literal string `$S`, tools wrote there, and Git happily versioned it. Proposal: **`.gitignore` `$S/`, `.recovery-vault/`, and any `$*` literal**, and move real scratch to an absolute path outside the repo. Scratch that can be committed is a trap.

Contracts Consul (Warlock): The mid-recovery TagKit re-pin is the quiet one. A dependency contract changed under the foundation (managed `__contains__`), and nothing caught it until self-tests were run by hand this session (QST-0051). Proposal: **a dependency pin is a gated change** — after any bump, run the Kit self-tests as an acceptance gate before the pin is allowed to stand. Doctrine already says pins move deliberately; make the gate real.

Workshop Consul (Artificer): The "source truncated, `.pyc` intact" signature is detectable. Proposal: a **loss detector** — a small check (Make target or pre-commit hook) that flags any tracked `.py` that is near-empty while a corresponding `.pyc` is substantially larger, and any tracked `.py` that shrank by more than, say, 80% versus `HEAD`. It would have screamed during the accident instead of after.

Testing Consul (Rogue): Recovery is being judged file-by-file with no single green light. Proposal: **one boot-and-generate smoke gate** — `import app.main` (or the beta's player root) plus one Player and, when in scope, one NonPlayer summon, run from a Make target. "Done" means that gate passes, not "the file looks restored." QST-0072 already lists this; make it the acceptance definition, not a checkbox.

Simplicity Consul (Monk): Two module trees and two `CharactersKit.py` mean two futures. Every fix now has to be applied twice or it drifts. Proposal: **decide one home** (`AtlasLusoris` or `AtlasActorLudi`) and make the other an import shim or delete it, before more restoration lands on the wrong copy.

Lorekeeper (Elf Sage): The one thing that worked was the **board plus the Questae** — async, durable, survived three agents dying on token exhaustion. Keep leaning on it: live chat between agents is lost when a session ends; a Questa is not. Proposal: **every agent writes its claim and its finding to the Curia, not only to chat**, so the next cold-started agent inherits the state. This session's findings went to QST-0051 and here precisely for that reason.

Monk (closing): None of these are new frameworks. They are a commit, a tag, a `.gitignore` line, two small checks, one smoke target, and one deletion. The accident was cheap to cause; make it cheap to survive.

---

## ✅ Convergence check
- [x] Every called Consul has spoken.
- [x] Every objection answered (no dissent: the proposals are independent and additive).
- [x] Concrete proposals on the table (collected into QST-0052).

---

## 🕊️ Vox report

Vox: The loss had **one root cause** (advancement existed only in the uncommitted working tree, erased by a restore to an old Git state) and **four contributing footguns** (a committed literal `$S/` scratch dir; a bulk operation that truncated sources while `.pyc` survived; a mid-recovery TagKit re-pin that broke the foundation unnoticed; and two divergent module trees). The council converged with no dissent on seven cheap, standing guards: (1) mandatory checkpoint commit before any tree-altering Git command on recovery/migration branches; (2) a pre-reset safety tag + stash-create; (3) `.gitignore` for `$S/`, `.recovery-vault/`, and `$*` literals, scratch moved outside the repo; (4) Kit self-tests as an acceptance gate after any dependency pin bump; (5) a loss detector for `.py` truncated-vs-`.pyc` or shrunk-vs-`HEAD`; (6) one boot-and-generate smoke gate as the definition of "done"; (7) consolidate the duplicate module trees to one home. All seven are tracked in **QST-0052**.

→ Awaiting Julio's decision. To be recorded as a Decree if adopted.
