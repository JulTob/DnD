# 🏷️ TagKit Doctrine — Tag-Oriented Programming

> **Canon.** Read, do not edit. **TagKit is an independent, settled upstream project** — repo `github.com/JulTob/Tag_Oriented_Programming`, pinned in `requirements.txt` to a specific commit. Its GitHub Guide is the authoritative *paradigm* text; we do **not** vendor, fork, or keep local beta copies of it. This Doctrine is the short, binding summary: **how we use TagKit in this project, and how we propose changes to it upstream.**

## The paradigm, in one breath

**Tag-Oriented Programming (TOP)** composes orthogonal semantic layers on one stable object identity.

- OOP asks: *what is this object in essence?*
- TOP asks: *what is this object for?*

A **Target** keeps its identity. **Tags** are applied to it (`Human(charlie)`), and the Target becomes an **Agent** of that Tag. Semantic meaning grows by composition, not by deep inheritance.

```python
charlie = Character("Charlie")
Human(charlie)      # charlie is now in the Human field
Wizard(charlie)     # …and the Wizard field

assert isinstance(charlie, Character)   # class layer: unchanged
assert charlie in Wizard                # tag layer: true
```

## Why this project uses it

D&D characters *are* layered semantics: species + background + class + subclass + features, combined dynamically. That is exactly what TOP models cleanly and OOP models painfully. **TagKit was built for this project.** Using it well is not optional flavor — it is the design target.

## The rules of use (binding)

1. **Model domain axes as Tags, not as string checks or ad-hoc dicts.** Species, roles, backgrounds, conditions, damage types, rarity — these are Tags / canonical types (`Compass_of_*`), never scattered `if kind == "wizard"` strings.
2. **Prefer composition over inheritance.** Augment objects by applying Tags, not by growing class trees.
3. **One source of truth per type.** Shared types come from a single `Compass_of_*`; modules import them, never redefine them.
4. **Use the defined composition modes** and keep them explicit:
   - **Augmentation** — introduce a *new* contribution name (must fail if the name already exists).
   - **Extension** — refine an existing contribution; must receive the previous meaning explicitly (`previous`).
   - **Mutation** — replace the current contribution from that point upward.
5. **Contracts where obligations are real:** `Expectation` (must hold before applying), `Condition` (must hold after), `Exclusion` (no invalid siblings), `Final`/`Sealed` where extension must stop.
6. **Repeat the pattern modularly.** New content should slot into the existing Tag structure the same way existing content does. If adding a race requires touching five unrelated files, that is a smell — mint a Questa.

## TagKit is upstream — how we consume it

- **Depend, don't vendor.** TagKit is installed from its pinned GitHub commit (`requirements.txt`). Never copy its source, its guide, or a "beta" into this repo.
- **The API is whatever the pinned commit exposes** — consult the GitHub Guide, not memory. The surface this project already uses is `from TagKit import Tag, Imprint` (plus the composition helpers in our own `AtlasTOP/`). `AtlasTOP/` is **our** domain layer *on top of* TagKit, not part of TagKit.
- **To adopt new TagKit behavior,** bump the pinned commit deliberately (a normal dependency change → confirmation per Canon), then use it.

## When TagKit is insufficient — "Suggest to TagKit"

If a clean, idiomatic solution is **blocked by a limitation of TagKit itself**, do not hack around it and do not patch it locally (it's upstream).

1. Mint a Questa of type **`tagkit-upstream`** titled **"Suggest to TagKit: X"** — a proposal to the independent project, with the exact limitation, the code you wanted to write, and the workaround currently forced.
2. It is triaged with high priority, but as an **upstream proposal**: it lands in TagKit's own project, and here we only bump the pin once accepted.
3. If we're truly blocked meanwhile, record the temporary workaround in `AtlasTOP/` (our layer) — never inside a local TagKit copy.

**Rationale:** TagKit is the heart the whole project beats on — but it is its *own* heart, kept in its own repo. We treat it with care by proposing upstream and pinning deliberately, not by forking it into drift.
