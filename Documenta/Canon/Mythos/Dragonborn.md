# 🐉 Dragonborn

> 📖 **In flow.** 1 of 12 chapters are still proposals. 📜 4 · 📚 2 · 📔 5 · 📖 1

> - 📕 **inherited from the 2024 rules.** Moving it costs rules compatibility.
> - 📙 **an aesthetic change.** The same rule wearing our name and look.
> - 📒 **a rule we changed.** A house rule, and it already cost compatibility.
> - 📘 **supportive lore.** It holds a rule or a core element up.
> - 📗 **deep lore.** Design that supports the fantasy rather than a rule.
> - A book marks a statement only if it can change exclusively through the
>   Questa / Agora / Decree system. Anything with no Questa and no Decree behind
>   it carries no book, however settled it feels.

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from `Dragons-and-the-Overcoming.md`, the Dragonborn kit,
`AtlasNomina/Races/Dragon.py`, the class analyses and the design notes. The Dragon
canon's first rule governs every line here: never explain it on the page.*

> **In one sentence.** The children of dragons, and none the wiser for it: a
> people who built a civilisation of rules by watching beings who kept none,
> and who stand nearer than anyone to the thing the dragons did, without ever
> being told so.

---

## 📜 0. Rules

*The fixed points, and what we made of them. The books are defined at the head
of the page.*

### The rules as given

*Each entry is the rule itself, complete enough to resolve at a table. Not a
summary and not a cross-reference.*

> 📕 **Creature Type** Humanoid. **Size** Medium, and Medium is the only
> option. **Speed** 30 feet.
>
> 📕 **Darkvision.** You have Darkvision with a range of 60 feet. You can see in
> Dim Light within 60 feet as if it were Bright Light. In Darkness within that
> range you can see as if it were Dim Light: you have Disadvantage on Wisdom
> (Perception) checks that rely on sight there, and you discern colors there
> only as shades of gray.
> > 📘 _A dragon sees in the dark. So, a little, do you._ (proposed)
>
> 📕 **Draconic Ancestry.** Your lineage traces back to a dragon progenitor of
> one of ten kinds, fixed once when the Character is made. That kind determines
> a single damage type: Acid (Black, Copper), Lightning (Blue, Bronze), Fire
> (Brass, Gold, Red), Poison (Green), Cold (Silver, White). That damage type is
> the damage type of your other draconic traits, which are your Breath Weapon
> and your Damage Resistance. Nothing else about the ancestor dragon is
> mechanical.
>
> 📙 **Damage Resistance** [printed inside the **Draconic Ancestry** entry, not
> as its own entry]: You have Resistance to the damage type determined by your
> Draconic Ancestry trait (Acid, Cold, Fire, Lightning or Poison). Resistance
> means you take half damage of that type, rounded down, after every other
> modifier to the damage is applied.
>
> 📕 **Breath Weapon.** When you take the Attack action on your turn, you can
> replace one of your attacks with an exhalation of magical energy in either a
> 15-foot Cone or a 30-foot Line that is 5 feet wide, choosing the shape each
> time you use the trait. Each creature in that area makes a Dexterity saving
> throw against DC 8 + your Proficiency Bonus + your Constitution modifier,
> taking damage of your Draconic Ancestry's type on a failed save and half as
> much damage on a successful one. The damage is 1d10 at character levels 1 to
> 4, 2d10 at 5 to 10, 3d10 at 11 to 16, and 4d10 at 17 and above. You can use
> this trait a number of times equal to your Proficiency Bonus, and you regain
> all expended uses when you finish a Long Rest.
> > 📘 _Everything you were taught to hold in, let out once, at something._ (proposed)
>
> 📕 **Draconic Flight** (level 5). As a Bonus Action you sprout spectral wings
> on your back, which appear to be made of the same energy as your Breath
> Weapon. They last for 10 minutes, or until you retract them (no action
> required) or you have the Incapacitated condition. During that time you have a
> Fly Speed equal to your Speed, which is 30 feet for a Dragonborn with no other
> speed modifier. Once you use this trait, you can't use it again until you
> finish a Long Rest.
> > 📘 _The ones who stayed home never grew these. You did not ask why. You went._ (proposed)

No rule of the Dragonborn has been changed, so this page carries no 📒. Three
things in the block above are presentation and not rule. The Resistance folded
into the Draconic Ancestry entry is the 📙. The chip-only Darkvision is a
ratified convention (QST-0051) that is also an open one (QST-0094). And the
Disadvantage sentence inside Darkvision is not in the 2024 glossary's Darkvision
entry at all: it follows from Darkness-seen-as-Dim-Light being Lightly Obscured,
and `SpeciesKit/traits.py` prints it on purpose, so that a player reading the
sheet does not assume darkvision cancels the penalty.

### The supportive lore

> 📘 **The two culture wells are `japan` and `aztec`, and they are two keys and
> never one.** The Aztec side is the Coatl. Qing China belongs to the Fae and
> not to the Dragonborn. Fused keys were rejected: a species holds a list of
> keys, not a blend, and holding two at once is the rule of which this pair is
> the named example.
> Ratified by **QST-0046.2** and **QST-0046.5**.
>
> 📘 **The Japanese weapon vocabulary is the Dragonborn's, and the Aztec
> register reaches the same roll.** A Dragonborn Longsword draws Katana beside
> Jian and Longsword; a Dragonborn Paladin reaches Macuahuitl and Nodachi from
> one roll.
> Ratified by **QST-0046.2** and **QST-0046.5**.
>
> 📘 **`eragon_dragons` is a legend marker feeding the same reach map as the
> societies, and the Dragonborn reach its vocabulary** (Wyrmrider's
> Greatblade).
> Ratified by **QST-0046.5**.
>
> 📘 **The ninja register belongs to the Monk and stacks on top of the species
> keys**, so a Dragonborn Monk carries both.
> Ratified by **QST-0046.2**.
>
> 📘 **Darkvision prints as a chip and not as a paragraph on this sheet, by
> design, because it is a record rather than prose; and the cross-species
> convention is open.** Five species print the rule; the Dragonborn and the
> Aasimar print the chip.
> Ratified by **QST-0051**; reopened as a question by **QST-0094**.
>
> 📘 **Breath Weapon already carries the house pattern of an inspiration line
> before the rule, and Draconic Flight no longer announces its own level.**
> Ratified by **QST-0094** and **QST-0055**.
>
> 📘 **The Dragonborn kit is the project's reference implementation for
> species-feature voice**, together with the Aasimar.
> Ratified by **QST-0062**.
>
> 📘 **The Draconic Ancestry resolves to a damage type today, and pointing it at
> a generated dragon instead is acknowledged future work.**
> Ratified by **QST-0050**.
>
> 📘 **Kobolds are draconic kin, a step aside from the Dragonborn, and are not
> yet a playable species.**
> Ratified by **QST-0053**.
>
> 📘 **No people may be metaphysically silent.** The Dragon canon's table gives
> one organising principle per people, and a species either takes an existing
> one or brings its own.
> Ratified by **QST-0053**.
>
> 📘 **Deep lore is never explained to the player.** User-facing text invites
> and inspires; it never lectures. Everything this page keeps unspoken is kept
> unspoken under this rule.
> Ratified by **Decree 0006**.
>
> 📘 **A dragon is a legitimate object of an Order's devotion.** What an Order
> must have is cultists, devotion and obligation, and not a deity.
> Ratified by **QST-0048**.

That is the whole of the supportive lore this page can currently mark.
Everything else below rests on the canon documents and on this page's own
decisions log, which are not the Questa / Agora / Decree system, so it carries
no book until a Questa says otherwise. Nothing in either Agora discusses this
species by name.

### Unratified, and what each one needs

*Stated as design, not as law. Each line names the Questa that would ratify it.*

- **The Ascending.** A dragon is not a kind of creature but something a person
  becomes; realisation actualises the body; anyone can Ascend, and it is not a
  bloodline. This rests on `Dragons-and-the-Overcoming.md` alone. Two Agora
  Dialogs restate it (0014 Barbarian, 0017 Druid), both marked 🟡 provisional
  and both citing the canon file as the authority. Needs a Questa ratifying the
  Dragon canon itself, with the bloodline question settled.
- **The inherited shape.** An Ascending assembles the dragon from every story
  the person ever heard; no two traditions give the same silhouette; none is the
  real one; the east and west split is forbidden. The system's only
  silhouette-adjacent ruling is the culture-key split, which decides vocabulary
  reach and never body shape. Needs a Questa on draconic silhouette by
  tradition, and on what the sheet may print.
- **Two silhouettes for the two keys**: the Japanese *ryū* of the `japan` well
  and the feathered serpent of the `aztec` well, the Aztec-well Dragonborn as
  Quetzalcoatl's child, and the colour as the only thing drawn. This is the
  page's own inference from the two keys, and none of those words appears in the
  formal system. Needs the same Questa on physiology by culture key.
- **The dragon's character**: owes nobody anything, lives without friction, the
  hoard is the meaning and not the gold, some come back down in a humanoid
  shape, and they resist godhood and get worshipped anyway. Canon prose only.
  Needs a Questa making it citable law.
- **Descent, proximity, and the observed code.** That Dragonborn descend from
  dragons, live near enough to speak with them, and built a codified, grandiose,
  outward-facing civilisation by watching beings who kept no rules. This rests
  on the species entry and the canon. Needs a Questa ratifying Dragonborn
  society and the observed-code origin as the people's organising principle.
- **Nearest to the Ascending of any people.** Nothing in the system ranks
  peoples by nearness to it. Needs a Questa that ranks them or rules that no
  ranking is canon.
- **Draconic Flight as the tell.** QST-0055 and QST-0094 decide the entry's
  voice and remove its level announcement; neither gives the trait a meaning.
  Needs a Questa on whether the feature carries the Ascending's tell, and
  whether its line may hint at it.
- **The ancestor map**: ten colours onto five damage types, drawn once per
  Character and kept. This rests on `Map_of_Ancestors.py`, which the system
  names once, as a filename in QST-0079's vault inventory. Needs a Questa
  ratifying the ten colours, the five damage types and the draw-once rule.
- **Every trait number.** No Questa states a Dragonborn trait value. The only
  Dragonborn number the system quotes is the level 5 inside the *"Gained at
  Level 5."* string that QST-0094 removed, and the Darkvision ranges it quotes
  elsewhere belong to other species. Needs a Questa verifying the numbers
  against the 2024 rules and printing them resolved, the way QST-0057 and
  QST-0059 do for spells. The kit's self-test does reach this species, but only
  through what `_test_playable_species` asserts of every playable one: Creature
  Type, size, speed, the already-gained vocabulary rule, and that no Species
  entry is empty unless its chips are the feature. Not one Dragonborn number is
  asserted anywhere: not the ancestor map, not the breath dice, not the save DC,
  not the granted Resistance. That is the kit's largest test gap.
- **The clan's "we".** The species entry does speak in the first person plural
  (*"We have a duty to our clans"*), and turns to the reader only in its closing
  question. QST-0094's open question 2 files the Dragonborn among the species
  that address the reader as "you", so the record is the stale half and not the
  page. Needs QST-0094's question 2 answered, and its list corrected.
- **The dragon cult's shape**: an imperial cult with a genuine contemplative
  strand, not a cargo cult, and the three relations (as rulers, as masters, and
  no longer following). Species description only. Needs a Questa, including what
  of it may reach the player.
- **The code as the people's substance**, with its cost (expectation crushes
  people, and a hardness is demanded of their own) and its good (cohesion,
  service, the warrior in the garden). Needs a Questa on Dragonborn etiquette as
  a design axis, and on which backgrounds and classes are licensed to spend it.
- **Isolated and imperial at once**, as the reason for this pair of keys.
  QST-0046.2 and QST-0046.5 choose the keys and give a different reason. Needs a
  Questa recording the isolationist and imperialist rationale, amending
  QST-0046.2.
- **The Dragon Cultists as the philosophical failure case**, and the "Secrets of
  the Dragon Master" hook as the canon's descent seen by a believer. Neither
  name appears in the formal system. Needs a Questa reading the background
  against the Dragon canon and settling its relation to the Order Cultist
  background of QST-0061.
- **The Ascendant Dragon's slot.** That the Orders' Primal dragon devotion fills
  it and no subclass is minted. QST-0048 rules only that a dragon may be an
  Order's devotion. Needs a Questa on the slot, and the pointer §10 asks for.
- **`wyrm_myth` as the Dragonborn's and the Kobolds'.** The table agrees with
  the page: `Map_of_Gear_Titles._CULTURES` gives the Dragonborn `japan` and
  `aztec` with the legends `eragon_dragons` and `wyrm_myth`, gives the Kobold
  `wyrm_myth` as well, and leaves the Goliaths holding `rome`, `sparta` and
  `homeric` with `arthuriana` as their only legend. QST-0046.4 is Solved, but it
  rules on the classical societies and on `homeric`, not on this row: its remark
  that the Goliaths hold `wyrm_myth` describes the table before the split, and
  its answer to question 3 only leaves the monstrous register with `wyrm_myth`,
  wherever that key ends up sitting. So §5's three or four ways out is genuinely
  open, and nothing ratifies the Dragonborn row either way. Needs a Questa on
  who holds `wyrm_myth`, amending QST-0046.4 if the answer moves it.
- **The loaded-name rule for gear titles**, under which a Dragonborn drawing a
  *Wyrmbane* is a kinslayer or a trophy-taker and better either way. The nearest
  ruling, QST-0048's fourth principle, states guided rather than filtered
  randomness for Orders, not for gear pools. Needs a Questa stating the rule for
  titles: a mismatch between the draw and the carrier is a story, and no pool
  may be filtered to prevent it.
- **The shared-source draw**, that the Draconic Sorcerer's ancestry is the
  species' ancestry, one draw and one colour. This lives in this page's
  decisions log and nowhere else, and the code does not implement it yet:
  `draconic_ancestor` is read only inside the Dragonborn package. Needs a Questa
  ruling that a species and a subclass sharing a source draw once, with the
  Draconic Sorcerer as the worked case.
- **The scope of the species law**: moral determinism forbidden, plainly
  physical traits permitted. The only no-bioessentialism ruling in the system,
  QST-0048's second principle, is about Order membership. Needs a Questa fixing
  the scope once, asserted by the SpeciesKit self-test.
- **The class and background readings** of §6 and §7, and the dragon against
  giant axis (`arthuriana`). The class Dialogs are provisional and decide each
  class's own fantasy; nothing assigns the myth conflict. Needs a Questa
  establishing species by class readings as a ratified layer, and one assigning
  the myth axis across Goliath and Dragonborn.
- **The Couatl** as a dragon bound to an Ideal, or an Ideal wearing a dragon's
  shape. QST-0050 owns settled Celestial lore and its descent list holds no
  dragon. Needs QST-0050 extended.
- **The prayer lines** as the code made faith, and the War line's double stop
  (the `("Dragonborn", "War")` seat reads *"Life is a long battle.."*).
  `Map_of_Cleric_Prayers.py` reaches the formal system twice: QST-0087, for one
  rewritten Cleric paragraph, and Agora Dialog 0016, which proposes new Domain
  openings and leaves every prayer seat as it is. Neither names this species.
  Needs a Questa sweeping the prayer ledger.
- **The name canon and the Draconic morphemes** (*ji* wing, *kan* to wing, the
  dragonkin endings). `AtlasNomina/Races/Dragon.py` is named once, in Curia
  QST-0023, for its implicit string concatenations. Needs a Questa ratifying the
  corpus and the canon line at its head.
- **The proposed lines of §9 and §12.** Drafts, not landed content. QST-0094
  sets the precedent by carrying the four Dwarf inspiration lines as proposals,
  and it carries no Dragonborn line. Needs QST-0094 to carry these the same way.

### What the rules force, and what we chose

The Ancestry and the Flight are the demanding ones. The rules force one
ancestor, fixed once, whose colour is the only mechanical fact about it, and
whose single damage type is shared by the Breath Weapon and the Resistance. They
also force a body that grows wings at level 5, made of the breath's own energy,
for ten minutes once a day. The rules give a colour, an element and a schedule,
and then stop.

Our answer is that **a dragon is not a kind of creature but something a person
becomes**, and that **Draconic Flight is the tell**.

**What that buys beyond the rule.** The ancestor is drawn once from a named,
level-free bag, so a Dragonborn never changes colour on levelling. Read against
the canon that draw becomes the inherited half of the canon's own sentence: the
shape is inherited even when the self is not. A Dragonborn who re-rolled colour
at each level would say the opposite thing. The Flight's timing does the rest of
the work: level 5 is when a Character has left home, so the wings arrive on the
adventurer and never on the clan, and the trait's own schedule carries the tell
without a line having to name it. That is why the proposed line stops at "You
went". The Breath Weapon and the Resistance share one type because they are one
organ, and folding the Resistance into the Draconic Ancestry entry is that
reading in the layout. The society follows from the same reading: a people who
built a code by watching beings who kept none needs a dragon that authors
itself, or there is nothing to watch and the code has no origin. Downstream, the
Draconic Sorcerer's shared draw, the Dragon Cultist as a philosophical failure
rather than a generic cult, the Ascendant Dragon's Order slot and the Couatl all
read off this one interpretation.

⚠️ **What breaks if a later hand removes the Ascending as flavour.** Draconic
Flight becomes a free Fly Speed arriving at level 5 for no reason, and its line
has nothing to point at. The Dragon Cultist's "someday you will become your own
Master" stops being a misreading and becomes a promise. The Ascendant Dragon has
nothing behind it, and the next hand mints a subclass for a slot the Orders
already fill. The level-free ancestor draw looks like an oversight, and somebody
improves it into a re-roll per level. The Couatl loses the half of it that is a
dragon. The interpretation is invisible on the sheet on purpose, under Decree
0006, and that is exactly what makes it easy to delete in good faith. That it is
unratified is an argument for writing the Questa, not for treating it as free.

### The variable detail

Drawn per Character, and none of it ratified: the ancestor colour, one of ten,
unweighted, from the `dragonborn.ancestor` bag, and with it the damage type
carried by the Breath Weapon and the Resistance; and the name, from the Draconic
corpus. The ancestor is a recorded field and not a Heritage, so the draw gives
the Dragonborn no subspecies and does not divide the people.

None of it was filled in at random. The colour is the only thing the rules make
mechanical about the ancestor, so drawing it once and keeping it level-free is
the canon's inherited shape held still while the self stays the player's. The
silhouette is deliberately not drawn: the canon gives one shape per tradition
and no true one, so the sheet prints a colour and leaves the shape alone. The
names come from a corpus whose morphemes mean something, so a drawn name reads
as Draconic rather than as noise. It carries no book because no Questa says so.

---

## 📚 1. Where the Dragonborn lives in the code

| What | Where | State |
|---|---|---|
| Species entry | `AtlasActorLudi/SpeciesKit/Dragonborn/__init__.py` | Shipping. First person plural ("we"), the clan's voice. Closes on "which observance you have kept, and which one you have quietly stopped keeping." |
| Ancestors | `Dragonborn/Map_of_Ancestors.py` | Ten colours, five damage types, drawn once and kept. |
| Traits and rules | `Dragonborn/traits.py`, `resolution.py` | Reference kit for voice (QST-0062). Breath Weapon carries a line; Draconic Ancestry names the colour and its damage; Darkvision is chip-only; Draconic Flight has no line. |
| Names | `AtlasNomina/Races/Dragon.py` | Opens with the canon in one sentence: "Dragons are not born, they become." Draconic morphemes (*ji* wing, *-on* / *-in* dragonkin). Inspirations: real dragons, Chinese, Japanese. |
| Culture keys | `japan`, `aztec`; legends `eragon_dragons`, `wyrm_myth` | Two distinct wells, never fused. `wyrm_myth` is an open question (§5). |
| Prayer | `Map_of_Cleric_Prayers.py` | *Clan. Honor. Duty.* *Your word is your bond.* Light: *Fire spreads. We gather around it.* War: one typo. |
| Canon | `Documenta/Canon/Dragons-and-the-Overcoming.md` | The Ascending; the rules for writing dragons. |

---

## 📜 2. Origin: what a dragon is, and what a Dragonborn is not

**A dragon is not a kind of creature. It is something a person becomes.** A
person carries the potential to overcome the culture that made them and arrive
at a self genuinely their own; when that happens, realisation actualises the
body. The word for it is Ascending, and it is literal when they fly off.
Anyone can Ascend; it is not a bloodline. The shape is inherited even when the
self is not: an Ascending produces the dragon that person was always carrying,
assembled from every story they ever heard about dragons. No two traditions
produce the same silhouette and none is the real one.

**A dragon is not good.** It owes nobody anything and lives without friction.
The hoard is the meaning, not the gold. Some come back down and run a guild or
a bloodline in a humanoid shape, because the shape is a tool once you are past
needing it to be a self. They resist godhood and get worshipped anyway.

**Dragonborn descend from dragons, are shaped like them, and live near enough
to speak with them.** They built a civilisation of rules by observing beings
who were following none, which is why the society is codified, grandiose and
outward-facing: every value arrived by watching somebody else. **And they are
not the ones who missed it.** Of every people in the setting the Dragonborn
are best placed to Ascend for real, because they are nearest the thing and can
ask it questions. Whether any of them does is never confirmed on the page.

**Draconic Flight at level 5 is the tell.** An adventuring Dragonborn sprouts
wings that the ones who stayed home do not. Leaving, and becoming something of
your own out there, is the first flicker of the real thing. Nobody in-world
names it that.

---

## 📔 3. The vessel: physiology

Wingless, bipedal dragons: scaled, bright-eyed, thick-boned, horned, coloured
after the ancestor. **Ten ancestors, five damage types**, drawn once per
Character and kept:

| Ancestor | Damage | Ancestor | Damage |
|---|---|---|---|
| Black | Acid | Gold | Fire |
| Blue | Lightning | Green | Poison |
| Brass | Fire | Red | Fire |
| Bronze | Lightning | Silver | Cold |
| Copper | Acid | White | Cold |

**Breath Weapon** (a cone or a line, the ancestor's damage; the line on the
sheet is the project's: *"Never exasperate a Dragonborn, for they will sigh and you
will burn."*). **Draconic Flight** at 5: spectral wings made of the same energy
as the breath, ten minutes, once a day. **Darkvision** at sixty feet.

**Silhouettes.** The canon forbids an east/west split: every silhouette is one
tradition's answer. On the two Dragonborn keys that gives two: the Japanese
*ryū* (the serpentine sky-dragon of the `japan` well) and the **feathered
serpent** of the `aztec` well. A Dragonborn of the Aztec well is Quetzalcoatl's
child, and the sheet never says which silhouette a Dragonborn carries: the
colour is the only thing drawn, and the shape is the player's.

---

## 📔 4. Society: the clan that learned its rules by watching

**Three relations to dragons**, all in the entry: *"Some of us follow them as
our rulers, and some of us as masters, and some of us don't follow them
anymore."* The religion around dragons is an imperial cult with a monastic
strand: observance, hierarchy and rite at the level of the state, a genuine
contemplative tradition running through it, and ordinary personal spirituality
beside both. It is not a cargo cult. Christianity and Buddhism are the
parallel: living religions full of people imitating a transcendence they have
not had, and not fraudulent for it.

**The code.** *"How to greet a superior and how to greet an equal, which hand
takes the cup, what is owed to a house that shelters you and what is owed to
one that does not."* Learned from dragons, done for themselves. The cost is
real: expectation crushes people, and a hardness gets demanded of their own.
So is the good: cohesion, service, a house that will not let you fall, "and
the warrior in the garden who watches the trees blossom and does not need to
be anywhere else."

**Isolated and imperial at once.** The two wells are chosen for this: Japan
and the Mexica, each isolationist and imperialist in its own way, as two
distinct keys. The Dragonborn are "quite isolated, and rare to find outside
their lands"; the entry's own question is *why {name} left home*.

**The Dragon Cultists** are the failure case, and they fail on the philosophy
rather than on sincerity: a self authored to someone else's specification is
precisely the thing that has to be overcome. They worship the man who despised
movements. The Dragon Cultist background ("someday you will become your own
Master") is the Ascending misread as a promotion, and its "Secrets of the
Dragon Master" hook (dragons walking among mortals in humanoid bodies) is the
canon's "some come back down" seen by a believer.

**The Ascendant Dragon monks** "use the word Ascending, and they mean it"
(canon). No such subclass exists in 2024; the Orders' Primal devotion *"a
beast that is always described the same way by people who have never met"* is
their slot. An Order with that devotion and a Monk in it is the Ascendant
Dragon school without a subclass, and keeps the rule that nobody explains.

---

## 📜 5. Culture and registers

**Japan.** Katana, yari, folded steel, lacquered silver (Materials). The
codified clan society, the garden warrior, the *matagi* bear-hunters
(Ranger), *yabusame* mounted archery, the karakuri (Artificer), Noh's mask
worn by the god (Bard, Glamour), Goemon the thief (Rogue: the Dragonborn Rogue
is the noble thief, not the shinobi, because the canon gives the ninja to the
Monk).

**Aztec.** Macuahuitl, obsidian (Materials). The eagle and jaguar knights
(the Aztec knightly orders: the jaguar is unspent vocabulary and belongs to the
Monk before the Barbarian), the *telpochcalli* (the commoners' warrior school:
the Fighter), *flower and song* as the Nahua name for poetry and for the only
truth on earth (the Bard; the Cleric ledger already carries *"Flower and song:
that is our offering"*), the *nahual* (the animal double one is born to: the
Draconic Sorcerer's Aztec face), Nezahualcóyotl the poet-king ("Not forever on
earth: only a little while here", already in the ledger).

**Legend registers.** `eragon_dragons` is dragon-*side* vocabulary (Rider's
Blade, Oath-Sworn Blade, Wyrmrider's Greatblade). `wyrm_myth` is *anti*-dragon
vocabulary (Dragonslayer, Wyrmbane, Hoard-Cleaver, Serpent's Bane), held by the
Dragonborn and Kobolds: the dragons carry the weapons made for killing them.
The brief leaves it open with three ways out (leave it as a story; give it to
the Goliaths; split it); the Ranger page offers a fourth (the Ranger holds it
by Guild, as the class of the named quarry). By the loaded-names rule, a
Dragonborn drawing a *Wyrmbane* is a kinslayer or a trophy-taker, which is
good either way.

**Names.** *Dragons are not born, they become.* Some Dragonborn keep the
culture of their ancestors and carry their names; the Draconic tongue's
morphemes are in the file (*ji* wing, *kan* to wing; *-on*, *-lon*, *-ion*
dragonkin masculine; *-in*, *-lin*, *-jin* feminine). The canon in the name
file is the same canon as the Documenta, which is how it should be.

**Prayers.** *Clan. Honor. Duty.* and *Your word is your bond* are the code as
faith. *Fire spreads. We gather around it* (Light) is the garden warrior's
hearth. Repair: War's *"Life is a long battle.."* carries a double stop.

---

## 📔 6. Metaphysics: the Dragonborn and the classes that touch the Ascending

The Dragon canon runs through more classes than any other principle in the
setting, and the Dragonborn is where they all land.

| Class | The Dragonborn in it | The Ascending, unspoken |
|---|---|---|
| **Barbarian** | "A dragon has no rules." The Dragonborn who stopped translating. The World Tree's "if you can see through the veil, you can cross it" is the only Path text about crossing. | The roster's quietest Ascending candidate. |
| **Sorcerer** | Two sets of wings: Draconic Flight at 5 (species), Dragon Wings at 14 (Draconic Sorcery, lasting until dismissed). **Decided (the author, general rule): the Sorcerer's ancestry is the species' ancestry, one draw, one colour.** | The mini-Ascension, then something more. |
| **Monk** | The most literal ninja on the roster; the Aztec jaguar knight. The Ascendant Dragon is an Order devotion, not a subclass. | The canon's own monks, "and they mean it". |
| **Wizard** | The Wizard's register is the Dao De Jing, and the Laozian dragon speaks "in parables and weather". The entry complains that dragons speak in riddles nobody should waste a life translating; the Dragonborn Wizard translates. | The clan's translator, reading the idiom the clan refuses. |
| **Bard** | Flower and song; the clan's one licensed liar; and the Mythopoeic loop ("the story changes the next dragon born out of it"): a Dragonborn Bard's tale about a dragon changes the next dragon. | The Bard operates the mechanism from outside. |
| **Cleric** | The watcher is the clan, not the dragon: "a dragon owes nobody anything… is not kind in any way that serves others." *Clan. Honor. Duty.* | The Dragonborn Cleric knows the dragon is not listening. |
| **Paladin** | The class in species clothing: the code as oath, "which hand takes the cup". Expectation is the cost. | An oath is the one thing a dragon never gives. |
| **Warlock** | A Dragonborn signing with a dragon is the cult made personal; the Great Old One as an Ascended dragon's label on its hoard is one reading, never confirmed. | "You, mine." as a hoard tag. |
| **Artificer** | A civilisation built by observing; the Battle Smith who observed a dragon and built a friend shaped like one. | Draw the Defender's form; never say dragon. |
| **Druid** | Shinto's kami on the `japan` key: every place has its spirit, and the code extends to how you greet a river. | The Land Circle as etiquette. |
| **Ranger** | The matagi; yabusame. | The named quarry, and the slayer's words (§5). |
| **Fighter** | The telpochcalli; "a hardness gets demanded of their own." | The training society made a school. |
| **Rogue** | Goemon, Huehuecóyotl. Not the shinobi. | The clan's one unlicensed liar. |

**Dragon versus giant.** The myth layer sets Dragonborn and Goliaths against
each other: the dragon-slaying knight is a Goliath story about a Dragonborn
(`arthuriana`). A Goliath with dragon magic is the myth's defector; a
Dragonborn Ranger holding `wyrm_myth` is the slayer from inside the family.

**The Couatl** (the author, Aasimar page). A dragon bound to an Ideal, or an Ideal
that came to wear a dragon's shape: the Celestial Dragons. The Dragonborn are
the people who would recognise a Couatl as *both* things, and would not say so.
See [Celestials.md](Celestials.md) §6.

---

## 📔 7. Backgrounds

- **Dragon Cultist.** The species' own background and its failure case (§4).
  The cultist Dragonborn is the one who could ask the dragon directly and
  chose the cult instead. The Dragon Cultist Sorcerer "who is actually
  changing" and the Dragon Cultist Bard "making the dragon they worship" are
  the two sharpest readings on the roster.
- **Stranger.** The emigrant from an isolated empire: "a language fewer people
  speak each year" is Draconic outside the clan-lands; "the rites that were
  made illegal" are the observances quietly stopped. The entry's closing
  question and the background's hook are one story.
- **Herald.** The clan's envoy; etiquette as diplomacy; "harming a herald is
  how small quarrels become wars" in a society that keeps score of what is
  owed to a house.
- **Squire.** "Greatness has logistics." The Squire who served a dragon in a
  humanoid body and never knew.
- **Servant.** The imperial court's sideboard, with a code of who pours for
  whom.
- **Guardian.** "A house that will not let you fall", as a job.
- **Sellsword.** ⚠️ The masterless-samurai cliché lands here. The register
  rescues it only if the Sellsword Dragonborn is Aztec: the mercenary of the
  flower wars.
- **Naturalist.** "A dragon's fang… what is left on the ground after a hard
  night is, to the right buyer, a spell component." A Dragonborn selling
  dragon parts to collectors: a story with teeth.
- **Archaeologist.** The codices; "the marks on the lintel copied exactly,
  including the ones you cannot read yet." The Dragonborn Archaeologist reads
  the old clan-lands' walls.
- **Debunker.** The cult debunked from inside: "there is always a reasonable
  explanation" for dragons walking among mortals, and there is not.
- **Survivor.** "It let you go." On a Dragonborn, the thing that let go may
  have been a dragon, which owes nobody anything and did not have to.
- **Official.** Noble is the one the generator reaches for and it is one
  sentence.

---

## 📜 8. Decisions log

**Standing (canon)**

- Never explain the Ascending on the page. A dragon owes nobody anything. The
  Dragonborn are not a joke and not a failure: play the dignity, the cost and
  the nearness together. No east/west split.

**Decided (the author, 2026-09-08, general)**

- Species-and-subclass synergies are drawn as one where they share a source:
  the Draconic Sorcerer's ancestry is the Dragonborn's ancestry.
- Physical traits are biological; the species law guards against monoculture,
  not against Breath Weapons.

**Open**

- **`wyrm_myth`**: leave it as a story, give it to the Goliaths, split it, or
  give it to the Ranger by Guild. The brief's own question, with a fourth
  option from the Ranger page.
- **Darkvision**: chip-only here and on the Aasimar, printed elsewhere. the author
  decided the Aasimar prints with a line; the same convention applied here
  would want a line (§9).
- **Draconic Flight has no line**, and it is the canon's tell. A line that
  hints and never names (§9).
- **The Ascendant Dragon** as an Order devotion: a note in the Dragon canon
  pointing at `Map_of_Traditions` so nobody mints a subclass for a slot the
  Orders fill.

**Repairs**

- Prayer ledger, Dragonborn × War: *"Life is a long battle.."* (double stop).

---

## 📖 9. Lines

*Proposals. Second person, the clan's plain register (the entry's "we" becomes
the sheet's "you" in the traits), no proper nouns, no em-dashes. The Breath
Weapon's saying is the project's and stands.*

| Entry | Line |
|---|---|
| **Darkvision** | *A dragon sees in the dark. So, a little, do you.* |
| **Draconic Ancestry** | Keep the current sentence (it names the colour and the damage; that is the whole feature). |
| **Breath Weapon** | Keep: *An ancient saying: Never exasperate a Dragonborn, for they will sigh and you will burn.* |
| **Draconic Flight** | *The ones who stayed home never grew these. You did not ask why. You went.* |

The Flight line is the closest the sheet may come to the tell: it says the
wings came with leaving, and stops.

---

## 📚 10. Pointers

- **Dragon canon**: add the Couatl and the Ascendant Dragon's Order slot.
- **Goliath page**: dragon versus giant; the slayer's words.
- **Sorcerer page**: the ancestry synergy.
- **Monk page**: the jaguar knight; the Ascendant Dragon Order.
- **Cultural Inspirations**: `wyrm_myth`, and the two silhouettes.

---

## 📔 12. Breath Weapon

The one trait that opens on a rule with no line of its own:

| Trait | Line |
|---|---|
| Breath Weapon | *Everything you were taught to hold in, let out once, at something.* |
