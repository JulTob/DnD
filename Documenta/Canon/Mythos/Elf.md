# 🌙 Elf

> 📖 **In flow.** 1 of 12 chapters are still proposals. 📜 6 · 📚 2 · 📔 3 · 📖 1

> - 📕 **inherited from the 2024 rules.** Moving it costs rules compatibility.
> - 📙 **an aesthetic change.** The same rule wearing our name and look.
> - 📒 **a rule we changed.** A house rule, and it already cost compatibility.
> - 📘 **supportive lore.** It holds a rule or a core element up.
> - 📗 **deep lore.** Design that supports the fantasy rather than a rule.
> - A book marks a statement only if it can change exclusively through the
>   Questa / Agora / Decree system. Anything with no Questa and no Decree behind
>   it carries no book, however settled it feels.

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from `Elves-and-the-Dreaming.md`, the Elf kit and its five
lineages, `AtlasNomina/Races/Elf.py`, the old wiki, the class analyses and the design
notes. The Elf canon's first rule governs every line: never explain the Dreaming
on the page.*

> **In one sentence.** Elves came out of the Fae, and the Fae are made of
> dream; something of that stayed in them, so an elf is malleable the way a
> dream is, and a people that lives somewhere long enough, and loves it long
> enough, begins to look like it.

---

## 📜 0. Rules

*The fixed points, and what we made of them. The books are defined at the head
of the page.*

### The rules as given

*Each entry is the rule itself, complete enough to resolve at a table. Not a
summary and not a cross-reference.*

> 📕 **Creature Type** Humanoid. **Size** Medium, the only option, so nothing is
> chosen and nothing is rolled. **Speed** 30 feet, and 35 feet for the Wood Elf
> lineage.
>
> 📒 **Darkvision.** You can see in Dim Light within 60 feet as if it were Bright
> Light. In Darkness within that range you see as if it were Dim Light: you have
> Disadvantage on Wisdom (Perception) checks that rely on sight, and you discern
> colors there only as shades of gray. The Dark Elf and Shadow Elf lineages raise
> the range to 120 feet, and nothing else in the sentence changes; the entry
> prints the resolved number, so a Dark Elf's entry reads 120 feet. Two things in
> that paragraph are ours rather than the rulebook's. The 2024 rule gives 120 feet
> to one lineage, not two. And the Disadvantage clause is not in the published
> Darkvision entry at all: it follows from Darkness-seen-as-Dim-Light being
> Lightly Obscured, and the kit prints it deliberately, scoped to that Darkness,
> because a player reading the sheet would otherwise assume darkvision cancels the
> penalty.
> > 📘 _The dark is only the Dream with the lights off. You have never been afraid of it._ (proposed)
>
> 📕 **Fey Ancestry.** You have Advantage on saving throws you make to avoid or
> end the Charmed condition.
> > 📘 _The echoes of the Fae still linger in you._ (proposed)
>
> 📕 **Keen Senses.** You have proficiency in one skill of your choice from
> Insight, Perception, or Survival. On a generated sheet the choice is already
> made, and the entry names the one skill.
> > 📘 _Your elven eyes are sharp and your attention focused._ (proposed)
>
> 📕 **Trance.** You don't need to sleep, and magic can't put you to sleep. You
> can finish a Long Rest in 4 hours if you spend those hours in a trancelike
> meditation, **during which you retain consciousness**.
> > 📘 _Elves are said to be made of the same essence as dream and nightmare._
>
> 📒 **Elven Lineage.** You belong to one elven lineage, chosen when you make the
> character, from the five below. Intelligence, Wisdom, or Charisma is your
> spellcasting ability for the spells this trait grants. Your Species Spell Save DC
> is **8 + your Proficiency Bonus + that ability's modifier**, and your species
> spell attack bonus is **your Proficiency Bonus + that modifier**. You gain the
> lineage's cantrip at character level 1, its level 1 spell at character level 3,
> and its level 2 spell at character level 5. You always have those level 1 and
> level 2 spells prepared. You can cast each of them once without expending a
> spell slot, regaining that use when you finish a Long Rest, and you can also
> cast them using spell slots. The cantrip is cast at will, like any cantrip.
>
> 📕 **High Elf**: you know Prestidigitation, and whenever you finish a Long Rest
> you can replace it with a different cantrip from the Wizard spell list. At
> character level 3 you gain Detect Magic, and at character level 5, Misty Step.
> > 📘 _Your people traded with more than merchants, and not everything you brought home was cargo._ (proposed)
>
> 📕 **Wood Elf**: your Speed becomes 35 feet. You know Druidcraft. At character
> level 3 you gain Longstrider, and at character level 5, Pass Without Trace.
> > 📘 _The woods have always cared for your people._
>
> 📙 **Dark Elf** [renames **Drow**]: your Darkvision range becomes 120 feet. You
> know Dancing Lights. At character level 3 you gain Faerie Fire, and at character
> level 5, Darkness. Rule for rule the published Drow, under our name.
> > 📘 _The dark taught your people how to survive it, and some of that lesson still answers to you._ (proposed)
>
> 📒 **Fae Elf** [renames **Lorwyn Elf**]: you know Thorn Whip. At character level
> 3 you gain Command, and at character level 5, Silence. Published in another
> book, not as 2024 rules content.
> > 📘 _The crossing into the Feywild left more on you than long ears._ (proposed)
>
> 📒 **Shadow Elf** [renames **Shadowmoor Elf**]: your Darkvision range becomes
> 120 feet. You know Starry Wisp. At character level 3 you gain Heroism, and at
> character level 5, Gentle Repose. Published in another book, not as 2024 rules
> content.
> > 📘 _Telling dream from thought took practice, and the practice stayed._ (proposed)

**Four entries carry a 📒, and three separate changes stand behind them.** First,
the **option list**: the 2024 rules offer three lineages, and this kit offers
five. Dark Elf is the Drow renamed, which costs nothing. Fae Elf and Shadow Elf
are a different book's content, so a table playing from the 2024 rules alone
cannot find them, and the kit pins the whole Elf to the 2024 rules, which cites
those two to a book they are not in. There is no per-Heritage source field to
carry a different citation: the source title, URL and locator are Records on the
Species pin and reach every lineage under it. Second, the **spellcasting
ability**: the published rule makes it a free player choice fixed at selection,
and here a seeded draw picks one when the lineage lands, and the character's own
class casting ability then overwrites it at resolution time whenever that ability
is one of the three. Third, the **Darkvision upgrade scope**: the published rule
gives 120 feet to one lineage, and here two lineages have it. All three are
deliberate, all three cost rules compatibility, and **none of them is declared
anywhere in the formal system**. They are undeclared until a Questa records them,
and the citation fault is fixed by a per-lineage source pin, not by touching the
rules.

**Two notes on what the Elf is not.** The Elf class carries the Kinship tag
`Fey`, which is classification for names, titles, gear vocabulary and familiar
affinity only. It grants no resistance, no sense and no trait, and no spell that
seeks Fey creatures finds an Elf, because the rules question is answered by the
Creature Type, and there the answer is Humanoid. And the Wood Elf's 35 feet and
the Dark and Shadow Elf's 120 feet are never restated inside the lineage entry:
the live number lives in the entry that owns it, which is the project's own
convention and correct as written.

**Four faults in the printing, not in the rules.** The lineage entry lists the
cantrip in the same bullet list as the level 1 and level 2 spells, so the
once-per-rest paragraph beneath it reads as if the cantrip were once per rest;
the ledger is right, it records a free cast only for spells above level 0, and
only the printed text is wrong. A self-test asserts that exact wording, so the
fix has to move the assertion too. The body text names the highest of the three
abilities while the chip and the save DC use the stored one, so a sheet can
contradict itself on one entry. The Trance entry compresses the rule's meditation
clause to "by meditating", dropping both the trancelike meditation and the
retained consciousness. The Fae Elf's cantrip swap is declared in the lineage
file, on a Druid list, and never delivered, which is why the rule above is silent
on it; only the High Elf's swap is printed. In each case the entry above is the
rule.

**And one fault that is neither.** `Drow.py` is not an alias of `Dark_Elf`. It is
a second, complete class holding the same description text, the same three spells
and the same 120 feet, imported by nothing, absent from the lineage tuple, and
therefore unreachable: the name `Drow` cannot be selected, and asking for it by
name raises. The two files are a duplicate, and which one survives is a decision
nobody has taken.

### The supportive lore

> 📘 **Never explain the Dreaming to the player.** The lore is design-team
> material. Player-facing text invites and inspires; it never lectures, and the
> responsibility of making sense belongs to the user's imagination. This is the
> first rule governing every line of this page.
> Ratified by **Decree 0006**.

> 📘 **The house pattern for trait entries is the one the Elf already follows**:
> an italic inspiration line in the project's voice, a blank line, then the rule
> in the 2024 rulebook's present tense. The Elf is one of the four peoples the
> pattern was read off, and the peoples that had lost it are rewritten against
> them.
> Ratified by **QST-0094**.

> 📘 **The Elf's culture keys are `norse`, `rus`, `mongol` and `celt`: far-north
> Europe, the Celts, the Rus and the Mongols.** Four atomic keys held as a list.
> Fused keys were rejected, so the Elf never gets a blend.
> Ratified by **QST-0046.2**.

> 📘 **The Norse register belongs to the Elves and to no other people.** The Old
> Norse gear words were freed for them, and a self-test asserts that Brynja
> reaches an Elf and never a Gnome, so the two do not blur again.
> Ratified by **QST-0046.2**.

> 📘 **Elves and Fae are partners in the culture network.** Culture is a network
> of influences, and the Elf/Fae pairing is one of its declared edges. This is a
> neighbourhood, not a descent.
> Ratified by **QST-0046.2**.

> 📘 **The woods' materials are the Elf's substance, drawn from the hero's own
> Tags**, oak and yew among them, and the Wood Elf reaches sylvan gear vocabulary
> as a trade layer (Wood Elf Longbow becomes Yew of the Green).
> Ratified by **QST-0046.2**.

> 📘 **Legend markers sit beside the real cultures and feed the same reach map**,
> and the Elf holds two of the twelve, `tolkien_elves` and `fairytale_fae`, so a
> name is one roll across both families. Mithril reaches the Elf through the
> legend register rather than the society register.
> Ratified by **QST-0046.5** and **QST-0046.6**.

> 📘 **The Elf declares five lineage siblings, more than any other people, and
> the lineage axis is where the people expands.** Eladrin, Sea Elf and Shadar-Kai
> belong under the Elf as Heritages rather than as peoples of their own.
> Ratified by the **QST-0079** vault survey and **QST-0053**.

That is the whole of the supportive lore this page can currently mark, and two
cautions come with it. The Elf is the only Species that declares five Heritages
(the Tiefling declares three, the Gnome two, and no other Species declares any),
but the vault survey counts sibling shapes rather than Heritages and lists six
under the Goliath, so "more than any other people" is true of the Heritage axis
and not of that survey's own count; the Goliath's six are Traits. Two different
Questae are numbered 0079, and this is the one in the Open queue. QST-0053 states
the three candidate Heritages in a note rather than a decision, and it is still
Open. QST-0046.2 lives in the legacy `Curia` tree rather than under `Documenta`,
so a reader chasing it in one place will not find it.

Everything below rests on `Elves-and-the-Dreaming.md`, on the lineage paragraphs
in the code, on the old wiki and on this page's own decisions log. The formal
system names the Dreaming canon file exactly once, in Decree 0006, and only to
borrow its Death-of-the-Author rule; the word *dream* appears nowhere else in the
Questa and Agora corpus in an Elf sense. Neither Agora queue holds an Elf question
at all. So the origin, the mechanism and the lineage bodies carry no book until a
Questa says otherwise.

### Unratified, and what each one needs

*Stated as design, not as law. Each line names the Questa that would ratify it.*

- **The origin substance: Elves came out of the Fae, and the Fae are made of
  dream.** QST-0046.2 ratifies the Elf/Fae partnership as a culture edge, which
  is a neighbourhood and not a descent. Needs a Questa "The Elf's origin
  substance", so the trait lines and the Archfey reading have a ratified premise.
- **Lineages are cultures, not bloodlines, and the drift is the mechanism.** The
  nearest ratified rule (the species law, in Dialog 0014 of the legacy `Curia`
  tree, and not in the `Documenta` dialog that carries the same number) forbids
  determinism by blood or by upbringing without establishing collective drift as
  the alternative. Needs a Questa "Elf lineages are cultures, and drift is the
  mechanism", stating what it forbids: no individual transformation, no bloodline.
- **The mechanism is collective, a shared subconscious in the Jungian sense.**
  Zero hits across the whole formal system. Needs a Questa "The Dreaming is a
  collective subconscious", which must also decide whether the framing may ever
  surface in player-facing text.
- **Five lineages from three wars, and two branches that never came across.** The
  QST-0079 vault survey counts five and nothing else; QST-0053 in fact opens the
  set to three more Heritages the three-wars frame has no room for. Needs a Questa
  "Which Elf lineages are canon, and what each one's origin is".
- **Fae, Fata and Shadow are one substance, and the slip is used once per text at
  most.** Nothing in the formal system touches it; the fae court appears only as
  the Bard's Glamour ancestry, tied to a College and never to the Elf. Needs a
  Questa "Fae, Fata and Shadow are one substance", turning the once-per-text
  limit into a checkable rule.
- **Physical traits are biological, and the species law is already narrower than
  it looks.** Its one formal statement forbids *moral* determinism by blood or by
  upbringing, so the limit to moral traits is written into the law itself, but
  nothing says the limit is deliberate or names what falls outside it. Needs a
  Questa "Taught, not inherited: what the law does and does not cover", naming
  Keen Senses, Fey Ancestry, Trance and Darkvision.
- **Trance is elves never entirely having left the Dreaming, which four hours of
  meditation reach.** The explanation lives only in the shipping italic line.
  Needs a Questa "Trance reaches the Dreaming".
- **The five lineage bodies and tempers**: the Wood Elf's stag horns, the High
  Elf's cold skin, the Dark Elf's stone-coloured skin, the Fae Elf's arm-long
  ears, the Shadow Elf's white eyes. These live in the five heritage paragraphs
  and nowhere in the formal system. Needs a Questa "The five lineages: body,
  temper and voice", so later prose has a source to keep faith with.
- **The Drow name is in-world slander, and the Dark Elf is a welcoming
  meritocracy.** The reading lives in the shipping heritage paragraph and in the
  wiki. The vault-restore Questa numbered 0081, the one in the legacy `Curia`
  tree, records an intent to alias `Drow` to `Dark_Elf` and attaches no reading to
  it; the Questa numbered 0081 under `Documenta` is a different piece of work
  entirely and says nothing about elves. Needs a Questa "The Drow name is in-world
  slander", which should also say what the old name may imply on the page.
- **Elvenkind: three wars, a recent peace that holds because nobody counts
  grudges, and the Warmongers, Dark Lords and Separatists who threaten it.** Zero
  hits. Needs a Questa "Elvenkind: the peace and what threatens it", because the
  Sellsword, Soldier and Stranger backgrounds are already justified from it.
- **The Khans, and the nomadic clan that carries music and crafts abroad.** Only
  the bare `mongol` key is ratified, and a culture key is not a social
  institution. The word is not merely old-wiki register either: *Khan* ships today
  as an Elf title in the story map, with no Questa behind it. Needs a Questa "Elf
  society: Khans and the travelling clan", which either promotes the register or
  retires it.
- **Elven speech: th becomes S, T or Z, because elves don't show their tongues.**
  Zero hits. Needs a Questa "The Elf name corpus and its phonetic rule".
- **The name corpus's Persian elegance and Romani travel.** This one conflicts
  with a ratified line rather than merely lacking one: QST-0046.2 gives the
  Goblins the Persian register exclusively and gives the Elf only its four keys,
  so Persian elegance in the Elf name file has no key to stand on. Needs a Questa
  "Reconcile the Elf name corpus with the Elf's culture keys", which either grants
  a marker or removes the inspiration.
- **The Other People, the Hidden Folk**: the *aos sí* and *huldufólk* register as
  the species' own name for itself. Zero hits. Needs a Questa "The Other People:
  the Elf's own name for itself".
- **The Jungian slot in the metaphysics table.** QST-0050 ratifies the Celestial
  half (an Ideal fixed) and nods at the dwarven soul-metal, which makes the Elf's
  missing slot conspicuous rather than implied. Needs a Questa "The Elf's
  organising principle", written in QST-0050's shape.
- **The Elves are Druids at species scale.** The Druid's slowed ageing is
  ratified as the class's elder note and says nothing about the Elf. Needs a
  Questa "The Elf and the Druid are the same mechanism at two scales", including
  the standing order never to state it on the page.
- **The three class tensions**: the Moon Druid's nightly shape as a learned form,
  the Wild Magic surge as the Dream leaking through one person, and the Wizard's
  writing and the Artificer's mechanisms as the two forbidden acts. No dialog or
  Questa reads any subclass against a people. Needs a Questa "Where the classes
  strain the Elf canon"; each tension is currently a wiki-only dispensation from a
  wiki-only rule.
- **The Bard drifts the people, and the Archfey pact is signed in the Elf's own
  substance.** The fae court is ratified for the Bard's College and never for the
  Elf; the Archfey is treated purely as a rules-edition problem. Needs a Questa
  covering both readings.
- **The Elf's registers lending to named classes**: the Berserker's Norse home,
  Skaði and Ullr for the Ranger, Loki and Gwydion for the Rogue, Egil and the
  *filí* for the Bard, Tam Lin for the Warlock, the Hávamál for the prayers,
  Gawain's girdle for the Paladin, the steppe archer for the Monk. Every dialog
  that touches this material frames it as a *class* source, never as the Elf's.
  Needs a Questa "The Elf's registers and which class each one lends to".
- **The shadow budget across four sites.** The page credits Decree 0005 with a
  mild negative affinity, and Decree 0005 decides ability-score affinity only and
  never mentions shadow, themes or repetition. The `shadow` gear theme is real;
  the nudge is not. Needs a Questa that actually decides it.
- **The species entry's "we" logged as Decided.** QST-0094 records the split
  across the ten peoples and files it as one of two conventions still to decide,
  noting that the voice law exempts descriptions and that consistency here is a
  taste call. The log should read Open until that convention is closed.
- **The Ranger and the word "archer".** A page-level proposal with no Ranger
  dialog behind it, and there is no Ranger dialog in either tree. Needs that
  dialog, or a Questa "Refuse 'archer' in the Ranger text", before the class text
  is written.
- **The stray letters on generated Elf names.** The fault is not a joining table
  and not a whitespace bug: the surname literals in the Elf name corpus carry the
  letters themselves, so *Flameseekerg*, *Ravenwatcherg* and *Dreamweaverg* sit in
  the table beside *Starfalld* and *Twilightveild*, while the template file the
  corpus was copied from holds the clean *Flameseeker*. Neither cited Questa
  covers it: QST-0052 diagnoses a trailing *space* on a Tiefling and never
  mentions the Elf, and the 0081.5 sidequest records that race strings carry a
  trailing space and that subrace strings do not. Needs its own sidequest, scoped
  to repairing the corpus entries.
- **Deleting `Drow.py` under the one-file rule.** QST-0091.1 never mentions the
  Drow, and the re-export aliases it blesses are import lines in a package
  `__init__`, which is not what this file is: it is a second class definition
  holding the Dark Elf's whole rule set under the old name, reachable by nothing.
  Needs a sidequest "Does the Dark Elf keep its Drow name anywhere?", which is a
  decision about the name and a cleanup of the duplicate, in that order.
- **The proposed Darkvision line.** QST-0094 opens the cross-species Darkvision
  convention and proposes four inspiration lines, all of them the Dwarf's. The
  Elf's proposal should be carried into that Questa's awaiting list rather than
  living on this page.
- **The Elf's Cleric prayers as the Dream's own voice.** The formal system reaches
  the prayer file repeatedly, always for the Cleric's class and domain voice, and
  never for the per-people lines. Needs a Questa "The species prayers", which
  should also move them off a name key onto the Kinship Tag, since the Elf's lines
  are keyed on the string "Elf" today.

### What the rules force, and what we chose

The Elven Lineage is the demanding one. It forces a single people that arrives in
five fixed variants, where the variant decides how far the eyes reach, how fast
the legs carry, and what magic answers, and where the variant is set at creation
and never moves again. Read plainly, that is a bloodline: five bodies with five
inheritances, which is the one thing the species law forbids.

Our answer is that **the lineages are cultures**. Dream of the forest for a
thousand years and the people become Wood Elves. The drift is slow, it is
collective, and it belongs to nobody's choosing. The rule's fixity then describes
where a Character comes from rather than what a Character is made of.

**What that buys beyond the rule.** The 120-foot Darkvision on two lineages stops
being an anomaly and becomes the obvious reading: two peoples lived in the dark,
so two peoples see in it, and the published rule's single upgrade was the odd
case. The Wood Elf's 35 feet is a thousand years of forest instead of a gene. The
Dark Elf rename works, because a culture's name is what other people call it, and
a name can be slander; a bloodline's name could not be. The class-aligned
spellcasting ability turns from an override into a consequence: the culture
teaches the spells, and the faculty the Character already trains is the one that
carries them. And the expansion slot stays open, which is what QST-0053 needs:
Eladrin, Sea Elf and Shadar-Kai can be added as Heritages, because a people can
acquire another culture and cannot acquire another bloodline.

⚠️ **What breaks if a later hand reads the lineages as subraces again.** The five
tempers become inherited temperaments, and the species law is broken in the one
place the project cares most about it. The Drow slander reading loses its footing
and the rename goes back to being cosmetic. The second 120-foot lineage becomes a
rules error to be repaired rather than a reading to be kept. The class-aligned
ability becomes an unexplained silent overwrite with nothing to say for itself.
QST-0053's three candidates have no door. And the Bard and Druid readings, which
both run on collective drift, lose their mechanism at once. That this whole
interpretation is unratified is an argument for writing the Questa, not for
treating the lineages as free.

### The variable detail

Drawn per character, and none of it ratified: which of the five lineages the
Character belongs to; which skill Keen Senses takes, drawn from Insight,
Perception and Survival; which of Intelligence, Wisdom or Charisma first carries
the lineage spells, before the class alignment settles it; the given name and the
surname from the Elf corpus; and the Cleric's prayer line.

None of it was filled in at random. Every draw comes from its own named Dice Bag,
so the lineage, the skill and the ability each have their own stream. The Keen
Senses draw excludes whatever the Character is already proficient in, so the
trait adds something rather than doubling a skill the class handed over, and only
where the class already holds all three does it fall back to the full list. The
ability draw is seeded, so a replay of the same character reaches the same
answer, and the class alignment then puts the people's magic through the faculty
that Character actually trains. The five lineages are five cultures, each with
its own gear vocabulary and its own register. The names follow the corpus's
phonetic rule. And the species spell attack bonus is computed and deliberately
not shown as a chip, because the sheet's Attack Rolls table already carries it,
while the save DC has no such table and keeps its chip. It carries no book
because no Questa says so.

---

## 📚 1. Where the Elf lives in the code

| What | Where | State |
|---|---|---|
| Species entry | `AtlasActorLudi/SpeciesKit/Elves/__init__.py` | Shipping. First person plural. Three wars, one word (Elvenkind), and "seven hundred years to be patient in, and you only need one second to shoot." |
| Lineages | `Elves/Wood_Elf.py`, `High_Elf.py`, `Dark_Elf.py`, `Fae_Elf.py`, `Shadow_Elf.py` (`Drow.py` is the Dark Elf's older name) | Each carries a "we" paragraph (the body and the temper) and a lineage spell set. Fae and Shadow Elves are the Lorwyn pair, renamed. |
| Traits and rules | `Elves/traits.py`, `resolution.py` | The house pattern (QST-0094): an italic line, then the rule. Trance's line: *"Elves are said to be made of the same essence as dream and nightmare. Perhaps there is more than mere poetry to it."* |
| Names | `AtlasNomina/Races/Elf.py` | Inspirations: Persian, Nordic Fae (Huldufólk), Iceland, Romani, Celtic Ireland. "Th becomes S, T or Z: elves don't show their tongues." White pupils. Society notes in the file header. |
| Culture keys | `norse`, `rus`, `mongol`, `celt`; legends `tolkien_elves`, `fairytale_fae` | "A bit Fae and a bit other people, in a colder nature." |
| Prayer | `Map_of_Cleric_Prayers.py` | *Dreams are made to be lived.* *May the dream guide your way.* Light: *Light, love, and music will endure.* Knowledge: *We live in one another's shadow* (Irish). |
| Old wiki | `app/Wiki/Lore.html` | The "Other Folk, Fata and Hidden People"; clans called **Khans**; "a living echo of dreams." |
| Canon | `Documenta/Canon/Elves-and-the-Dreaming.md` | Lineages are cultures; the drift is collective; Fae, Fata and Shadow are one substance. |

---

## 📜 2. Origin: the Dreaming

**Lineages are cultures, not bloodlines.** Dream of the forest for a thousand
years and you become a Wood Elf: hairier, some with little stag horns. Dream
of the deep places and you become a Dark Elf, skin like the stones of home.
Dream of the crossings and your ears grow exquisite. Never by one elf's
choosing; over centuries; and never alone. An elf raised elsewhere drifts
elsewhere, given time.

**The mechanism is collective.** A shared subconscious in the Jungian sense.
Every legend the people tell shapes them a little; every century of living
somewhere marks the whole culture; the individual carries what the people
dreamt. This is why the lineage entries are written in the first person
plural: *we* adapted, *our* forebears stayed where the trees were.

**Five lineages from three wars.** The species entry names three: painted faces
hunting intruders in the woods (Wood), icy ships conquering seas (High),
ambushers who came from below (Dark). The Fae Elf and the Shadow Elf are the
branches that never came across at all, which is why their marks are the
strangest.

**Fae, Fata, Shadow: one substance.** The Dream wears a different face
depending on who is looking, and mortals named each face separately because
they met it separately. Fae is the Dream met as court, glamour and bargain
(Titania, the Archfey). Fata is the same thing met as one old woman in a wood
(Baba Yaga; Latin *fata*, the Fates, through *fatare*, to enchant, is where
*fairy* comes from). Shadow is the Dream met as nightmare. Nothing
distinguishes them but the encounter. A fae speaker who calls itself a shadow
is telling the literal truth and the mortal hears poetry; use it once per text,
never more, or it becomes a lecture.

**What it quietly explains.** Trance: elves never entirely left the dreaming,
so four hours of meditation reach it. Why the Shadow Elf is not a villain: the
nightmare face is the same substance.

**Physical traits are biological** (the species law permits biology): Keen
Senses, Fey Ancestry, Trance, Darkvision. The Dream shaped the body over
centuries; the body is what the Character has tonight.

---

## 📜 3. The five lineages

| Lineage | The dream | The body (from the "we" paragraphs) | The temper | Where the answers come from |
|---|---|---|---|---|
| **Wood Elf** | The forest, a thousand years | Hairier; some with little stag horns; some still paint their faces | Pensive, observant, direct | The druids first |
| **High Elf** | The ice, the ships, the sea | Golden hair; skin cold to the touch whatever its tone | Patient, cold, adaptive; "found magic, found commerce, found crafts" | The magi and the wizards |
| **Dark Elf** | The Underdark, and staying | Silvery hair; skin like the stones of home | Cunning, calm, welcoming; "a meritocracy… while others poisoned our legend" | The priest and the cleric |
| **Fae Elf** | The crossings; the branch that never came across | Ears "exquisitely long, sometimes as long as our arms"; the most beautiful of elvenkind "even with our charms off" | Polite, friendly, more open to emotion | The Courts |
| **Shadow Elf** | The Shadow realm, "what was left"; the other branch that never came across | Skin any grey from perfect white to pitch black; eyes all white | Stoic, reflective, analytic: "to discern dream from thought" | The oracles and mystics |

The lineage paragraphs are the species' physical voice. Two
things they establish that later prose must keep: the Dark Elf's legend was
*poisoned by others* (the Drow slander is in-world slander), and the Shadow Elf
"feels scary at times, but it's home."

---

## 📔 4. Society: the Other People

**Elvenkind.** *"War after war, we fought each other, but now one word unites
us… Today a long peace holds, and it holds because nobody is counting grudges
any more."* The peace is recent, defended by "arrow and spell", and threatened
by "Warmongers, Dark Lords and Separatists". The elves are the setting's people
who *chose to forget*, against the Dwarves who remember and the Goliaths who
fell. The Bard page found the Dream drifts on story; a people who stopped
telling the war stories stopped becoming the war.

**Khans.** The old wiki: elves wander in powerful, secretive clans called
Khans, "guardians of ancient magics and legends lost to mortal memory." The
name file's society notes add a scholarly, artistic society blending Persian
elegance with Nordic secrecy, druidic rituals, seasonal festivals, and **a
nomadic clan that travels the world, bringing music and crafts to other
cultures.** The `mongol` key is the steppe; the `rus` key is the river-road;
`norse` is the icy ships; `celt` is the woods and the harp. The Khan is what a
clan is called when its people were archers who rode.

**Speech.** *"Th becomes S, T or Z: elves don't show their tongues."* A
phonetic rule with a manner inside it, and the kind of detail the wiki should
keep.

**The Other People, the Hidden Folk.** The old wiki's register: Celtic and
Nordic legend's *aos sí* and *huldufólk*, "those who walk at the edge of the
seen and unseen." The species entry's opening is the same claim from inside:
*"The Other People. That's us."*

---

## 📜 5. Culture and registers

**Norse**: the berserkr and the úlfheðinn are Odin's, so the Berserker's mythic
home is Elven (Barbarian page); Egil the poet-berserker and his head-ransom
(Bard); Skaði and Ullr, the huntress and the bowman, so the Elf Ranger has its
own gods and need not be Legolas (Ranger); Loki the thief (Rogue); the Hávamál
in the prayers (*"Cattle die, kinsmen die…"*); Tam Lin and Thomas the Rhymer
on the Celtic side, the only stories where an Archfey pact *ends* (Warlock).

**Celt**: the historical druids ("they think it improper to commit their
studies to writing", Caesar), so the druid as an institution is Elven and a
Human Druid is one by trade (Druid page); Gwydion the trickster-magician
(Rogue); the *filí* whose satire raised blisters (Bard); *"We live in one
another's shadow"* (Knowledge prayer); Gawain's girdle and the Wild Hunt
(Paladin, Ranger).

**Mongol and Rus**: the steppe archer's speed on foot (Monk); the river-road;
the Khan as the clan's name; *"Gods are not in strength, but in truth"* (Rus,
Knowledge); *"The Eternal Light is watching"* (Mongol, Light).

**Legends**: `tolkien_elves` (Elven blades, star-glass, mithril shirts);
`fairytale_fae` (cold iron, thorn and briar, the rowan staff; shared with the
Fae and the Goblins).

**Materials**: oak, yew and the woods' materials through the Elf and Druid
themes; mithril through the Tolkien register.

**Names**: Persian elegance, Icelandic and Celtic sagas, Romani travel, the
Huldufólk. The generator's elves: Elri Flameseeker, Nailo Dreamchaser,
Siamin Nightweaver, Dinendenan Gloryfinder, Zeirgelidrar Redresen. (The
trailing "g" on some generated Elf names, *Flameseekerg*, *Gloryfinderg*, is
QST-0052's trailing-character bug and not a naming choice.)

---

## 📜 6. Metaphysics: the people decided by what everyone imagines

**Against the other Platonisms.** Two peoples are Platonic (Dwarf: soul-metal
given; Celestial: an Ideal fixed) and the Elves are Jungian: the only people
whose nature is decided by what everyone agrees to imagine. That is the joke,
and the design.

**The Elves are Druids at species scale.** "Dream of the forest for a thousand
years" is Archdruid's slowed ageing done unconsciously by a whole people. An
Elf Druid does on purpose, in one life, what the species does over centuries.
Never say so.

**Change is slow and shared: three tensions the classes create.**

- **The Moon Druid** changes shape nightly. Wild Shape is a learned form, not a
  lineage drift, so the canon is not broken; the elders will *think* it is.
- **The Wild Magic Sorcerer**'s surges may change an elf's body in a scene, which
  the canon says never happens. The dice can break the rule; the story is the
  Dream leaking through one person, and the elders' horror.
- **The Elf Wizard writes it down**, and the Dream is never written. The
  elders' one forbidden act. **The Elf Artificer** builds mechanisms, which the
  Gnomes left the Dream to do; the reverse Gnome. The second forbidden act.

**The Bard drifts the people.** *"Every legend the people tell shapes them a
little."* An Elf Bard's ballads are, over centuries, what the next Wood Elves
look like. The class that operates the Dream from outside (Bard page).

**The Archfey Warlock signed with the substance they are made of.** The verse's
"we shadows" is literal for an elf. A Fae Elf Archfey Warlock is the Dream's own
child taking the Dream's own terms, and "We shall never see quite where" is the
one privacy the patron grants.

**The shadow budget.** Shadow Elf, Shadow background, Warrior of Shadow, the
`shadow` gear theme: four sites that can land on one sheet. The canon's own
rule about the slip (once per text) is broken by composition. A mild negative
affinity between them (Decree 0005) keeps the word rare without closing a door.

---

## 📔 7. The classes: the Dream in each

| Class | The Elf in it |
|---|---|
| **Barbarian** | The Berserker's mythic home (Odin's bear-shirts and wolf-coats): a High Elf Berserker off the icy ships is the truest berserkr on the roster; a Wood Elf Wild Heart is an elf mid-drift. |
| **Druid** | The species at scale; the Moon Elf's elders (§6). |
| **Ranger** | Skaði and Ullr; the Dark Elf Gloom Stalker ("ambushers who came from below"); the Fey Wanderer who came back "a little too charming for the woods". ⚠️ The Elf Ranger is the cliché's landing zone; refuse "archer". |
| **Bard** | Egil's head-ransom; the skald's *níð* as Cutting Words; the Dream drifting on story. |
| **Wizard** | The one who writes what the species dreams (§6). The Fae Elf Bladesinger and the sword dance that taught calligraphy. |
| **Warlock** | The Archfey: signed with the substance (§6). Tam Lin as the pact that ended. |
| **Rogue** | Loki, Gwydion; the Dark Elf Assassin. The shadow budget. |
| **Monk** | The steppe archer's speed; Trance and mushin are neighbours (an elf is vestigially in the Dream already). The Shadow Elf Warrior of Shadow: the nightmare face as an element. |
| **Paladin** | Gawain's girdle: the Ancients Paladin sworn to what was here first, which for an elf is the Fae, which is the Dream, which is their own subconscious. Undying Sentinel gives an elf nothing they did not have. |
| **Cleric** | The watcher is *everyone*: the shared Dream. "Maybe the universe itself" is the Elf's guess, and closer to true than they know. |
| **Sorcerer** | Wild Magic as the Dream drifting fast in one elf (§6). |
| **Fighter** | Studied Attacks across a century; the Chaotic Psi Warrior ("you are your own master") as a Dream-descended child refusing the collective. |
| **Artificer** | The reverse Gnome (§6). |

---

## 📔 8. Backgrounds

- **Shadow.** The Shadow background ("you were born on the other side, where
  the Fae are made of dream and shadows are made of nightmare") is the Elf
  canon's own sentence. On a Shadow Elf it is redundant; on a Fae Elf it is the
  branch meeting its nightmare face. Mind the budget.
- **Fated.** "Promised to a witch." Fata is the Dream met as one old woman; a
  Fated Elf was promised to their own substance.
- **Naturalist, Wildkeeper.** The Wood Elf's defaults; the drift as a career.
- **Stranger.** An elf who left Elvenkind: "a language fewer people speak each
  year" in a people who live seven centuries is a slow catastrophe.
- **Vagabond.** The nomadic clan of the name file: the elf who brings "music
  and crafts to other cultures".
- **Ice Nomad.** The High Elf's ice, on foot.
- **Sellsword, Soldier.** The peace "needs arrow and spell to defend it";
  the Elf who defends it for pay.
- **Investigator, Debunker.** The Shadow Elf's "discern dream from thought" as a
  profession.
- **Servant, Gambler.** The elf in a drawing room, where the Dream is
  furthest away.

---

## 📜 9. Decisions log

**Standing (canon)**

- Never explain the Dreaming on the page. Lineages are cultures, never
  bloodlines. Change is slow and shared: no elf transforms in a scene, no elf
  transforms alone. The Fae/Fata/Shadow slip once per text, at most.

**Decided**

- The species entry speaks as "we" (`9be3a07` era); the lineage paragraphs
  likewise.
- The house pattern for trait entries (italic line, then rule) is the Elf's
  and the Halfling's, and the reference for the other peoples (QST-0094).

**Open (this page proposes)**

- The shadow budget nudge (Decree 0005) across Shadow Elf, Shadow background,
  Warrior of Shadow and the `shadow` gear theme.
- The `Drow.py` file duplicates `Dark_Elf.py` under the old name; one should
  go (QST-0091.1's one-file rule).
- The Elf Ranger and "archer": the class text, when written, should not say
  the word; the species entry already owns the bow.
- QST-0052: trailing "g" on generated Elf names.

---

## 📖 10. Lines

*The Elf's trait lines exist and are the house pattern. Listed here as the
reference, with one proposal.*

| Entry | Line (shipping) |
|---|---|
| **Keen Senses** | *Your elven eyes are sharp and your attention focused.* |
| **Fey Ancestry** | *The echoes of the Fae still linger in you, letting you see…* |
| **Trance** | *Elves are said to be made of the same essence as dream and nightmare. Perhaps there is more than mere poetry to it.* |
| **Wood Elf lineage** | *The woods have always answered your people, and some of that answer stayed with you.* ("first" was removed: the nativist undertone.) |
| **Dark Elf lineage** | *The dark taught your people how to survive it, and some of that lesson still answers when you call.* |
| **High Elf lineage** | *Your people traded with more than merchants, and not everything you brought home was cargo.* |
| **Fae Elf lineage** | *The crossing into the Feywild left more on you than long ears.* |
| **Shadow Elf lineage** | *Telling dream from thought took practice, and the practice stayed.* |
| **Darkvision** (proposal, if the Aasimar convention spreads) | *The dark is only the Dream with the lights off. You have never been afraid of it.* |

---

## 📚 11. Pointers

- **Druid page**: the species at scale; the Moon Elf.
- **Bard page**: the Dream drifts on story.
- **Barbarian page**: the Berserker's Norse home.
- **Ranger page**: Skaði; refuse "archer".
- **Warlock page**: "we shadows" as literal.
- **Monk and Rogue pages**: the shadow budget.
- **Celestials page**: fixed against malleable.
