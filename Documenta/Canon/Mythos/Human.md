# 🧭 Human

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
Compiled 2026-09-08 from the Human kit, the species entry, `AtlasNomina/Races/Human.py`,
`Cultural-Inspirations.md`, the class analyses and the design notes.*

> **In one sentence.** The wonderful wanderers: there is nowhere humans are not
> and nowhere humans wouldn't go, they thrive by friendship, and they organise;
> there is always a human kingdom a couple of days' walk away.

---

## 📜 0. Rules

*The fixed points, and what we made of them. The books are defined at the head
of the page.*

### The rules as given

*Each entry is the rule itself, complete enough to resolve at a table. Not a
summary and not a cross-reference.*

> 📕 **Creature Type.** You are a Humanoid. That is your Creature Type for every
> rule that cares about one: a spell that targets a Humanoid (Charm Person names
> one Humanoid you can see), and any effect that includes or excludes Humanoids.
>
> 📕 **Size.** You are Medium (about 4 to 7 feet tall) or Small (about 2 to 4
> feet tall), chosen when you select this species. Your size sets the space you
> occupy, and it gates Grapple and Shove, which can target a creature no more
> than one size larger than you.
>
> 📕 **Speed.** Your Speed is 30 feet.
>
> 📕 **Resourceful.** You have Heroic Inspiration after every Long Rest. Heroic
> Inspiration is a state you either have or do not have, so a second grant does
> not stack; if you gain it while you already have it, you can give it to a
> player character who lacks it. You can expend it to reroll any one die
> immediately after rolling it, and you must use the new roll. The recharge is
> the Long Rest: there is no per-day limit, and a Short Rest does not restore it.
>
> 📕 **Skillful.** You gain proficiency in one skill of your choice, from the
> eighteen skills (Athletics, Acrobatics, Sleight of Hand, Stealth, Arcana,
> History, Investigation, Nature, Religion, Animal Handling, Insight, Medicine,
> Perception, Survival, Deception, Intimidation, Performance, Persuasion), minus
> any you are already trained in. The generator resolves the choice and prints
> the resolved skill, so a finished sheet reads "You have proficiency in
> Survival."
>
> 📒 **Versatile.** You gain one Origin feat of your choice, and you must still
> meet its prerequisites. The generator draws the feat and prints it under its
> own name, with the full feat rules in its own entry; the trait's own name never
> appears on the sheet.
> > 📘 _Somebody, somewhere along the road, taught you one more thing. You did not always ask what it would cost._ (proposed)

Nothing in the Human is renamed, so this page carries no 📙. One rule is changed,
so it carries one 📒.

**Size, and why it carries no 📒.** The two options and their heights are the
2024 rule exactly. What the kit adds is a generation weighting the published rule
does not have: `size_weights=(95, 5)` in `Humans.py`, so an unattended draw
returns Medium 95% of the time and Small 5%. That is not a house rule. The
published rule is a free player choice, and a generator that prints a finished
sheet has to resolve it, exactly as it resolves the Skillful skill and the
Versatile feat. A player who states a size still gets it, and nothing about what
is legal at the table moves. The weighting is recorded under the variable detail
below, with the other resolved choices.

**Versatile, and why it carries the 📒.** One rule change, one dropped
recommendation, one added clause and one presentation change.

- **The pool.** The published trait draws from the Player's Handbook's ten Origin
  feats. The base table here holds twelve entries, because it splits Magic
  Initiate into Cleric, Druid and Wizard. This one draws from **37**: those
  twelve plus 25 Origin feats from five later official books (Eberron: Forge of
  the Artificer, Forgotten Realms: Heroes of Faerûn, Astarion's Book of Hungers,
  Lorwyn: First Light, Ravenloft: The Horrors Within), nine of the 25 being Dark
  Gifts. A Human generated here can sit down at a Player's Handbook table holding
  a feat that table has never seen. That is the compatibility cost, and it is
  what the 📒 marks.
- **"Skilled is recommended" is dropped.** Advice rather than a rule, so it costs
  nothing mechanically; it is noted because the entry above would otherwise read
  as the published text and is not.
- **"You must still meet its prerequisites" is added text**, and nothing checks
  it. No feat in the pool carries a prerequisite: the Dark Gifts' published one
  ("a Ravenloft campaign") was deliberately dropped when they were written in.
- **The trait is not printed under its own name.** Versatile has no grant of its
  own in the source. The feat it draws is granted with a source string naming
  Versatile, and the sheet's view layer keys off that string to write its own
  prose ("Humans have complex lives, and they adapt quickly. You have this extra
  Origin Feat: ..."). The Trait's own description text never reaches a reader.

**The 📒 is undeclared.** No Questa and no Decree stands behind the enlarged
pool. It is marked 📒 because it already costs compatibility, not because the
system has recorded it, and the mark stays provisional until a Questa says
otherwise.

⚠️ The enlarged pool is not stable in practice, which is part of what that Questa
has to settle. Three faults, all reproduced in this worktree today:

- **Its size depends on import order.** The base table is mutated in place by the
  feat atlas rather than shadowed, so a caller that reaches the species kit
  without pulling the atlas in generates published-rules Humans. Importing
  `SpeciesKit.Humans` alone leaves the pool at 12 entries; importing
  `Grimoire_of_Characters` leaves it at 37.
- **Two of the added 25 fail outright.** Echoing Soul and Symbiotic Being both
  import a name (`STANDARD_LANGUAGES`) that `AtlasLudus.Map_of_Languages` does
  not define, and the ImportError surfaces as an Imprint failure that aborts the
  Character. A probe of 400 seeded Humans lost 13 of them to it.
- **A draw can land on a feat the Background already granted**, and the species
  feat then vanishes with no error anywhere: applying a feat Tag a Character
  already carries adds nothing to the sheet and raises nothing.

None of the three is recorded. No row on the Repairs Ledger names them and no
Questa does. Declaring the pool means fixing its boundary and its stability in
one ruling.

### The supportive lore

> 📘 **The four culture keys are `africa` (Sub-Saharan), `egypt`, `maghreb`
> (Moorish and Berber) and `carthage` (Punic).** Africa is read across the whole
> continent and its history, as four traditions rather than one, and the keys are
> orientative: they weight the pools rather than replacing them.
> Recorded by **QST-0046.2**. `egypt` and `carthage` are live keys in those
> tables, named among the entries **QST-0046.4** had to rewire when it split the
> classical markers.
>
> 📘 **Four societies is the Human's count, and that count is why the cultural
> budget is shared.** A people holding four societies paid four times the
> cultural weight, drowned the trade layer and broke the rustic test, so the
> budget became one figure split across the markers held rather than a weight per
> marker.
> Recorded by **QST-0046.5**. In the live table the split counts the legend
> marker too, so the Human's five markers take a share of two apiece.
>
> 📘 **The markers drive substance as well as name.** Materials are keyed by the
> same markers as the gear titles, so one species row drives both the name and
> the material, and materials stay flavour rather than a number.
> Ratified by **QST-0046.6**.
>
> 📘 **Skillful grants one skill, and the Background then grants two more from a
> pair fixed in the Background.** Nothing stops them overlapping, and the probe on
> the record put the collision at 23 Humans in 200, roughly one in nine, losing
> the species skill silently. That is the collision the Human's skill draw has to
> live with.
> Recorded by **QST-0050.5**.
>
> 📘 **The species entry speaks in the first person plural**, as "we" and "our
> people", landed at commit `9be3a07` together with one Species section on the
> sheet.
> Recorded by **QST-0087**. That the Human, Dwarf and Elf say "we" while seven
> other peoples address the reader as "you" is an open taste call and not a
> settled convention (**QST-0094**).
>
> 📘 **The feature entries carry an italic inspiration line and then the rule in
> the rulebook's present tense.** The Human sits in the audit row where every
> entry follows that pattern.
> Recorded by **QST-0094**.
>
> 📘 **Backgrounds and classes stay class- and alignment-agnostic: premise may be
> stated, personality may not be prescribed, and no institutional history the
> player never chose.** So a Human Cleric's priesthood is a draw, never a mandate.
> Law by **Decree 0007**.
>
> 📘 **A people should not be metaphysically silent.** The peoples table carries
> one organising principle per people, and a people either takes an existing one
> or brings its own. This is the norm the compact answers; the compact itself is
> unratified, below.
> Recorded by **QST-0053**.

Two of those identifiers are solved (QST-0046.4, QST-0046.6) and Decree 0007 is
law. The rest are open or working questae, so a book here means the claim is
inside the formal system, not that the system has finished with it. Two of them
(QST-0046.2, QST-0050.5) still live in the legacy `Curia/` tree that QST-0093.9
is folding into Documenta; the duplication is that unfinished rename, not a
second system.

### Unratified, and what each one needs

*Stated as design, not as law. Each line names the Questa that would ratify it.*

- **The compact as the Human's metaphysic.** The alliance, the institution, the
  marriage across peoples: something a people *makes between*, where every other
  principle is something a people *is*. The metaphysics table holds five peoples
  (Dwarf, Aasimar, Elf, Dragonborn, Orc) and gives the Human no principle at all.
  Needs a Questa entering the Human's organising principle into that table and
  ruling it against the ones already there, per QST-0053. The geography claim
  (there is always a human kingdom a couple of days' walk away) rides on the same
  Questa, or on a Places Questa if it is meant to bind the map.
- **The baseline, and the refusal of the Britain default.** Filed as decided, and
  resting on `Cultural-Inspirations.md`, which is canon and not the formal
  system. Needs a Questa recording that the Human is the setting's measured-from
  baseline and that the Anglo-Celtic default is refused.
- **`arthuriana` as the Human's one legend register**, early Arthur, shared with
  the Paladin and the Goliaths. QST-0046.4 names the key only as an entry needing
  rewiring and assigns it to nobody; QST-0046.5 records that twelve legend
  markers exist without saying who holds which. Needs a Questa assigning legend
  markers to peoples, the way the five classical society keys were assigned.
- **The per-Character *nomina* draw, and what it should draw from.** The draw is
  real and seeded (purpose `identity.species.Human.nomina_culture`, namespace
  `GenLegendNomina`), and it is stable per Character. But it does not draw a
  culture key. It draws one of twelve weighted human types (Local, Foreigner,
  Highlander, Nomad, Islander, Forester, Plainsfolk, Urbanite, Northerner,
  Southerner, Easterner, Westerner), and the name lexicon reads only "Islander"
  out of that result; the given-name pool is one blended agender list, not one
  culture at a time. So "the Human's naming is a mosaic by design" is a proposal,
  not a description of the code. Needs a Questa deciding whether the draw should
  be over `africa`, `egypt`, `maghreb` and `carthage` at all, fixing the contract
  and its seeded stream under Decree 0002, and ruling whether the drawn key must
  agree with the gear. Repairs Ledger B7 (the Human male name lists have never
  fired) sits in the same module and should be settled with it.
- **Versatile's pool: base feats plus every later official Origin feat.** Needs a
  Questa deciding the boundary explicitly, rather than by whatever the registry
  happens to hold when it is read, and covering the three faults above.
- **Dark Gifts in that pool, and that being the design.** A Human Tomb Raider may
  carry *Shadow Cast* with no shadow in sight, and what such a sheet needs is the
  gift's own line rather than a gate. The lines exist only as docstrings and
  never reach the sheet (Repairs Ledger E7). Needs one Questa deciding both
  halves at once, the absent gate and the docstring reaching the page.
- **Resourceful's grant, and the reading that none of the three traits is
  inherited**: luck, a trade, one more thing learnt, all of it given. The standing
  species law bans monoculture and moral determinism, and plainly physical traits
  may still be biological, so this reading has to be asserted for these three
  rather than deduced from the law. Needs a Questa extending QST-0056 (a feature
  must grant what it names) to the Human's three traits, so the grant and the
  taught-not-inherited reading are both on the record.
- **The trait lines.** *Today is **the** day, my friend.* and *You learnt by
  trying.* ship. Versatile has no italic line at all: its trait text is never
  rendered, and the prose the sheet shows is the view layer's own. Needs a Questa
  holding the lines for the author's word, exactly as QST-0094 holds the Dwarf's
  four, and reconciling the Versatile gap with QST-0094's audit row that says
  every Human entry already carries a line.
- **The four culture-keyed prayers and the species line.** `africa`/Life,
  `egypt`/Grave, `carthage`/Life and a plain `maghreb` line, under the Human's
  species prayer *Ask the gods, but trust yourself.* Needs a Questa on
  culture-keyed prayers, extending the QST-0080.1 lane from Domain openings to
  the species and culture pools.
- **The Human Cleric drifting toward the intercessor, and the institution as the
  Human's watcher.** Dialog 0016 is the only Agora text on the word, it rejects
  the intercessor as the Cleric's fantasy, and it names no species axis at all.
  Needs a Questa asking whether the species inflects the watcher, institution
  against parent.
- **The Orders engine as Human-shaped**, the Human building orders where every
  other people joins one. QST-0048, its notes and QST-0061 specify the engine and
  name no people. Needs a Questa on who builds the Orders, checked against Decree
  0007's standard on institutional history the player never chose.
- **The Human as every class's default**, and the default as where the cliché
  lands. The Human is the heaviest species draw (weight 120 against 100 for the
  next), but no Questa names a default species, and the generator questae treat
  species as drawn or passed. Needs a Questa recording whether there is a default
  species at all, since the argument depends on it.
- **The writer's rule**: a Human Character is never generic, a Human Character is
  Egyptian, Carthaginian, Maghrebi or African, and the sheet should know which,
  with the gear and the name agreeing. QST-0046.2 frames the same four keys the
  other way, as orientative and implemented as a weight that deliberately never
  replaces the generic pool. Needs a Questa ruling the writer's rule and
  reconciling the two, because "never generic" and "orientative" cannot both be
  the law.
- **The per-key wells**: Thoth and the House of Life, Setne, Imhotep, Beni Hasan,
  Sekhmet, Rhampsinitus, the Nile, the Sothic year; Hannibal's oath, the Sacred
  Band, Hanno's *Periplus*; the griot and the kora, Anansi, Legba, the bluesman;
  the oud and the ney, the desert and the sea. Needs a Questa splitting the four
  keys' vocabulary and register the way QST-0046.4 split Athens, Sparta, Homer,
  Rome and the Vatican. The Human's keys have never had that pass.
- **The material rows.** Three per key in the live table: `africa` bloomery iron,
  ebony and brass, cowrie-set ironwood; `egypt` gilded bronze, carnelian-set
  gold, acacia and electrum; `maghreb` nickel-silver, cedar and camel bone,
  coral-set brass; `carthage` Tyrian-dyed bronze, esparto and iron, ivory-inlaid
  bronze. QST-0046.6 decided the mechanism and two vocabulary constraints, never
  these twelve rows. Needs a Questa asserting them against its coverage rule,
  that every marker a species can hold reads on a blade, a haft and a coat.
- **"Against everyone."** Two species entries name the Human directly: the Orc's
  ("the humans came to call it discovery") and the Halfling's (the scandal of the
  decade was befriending one). The Tiefling and Aasimar links are made on the
  wiki pages and not in the entries themselves: the Tiefling entry says "ordinary
  parents" and names no people, and the Aasimar entry mentions neither humans nor
  temples. So the ledger is thinner than the pages imply, and the pages are
  currently each other's only evidence. Needs a Questa ratifying the cross-people
  ledger, so each grievance is recorded once and each entry either carries it or
  does not.
- **The backgrounds as the Human's identity layer**, the written ones doing what
  the species entry cannot, and the official ones being the Human's natural draws
  and its thinnest prose. Documenta's Q-0011 with Dialog 0008 is still open on the
  written roster, and Q-0012 on the catalogues. Needs both settled into a Decree,
  plus a Questa on whether any people is background-first, and one on the official
  backgrounds' prose depth.

### What the rules force, and what we chose

The Human is the species the rules left empty. There is no Darkvision, no
resistance, no breath, no natural weapon, no lineage layer at all: the Human
declares no Heritage, which matches the published rule. Size is a choice, Speed
is the default, and the three traits are all choices resolved somewhere else, on
somebody else's table: one skill from the skill list, one feat from the feat
list, and one reroll. Mechanically a Human is other peoples' tables with a
Humanoid tag on top. That is the fixed point, and it cannot be filled in with a
trait, because the rules did not give the Human one to fill.

The project's answer is to read the blank as **made between**, and to put the
baseline in Africa, Egypt, the Maghreb and Carthage rather than in Britain.

**What that buys beyond the rule.** The three traits stop being inheritance and
become gifts, which is the reading the species law leaves open for traits that
are not plainly physical: Resourceful is the luck a road gives, Skillful is a
trade somebody taught, Versatile is one more thing learnt from one more ally. The
wide Versatile pool becomes design rather than accident, so a Dark Gift on a
Human sheet is the alliance nobody chose, and the repair it calls for is the
gift's own line and not a gate. The empty Heritage set stops being a hole,
because the Human's lineage layer is the culture key and the background, which is
why the background carries the identity and why a per-Character draw over the
four keys is worth having even though the code does not do it yet. The four keys
give the setting's most-drawn species the one place where the world states its
geography, and every class page's rescue from its own cliché is the same four
keys. And the Human's virtue and the other peoples' grievances become a single
fact, so the people pages agree instead of contradicting each other.

⚠️ **What breaks if a later hand flattens the four keys into a generic human.**
The species is then empty in full: three mechanical choices, no body, no lineage,
no vocabulary, nothing for a reader to picture. The Orc and Halfling entries lose
the people their grievances name, and the Tiefling and Aasimar pages lose the
institution they were about to name. The traits have to become inheritance again,
which is the moral determinism the species law exists to stop, and Versatile's
pool turns back into a bug to be gated. And the setting quietly reverts to the
default the brief exists to refuse. The keys are not decoration on a plain
species; they are the only content the rules left room for. That most of this
reasoning is unratified is an argument for writing the questae above, not for
treating the keys as free.

### The variable detail

Drawn per Character, and carrying no book: the size, when none is requested
(Medium 95%, Small 5%); the Skillful skill, from the eighteen minus whatever the
Character is already trained in; the Versatile Origin feat, from the 37 in the
pool; the *nomina* type, one of twelve; and, per item, the gear title and
material, drawn across the four culture keys and the influence neighbours they
reach.

Most of it was not filled in at random. The size weighting keeps Small a real
possibility without making it the common Human. The skill and the feat are the
two in-species choices the published rule leaves to a player, so a generator that
prints a finished sheet has to make them, and it prints the result rather than
the choice. The culture keys drive the title and the material together, so the
name and the blade agree without anybody wiring them twice.

The *nomina* draw is the exception, and it should be read as unfinished rather
than as design: it is seeded and held per Character, but it draws a type
(Nomad, Foreigner, Southerner and nine others) rather than one of the four keys,
and only "Islander" changes what the name pool contains. Until the Questa above
rules on it, a Human's name does not know which of the four wells the sheet is
drawing from.

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

