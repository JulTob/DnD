# Dialog 0003 — The minimal Character, and instantiating the RNG & core mechanisms

- **Question (Q-0006):** What is the minimal expression of what the generator builds — the root **Character** — and how are the **RNG and core mechanisms** instantiated into it, so PC and NPC can diverge by TOP tags?
- **Raised by:** Julio (arbiter)
- **Related Questae:** QST-0016 (flagship unify), QST-0006 (paradigm), QST-0013 (Modifier one-source), QST-0002/0008 (one sheet)
- **Consuls called:** Bard, Lorekeeper, Druid, Wizard, Sorcerer, Paladin, Warlock, Monk, Rogue
- **Status:** 🟢 converged — awaiting Julio's arbitration

---

## 🧭 Framing
Julio's ruling: the root is **Character** (the umbrella — a PC and an NPC are both characters); PC and NPC diverge as **role Tags**, not parallel classes. The council must design (a) the **minimal** substrate the root carries, and (b) how the **RNG + core mechanisms** (dice, score generation, seed) are instantiated so a Character is **reproducible from its seed alone**. Canon: composition over inheritance; one source of truth per rule; keep it minimal (no over-collapse — no `if is_npc:`).

---

## 🗣️ Deliberation

Understanding Consul (Bard): Start with the irreducible question — what is the *least* a generated character can be and still be one? My answer: a **name** (and optional **title**), a set of **ability scores**, and the **seed** that produced them. Species, class, background, story — all of that is enrichment layered on top. If we can generate "a being named X with six scores from seed 1234," the skeleton is right; everything else is a Tag. *(A note on words: "identity" is avoided here — it already means the Target's stable object-identity in TOP, and there's an `AtlasTOP/identities.py` `CharacterIdentity` Tag. The root just holds plain `name`/`title` strings; richer identity is that tag's job.)*

Lorekeeper (Elf Sage): Canon agrees. The immutable substrate of *any* 5e/2024 creature is the **six ability scores** (STR/DEX/CON/INT/WIS/CHA) and a **size**. From those plus a **tier** (level for PCs, CR/level for NPCs) the rest is *derived*: proficiency bonus, and — with class/species tags — HP and AC. The **modifier** is a pure rule, `floor((score-10)/2)`; it must live in one place (QST-0013), and the root should call it, never re-derive it.

Druid (Architecture Consul): So the root `Character` is a TagKit `Tagged` base holding only {`name`, `title`, scores, size, tier, seed} — plus the RNG (below). (Plain string fields — *not* an `Identity` object; the existing `CharacterIdentity` Tag in `AtlasTOP/identities.py` handles anything richer.) `Species`, `Role` (class/archetype), `Background` are Tag axes; `PlayerCharacter` and `NonPlayer` are role Tags that add their divergent contributions. The two current Grimoires (`Character`, `NPC`) collapse into this one root + role tags; AtlasLusoris/AtlasAlusoris become role/view layers (this is where QST-0005 dissolves).

Methods Consul (Wizard): The crux is the RNG, and today it's a mess: `import app.random as random`, stdlib `from random import randint`, and `random.seed(npc_seed)` mutating **global** module state. Proposal: **the Character owns its own RNG** — `self.rng = random.Random(self.seed)` — and *every* roll (score generation, dice, tag imprints) draws from `self.rng`. A character then becomes a pure function of its seed. Deterministic, isolated, and the shareable-URL feature (already built) gains a real guarantee.

Flow Consul (Sorcerer): Second, and I'll sharpen it to a *bug*, not a nicety: global `random.seed()` is **shared mutable state**. Two Shiny sessions generating at once, or the NPC-list loop interleaving with a character build, will read each other's RNG and corrupt reproducibility. An instance `Random(seed)` per Character isolates the stream. This removes a whole class of heisenbugs.

Safety Consul (Paladin): Then the seed is a contract, not a decoration. Validate it at the boundary (the URL/hash already carries it), coerce to int, and hold the invariant **same seed ⇒ same Character**. Fail loudly on a malformed seed rather than silently drawing from a fresh global.

Contracts Consul (Warlock): I'll state the skeleton's invariants precisely, as TagKit contracts on the root: `scores` each in the valid range; `size` a canonical `Compass` value; `tier ≥ 1`; `seed` present and integral; and the reproducibility invariant Paladin named. Core mechanisms — the **Dice** in `AtlasLudus` — must take an `rng` argument (or a Character) instead of importing global random. That's the "instantiate core mechanisms into the root": dice roll *through* the character's stream.

Simplicity Consul (Monk): Guard the word **minimal**. The root holds {identity, scores, size, tier, seed, rng} — and *nothing else*. Species, class, HP, AC, skills, story are Tags/derived, never fields on the base. The temptation will be to hang "just one more" attribute on Character; resist it. If it can be derived or tagged, it is not part of the skeleton.

Methods Consul (Wizard): Agreed — HP/AC are *derived*, computed from tier + tags, not stored on the root. Concede that point to the Monk.

Testing Consul (Rogue): Two tests define "done" and I want them written first: **reproducibility** — `build(seed) == build(seed)` field-for-field — and **isolation** — building two characters with different seeds, interleaved, yields the same result as building them separately. If instance-RNG is real, both pass; if global state leaks, isolation fails. That test *is* the proof of the design.

Bard (Understanding Consul): Then the shape is settled and small: a Character is *a seed made flesh* — identity + scores + size + tier, rolled from an owned RNG, enriched by tags. No objection remains.

Druid: Converged.

---

## ✅ Convergence check
- [x] Every called Consul has spoken.
- [x] Objections answered (Monk's minimalism trimmed HP/AC off the root; Wizard conceded).
- [x] Concrete skeleton + RNG design + a test that proves it.

---

## 🕊️ Vox report

Vox: Report on **Q-0006 — the minimal Character and its RNG/core mechanisms.**

**Common ground (unanimous):**
- Root = **Character** (umbrella). PC/NPC are **role Tags**, not classes.
- Minimal substrate: **`name` (+ optional `title`), six ability scores, size, tier (level/CR), seed** — and an **owned RNG**. Nothing else lives on the root. (Plain fields, not an `Identity` object; richer identity is the existing `CharacterIdentity` Tag.)
- **HP, AC, PB, modifier are derived**, via single-source rule functions (Modifier per QST-0013) — never stored on the base.
- **Core mechanisms (Dice, score rolls) draw from the Character's own RNG**, not global module state.
- Invariant: **same seed ⇒ same Character** (reproducibility), proven by a test.

**Options & tradeoffs (the real fork — how the RNG lives):**
1. **Instance RNG on the Character** *(council's lead)* — `self.rng = Random(seed)`; all rolls draw from it. *Pro:* deterministic, isolated, concurrency-safe, seed-reproducible; fixes a latent shared-state bug. *Con:* must thread `rng` through Dice and the generators (plumbing across a few Atlases).
2. **Keep global seeding (status quo)** — `random.seed()`. *Pro:* zero refactor. *Con:* shared mutable state; breaks under concurrent Shiny sessions / interleaved list generation. Rejected by the council.
3. **Functional core** — pure `roll_*(rng)` functions; Character is a thin data record composed by tags. *Pro:* the most testable and TOP-pure. *Con:* the largest refactor; best adopted incrementally *after* option 1.

**Code sketch (illustrative, not final spelling):**
```python
class Character(Tagged):                 # the umbrella root
    TAG_ROOTS = (Species, Role, Background)
    def __init__(self, seed: int, name: str | None = None, tier: int = 1):
        self.seed = int(seed)
        self.rng  = Random(self.seed)    # owned RNG = the core mechanism
        self.name = name
        self.tier = max(1, tier)
        self.size = Size.MEDIUM
        self.scores = roll_scores(self.rng)   # dice/score gen draw from self.rng

# derived, not stored:  modifier(score) · proficiency_bonus(tier) · hp(...) · ac(...)
# roles are tags:
PlayerCharacter(hero)      # leveling, subclass, shareable build
NonPlayer(guard)           # archetype, legendary/lair/region, plot hook, light mode
```

**Consul positions:** Wizard & Sorcerer led the instance-RNG (correctness); Monk held the line on a minimal root (HP/AC derived, not stored); Warlock specified the invariants + Dice-takes-rng; Lorekeeper fixed the canon substrate + single-source modifier; Rogue defined the two proof tests; Bard framed "a seed made flesh."

**Synthesis:**
- **Leading recommendation:** Option **1 (instance RNG on Character)** as the foundation — smallest change that fixes the shared-state bug and guarantees seed-reproducibility — with Option **3 (functional core)** adopted incrementally afterward as tags migrate. Sequence behind QST-0006 (paradigm) so the composition spelling is settled first.
- **Strongest alternative:** go straight to Option 3 (functional core) if you'd rather pay the bigger refactor once and land the purest TOP design in a single move.

**Sidequests this would spawn (on your decree):**
- `QST-0016.1` — define the `Character` root skeleton + `Compass_of_Size` / tier.
- `QST-0016.2` — instance RNG; make Dice + score-gen take the Character's `rng`.
- `QST-0016.3` — `PlayerCharacter` / `NonPlayer` role tags; migrate the two Grimoires.
- `QST-0016.4` — one sheet renderer over the composed Character (folds QST-0002/0008).
- `QST-0016.5` — reproducibility + isolation tests (Rogue).

→ **Awaiting Julio's decision.** Your arbitration becomes **Decree 0002** and opens the sidequests above.
