# Dialog 0007 — Title map as narrative identity

- **Question (Q-0010):** How should generated titles become thematic, deterministic narrative identity without leaking lusor internals?
- **Raised by:** Julio (via Agent)
- **Related Questae:** QST-0027 · QST-0027.1 · QST-0027.2 · QST-0027.3 · QST-0027.4 · QST-0016 · Decree 0002
- **Consuls called:** Bard, Druid, Warlock, Wizard, Monk, Rogue, Lorekeeper
- **Status:** 🟡 open

---

## 🧭 Framing

Julio wants titles to be one of the generator's main thematic elements:
the small phrase by which a character is known, and therefore a prompt for how
the player might inhabit that character. "The Protector of the Realm" implies a
caring, public-facing figure. "The Dark Shadow" implies secrecy, edge, and
threat.

The linked wiki page `0.1-🧭-Themes` frames theme as a compass: it aligns
characters, conflicts, settings, and outcomes. A title should behave like that
in miniature. It should not be only a random adjective plus noun. It should
carry a readable thematic signal: protection, defiance, mastery, fate, shame,
hope, power, grief, discovery, and similar axes.

Technical constraints from the current code:

- `AtlasNomina/Map_of_Titles.py` is a flat, ~7,400-line function-heavy module.
  - Pros: It works like a charm, is simple, and easy to expand and work with. 
- `Title(lusor)` resets global random state with `random.seed(lusor.seed)`.
  - Con: This is a breach of abstraction.
- `Descriptor`, `Rank`, `Place`, `Artifact`, and `Origin` choose through module
  global `random`.
  - The randomness engine should be selected when imported, to select one for each character's rng/dice
- `Genus(lusor)` probes concrete attributes (`race`, `subrace`, `archetype`,
  `char_class`, `gender`, `alignment`) and therefore crosses abstraction
  boundaries.
- The title map already wants membership-style selection (`"Wizard" in lusor`,
  `"Lawful" in genus`), but the protocol is not explicit.
- `Element(lusor)` yields values, while `Origin(lusor)` interpolates the
  generator object itself unless corrected.

Out of scope for this first discussion: implementing the full refactor. This
dialog should first settle the boundary, the RNG source, the module shape, and
the memory/return strategy. Implementation follows as small QST-0027 sidequests.

---

## 🗣️ Deliberation

Understanding Consul (Bard): The title is not garnish. It is the character's
one-line myth. The title map should therefore be organized around meaning as
well as sound: not only "does this phrase sound cool?", but "what promise does
this phrase make to the player?" The wiki's theme map gives us the language:
passion, mastery, discovery, defiance, hope, fear, guilt, fate, identity,
legacy. Those are stronger selector axes than a single flattened word list.

Architecture Consul (Druid): The first technical boundary is clear. The title
map should ask one general question: `"Characteristic" in lusor`. It should not
reconstruct `race`, `subrace`, `class`, `background`, or alignment by probing
attributes. Strings, lists, sets, dicts, and generated Characters can all honor
membership. The concrete object owns how membership is answered; the title map
only consumes the answer.

Contracts Consul (Warlock): Then the contract is simple enough to bind. A
title source is acceptable if membership checks are meaningful and if the
randomness source is explicit. For concrete generated characters, membership
must include the public characteristics the generator promises: species/race,
subrace, class or archetype, subclass, background, gender, alignment, and later
theme tags. For plain collections, membership is their normal Python contract.

Methods Consul (Wizard): Randomness must follow Decree 0002. `Title` cannot
seed global `random`. Every selection function should receive the same random
source, whether that is `character.Dice`, a passed `random.Random`, or a small
adapter over `Roll(D=)`. This keeps title generation reproducible and prevents
one character generation from perturbing another.

Simplicity Consul (Monk): Keep the public API boring. A title call should
return one string. Do not expose a generator just because one helper currently
uses `yield`. If memory or construction cost is real, move stable word pools to
module-level immutable tuples and build only the final candidate pool per call.
No cache layer until a measurement or a repeated-work hotspot proves it earns
its weight.

Testing Consul (Rogue): The first proof should live at the bottom of
`Map_of_Titles.py`: run the module and test strings, lists, sets, dicts, and a
small object with `__contains__`. Then test two seeded random sources produce
the same title, two different seeds can differ, and no generated title contains
`<generator object`. That last one catches the current `Element`/`Origin`
failure directly.

Lorekeeper (Elf Sage): The title vocabulary should remain original and
campaign-owned. It can echo broad D&D archetypes and the project's own wiki
themes, but it should avoid relying on protected setting names as the source of
flavor. "Oath", "Ash", "Crown", "Void", "Mercy", "Rebellion", "Last Light"
are usable thematic language; named lore should be deliberate and reviewed.

---

## ✅ Convergence check

- [x] Every called Consul has spoken.
- [ ] Every objection has been answered or conceded.
- [ ] At least one concrete proposal (with code sketch) is on the table.

---

## 🕊️ Vox report

Vox: Pending. The first open point for Julio is the selector boundary:
should `Map_of_Titles` standardize on `"Characteristic" in lusor`, with simple
support for built-in strings and collections, before any deeper vocabulary
refactor?

→ Awaiting Julio's direction before drafting a Decree or touching code.
