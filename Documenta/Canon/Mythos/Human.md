# 🧭 Human

> 📖 **In flow.** 1 of 10 chapters are still proposals. 📜 4 · 📚 2 · 📔 3 · 📖 1

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from the Human kit, the species entry, `AtlasNomina/Races/Human.py`,
`Cultural-Inspirations.md`, the class analyses and the design notes.*

> **In one sentence.** The wonderful wanderers: there is nowhere humans are not
> and nowhere humans wouldn't go, they thrive by friendship, and they organise;
> there is always a human kingdom a couple of days' walk away.

---

## 📚 1. Where the Human lives in the code

| What | Where | State |
|---|---|---|
| Species entry | `AtlasActorLudi/SpeciesKit/Humans.py` | Shipping. First person plural ("our people"). Closes on "what kinds of organizations {name} may belong to, such as guilds, schools, or militias." |
| Traits and rules | `Humans.py` (Resourceful, Skillful, Versatile) | Resourceful: *"Today is **the** day, my friend."* Skillful: *"You learnt by trying."* Versatile grants a second Origin feat, drawn from the whole pool. |
| Names | `AtlasNomina/Races/Human.py`, `HumanLegacy.py` | "Agender-neutral from African, Native, Aboriginal origins" and beyond; a per-Character *nomina culture* is drawn (`identity.species.Human.nomina_culture`), so a Human's name comes from one culture at a time. |
| Culture keys | `africa`, `egypt`, `maghreb`, `carthage`; legend `arthuriana` | "The baseline everyone else is measured from." Bloomery iron, ebony; gilded bronze, carnelian, electrum; nickel-silver, cedar, camel bone; Tyrian-dyed bronze, esparto, ivory. |
| Prayer | `Map_of_Cleric_Prayers.py` | *Ask the gods, but trust yourself.* Africa/Life: *Haste has no blessing.* Egypt/Grave: *What endures the grave weighs on the living.* Carthage/Life: *Perhaps someday even this will be a joy to remember.* Maghreb: *Help yourself, and Heavens will help you.* |
| Metaphysic | not in the peoples table | Proposed in §2. |

---

## 📜 2. Origin: the compact

*"In worlds full of monsters, magic, and dangers, our people learned not just to
survive but to thrive. And it is all thanks to the power of friendship. We
befriend most species, and coexist with them. We trade, we help each other, we
build relationships and even marriages. Humans tend to organize, making
institutions and orders part of our legacy."*

The peoples table gives no organising idea to the Human. This page proposes
**the compact**: the alliance, the institution, the marriage across peoples.
Every other principle is something a people *is* (a metal, an Ideal, a dream, a
self, a path); the Human's is something a people *makes between*. Humans are the
setting's connective tissue, and "there is always a human kingdom a couple of
days' walk away" is the compact as geography.

**The baseline.** The brief calls the Human "the baseline everyone else is
measured from", and then does the one thing most fantasy does not: it puts the
baseline in **Africa, Egypt, the Maghreb and Carthage**, so that the world is
deliberately not "Britain with magic Irish and barbarian Scots". The setting's
default human is southern Mediterranean and African, with early Arthur
(`arthuriana`) as the one legend register, shared with the Paladin and the
Goliaths.

**Physical traits.** Resourceful (Heroic Inspiration every Long Rest), Skillful
(a proficiency), Versatile (a second Origin feat). Nothing biological; the
Human's traits are what the compact gives: luck, a trade, an extra thing
learned.

---

## 📔 3. Society: institutions and orders

*"Humans tend to organize, making institutions and orders part of our legacy."*

The Orders engine (`AtlasOfOrders`) is Human-shaped: houses with signs cut into
lintels, academies, temples, lodges, companies. Every people may join one; the
Human *builds* them. The temples and academies that take Aasimar children, the
fines and the guards that walk Tieflings to the edge of town, the kingdoms that
fenced the Orc plains: all Human institutions doing what institutions do. The
Human entry's virtue and the other entries' grievances are one fact.

**The name draw.** A Human draws a *nomina culture* per Character, so one Human
is named from one culture and the next from another. The Human is the one
species whose name is a mosaic by design, and the Cultural Inspirations brief's
own goal ("every character comes from somewhere a reader can understand")
applies most literally here.

---

## 📜 4. Culture and registers

The Human's wells are the least spent in the class pages and the richest when
reached for, because every class's *default* is Human and every default is the
cliché's landing zone. The keys rescue it:

**Egypt**: Thoth and the House of Life (the Wizard), Setne Khamwas robbing a
tomb for the Book of Thoth (the Tomb Raider Wizard), Imhotep the first named
engineer (the Artificer), Beni Hasan's wrestlers (the Monk: the oldest martial
art on a wall), the Sothic year and the Nile's flood (the Stars Druid), Sekhmet
whose rage had to be tricked with red beer (the Barbarian), the Treasure of
Rhampsinitus (the Rogue: the oldest heist on record), the Nile crocodile (a
Beast Master's companion), the sistrum (the Bard's instrument).

**Carthage**: Hannibal's oath at nine (the Vengeance Paladin), Hanno's
*Periplus* down the African coast (the Ranger as the writer of the first travel
account), the Sacred Band (the Banneret), *"Perhaps someday even this will be a
joy to remember"* (Virgil's Aeneas, at Carthage's shore, in the Life prayers).

**Africa**: the griot and the kora (the Bard), Anansi who owns all the stories
and Legba who opens the crossroads (the Trickery Cleric, the Fiend Warlock),
the bluesman's midnight tuning (the Warlock's pact as a trade of skill), *"Haste
has no blessing"*.

**Maghreb**: the oud and the ney (instruments), nickel-silver and cedar,
*"Help yourself, and Heavens will help you"*, the desert and the sea from the
chant's first line ("the cold weight of a sea").

**Arthuriana**: shared with the Paladin (so a Human Paladin doubles it and reads
flat) and the Goliaths (early Arthur, the decline myth).

**Materials**: bloomery iron and cowrie-set ironwood; gilded bronze, carnelian,
acacia and electrum; Tyrian-dyed bronze, esparto, ivory-inlaid bronze.

---

## 📜 5. Metaphysics: the people who make between

**The Human Cleric drifts toward the intercessor.** The only people whose
watcher is an institution (Cleric page); the background draw decides whether
they become a priest, which the canon says a background must never force.

**The Human is every class's default**, and the default is where the cliché
lands: the Conan Barbarian, the Legolas-less archer Ranger, the Bilbo-less
Thief, the tower Wizard. Every class page found the same rescue: reach for the
four keys. The Human page's one rule for writers: *a Human Character is never
generic; a Human Character is Egyptian, Carthaginian, Maghrebi or African, and
the sheet should know which.*

**Versatile draws Dark Gifts, and that is the design.** A Human's second Origin
feat is drawn from base feats and every setting Origin feat, Dark Gifts
included, so a Human Tomb Raider can carry the Shadow background's *Shadow
Cast* ("It Follows") with no shadow in sight. What such a sheet needs is not a
gate but the gift's own line, which already exists as a docstring in the source
and never reaches the page. A Human carrying one is the compact's shadow: the
boon from the one alliance nobody chose.

**Against everyone.** The Human is measured from, and the other peoples measure
themselves *against*: the Orc entry names Humans among the takers ("came to
call it discovery"); the Halfling scandal was befriending one; the Tiefling is
born to them; the Aasimar's temples are theirs. The compact has a cost and the
other entries carry it.

---

## 📔 6. The classes: the compact in each

| Class | The Human in it |
|---|---|
| **Cleric** | Institutions; the intercessor risk; "Ask the gods, but trust yourself." |
| **Paladin** | Hannibal's oath (Vengeance); the Sacred Band (Banneret is a Fighter, but the Human holds the Band); doubles `arthuriana` and reads flat. |
| **Wizard** | Thoth, the House of Life, Setne. |
| **Artificer** | Imhotep. |
| **Bard** | The griot and the kora; the sistrum. |
| **Ranger** | Hanno's *Periplus*; Hawkeye and Quatermain as the adventure novel's own hero. |
| **Rogue** | Rhampsinitus's thief. |
| **Monk** | Beni Hasan, older than any school the sangha remembers. |
| **Barbarian** | Sekhmet; "the cold weight of a sea"; the Wild Heart's Wolf ("the ones you hunt with") as the compact in a Path. |
| **Druid** | The Sothic year; the Nile. |
| **Warlock** | The crossroads; "there is always a human kingdom two days' walk away, and a patron a little further." |
| **Fighter** | The default; the Egyptian and Carthaginian wells rescue it. |
| **Sorcerer** | The Servant Aberrant (seed 15): "you heard it all again, coming from inside you." |

---

## 📔 7. Backgrounds

The Human draws every background, and the custom ones do the work the species
entry cannot: the Stranger (a people scattered *among* humans), the Servant
(the great house), the Revolutionary (the Cause against the institution), the
Bailiff (the institution's hand), the Herald (the institution's mouth), the
Squire (the institution's logistics), the Inquisitor (the institution's left
hand), the Gambler (the institution's back room). The Human is the species for
whom the *background* is the identity, which is what "think of what kinds of
organizations {name} may belong to" already says.

The official backgrounds (Acolyte, Artisan, Guard, Noble, Soldier, Sage…) are
the Human's natural draws and are one sentence each (Cleric page §8). ⚠️ The
species that most needs its backgrounds to speak has the thinnest ones.

---

## 📜 8. Decisions log

**Decided**

- The four keys, and the refusal of the Britain default (the brief).
- The species entry speaks as "we" (`9be3a07`).
- The per-Character nomina culture draw.

**Open (this page proposes)**

- **The metaphysic**: *the compact*, for the peoples table.
- **The Dark Gift lines onto the sheet** (§5, and the Feats page §3).
- **The writer's rule**: a Human Character is never generic; the sheet should
  know which of the four wells it is drawing from, and the gear and name
  should agree.

---

## 📖 9. Lines

*The two trait lines exist. One proposal for Versatile, which has none.*

| Entry | Line |
|---|---|
| **Resourceful** | *Today is **the** day, my friend.* (shipping) |
| **Skillful** | *You learnt by trying.* (shipping) |
| **Versatile** (proposal) | *Somebody, somewhere along the road, taught you one more thing. You did not always ask what it would cost.* |

---

## 📚 10. Pointers

- **Cleric page**: the intercessor risk.
- **Warlock page**: the Dark Gift leak.
- **Orders**: the Human as the Orders' builder.
- **Cultural Inspirations**: the baseline's four keys; the brief's whole point.
- **Official backgrounds**: the Human's thinnest draws.

