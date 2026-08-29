# Dialog 0010 — Build interests and the goal level

- **Question:** Should ability scores be decided by *interests the build declares for its goal level* (counting what the finished character will actually use), rather than by a class's static preference order?
- **Raised by:** Julio
- **Related Questae:** QST-0049 (ability weights), Decree pending
- **Consuls called:** Architecture (Druid), Methods (Wizard), Contracts (Warlock), Flow (Sorcerer), Testing (Rogue), Simplicity (Monk), Lorekeeper
- **Status:** 🟢 converged

---

## 🧭 Framing

The ability-weight model was just unified into one dictionary (`GuildKit.ability_weights`), with
ordered `ABILITY_PREFERENCE` declarations converted to rank-decayed weights. Two views read it:
`ability_preference` (the ordering) and `guild_ability_prefs` (the top two, which the rolled array
uses).

Julio raises a deeper objection to how that model treats a multiclass dip. The implementation
weighs a dip as an origin, on the reasoning that "two levels of Wizard is a thing you did, not a
thing you are." **That reasoning is wrong for this project**, and the reason it is wrong reframes
the whole model:

> *"We are a generator, not a game. We know the path it will take. If we optimize for a goal level
> (5, 10, 20 maybe) we can know upfront what choices we need to make upfront. If I run the choices
> I will be taking and spells I'll know at level 20 then I can just count how many of my spells ask
> for a spell attack or a DC, and add 1 to my spellcasting score interest, even if I am built at
> level 1. We know the subclass at level 1, even when technically that doesn't apply."*

And the case where the answer is genuinely unknown until the build exists:

> *"If I make a martial, and it doesn't need strength for anything, but it randomly selected feats
> that need dex, then I'd just grab a rapier. One of dex/str is important, but you don't know which
> one upfront."*

The proposal: **model build interests as Tags carrying the dictionary, rank the build's interests,
and prioritize at construction.** With a stated fallback if that is too much: weight the extra
things already known (the subclass) instead.

### Two facts the council must reason from

Both were verified in the codebase before this Dialog opened.

**1. The path is already knowable.** `Character.Dice_Bag` seeds from
`f"{char.seed}|{purpose}|{version}"` and its docstring states that *level is deliberately absent*.
Any draw made from a named bag returns the same answer whether asked at level 1 or level 20. The
generator does not need to *simulate* progression to know it: for named bags, look-ahead is free
and exact.

**2. Only 96 of 327 `Pick` sites use a named bag.** 158 sites draw with no `dice=` at all, from
shared RNG state. Those are **order-dependent**: any look-ahead pass that actually *runs* them
early would consume that state and change the character that finally gets built.

### Constraints from Canon

- `Canon/TagKit-Doctrine.md` — Tags declare; collectors obey. No side registers.
- Identity draws must survive a level-up (the named, level-free bag discipline).
- One model, not three (the unification just landed; do not re-fork it).

### Out of scope

The half-caster variance question (softmax temperature, contested gaps) is downstream of this: if
interests are counted, a Paladin's contest may resolve itself from what the build actually holds.

---

## 🗣️ Deliberation

**Architecture Consul (Druid):** Julio is right and my own last recommendation was wrong. I weighed
a dip as an origin because I was reasoning about a *player at a table* who dipped at level 8 and
must live with it. That character does not exist here. The generator emits a finished level-N
sheet; there is no "later." A Rogue 1 / Wizard 19 is a Wizard who owns a dagger. Weighing the
Wizard side as an origin produces a character built for the wrong thing.

The correction is not a new constant, it is a change of *unit*. The Guild's opinion should be
weighted by **its share of the goal level**, which the Character already publishes in
`char.guild_levels`. Rogue 1 / Wizard 2 leans Wizard by 2:1; Rogue 10 / Wizard 2 leans Rogue by
5:1. Nothing needs to know which was "primary."

Structurally I want to name the thing being built. Right now `ABILITY_PREFERENCE` conflates two
different claims: *"my class is about Strength"* (an identity) and *"seventeen of my level-20
spells roll a save DC"* (a count of evidence). Those should not be the same field. I propose a
second, additive channel — call it an **Interest** — that accumulates evidence, while
`ABILITY_PREFERENCE` keeps stating identity.

**Methods Consul (Wizard):** Agreed on the unit, and I want to be precise about what "counting"
means, because there are two very different algorithms hiding in Julio's sentence and only one of
them is affordable.

*Algorithm A — simulate then rewind.* Build the character to the goal level, observe what it holds,
throw it away, rebuild with the observed weights. Cost: two full generations. Correctness: exact.
And per the framing's second fact, it is **not safe today** — 158 draw sites would advance shared
RNG during the throwaway pass, so the rebuild would not reproduce the character we measured. We
would be optimizing for a build that then fails to occur.

*Algorithm B — declared interests, no simulation.* Nothing needs to be run. A spell does not have
to be *drawn* to know it asks for a DC; the Spell Tag can say so. A Training Tag knows its own
`min_level`, so the set of features a build will hold at the goal level is a **filter, not a
draw** — pure, cheap, and side-effect free. Sum the declared interests of everything whose
`min_level <= goal_level`, and you have Julio's count without touching the RNG.

Algorithm B gets most of A's value at a fraction of the cost, and it is the one I recommend. The
count is a sum over a filtered set:

```python
def build_interests(char, goal_level=None):
	"""What this build will actually use, by the level it is built for."""
	goal = int(goal_level or getattr(char, "goal_level", 0) or char.level)
	interest = dict.fromkeys(ABILITY_KEYS, 0)

	for tag in Tags(char):
		for source in tag.__mro__:
			wants = source.__dict__.get("ABILITY_INTEREST")
			if wants is None:
				continue
			if int(getattr(source, "MIN_LEVEL", 1)) > goal:
				continue          # it never arrives; it gets no vote
			for key, points in dict(wants).items():
				if key in interest:
					interest[key] += int(points)

	return interest
```

**Contracts Consul (Warlock):** I will hold the invariants, because this proposal quietly
introduces a new one and it needs to be said aloud.

`ABILITY_INTEREST` and `ABILITY_PREFERENCE` must not be the same kind of number. Preference is
**ordinal and bounded** — a class's order, where rank 1 beats rank 2 no matter how much evidence
piles up. Interest is **cardinal and unbounded** — it counts things, and seventeen spells really
should outweigh three. Mixing them in one addition is how a Wizard ends up with a Constitution
primary because it happens to hold many Constitution-ish features.

So the contract is: **interest ranks within a band, it does not cross bands.** Concretely,
interest resolves ties and orders the contested region; it never lifts an ability past the Guild's
declared lead. That keeps the guarantee the unification just bought us (a declared order survives
intact) while giving Julio the evidence-driven ordering he wants inside it.

The second invariant: **an interest must name its evidence.** `+1 CHA` with no reason is a magic
number that nobody can audit in six months. I want the declaration to carry what it counted:

```python
class Spell(Tag):
	ABILITY_INTEREST = {}          # default: a spell wants nothing

class Attack_Roll_Spell(Spell):
	"""Rolls against AC, so it wants the casting ability high."""
	ABILITY_INTEREST = {"CASTING": 1}

class Save_DC_Spell(Spell):
	"""Sets a DC, so it wants the casting ability high."""
	ABILITY_INTEREST = {"CASTING": 1}
```

Note `"CASTING"` rather than `"CHA"`. A spell does not know which ability casts it — the Character
does, via `Casting_Ability`. Writing `CHA` in a spell would break the Occultist the moment it was
counted. The collector resolves the symbolic key. This is the same substitution the Casting Variant
already performs, and it must be reused, not reinvented.

**Flow Consul (Sorcerer):** My lens is ordering, and this is where the proposal is genuinely hard.

Today: `Apply_Guild → Apply_Specialization → Apply_Background → set_combat_attributes → set_stats →
set_char_features`. Interests want to be counted **before** `set_stats`, because they decide the
array. But Julio's rapier case is evidence that only exists **after** `set_char_features`, because
the feats are drawn there.

That is a real cycle and I will not pretend otherwise. But it is not one cycle, it is two different
questions that got the same name:

- **Declared interests** (spells, class features, subclass) are knowable from the Tags and
  `min_level` *before any draw*. These are pure. They can be counted at any time and want to be
  counted early.
- **Drawn interests** (which feats happened to come up) are only knowable after the draw.

So: count the declared ones before `set_stats`, and let the drawn ones inform only what is chosen
*after* they exist. Julio's own example already respects this split — he does not re-roll his
Strength because he drew Dexterity feats, he **grabs a rapier**. Equipment is selected in
`set_char_features`, after feats. The evidence and the decision are already on the same side of the
line.

I propose no second pass and no fixpoint. One extra step, before the scores:

```
Apply_Guild → Apply_Specialization → Apply_Background
	→ Settle_Interests(char, goal_level)      # new: pure, no draws
	→ set_combat_attributes → set_stats → set_char_features
```

**Testing Consul (Rogue):** I want to break this, and I have three ways.

*One — the look-ahead that eats the seed.* Already named in the framing, and it is why I object to
Algorithm A on sight. But I want the guard written down rather than left as good intentions: the
interest pass must be **provably pure**. That is testable, and cheaply: snapshot the shared RNG
state around `Settle_Interests` and assert it did not move.

```python
state = random.getstate()
Settle_Interests(char, goal_level=20)
assert random.getstate() == state, "the interest pass consumed the seed"
```

*Two — the goal level that changes the level-1 sheet.* If a character built at level 1 for a goal
of 20 gets a different array than one built at level 1 for a goal of 1, then `goal_level` is part
of identity and must be recorded, or the same seed yields two different characters and share-links
break. I am not objecting to that — I think it is correct and desirable — but it must be
**explicit**: `goal_level` becomes a generation parameter with a default, and it goes in the sheet
data.

*Three — the empty build.* A level-1 Fighter has almost no features. If interests are counted and
the class's declared preference is not, an early character has no opinion at all. The Warlock's
band rule already prevents this, and I am satisfied by it, but the test I want is the boring one:
every class at every level from 1 to 20 still produces a primary ability, and it is never `None`.

**Simplicity Consul (Monk):** I am the one who is supposed to ask whether this is too much, and
Julio pre-empted me by offering the fallback himself.

Let me weigh it honestly. The **full** proposal requires: an `ABILITY_INTEREST` declaration on
spells, class features, feats and subclasses; a symbolic `CASTING` key; a goal-level filter; a new
pass; and a purity guard. That is a real amount of new surface, and most of it must be *authored*
— someone has to go and mark seventeen spells.

The **fallback** Julio names — "weight additional features we have, like knowing the subclass" — is
nearly free, because the subclass Tag is already applied at level 1 and already carries
`ABILITY_PREFERENCE`. We are already doing it.

So I will say the unpopular thing: the value here is not evenly distributed. Counting *spells* is
the expensive half and the low-yield one, because a full caster's casting ability is already ranked
first by its Guild and no amount of counting will change it. Counting is only decisive where the
class is **genuinely contested** — the half-casters, the gish subclasses, and the martial whose
Strength has no job. That is maybe six classes out of thirteen.

My concrete proposal: **build the mechanism, but declare interests only where they can change an
outcome.** An `ABILITY_INTEREST` that is absent costs nothing and means "no opinion." Start with
the contested classes and the drawn feats; leave the spell corpus unmarked until a case proves it
matters. This also means we never have to mark 81 spells to get the first result.

**Lorekeeper (Elf Sage):** Two rules checks, one caution, and a correction to Julio's example that
strengthens it.

*The correction.* Julio's rapier is exactly right and the rule is worth naming: the 2024 Finesse
property lets the wielder choose Strength **or** Dexterity for both attack and damage. So a martial
who drew Dexterity feats does not need a different *stat*, it needs a different *weapon* — and the
generator already owns weapon selection. This is the cheapest win on the table and it needs no
interest model at all: **if the build's Dexterity exceeds its Strength, prefer Finesse weapons.**
That is one comparison at equipment time.

*Check one.* Counting spells "that ask for a spell attack or a DC" is sound as a measure of caster
investment, but the two are not equivalent in the 2024 rules. A save-DC spell uses the DC every
single cast against every target; an attack-roll spell rolls once per target. If we ever weight
them, the DC spell is worth more. I would not build that distinction now, but do not bake in the
assumption that they are equal by writing them as the same number without a note.

*Check two.* "We know the subclass at level 1, even when technically that doesn't apply" — this is
true for the generator and it is also true in 2024 for exactly one class. The 2024 PHB moved
subclass choice to level 3 for every class. So a level-1 or level-2 sheet showing a subclass is
already a deliberate divergence from RAW. I am not objecting; the generator's whole premise is a
finished character. But it should be a *recorded* divergence, because a rules-lawyer will find it.

*The caution.* Optimizing toward a goal level makes every generated character **build-optimal**,
and a party of build-optimal characters is a party with no texture. The Wizard with a 9 Strength is
funnier and more playable than the Wizard with a defensible Strength. I would like whatever lands
here to keep a deliberate slack — the same instinct that made the Occultist a 5% easter egg rather
than a menu option.

**Architecture Consul (Druid):** Conceding to the Monk on scope and building on the Lorekeeper's
correction. The Finesse rule is the proof that this proposal has a cheap half and an expensive half,
and they can ship separately. The cheap half needs no `ABILITY_INTEREST` at all: the *comparison*
happens at equipment time between two numbers that already exist.

Revised structural proposal, in the order I would land it:

1. **Guild weight by level share** (fixes the dip; uses `char.guild_levels`, already published).
2. **Goal level as a recorded generation parameter** (Rogue's point two).
3. **`ABILITY_INTEREST` on Tags, filtered by `min_level`, resolving inside the band** (Warlock's
   contract, Wizard's Algorithm B).
4. **Finesse-aware weapon choice** (Lorekeeper; independent of 1–3 and shippable immediately).

**Methods Consul (Wizard):** Accepting the Monk's staging without reservation — a sparse
declaration is strictly better than an exhaustive one here, because an absent `ABILITY_INTEREST` is
already the correct default. I withdraw any suggestion of marking the spell corpus up front.

One refinement to the Druid's item 1, since it is the piece that answers Julio's actual objection
and I want it exact. Level share should scale the Guild's opinion, not replace its rank decay:

```python
@staticmethod
def ABILITY_WEIGHT(char, source):
	"""A Guild speaks in proportion to how much of this build it is."""
	levels = getattr(char, "guild_levels", None) or {}
	mine = int(levels.get(getattr(source, "NAME", None), 0))
	total = sum(levels.values()) or int(getattr(char, "level", 1) or 1)

	if not mine:
		return WEIGHT_ORIGIN

	return max(
		round(WEIGHT_CLASS * mine / total),
		WEIGHT_ORIGIN,
		)
```

Rogue 1 / Wizard 2 → Rogue 33, Wizard 67: the Wizard side leads, which is Julio's point. Rogue 10 /
Wizard 2 → Rogue 83, Wizard 17: the Rogue leads. Single-class is unchanged at 100, so twelve of
thirteen guilds see no difference whatsoever.

**Contracts Consul (Warlock):** That satisfies my band invariant as long as one thing is stated:
with proportional weights, two Guilds at equal levels tie at 50/50 and their rank decay then decides
between them. A Fighter 10 / Wizard 10 would get `STR 50, CON 40` against `INT 50, CON 40` — a tie
on the lead and a *doubled* Constitution. That is arguably the correct answer for a gish, and I am
content, but it must be a **declared** outcome and not an accident. Add it to the test matrix.

**Testing Consul (Rogue):** Taking that as a test case, along with my three. No unanswered
objection from me if the purity assertion and the goal-level recording both land.

**Simplicity Consul (Monk):** No unanswered objection. The staged version is small enough that
items 1 and 4 could land this week and 2–3 could wait for a case that demands them.

**Lorekeeper (Elf Sage):** No unanswered objection, provided the subclass-before-level-3 divergence
is recorded in Canon rather than left implicit, and the slack survives.

---

## ✅ Convergence check
- [x] Every called Consul has spoken.
- [x] Every objection has been answered or conceded.
- [x] At least one concrete proposal (with code sketch) is on the table.

---

## 🕊️ Vox report

**The question.** Should ability scores follow *interests the build declares for its goal level*
rather than a class's static preference order?

**Common ground.** All seven Consuls agree Julio's core objection is correct and the current
treatment of a multiclass dip is wrong: this is a generator, the whole path is known, and a Guild's
say should scale with **its share of the goal level**. All agree the mechanism must be *declarative*
— Tags state what they want, a collector sums — and that no simulation of progression should occur.
All agree the work splits into a cheap half and an expensive half that can ship separately.

**The options.**

| Option | What it is | Tradeoff |
|---|---|---|
| **A — Simulate and rewind** | build to the goal level, measure, rebuild | Exact, but **unsafe today**: 158 of 327 draw sites use no named bag, so the throwaway pass would move shared RNG and the rebuild would not reproduce what was measured. Also doubles generation cost. Rejected by the council. |
| **B — Declared interests, filtered by `min_level`** | Tags declare `ABILITY_INTEREST`; sum whatever arrives by the goal level; no draws | Pure, cheap, exact for everything that is not itself random. Needs new authored declarations. **Recommended.** |
| **C — Subclass-only weighting** (Julio's own fallback) | use what is already applied at level 1 | Nearly free, already half-built. Cannot express the martial-with-Dex-feats case at all. |
| **D — Finesse-aware equipment** | if Dexterity exceeds Strength, prefer Finesse weapons | Independent of all the above, one comparison, needs no model. Solves Julio's rapier case outright. |

**Who favored what.** Druid and Wizard led on B with the level-share fix as its first step. Monk
argued B should be built but **declared sparsely** — only where it can change an outcome — and
warned that marking the spell corpus is the expensive, low-yield half, since a full caster's casting
ability is already ranked first. Warlock accepted B under a strict contract: interest is cardinal
and orders *within* a band, preference is ordinal and sets the band, and the two must never be added
across. Sorcerer resolved the apparent circularity by splitting declared interests (knowable before
the scores) from drawn interests (only knowable after), noting Julio's own example already respects
the split. Rogue accepted B conditional on a purity assertion and on `goal_level` becoming a
recorded generation parameter. Lorekeeper supplied option D from the 2024 Finesse rule and asked
that deliberate slack survive optimization.

**Code proposals.** `ABILITY_WEIGHT` scaling by `guild_levels` share (Wizard, above);
`build_interests` as a filtered sum over `Tags(char)` (Wizard); symbolic `"CASTING"` interest keys
resolved through the existing `Casting_Ability` substitution (Warlock); one new pure step
`Settle_Interests` before `set_stats` (Sorcerer); RNG-purity assertion (Rogue).

**Vox's synthesis.** The council's leading recommendation is **B, staged, in four steps** — level
share first (it answers Julio's objection directly and touches only multiclass characters), then
goal level as a recorded parameter, then `ABILITY_INTEREST` declared sparsely on contested classes
and drawn feats, with the spell corpus left unmarked until a case demands it.

The strongest alternative is **D alone**: ship Finesse-aware weapon choice and the level-share fix,
and stop. That covers Julio's two concrete examples — the dip and the rapier — for a fraction of the
work, and leaves the interest model unbuilt until something needs it that these two do not reach.

Three items are decisions Vox will not make, and carries to Julio:

1. **Goal level default** — 20, the sheet's own level, or a generation parameter the caller sets?
   This changes what a level-1 sheet looks like.
2. **Scope of declaration** — contested classes only (Monk), or the full corpus including spells?
3. **The slack** — how much deliberate sub-optimality survives, given that a party of
   build-optimal characters has no texture (Lorekeeper).

→ Awaiting Julio's decision. To be recorded as Decree 0004.
