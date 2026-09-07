# 🌍 Cultural Inspirations — the peoples and their sources

*Julio's setting brief, recorded 2026-08-03. This is intent, not implementation:
`AtlasInventarium/Map_of_Gear_Titles` is one consumer of it, and later work
(names, architecture, cuisine, story) should read from the same directions.*

---

## The law

**One culture key = one culture.** Never fuse two inspirations into a single
marker (`japonic_aztec`, `norse_steppe_celtic`, and the like are wrong).

A **species** may draw from many cultures. That is recorded as a *list of
separate keys*, not as a blended label. Overlap between peoples is modelled by
the influence network (`_INFLUENCES`), not by merging vocabulary pools.

Fiction registers (`wyrm_myth`, `grimdark`, `arthuriana`, …) are also separate
keys; they are not real-world cultures, and they do not merge real-world ones.

---

## The aim

Every people is a **real human culture cranked to romantic excess** — the
fantasy is the over-the-top version of a recognisable base, plus extra.

- Spain sought gold in America → **gold-fevered Dwarves**.
- Isolationist and imperial at once → **Dragonborn**, drawing on Japan **and**
  the Mexica as two distinct wells.
- Mysterious and exotic → **Fae**, orientalism multiplied by a thousand.

The point of anchoring on real cultures is that **every character comes from
somewhere a reader can understand**. It may be turned up loud, but it is
legible, and it deliberately avoids the default of fantasy where "the world is
Britain with magic Irish and barbarian Scots".

## The peoples

Each row lists **separate** culture keys the species may hold. Plus any fiction
register is listed on its own line of thought, not fused into a real-world key.

| People | Culture keys (each distinct) | Character |
|---|---|---|
| **Dragonborn** | `japan`, `aztec` (+ `eragon_dragons`, `wyrm_myth`) | Isolated from the rest, yet imperialist |
| **Kobold** | `japan`, `china`, `korea` (+ `wyrm_myth`) | A step to one side of the Dragonborn |
| **Fae** | `china` (+ `fairytale_fae`); India reached via influences | Mysterious and exotic; orientalism ×1000 |
| **Goblin** | `persia`, `levante` (+ `fairytale_fae`, `grimdark`) | Marginalised; no single real parallel claimed as identity |
| **Human** | `africa`, `egypt`, `maghreb`, `carthage` (+ `arthuriana`) | The baseline everyone else is measured from |
| **Elemental** *(not yet playable)* | `india`, `oceania` (+ `arabian_nights`) | A caste society; mixed elementals outcast by every side |
| **Elf** | `norse`, `rus`, `mongol`, `celt` (+ `tolkien_elves`, `fairytale_fae`) | A bit Fae and a bit "other people", in a colder nature |
| **Dwarf** | `iberia`, `andalus` (+ `folklore_dwarf`, `tolkien_dwarves`) | Gold-fevered |
| **Gnome** | `italy`, `germany`, `switzerland` (+ `folklore_dwarf`, `clockpunk`) | Middle point of the Renaissance pair |
| **Aasimar / Celestial** | `athens`, `vatican`, `sangha` | The pensive kind: philosophical, contemplative |
| **Giant / Goliath** | `rome`, `sparta`, `homeric` (+ `arthuriana`) | The naturalist kind: physical, practical, with general mysticism and naturalism |
| **Monk** *(class)* | adds `ninja` (+ `anime`) on top of species cultures | Monks read as ninja across every people |

## Elementals: India, Oceania, and a caste that outcasts its own

*Julio, 2026-08-05: "India was for the elementals, along with oceania (water
elementals). I completely forgot."*

Recorded in full even though **no elemental is playable in 2024**, precisely
because it was forgotten once. The mapping exists so the next person does not
have to rediscover it.

- **`india`** is the elemental homeland: ancient, complex and mysterious all at
  once. It is *not* the Fae's, though the Fae reach it through `china` in the
  influence network.
- **`oceania`** belongs to the **water** elementals: island and reef vocabulary,
  greenstone, shark-tooth, coral, the long canoe.

The society is the interesting part. Elementals live under a **caste tension
amounting to apartheid**, divided by element, each keeping to its own. The
outcasts are the **mixed elementals**: a being of two elements belongs to
neither caste and is cast out by both sides at once. They are not exiles from a
single home; they are refused by every home they could claim.

That gives the species a built-in story hook that needs no villain, and it is the
reason the mapping holds two societies rather than one: an elemental drawing on
India and Oceania at the same time is already, structurally, a mixture.

## Celestials and Giants: the distinctive comparative

*Julio, 2026-09-07, correcting an earlier mix-up: Celestials had been recorded
as Roman and Goliaths as Greek. It is the other way round, and it does not stop
at a swap.*

These two are the only peoples who hold **both** Greece and Rome as identity
rather than as the background inheritance everyone carries. They do not divide
the classical world between them. They each take **half of each**, and the
halves they take are opposites.

| | **Aasimar / Celestial** | **Goliath / Giant** |
|---|---|---|
| Greek half | **Athens**: the academy, the portico, the argument carried to its end | **Sparta and the Iliad**: the agoge, the single combat, the giants and titans |
| Roman half | **Vatican Rome**: the see, the vestment, the sacred office, the canon | **Legionary Rome**: the road, the aqueduct, the siege engine, the drill |
| Temper | Pensive, philosophical, contemplative | Naturalist, physical, practical |
| Meets a problem by | Reasoning it through first | Doing it, and reasoning after |
| Authority rests on | Consecration and argument | Deed and physical proof |
| Failure mode | Deliberates while the thing burns | Solves the wrong problem, thoroughly |

So the pairing is deliberately crossed:

- The **Celestial** is Greek in mind and Roman in office. Athens gives the
  reasoning; the Vatican gives the vestment and the hierarchy it reasons inside.
- The **Goliath** is Roman in method and Greek in myth. The legion gives the
  road and the drill; the Iliad gives the heroes, the giants and the titans
  they descend from.

Neither is the "civilised" one and neither is the "brute". A Celestial's
contemplation and a Goliath's practicality are two ways of being serious.

### What this costs us

This is the complexity Julio flagged. Until now `greece` and `rome` were single
markers, and the network already had *everyone* inheriting them faintly. Now two
peoples hold both, for opposite reasons, and one marker each can no longer tell
them apart: give both species `greece` + `rome` and they become the same people
in the generator, holding the same vocabulary.

The lore above is **decided**. The key split that expresses it is **ruled but
not yet applied** (see `Questae/Open/QST-0046.4`): break the two markers into
five atomic ones, keeping the "no invented middle ground" rule since all five
are real and named for themselves.

| Key | Holds | Given to |
|---|---|---|
| `athens` | Philosophy, the academy, the fleet | Aasimar |
| `vatican` | Sacerdotal Rome: office, vestment, canon | Aasimar |
| `sangha` | The Buddhist monastic order of South and Southeast Asia | Aasimar |
| `sparta` | Martial Greece: the agoge, the phalanx, the duel | Goliath |
| `homeric` | The Iliad, the heroic age, titans and giants | Goliath |
| `rome` | Practical Rome: legion, road, aqueduct | Goliath |

*Julio, 2026-09-07: "I like the atomic categories: Athens, Sparta, Homeric…
that's very organized."* Homer earns his own key rather than being bundled into
Sparta: a hoplite in formation is not Achilles, and the two registers were doing
different work under one name.

`_INFLUENCES` then keeps them neighbourly (Athens reaches Sparta, Sparta reaches
Homer, the Vatican reaches Rome), so the two peoples still share a classical
world without becoming interchangeable inside it.

### Why Arthur belongs to the Giants

*Julio, 2026-09-07.*

Arthuriana sits with the Goliaths, not the Celestials, and the reason is the
whole point of the pair.

**Arthur is the hinge between Rome and the medieval world.** He is what the
legion becomes once the legion has gone: a washed and half-remembered story of a
decaying garrison, sprouting a warlord who carves the people into a caste of
knights above everyone else. That is not a founding myth. It is a **decline**
myth, and the Goliaths are the fallen civilisation.

The contrast with the Celestials is exact, and it is why the two peoples need
different registers rather than a shared classical one:

| | **Celestial** | **Goliath** |
|---|---|---|
| What happened to their world | It **endured**. They are the chosen, and the Vatican still stands today | It **fell**. The empire split, interbred, and ran itself into oblivion |
| So their legends are | Continuity: the office, the canon, the unbroken line | Aftermath: the ruin, the warlord, the caste that outlived the reason for it |

"The greater they fall." A Goliath carries the grandeur of Rome and the wreckage
of it in the same hand, which is a far more interesting thing to hand a player
than simple bigness.

**The Arthurian epoch is also thick with giants**, which is the second reason it
fits. The beanstalk and the giant at the top of it; the seven-league boots taken
from an ogre; the knights who went out to kill dragons. Those are the stories
this register actually tells, and they are giant-stories before they are
knight-stories.

That last one carries a further implication worth naming: **dragon versus
giant**. Dragonborn and Goliaths are set against each other in the myth layer,
not merely different from one another. The dragon-slaying knight is a Goliath
story about a Dragonborn.

### The Celestial is an order, not a church

*Julio, 2026-09-07: "another society for the celestials is the sanscrit
subculture. The priesthood in south and southeast asia, in a buddhist style
more than hindu."*

`sangha` is the third Celestial marker, and it changes what the species *is*.
With Athens and the Vatican alone, a Celestial read as a Catholic prelate with
a Greek education. With the sangha beside them, the through-line is no longer
any one faith: it is **the contemplative order as such**, wherever it is found.
Athens reasons, the Vatican consecrates, the sangha renounces. That is a far
better fit for "the pensive kind" than a single church could be.

Named for the **order**, not for the language, so it sits beside `vatican` as an
institution rather than beside `india` as a place. Its register is the
Sanskrit and Pali textual culture and the monasteries of Sri Lanka, Burma,
Thailand and Cambodia: the Khakkhara staff, the vajra, the dha and the krabi,
worked in temple bronze and saffron-lacquered wood.

**Buddhist, not Hindu, and that separation is load-bearing.** Hindu India is
already the key `india`, and `india` belongs to the **Elementals**. Keeping the
monastic order in its own key is what stops a Celestial and an Elemental
drawing from the same well. They still touch: `sangha` reaches `india` at 2,
because the order came from there.

Still undecided: whether `vatican` reads too modern for the setting (`see`,
`basilica`, `apostolic` are the alternatives), and whether `sangha` is the right
name for the third (`theravada` and `nalanda` are the alternatives; `sanskrit`
was rejected only because it names a language rather than a people).

## Cultures overlap, and that is the point

**No people is sealed off.** The map is a *network of influences*, not a set of
boxes, and a weapon, a word or a custom may belong to several cultures at once.

- Dwarves and Gnomes trade and share settlements.
- Elves and Fae are close partners.
- Goblins live among Humans.
- Iberia is strongly shaped by the Umayyads — still `iberia` and `andalus`, not one key.
- Vikings reached Spain and North Africa — still `norse` influencing `iberia`, not a merge.
- Celts are part of Spain (Galicia) as well as the north — `celt` stays its own key.
- China and India both reach Arabia — separate keys, linked by `_INFLUENCES`.
- **Everyone** inherits Greece and Rome, faintly, through `_INFLUENCES`.
  Aasimar and Goliaths are the exception: for those two it is identity, not
  inheritance, and they take opposite halves of each (see the comparative above).

India is complex, mysterious and ancient all at once; all cultures are
relatable. Overlap should be modelled, not avoided.

## The legend register: stories are markers too

*Julio, 2026-08-05: "you may also add variations like 'fairytale_elf' or
'folklore_dwarf' which are 'real life' stories and models to get inspiration
from, even 'Tolkien_Elfs' and 'Eragon_Dragons' even 'anime' for monks, or other
cultural/fantasy collage of sources, for items like Mithril and such."*

A people is read against **two** families of source: the real cultures above, and
the **stories** the reader already knows. Both are markers, both feed the same
network, and a name is a single roll across the pair.

| Legend key | The register it supplies | Held by |
|---|---|---|
| `tolkien_elves` | Elven blades, star-glass, mithril shirts | Elf |
| `tolkien_dwarves` | Rune-axes, delving, mithril mail | Dwarf |
| `folklore_dwarf` | Knockers, nisse, the tapping hammer | Dwarf, Gnome |
| `fairytale_fae` | Cold iron, thorn and briar, the rowan staff | Fae, Elf, Goblin |
| `eragon_dragons` | Rider's blades, sworn oaths, wyrm-riding | Dragonborn |
| `wyrm_myth` | Dragonslayers, hoards, serpent-bane | Dragonborn, Kobold, Goliath |
| `arabian_nights` | Djinn scimitars, wish-knives, the lamp | Elemental |
| `arthuriana` | Kingswords, the questing lance, blazoned shields | Human, Aasimar, Paladin |
| `sword_and_sorcery` | Reaver's axes, beast-pelts, black meteor iron | Barbarian |
| `grimdark` | Warglaives, penitent flails, pitted iron | Warlock, Tiefling, Goblin |
| `clockpunk` | Ratchet crossbows, wheel-locks, geared bronze | Gnome, Artificer |
| `anime` | The nameless blade, impossible greatswords, twin kama | Monk |

#### Open: `wyrm_myth` is the slayer's register, held by the dragons

Worth settling, because the "dragon versus giant" note above sharpens it.

`wyrm_myth` does not contain dragon vocabulary. It contains **anti-dragon**
vocabulary: Dragonslayer, Wyrmbane, Hoard-Cleaver, Serpent's Bane, Wyrm-Spear,
Dragon Lance, Scale-Faced Shield. It is Beowulf, Sigurd at Fafnir's throat, and
Saint George. Its influences say the same (`norse`, `homeric`, `china`).

It is currently held by **Dragonborn and Kobolds**: the dragons are carrying the
weapons made for killing them. That can be read as a story rather than a fault,
and by the standing rule that loaded names stay in the pool (a justiciar is not
automatically just), a Dragonborn drawing a *Wyrmbane* is a kinslayer or a
trophy-taker, which is good.

But it sits oddly beside the new lore, which puts dragon-slaying on the
**Goliath** side. Three ways out, none applied:

1. **Leave it.** The mismatch is a story, and Goliaths get their dragon-slaying
   through `arthuriana` instead.
2. **Give `wyrm_myth` back to the Goliaths** and leave Dragonborn with
   `eragon_dragons`, which is genuinely dragon-*side* (Rider's Blade,
   Oath-Sworn Blade, Wyrmrider's Greatblade, Rider's Scale). This would make
   "dragon versus giant" real in the vocabulary: the slayers hold the slaying
   words. Kobolds would then need a register of their own.
3. **Split it in two**, a dragon-side and a slayer-side register, and give one
   to each.

Three rules govern the register:

1. **Legends are kept in their own table** (`_LEGEND_NOUNS`), not folded into the
   societies. A wrong people is a history question; a wrong legend is a genre
   question. Different edits, different reviewers.
2. **Some legends are summoned by Guild, not species** — a Barbarian reads as
   sword-and-sorcery whoever their parents were, and a Paladin as Arthurian.
3. **The naming rule from the societies still applies.** *Mithril* and
   *Warglaive* stand alone; anything else carries its category (*Elven Blade*,
   *Rune-Axe*).

## Materials speak the culture too

*Julio, 2026-08-05: "it would be cool to add 'materials', like 'obsidian sword'
or 'silver katana' that also speak to the culture: Dwarves may focus more on
metals, and gnomes on jewels."*

`Map_of_Materials` is keyed by the **same markers**, so one species row drives
both what a thing is called and what it is made of. Obsidian is Aztec, folded
steel and lacquered silver are Japanese, wootz is Indian, greenstone is Oceanic,
Toledo steel is Iberian, and **mithril** belongs to the two Tolkien registers.

- **Leanings, not laws.** Dwarves lean toward metals and Gnomes toward jewels
  through extra weight, never through a closed door.
- **Every material must read on a blade, a haft *and* a coat**, because the
  placeholder does not know what it is filling. Gems therefore appear as
  settings (*"emerald-set steel"*), never as whole objects.
- **Materials are flavour only**: no price, no weight, no grant. A material that
  ought to be lighter or stronger has stopped being a describing word and belongs
  in the Ledger as its own item.

## How this is implemented today

`Map_of_Gear_Titles` holds the first machine-readable version:

- `_CULTURES` — species (and Monk) → a **tuple of distinct culture keys**.
  Dragonborn is `japan` **and** `aztec`; Kobolds are `japan`, `china`, and
  `korea`; a Dragonborn Monk adds `ninja` on top of the species list.
- `_CULTURAL_NOUNS` — vocabulary **per culture key**. Katana lives under
  `japan`; Macuahuitl under `aztec`. No shared fused pool.
- `_INFLUENCES` — weighted neighbours between those same keys. Japan reaches
  China and Korea; Aztec stands as its own pool. A Dwarf's reach can touch
  Maghreb or Carthage without the Dwarf *becoming* those cultures.
- `_LEGEND_NOUNS` — the story register, same shape, its own table.
- `cultures_of(hero)` / `influences_of(hero)` — assemble the list, then roll
  across the network. A Dragonborn may draw a Katana *or* a Macuahuitl —
  two cultures, one people.
- `societies_of(hero)` / `legends_of(hero)` — the **double mapping**. Julio:
  *"For errors like this is useful to have a species - society - weapon double
  mapping. Would make these errors an easy fix."* Splitting the two families
  turned the Aasimar/Goliath mix-up into a one-line diagnosis.

One rule that is easy to lose and hard to notice:

**A people's own voice is a budget, shared among the markers they hold, not a
weight paid per marker.** `_CULTURAL_BUDGET` (12) is divided by the number of
markers. Without this, a Human holding four societies shouts four times louder
than an Aasimar holding one, the trade layer vanishes underneath, and
rich-heritage species become quietly monotonous. It fails no test loudly; the
rustic-Spear share assertion is what catches it.

Two rules that keep it legible:

1. **Culture-marked words live only in the culture that says them.** Generic
   pools hold the proper name plus plain English; Katana, Yari, Gladius and
   Targe are reachable only through a people who would use them. (Leaving a
   marked word in the generic pool leaks it to everyone — that is how a Dwarf
   once ended up carrying a Yari.)
2. **Famous names stand alone; unfamiliar ones carry their category** —
   *Katana* and *Shuriken* bare, but *Honda Sling*, *Khopesh Sabre*,
   *Akinakes Blade*. This keeps the weapon legible, and keeps its **Weapon
   Mastery** obviously applicable.

## Open directions

The same mapping should eventually inform names, places, cuisine, architecture,
prayer, and story vocabulary — not just gear. Consumers must keep the **one
key = one culture** law; if a species needs two inspirations, give it two keys.
