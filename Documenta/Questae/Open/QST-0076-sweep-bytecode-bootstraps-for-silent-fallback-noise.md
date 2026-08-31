# QST-0076 — Sweep `.recovery-vault` bytecode bootstraps for the silent-fallback noise pattern

- **Type:** bug / recovery
- **Priority:** 🟢 low (cosmetic — nothing here has crashed generation)
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** whoever holds a bytecode-bootstrap file when they next touch it
- **Parent:** QST-0072 (post-accident recovery)
- **Sidequests:** —
- **Related:** QST-0072 · QST-0077 (the solved first instance this sweep generalizes from) · `.recovery-vault/` (134 `.pyc` files) · `Documenta/Canon/` recovery law (transcript > bytecode > rewrite)

> **Numbering note:** minted from `codex/recovery-2026-08-29`, which only has
> Questae up to QST-0072 in its own history. `Julio_Cl/dnd-genlegend-recovery-ea160e`
> already used QST-0073–0075 for unrelated tickets (Decree 0006's scope work) on
> a branch this one hasn't merged with. Picked 0076 to dodge that collision;
> reconcile the number if it still collides at merge time.

---

## 🔍 Diagnosis (what & where)

Confirmed by direct fix, not suspicion: `AtlasEpica/Map_of_Stories.py` (a
bytecode-bootstrap file, loading compiled `.pyc` from `.recovery-vault/epica/`
per QST-0072's recovery law) carried a `Name(hero)` function that tried
`hero._name` — a private attribute the **pre-accident** Character carried —
inside a `try/except Exception as e: print(e)`, falling back to
`FullName(hero)` on every single call. The current (post-TagKit-refactor)
Character never has `._name`, so this fired, and printed, on **every**
character generated — 100% reproduction, confirmed across 19 seeds.

It never crashed anything: the fallback always ran, and `FullName(hero)`
correctly reads the current Character's public `.name`. Purely stdout noise.
Fixed by disassembling `Map_of_Stories.Name` (`dis.dis`), confirming the exact
branch taken, and patching a corrected `Name` into both the wrapper module's
namespace and the compiled body's own `__dict__` (functions compiled into the
vaulted bytecode close over the body module's globals, not the wrapper's —
patching only the wrapper is a no-op for anything the bytecode calls
internally). See the fix and its doc-comment in `Map_of_Stories.py` itself.

**The open question this Questa is for:** is this pattern — a private
pre-accident attribute (`._name`, or others shaped like it) tried first,
caught, printed, silently downgraded — repeated across the other 133 files in
`.recovery-vault`? Nobody has swept for it. Given how mechanical and
low-risk the fix was here (three lines, verified by disassembly, zero
behavior change beyond removing noise), it's a strong candidate for a fast,
low-stakes pass distinct from the real flagship recovery work (GuildKit,
SpeciesKit, Training) already claimed elsewhere.

## 🧾 Evidence

- `AtlasEpica/Map_of_Stories.py` — the fixed instance, with the disassembly
  reasoning in its own doc-comment.
- `dis.dis(module.SomeFunc)` against any bytecode-bootstrap import is enough
  to confirm or rule out the pattern per-function — no transcript or `.pyc`
  archive dig required for this specific check.

## 🎯 Desired outcome

For each bytecode-bootstrap module still in `.recovery-vault` use:
1. `grep` the module's public functions for ones with an unusually generic
   `except Exception` (disassembly shows this as a `PUSH_EXC_INFO` block
   right after the happy-path `LOAD_ATTR`/`RETURN_VALUE`) — that shape is the
   signature to look for.
2. Disassemble each candidate to confirm what's actually being tried and
   what it silently falls back to.
3. If the failing branch is *always* taken against the current Character/
   Agent shape (as here), patch the direct, correct call in — same pattern as
   `Map_of_Stories.Name` — including the `body.__dict__[...]` mirror, since
   skipping that half makes the fix a no-op for internal callers.
4. Leave alone anything where the fallback ISN'T always taken, or where the
   "broken" attribute might be real, current, and simply absent on a
   specific race/class combination — that's a different bug, not this
   pattern, and needs its own diagnosis.

## 🧭 Notes for the Agora / implementer

- Cosmetic priority — does not block Decree 0006's beta. Pick up between
  flagship recovery lanes, not instead of them.
- This is exactly the kind of narrow, mechanical, disassembly-verifiable fix
  that doesn't need the session transcript or a design decision — safe for
  whoever has a spare slice of time on a claimed file already.
- Do **not** use this Questa as license to rewrite a whole bootstrap file's
  logic from imagination. Same recovery law as QST-0072: transcript payload
  first, disassembly-confirmed correction second, never a guess.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
*(not yet convened — narrow enough it may not need one; flag if disassembly turns up something structural)*
