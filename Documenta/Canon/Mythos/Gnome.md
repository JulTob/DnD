# 🔧 Gnome

> 🚧 **In flow.** 1 of 10 chapters are still proposals. 🔒 4 · 🧾 2 · 🔎 3 · 🚧 1

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from the Gnome kit and its two lineages, the species entry,
`AtlasNomina/Races/Gnome.py`, `Cultural-Inspirations.md`, the class analyses and
the design notes.*

> **In one sentence.** Everyone's favourite neighbours, nobody's countrymen: a
> people who came out of the Fae like the Elves and chose curiosity over the
> Dream, who keep their ways in things rather than in land because land can be
> taken, and whose grandmother could fit the whole history of the people into a
> piece of jewellery small enough to swallow, and did, twice.

---

## 🧾 1. Where the Gnome lives in the code

| What | Where | State |
|---|---|---|
| Species entry | `AtlasActorLudi/SpeciesKit/Gnomes/__init__.py` | Shipping. "Your people", "your family": second person with a collective inside it. Closes on "what {name} carries that is worth more than it looks." |
| Lineages | `Gnomes/Forest_Gnome.py`, `Rock_Gnome.py` | "Your family never took the city offer" / "took the city offer and filled a workshop with it." The two lineages are one decision, taken two ways. |
| Traits and rules | `Gnomes/resolution.py`, `traits.py` | Darkvision: *"The Fae are said to be part of the Dream. Maybe Gnomes still carry some of it, because you have always felt the night welcomes you."* Gnomish Cunning: *"Curiosity got your people through worse than a spell, and it still does."* Lineage lines for both. |
| Names | `AtlasNomina/Races/Gnome.py` | Italian (Renaissance lists), Galician. The generator's Gnomes: Barbato Wedello Walvittar Mindtwister, Dorella Gionora Giovanini Fishreicheck, Teodora Lichola Orsa Kochwegsohn: Italian and German compounds four names long. |
| Culture keys | `italy`, `germany`, `switzerland`; legends `folklore_dwarf`, `clockpunk` | "Middle point of the Renaissance pair." Milanese steel, Solingen steel, garnet-set steel, rock-crystal; clockwork brass, spring steel, geared bronze. Gems lean here. |
| Prayer | `Map_of_Cleric_Prayers.py` | *Wonder and Wander.* *Care not for what you cannot change. Change what you can.* *Care not for what you cannot carry.* Knowledge: Dante. Life: Saint-Exupéry. |
| Metaphysic | not in the peoples table | Proposed in §2. |

---

## 🔒 2. Origin: curiosity, not fae magic

*"Your family has been in this house for four hundred years, and you will still
be asked to go back to the Feywild. But everyone loves what your people made:
the lenses, the clockwork, the smoking herbs. These were found not by fae
magic, but by curiosity."*

The Gnome came out of the Fae, as the Elves did, and the Darkvision line keeps
the connection ("Maybe Gnomes still carry some of it"). But where the Elves are
made malleable by the Dream, **the Gnomes refused the Dream for the mechanism.**
The species entry separates the two explicitly, and the Artificer page found
that this makes the Gnome the Artificer's people *by refusal*: the one who left
the Feywild to *build*.

The peoples table gives the Gnome no organising idea. This page proposes
**curiosity**: not as a mood but as the principle that replaced the Dream. The
Elf is shaped by what everyone imagines; the Gnome by what one person wanted
to find out. *"Wonder and Wander."* Gnomish Cunning is the rule: "Curiosity got
your people through worse than a spell."

**Physical traits are biological**: Darkvision, Gnomish Cunning (Advantage on
Intelligence, Wisdom and Charisma saves), and the lineage magic (the Forest
Gnome's Minor Illusion and Speak with Animals; the Rock Gnome's Mending,
Prestidigitation and the Clockwork Device).

---

## 🔎 3. Society: ways kept in things

*"Your own keep their ways in things rather than in land, because land can be
taken. A song, a recipe, a pattern in a rug, a joke that only works in the
Sylvan tongue: those travel with you."*

**Everyone's neighbour, nobody's countryman.** Four hundred years in the house
and still asked to go back. The Gnome is a diaspora *with* a welcome ("in the
good years everyone is a friend"), against the Tiefling's without and the
Stranger's precarious one. The Gnome and the Dwarf "trade and share
settlements": the Renaissance pair, one trade route, the Dwarf's metals and the
Gnome's jewels.

**The two lineages are one decision.** The city offer was made; the Rock
Gnomes took it and filled a workshop ("a bird that sings on the hour and has
done since your great-grandfather wound it"); the Forest Gnomes did not, and
put down roots "past the last farm where the wood begins", where the fae are
nearer and some of it rubbed off. Not two bloodlines: two answers to one
letter.

**The swallowed jewel.** The grandmother who fit the whole history of the
people into a piece of jewellery small enough to swallow, twice, is the
species' best sentence and its metaphysic in an object: history as a portable
thing. The Wizard's Spellbook map draws "a necklace of amethysts, each stone a
page" for Jeweler's Tools, which is the grandmother's jewel made to cast, by
accident. Protect the accident.

**Anything can be taken apart.** *"You were taught that anything can be
observed, taken apart, solved and improved, that most things should be, and
that the shame is not in breaking it but in failing to make something out of
the pieces."* The Rock Gnome's creed, and the Renaissance's.

---

## 🔒 4. Culture and registers

**Italy**: the Renaissance workshop, Milanese steel, the commedia dell'arte
(Arlecchino's mask and the improvised scene: the Gnome Glamour and Lore Bards),
Dante in the Knowledge prayer, the Antikythera-to-clockwork line of made skies.
**Germany**: Solingen steel, Reynard the fox of the beast epic (the Gnome
Arcane Trickster), Wayland the smith who built wings (the Gnome Artificer's
flier), the hurdy-gurdy (the Gnome's instrument is a machine). **Switzerland**:
garnet-set steel, rock-crystal, the alphorn, clockwork's homeland. **Legends**:
`clockpunk` (Ratchet Crossbow, Wheel-Lock Pistol, Gearwright's Hammer), shared
with the Artificer by Guild so a Gnome Artificer holds it twice (quieter, by
the dilution rule, not louder); `folklore_dwarf` (knockers, nisse, the tapping
hammer), shared with the Dwarves.

**Names**: Italian Renaissance lists and Galician. The four-part compound is a
device of its own: a Gnome's name is a small inventory.

**Prayers**: *Care not for what you cannot carry* is the species' metaphysic
as a proverb.

---

## 🔒 5. Metaphysics: the reverse Elf

**The Gnome and the Elf.** Both came out of the Fae. The Elf stayed in the Dream
and is shaped by it; the Gnome left it for curiosity and is shaped by what they
made. The Elf Artificer is the reverse Gnome (the Dream's own child who
prefers the machine); the Gnome who *went back* to the Feywild with a machine
is the reverse of the reverse, and the most interesting Gnome on the roster.

**The Gnome and the Dwarf.** One trade route. The Dwarf's metal is holy and
given; the Gnome's jewel is carried and made. The Dwarf's homecoming needs
gold; the Gnome's home is what they carry.

**The Gnome and the Tiefling.** Two diasporas: one welcomed and still asked to
leave, one hated and never asked anything.

**Clockwork against ziran.** The Clockwork Sorcerer is the anti-dragon (order
imposed on the self); the Gnome is its people, and Kepler's clockwork universe
is the Gnome's cosmology (Sorcerer page). A Gnome Clockwork Sorcerer is native
and flat; the Gnome Wild Magic Sorcerer is curiosity that would not wait.

---

## 🔎 6. The classes: curiosity in each

| Class | The Gnome in it |
|---|---|
| **Artificer** | Native by refusal of the Dream; doubles `clockpunk`. The interesting one went back to the Feywild with a machine. |
| **Wizard** | The swallowed jewel as a spellbook (Jeweler's Tools). "Anything can be taken apart" as scholarship. |
| **Rogue** | Reynard; Mage Hand Legerdemain is a screwdriver at range; the Renegade Gnome Arcane Trickster (seed 65) is "through a lock before they finish arguing about the noise". |
| **Bard** | Commedia: the masked improviser with a hurdy-gurdy. |
| **Sorcerer** | Clockwork (native), Wild Magic (curiosity that will not wait). |
| **Monk** | Mercy: the anatomist, "the whole map" of the body as a mechanism. Vesalius with a mask. |
| **Barbarian** | World Tree: the Renaissance cosmos, and the Hermeticist's "as above, so below" as the tree. A Gnome whose Rage is curiosity refusing to wait. |
| **Fighter** | The Eldritch Knight learned magic as clockwork ("this movement, this word, in this order"); `clockpunk` hands them a wheel-lock. |
| **Druid** | Tension: the craft is a place; the grandmother said never to love land. A Gnome Stars Druid found the one place that cannot be taken. |
| **Ranger** | Forest Gnome: the companion talks back (Speak with Animals). A badger, or a clockwork bird. |
| **Cleric** | The watcher as heirloom: the Holy Symbol is the thing worth more than it looks. |
| **Paladin** | Devotion: the oath as the thing carried; Sacred Weapon as heirloom. |
| **Warlock** | Archfey: asked to go back for four hundred years, and finally went, on terms. |

---

## 🔎 7. Backgrounds

- **Hermeticist.** "A traveling jeweler you hosted for a winter." The Gnome's
  own background by marker: correspondence, jewels, the locked cabinet. The
  Hermeticist Gnome is the Renaissance magus.
- **Archaeologist.** "The record will make you the reference": the Gnome who
  keeps history in a thing, professionally.
- **Naturalist.** "You paint fast." Curiosity as a career; the lenses.
- **Debunker.** "The medium's table lifts because of a very strong left knee."
  The Gnome who takes the trick apart.
- **Investigator.** "Observe. Record. Eliminate." The Rock Gnome's creed as a
  method.
- **Renegade** (seed 65). The crew as the thing carried.
- **Servant** (seed 43). The sommelier who catalogued the cellar.
- **Squire** (seed 75). The one who kept the archmage's book.
- **Stranger.** The Gnome's four hundred years, without the welcome.
- **Fated.** "You break things." The Gnome who breaks things and makes
  something out of the pieces: the species' creed as a curse.
- **Artisan (official).** One sentence.

---

## 🔒 8. Decisions log

**Decided**

- The three keys and the two legends; the Gnome as the Renaissance pair's
  middle point; gems lean to the Gnome.
- The species entry and lineage voice.

**Open (this page proposes)**

- **The metaphysic**: *curiosity*, as the principle that replaced the Dream,
  for the peoples table.
- **The Gnome Artificer** should not be the default the generator offers most
  (the doubled `clockpunk` reads flat by design).
- **Darkvision** already prints with a line here; if the Aasimar convention
  spreads, nothing changes.

---

## 🚧 9. Lines

*The lines exist and are strong; listed as the reference.*

| Entry | Line (shipping) |
|---|---|
| **Darkvision** | *The Fae are said to be part of the Dream. Maybe Gnomes still carry some of it, because you have always felt the night welcomes you.* |
| **Gnomish Cunning** | *Curiosity got your people through worse than a spell, and it still does.* |
| **Forest Gnome lineage** | *You were not supposed to go into the woods, but the Fey felt closer there, and you learnt to listen…* |
| **Rock Gnome lineage** | *You learned early that anything could be taken apart and improved, and somewhere along the way you learned to do it with a word instead of a screwdriver.* |

---

## 🧾 10. Pointers

- **Artificer page**: native by refusal.
- **Elf page**: the reverse Gnome.
- **Dwarf page**: one trade route.
- **Wizard page**: the swallowed jewel.
- **Sorcerer page**: Kepler.
