# 🎭 NPCs and Villains: the other side of the table

*Wiki entry for the design team. The NonPlayer side has three engines: the
live summoner the app calls (`Map_of_NonPlayer_Generation`, running from
vaulted bytecode since the 2026-08-29 recovery), the legacy `NPC` class in
`AtlasAlusoris/Grimoire_of_NPC.py`, and the Dungeon Master Companion's
Adventure oracle in `AtlasEpica`. Compiled 2026-09-08 from the code, four
legacy NPCs, and the villain sourcebook in the project's book folder.*

> **In one sentence.** The NPC catalogue was written before the peoples' canon
> and says the opposite of it for Celestials and Fiends, the undead table is
> the one that already thinks the way the canon does, and today no NPC can be
> summoned at all.

---

## 1. State of the engines (report, not repair)

*Framing, appended after reading Decree 0004: the first publish is the Player
Character generator, and "NonPlayer Characters, NPC lists, Dungeon Master
Companions, dungeons, and Epica stay in the repository. They are parked, not
deleted," behind `PLAYER_ONLY_PUBLISH` in `app/publish_scope.py`. Everything in
this section is therefore a defect in a parked path, not a shipped one; the
Questae to unpark them (QST-0084, 0085, 0086, 0075) are where it lands.*

⚠️⚠️⚠️ **The live NonPlayer summoner fails on every attempt.** `summon_nonplayer`
(with or without arguments) raises *"Unable to summon a NonPlayer Character
after five attempts."* Every attempt dies in the vaulted `Grimoire_of_NPC` at
`SetSize`: it calls `Size` with two arguments and `Map_of_Size.Size` takes one.
The Alusoris sheet and the DM Companion cannot produce a character. The
bytecode being run is a longer, newer `Grimoire_of_NPC` than the 577-line
source on disk, so the source of truth for the NonPlayer lane is still the
vault, against the recovery board's own restore order.

Other findings on the way there, all in the legacy source:

- `generate_npcs` calls `NPC.NPC(...)` on the class: dead on arrival.
- The NPC's story is always empty: `SetMyStory` swallows a `TypeError` from
  the Story engine applying TagKit's `~` to a plain `NPC`.
- `NPC.alignment` assigns the drawn alignment and returns a local "Neutral";
  four of four sampled NPCs printed True Neutral.
- `Map_of_Prose_Adventure` imports `Locus`, `Power` and `Plan` from
  `Grimoire_of_Adventure`, which defines none of them, so the scene module and
  `Charts_of_Choice_Collapse` fail to import. "Generate scene" has nothing
  behind it.

What works: the legacy class produces names, titles, traits, ideals and plot
hooks (*Asusala Yuluihel, The Gaze Speaker, Seraph Priest, "Justice. Place in
society shouldn't determine one's access to what is right."*).

---

## 2. The catalogue

Twenty-five kinds in `race_weights` (Aberration, Aven, Beast, Beastfolk,
Catfolk, Celestial, Construct, Dragon, Dwarf, Elemental, Elf, Fey, Fiend,
Giant, Gnome, Goblin, Halfling, Human, Kobold, Lizardfolk, Monstrosity, Ooze,
Orc, Plant, Snakefolk, Undead, Vampire), each with a weighted sub-table and a
design comment. Three of the sub-tables matter to the canon.

### Celestials: the table the canon overturned

The docstring is the 2014 Monster Manual: *"servants of deities… Celestials
tend to be good by nature, so the exceptional celestial who strays from a good
alignment is a horrifying rarity."* The Celestials canon says the reverse on
every point: Ideals prior to gods, no sender, not good, and the Descents as
manners of falling that are common, not rare.

The sub-table: *Angelic Bloodline, Half-Angel, Angel, Ascended, Saint, Couatl,
Forgotten God, Lesser God, Tutelar, Planetar, Seraph, Throne, Unicorn,
Celestial Serpent, Valkyrie, Solar, Ki-rin, Deva, Asura, Archon, Archangel,
Avatar, Zodiac.* Pseudo-Dionysius, the Vedas, the Norse, the Monster Manual
and the horoscope in one list.

- ✅ *Zodiac* ("star-made beings that weave fate") is the Star Descent already.
  *Saint* is the Dwarf canon's word. *Ascended* is the Dragon canon's word.
  *Couatl* is on the Celestials page. The pieces exist.
- ⚠️ "Angelic Bloodline" and "Half-Angel" are the Aasimar told as ancestry,
  which the Aasimar page spent a section refusing.
- **Proposal.** A Celestial NPC is **an Ideal and a manner**: draw one of the
  eight Ideals, then a Descent from the Celestials page (Star, Muse, and the
  rest), and let the kind-name be the manner's name. *Seraph, Throne, Archon*
  can stay as the words mortals use for the same thing seen at different
  distances, the way Fae, Fata and Shadow are one substance with three names.

### Fiends: the mechanism, half-applied

The docstring is right where it is its own: *"Devils are related to Guilt,
Sin, Desire, Punishment and Retribution. Demons to Chaos, Vanity, Ego, Lust,
Change, Sickness and War."* Those are belief axes, which is what the Tieflings
canon says fiends are made of.

- ✅ *Dwarvendevil, Elvendevil, Orkishdevil, Goblindevil, Dwarvendemon…*: a
  fiend per people. If belief makes fiends, every people damns its own, and
  this table already knows it. Keep and name them properly.
- ⚠️ **"Tiefling: 30" is the heaviest entry in the Fiend table.** The canon's
  first rule is that a tiefling is a person born to ordinary parents; listing
  them as a fiend kind is the theological shift the setting is about, performed
  by the generator. Move them to the peoples (the player Species already
  exists) and leave the fiends to the fiends.

### Undead: the table that already thinks like the canon

*Despair Specter, Honor Phantom, Penance Wraith, Pride Mummy, Fear Shadow,
Wrathful Wraith, Mischief Poltergeist, Protector Spirit, Ungone Ghost, Thinker
Skull, Tomb's Hoarder, Vengeful Revenant, Weeping Howler, Cursed Eternal.*

✅✅ **An undead is an emotion that would not stop.** Each kind is a feeling or
a vice with a body: the Barbarian canon's "living true to an emotion" carried
past death, and the Tiefling canon's belief-engine with the believer removed.
Nobody wrote this down and it is the best-designed table in the file. It is
also the one NPC table whose names would work as the *sentence* the Celestials
page asks for ("the Penance Wraith is the one that is still apologising").

### The rest, briefly

- **Elves**: seventeen lineages (*Night, Eclipse, Sands, Urban, Sun, Snow…*).
  The player canon says lineages are places dreamt long enough; seventeen
  places is fine, the names are Warcraft's.
- **Dragons**: the table lists dragon kinds. The canon says a dragon is a
  person who Ascended; the NPC table should be persons, with a hoard that is a
  meaning, and the kind as the shape their tradition gave them.
- **Humans**: the twelve relative-geography cultures the Names page found
  (*Local, Foreigner, Highlander…*), not the Cultural-Inspirations keys.

---

## 3. Archetypes and backgrounds: two vocabularies

`Archetypes` (43) mixes the thirteen Guilds with roles (*Artist, Commoner,
Crafter, Merchant, Mentor, Scholar*) and villain roles (*Bandit, Cultist,
Pirate, Spy, Trickster, Witch, Ninja*). The live path's `NONPLAYER_BACKGROUNDS`
is the sixteen official backgrounds plus twenty-four of those role names.

⚠️ **None of the thirty-two written backgrounds is available to an NPC.** This
is the same gap the Stories page found from the other side, and it costs more
here, because the written backgrounds' hooks are already DM-facing: *Markers*,
*Indentured*, *House Calls* are things that happen to the party, written for
the person running the table. A Servant NPC with the Servant's hook is a
finished villain-adjacent character in one paragraph, and the generator cannot
make one.

---

## 4. Personality: 4,209 lines, gated by alignment

`Map_of_Personality` holds introductions, 335 plot hooks, traits and ideals.
The gates are alignment (Lawful, Chaotic, Good, Evil, Neutral) and a handful of
archetypes (Priest, Cultist, Scholar, Bard, Traveler). The kind is never a
gate: `subrace` appears 1,276 times and every one is an f-string ("I'm a
{subrace}. What can I do for you?").

- The introductions are keyed by Intelligence and Charisma modifiers; the low
  corner is the caveman ("Me {name}. Call me {title}!").
- The ideals are the 2014 background ideals verbatim ("Aspiration. I seek to
  prove myself worthy of my deity's favor…").
- The plot hooks are first-person and serviceable ("There is something trapped
  in this place. I seek to keep it that way." is good). Register: 2014.

**The villain book's method** (in the project's book folder) is the standard
the NPC prose should meet: *values, not morals*. "A character can have no
hang-ups about stealing in general but still hold that it isn't good to steal
from friends." One value per NPC, stated as a line the DM can play, replaces
most of the alignment gating. The book's five types map onto the archetypes
cleanly:

| Type | Archetypes | What the value is about |
|---|---|---|
| **Outlaw** | Bandit, Pirate, Criminal, Spy, Ninja, Trickster | Who they will not rob. |
| **Leader** | Noble, Knight, Hero, Mentor, Soldier | Who they will not spend. |
| **Believer** | Cultist, Priest, Shaman, Witch, Warlock | Whether they believe it. "The player decides if a Believer has a genuine investment in what they preach." |
| **Opulent** | Merchant, Noble, Artist, Crafter | What they will not sell. |
| **Supernatural** | Undead, Fiend, Celestial, Dragon, Vampire, Fey | What they were before. |

The Celestials page's antagonist shapes are Believers and Supernatural at
once; the Dragon Cultist background is a Believer who worships a Supernatural
that despises worship.

**Draft value lines**, one per villain-facing archetype:

| Archetype | Line |
|---|---|
| Bandit | *Not from the ones who fed us. Everyone else is weather.* |
| Pirate | *The ship is the country. The rest is coastline.* |
| Spy | *I have never lied to the one who pays. Ask me who that is.* |
| Cultist | *I believe it. That is the part they cannot forgive.* |
| Priest | *I stopped believing years ago. The people did not, and they are my job.* |
| Witch | *I keep the bargains. Read them before you sign.* |
| Knight | *I gave my word once. Everything since is the shape of keeping it.* |
| Noble | *The house before the name. The name before me.* |
| Merchant | *Everything has a price. I have never once sold the thing that does not.* |
| Mentor | *I will teach you everything, and one thing I will keep, and you will hate me for the right one.* |

---

## 5. The Dungeon Master Companion

The Adventure oracle is well shaped: one BBEG ("the DM Character; villain,
Quest Master, guardian, or other roles are equally valid; the actuators do not
assume evil"), an **Area** (Urban, Forest, Dungeon, Swamp, Mountain, Desert,
Coast, Graveyard), a **Lair** inside it (Tower, Temple, Castle, Catacomb, Port
Den, Circle, Cave, Manor: "polite face over a rotten core"), and six **Themes**
(Love, Hubris, Nest, Discovery, Mastery, Creation) collapsed from the DM
Character's Tags with the same seeded, gated collapse the Stories use.

✅ The Themes are the right axis: six reasons a person builds a lair, none of
them "evil." ✅ The page copy: "They may be a villain, a Quest Master, a
contested…" carries the design.

⚠️ The scene layer behind it does not import (§1). ❓ The Dungeon Area's
description reads "Tragones y Mazmorras sense": Julio's pun, in a string that
may print.

---

## 6. Proposals

1. **Restore the NonPlayer lane from source**, then the `Size` call. Until
   then the NPC side of the app is dark, and this page's other proposals wait.
2. **Celestial NPC = Ideal × Descent** (§2), keeping the old kind-names as
   distances, not kinds.
3. **Tiefling out of the Fiend table**; the per-people fiends kept and named.
4. **The written backgrounds available to NPCs**, hooks as plot hooks.
5. **Values, not alignment**, as the personality gate; one line per archetype
   (§4); the undead table's method (an emotion with a body) as the model for
   the Supernatural type's lines.
6. **Dragon NPCs as persons who Ascended.**
7. The Prose Adventure axes (Locus, Power, Plan) defined or the imports
   dropped, so "Generate scene" does something.

---

## 7. Decisions log

**Standing**: the Adventure oracle's shape (BBEG, Area, Lair, six Themes); the
undead sub-table; the Fiend docstring's two belief axes; the per-people fiends.

**Open (this page proposes)**: §6.

**Julio's call**: "Tragones y Mazmorras" on the sheet; whether *Angelic
Bloodline* and *Half-Angel* survive as NPC kinds at all.

---

## 8. Pointers

- **Celestials page**: the Ideals, the Descents, the antagonist shapes an NPC
  Celestial should be drawn from.
- **Tiefling page**: born to ordinary parents; belief makes fiends.
- **Barbarian page**: living true to an emotion, which the undead table
  extends past death.
- **Dragonborn page**: a dragon is a state.
- **Stories-and-Titles**: the same background gap from the player's side.
- **Names**: the NPC Human cultures.
- Recovery board: `.recovery-vault/RECOVERY-COORD-final.md`.
