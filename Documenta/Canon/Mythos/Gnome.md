# 🔧 Gnome

> 📖 **In flow.** 1 of 11 chapters are still proposals. 📜 5 · 📚 2 · 📔 3 · 📖 1

> - 📕 **inherited from the 2024 rules.** Moving it costs rules compatibility.
> - 📙 **an aesthetic change.** The same rule wearing our name and look.
> - 📒 **a rule we changed.** A house rule, and it already cost compatibility.
> - 📘 **supportive lore.** It holds a rule or a core element up.
> - 📗 **deep lore.** Design that supports the fantasy rather than a rule.
> - A book marks a statement only if it can change exclusively through the
>   Questa / Agora / Decree system. Anything with no Questa and no Decree behind
>   it carries no book, however settled it feels.

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

## 📜 0. Rules

*The fixed points, and what we made of them. The books are defined at the head
of the page.*

### The rules as given

*Each entry is the rule itself, complete enough to resolve at a table. Not a
summary and not a cross-reference.*

> 📕 **Creature Type** Humanoid. **Size** Small, the only option the species
> declares. **Speed** 30 feet.
>
> 📕 **Darkvision.** You can see in Dim Light within 60 feet as if it were Bright
> Light. In Darkness within that range you can see as if it were Dim Light: you
> have Disadvantage on Wisdom (Perception) checks that rely on sight, and you
> discern colors there only as shades of gray. All three clauses are scoped to
> that Darkness, and none of them touches the Dim Light you are reading as
> Bright. (The Disadvantage sentence is not in the 2024 glossary's Darkvision
> entry. It is the Lightly Obscured rule spelled out, because Darkness seen as
> Dim Light is Lightly Obscured, so printing it adds nothing to the rule.)
>
> 📕 **Gnomish Cunning.** You have Advantage on Intelligence, Wisdom, and
> Charisma saving throws. There is no trigger, no use limit and no recharge: the
> Advantage applies to every one of those saves.
>
> 📕 **Gnomish Lineage.** You are part of a lineage that grants you supernatural
> abilities. Choose one option: Forest Gnome or Rock Gnome. Whichever you choose,
> Intelligence, Wisdom, or Charisma is your spellcasting ability for the spells
> you cast with this trait, chosen when you take the lineage. The spell save DC
> for those spells is 8 + your Proficiency Bonus + that ability's modifier, and
> the spell attack bonus is your Proficiency Bonus + that modifier.
>
> 📙 **Forest Gnome Lineage** [renames **Gnomish Lineage**, its **Forest Gnome**
> option]: you know the Minor Illusion cantrip. You also always have the Speak
> with Animals spell prepared. You can cast Speak with Animals without expending
> a spell slot a number of times equal to your Proficiency Bonus (2 at levels 1
> to 4, 3 at 5 to 8, 4 at 9 to 12, 5 at 13 to 16, 6 at 17 to 20), and you regain
> all expended uses when you finish a Long Rest. You can also cast it using any
> spell slots you have.
>
> 📙 **Rock Gnome Lineage** [renames **Gnomish Lineage**, its **Rock Gnome**
> option]: you know the Mending and Prestidigitation cantrips. In addition, you
> can spend 10 minutes casting Prestidigitation to create a Tiny clockwork device
> with AC 5 and 1 Hit Point. When you create it you determine its function by
> choosing one effect from Prestidigitation; if the chosen effect has options
> within it, you choose one of those at creation, and the device does that one
> thing only. You or another creature can produce that effect by taking a Bonus
> Action to activate the device while touching it. You can have three such
> devices in existence at a time. Each one lasts 8 hours from its creation, or
> until you dismantle it with a touch as a Utilize action.

**No rule of the Gnome has been changed, so this page carries no 📒.** One line
looks like a house rule and is not. `AtlasLudus/Map_of_Languages.py:1388` reads
`if char == "Gnome": ling.Add("Gnomish")`, which would hand Gnomish to every
Gnome by species, against the 2024 rules, where languages arrive through a
character's origin and no Gnome trait grants one. It never fires: the branch
compares the Character object to a string, so it is false for that row and for
every other people's row beside it. The Repairs Ledger records it as **B1**, and
the reading behind it states the consequence plainly: no species has ever granted
a language, and the Languages box reads Common plus one entry taken by
`set.pop()` from the standard list. That is a defect of the languages engine,
species-agnostic and already logged, not a rule of the Gnome, and it costs this
page no compatibility. If the comparison is ever repaired, the line becomes a
real change and needs a Questa before it ships.

Two cautions about the entries above, both about what the sheet does with them.
**Gnomish Cunning prints and holds nothing.** `Gnomish_Cunning` in
`Gnomes/traits.py` is an empty Trait: it writes no value, and its entry in
`Gnomes/resolution.py` passes no chip, so the Advantage lives in a paragraph of
prose and nothing on the sheet can be read for it as a flag or a number. Every
sibling trait of the same shape does write one: the Halfling's `Brave` sets
`frightened_saving_throw_advantage` and prints a chip, the Goliath's
`Powerful_Build` sets `grapple_escape_advantage`, the Dwarf's
`Dwarven_Resilience` pushes Poison onto the sheet's own `damage_resistances`.
And the printed lineage entry drops the scope clause, giving "Spellcasting
Ability. Intelligence." without saying what the ability is for, even though the
same resolution already computes and stores `species_spell_save_dc` and
`species_spell_attack_bonus` from it. The rules above are the rules the sheet
states. The first is not yet a rule the sheet holds.

### The supportive lore

> 📘 **The Gnome's culture is three traditions: the Italian and German
> Renaissance, plus the Swiss.** Switzerland is the middle point of the pair,
> geographically between the two, and it is a register in its own right rather
> than more Renaissance.
> Ratified by **QST-0046.2** (`Curia/Questae/Working/QST-0046.2-gear-titles-and-materials.md`).
>
> 📘 **Gems and jewels lean to the Gnome, as metals lean to the Dwarf.** Extra
> weight in the draw, never a closed door.
> Ratified by **QST-0046.6**.
>
> 📘 **The Gnome and the Dwarf cohabit.** They trade and share settlements, and
> the culture map carries that as a route in the influence network rather than
> as a merged key.
> Ratified by **QST-0046.2**.
>
> 📘 **The Norse register belongs to the Elf, not the Gnome.** The boundary is
> machine-enforced: a self-test asserts that the name Brynja reaches an Elf and
> never a Gnome, so the two peoples cannot blur again.
> Ratified by **QST-0046.2**.
>
> 📘 **Markers share one budget, so holding more of them makes a people quieter
> per marker, not louder.** The cultural budget is split across the markers a
> people holds, and the marker list is deduplicated, so a marker reached from two
> sources at once is still counted once.
> Ratified by **QST-0046.5**.

That is the whole of the supportive lore this page can currently mark. Two of
those identifiers sit under `Curia/Questae/`, which is the same Questa system
under the folder's legacy name (QST-0046.4 records the rename as unfinished, not
as a decision), so they are still falsifiable by reading the file. Everything
below rests on the canon documents and on this page's own decisions log, which
are not the Questa / Agora / Decree system, so it carries no book until a Questa
says otherwise.

### Unratified, and what each one needs

*Stated as design, not as law. Each line names the Questa that would ratify it.*

- **Out of the Fae, and the refusal of the Dream.** The origin claim rests on the
  species entry and the Darkvision line. No questa or decree names the Feywild in
  any connection with the Gnome, and the questae that use the words *Fae* and
  *Dream* use them for other things. Needs a questa on the Gnome's origin that
  edits the peoples table, the way QST-0046.4 ruled the classical markers.
- **Curiosity as the organising principle.** The page proposes it and says so.
  The metaphysics table leaves the Gnome out entirely, and QST-0053 states only
  the general rule that a people should not be metaphysically silent. Needs a
  questa ruling curiosity and filling the row in `Dragons-and-the-Overcoming.md`.
- **The city offer as the lineage split.** Two answers to one event rather than
  two descents. The phrase occurs in no questa, dialog or decree; the only formal
  mention of the lineages is the import bug of QST-0038
  (`Curia/Questae/Solved/QST-0038-speak-with-animals-alias.md`, one of three
  files sharing that number). Needs a questa ratifying the device, which the
  Lineages page already treats as one of its two models.
- **Ways kept in things, not land.** The portability doctrine (a song, a recipe,
  a pattern in a rug) rests on the species entry alone. Needs a questa, so the
  class and background pages can cite it.
- **Everyone's neighbour, nobody's countryman.** A diaspora with a welcome,
  against the Tiefling's without and the Stranger's precarious one. The word
  returns nothing in the formal system and no questa sets the comparative. Needs
  one ruling the three diasporas together, the way QST-0046.4 ruled the Aasimar
  and Goliath pair.
- **The swallowed jewel, and the jeweller's practice.** QST-0064.1 writes that
  practice as **Jewelcraft Proficiency** and never names the Gnome; the amethyst
  necklace as a spellbook is the Wizard page's. Needs a questa linking the object
  to the species, so the accident is protected rather than remembered.
- **The Rock Gnome creed as species doctrine.** "The shame is not in breaking it
  but in failing to make something out of the pieces" is quoted or leaned on by
  the Wizard, Investigator and Fated readings and ruled by nothing. Needs a
  questa making the sentence citable.
- **The two legend markers, `clockpunk` and `folklore_dwarf`.** Neither is
  assigned to the Gnome anywhere in the formal system: `clockpunk` occurs in no
  questa, dialog or decree at all, and `folklore_dwarf` occurs once, as an
  example of the legend-marker idea in QST-0046.5, never on a people's row. Needs
  a questa naming both on the Gnome row.
- **Three culture keys named `italy`, `germany`, `switzerland`.** The only questa
  that names the Gnome's registers names two, `renaissance` and `swiss`, from
  before the atomic split. QST-0046.4 raises the Gnome only in its open
  questions, asking whether Gnomes want a piece of the five classical markers,
  and that question is unanswered. Needs a questa splitting `renaissance` the way
  QST-0046.4 split `greece` and `rome`, and answering that fourth question.
- **The register vocabulary.** Arlecchino and the commedia, the
  Antikythera-to-clockwork line, Reynard, Wayland, the hurdy-gurdy, the alphorn,
  rock-crystal, Milanese and Solingen steel: all return nothing in the formal
  system, which has so far ratified weapon words and materials only. Dante and
  the *Commedia* do reach it, but as the Cleric's tradition in that Guild's
  core-fantasy Dialog, never as the Gnome's register. Needs a questa on the
  Gnome's register.
- **The prayer lines.** The species tuple holds four (*Wonder and Wander*, and
  three turns on *Care not for what you cannot change* and *cannot carry*), with
  Knowledge keyed to Dante's line and Life to Saint-Exupéry's. The questa that
  committed the prayer ledger
  (`Curia/Questae/Solved/QST-0080-grok-session-cleric-voice-salvage.md`, not the
  QST-0080 under `Documenta/`, which is a different subject with the same number)
  decided only the Guild and Domain voices. Needs a questa on the species lines.
- **The name corpus.** Italian Renaissance lists plus Galician, and the name four
  parts long as a device. QST-0023
  (`Curia/Questae/Open/QST-0023-implicit-string-concats-in-races.md`) touches
  `AtlasNomina/Races/Gnome.py` only as a string-concatenation bug site. Needs a
  questa ratifying the two sources and the compound as intended.
- **The Gnome as the Artificer's people by refusal.** The Artificer dialog
  settles that class's fantasy without naming any species, and no class dialog
  names the Gnome except one passing reference to the QST-0038 import failure.
  Needs a questa or Dialog seating peoples under Guilds.
- **The Elf/Gnome mirror.** No questa pairs the two peoples; the only formal
  pairing separates their gear registers, not their metaphysics. Needs a questa
  on the comparative, so the reverse-Gnome reading rests on one decision.
- **Kepler's clockwork universe, and the Clockwork Sorcerer as native.** Kepler
  occurs nowhere in the Questa system (only on the Sorcerer and Artificer pages
  of this folder), and there is no Sorcerer core-fantasy dialog. Needs a questa
  on the Gnome's cosmology.
- **The thirteen class readings of §6.** The class dialogs decided fantasy with
  no species column. Needs one questa ratifying the Gnome column as a set, or a
  sidequest per class under it.
- **The eleven background readings of §7, and the three seeds.** Hermeticist
  reaches the formal system only as a grep target in QST-0091 and QST-0091.4;
  Archaeologist, Debunker, Investigator, Squire and Servant return nothing, and
  seeds 65, 43 and 75 appear in no questa. Needs a questa pinning the seeds, so
  the evidence is reproducible rather than remembered.
- **"The species entry and lineage voice", logged as Decided in §8.** The formal
  system says it is open: QST-0094 lists the species-description voice as one of
  two conventions still to decide, QST-0062 files the Gnome on one side of an
  unresolved two-register split, and QST-0051 still lists `Gnomes/` among the
  resolvers carrying filler attribution before the rule (stale for the Gnome
  today, but the questa is what moves). QST-0094 solved is what settles the line.
- **Darkvision printing with a line here, in §8.** QST-0094 leaves the
  cross-species Darkvision convention explicitly open (Elf, Orc, Gnome, Dwarf and
  Tiefling print the rule; Aasimar and Dragonborn print the chip only), and its
  audit table still files the Gnome as authored prose then the rule with no
  italic marker, which the current entry has since outgrown. Needs QST-0094 to
  answer its own question of one convention or two.
- **The Gnome Artificer suppressed as a default offer, in §8.** Nothing in the
  formal system touches species and Guild offer weighting, and the shared budget
  does not do this work either: the marker list is deduplicated, so a Gnome
  Artificer holds neither more nor fewer markers than any other Gnome and
  `clockpunk` is neither louder nor quieter for arriving twice. Needs a questa
  asking whether a doubled marker should affect a pairing in the offer at all.
- **"Physical traits are biological" applied to these traits.** The page asserts
  it for Darkvision, Gnomish Cunning and the lineage magic. QST-0051 and QST-0062
  discuss how the traits are voiced, never whether they are inherited. Needs a
  questa ruling the inspiration line per trait.

### What the rules force, and what we chose

The lineage is the demanding one. It forces two options under a single name,
both granting spells, both drawing on one ability chosen from three, and it says
nothing about why a Gnome is one or the other. Nothing else fills the gap:
`Kin_Fey` is a kinship reading rather than a Creature Type, and per the kinship
layer it grants no resistance, no sense and no trait, so the rules answer stays
Humanoid and a spell that seeks Fey does not find a Gnome. The Gnome is left
with a fae connection that has no mechanism, and a split with no cause.

Our answer is **one offer answered twice**. The city offer was made to the whole
people. The Rock Gnomes took it and filled a workshop (the bird that sings on
the hour, wound by a great-grandfather); the Forest Gnomes did not, and settled
past the last farm where the wood begins, where the fae are nearer and some of
it rubbed off. Not two bloodlines: two answers to one letter. Darkvision carries
what is left of the descent, and its line is the only place the kit says so.

**What that buys beyond the rule.** A Forest Gnome and a Rock Gnome at one table
are cousins rather than strangers, so the generator can draw either without
implying a separate ancestry, and the species' social claim (one people wherever
they live, ways kept in portable things) survives contact with a rule that looks
like two descents. The Rock Gnome's clockwork device becomes the workshop's
answer rather than a racial aptitude, which is why the creed about taking things
apart can be a teaching. The Forest Gnome's free casts scaling with Proficiency
Bonus reads as listening that improved with practice, not a gift of fixed size.
And Darkvision doing the fae work leaves the origin with exactly one mechanical
trace, held by the one trait that cannot be argued away.

⚠️ **What breaks if a later hand takes the city offer for decoration.** The two
lineages revert to two bloodlines, which contradicts the whole society chapter.
The Lineages page loses one of its two worked models of what a lineage is. The
Rock Gnome's device stops being a decision and becomes an aptitude, and the
creed loses the event it was taught at. Worst, since `Kin_Fey` grants nothing,
Darkvision's line is the only mechanical trace of the fae descent: cut it as
flavour and the origin rests on nothing whatsoever. That this reasoning is
unratified is an argument for writing the Questa, not for treating the offer as
free.

### The variable detail

Drawn per character, and none of it ratified: which lineage the Gnome takes; the
spellcasting ability for its spells (Intelligence, Wisdom or Charisma); which of
Prestidigitation's effects a Rock Gnome's device carries and what the device is
made to look like; and the name, four parts long, drawn from the module's
Italian Renaissance and Galician sources and its Italian and German pools.

None of it was filled in at random. The ability is drawn from a seeded bag and
then aligned to the character's class whenever that class casts on one of the
three, because nobody picks their second-best score; both outcomes are legal
choices, so the alignment costs no compatibility, and the recorded ability can
change once the class exists. Either lineage draw tells the same story, because
both are answers to the same offer. The name four parts long reads as a small
inventory, which is the portability doctrine in a name.

One number in the declaration is not a statistic: `weight=80` is the generator's
draw weight, and the declaration validates it as a species generation weight, not
as pounds. No height or weight table exists for the species anywhere in the kit,
and the published "about 3 feet tall" is carried nowhere.

---

## 📚 1. Where the Gnome lives in the code

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

## 📜 2. Origin: curiosity, not fae magic

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

## 📔 3. Society: ways kept in things

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

## 📜 4. Culture and registers

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

## 📜 5. Metaphysics: the reverse Elf

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

## 📔 6. The classes: curiosity in each

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

## 📔 7. Backgrounds

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

## 📜 8. Decisions log

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

## 📖 9. Lines

*The lines exist and are strong; listed as the reference.*

| Entry | Line (shipping) |
|---|---|
| **Darkvision** | *The Fae are said to be part of the Dream. Maybe Gnomes still carry some of it, because you have always felt the night welcomes you.* |
| **Gnomish Cunning** | *Curiosity got your people through worse than a spell, and it still does.* |
| **Forest Gnome lineage** | *You were not supposed to go into the woods, but the Fey felt closer there, and you learnt to listen…* |
| **Rock Gnome lineage** | *You learned early that anything could be taken apart and improved, and somewhere along the way you learned to do it with a word instead of a screwdriver.* |

---

## 📚 10. Pointers

- **Artificer page**: native by refusal.
- **Elf page**: the reverse Gnome.
- **Dwarf page**: one trade route.
- **Wizard page**: the swallowed jewel.
- **Sorcerer page**: Kepler.
