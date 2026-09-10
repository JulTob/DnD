# 🧀 Halfling

> 📖 **In flow.** 1 of 9 chapters are still proposals. 📜 4 · 📚 2 · 📔 2 · 📖 1

> - 📕 **inherited from the 2024 rules.** Moving it costs rules compatibility.
> - 📙 **an aesthetic change.** The same rule wearing our name and look.
> - 📒 **a rule we changed.** A house rule, and it already cost compatibility.
> - 📘 **supportive lore.** It holds a rule or a core element up.
> - 📗 **deep lore.** Design that supports the fantasy rather than a rule.
> - A book marks a statement only if it can change exclusively through the
>   Questa / Agora / Decree system. Anything with no Questa and no Decree behind
>   it carries no book, however settled it feels.

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from the Halfling kit, the species entry, `AtlasNomina/Races/Halfling.py`,
the class analyses and the design notes.*

> **In one sentence.** Nothing bad ever happens to Halflings, and it is paradise,
> and it is unbearable; sooner or later one of them stands in the valley on a
> perfect afternoon and decides to walk away.

---

## 📜 0. Rules

*The fixed points, and what we made of them. The books are defined at the head
of the page.*

### The rules as given

*Each entry is the rule itself, complete enough to resolve at a table. Not a
summary and not a cross-reference.*

> 📕 **Creature Type** Humanoid. **Size** Small, the only declared option, so it
> is never rolled: with a single option the generator takes it without touching
> the Dice Bag. **Speed** 30 feet.
>
> 📕 **No lineage.** The Halfling has no lineage, heritage or ancestry choice.
> Nothing under the species is chosen or drawn, and the declaration carries no
> heritages, so the Halfling never reaches the heritage table.
>
> 📕 **Brave.** You have Advantage on saving throws you make to avoid or end the
> Frightened condition. Both directions are covered: the save that would stop the
> condition being applied, and the save an ongoing effect allows you to make to
> end it (usually at the end of each of your turns, where the effect that imposed
> it grants one). No other condition is covered, and the Disadvantage the
> Frightened condition itself imposes on ability checks and attack rolls is not
> touched. Unlimited uses, no recharge.
> > 📘 _You were brave enough to leave home. You can handle this._
>
> 📒 **Halfling Nimbleness.** You can move through the space of any creature that
> is at least one size larger than you, though you can't stop there. For a Small
> Halfling that is every Medium, Large, Huge and Gargantuan creature. Moving
> through that space is still Difficult Terrain under the general movement rules,
> and it is those rules, not this trait, that forbid ending a move in another
> creature's space. No action, unlimited uses, no recharge. The published trait
> reads "a size larger"; the difference is set out below.
> > 📘 _This is just like child's play. Try not to get caught._
>
> 📕 **Luck.** When you roll a 1 on the d20 of a D20 Test, you can roll the die
> again, and you must use the new roll. A D20 Test is any attack roll, ability
> check or saving throw. The trigger is the natural 1 on the die, not a modified
> total of 1, and it is the d20 only, never a damage die. The reroll is optional
> and its result is binding: once the die is rerolled the 1 cannot be kept.
> Unlimited uses, no per-turn and no per-round cap, no recharge of any kind.
> > 📘 _Halflings are said to be the luckiest people alive._
>
> 📕 **Naturally Stealthy.** You can take the Hide action even when the only
> thing concealing you is a creature that is at least one size larger than you.
> That is an extra qualifying circumstance, not a replacement: the action's usual
> conditions (Heavily Obscured, or behind Three-Quarters Cover or Total Cover)
> still work as they do for everyone else. Every other part of the action applies
> unchanged: you must be out of any enemy's line of sight, you must succeed on a
> DC 15 Dexterity (Stealth) check, on a success you have the Invisible condition
> and your check total is the DC for a creature to find you with a Wisdom
> (Perception) check, and you stop being hidden as soon as you make a sound louder
> than a whisper, an enemy finds you, you make an attack roll, or you cast a spell
> with a Verbal component. Unlimited uses, no recharge.
> > 📘 _You read in your stories that halflings can become invisible._

The Halfling has no Darkvision, no ability score increase and no granted
language. The 2024 rules put ability scores and languages in the Background. In
this codebase the Languages box is not filled from the Background at all: it
comes from `Character_Languages` in `AtlasLudus/Map_of_Languages.py`, whose
species branches compare the Character object to a string (`char == "Elf"`) and
therefore never fire, so no species here has ever granted a language. Separately,
the legacy NPC movement map still carries the 2014 walk of 25 feet for the
Halfling (`AtlasPugna/Map_of_Movement.py`); the player path reads the 30 from the
species declaration and never consults it.

**The 📒, stated plainly.** Halfling Nimbleness ships as "at least one size
larger than you". The 2024 trait reads "a size larger than you", a single step.
The constant behind it is named `MINIMUM_RELATIVE_SIZE`, a floor and not a step,
and `Naturally_Stealthy` carries a constant of the same name, which is where "at
least" belongs: the published entry uses both phrasings in the same block, and
the kit has flattened them to the wider one. What the widening actually buys is
nothing. The general movement rules already let anyone pass through the space of
a creature two or more sizes larger, so for a Small Halfling every creature above
Medium was passable already, and the printed trait's own reach was only ever the
Medium ones. The divergence is in the text and not in play. It still counts,
because the sheet prints the text, and nothing declares it: no Questa, no Decree,
and no page of Documenta (§1 and §7 of this page discuss only the flavour lines).
The same wide phrasing sits in the pre-wipe entry preserved in
`.recovery-vault/AUTHORED-TEXT-ARCHIVE.md`, so it was carried over rather than
introduced by the voice rewrite, and it stays undeclared until a Questa records
it. Many tables read the published rule the way the kit writes it, so this may be
a disambiguation rather than an intended house rule.

**Two further differences are wording only and change no rule.** Luck says "you
can roll the die again" for the published "you can reroll the die". Nimbleness
says "though you can't stop there" for "but you can't stop in the same space".

### The supportive lore

> 📘 **The four trait entries follow the house pattern: an italic inspiration
> line, a blank line, then the rule in the 2024 rulebook's present tense.** The
> Halfling resolution is named, with the Elf's, as the reference for that pattern,
> and the recovery-era "Gained at Level 1. X granted Y" voice was rewritten out of
> it here.
> Ratified by **QST-0094**.

That book covers the four trait entries only. The species entry is a different
object: it is projected as narrative at level 0 and carries no rule and no
inspiration line, and QST-0094 leaves the description voice convention explicitly
open.

That is the whole of the supportive lore this page can currently mark. The
searches, so the negative result can be checked: "Halfling" appears in seven
files of the formal system (QST-0023, QST-0051, QST-0062, QST-0079, QST-0081,
QST-0081.5, QST-0094), all of them engineering, recovery or voice questae, and in
no file of either Agora tree, Dialogs, Decrees, Questions and Consuls included.
Everything below rests on the canon documents, on the authored prose in the kit,
and on this page's own decisions log, none of which is the Questa / Agora /
Decree system, so it carries no book until a Questa says otherwise.

### Unratified, and what each one needs

*Stated as design, not as law. Each line names the Questa that would ratify it.*

- **Sufficiency as the Halfling's metaphysic.** §2 proposes it and §6 files it as
  open. The peoples table in `Dragons-and-the-Overcoming.md` holds five rows and
  no Halfling one, so it is not even canon-backed. Needs a Questa seating the
  Halfling's organising idea, in the shape **QST-0053** demands of a newly added
  species: take an existing one or bring its own, and never stay metaphysically
  silent. QST-0053 asks that of new species only, so extending it to a species
  already shipping is itself part of the decision.
- **The valley.** The wide green valley, the generous soil, the wet spring, the
  three hundred years of peace written down in recipe books, the cousin who
  befriended a human. This is authored prose in the kit, quoted by the page; no
  Questa or Decree touches Halfling setting content. Needs a Questa fixing the
  homeland as canon, the way **QST-0050** records the Celestials' cosmology and
  cultural register as settled lore.
- **Paradise as the engine.** "It is paradise, and it is unbearable", and
  therefore the adventurer is produced by excess and not by lack. The causal
  claim is the sufficiency thesis and stands or falls with it, so it belongs to
  the same Halfling-origin Questa.
- **Adventurers made by reading**, and trait lines that quote the reading back at
  them. **QST-0094** ratifies the *form* of those lines and never their content.
  Needs a Questa deciding whether the reading motif is the canonical route to
  adventure or one flavour among several.
- **The Tolkien nod, and that it stays a nod.** The inspirations header in
  `AtlasNomina/Races/Halfling.py` lists "Hobbits", and the pools go further than
  a register: Bilbo, Frodo, Samwise, Adaldrida, Gamwick, Underfut and Bolson are
  in the drawable names. The dosage is decided nowhere. **QST-0046.5** owns the
  legend markers, and the Halfling has no row. Needs a sidequest of QST-0046.5
  setting the Halfling's markers and their weight.
- **Physical traits are biological.** Brave, Nimbleness, Luck and Naturally
  Stealthy read as inherited rather than taught, and "the valley did not
  culturise anyone into rerolling a 1". This is not a per-species exemption: the
  standing rule in `Mythos/README.md` already says the species law guards against
  monoculture and moral determinism only, and that physical traits are
  biological. That rule lives in a canon file, which is not the Questa system, so
  it carries no book, and the nearest formal text pulls the other way:
  **QST-0094** proposes the Dwarf's lines in the taught-or-gifted register and
  never adjudicates the Halfling. What actually needs deciding is where Luck sits,
  since a trait that edits a die is not obviously physical. Needs a Questa drawing
  the line per species and per trait.
- **The control group.** The people to whom nothing has happened, set against the
  Dwarves who fell, the Orcs who were fenced and the Tieflings who were
  condemned. It commits four species at once, so it needs a Questa ratifying the
  comparative frame.
- **The return.** The valley is never a villain, the leaving is a hunger for a
  story, and the Halfling intends to go back, read off the entry's own closing
  prompt ("what stories {name} will tell on getting back"). ⚠️ The page's
  stronger claim, that no other species entry promises a return, is false as it
  stands: the Dwarf entry says the clan will hail a dwarf who comes home with
  enough gold, and asks what the character will do with the gold carried home.
  What is singular is the *kind* of return, a story rather than a haul, which is
  the contrast §4 already draws. Needs a Questa fixing the return as canonical
  intent, in the corrected form and not the negative one.
- **Culture keys, and the naming register.** Verified in code: `_CULTURES` has
  sixteen rows, five of them keyed by class rather than by people, and none for
  the Halfling and none for the Orc, so the gear comes from the generic pool. The
  temperate farming register (English given names, French surnames, the food
  lexicon) is implied and unkeyed. `Draft-Tables.md` §E already drafts three
  options for the Halfling's keys and nothing has chosen one. Needs a sidequest of
  **QST-0046.5** keying the row, the way **QST-0046.4** retargeted the Aasimar and
  Goliath rows.
- **The thirteen class readings of §4 and the nine background readings of §5**,
  including the ✅ on Fated and "logistics is the species' one professional
  skill". The Agora's class-fantasy Dialogs name no species pairing for the
  Halfling, and **QST-0061** is about the Order background's entry count and
  voice, not about species readings at all. Needs a Questa, or a Dialog in the
  class-fantasy series, deciding whether species-by-class and species-by-background
  readings are canon or authorial illustration, before any of them reaches a
  sheet.
- **The two contrasts.** Two peaces against the Elves, one earned and one given;
  two returns against the Dwarves, one needing gold and one needing a story. Each
  also commits the other people's page, so each needs a Questa.
- **The Stranger nudge.** §6 proposes steering the one people who can always go
  home away from the one background that cannot. **Decree 0005** ("a nudge, not a
  filter") governs ability affinity weighting the options a build draws, spells
  and feats, not species weighting a background, and it argues against hard
  filtering rather than for this nudge. Needs a Questa deciding whether species
  may weight background selection at all.
- **The Cleric prayer pool.** "One can simply walk anywhere", "Rush not. Small
  feet. Small steps. Long journeys", and Life's "Haste has no blessing" live in
  code only. **QST-0091.1** counts the species keying of that file among the
  seven places a species is spelled, an engineering complaint, and Dialog 0016
  ratifies the Cleric's watcher fantasy without naming a species. Needs a Questa
  ratifying the per-species pools as authored content, so the Halfling's lines
  survive the re-keying.
- **"Concerning Halflings" stays, and the entry's person.** §6 files the opening
  under Decided, but **QST-0094** never mentions it, and its open convention on
  description voice lists the Halfling among the entries that address the reader
  as "you" rather than as "we". The shipping text does both: it opens "nothing
  bad ever happens to us. Our homeland is a wide green valley", and turns to "You
  read those stories. So you left." So the audit's own classification is what the
  entry contradicts. QST-0094's open convention is the Questa that would settle
  both.

### What the rules force, and what we chose

The rules give a Small body at a Medium body's speed, four traits, and no wound
of any kind. Three of the four are about being small among the large: Nimbleness
walks through the bigger creature, Naturally Stealthy hides behind it, Brave
saves against being afraid of it. Luck is about a die. Nothing in the set has a
cost, a recharge or a limit, which is unusual, and nothing in it explains itself.

Our answer is to read the set as **the valley's dividend rather than a survival
kit**, and to put the explanation entirely in the four inspiration lines. The
traits are treated as biological, not taught. The lines then set each one against
a person who has just left home and has never once needed it: *"You were brave
enough to leave home. You can handle this."* *"This is just like child's play.
Try not to get caught. You may die."* *"Halflings are said to be the luckiest
people alive. You hope so."* *"You read in your stories that halflings can become
invisible. You often wish it were true."*

**What that buys beyond the rule.** The rules say the Halfling is lucky; the
lines say the Halfling has only heard so. That gap is the entire species: someone
who owns four traits and has never had an occasion to use one. Brave stops being
a fear rule and becomes the act of leaving. Naturally Stealthy cites the books
that produced the adventurer, so the reading motif of §2 is carried by a trait
entry instead of by commentary. And because the four entries are the project's
own reference for the house pattern (📘 above), they hold the convention up as
well as the species.

⚠️ **What breaks if a later hand rewrites the four lines into plain rulebook
voice**, or "corrects" them so the trait is stated confidently. The species loses
its only statement of its drive: nothing else on a generated sheet says why a
Halfling left. Luck becomes a boast, which no Halfling on this page makes.
Naturally Stealthy stops pointing at the stories, and the reading motif has
nothing left to stand on. The Dwarf and the Tiefling entries have since been
rewritten into the same rule voice but still ship with no inspiration line at
all, and the four Dwarf lines proposed in QST-0094 were written to be measured
against these; delete these and the pending lines lose their model. The lines are
not decoration; they are the only place the rules are given a reason.

*(A correction the page owes the code: the shipping Nimbleness line ends "You may
die." and the shipping Luck line ends "You hope so.". §1, §7 and `Lines-Annex.md`
all record both as shorter, the Luck one trailing into an ellipsis. The page
claims to mirror the shipping text, so the page is what is wrong, in three
places.)*

### The variable detail

Drawn per character, and none of it ratified: the given name and surname (English
given names from the food and delights-of-life lexicons, French surnames, plus a
phonotactic composer for the rest, so Apricot Pecan and Macedonon), the Cleric
prayer if the character is one, and the gear. Size is not among them, because
Small is the only option, and neither is speed. Two things the entry hands to the
player rather than rolling: what foods the character misses from home, and what
stories they will tell on getting back.

None of it was filled in at random: the food lexicon is the valley, and the two
prompts leave the going-back for the player to fill in, which is the one promise
the species entry makes. The gear is the exception and it is an absence, not a
choice: with no culture row, it comes from the generic pool because nobody has
keyed one yet.

---

## 📚 1. Where the Halfling lives in the code

| What | Where | State |
|---|---|---|
| Species entry | `AtlasActorLudi/SpeciesKit/Halflings/__init__.py` | Shipping. "Concerning Halflings" (the Tolkien nod in the first word). First person plural, then "you left". Closes on the foods missed and the stories to tell on getting back. |
| Traits and rules | `Halflings/resolution.py`, `traits.py` | House pattern (QST-0094). Brave: *"You were brave enough to leave home. You can handle this."* Nimbleness: *"This is just like child's play. Try not to get caught."* Luck: *"Halflings are said to be the luckiest people alive. You hope…"* Naturally Stealthy: *"You read in your stories that halflings can become invisible. You often wish it were true."* |
| Names | `AtlasNomina/Races/Halfling.py` | Inspirations: food, the delights of life, hobbits. Names in English, surnames in French. The generator's Halflings: Apricot Pecan, Achunne Efrisemoot, Macedonon. |
| Culture keys | **none** | ⚠️ No row in `_CULTURES`; gear from the generic pool. |
| Prayer | `Map_of_Cleric_Prayers.py` | *Rush not. Small feet. Small steps. Long journeys.* *One can simply walk anywhere.* *The world is a big place. It is also a great place.* *Every day is a new story.* *The world is not inside your books.* Life: *Haste has no blessing* (Swahili). |
| Metaphysic | not in the peoples table | Proposed in §2. |

---

## 📜 2. Origin: the unbearable paradise

*"Our homeland is a wide green valley where the soil is so generous nobody has
gone hungry in living memory, the worst weather is a wet spring, and the
scandal of the decade was somebody's cousin adventuring out to the next village
and befriending a human… We have had three hundred years of peace and comfort,
all of it written down in recipe books."*

*"It is paradise, and it is unbearable."*

The peoples table gives no organising idea to the Halfling. This page proposes
one, in the shape the others take: **sufficiency**. The Dwarf's metal must be
proven; the Celestial's Ideal cannot bend; the Elf drifts; the Dragon authors
itself; the Orc walks a path. **The Halfling has enough**, and "enough" is the
only thing in the setting that produces an adventurer by *excess*: the valley
makes restless dreamers because nothing is missing. *"Sufficient unto the day"*
is already in the Life prayers. The Halfling's adventure is the one thing the
valley could not supply, and the species entry says so: "Looking for a story of
your own."

**The stories.** *"Some write it down in books that dry out the brains of the
next restless dreamer. You read those stories. So you left."* The Halfling is
the one people whose adventurers are *made by reading*, and whose trait lines
quote the reading back at them ("You read in your stories that halflings can
become invisible. You often wish it were true."). The Tolkien nod is deliberate
and gentle, and it should stay a nod.

**Physical traits are biological**: Brave, Nimbleness, Luck, Naturally
Stealthy. The valley did not culturise anyone into rerolling a 1.

---

## 📔 3. Society: the valley

Three hundred years of peace, recipe books as the literature, the scandal of
the decade a friendship with a human. The Halfling is the setting's control
group: the people to whom nothing has happened, against the Dwarves who fell,
the Orcs who were fenced, the Tieflings who were condemned.

The valley is never a villain. Its comfort is real and the Halfling misses it
("think of what foods {name} misses from home"); the leaving is a hunger for a
story, not an escape. The Halfling adventurer intends to *go back* ("what
stories {name} will tell on getting back"), which no other species entry
promises.

**No culture keys.** ⚠️ With the Orc, the Halfling is one of two playable
peoples with no row in the gear map. The name file (English names, French
surnames, food) and the entry (the wide green valley, the wet spring, the
cellar of cheese and dried tomatoes) suggest a temperate farming register that
the brief has not keyed. Undecided; the wells the class pages reached for
were the fiddle and the spoon (Bard), the recipe book (Wizard, Alchemist), the
pony and the goose (Beast Master).

---

## 📜 4. Metaphysics: what happens to someone nothing happened to

The Halfling is the setting's best instrument for reading every class *comically
and correctly at once*, because the class arrives at a person the valley did not
prepare, and the person does it anyway.

| Class | The Halfling in it |
|---|---|
| **Barbarian** | "Delighted by a meal." The Berserker's whole-of-the-moment paragraph is a Halfling's life; Bullroarer Took knocking a goblin's head into a rabbit hole. Joyful totality, without irony. |
| **Monk** | Self-Restoration: forgoing food and drink does not exhaust you. The one thing the valley cannot understand; the Halfling who learned not to need the cellar. |
| **Rogue** | Bilbo the burglar is the cliché; the Soulknife is the fresh one: the valley's one telepath, who can now hear the bad thing coming. |
| **Sorcerer** | Wild Magic: the valley's one accident. |
| **Bard** | The anthology is cookery; Countercharm is a lullaby; the fiddle and the spoon. The most comforting repertoire on the roster and the least useful in a dungeon, which is the species. |
| **Wizard** | The Spellbook map's docstring says "a cook's are recipes": the valley's literature, made to cast. |
| **Artificer** | The Alchemist's elixirs are recipes; Chemical Mastery ("you have tasted most of them yourself") is a Halfling's approach to food. |
| **Paladin** | An oath sworn in a place where oaths were never needed. Ancients: the green valley as the thing that was here first. |
| **Druid** | Grew up inside a covenant nobody negotiated; the Stars are the valley's only wilderness, up (Apricot Pecan, seed 29). |
| **Cleric** | The watcher was never once needed until the day they left the valley, and now it is. "One can simply walk anywhere." |
| **Ranger** | "The scandal of the decade was somebody's cousin adventuring out." The Halfling Ranger *is* that cousin; the pony is the companion. |
| **Fighter** | The one who made something bad happen to themselves on purpose, every morning at the post. |
| **Warlock** | The Archfey's "You can lose. That is the art." is what the valley never offered; a Halfling signs to be at risk. |

**Against the Elves.** The Elves chose to forget their wars; the Halflings never
had any. Two peaces, one earned and one given. **Against the Dwarves.** The
Dwarf's homecoming needs gold; the Halfling's needs a story. Two returns.

---

## 📔 5. Backgrounds

- **Vagabond.** "The day a place starts to feel like a cage, you're already
  gone." The valley as the cage, gently.
- **Gambler.** "Standing up smiling is the job." The Halfling who left a
  paradise to find out what losing feels like.
- **Servant.** The valley's cook at a great house's sideboard, learning "the
  entire register" of a cellar; the Cupbearer feat.
- **Naturalist.** "Half of what you have catalogued has bitten you at least
  once." The first Halfling anything ever bit.
- **Destined.** "You can walk further than anyone else in the party." The
  species' own joke, taken as prophecy.
- **Fated.** "Nothing bad ever happens to us" against "You are cursed."
  ✅ The Fated Halfling is the valley's exception, and knows it, and left so as
  not to spoil the milk at home.
- **Survivor.** The one bad thing that happened, to the one people it never
  happens to. The hardest Halfling.
- **Squire.** "Greatness has logistics": the Halfling who kept the packs dry and
  knew exactly how many days of food were left, which is the species' one
  professional skill.
- **Farmer (official).** The Halfling's own background is one sentence.

---

## 📜 6. Decisions log

**Decided**

- The species entry and the four trait lines are the house pattern's
  reference (QST-0094). "Concerning Halflings" stays.

**Open**

- **Culture keys**: none. The temperate farming register is implied and
  unkeyed.
- **The metaphysic**: this page proposes *sufficiency* for the peoples table.
- **The Stranger and the Halfling**: the one people who can always go home
  should perhaps be nudged away from the one background that cannot.

---

## 📖 7. Lines

*The four trait lines exist and are the reference; no additions.*

| Entry | Line (shipping) |
|---|---|
| **Brave** | *You were brave enough to leave home. You can handle this.* |
| **Halfling Nimbleness** | *This is just like child's play. Try not to get caught.* |
| **Luck** | *Halflings are said to be the luckiest people alive. You hope…* |
| **Naturally Stealthy** | *You read in your stories that halflings can become invisible. You often wish it were true.* |

---

## 📚 8. Pointers

- **Cultural Inspirations**: the Halfling's keys (open).
- **Barbarian, Monk, Rogue, Bard, Wizard pages**: the comic-heroic pairings.
- **Elf and Dwarf pages**: two peaces, two returns.
