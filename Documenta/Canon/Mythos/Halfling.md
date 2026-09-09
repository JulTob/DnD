# 🧀 Halfling

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from the Halfling kit, the species entry, `AtlasNomina/Races/Halfling.py`,
the class analyses and Julio's notes.*

> **In one sentence.** Nothing bad ever happens to Halflings, and it is paradise,
> and it is unbearable; sooner or later one of them stands in the valley on a
> perfect afternoon and decides to walk away.

---

## 1. Where the Halfling lives in the code

| What | Where | State |
|---|---|---|
| Species entry (Julio's) | `AtlasActorLudi/SpeciesKit/Halflings/__init__.py` | Shipping. "Concerning Halflings" (the Tolkien nod in the first word). First person plural, then "you left". Closes on the foods missed and the stories to tell on getting back. |
| Traits and rules | `Halflings/resolution.py`, `traits.py` | House pattern (QST-0094). Brave: *"You were brave enough to leave home. You can handle this."* Nimbleness: *"This is just like child's play. Try not to get caught."* Luck: *"Halflings are said to be the luckiest people alive. You hope…"* Naturally Stealthy: *"You read in your stories that halflings can become invisible. You often wish it were true."* |
| Names | `AtlasNomina/Races/Halfling.py` | Inspirations: food, the delights of life, hobbits. Names in English, surnames in French. The generator's Halflings: Apricot Pecan, Achunne Efrisemoot, Macedonon. |
| Culture keys | **none** | ⚠️ No row in `_CULTURES`; gear from the generic pool. |
| Prayer | `Map_of_Cleric_Prayers.py` | *Rush not. Small feet. Small steps. Long journeys.* *One can simply walk anywhere.* *The world is a big place. It is also a great place.* *Every day is a new story.* *The world is not inside your books.* Life: *Haste has no blessing* (Swahili). |
| Metaphysic | not in the peoples table | Proposed in §2. |

---

## 2. Origin: the unbearable paradise

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

## 3. Society: the valley

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
the brief has not keyed. Julio's call; the wells the class pages reached for
were the fiddle and the spoon (Bard), the recipe book (Wizard, Alchemist), the
pony and the goose (Beast Master).

---

## 4. Metaphysics: what happens to someone nothing happened to

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

## 5. Backgrounds

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

## 6. Decisions log

**Decided (Julio)**

- The species entry and the four trait lines are the house pattern's
  reference (QST-0094). "Concerning Halflings" stays.

**Open (Julio's to decide)**

- **Culture keys**: none. The temperate farming register is implied and
  unkeyed.
- **The metaphysic**: this page proposes *sufficiency* for the peoples table.
- **The Stranger and the Halfling**: the one people who can always go home
  should perhaps be nudged away from the one background that cannot.

---

## 7. Lines

*The four trait lines exist and are the reference; no additions.*

| Entry | Line (shipping) |
|---|---|
| **Brave** | *You were brave enough to leave home. You can handle this.* |
| **Halfling Nimbleness** | *This is just like child's play. Try not to get caught.* |
| **Luck** | *Halflings are said to be the luckiest people alive. You hope…* |
| **Naturally Stealthy** | *You read in your stories that halflings can become invisible. You often wish it were true.* |

---

## 8. Pointers

- **Cultural Inspirations**: the Halfling's keys (open).
- **Barbarian, Monk, Rogue, Bard, Wizard pages**: the comic-heroic pairings.
- **Elf and Dwarf pages**: two peaces, two returns.
