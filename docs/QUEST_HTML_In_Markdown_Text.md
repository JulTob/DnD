# Quest: HTML tags leak into feature text on the sheet

**Status:** open · **Scope:** `app/components/shared.py`, feature/spell description authoring
**Found:** 2026-07-31, reported by the author (Light cantrip), root cause traced.

---

## Symptom

The Aasimar **Light Bearer** feature renders literal markup on the sheet:

> Until the spell ends, the object sheds Bright Light in a 20-foot radius and Dim Light
> for an additional 20 feet. The light can be colored as you like. `<br>` Covering the
> object with something opaque blocks the light.

The `<br>` is shown as text instead of a line break.

## Cause

A mismatch between how descriptions are AUTHORED and how they are RENDERED.

- **Authored as HTML.** `Light Bearer`'s description is an HTML string
  ([Grimoire_of_Features/__init__.py:937](../AtlasLusoris/Grimoire_of_Features/__init__.py:937)):
  it contains `<b>`, a `<div class="spell">…</div>` wrapper, and the embedded spell text
  from [Lodge_of_Spells.py:290](../AtlasMagia/Lodge_of_Spells.py:290) carries a literal
  `<br>`.
- **Rendered as Markdown.** `feature_item` passes the description to `ui.markdown()`
  ([shared.py:257](../app/components/shared.py:257)), which escapes raw HTML.

So every feature whose description contains HTML will leak tags. Light Bearer is simply
the most visible instance — this is systemic, not a one-off typo.

Note this is the SAME class of bug already fixed once in the equipment rows, where
`ui.tags.b(safe_str(item))` escaped the `Entry` HTML and was changed to `ui.HTML(...)`.

## Options

1. **Render trusted description HTML with `ui.HTML`** (matching the equipment fix).
   Simple and consistent, but every author of a description then holds a loaded gun —
   all description text becomes trusted markup.
2. **Author descriptions in Markdown only**, and convert the handful of HTML-bearing
   ones (spells especially). Safer, but touches a lot of content and fights the fact
   that `Spell`/`Entry` deliberately ARE HTML (Venustas Scriba).
3. **Detect and branch** — if the text contains markup, render with `ui.HTML`, else
   `ui.markdown`. Pragmatic, but a guess-at-runtime rule is exactly the kind of implicit
   behaviour this codebase avoids elsewhere.

Recommended: **(1)**, because the Scriba design already commits to "the value IS the
HTML" — `Entry`, `Chip`, `Spell` and now `Item` all render themselves as markup. Making
the sheet honour that consistently is the smaller, more coherent change. Descriptions are
code-authored, never user input, so the trust boundary is not actually widened.

## Acceptance

- No literal `<br>`, `<b>`, `<i>`, or `<div` visible in any rendered sheet section.
- A sweep over every generated feature description for all guilds and species finds no
  escaped markup — worth adding as an invariant to the verification harness, since this
  bug is invisible until someone happens to read the right feature.
- Markdown-authored descriptions (most Trainings) still render their emphasis correctly.
