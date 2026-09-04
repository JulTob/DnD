# Dialog 0017: the Druid core fantasy

- **Topic:** The Druid's core fantasy, verified against the 2024 rules, and the provisional class and Circle descriptions for the beta character generator.
- **Commissioned by:** Julio (in chat, 2026-08-31), as part of the all-classes description commission: find the core fantasy through archetypal analysis, verify the rules establish it, write the prose in a register that fits the class.
- **Date:** 2026-08-31
- **Consuls called:** Lorekeeper (Elf Sage), Venustas (Bard), Contracts (Warlock), Simplicity (Monk). Vox reports.
- **Status:** 🟡 provisional. The texts below ship as provisional pending Julio's word.

---

## 🧭 Framing

This commission arrived with no seed from Julio and no found text to inherit.
Both facts were verified before the council spoke:

- `AtlasLusoris/AtlasOfGuilds/DruidKit.py` is a 33-line stub: four bare
  `Build_Specialization` calls (Land, Moon, Sea, Stars), no `extends`, no
  `heading`. The texts proposed here get wired later, following the sibling
  kits' practice (`heading="Circle of the Land"` and so on, rendering the
  Circle paragraphs *under* the class's own).
- The recovery vault holds no Druid prose. Extracting the top-level names from
  `.recovery-vault/GuildKit.cpython-314.pyc` finds exactly four description
  constants: `BARBARIAN_DESCRIPTION`, `FIGHTER_DESCRIPTION`,
  `WARLOCK_DESCRIPTION`, `WIZARD_DESCRIPTION`. This Dialog is a fresh
  derivation, not a reconciliation.
- The rules are real source: `AtlasLusoris/AtlasOfTraining/Map_of_Druid_Training.py`
  (2024 PHB core plus all four Circles, 649 lines). The chassis
  (`GuildKit`): WIS primary, CON secondary, d8 Hit Die, INT and WIS saves,
  medium armor, the Adept vocation it shares with Cleric and Ranger.

One house fact the deliberation leans on: in this project the neighbouring
texts already claim territory. The Barbarian's Wild Heart says "you carry the
wild things in your heart" (the *inner* wild), and the Dragons canon
(`Documenta/Canon/Dragons-and-the-Overcoming.md`) owns self-authorship, the
becoming-what-you-are slot. Whatever the Druid is, it cannot be either of
those, or the roster blurs.

---

## 🗣️ Deliberation

**Lorekeeper (Elf Sage):** Three candidate fantasies, each with its
literature. All three are genuinely druidic; the question is which one is the
trunk and which are branches.

*Candidate A, the elder belonging.* The wild as the older order, and the
druid as someone still on speaking terms with it. The purest page is the
"Piper at the Gates of Dawn" chapter of The Wind in the Willows: Rat and Mole
row into the presence of something older than fear, are known by it, and are
gently made to forget, because mortals cannot carry that memory around. Sir
Gawain and the Green Knight runs on the same current: the Green Man rides
into the young court out of the old world, and the whole poem is the new
order being tested by the elder one. Tolkien's Bombadil ("Eldest, that's
what I am") is the figure the argument cannot touch because he predates the
argument. And Blackwood's "The Willows" is the same elder world with the
warmth removed: vast, indifferent, barely noticing us. In all four, the wild
is not scenery. It is society: an older one, still holding a chair for you.

*Candidate B, the honest shape.* Shapeshifting as truth-telling: the wild as
the true self, and the animal form as the self undisguised. The native well
is the Hanes Taliesin chase: Gwion becomes hare, salmon, wren, grain, and
Ceridwen answers greyhound, otter, hawk, hen, form matching form like
question and answer. Ovid's Metamorphoses makes change the engine of the
whole world. T.H. White's The Sword in the Stone has Merlyn school Wart as
perch, ant, goose and badger, each shape one lesson in being alive. Le Guin's
A Wizard of Earthsea files the caution: Ged stays a hawk too long and nearly
loses the man.

*Candidate C, the forgotten treaty.* The druid as keeper of a covenant
humans no longer remember signing. Princess Mononoke is the master text
(Ashitaka walking between iron town and forest, seeing with eyes unclouded),
Nausicaä its sibling (the poisoned wild is secretly doing the world a
kindness, and needs one interpreter). The Lorax speaks for the trees;
Treebeard is on nobody's side because nobody is altogether on his; Leopold's
A Sand County Almanac argues the community boundary outward until soil and
water and beast are members. And the oldest version is written law: the
sabbath of the land, the corner of the field left unharvested. People really
did once sign.

**Venustas (Bard):** Before we weigh them, two collisions to put on the
table, because they cut Candidate B off at the knees at class level.

First, the Wild Heart. Its found text already says "There is a wild instinct
that maybe everyone carries and few listen to. You listen." and ends
carrying the wild things in its heart. That Path owns the inner wild. A
Druid class text on the thesis "the wild is your true self" would make the
two guilds read as one fantasy at two volumes.

Second, the canon. "Become what you are" is the Dragons' doctrine, the
Ascending, and the house rule there is that nobody on the page gets to
explain it or claim it. A class description built on shapeshifting as
self-authorship walks straight into that reserved ground. If B survives
anywhere, it has to be reframed away from *self* and toward something else.

**Contracts (Warlock):** Then let the rules speak, because they settle it
more cleanly than I expected. I read every core lesson and all four Circles
in `Map_of_Druid_Training.py`.

The single most decisive wording sits inside Wild Shape itself: you
shape-shift into "a Beast form **you have learned**." Learned. Not
unleashed, not revealed, not remembered from some inner deep. The rules
treat every form as outward-facing knowledge, an acquaintance made, which is
the opposite of Candidate B's inner honesty. And the second most decisive
fact is an absence: nothing in the core class mechanics imposes a duty. No
feature rewards protecting anything, no rule punishes a felled tree.
Candidate C's treaty is folklore about the class until level 3, where
exactly one Circle makes it mechanical.

The rules read, each key feature and the one line of what it proves:

| Feature (level) | What it proves about the fantasy |
|---|---|
| Spellcasting (1) | "Drawing on the power of the natural world": the power is drawn, not owned. And the ability is Wisdom, so the craft is perception. Attention, rewarded. |
| Druidic (1) | A secret language, taught, with hidden messages others automatically fail to find. Membership in something older than any kingdom, with letters left for people not yet born. |
| Primal Order (1) | Magician or Warden: two ways of serving the same old order, and the generator settles which. The class prose may lean on neither weapons nor extra spellcraft. |
| Wild Shape (2) | "a Beast form you have learned": forms are acquaintances, not confessions. Duration in hours, not minutes: a way of moving through the world, not a combat trick. |
| Wild Companion (2) | The familiar arrives Fey: the older world sends you company from its own house. |
| Wild Resurgence (5) | Spell slots and Wild Shape convert into each other, both directions. Speaking with the wild and wearing the wild are one currency. |
| Elemental Fury (7) | The same elemental might backs the cantrip and the claw. Whichever hand you use, the same world is behind it. |
| Beast Spells (18) | You keep your speech inside the borrowed body. The two halves of the craft stop being halves. |
| Archdruid (20) | Unlimited shapes, and the body ages one year in every ten. The wild starts keeping you on its own calendar. |

What this table describes is Candidate A, sharpened: not vague belonging but
**membership maintained through attention**. Wisdom is the engine, Druidic
is the passport, the shapes are the vocabulary, and Archdruid is the elder
world adopting your clock at the end. The treaty never appears; the true
self never appears; the long acquaintance appears at levels 1, 2, 5, 18 and
20.

**Lorekeeper (Elf Sage):** Conceded at class level, on both B and C, with
the migrations flagged so nothing is lost. B does not die, it *reframes* and
moves to the Moon, where the subclass is literally named for the one body
that changes every night and is never anything but itself. Shapeshifting as
honesty survives there in the only form the rules permit: not "the beast is
the real you" but "you change the way the moon changes, and every phase is
true." Le Guin's caution is answered by the same figure: the moon has never
once failed to come back. And C moves to the Land, the one Circle whose
level-14 feature is the treaty made visible: Nature's Sanctuary, where beast
and plant must save against their own wish to strike you. The class refuses
the duty; a Circle may keep the covenant. That contrast is roster texture,
exactly as the Barbarian keeps possession out of the class and gives it to
the Zealot.

**Venustas (Bard):** Now the register, because for this class it can be
derived rather than invented. The engine is Wisdom, the craft is attention,
so the prose should *perform* attention: the register of **nature writing,
the field diary kept by someone who walks**. Grahame is its warm pole,
Leopold its ethical pole, Mary Oliver its devotional pole ("attention is the
beginning of devotion" is practically the Druid's Spellcasting entry), and
the sentences move at walking pace. Concrete senses over abstractions: crows,
rain, the two kinds of silence. Metaphors kept domestic and warm (a friend's
coat, letters waiting) rather than grand, because the thesis is familiarity
with the elder world, not awe before it. Awe is the World Tree Barbarian's
register; the Druid is past awe, the way you are past awe with an old
friend.

Against the siblings, so the shelf reads as a set: the Barbarian chants, the
Fighter talks between drills, the Warlock confesses, the Wizard writes
aphorisms. The Druid *notices*. And one deliberate register shift at the
close: the last three sentences of the class text go geological ("Mountains
count in winters. Forests count in centuries. So, in time, will you."),
which is Archdruid's slowed ageing performed as rhythm, the sentences
lengthening their own units of time. The Fighter's "When Death comes for
you, it will not collect" is the precedent for letting the closing line
reach for the level-20 truth.

**Simplicity (Monk):** My lens is the knife, and for a fresh derivation the
knife guards against three temptations rather than against edits.

*The eco-sermon.* The moment the class text scolds anybody, it moral-locks a
class the way we refuse to moral-lock backgrounds. The wild being older than
walls is a fact of the setting; walls being wrong would be a doctrine. The
drafts must stay non-adversarial: the druid is not against the city, the
druid simply never dropped the older acquaintance. I will read every line
for a wagging finger.

*The lore-dump.* No order named, no first tree, no history of druidry.
Letters in leaf and stone, an old understanding, people you will never
meet: things a player can inhabit, with the meaning left to them.

*The open choice.* The generator has already settled the Primal Order
(Magician or Warden, drawn in `apply` from a named Dice Bag, per the map),
so the class prose may assume neither armor nor extra cantrip. Likewise the
Land's terrain, re-chosen each Long Rest in 2024, is a genuine at-table
decision and so *may* stay open in its feature entry; the description prose
still should not enumerate options.

Calibration: class at three short paragraphs, each Circle at two. That
matches the Fighter and Fiend density.

**Contracts (Warlock):** The Circle verification, and three findings the
texts must answer rather than write around.

*Land.* Circle Spells keyed to terrain, re-chosen per Long Rest (each
country teaches you its own way of answering); Land's Aid heals allies and
poisons a foe in one gesture (the ground feeds its own and turns on the
rest); Natural Recovery returns spell slots on a Short Rest (rest on the
land and it restores you); Nature's Ward grants Immunity to Poisoned,
Frightened and disease, and natural plants stop impeding you (the place no
longer treats you as a stranger); Nature's Sanctuary at 14 makes Beasts and
Plants save or turn aside (the covenant, visible). The treaty fantasy is
fully funded here and only here.

*Moon.* Circle Forms scale the Beast CR and open the Elementals at 10 (not
even flesh is the limit of the vocabulary); Moon Spells are the night side:
Faerie Fire, Moonbeam, Vampiric Touch, Greater Invisibility. **Finding one:
Vampiric Touch is Necrotic and predatory. The Moon list is genuinely
nocturnal, teeth included, so the text must not paint pure silver.** And a
detail I want on record because it is beautiful: in the 2024 rules Moonbeam
is the spell shapechangers dread (Disadvantage on the save, forced back to
true form). The Moon druid's own light polices false shapes while its Wild
Shape grants true ones. Honesty of shape is not our metaphor imposed on the
kit; it is the kit. Moonlight Step moves you the way light moves; Lunar Form
resists everything but Psychic and Radiant while regenerating: phases do not
destroy the moon.

*Sea.* Wrath of the Sea is an aura: you do not aim the sea, you stand in it
and it happens around you. Aquatic Affinity opens the border (Swim Speed,
water-breathing). Stormborn makes Cold, Lightning and Thunder weather rather
than harm, and pushes with every storm-flavoured spell. **Finding two:
Oceanic Gift computes one number and pays it out both ways, damage to
enemies and the same Hit Points to friends. "It feeds a coast and drowns it
with the same water" is not a metaphor we chose; it is the arithmetic of the
level-14 feature.** No treaty anywhere in this Circle: the sea signs
nothing. The roster texture writes itself: Land signs, Sea never did.

*Stars.* Star Map is attention written down until the record itself becomes
a Focus, with Guidance and Guiding Bolt always ready (the sky repays being
read, in guidance). Cosmic Omen is Hesiod as a Reaction: read the sky at
rest, then tell luck which way to lean, Weal or Woe. **Finding three, and
the structural one: Starry Form spends a use of Wild Shape.** The night sky
is reached through the class's own signature currency. The rules are saying
the stars are one more wilderness, and the constellation figures (Archer,
Chalice, Dragon) are its beasts, lent the same way. Twinkling Constellations
brightens them; Full of Stars turns the watcher partly into the watched,
incorporeal. The arc is attention, then reading, then becoming.

**Venustas (Bard):** Accepting all three findings into the drafts: the
Moon's closing line answers the teeth, the Sea's closing image is the
two-handed wave, and the Stars text ends on becoming what you watched. One
more literary note for the Sea, since the well should be the house's
preferred ones where it can: Hemingway's The Old Man and the Sea gives us
la mar, the sea loved in the feminine and never once trusted, which is the
exact register of a Sea druid's devotion, and Hokusai's Great Wave holds the
whole subclass in one image: beauty, scale and threat in a single curl of
water, the boats small, the mountain smaller. For the Stars, Hesiod's Works
and Days (sow when the Pleiades rise, sail when they set) and the Polynesian
wayfinders, who read stars and swell together and crossed an ocean by
attention alone: the oldest literacy, older than letters.

**Simplicity (Monk):** The drafts below pass my three guards: no sermon, no
proper noun, no open choice. Two flags for Julio rather than for us. The
class close ("So, in time, will you") spends its last breath on the
level-20 truth, like the Fighter's Death line; I judge the precedent
sufficient. And the Land text uses covenant language ("what may be taken and
what must be left") while staying hospitality rather than job; if it reads
as duty to Julio, the fix is one sentence, not a rewrite. No unanswered
objection from me.

**Contracts (Warlock):** No unanswered objection. The rules read stands.

**Lorekeeper (Elf Sage):** No unanswered objection. The migrations are
recorded.

**Venustas (Bard):** No unanswered objection.

---

## 🌿 Circle analyses

Each Circle is a different grammar of the same conversation the class text
opens: the place that answers, the change that stays, the wild that owes
nothing, the wild that outlasts everything.

### Land

**Fantasy in one line:** The old covenant kept: you remember what each place
is owed, and the place remembers you back.

Candidate C, housed where the rules fund it. The evidence is Leopold's land
ethic (the community enlarged until the soil is a member), Treebeard's
weariness, the Lorax's advocacy softened from placard to practice, and the
old written forms of the pact: the field's corner left standing, the
seventh-year rest. The text frames the covenant as hospitality, guest
becoming kin, never as employment. Rules echo: Circle Spells re-learned per
terrain (each country teaches its own way of answering); Land's Aid feeding
allies and poisoning a foe in one gesture; Natural Recovery (rest on the
land and it restores your reach); Nature's Ward (poison forgets your name,
fear finds no hold, green things part); Nature's Sanctuary (beast and briar
turn aside: the treaty made visible at 14).

### Moon

**Fantasy in one line:** Change that stays itself: you change as the moon
changes, and every phase of you is true.

Candidate B, reframed and housed. The Taliesin chase and Ovid stand behind
it; the werewolf myth is inverted (the moon forces a shape on the cursed,
and offers shapes to you); Le Guin's caution about losing the man in the
hawk is answered by the figure itself, because the moon always comes back.
The deliberation's Moonbeam finding anchors the honesty reading in the kit:
this Circle's own light forces false shapes to confess, while its forms are
all true. Rules echo: Circle Forms scaling to Elementals (not even flesh
limits the vocabulary); the nocturnal spell list, teeth included (Vampiric
Touch is in the text's "answer for both"); Improved Circle Forms putting
Radiant moonlight in the claw; Moonlight Step (you move the way light
moves); Lunar Form regenerating under Resistance (phases do not destroy the
moon).

### Sea

**Fantasy in one line:** You keep company with the one wild that never
signed anything, and you carry its weather home.

The contrast Circle: where the Land keeps covenant, the sea owes nothing,
and the Sea druid loves it precisely for never pretending otherwise. The
Odyssey's unappeasable water, Hemingway's la mar (loved in the feminine,
never trusted), Hokusai's one curled wave over the small boats. The fantasy
is devotion without terms: not mastery of the sea but membership in its
weather. Rules echo: Wrath of the Sea as an aura (you stand in the sea and
it happens around you); Aquatic Affinity opening the border (breath, speed);
Stormborn making Cold, Lightning and Thunder into family weather, every
storm-spell shoving like surf; Oceanic Gift computing one number and paying
it as harm to enemies and healing to friends: the same water feeding and
drowning, with no hatred in it anywhere.

### Stars

**Fantasy in one line:** The night sky is the oldest wilderness, and you
learned to read it.

The Circle for the druid whose wild is up. Hesiod's almanac sky (sow at this
rising, sail at that setting), the shepherds and wayfinders who read stars
before anyone read letters, the universal habit of drawing figures on the
dark. The structural finding carries the analysis: Starry Form spends Wild
Shape, so the constellations are this class's beasts, lent from a higher
pasture by the same old friendship. Rules echo: Star Map (watching until the
watching becomes a map, a record that casts); Cosmic Omen (read the sky at
rest, then tip luck Weal or Woe a breath before it lands); Starry Form's
Archer, Chalice and Dragon drawn on you in light; Twinkling Constellations
brightening them; Full of Stars (partly incorporeal: watch anything long
enough, with enough love, and you take on its nature).

---

## ✅ Convergence check

- [x] Every called Consul has spoken.
- [x] Every objection has been answered or conceded.
- [x] The rules read covers every core lesson and all four Circles.
- [x] Proposed texts are on the table; findings flagged for Julio, not
      written around.

---

## 📜 The proposed texts

Plain prose, paragraphs separated by blank lines, ready to lift into the kit
as string constants when the wiring lands (headings per sibling practice:
"Circle of the Land", "Circle of the Moon", "Circle of the Sea", "Circle of
Stars").

**DRUID_DESCRIPTION** (fresh, this Dialog):

```
Walls are young. Roads are young. The wild was here long before either, and it will be here after, and it has not forgotten you. There are letters waiting for you out there, left in leaf and stone by people you will never meet, in a language the cities never learned. You go in under the trees and something old takes notice, the way an old friend takes notice: without any surprise at all.

Your craft is attention. You can sit still long enough to hear a forest change its mind. You know what the crows are arguing about, which silence means rain and which silence means run. People call what you do magic. Most of it is listening. The rest the world does for you, because you ask the way it likes to be asked.

And when asking is not enough, you have shapes. You watched the wolf until you could be the wolf. Every form you wear was learned like a friendship, by walking beside it season after season, and the wild lends you its bodies the way a friend lends a coat. Keep such company long enough and you begin to keep its calendar. Mountains count in winters. Forests count in centuries. So, in time, will you.
```

**LAND_DESCRIPTION** (fresh, this Dialog):

```
There is an old understanding between people and the places that feed them. Most have let it lapse. You keep it. You learn each country the way you would learn a house you are welcomed in: where the water runs, what the soil is owed, what may be taken, what must be left. And a place notices being known. Rest in it and it restores you. Stand your ground and the ground stands with you.

The land keeps you back. Green things part to let you through. Poison forgets your name. Fear finds nothing in you to hold. Even the beast, even the briar, turns aside rather than strike the one who remembered the terms. Nothing was ever signed. Nothing needed to be. That is what keeping faith means.
```

**MOON_DESCRIPTION** (fresh, this Dialog):

```
The moon is never the same two nights running, and it has never once been anything but the moon. That is the lesson you took to heart. You change the way it changes: wholly, openly, on no schedule but your own necessity, and without ever losing the thread of yourself.

Others wear a shape the way they wear a mask. You wear yours the way the moon wears a phase. Wolf, bear, something vast, something with no blood in it at all: each one is true while it lasts, because the constant was never the body. And you keep the night's whole company. There is silver in the dark, and there are teeth in it, and you answer for both.
```

**SEA_DESCRIPTION** (fresh, this Dialog):

```
The land can be lived with. The sea cannot, and never lies about it. It feeds a whole coast and drowns it with the same water. That is why you went to it: of all the wild things, it is the one that has never once pretended to be tame, and you loved it for that.

You came back with its weather in you. Fog follows you like a dog. Thunder waits behind your teeth. Cold and lightning pass you by, the way a storm spares its own. And when you finally open your hands, the wave does what the sea has always done: one water, feeding your people and breaking what stands against them, with no hatred in it anywhere.
```

**STARS_DESCRIPTION** (fresh, this Dialog):

```
One wilderness sits beyond every axe and every wall, and it comes out at dusk. Shepherds learned to read it before anyone read anything else: sow when this rises, sail when that one sets. It is the oldest of the wild places, and the quietest, and you kept its first literacy alive. You watched until the watching became a map.

The sky repays a patient reader. It tells you, a breath early, which way luck is about to lean. It lends you its figures the way the forest lends its beasts: an archer, a chalice, a dragon, drawn on you in light. Watch anything long enough, with enough love, and you begin to take on its nature. You have watched the night for years. That is why you shine.
```

---

## 🕊️ Vox report

**The choice made.** The Druid's core fantasy is **the elder belonging,
sharpened to membership through attention**: the wild is not scenery but an
older society you never left, your craft is attention paid so long that the
world answers, and its shapes are lent to you like a friend's coat. The 2024
rules were verified to establish it: Wisdom casting and "drawing on the
power of the natural world" (attention, rewarded), Druidic's hidden letters
(membership), Wild Shape's forms "you have learned" (acquaintance, not
confession), Wild Resurgence's one currency, and Archdruid's slowed ageing
(the wild adopting your clock). The tone register is **nature writing, the
walker's field diary**: sentences at walking pace, concrete senses, warmth
without awe, with one deliberate geological shift in the class text's
closing tricolon. Each Circle refracts the conversation: Land is the place
that answers (the covenant candidate, housed where Nature's Sanctuary funds
it), Moon is the change that stays itself (the honesty candidate, reframed
and anchored by Moonbeam's own rules), Sea is the wild that signs nothing,
Stars is the wilderness overhead, read until the reader begins to shine.

**The strongest rival.** Candidate C, the forgotten treaty (Mononoke,
Nausicaä, the Lorax, Leopold): rejected at class level because no core
mechanic imposes or rewards guardianship, so a duty-built class text would
promise what the sheet never delivers; preserved at Circle level, where the
Land's features pay the fantasy in full. Candidate B (the wild as the true
self) was cut harder: Wild Shape's own wording makes forms learned rather
than revealed, the Barbarian's Wild Heart already owns the inner wild, and
self-authorship is the Dragons' reserved ground; it survives at the Moon as
change-that-stays-itself.

**Open questions for Julio.**

1. **The class close** ("Mountains count in winters. Forests count in
   centuries. So, in time, will you.") spends its last line on Archdruid's
   level-20 ageing, on the Fighter's "When Death comes for you, it will not
   collect" precedent. Confirm the reach is wanted at class level.
2. **The Moon's teeth.** The council kept the night's predatory side
   ("there are teeth in it, and you answer for both") because Vampiric Touch
   sits on the Moon list. If the Moon should read purely silver, that
   sentence is the one to change, and the rules finding should be recorded
   as overruled rather than unnoticed.
3. **The Land's covenant tone.** Hospitality was chosen over duty
   ("welcomed in", not "sworn to"). If it still reads as a job to Julio,
   the fix is the first paragraph's middle sentence, not the fantasy.
4. **Wiring.** DruidKit.py currently passes no `extends`/`heading`; when the
   texts land, headings should follow sibling practice ("Circle of the
   Land", and so on) so Circle prose renders under the class's own.

→ Awaiting Julio's word. The five texts ship as provisional until then.
