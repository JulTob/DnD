# ✨ Spells and Invocations: what a caster knows, and why

> 🚧 **Draft.** Analysis and proposals, not yet authoritative. Under review.

*Wiki entry for the design team. `AtlasMagia/Lodge_of_Spells.py` holds the
spells, `AtlasMagia/SpellsKit.py` their Tags, `Grimoire_of_Spellcasters.py`
the per-Guild draw, `InvocationKit.py` and `Map_of_Eldritch_Invocations.py`
the Warlock's clauses. Compiled 2026-09-08 from the code and six generated
casters (seed 42, levels 5 and 7).*

> **In one sentence.** A spell list is a biography, and the generator writes
> it by drawing uniformly from the whole class list: a Bladesinger at level 5
> knows Tenser's Floating Disk, Gentle Repose and Arcane Lock and no damage
> cantrip, and nothing about the sheet explains where that Wizard studied.

---

## 1. Inventory

| Layer | Count | State |
|---|---|---|
| Spell instances in the Lodge | 319 | Full 2024 texts with bold labels and explicit breaks (*Fireball*, *Eldritch Blast*, *Cure Wounds*). ✅ The register is the rulebook's, which is correct for shared rules. |
| `SPELL_DATA_2024` dict in the same file | 136 | Compressed one-liners ("Up to ten creatures gain the ability to breathe underwater for a full day"), six with "(scaling with level)" shorthand, levels 0 and 3 to 9 only. A second, thinner registry for spells the first already has. |
| Class lists (`SPELL_LISTS`) | Wizard 293, Arcane Trickster 174, Bard 141, Warlock 141, Druid 136, Sorcerer 123, Cleric 101, Artificer 80, Eldritch Knight 60, Ranger 58, Paladin 49 | Hand-built per level. Wizard level 2 holds 79 spells, which is the Legacy layer mixed in. Expansion spells (*Green Flame Blade, Earthbind, Raulothim's Psychic Lance*) sit in the Warlock list unmarked; the `Legacy` Tag exists for this. |
| Eldritch Invocations | 28 | "Seven shapes wearing different spell names": `at_will`, `free_cast`, `sense`, `choose_cantrip`, `familiar`, `origin_feat`, `apply`. ✅ The InvocationKit docstring is a model design note. |
| Spell Tags | School (exclusive), Tradition (Arcane/Divine/Primal), Ritual, Legacy | ✅ The vocabulary a themed draw would need is already declared. |
| Monk Focus techniques | 5 | Live in the Lodge of Spells, which is not their house. |

---

## 2. How spells are chosen

`Spellcaster.available_spells` takes the class list up to the highest slot
level, adds the Order's spells if the Character swore one, and
`_pick_distinct` draws the quota **uniformly** through the Character's Dice.
Nothing tilts it: not the Arcane Tradition, not the school, not the drawn
Spellbook, not the background, not the species or its culture.

The one exception is the **Warlock**, which reads its patron: Celestial, Fiend,
Great Old One and Archfey each add their always-prepared spells, and the 2014
Genie still adds its four elemental courts (Dao, Djinni, Efreeti, Marid), drawn
from a named Dice Bag. ✅ This is what every caster should do.

| Caster (seed 42) | What the draw produced |
|---|---|
| Wizard, Bladesinger, L5 | True Strike, Mind Sliver, Thunderclap, Friends; Tasha's Hideous Laughter, Witch Bolt, Tenser's Floating Disk, Gentle Repose, Arcane Lock, See Invisibility, Major Image, Protection from Energy, Summon Fey. A Spellbook of palm leaves. No school, no story. |
| Warlock, Celestial, L7 | Patron spells present (Aid, Cure Wounds, Guiding Bolt, Light, Sacred Flame, Daylight, Revivify, Guardian of Faith, Wall of Fire). Invocations: Agonizing Blast, Eldritch Mind, Ascendant Step, **Fiendish Vigor, Devil's Sight, Armor of Shadows**. A Celestial's clauses, named for a Fiend's. |
| Cleric, Light, L5 | Fourteen spells. The Light Domain's always-prepared spells are listed in a Feature ("3rd: Burning Hands, Faerie Fire…") and **absent from the spell cards**. |
| Sorcerer, Clockwork, L5 | Eleven spells. **No subclass spells**: the 2024 always-prepared lists for Draconic, Clockwork, Aberrant and Wild Magic are not added (the Warlock branch has them; the Sorcerer branch has zero). |
| Druid, Moon, L5 | Fine. Message and Find Familiar arrived through a background's Magic Initiate, correctly. |
| Bard, Glamour, L5 | **Resurrection (level 7) and Find the Path (level 6)** on a level-5 sheet. The Bard's baseline pool takes every level above 0 and is never capped by slot level. |

---

## 3. What the draw should know

*Decree 0005 §1 already states the principle: "A build's affinity is known before
anything is drawn… Affinity therefore weights the selection of what the
character receives." A spell list drawn uniformly is the one large selection on
the sheet that affinity does not yet weight. §2 of the same Decree calls Light,
Prestidigitation and Thaumaturgy "costume": the tilt proposed below is for the
spells that spend the ability, which is the Decree's own distinction.*

**Principle.** A spell list is where the Guild's register meets the Character's
biography. The list should be a *weighted* draw, never a lock (the Decree 0005
shape), with three tilts that already have data behind them:

1. **The specialization.** An Evoker leans Evocation; an Illusionist, Illusion;
   a Bladesinger toward the blade cantrips; a Light Cleric toward fire and
   sight. The School and Tradition Tags exist; the weights do not.
2. **The subclass's own spells, where the rules give them.** Sorcerer Origins,
   Cleric Domains (into the cards, not only the Feature), Paladin Oaths, Ranger
   archetypes, Druid Circles. The Warlock already does it.
3. **The drawn object.** The Wizard's Spellbook and the Cleric's holy symbol
   are drawn by tool and culture and say nothing about the spells. A Spellbook
   of palm leaves is a southern book; a book "bound in a hide nobody
   recognises" is a Great Old One's. One weight per material keyed to a
   school would make the object and the list agree without a word.

**What it buys.** The Wizard page found the class has no fantasy line of its
own; the Wizard's fantasy is *what they know*, and a coherent list is the line.
The Sorcerer page said each Origin ends on what the body is turning into; the
Origin's spells are that body's vocabulary.

---

## 4. The Warlock's clauses

✅ **The design is right.** Twenty-eight invocations as seven declared shapes,
prerequisites as Tags ("Tag membership is the question TagKit exists to
answer"), effects landing on plain attributes. `Apply_Warlock_Invocations`
draws with `Accept` from the eligible pool until the count is met.

⚠️ **The draw ignores the patron**, and the invocation names carry a register
the patron does not share. A Celestial Warlock issued *Devil's Sight, Fiendish
Vigor* and *Armor of Shadows* reads as a Fiend's. A tilt per patron would fix
most sheets and leave the exceptions as stories (the light issued you eyes for
the dark):

| Patron | Leans toward |
|---|---|
| Celestial | Ascendant Step, Gift of the Protectors, Eldritch Mind, Lessons of the First Ones |
| Fiend | Fiendish Vigor, Devil's Sight, Armor of Shadows, Lifedrinker |
| Great Old One | Gaze of Two Minds, Witch Sight, Eldritch Mind, Whispers of the Grave |
| Archfey | Mask of Many Faces, Misty Visions, One with Shadows, Master of Myriad Forms |

⚠️ **Open-choice language survives.** Agonizing Blast, Eldritch Spear and
Repelling Blast print "Choose one of your known Warlock cantrips". The choice
is made (`enhanced_cantrips` is recorded) and never printed. The sheet should
read *Agonizing Blast (Mind Sliver)*. Lessons of the First Ones prints "of
your choice (see Origin Feats in FeaturesKit)": a code reference on a sheet.

⚠️⚠️ **The Celestial patron paragraph leaks a Python object.** The sheet reads:

```
that patron of yours, Descent(kind='Star', names=('Polaris', 'Vega', 'Sirius', …)) of Justice
```

`WarlockKit` picks from `DESCENTS` and formats the pick directly; `DESCENTS`
now holds `Descent` records with a `names` tuple, so the paragraph should pick
a name from the Descent, not print the Descent. This is in the best-written
patron text on the sheet ("You wanted redemption? You got a job offer in
hell.") and it is on every Celestial Warlock.

**Lines for the clauses.** The Warlock register is the terms, and an invocation
is a clause. One line each, in the Fiend's interior voice, since the clause is
the same whoever signed:

| Invocation | Draft line |
|---|---|
| Pact of the Blade | *The weapon is the receipt.* |
| Pact of the Chain | *The familiar reports to both of you.* |
| Pact of the Tome | *The book was written before you opened it.* |
| Agonizing Blast | *The clause about pain was your addition.* |
| Eldritch Mind | *Nothing gets between you and the thought. Not even the knife.* |
| Devil's Sight | *You were issued eyes for where they keep things.* |
| Armor of Shadows | *The dark holds you the way a coat does: because it was told to.* |
| Fiendish Vigor | *A little more life each time. Lent.* |
| Mask of Many Faces | *Whose face you wear is in the terms. Which one is not.* |
| Misty Visions | *You show them what is not there. They do the rest.* |
| Repelling Blast | *Distance is the one gift you can give them.* |
| Ascendant Step | *Up is a direction you were given. Not a promise.* |
| Gaze of Two Minds | *You borrow a pair of eyes and give nothing back. Yet.* |
| One with Shadows | *Stand still in the dark and you are part of it. Move, and you are yours again.* |
| Thirsting Blade | *The blade wants twice what you asked. So did you.* |
| Whispers of the Grave | *The dead answer. They were told to.* |
| Lifedrinker | *What it takes, you keep. That was the clause.* |
| Witch Sight | *You see what things are. It has not made you happier.* |
| Lessons of the First Ones | *One lesson from before the terms. They let you keep it.* |
| Gift of the Protectors | *Names in the book. Whoever is written there falls a little slower.* |

---

## 5. The spellcasting section itself

Each caster's section opens on a sentence, and they are the weakest
sentences on the sheet: "As a student of arcane magic, you have learned to
cast spells." "As a student of natural magic, you have learned to cast
spells." "You regain all expended slots when you finish a long rest."

The Guild pages settled a register per class. One opening line each, in it:

| Guild | Draft opening |
|---|---|
| Wizard | *What you know, you took. The book is where you keep the receipts.* |
| Cleric | *You do not cast these. You ask, and they are answered, and you have stopped being surprised.* |
| Druid | *The land lends. You have learned how to ask, and how to give it back.* |
| Sorcerer | *It was in you before you had a word for it. The words came later, and they are still catching up.* |
| Warlock | *Pact Magic. The name is exact. Read the terms.* |
| Bard | *A song is a spell that admits what it is. These are the ones that do not.* |
| Paladin | *The oath speaks. This is what it says when it has to.* |
| Ranger | *What the edge of the map taught, in the only language it has.* |
| Artificer | *Magic is a component. You know where it goes.* |
| Eldritch Knight | *A careful study, between drills.* |
| Arcane Trickster | *Small magic, well placed. The big kind gets you noticed.* |

The Warlock's section title wears a gothic face while every other class uses
the house header (`Map_of_SpellFonts.py`); the file's own note is right that a
page of it would be noise, and one title in it is a voice. ❓ The house
preference for plain Unicode over hosted webfonts applies here; undecided.

---

## 6. Repairs

- Bard pool capped by slot level.
- Sorcerer subclass spells added (Draconic, Clockwork, Aberrant, Wild Magic).
- Cleric Domain spells merged into the cards; Feature ordinals ("3rd") to 2024
  form ("Level 3").
- The Celestial patron `Descent` repr.
- Enhanced cantrip printed; "see Origin Feats in FeaturesKit" removed.
- One spell registry: the 136-entry dict retired or generated from the Lodge.
- Legacy Tag applied to the expansion spells in the Warlock list.
- Focus techniques moved out of the Lodge.

---

## 7. Decisions log

**Standing**: the Lodge's rulebook register for spell texts; the invocation
shapes; the Warlock's patron-keyed spells; uniform draw through the
Character's Dice.

**Open (this page proposes)**: weighted draws by specialization, subclass and
drawn object (§3); patron-tilted invocations (§4); twenty invocation lines;
eleven opening lines (§5).

**Undecided:** the gothic title face.

---

## 8. Pointers

- **Wizard page**: the class with no line of its own; the list as the line.
- **Sorcerer page**: the Origin's spells as the body's vocabulary.
- **Warlock page**: the terms register; the device law.
- **Celestials page**: the Descents and their names.
- **Feature-Text canon**: no open-choice language; resolve what the sheet
  knows.
- **Feats page**: Magic Initiate as the background's way into a list.
