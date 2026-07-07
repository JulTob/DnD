# 🪶 Code Style — Light, Readable, Arcane

> **Canon.** Read, do not edit. Style here is *strict* on purpose: the codebase is meant to be an artistic masterpiece as well as correct software. Readable, light, easy to follow.

## The spirit

Code should read like a clean spell: every line earns its place, nothing is there to impress. **Clever is not a compliment.** Clear beats clever; readable beats dense; explicit beats magical; a repeated known pattern beats a new invention.

## The strict rules

### Readability first
- Names are descriptive and follow `Canon/Conventions.md`. Domain meaning must be obvious from names and structure.
- Functions stay small and focused — one responsibility. If you must scroll to understand a function, split it.
- Public functions carry a docstring: one line minimum; note args/returns/raises when not obvious.
- Type hints on public functions and non-obvious parameters.

### Lightness (anti-overengineering)
- **Do not build machinery for a problem you do not yet have.** No speculative abstraction, no configuration knobs nobody asked for, no frameworks-within-the-framework.
- Prefer the smallest thing that works and reads well. Delete before you add.
- If an abstraction does not earn its weight (used once, or as clear inline), inline it.
- A bridge/God-object that "does everything" is a smell. Split by responsibility.

### Structure discipline (one purpose per place)
> This is *why* the project uses TOP and not OOP. Guard it.
- **Each Atlas has one clear purpose.** Its name states its domain. Never a catch-all — *"let's put everything TOP-ish in a folder"* is exactly the sloppiness TOP exists to prevent. (See `AtlasTOP`, removed by Decree 0002.)
- **Refactor the existing filesystem; never build a parallel codebase on top.** Fix the file that has the problem. Do not scaffold a new shadow layer beside it. Solve issues where they live, as they arise.
- **Import TagKit; write simple, clear code.** TagKit is the engine (upstream, pinned). Our job is plain, legible domain logic on top — not a re-implementation, not a wrapper framework.
- **Agents must actively catch bloat** — an unrequested new package, a parallel abstraction, a "helper" layer nobody asked for. Flag it, name why, and prefer removal.

### Repeat patterns modularly
- New content slots in the **same way** existing content does. Consistency of shape is a feature — a maintainer should be able to predict the next file from the last.
- **TagKit patterns especially** are the default vocabulary (see `TagKit-Doctrine.md`). Reach for them before inventing new structure.

### Python practice (PEP 8 + project sense)
- `snake_case` for functions/variables, `CapWords` for classes; 4-space indent; imports ordered stdlib → third-party → local; no unused imports; no `import *` outside a documented public API.
- `with` for resources; comprehensions where they clarify; `enumerate`/`zip` over manual indexing; `isinstance` over `type ==`.
- No mutable default arguments. No bare `except`. No `eval`/`exec` on external data.
- Explicit over implicit — return `None` on purpose, not by accident.

### Safety & contracts
- Validate inputs at boundaries; fail fast with a clear error over silent fallback.
- Handle `None`/missing attributes explicitly.
- State pre/postconditions where a contract is real (e.g. "npc must have `.race`"; "returns a non-empty list of `ConditionType`").

### Testing lives inside the module (`__main__` self-tests)
> A module should be **self-contained**: it carries its own proof that it works, and that proof doubles as documentation of how to use it.
- Each module puts its tests in an `if __name__ == "__main__":` block at the foot of the file. Running the file (`python path/to/module.py`) runs its own checks.
- The self-test is written to also **read as a usage example** — the clearest possible "how do I use this?" for the next reader.
- Prefer this over a separate mirrored `tests/` batch. A module and its proof travel together; there is no far-away test file to fall out of sync. (This is why `tests/test_top_integration.py` was retired with AtlasTOP.)
- Keep self-tests light and deterministic (seed any randomness). If a cross-module/integration test genuinely can't live in one module, that is the rare exception — justify it.

## The flavor layer (kept honest)

Arcane tone is welcome and encouraged — in user-facing strings, comments, docstrings, and thematically-named symbols. It must **never** cost clarity. A newcomer must always be able to translate the flavor into plain meaning. When flavor and clarity collide, clarity wins and the flavor moves to a comment.

## Enforcement

Tool-specific review agents may enforce slices of this Canon. They are **downstream** of this file: if a rule disagrees with this Canon, the rule is wrong and gets a Questa. See `Agentia/Agents-Compliance.md`.
