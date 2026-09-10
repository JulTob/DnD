# 🐎 Orc

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
Compiled 2026-09-08 from the Orc kit, the species entry, `AtlasNomina/Races/Orc.py`,
the peoples table in the Dragon and Elf canon, the class analyses and the design
notes.*

> **In one sentence.** The children of the horizon: the people who were on the
> plains first, were never asked, and are called raiders for riding the roads
> that were theirs. Every soul walks a wind path, and if they fall, they carry on.

---

## 📜 0. Rules

*The fixed points, and what we made of them. The books are defined at the head
of the page.*

### The rules as given

*Each entry is the rule itself, complete enough to resolve at a table. Not a
summary and not a cross-reference.*

> 📕 **Creature Type** Humanoid. **Size** Medium. **Speed** 30 feet.
>
> 📕 **Adrenaline Rush.** You can take the Dash action as a Bonus Action. When
> you do so, you gain a number of Temporary Hit Points equal to your Proficiency
> Bonus. You can use this trait a number of times equal to your Proficiency
> Bonus, and you regain all expended uses when you finish a Short Rest or a Long
> Rest. Both quantities are the same number: 2 at levels 1 to 4, 3 at 5 to 8, 4
> at 9 to 12, 5 at 13 to 16, 6 at 17 to 20.
> > 📘 _The winds of your storm are hard to catch, rider. Run, be free, and run._
>
> 📕 **Darkvision.** You can see in Dim Light within 120 feet as if it were
> Bright Light. In Darkness within that range you can see as if it were Dim
> Light: you have Disadvantage on Wisdom (Perception) checks that rely on sight
> there, and you discern colors in that Darkness only as shades of gray.
> > 📘 _The ride does not end at nightfall, and neither does your watch._ (proposed)
>
> 📕 **Relentless Endurance.** When you are reduced to 0 Hit Points but not
> killed outright, you can drop to 1 Hit Point instead. Once you use this trait,
> you can't use it again until you finish a Long Rest. One use, and a Short Rest
> does not restore it.
> > 📘 _Do not fall, rider! Be strong! Carry on!_

No rule of the Orc has been changed, so this page carries no 📒, and no trait
wears a house name, so it carries no 📙 either. Two further absences are worth
stating, because both are correct rather than missing. The Orc has no lineage,
heritage or ancestry choice: `Orcs/__init__.py` passes no `heritages=`, and
`Heritages_By_Species` skips any species whose `HERITAGES` is empty, so the Orc
never reaches `HERITAGES_BY_SPECIES`. And the species grants no language, which
is the 2024 arrangement: languages come with the background rather than with the
people.

Four implementation facts sit under those entries.

**The size is never rolled.** `size_options=("Medium",)` is a single option, and
`_selected_size` in `physiology.py` takes the one option directly instead of
opening a Dice Bag. Only a species declaring two or more options rolls for it.

**The 120 feet is a floor, not a value.** It is the Orc's own published range,
twice the 60 that `SpeciesKit/traits.py` holds as the standard, and
`Set_Orc_Range` writes it as `max(current, 120)`, so a wider darkvision from
another source is never reduced to it.

**The Disadvantage clause is printed on purpose.** It is not in the 2024
glossary's Darkvision entry. It follows from Darkness-seen-as-Dim-Light being
Lightly Obscured, and the shared `Darkvision_Rules` helper prints it because a
player reading the sheet would otherwise assume darkvision cancels the penalty.
Both scope clauses ("within that range", "in that Darkness") are load-bearing
and an earlier wording lost both, which promised unlimited darkvision in true
Darkness and claimed the Orc could not tell red from blue at noon. It is a
consequence written out rather than a rule changed, so it takes no 📒.

**Adrenaline Rush prints the number and drops the formula.** The projected entry
resolves the Proficiency Bonus, so at level 1 it reads "you gain 2 Temporary Hit
Points. You can do this 2 times", with two chips ("Adrenaline Rush Uses", "Rush
Temporary HP"). Darkvision carries one chip reading "120 ft" and Relentless
Endurance one reading "1 / Long Rest". The scaling itself survives on the Tag as
`adrenaline_rush_use_scaling`, so the record loses nothing, but it leaves the
printed entry, and `Feature-Text.md` asks for the other form.

### The supportive lore

> 📘 **One culture key is one culture. A species holds a list of keys, never a
> blend.** Fused keys were rejected by name, markers are atomic, and a people
> that sits between traditions holds both markers rather than an invented middle
> one. Culture-marked words are reachable only through the key that owns them,
> the generic pools are deliberately culture-neutral, and overlap between
> peoples is modelled by weighted influence rather than by sharing a key.
> Ratified by **QST-0046.2** and **QST-0046.5**.

> 📘 **`mongol` belongs to the Elf.** It sits on the Elf row of the culture
> table with `norse`, `rus` and `celt`, and on no other species row. The
> influence mechanism, not a second owner, is how a people reaches a neighbour's
> well.
> Ratified by **QST-0046.2**.

> 📘 **Cultural materials ride the same species row as the gear titles.**
> `Map_of_Materials._CULTURAL_MATERIALS` is keyed by the same markers as
> `Map_of_Gear_Titles._CULTURES`, so one row decides both a people's names and
> its substances, and correcting a species corrects both at once. A species with
> no row therefore loses both in one stroke.
> Ratified by **QST-0046.6**.

> 📘 **The metaphysics table holds one organising principle per people, and a
> species may not be metaphysically silent.** A species either takes an existing
> principle or brings its own. The requirement is formal; which row the Orc
> holds is not, because the questa names no row.
> Ratified by **QST-0053**.

> 📘 **The three trait entries are written in the house pattern**: an italic
> inspiration line in the project's voice, a blank line, then the rule in the
> 2024 rulebook's present tense. The Orc is one of the four kits that exemplify
> it, rewritten out of the earlier "Gained at Level 1. X granted Y" voice, and
> the agent-prefixed phrasing for Adrenaline Rush was rejected as bloat.
> Ratified by **QST-0094** and **QST-0062**.

> 📘 **A sheet prints the number the sheet already knows; a chip is a lookup and
> the prose is the entry.** Feature text is compared against the Feature-Text
> standards before it lands: explicit breaks, dice notation, resolved numbers,
> no open-choice language. That is what licenses Adrenaline Rush printing 2
> instead of "your Proficiency Bonus", and the chips beside the three entries.
> Ratified by **Decree 0007**.

> 📘 **The reading stays class- and alignment-agnostic.** For prose a player
> reads, premise may be stated and personality may not be prescribed. This is
> what holds the Rogue caveat in §7: the raider reading is available and must
> never be the default.
> Ratified by **Decree 0007**.

That is the whole of the supportive lore this page can currently mark, and none
of it is about the Orc in particular: four are laws the page invokes and three
are conventions it obeys. Everything below rests on the canon documents, on the
species entry itself and on this page's own decisions log, which are not the
Questa / Agora / Decree system, so it carries no book until a Questa says
otherwise.

### Unratified, and what each one needs

*Stated as design, not as law. Each line names the Questa that would ratify it.*

- **The wind path as the metaphysic.** A route each soul walks rather than a
  substance it is made of, and the only route among the five peoples the table
  names. It rests on one line of that table in `Dragons-and-the-Overcoming.md`
  and on the entry's own prose. QST-0053 binds the table but names no row.
  Needs a Questa ratifying the metaphysics table row by row, and the same
  Questa would say what the five other peoples hold.
- **The Orc's culture keys.** None assigned. The code genuinely has no Orc row
  in `_CULTURES`, and neither QST-0046.2's species table nor the canon brief in
  `Cultural-Inspirations.md` mentions the Orc at all, so the omission is in both
  places and no Questa raises it. Needs an Orc row as a sibling of QST-0046.4,
  deciding the keys or ruling the Orc deliberately unkeyed.
- **Cultural materials: none of the Orc's own.** Horn, sinew and felt-bound iron
  sit under `mongol`. The Orc does hold a trade-theme materials row of its own
  ("hide-bound iron", "scarred oak", "rough-forged steel"), so this is a missing
  culture axis and not a missing people. By QST-0046.6 the culture-key Questa
  above decides it in the same stroke, so it needs no Questa of its own.
- **The name file's fused inspirations.** `AtlasNomina/Races/Orc.py` heads its
  list with eight: Britain, `Skales`, the Celts, the Vikings (`Bikings`), cowboy
  America, Native Americans, pre-Columbian American languages, and the Boyz of
  40k. The header is written in the file's own orthography, which is why two of
  the eight read as misspellings. The law against fusion is ratified; its
  application to this file is decided nowhere and the file is untouched. Needs a
  Questa choosing between splitting the eight into keys and cutting the header.
- **The phonetic rule as a design that survives any key.** The file states it as
  *"Big Fangs: 'S' wuld bite the tonke, 'z' inztead"*, with the substitutions
  under it. Nothing in the formal system mentions it. Needs the same name-file
  Questa, ratifying the rule as kept before deciding what happens to the header
  around it.
- **The steppe by temper.** The horse, the eagle, the long ride, the standard
  that is not a flag, the epic without a book, and the class pages' readings
  (the berkutchi's golden eagle, the *nerge* ring-hunt, the manaschi's
  half-million lines, the yak-tail tug, the morin khuur). The word "Orc" does
  not appear once in the Agora's Dialogs, and the only occurrence of "steppe" in
  the Questae is inside `norse_steppe_celtic`, the fused key that was rejected.
  Needs a Questa deciding whether these are the Orc's canon or wells a DM may
  reach for, which the culture-key Questa settles either way.
- **The history: nobody asked.** The plains first, the dwarves for the gold
  underneath, the humans to call it discovery, the elves with trade and curses.
  It rests on the species entry and the three other canon pages. Needs a
  species-lore Questa ratifying the origin account and its cross-reads as canon
  rather than as shipped prose.
- **The exonym carried, not reclaimed.** "You are called raiders instead of
  riders" is the species' wound, and unlike the Barbarian's it is not taken
  back. Needs the same species-lore Questa, stating this plainly so later text
  cannot quietly reclaim it.
- **The four storm prayers, and their disagreement.** Two of the four
  contradict each other on purpose (does the rider master the storm or follow
  it), which is the Zealot against the Berserker. No Questa records the lines or
  the design. Needs a Questa ratifying the species prayer pools, which would
  also settle whether a people with no culture key should be short a whole
  source in the ledger.
- **The rule about parallels.** The Tiefling canon forbids naming a parallel or
  writing a line traceable to one real group. Death of the Author, which both
  **Decree 0006** and **Decree 0007** carry, decides lore-dumping rather than
  traceability, and no decree extends the Tiefling rule to another people. Needs
  a Questa promoting it to a project-wide decree, with the Orc named.
- **The species entry's voice.** The file is second person throughout except for
  one first person plural clause and the sentence after it ("we orcs carry our
  own through the storm. If we fall, we carry on"), and QST-0094 files the Orc
  among the seven kits that address the reader as "you" while leaving the
  convention open. The decisions log's "the entry speaks as 'we'" therefore
  states more than the Questa does. Needs the Questa that settles QST-0094's
  open convention, one description voice for all ten peoples or two by design.
- **The class table and the backgrounds list.** The Ranger reading, the Sea
  Druid as the happiest pairing, the pact as the first consent, the Wizard as
  the first rider to write the epic down, the Steel Defender as the first horse
  an Orc never had to bury, and the whole of §8. All of it rests on the canon
  class pages and this page. Needs a Questa ratifying the readings as design
  record, or filing them as DM-facing suggestion with no claim on canon.
- **The Repairs line.** "None found in the Orc's own text" is true of the three
  defects QST-0062 names: `Orcs/resolution.py` and `Orcs/traits.py` carry no
  "granted", no "Gained at Level", no "The X carries N" and no "this Character".
  It still reads against the two Questae as filed, because QST-0062 lists the
  Orc among five kits using a clipped agentless notation and QST-0051 lists
  `Orcs/` under the same defect, and neither has been closed for this kit. One
  real gap is left, and it is the fourth implementation fact above:
  `Feature-Text.md` gives the resolved-number form as "4 times (equal to your
  Proficiency Bonus)" and the Gnome kit writes it that way, while Adrenaline
  Rush drops the parenthetical as the Aasimar kit does. Close QST-0062 and
  QST-0051 for the Orc kit and settle which of the two forms is the house one,
  and the line can then read "none" with backing instead of against it.

### What the rules force, and what we chose

The set is the demanding thing, not any one trait. The rules force a body with
no lineage and no choice to make: one size, 30 feet, a Dash it can spend as a
Bonus Action for a small cushion of Temporary Hit Points, sight at twice the
standard darkvision range, and one refusal to fall at 0 Hit Points that comes
back only after a Long Rest. Three traits that no rulebook connects.

Our answer is **the wind path**: a route each soul walks, rather than a
substance it is made of. On the peoples table the Dwarf is a metal, the
Celestial an Ideal, the Elf a dream, the Dragon a self. The Orc is the one whose
organising idea is a road. *"Every soul walks a wind path, and we orcs carry our
own through the storm. If we fall, we carry on."*

**What that buys beyond the rule.** The three traits stop being three numbers
and become one body shaped for the long ride: the burst that gets a rider clear
and gives them something to spend, the watch that does not end at nightfall, and
the refusal to be left behind. Relentless Endurance is not a survival gadget, it
is the entry's last sentence turned into a rule, and prose and mechanic are
tied there as tightly as anywhere on the roster. The route also carries the
quarrel. Nothing in the metaphysic is a possession, so the fencing of the plains
is a wrong done to a people who never claimed to own them, and the entry can
accuse without making a property claim. That is what keeps the history readable
as grievance rather than as title. And because a route can be followed or
mastered, the two storm prayers that disagree are a design, not a slip: the
Berserker carried by the storm against the Zealot who commands it. The Primal
Tradition's practice ("nothing is written; it is walked, and shown, and walked
again") is the same idea in an Order's mouth, which is why an Orc Wizard writing
the epic down is a transgression and not a career change.

⚠️ **What breaks if a later hand takes the wind path for decoration.**
Relentless Endurance loses its only explanation and reads as a free extra life.
The three traits fall apart, and the next hand to touch them has no reason to
keep Darkvision at 120 rather than trim it to the standard 60. The plains
history turns into a land claim, which is the one reading the entry was written
to avoid, and the rule about parallels gets harder to keep. The two storm
prayers stop disagreeing on purpose and look like a drafting accident somebody
should tidy. The Barbarian, Wizard, Druid and Warlock readings all lose their
hinge at once. That the wind path is unratified is an argument for writing the
Questa, not for treating the route as free.

### The variable detail

Drawn per character, and none of it ratified: the name, the gear title and the
material, and, for a Cleric only, the prayer.

**The name.** It is composed from hand-written pools in
`AtlasNomina/Races/Orc.py`: a given-name list, a surname list, and onset, nuclei
and coda syllables. The phonetic rule (Th to z, S to Z, Gue to ke, ou to u, J to
X, h to j, and Va, Ve and Vi to B) is an authoring rule rather than a runtime
transformation, already baked into every syllable in the file. The phonetics are
physiology rather than flavour: big fangs, so an S would bite the tongue and a Z
takes its place, and every substitution follows from a mouth.

**The gear and the material.** Both draw on two axes the Orc holds and one it
does not. It holds `savage` on the title side, with its own nouns
("Skullsplitter", "Bonebreaker", "Boar Spear") and epithets ("the Red Hour",
"the Wild"), and a trade row on the material side ("hide-bound iron", "scarred
oak", "rough-forged steel"). What it has no row for is the culture axis, so its
Longsword takes its noun from the generic pool, which is culture-neutral by
design and not by omission (QST-0046.2), where a Dwarf reaches "Toledo Blade";
and `cultural_materials` returns nothing for it at all, because it reads
`influences_of`, which is built from the culture markers. The gap therefore
shows in the noun rather than in the whole title, which is why it is easy to
miss on a sheet. Where an Orc does reach a culture it comes from a class row and
never from the people: the Barbarian row carries `sword_and_sorcery`, whose
influence reaches `mongol` at weight 1, which is the neighbour mechanism working
exactly as the first book describes it.

**The prayer.** The four storm lines are Cleric lines. `prayer_ledger` assembles
the defaults, the Domain's lines, the species' own and, for a people with keys,
the culture's, and `pick_prayer` draws one from the whole assembly. The Orc has
no species-by-Domain entry and no culture keys, so the four are the only lines
the people contributes, and the missing row costs it a third thing here as well.
The four are two pairs, and one pair disagrees on purpose.

None of it is arbitrary, and none of it carries a book, because no Questa says
so.

---

## 📚 1. Where the Orc lives in the code

| What | Where | State |
|---|---|---|
| Species entry | `AtlasActorLudi/SpeciesKit/Orcs/__init__.py` | Shipping. First person plural. Closes on "why {name} left the Orc Camp, and what would bring them back." |
| Traits and rules | `Orcs/resolution.py`, `traits.py` | House pattern (QST-0094). Adrenaline Rush: *"The winds of your storm are hard to catch, rider. Run, be free, and run."* Darkvision: *"The ride does not end at nightfall, and neither does your watch."* Relentless Endurance: *"Do not fall, rider! Be strong! Carry on!"* |
| Names | `AtlasNomina/Races/Orc.py` | A phonetic rule with a body inside it: "big fangs: S would bite the tongue, Z instead" (Th→z, S→Z, Gue→ke, ou→u, J→X, h→j, V→B). Inspirations listed as a fusion (§5). |
| Culture keys | **none** | ⚠️ The Orc has no row in `_CULTURES`; gear draws from the generic pool only. |
| Prayer | `Map_of_Cleric_Prayers.py` | *The storm is coming.* *The storm guides the winds.* *The wind rider must master the storm.* *The wind rider must follow the storm.* |
| Metaphysic | the peoples table | *The wind path: a route each soul walks rather than a substance it is made of.* |

---

## 📜 2. Origin: the wind path

Each people has one organising idea. The Orc's is the only one that is a
*route* rather than a substance: the Dwarf is a metal, the Celestial an Ideal,
the Elf a dream, the Dragon a self; **the Orc is a path walked.** *"Every soul
walks a wind path, and we orcs carry our own through the storm. If we fall, we
carry on."* Relentless Endurance is the sentence as a rule: reduced to 0 Hit
Points, you drop to 1 instead, once a day.

The path is walked, not owned. The plains "are open to everyone, and riders
must travel." Nothing in the Orc's metaphysic is a possession, which is the
whole quarrel with everyone who fenced the plains.

**Physical traits.** Adrenaline Rush (a Dash as a Bonus Action with Temporary
Hit Points), Darkvision, Relentless Endurance. Endurance, speed, the watch that
does not end at nightfall: a body shaped for the long ride.

---

## 📚 3. History: nobody asked

*"Your people were on the plains first. Then the dwarves came for the gold
underneath, the humans came to call it discovery, and the elves promised trade
and brought curses. No orc was asked."*

Three peoples, three takings, in one sentence, and each is the other people's
entry seen from the plains: the Dwarves' "long terrible expeditions" chasing
metal; the Humans' "there is nowhere humans wouldn't go"; the Elves' "found
commerce". The Orc entry is the setting's one account of what the other
peoples' virtues cost.

*"Now all orcs are riders and no camp is safe. The new peoples fence the plains
and attack when your beasts pass through the old ways. You are called raiders
instead of riders."* The exonym is the species' wound, and unlike the
Barbarian's it is *not* reclaimed: the Orc's answer is to ride further, carry
more, and go without longer than anyone who says it.

**The rule about parallels.** The Orc entry rhymes with real histories of
displacement, and the name file lists real peoples. The Tiefling canon's rule
applies in spirit: never name the parallel on the page. The entry does not, and
must not.

---

## 📔 4. Society: riders

**The camp.** No camp is safe, so the camp moves. The Orc entry's closing
question is "why {name} left the Orc Camp, and what would bring them back": the
camp is the home, and it is the one home on the roster that is always somewhere
else.

**The rider, not the raider.** *"You ride further, carry more and go without
longer than anyone who says it."* Tireless and Roving as a people. The Ranger
page found the Orc entry is already a Ranger's; the Barbarian page found the
two storm prayers disagree on purpose (does the rider master the storm or
follow it?), which is the Zealot against the Berserker in the species' own
mouth.

**The storm.** *"The storm is coming. The storm guides the winds."* The storm
is the Orc's weather, god and road at once, and the species has no Cleric
watcher but this. The Sea Druid Orc (Druid page) found the one plain that
cannot be fenced.

**The steppe by temper, unkeyed.** The Orc reads as the steppe (the horse, the
eagle, the yak-tail tug, the epic recited without a book), but `mongol` is an
Elven key and the Orc has *no key at all* (§5). The temper is in the entry; the
vocabulary is nowhere.

---

## 📜 5. Culture: the missing keys

⚠️ **The Orc has no culture keys.** Every playable people except the Orc and the
Halfling has a row in the gear map; the Orc draws a plain Longsword where a
Dwarf draws Toledo steel. The name file's inspirations are a *fusion* (Britain,
Celts, Vikings, cowboy America, Native Americans, pre-Columbian languages, the
Boyz of 40k), which the brief's law forbids as keys ("one culture key = one
culture; never fuse"), and none of them is assigned.

This is the decision to make, and the page records the directions without
choosing:

- The entry's *temper* is the steppe rider (the horse, the eagle, the long
  ride, the standard that is not a flag, the epic without a book). `mongol` is
  already the Elves'; the brief models overlap by influence, not by sharing.
- The name file's phonetics ("S would bite the tongue") are a design in their
  own right and survive any key.
- The class pages have already read the Orc through the steppe: the berkutchi's
  golden eagle (Beast Master), the *nerge* ring-hunt (Hunter), the manaschi's
  half-million lines (Lore Bard), the yak-tail tug (Banneret), the morin khuur
  (instrument). If the Orc gets a key, those readings land on it; if not, they
  stay as the wells a DM reaches for.

**Prayers**: the four storm lines. **Materials**: none of the Orc's own; horn
and sinew and felt-bound iron sit under `mongol`.

---

## 📜 6. Metaphysics: the storm and the path

**Rage's second cosmology.** *"If we fall, we carry on"* is Relentless Rage in
nine words, and the storm is the Orc's Rage. The rider carried by the storm
(Berserker) and the rider who masters it (Zealot) are the two prayers.

**The pact as the first consent.** *"No orc was asked."* A Warlock's pact is the
one time in the species' history somebody asked (Warlock page).

**The first book.** The Primal practice is "nothing is written; it is walked",
which is the Orc's metaphysic word for word: a *route*. An Orc Wizard is the
first of the riders to write the epic down, and the manaschi will not forgive
them (Wizard page). An Orc Artificer's Steel Defender is the first horse an Orc
never had to bury (Artificer page).

**Against the Dwarves.** The Dwarf came for the gold underneath; the Orc was on
top of it. The two entries are one event from both sides, and a Dwarf and an
Orc in one party carry it.

**The unfenced plain.** The sea signs nothing and cannot be fenced (Druid page):
the Orc Sea Druid is the species' happiest pairing and the dice found it.

---

## 📔 7. The classes: the ride in each

| Class | The Orc in it |
|---|---|
| **Ranger** | The species entry is already a Ranger's. Horde Breaker is the nerge from the horde's side; the golden eagle on the arm. |
| **Barbarian** | Rider carried or rider mastering: the two prayers. Adrenaline Rush is Instinctive Pounce as a species trait. |
| **Paladin** | Vengeance: the species grievance as a vow. Glory: the rider's kleos. The Banneret's tug ("a banner is not always a flag"). |
| **Druid** | The Sea: the one plain that cannot be fenced. The Land Circle's covenant ("what may be taken, what must be left") is the Orc grievance as doctrine. |
| **Bard** | The manaschi: the horde's memory, no book. "No orc was asked" is the epic's first line. |
| **Monk** | "Run, be free, and run" is Step of the Wind with a species name. |
| **Cleric** | The storm is the watcher; the two prayers disagree about whether it carries or commands. |
| **Wizard / Artificer** | The first book; the unburied horse. |
| **Warlock** | The first consent. |
| **Fighter** | The tercio's alférez becomes the tug-bearer; endurance as the drill. |
| **Rogue** | ⚠️ "You are called raiders instead of riders" is the exonym; an Orc Thief or Assassin who decided to earn it is a dangerous story and must not be the default. Keep alignment out. |
| **Sorcerer** | Wild Magic as the storm in one rider. |

---

## 📔 8. Backgrounds

- **Ice Nomad.** *"Your people do not stay; they follow: the herds, the thaw,
  the old roads."* The Orc's background in all but the ice; the two texts
  should be read together, and an Orc Ice Nomad is nearly redundant.
- **Stranger.** "You will be from somewhere else for the rest of your life."
  The Orc whose somewhere else is a camp that moved.
- **Vagabond.** "The road raised you." The ride without the horde.
- **Survivalist.** "Carry nothing you can't carry yourself."
- **Wildkeeper, Naturalist.** The plains as the field; the herds.
- **Sellsword.** The rider for hire, called a raider by the employer.
- **Herald.** The camp's envoy to the peoples who fenced it.
- **Renegade.** "You took a corner of the world and dared them to come get
  it": the fence, reversed.
- **Bailiff.** The law that fenced the plains, served by one of the fenced.
- **Guardian.** "No camp is safe." The one who stands at the camp's edge.
- **Revolutionary.** The Cause is the plains.
- **Squire, Servant.** The rider who served a settled master.

---

## 📜 9. Decisions log

**Decided**

- The species entry speaks as "we"; the three trait lines are the house
  pattern's reference along with the Elf's and the Halfling's (QST-0094).
- The wind path as the metaphysic (peoples table).

**Open**

- **The Orc's culture keys.** None assigned; the name file's list fuses. The
  steppe temper is in the entry.
- **Materials**: none of the Orc's own until a key exists.
- **The name file's inspirations** should be split into distinct keys or
  cut, per the law, whichever the author chooses.

**Repairs**

- None found in the Orc's own text. The Cleric ledger's Orc lines are clean.

---

## 📖 10. Lines

*The three trait lines exist and are the reference. No additions.*

| Entry | Line (shipping) |
|---|---|
| **Adrenaline Rush** | *The winds of your storm are hard to catch, rider. Run, be free, and run.* |
| **Darkvision** | *The ride does not end at nightfall, and neither does your watch.* |
| **Relentless Endurance** | *Do not fall, rider! Be strong! Carry on!* |

---

## 📚 11. Pointers

- **Cultural Inspirations**: the Orc's keys (open).
- **Ranger, Druid, Bard, Barbarian pages**: the steppe readings.
- **Dwarf page**: the gold underneath.
- **Tiefling page**: the rule about parallels.
