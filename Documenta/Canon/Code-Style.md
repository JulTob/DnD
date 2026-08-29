# 🪶 Code Style — Light, Readable, Arcane

## Spirit

Code should read like a clean spell: every line earns its place and nothing is
there to impress.

Clear beats clever. Readable beats dense. Explicit beats magical.

That last one governs emitted text as much as code: the prose a player reads is
formatted by what an author wrote, never by a rule that infers intent at render
time. See `Feature-Text.md`.

That last one governs emitted text as much as code: the prose a player reads is
formatted by what an author wrote, never by a rule that infers intent at render
time. See `Feature-Text.md`.

## Visual density

Prefer short lines, small logical blocks, and visible separation between:

1. input validation;
2. resolution;
3. mutation;
4. projection;
5. return.

Do not compress several decisions into one expression.

## Waterfall layout

Long signatures, calls, aggregates, contracts, and boolean expressions fall
vertically.

```python
def summon_character(
        *,
        species: str,
        guild: str,
        background: str,
        seed: int,
        ) -> Character:
    return build_character(
            species=species,
            guild=guild,
            background=background,
            seed=seed,
            )
```

Rules:

- one parameter or argument per line once the construction wraps;
- input parameters use the established double indentation;
- the closing delimiter remains inside the visual cascade;
- do not detab the closing line to the far-left margin;
- break dense boolean expressions into named predicates or vertical clauses;
- preserve the local package's tabs/spaces convention in touched legacy code;
- do not reformat unrelated files merely to impose a new style.

## Cascade

A call is a river. When it opens, its inputs fall together beneath it. The
first positional input is normally the thing receiving the operation; later
inputs provide its context.

Keep a single-input cartouche on one breathable line:

```python
Find_Alignment( character )
data[ key ]
```

Let a contextual call cascade:

```python
shape(
        character,
        size=size,
        )
```

Long dotted reads may also descend. Python requires the expression to be
enclosed and the dot to begin the continued line; a trailing dot followed by a
newline is not valid Python.

```python
if selected_heritage is not None:
    character.heritage = (
        selected_heritage
        .__name__
        .replace(
                "_",
                " ",
                )
        )
```

Do not force a short `object.attribute` onto several lines. The cascade serves
navigation: it should reveal a long route, not decorate a short one.

## One purpose

Each public subprogram has one clear purpose. Each purpose deserves one clearly
named subprogram when extracting it makes the flow easier to scan.

Avoid both extremes:

- a long function that mixes selection, mutation, rendering, and I/O;
- dozens of one-line helpers that hide a straightforward sequence.

## Models and ownership

- Stable domain distinctions use types, records, and Tag branches.
- Public contracts live in the owning Kit or Map.
- Implementation details stay private to that unit.
- Shared Tag families have one canonical home.
- Presentation components do not own production rules.
- Compatibility adapters live at the boundary and have an exit path.

Refactor the active production line. Do not build a shadow architecture beside
it.

## Python naming

- `CapWords` for classes and Tags;
- `snake_case` for new ordinary functions, variables, and records;
- `Find_Subject` for a public, read-only derivation from current Tags;
- retain established public legacy names only when compatibility requires;
- themed module names follow `Conventions.md`;
- names describe the domain purpose rather than the implementation trick.

Use `isinstance` for object-kind checks. Use context managers for scoped state.
Return `None` intentionally, never by accident.

`Find` is distinct from mutation and boundary resolution:

- `Find_Alignment( character )` derives an answer from carried Tags;
- `Resolve_Species( request )` maps external input to a canonical Tag; and
- `Apply_Species( character, species )` changes semantic membership.

A `Find` function does not apply Tags, roll Dice, or create a compatibility
Record.

## Contracts and failures

Validate inputs at public boundaries. Use TagKit `@Pre` and `@Post` when the
obligation belongs to Tag application.

Failure messages should name:

- the rejected value;
- the expected semantic set or condition;
- the boundary that rejected it.

Do not catch broad exceptions merely to continue with corrupted state. A
compatibility fallback must be narrow, deterministic, and visible in the
current-state ledger.

## Randomness

Random sources are explicit and Character-owned.

Never:

- reseed a process-global module in production code;
- use salted `hash()` for replayable selection;
- let unordered iteration choose a result;
- roll values while rendering.

## Comments and documentation

Comments explain intent, invariants, provenance, or a non-obvious trade-off.
They do not paraphrase the next line.

Public functions and types receive concise docstrings when their contract is
not already evident from the signature.

## Tests

Use the smallest proof that protects the boundary:

- a light `__main__` self-test when it doubles as a useful module example;
- focused test functions for contracts and regressions;
- integration scripts for cross-Atlas generation, URLs, determinism, and
  frontend startup.

Tests are deterministic and name the invariant they protect. A rule does not
become less important merely because it crosses module boundaries.

## Flavor

Arcane tone is welcome in user-facing strings, documentation, and clear
thematic names.

Feature Entries separate imagination from mechanics:

```markdown
*The echoes of the Fae still linger in you.*

You have Advantage on saving throws against the Charmed condition.
```

- italicize the flavour paragraph;
- keep the rules paragraph in normal text;
- separate them with a blank line;
- keep numbers, conditions, actions, uses, ranges, and recovery language in the
  rules paragraph; and
- do not make a renderer guess which words are flavour—the author marks the
  boundary in the Entry description.

A wholly narrative Entry—such as a Species, Heritage, Background, or story
introduction—declares `narrative=True` when it is granted. Its renderer may
then italicize the whole body while leaving the Entry title upright. This is
an explicit presentation record, not an inference from the prose or source
name.

An Entry may contain only rules when no flavour is useful. It must never hide a
rule inside the italic paragraph.

When flavor and clarity collide, clarity wins.
