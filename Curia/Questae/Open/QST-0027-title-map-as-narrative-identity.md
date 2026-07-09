# QST-0027 — Title map as narrative identity

- **Type:** design/refactor
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Understanding (Bard), Architecture (Druid), Contracts (Warlock), Methods (Wizard), Simplicity (Monk), Testing (Rogue), Lorekeeper
- **Parent:** —
- **Sidequests:** QST-0027.1 · QST-0027.2 · QST-0027.3 · QST-0027.4
- **Related:** Q-0010 · Dialog 0007 · QST-0016 · Decree 0002 · `AtlasNomina/Map_of_Titles.py` · wiki `0.1-🧭-Themes`

---

## 🔍 Diagnosis (what & where)

`AtlasNomina/Map_of_Titles.py` is currently the only title map, but it is still
superficial relative to the role Decree 0002 gives it: every Character must have
a required `name` + `title`, and the title is the narrative identity seed.

The module has several different concerns mixed together:

- title grammar (`The {descriptor} {rank}`, `The {rank} {origin}`);
- word vocabulary for descriptors, ranks, places, artifacts, and origins;
- characteristic selection through concrete object probing;
- random selection and repeated seeding;
- duplicate avoidance;
- an unresolved return-vs-yield shape in `Element`.

The result can sound cool, but the code does not yet make titles a clean,
deterministic, thematic system.

## 🧾 Evidence

- `Title(lusor)` calls `random.seed(lusor.seed)` and then uses global
  `random.choices`.
- `Descriptor`, `Rank`, `Place`, `Artifact`, and `Origin` use global
  `random.choice`.
- `Genus(lusor)` checks `isinstance(lusor, str)`, `hasattr(lusor, "genus")`,
  and concrete attributes such as `race`, `subrace`, `archetype`,
  `char_class`, `gender`, and `alignment`.
- `Origin(lusor)` sets `element = Element(lusor)`, but `Element` is a yielding
  generator, so origin text can accidentally receive the generator object
  instead of an element word.
- The wiki theme note says theme is the compass that aligns characters,
  conflicts, settings, and outcomes. The title should express that compass in
  miniature.

## 🎯 Desired outcome

- Titles become a first-class thematic prompt for play.
- `Map_of_Titles` has one clear public contract and small internal helpers.
- The title generator consumes a general lusor interface instead of inspecting
  Character/NPC internals.
- Randomness is deterministic and explicit, in line with Decree 0002.
- Vocabulary pools are organized by useful criteria: word quality, thematic
  value, selector intent, maintainability, and app cost.
- Relevant self-tests live in the module's `__main__` block.

## 🧭 Notes for the Agora / implementer

- Open Dialog 0007 before implementing. This touches architecture, contracts,
  RNG, and theme.
- Refactor existing code where it lives; do not build a parallel title engine.
- Keep sidequests single-purpose:
  - QST-0027.1: selector/interface boundary;
  - QST-0027.2: RNG source;
  - QST-0027.3: vocabulary and theme structure;
  - QST-0027.4: return/yield/cache strategy.
- Preserve existing callers (`Character.New_title`, `NPC.SetTitle`) until a
  specific implementation QST changes them.

---

## ✅ Resolution (filled when Solved)

- **Decided by:** *(pending Julio)*
- **What changed:** *(pending)*
- **Practice/preference to remember:** Title is required narrative identity,
  not optional flavor text.

---

## 🏛️ Council

> Understanding Consul (Bard): The phrase is a compact theme, not decoration.
> Architecture Consul (Druid): The boundary leak is real; the title map should consume membership, not object anatomy.
> Methods Consul (Wizard): The global RNG violates the decreed Dice direction.
> Simplicity Consul (Monk): Split only where a responsibility is real; no replacement framework.
> Julio: Do not use line count as a proxy for quality; clean vocabulary by word value and maintainability.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `needs a Dialog`
