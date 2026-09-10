# 🏔️ Goliath

> 📖 **In flow.** 1 of 12 chapters are still proposals. 📜 5 · 📚 3 · 📔 3 · 📖 1

> - 📕 **inherited from the 2024 rules.** Moving it costs rules compatibility.
> - 📙 **an aesthetic change.** The same rule wearing our name and look.
> - 📒 **a rule we changed.** A house rule, and it already cost compatibility.
> - 📘 **supportive lore.** It holds a rule or a core element up.
> - 📗 **deep lore.** Design that supports the fantasy rather than a rule.
> - A book marks a statement only if it can change exclusively through the
>   Questa / Agora / Decree system. Anything with no Questa and no Decree behind
>   it carries no book, however settled it feels.

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from the Goliath kit and its six Giant heritages, the species
entry, `Cultural-Inspirations.md` (the Celestial/Giant comparative and the
Arthur ruling), the class analyses and the design notes on the Aasimar page.*

> **In one sentence.** Giants manifested before the first things and are still
> here if you know how to look at a mountain; each Goliath carries one Giant's
> favour the way other people carry a surname, tends the Order of Things, and
> comes from a civilisation that fell. The greater they fall.

---

## 📜 0. Rules

*The fixed points, and what we made of them. The books are defined at the head
of the page.*

### The rules as given

*Each entry is the rule itself, complete enough to resolve at a table. Not a
summary and not a cross-reference.*

> 📕 **Creature Type** Humanoid. **Size** Medium (about 7 to 8 feet tall).
> **Speed** 35 feet.
>
> 📕 **Giant Ancestry.** You are descended from Giants. Choose one of the six
> supernatural boons below; that boon is your Giant Ancestry. You can use it a
> number of times equal to your Proficiency Bonus, and you regain all expended
> uses when you finish a Long Rest.
>
> 📕 **Cloud's Jaunt** (Cloud Giant). As a Bonus Action, you magically teleport
> up to 30 feet to an unoccupied space you can see.
>
> 📕 **Fire's Burn** (Fire Giant). When you hit a target with an attack roll and
> deal damage to it, you can deal an extra 1d10 Fire damage to that target.
>
> 📕 **Frost's Chill** (Frost Giant). When you hit a target with an attack roll
> and deal damage to it, you can deal an extra 1d6 Cold damage to that target and
> reduce its Speed by 10 feet until the start of your next turn.
>
> 📕 **Hill's Tumble** (Hill Giant). When you hit a Large or smaller creature
> with an attack roll and deal damage to it, you can give that target the Prone
> condition.
>
> 📕 **Stone's Endurance** (Stone Giant). When you take damage, you can take a
> Reaction to roll 1d12, add your Constitution modifier to the number rolled, and
> reduce that damage by the total.
>
> 📕 **Storm's Thunder** (Storm Giant). When you take damage from a creature
> within 60 feet of you, you can take a Reaction to deal 1d8 Thunder damage to
> that creature.
>
> 📕 **Large Form** (character level 5). As a Bonus Action, if you are smaller
> than Large and there is room for you, you become Large for 10 minutes, and you
> can end it early with no action required. For that duration you have Advantage
> on Strength checks and your Speed increases by 10 feet (45 feet, from the
> Goliath's 35-foot base). Once you use this trait, you can't use it again until
> you finish a Long Rest.
>
> 📕 **Powerful Build.** You have Advantage on any ability check you make to end
> the Grappled condition, and you count as one size larger when determining your
> carrying capacity.

**Two of the six ancestries lost the word that makes them optional, and nobody
chose it.** Fire's Burn and Frost's Chill are printed as mandatory: the 2024 rule
reads *"you **can** deal an extra 1d10 Fire damage"*, and the shipping `EFFECT`
strings drop the "can" (`Giant_Heritages/Fires_Burn.py:21`,
`Frosts_Chill.py:23`), so the sheet says the damage simply happens. Read
literally that spends a use on every damaging hit, and a Goliath runs the pool
dry against a room of rats. The projection then contradicts itself in the same
paragraph, because the sentence the resolver appends is still optional: *"You can
do this 3 times, and you regain all expended uses when you finish a Long Rest"*
(`resolution.py:158`). Every number, damage type, range and duration is otherwise
the published one. Of the four remaining options, Hill's Tumble, Stone's
Endurance and Storm's Thunder all keep their "can"; Cloud's Jaunt never had one,
because a Bonus Action is already a thing you choose to take. So the slip is
confined to two files and reads as a wording error rather than a house rule. It
is undeclared either way until a Questa records it, and that Questa has to say
which: restore the "can", or state the change and accept the compatibility cost
it has already paid.

**The page carries no 📒.** Two entries were proposed as house rules and are
not. `Fire's Burn` and `Frost's Chill` render without the rule's "can", so the
printed sheet reads *"you deal an extra 1d10 Fire damage"* where the rule reads
*"you can deal"*. That turns an optional rider into a mandatory one and would
spend a use on every damaging hit. Their sibling options all keep "you can", so
this is a wording slip in an `EFFECT` string, not a declared change. A defect is
not a house rule: the entries above state the rule correctly and carry 📕, and
the slip is recorded on the Repairs Ledger.

**The page carries no 📙.** The code calls the option set `Giant_Heritage` and
hangs it off `Goliath.GIANT_HERITAGES`, and the Character record is
`character.giant_heritage`, but that record has no consumer outside the
self-test, and the sheet prints the published `Giant Ancestry: <option>`
(`resolution.py:154`). Nothing was renamed for the player, so no reskin needs
translating back.

Four notes on the rules as the code holds them.

**Size never rolls.** `size_options` has the single entry `"Medium"`, and
`_selected_size` takes `options[0]` without opening a dice bag when there is only
one (`physiology.py:30`). No height field exists anywhere in SpeciesKit, so the
published "about 7 to 8 feet tall" reaches no sheet. The one number in the
declaration that looks like a body measure, `weight=75`, is not pounds: `WEIGHT`
is the generator's draw weight for picking a species (`declarations.py:54`,
`application.py:26`).

**Large Form's Speed is an absolute, and it survives on purpose.** It is resolved
at build time as `speed + 10` (`resolution.py:214`) rather than printed as a
bonus. Class training does mutate `character.speed` on the live path (the Monk
adds 10 at level 2, `Map_of_Classes/Training/Monk.py:54`, and 5 more at four
later levels), so an absolute would go stale if it were computed once. It is not:
`New_Player` calls `Resolve_Species_Features` twice, the second time after
`apply_class_features()` (`Grimoire_of_Characters.py:234` and `:252`), and the
recompute assigns rather than accumulates, so it is idempotent. What remains is a
snapshot taken at that last pass. Anything that changes Speed after it, an item
or a spell, leaves the printed number behind.

**The Stone's Endurance chip disagrees with its own prose.** The chip renders
`1d12 +0` at Constitution 10, because `CHIP_VALUE` formats the modifier with
`:+d` (`Stones_Endurance.py:26`), while the prose of the same entry renders a
bare `1d12` through `_signed_die` (`resolution.py:97`). `_signed_die` is the
correct implementation, and the chip should call it.

**Two residues of the clipped voice are still shipping.** Every Giant Ancestry
entry opens with a bolded activation label taken from `heritage.ACTIVATION`
(`resolution.py:157`), so the sheet reads *"**Damaging Attack-Roll Hit.** When
you hit a target…"*, and that is not a phrase the 2024 rules use. And
`Frosts_Chill.DURATION` is *"Start of this Character's next turn"*, the last
third-person string left in the Goliath tree; it is a Record rather than printed
prose, but it is the exact pattern QST-0062 was raised to remove.

### The supportive lore

> 📘 **The Goliath's classical identity is Legionary Rome plus Spartan and
> Homeric Greece.** The Goliath and the Aasimar do not divide the classical world
> between them: each takes half of each, and the halves are opposites. What is
> ratified alongside it is the register pair, the Celestial half philosophical and
> pensive against the Goliath half practical and physical.
> Ratified by **QST-0046.4**.

> 📘 **Three atomic culture keys: `rome`, `sparta`, `homeric`.** The single
> markers `greece` and `rome` were retired and replaced by five atomic ones.
> QST-0046.4 gave the Aasimar `athens` and `vatican`; the Goliath holds the other
> three, with `rome` now meaning the practical legion (road, aqueduct, drill).
> Its open question 2 still asks whether `vatican` is the right word, which
> touches the Aasimar half only.
> Ratified by **QST-0046.4**.

> 📘 **Homer holds a key of his own.** `sparta` is the agoge and the phalanx;
> `homeric` is the Iliad and the heroic age, because a hoplite in formation is
> not Achilles. `homeric` is a *society* key and carries the titans and giants,
> while `wyrm_myth` keeps the monstrous register, so the two no longer hand a
> Goliath the same words twice.
> Ratified by **QST-0046.4**.

> 📘 **The substance follows the key.** `Map_of_Materials._CULTURAL_MATERIALS`
> splits the same five ways as the names: hoplite bronze is Spartan, Noric steel
> and tinned bronze are legionary. The five keys are present in the file
> (`Map_of_Materials.py:320`, `:339`, `:344`, `:351`, `:357`).
> Ratified by **QST-0046.4**.

That is the whole of the supportive lore this page can currently mark, and all of
it is culture. Nothing formal reaches the origin, the favour, the duty or the
fall: the four things this species is actually about are unbacked. Everything
below rests on the species entry, on `Cultural-Inspirations.md` and on this page's
own decisions log, which are not the Questa / Agora / Decree system, so it carries
no book until a Questa says otherwise.

### Unratified, and what each one needs

*Stated as design, not as law. Each line names the Questa that would ratify it.*

- **The Giants are the world, and they came before the gods.** "Manifested before
  the first things"; "the gods took the heavens and the songs, the First Ones kept
  the world". This is the species' organising principle and it rests on the entry's
  prose alone. Needs its own lore Questa. QST-0053 asks that a species take a
  principle from the metaphysics table in `Canon/Dragons-and-the-Overcoming.md` or
  bring its own rather than stay metaphysically silent, but it asks it of *new*
  playable species and never names the Goliath, so it is a model for the ruling
  and not the ruling.
- **One favour, drawn once, kept, and gifted rather than inherited.** The code
  enforces the count: `Current_Giant_Heritage` raises if two are carried, and
  `Imprint_Giant_Heritage` refuses the second, which the self-test proves by
  expecting `TagImprintError`. Nothing rules the draw permanent across a rebuild,
  nor the framing a gift from a relative who is also a landscape. QST-0079 (vault
  survey findings) knows the six only as a structural count, "Goliaths' Giant
  Heritages ×6", inside a file-shape survey. Needs a Questa so the Species Form's
  Heritage Tags carry the rule instead of the prose.
- **The six favours grant what their lines name.** No Questa names any of the
  six. QST-0056 ("features must grant what they name") is the standing
  verification Questa and does not mention the Goliath. Needs a sidequest of it,
  so the favour table is checkable rather than remembered.
- **The Order of Things as the Goliath's stated duty.** "Our strength is not our
  might, but our duty." The phrase returns nothing across the Questae and the
  Agora, and Dialog 0017 settled the Druid's covenant without it. Needs a lore
  Questa, which must also decide whether it is species prose only or the Land
  Circle's covenant too.
- **The trait lines as the house pattern.** *"You were made smaller than your
  ancestors, never lighter"* and *"For a few minutes you are the size your
  ancestors never stopped being"* are shipping text (`resolution.py:187` and
  `:229`). Three formal records touch them and none ratifies them. Two are stale:
  QST-0062 cites *"this Character"* in Powerful Build and QST-0051 cites *"Giant
  heritage manifested as…"*, and neither string is in `resolution.py` any more, so
  both Questae sit Open against text that has already been repaired. The third
  still bites. QST-0094's audit files the Goliath with the Gnome and the Aasimar
  as "authored prose paragraph, then the rule; no italic marker", explicitly *a
  second convention*, and names Elf, Halfling, Human and Orc as the pattern. The
  Goliath's lines cannot be cited as the reference while the only Questa that
  surveyed them records them as the exception. Needs QST-0094 to close, or a
  sidequest of it promoting this convention.
- **Their world fell.** The empire split, interbred and ran itself into oblivion,
  so the legends are aftermath. Zero formal hits in either sense. Needs a lore
  Questa that also says what the fall changes mechanically: which legend markers
  the Goliath may hold, and whether ruin vocabulary enters `_LEGEND_NOUNS`
  (`Map_of_Gear_Titles.py:733`).
- **⚠️ Early Arthur belongs to the Giants as a decline myth.** Recorded as decided
  on the canon page, whose stratum table gives early Arthur (`arthuriana`) to the
  Goliath and late Arthur (`crusader`) to the Aasimar. Two problems. In the Questa
  and Agora trees "arthur" occurs exactly once, as `arthuriana` inside
  QST-0046.4's list of `_INFLUENCES` to rewire; "crusader" and "decline myth"
  occur nowhere; "grail" occurs once and is not a lore assignment, it is the gear
  title *Grail-Knight's Greatsword* in QST-0046.5. And the canon page contradicts
  itself: its legend-register table still lists `arthuriana` under Human, Aasimar
  and Paladin, with no Goliath, while the stratum table above it hands early
  Arthur to the Goliath. Needs a Questa splitting `arthuriana` into early and late
  strata, fixing the register row, asserting the deliberate Grail Knight overlap,
  and self-testing that the two peoples do not both lead on the same Arthurian
  pool.
- **Dragon against giant in the myth layer.** No Questa opposes the two peoples;
  QST-0046.4 settled only the register split between `homeric` and `wyrm_myth`.
  Needs a Questa declaring the opposition and deciding what it licenses (title
  pools, kinship Tags).
- **⚠️ Who holds `wyrm_myth` is not merely open, it is contradicted.** The one
  formal statement of ownership is QST-0046.4, which says as a premise that
  "Goliaths already hold `wyrm_myth`" and whose Resolution leaves it holding the
  monstrous register while `homeric` takes the titans and giants. The canon page
  disagrees with the Questa and with itself: its register table lists three
  holders (Dragonborn, Kobold, Goliath), and the open section directly beneath
  says the register "is currently held by **Dragonborn and Kobolds**" and offers
  three unapplied ways out, one of which is giving it back to the Goliaths. Needs
  a sidequest of QST-0046.4 to name the holder (dragons, Goliaths, both, or a
  Guild rather than a species, which that page's own third rule already allows).
  Until it lands, three documents give three answers.
- **⚠️ The species entry speaks as "we".** Logged as decided. QST-0094 (Working)
  classes the Goliath among the species that address the reader as "you" and calls
  the convention a taste call still open, and the entry does both in three
  paragraphs ("Giants are your ancestors", then "we tend the world"). QST-0094
  must close on its open question 2 before the voice can be recorded as settled.
- **The species entry may name classes.** It closes on three questions that are
  three subclasses (the Land Circle, the Storm Barbarian, the Stars Circle), and
  it is the only entry that invites the class. Nothing formal covers it, including
  QST-0094, which governs description voice. Needs a sidequest of QST-0094 before
  the close becomes the pattern for the other nine.
- **The comparative beyond the register row.** Authority resting on deed against
  consecration, "does it and reasons after", and the two failure modes. Only the
  culture halves and the philosophical-against-practical pair are ratified; the
  other rows appear nowhere. Needs a Questa extending the QST-0046.4 correction to
  the full table.
- **The Palatine, the class assignments and the background pairings.**
  *Palatinus* as the Palatine guard of a fallen empire, the Barbarian as the
  species' home, the Rogue as Odysseus, the krypteia as the Gloom Stalker's
  shadow, Tyrtaeus as the Valor Bard, Vitruvius as the Wizard and the Artificer.
  "Goliath" occurs zero times in every Dialog and Consul file in both Agora trees,
  and Decree 0005 steers affinity from Guild, Specialization, casting ability and
  level, never from species. Two of the six names are not quite absent, and the
  difference changes the work. Tyrtaeus is already the Valor Bard's named ancestor
  in the legacy copy of Dialog 0015, which calls him the cleaner ancestor for the
  college and reads him through Sparta, while the converged Documenta copy of the
  same Dialog dropped him; so that pairing needs reinstating, not inventing.
  "Vitruvius" occurs once, as the etymology of `AtlasVenustas` in QST-0021, not as
  a class pairing. "Palatine" and "krypteia" return nothing anywhere. Needs a
  Questa deciding whether species and class affinity is recorded design at all,
  plus the Paladin core-fantasy Dialog, which does not yet exist (the Dialogs run
  Artificer, Barbarian, Bard, Cleric, Druid, Monk).
- **The war for the heavens.** The Trojans as the Titans, the Trojan War as
  Celestials against Titans, the Odyssey as the Goliaths', and Rhodes standing
  with the Giants. "Trojan" and "Rhodes" return nothing in either tree; "Odyssey"
  returns one hit, in the Druid Dialog 0017, about the sea and not about the
  Goliath. Needs a lore Questa ruling it deep lore, never a proper noun on a
  sheet, and deciding whether Rhodes becomes a sixth classical marker or stays
  inside `homeric`.
- **⚠️ The name pool, which is not what the work list said it was.** A Goliath
  carries the `Giant` kinship Tag (`kinship.py:62`), so names come from
  `AtlasNomina/Races/Giant.py` by way of the race map (`Map_of_Names.py:518`).
  Three things are true of that file, and only the last resembles the note this
  page used to carry. First, the pool is *already* Roman, Arthurian and titanic:
  Aurelius, Ambrosius, Agrippa, Aquila, Antonia and Augustu sit beside Arthur,
  Artorius, Uther, Merlinus, Lancelot, Gawain, Guinivere, Mordred, Percival,
  Bedivere and Tristan, and the titans (Cronus, Coeus, Crius, Iapetus, Hiperion,
  Themis, Thea, Tethis, Atlas) carry the `homeric` register. So `rome` and
  `homeric` are there in substance and `arthuriana` is there in force, which is
  the strongest code evidence the Arthur decision above has. What is missing is
  `sparta`: not one Spartan name in 942 lines. Second, `Surnames` returns `Names`
  unchanged (`Giant.py:893`), so the family name is drawn from the same pool of
  given names. Third, `Map_of_Names.py:591` appends a literal `son` to that
  surname for every Giant-kin character, which is where the Norse patronymic comes
  from: not from the pool, and not from the phoneme map, which is labelled "Old
  English + French" (`Linguistics.py:108`). Needs a Questa adding Spartan names,
  giving surnames a source of their own, ruling on the hardcoded patronymic, and
  asserting that no species draws another's culture-marked names, which is the
  leak QST-0046.5 already warns about.
- **The orphaned prayer.** *"We learn by suffering"* sits under the retired
  `greece` key, at `Map_of_Cleric_Prayers.py:294`, under the key
  `("greece", "War")`. The premise is backed and the retirement is enforced on
  one side only: QST-0046.4 retired the marker, and `Map_of_Gear_Titles.py:2057`
  and `:2058` now assert that `greece` appears in neither `_CULTURAL_NOUNS` nor
  `_INFLUENCES`, while the prayer ledger still keys on it. The repair is
  scheduled nowhere. Needs a sidequest of QST-0046.4 sweeping every consumer of
  the two dead markers, the Cleric prayer ledger included, so no authored line is
  left addressed to a key that no longer exists.

### What the rules force, and what we chose

Giant Ancestry is the demanding one. It forces a body that carries one boon out of
six, chosen at creation, and it forces that boon to be *supernatural*: a teleport,
a burning, a cold that slows, a Reaction that shrugs off a blow. And it refuses to
be a lineage. The Goliath declaration passes no `heritages=`, so `Goliath.HERITAGES`
is the empty tuple and `Heritages_By_Species()` skips the species entirely; the
self-test then asserts that `Goliath.GIANT_HERITAGES` is the six and that not one
of their display names appears in `HERITAGE_CHOICES` (`__main__.py:627`). That
matches the 2024 book, where the Goliath has no subrace. So the six are not six
kinds of Goliath. They are one thing every Goliath has, in six values.

Our answer is that **the favour is a gift from a relative who is also a
landscape**. The Giants are the world rather than its rulers; some of them made
something smaller and gave it life and many favours; each Goliath carries one and
knows which Giant it came from the way other people know a surname. Powerful Build
and Large Form then read as one claim in two features: *made smaller than your
ancestors, never lighter*, and *for a few minutes you are the size your ancestors
never stopped being*.

**What that buys beyond the rule.** The one-of-six stops being a menu and becomes
descent, so its permanence needs no defending: nobody asks why you cannot swap a
surname. The seeded draw becomes a fact about the character rather than a build
decision taken by a dice bag. Powerful Build, which is otherwise a carrying
capacity footnote, gets a physiology: a Medium creature that hauls like a Large one
was scaled down, not lightened. Large Form inverts from a growth buff into a
reversion, which is why it can be a Bonus Action and cost nothing to end: the
ancestral size is the default and the Goliath is the diminished one, permitted ten
minutes at the right size. And because the boon and the duty come from the same
relative, the entry's own metaphysic (*"our strength is not our might, but our
duty"*) rests on the one trait every Goliath carries, instead of floating above the
rules as sentiment.

⚠️ **What breaks if a later hand cuts the ancestors as flavour.** Giant Ancestry
becomes six damage riders with no reason to be permanent, and the first player who
wants to swap one has no answer. Powerful Build's two clauses stop having anything
in common. Large Form is a growth spell, and both of its trait lines stop meaning
anything, because both are about ancestors. The duty loses the mechanic it rests
on, and the Order of Things is left as prose with nothing under it. The avalanche
reading goes, and with it the prayer *"each snowflake is small, but it is part of
the avalanche"*, which is that reading in four words. That this whole argument is
unratified is a reason to write the Questa, not a licence to treat the ancestors as
decoration.

### The variable detail

Drawn per character, and none of it ratified: which of the six favours the Goliath
carries, from the seeded bag `identity.species.Goliath.giant_heritage`, drawn once
unless one was already applied (`resolution.py:46`); and the name.

The favour was not filled in at random. The six are the six Giant kinds of the
published rules, and `ANCESTRY_LINES` gives each one a sentence about the ancestor
rather than about the Goliath's temperament: stone "does not move aside for you
either", the storm "answers weather with weather", the cold "arrives the way cold
does, without announcing itself". So the draw names a relative rather than picking
a damage type, which is the whole of the interpretation above working at the one
point where the generator makes a choice.

The names are the exception, and the honest one. The pool is right about two of the
three ratified keys and silent on the third, its surnames are its given names over
again, and a hardcoded patronymic sits on top of all of it. It is on the work list
above, and it is a larger repair than a vocabulary top-up.

---

## 📚 1. Where the Goliath lives in the code

| What | Where | State |
|---|---|---|
| Species entry | `AtlasActorLudi/SpeciesKit/Goliaths/__init__.py` | Shipping. First person plural ("we tend the world"). Closes on three questions that are three classes (§7). Speed 35. |
| Giant heritages | `Goliaths/Giant_Heritages/` (Cloud's Jaunt, Fire's Burn, Frost's Chill, Hill's Tumble, Stone's Endurance, Storm's Thunder) | Each carries a line: *"The favour you carry came down from a Storm Giant, and it answers weather with weather."* |
| Traits and rules | `Goliaths/resolution.py`, `traits.py` | Powerful Build: *"You were made smaller than your ancestors, never lighter."* Large Form: *"For a few minutes you are the size your ancestors never stopped being."* Dice notation settled here (`_signed_die`). |
| Names | `AtlasNomina/Races/Giant.py` | "Giants (meaning)"; Wairimu, Ōga; an Oni subtype. Thin header. |
| Culture keys | `rome`, `sparta`, `homeric`; legend `arthuriana` (early Arthur) | Noric steel, hoplite bronze, heroic bronze and Mycenaean gold, lake-tempered steel in the Materials map. |
| Prayer | `Map_of_Cleric_Prayers.py` | *The winds are fast, but they do not hurry.* *Each snowflake is small, but it is part of the avalanche.* War: *Stand your ground. Understand your enemy.* Light: *The darkest night holds the brightest stars.* |
| Canon | `Cultural-Inspirations.md` §Celestials and Giants; §Why Arthur belongs to the Giants | The crossed comparative; the decline myth; dragon versus giant. |

---

## 📜 2. Origin: the First Ones

*"Giants manifested before the first things. And Giants are your ancestors.
Before anyone had a word for Winter, she had a name and a temper. Your
ancestors did not command the avalanche. They were the avalanche, and the
mountain, and the thunder. The gods took the heavens and the songs. The First
Ones kept the world, having never stopped being it."*

**The Giants are the world**, not its rulers. Some of them "turned and made
something much smaller, and gave it life, and many favors": each Goliath
carries one favour and knows which Giant it came from the way other people
know a surname. The heritage is a *gift* from a relative who is also a
landscape.

**The Order of Things.** *"We are part of this world, part of The Order of
Things, from the breathing sky to the living earth."* The Goliath's duty is to
tend the world and everything the Giants made, "with respect and awe". The
metaphysic in one line, from the entry: *"our strength is not our might, but
our duty."*

**Six favours**, drawn once and kept:

| Giant | Favour | The line's image |
|---|---|---|
| Cloud | Jaunt: a 30-foot teleport | "it was…" (a step through the sky) |
| Fire | Burn: extra Fire damage on a hit | "it has not…" (gone out) |
| Frost | Chill: Cold damage and slowed Speed | "it arrives the way cold does, without announcing itself" |
| Hill | Tumble: knock a target Prone | "what it puts…" (down, stays down) |
| Stone | Endurance: a Reaction that reduces damage | "stone does…" (not hurry) |
| Storm | Thunder: a Reaction that answers damage with Thunder | "it answers weather with weather" |

**Large Form** at 5: for a few minutes the Goliath is "the size your ancestors
never stopped being." **Powerful Build**: "made smaller than your ancestors,
never lighter."

---

## 📔 3. The comparative: Greek in myth, Roman in method

The Celestials and the Giants are the only peoples who hold Greece and Rome as
*identity*; everyone else inherits them faintly. They do not divide the
classical world: they each take half of each, and the halves are opposites.

| | **Goliath** | **Aasimar** |
|---|---|---|
| Greek half | **Sparta and the Iliad**: the agoge, the phalanx, the single combat, the giants and titans | Athens: the academy, the argument |
| Roman half | **Legionary Rome**: the road, the aqueduct, the siege engine, the drill | Vatican Rome: the see, the canon |
| Temper | Naturalist, physical, practical | Pensive, philosophical, contemplative |
| Meets a problem by | Doing it, and reasoning after | Reasoning it through first |
| Authority rests on | Deed and physical proof | Consecration and argument |
| Failure mode | Solves the wrong problem, thoroughly | Deliberates while the thing burns |
| What happened to their world | **It fell.** The empire split, interbred, ran itself into oblivion | It endured |
| So their legends are | **Aftermath**: the ruin, the warlord, the caste that outlived its reason | Continuity |

Neither is the civilised one and neither the brute: two ways of being serious.

**Homer earns his own key.** A hoplite in formation is not Achilles. `sparta`
is the agoge and the phalanx; `homeric` is the Iliad, the heroic age, the
titans and giants the Goliaths descend from. The Giants' own war is Homeric
before it is anything else.

---

## 📚 4. History: the greater they fall

**Arthur belongs to the Giants.** Early Arthur (`arthuriana`) is what the
legion becomes once the legion has gone: a washed and half-remembered story of
a decaying garrison, sprouting a warlord who carves the people into a caste of
knights above everyone else. Not a founding myth: a **decline myth**, and the
Goliaths are the fallen civilisation. A Goliath carries the grandeur of Rome and
the wreckage of it in the same hand. Late Arthur, the Grail and the sanctified
knight, went to the Celestials as `crusader`; the two strata overlap on the
Grail Knight, and that is deliberate.

**The Arthurian epoch is thick with giants.** The beanstalk, the seven-league
boots taken from an ogre, the knights who went out to kill dragons: giant
stories before they are knight stories.

**Dragon versus giant.** The Dragonborn and the Goliaths are set against each
other in the myth layer, not merely different. The dragon-slaying knight is a
Goliath story about a Dragonborn. The `wyrm_myth` register (Dragonslayer,
Wyrmbane, Serpent's Bane) is currently held by the dragons; the brief leaves
open whether it comes to the Goliaths, and the Ranger page offers a fourth
option (the Ranger holds it by Guild). A Goliath with dragon magic is the
myth's defector.

**The war for the heavens** (the author, Aasimar page). *"The gods took the heavens
and the songs. The First Ones kept the world."* Read the Trojan War as
Celestials against Titans: the Trojans are the Titans, the Iliad's gods
striking on the field are the Celestials' register, and the Odyssey (the long
way home from a war that is over) is the Goliaths'. Rhodes stands with the
Giants: another Greek culture for a people whose Greece is Sparta and Homer,
not Athens. Two peoples, one war, two camps. Deep lore, never a proper noun on
a sheet.

**The Palatine.** *Palatinus*, the Paladin's name, is the Palatine guard, and
Rome is the Goliaths' key. The imperial guard whose empire fell: the oath that
outlived its reason, in the class's own name (Paladin page). The Goliath
Paladin is the roster's most native pairing after the Goliath Barbarian.

---

## 📜 5. Culture and registers

**Sparta**: the agoge (the Fighter's training, the Champion's laurel), the
phalanx that marched to a flute (Tyrtaeus: the Goliath Valor Bard), the krypteia
(the Gloom Stalker's shadow, which the Goliaths do not talk about), *"We learn
by suffering"* (Aeschylus; orphaned in the prayer ledger under the dead
`greece` key and belongs here), *"Come back with your shield or on it"*.

**Homer**: the *aristeia* (a god breathes *menos* into the hero: the Goliath
Zealot is Diomedes in book five), the funeral games for Patroclus (the
Champion's laurel comes from a funeral), Atalanta and the Calydonian boar (the
Goliath Hunter), Hephaestus's tripods that walk (the Goliath Battle Smith),
Odysseus *polytropos* (the Goliath Rogue, inverting the size joke),
*"Always to be best and to excel above others"* (Iliad 6.208).

**Rome**: the palus (Vegetius' training post: the Fighter class text is
literally the Roman drill), Vitruvius and the aqueduct (the Goliath Wizard and
Artificer as the legion's engineers; Force Ballista is a Roman engine by
name), the road and the siege, *"While I breathe, I hope"* and *"Make haste
slowly"* in the prayers.

**Arthuriana**: Kingsword, Sword in the Stone, Oathblade, Questing Lance,
Blazoned Shield, White Harness. The aftermath knight's kit.

**Materials**: Noric steel, tinned bronze, legion-stamped iron; hoplite bronze,
olive wood, laconian iron; heroic bronze, boar-tusk, Mycenaean gold;
lake-tempered steel, chapel silver.

**Names**: the file is thin (Wairimu, Ōga, an Oni subtype: the Japanese ogre
as a Giant kind). ⚠️ The name pool does not yet carry the three keys; Spartan,
Homeric and Roman names (Leonidas, Ajax, Marcus) would put the comparative in
the first word a player reads. The generator's Goliaths (Bergoracan
Anarsiasson, Liernar Fonelarison, Bergalenon Drustson) read Norse by
patronymic, which is the Elves' key.

---

## 📜 6. Metaphysics: duty, not might

**The Goliath entry asks three classes' questions.** *"Do you respect and
protect the land? Do you rage with the storm? Or do you observe the cycles of
the night sky?"* The Land Circle, the Storm Giant's Barbarian, the Stars
Circle. It is the only species entry that invites the class, and the model for
how the others could close (Barbarian page). The Order of Things is the
Druid's covenant, and for a Goliath the elder society the Druid never left is
literally the family.

**Doing it, and reasoning after.** The Fighter's class text ("There is no
secret. That is the secret.") is the Goliath temper. The Barbarian's ("You
lose hesitation") too. The one Goliath who reasons first is the interesting
one: the Goliath Wizard, the Goliath Rogue.

**The fallen empire and the Dwarves' fallen mountain.** Two peoples with a
lost greatness they remember; the Dwarves carry ledgers and grudges, the
Goliaths carry duty and awe. The Dwarf wants the Crown back; the Goliath tends
the ruin. The Tiefling has a lost greatness nobody remembers at all.

**Against the Celestials.** The Goliath's authority is deed; the Aasimar's is
argument. A Goliath and an Aasimar in a party are the comparative table at a
campfire, and the Trojan War is their shared ancestor story told from opposite
camps.

**The avalanche and Rage.** *"They were the avalanche."* The Barbarian is the
Goliath's home class; the Storm Giant's Thunder answers damage with Thunder,
which is Retaliation as a species trait. *"Each snowflake is small, but it is
part of the avalanche"* is the World Tree's "you are very small, you are part
of it" in the Goliath's mouth.

---

## 📔 7. The classes: the favour in each

| Class | The Goliath in it |
|---|---|
| **Barbarian** | The species' home. "Do you rage with the storm?" A Homeric Goliath Zealot is the aristeia; a Storm Goliath Berserker answers weather with weather. |
| **Fighter** | The palus, the agoge, the laurel from a funeral. The Goliath Champion (seed 81) is native. |
| **Paladin** | The Palatine guard of a palace that is gone; Glory (Achilles' short life and long name); duty as the species' word before the class's. |
| **Druid** | Talking to relatives. The Order of Things is the Land Circle's covenant. |
| **Bard** | Tyrtaeus; the phalanx marched to a flute; "the greater they fall" is the song. |
| **Cleric** | The parent is the landscape: the most literal watcher on the roster. |
| **Wizard / Artificer** | Vitruvius; the legion's engineer; Hephaestus's tripods; the ballista. The one Goliath who reasons first. |
| **Rogue** | Odysseus. |
| **Ranger** | Atalanta; the krypteia as the Gloom Stalker's shadow. |
| **Monk** | The avalanche that learned to be light; a Cloud Goliath Shadow Monk teleports twice. |
| **Sorcerer** | The Storm as Wild Magic; Draconic as the myth's defector. |
| **Warlock** | A pact with an ancestor is a family matter; the Storm Archfey. |

---

## 📔 8. Backgrounds

- **Guardian.** "The wall between the weak and the wolves." Duty as a job; the
  Goliath Guardian is the phalanx's one shield.
- **Soldier, Sellsword.** The legion for hire; the good name is the road you
  built.
- **Ice Nomad.** The Frost Giant's child on the ice roads.
- **Squire.** "You served someone the songs are about." The Goliath Squire
  served a Giant, which is a mountain, which does not need its horses fed.
- **Herald.** The Goliath Herald walks in past the guards because nobody stops
  someone that size; "harming a herald is how small quarrels become wars" is a
  smaller quarrel than it sounds.
- **Stranger.** The emigrant from a fallen empire whose grandeur and wreckage
  are in the same hand.
- **Archaeologist.** The ruin as a career: the Goliath Archaeologist reads
  their own people's roads.
- **Naturalist, Wildkeeper.** The Order of Things as a field diary.
- **Survivalist.** Stone's Endurance as a background.
- **Destined.** Comic: the giant-blooded chosen one who "can walk further than
  anyone else in the party" and is right.

---

## 📜 9. Decisions log

**Decided**

- The crossed comparative (Greek in myth, Roman in method); the five atomic
  keys (QST-0046.4); early Arthur to the Giants, late Arthur to the Celestials
  (`a1f1837`, `ac9f3ce`).
- The species entry speaks as "we".

**Open**

- **`wyrm_myth`**: the brief's three options, and the Ranger page's fourth.
- **The name pool** does not carry the three keys (§5).
- **The Trojans as Titans**: a war of Celestials and Titans for the
  heavens, the Odyssey as the Goliaths', Rhodes with the Giants. Worth a
  paragraph in `Cultural-Inspirations.md` beside the comparative, as deep lore.
- **Darkvision**: the Goliath has none; nothing to decide.

**Repairs**

- Move *"We learn by suffering"* from the dead `greece` key to `sparta` or
  `homeric` in the prayer ledger (Cleric page §5).

---

## 📖 10. Lines

*The Goliath's trait lines exist and are among the best on the roster ("made
smaller than your ancestors, never lighter"). Listed as the reference; the
heritage lines are the house pattern for a drawn ancestry. No additions
proposed.*

| Entry | Line (shipping) |
|---|---|
| **Giant Ancestry** | *The favour you carry came down from a [Cloud / Fire / Frost / Hill / Stone / Storm] Giant, and…* (six variants; the Storm's: *it answers weather with weather*; the Frost's: *it arrives the way cold does, without announcing itself*) |
| **Powerful Build** | *You were made smaller than your ancestors, never lighter.* |
| **Large Form** | *For a few minutes you are the size your ancestors never stopped being.* |

---

## 📚 11. Pointers

- **Celestials page**: the comparative; the war for the heavens.
- **Paladin page**: the Palatine.
- **Fighter page**: the palus, the laurel.
- **Dragonborn page**: dragon versus giant; the slayer's words.
- **Dwarf page**: two fallen greatnesses.
- **Cultural Inspirations**: the Trojan reading; the name pool.
