# Decree 0005 — Affinity steers selection

- **Ratified by:** Julio, 2026-08-18, in session
- **Source:** Dialog 0010 (Q-0013), QST-0049
- **Status:** active

## Decision

**1. The causality runs forward, not backward.**

A build's **affinity** is known before anything is drawn: it follows from the Guild, the
Specialization, the casting ability, and the level the character is built for. Affinity therefore
**weights the selection** of what the character receives. Ability scores are *not* derived by
counting what a random draw happened to produce.

This settles Julio's objection to the council's framing. Dialog 0010 was still reasoning
"observe what got drawn, then set the scores", which keeps the arrow pointing the wrong way and
needs a look-ahead pass to work at all. Pointed forward, no look-ahead is required.

**2. Affinity is spent, not merely held.**

A feature contributes affinity only where it **spends** the ability. A spell that rolls a save DC
or an attack roll spends the casting ability; a utility cantrip does not.

> *"Some spells do not ask for spell DC or rolls. The fact that you cast Light with CHA is
> worthless for an Aasimar, just thematic and aesthetic."* — Julio

So Light, Prestidigitation and Thaumaturgy generate **zero** affinity. They are costume. Without
this rule the model concludes that every caster wants every casting ability, which is how a sheet
ends up carrying two spellcasting abilities that disagree.

**3. A Guild speaks in proportion to its share of the goal level.**

A multiclass dip is not "a thing you did" — this is a generator, not a table, and the whole path is
known when the sheet is emitted. A Rogue 1 / Wizard 19 is a Wizard who owns a dagger. The Guild's
weight scales with `char.guild_levels` against the goal level. Single-class characters are
unaffected.

**4. Equipment adapts last.**

The one place the arrow legitimately runs backward is the kit, because the evidence only exists
after the feats are drawn:

> *"If I make a martial, and it doesn't need strength for anything, but it randomly selected feats
> that need dex, then I'd just grab a rapier."* — Julio

Resolved by a comparison at equipment time, not by a model: where Dexterity exceeds Strength, prefer
**Finesse** weapons, which the 2024 rules already let the wielder attack and damage with either
ability. No re-rolling of scores; the character adapts what it carries.

**5. The interest-counting look-ahead is not built.**

No simulate-and-rewind pass, and no goal-level summation of declared interests as the primary
mechanism. Affinity is read from identity, which is cheaper and needs no purity guard.

## Reasoning

The council's common ground held: the mechanism must be declarative, must not simulate progression,
and a Guild's say must scale with its share of the goal level. What Julio changed was the direction
of the inference, and it makes most of the proposed machinery unnecessary.

Two facts decided it. First, `Character.Dice_Bag` keys on `f"{seed}|{purpose}|{version}"` with level
deliberately absent, so a named draw answers identically at level 1 and level 20 — the path is
knowable without running it. Second, the Wizard's Algorithm A was unsafe in practice: 196 of 283
`Pick` sites drew from the Character's single stream, so any throwaway pass would have moved that
state and the rebuild would not have reproduced the character it measured.

Pointing the arrow forward dissolves both concerns. `Pick(options, weights)` already takes weights,
so "weighted by affinity" is the call signature the codebase has; nothing needs to be counted after
the fact.

The spent-not-held rule is what keeps the model honest. It is also what makes the half-caster
question answerable from evidence rather than from a tuning constant: whether a build holds
**True Strike** — which attacks *and* damages with the spellcasting ability — is a fact about the
build, not a temperature someone chose.

## Alternatives not chosen

- **Simulate and rewind (council's Algorithm A).** Exact, but doubles generation cost and was unsafe
  against the shared draw stream. Rejected by the council before it reached Julio.
- **Count declared interests at the goal level (Algorithm B, as framed).** Pure and cheap, but keeps
  the inference backward: it still derives what a character is *for* from what it happened to
  receive. Superseded rather than refuted — the declaration surface it proposed may return if
  affinity alone proves too coarse.
- **Subclass-only weighting (the cheap fallback).** Nearly free, but cannot express the
  martial-who-drew-Dexterity-feats case at all, which was one of the two cases that prompted the
  question.
- **Softmax temperature for half-caster variance.** A global dial cannot produce variance for a
  Paladin without producing it for a Wizard, because every class currently declares the same gap
  between its first and second choice. Left unbuilt: under this Decree the contest is settled by
  what the build carries.

## Consequences

- **Q-0013 is settled; Dialog 0010 is closed** and linked from here.
- **The RNG refactor landed as a prerequisite** (this session). Every `Pick` now draws from a named
  Dice Bag — 87 explicitly, 196 through a purpose derived from the calling `module.function` — and
  the ability array has its own bag (`identity.scores`). Weighted selection is only stable because
  of this. **Every previously generated seed now yields a different character**; saved share-links
  from before this change do not reproduce.
- **Remaining migration:** the 196 derived purposes should become explicit dotted purposes
  (`identity.*`, `magic.*`), since a derived purpose changes if its function is renamed or moved.
  `Roll`/`Dice` still use the single stream for hit points and damage, which are not identity.
- **Constraint on implementers:** affinity weights are a **nudge, not a filter**. Hard-filtering the
  options would make every Covenantor pick the same Wisdom-friendly spells and flatten the variety
  the generator exists to produce.
- **Not decided here**, and still open from the Vox report:
  1. the **goal level** default (20, the sheet's own level, or a caller parameter) — it changes what
     a level-1 sheet looks like, and makes the goal part of identity;
  2. how much **deliberate slack** survives, given the Lorekeeper's caution that a party of
     build-optimal characters has no texture.
- **Canon note owed:** subclass is known at level 1 here, while the 2024 rules place the choice at
  level 3 for every class. A deliberate divergence, and it should be recorded rather than left for a
  rules-lawyer to find.
