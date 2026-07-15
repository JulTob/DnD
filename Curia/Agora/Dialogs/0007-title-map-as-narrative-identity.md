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

- `AtlasNomina/Map_of_Titles.py` keeps vocabulary, selector logic, title
  grammar, duplicate checks, and random selection in the same module. The line
  count is not itself a defect; the concern is whether each responsibility is
  readable, maintainable, and useful.
- `Title(lusor)` resets global random state with `random.seed(lusor.seed)`.
- `Descriptor`, `Rank`, `Place`, `Artifact`, and `Origin` choose through module
  global `random`.
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

Julio: `"Characteristic" in lusor` should be the boring expected behavior. The
final product will use TOP tags, so "Characteristic" will eventually be a tag
on the composed object. During testing it can be a string, list, set, dict, or
any container-like object with meaningful `in` behavior. That is good software
engineering because the title map consumes a stable contract instead of object
anatomy.

Julio: A long word list is not a problem by itself. Do not use line count as a
proxy for code quality. English has many useful words, and the generator should
use as many as it needs when the words are clean, readable, and useful. Clean
the list by strong criteria about the value of the words and the maintainability
of their organization, not because the list is long.

Julio: For RNG, the transitional contract is sensible, but name it
`set_random(Dice)`. The parameter name should keep the project's thinking model
and artistry: the Character carries Dice, not an abstract RNG wire. The function
sets the module-level random source to the provided Dice, falling back to
Python's `random` when unset or `None`. The value of that function is isolating
and specifying the contracted behavior while the abstraction layer migrates.

Julio: For vocabulary extensions, the ideal is to use the official, already
working TOP implementation from `JulTob/Tag_Oriented_Programming`. It was made
for exactly this kind of layered contribution. Do not build a fake local TOP
registry inside `Map_of_Titles`; if title words become Tag contributions, they
should use the pinned TagKit project.

Julio: The vocabulary should probably have a functional classification, because
some pools may later serve story generation or similar systems. Think in
reusable narrative material: Artifacts, Places, Essences or Elements, and
Themes. Use theme to classify, not only the immediate title slot.

---

## ✅ Convergence check

- [x] Every called Consul has spoken.
- [x] First point settled: `"Characteristic" in lusor` is the selector contract.
- [x] Second point settled: transitional random source is `set_random(Dice)`.
- [x] Third guardrail settled: real TOP behavior uses official TagKit, not a local imitation.
- [ ] Vocabulary structure and curation criteria still open within that guardrail.
- [ ] Return/yield/cache strategy still open.

---

## 🕊️ Vox report

Vox: Interim report on **Q-0010 — title map as narrative identity**.

**Common ground now settled:**

- `Map_of_Titles` should consume the boring Python contract:
  `"Characteristic" in lusor`.
- In the final TOP shape, a characteristic is a tag on the composed object.
- In tests, `lusor` may be a string, list, set, dict, or any object that
  implements meaningful membership.
- The title map should not inspect `race`, `subrace`, `char_class`,
  `background`, or other concrete internals to decide whether a selector
  applies.

**Correction from Julio:**

- Long vocabulary lists are not a defect by themselves. They are justified when
  the words are useful, readable, and app-manageable. Any cleanup must use real
  criteria: word quality, thematic value, duplication, typo risk, organization,
  and maintainability.

**RNG transition settled:**

- Add a transitional `set_random(Dice)` module interface.
- `Dice` names the character-owned randomness source and preserves the
  project's model language.
- Passing `None` or leaving it unset falls back to Python's `random`.
- This is a bridge while the title map migrates toward the Character Dice /
  `Roll(D=...)` source.

**TOP guardrail settled:**

- If title vocabulary becomes Tag-driven, it must use the official pinned
  TagKit/TOP project: `github.com/JulTob/Tag_Oriented_Programming`.
- Transitional subfunctions may organize the current title map, but they must
  be shaped as a migration path toward TagKit contributions, not as a new local
  TOP-like framework.
- `Map_of_Titles` may remain a plain map while the Character root migration is
  pending; it must not grow a parallel composition engine.

**Vocabulary structure under discussion:**

- Prefer reusable functional categories where they carry meaning beyond titles:
  Artifacts, Places, Essences/Elements, and Themes.
- Title-specific roles still exist (`Descriptor`, `Rank`, `Origin`), but they
  should draw from functional pools rather than trap useful words inside one
  title-only bucket.
- This keeps title vocabulary available for later story generation without
  forcing a new abstraction now.

**Vox synthesis:**

- Leading recommendation for QST-0027.1: implement direct membership
  consumption first, with tests for strings, lists, sets, dicts, and a tiny
  object with `__contains__`.
- Strongest alternative: add a small `has_characteristic(lusor, characteristic)`
  helper if raw membership proves too uneven across strings and mappings.

→ Selector contract, RNG transition, and official-TagKit guardrail settled by
Julio. Next open point: exact vocabulary structure and curation criteria.
