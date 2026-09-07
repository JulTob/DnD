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
| **Aasimar / Celestial** | Athenian Greece + Vatican Rome | The pensive kind: philosophical, contemplative |
| **Giant / Goliath** | Legionary Rome + Spartan/Homeric Greece (+ `arthuriana`) | The naturalist kind: physical, practical, with general mysticism and naturalism |
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
| `athens` | Philosophy, the academy, the pensive register | Aasimar |
| `vatican` | Sacerdotal Rome: office, vestment, canon | Aasimar |
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

Still undecided: whether `vatican` reads too modern for the setting (`see`,
`basilica`, `apostolic` are the alternatives), and whether `homeric` is properly
a *society* key or a *legend* one, given that Goliaths already hold `wyrm_myth`
and the two would overlap on titans and giants.

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
