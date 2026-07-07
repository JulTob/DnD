# QST-0018 — Remove AtlasTOP; fold its composition into the Grimoires

- **Type:** refactor
- **Priority:** 🔴 urgent  *(unsanctioned bloat; first concrete step of the unification)*
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Simplicity Consul (Monk), Architecture Consul (Druid), Contracts Consul (Warlock)
- **Parent:** QST-0016 (Character unification)
- **Sidequests:** —
- **Related:** Decree 0002, QST-0005 (Atlas merge), Canon Code-Style (structure discipline)

---

## 🔍 Diagnosis (what & where)
`AtlasTOP/` is an unsanctioned parallel TOP layer (a rogue-agent addition). It is thin: it applies species/class/background/etc. tags and stamps `top_layers["kind"] = "character"|"npc"`. It is imported at exactly two live call sites plus a test:
- `AtlasLusoris/Grimoire_of_Characters.py:10,68` — `from AtlasTOP import compose_character` → `compose_character(char)`.
- `AtlasAlusoris/Grimoire_of_NPC.py:10,65` — `from AtlasTOP import compose_npc` → `compose_npc(npc)`.
- `tests/test_top_integration.py` — imports many `AtlasTOP.*` symbols.

## 🧾 Evidence
`AtlasTOP/` = 11 files (`composition.py`, `identities.py`, `species/races/classes/subclasses/backgrounds/archetypes/subraces.py`, `_helpers.py`, `__init__.py`). `identities.py` shows the whole pattern: a `Tag` with an `@Imprint` that sets `kind`. Direct `from TagKit import Tag, Imprint` — so the same can be done inline in the Grimoires.

## 🎯 Desired outcome
`AtlasTOP/` deleted. The two Grimoires apply their species/class/background tags **directly with TagKit** (simple, clear, in the file that owns the object). The `kind` stamp becomes the **Player/Non role tag** (per Decree 0002). The test is rewritten against the new surface (or retired). Nothing on a parallel scaffold.

## 🧭 Notes for the implementer (do NOT bare-delete)
- **Order:** first move the composition inline into each Grimoire and prove they still build a character/NPC; **then** delete `AtlasTOP/`. Deleting first breaks the generator.
- This is the natural first slice of QST-0016 — the `kind` flag is already the PC/NPC distinction we're turning into a tag.
- Keep it minimal: import TagKit, tag the object, done. No new helper package.
- Confirm with Julio before the delete (per Canon).

## ✅ Resolution
*(pending — refactor the two Grimoires, then delete AtlasTOP)*

---

## 🏛️ Council
> Simplicity Consul (Monk): Eleven files to do what two `Tag` applications do inline. This is the textbook bloat the Canon now forbids. Fold and delete.
> Architecture Consul (Druid): The `kind = character/npc` stamp is the seed of the role tag — so this removal *is* the first step of unification, not a detour. Refactor in place, then cut.
> Contracts Consul (Warlock): Preserve the one behavior that matters (the species/class/background tags actually applied) and pin it with the reproducibility test before deleting. No objection.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `build` (refactor-then-delete; confirm delete with Julio)
