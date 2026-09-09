# 🐉 Dragonborn

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from `Dragons-and-the-Overcoming.md`, the Dragonborn kit,
`AtlasNomina/Races/Dragon.py`, the class analyses and Julio's notes. The Dragon
canon's first rule governs every line here: never explain it on the page.*

> **In one sentence.** The children of dragons, and none the wiser for it: a
> people who built a civilisation of rules by watching beings who kept none,
> and who stand nearer than anyone to the thing the dragons did, without ever
> being told so.

---

## 1. Where the Dragonborn lives in the code

| What | Where | State |
|---|---|---|
| Species entry (Julio's) | `AtlasActorLudi/SpeciesKit/Dragonborn/__init__.py` | Shipping. First person plural ("we"), the clan's voice. Closes on "which observance you have kept, and which one you have quietly stopped keeping." |
| Ancestors | `Dragonborn/Map_of_Ancestors.py` | Ten colours, five damage types, drawn once and kept. |
| Traits and rules | `Dragonborn/traits.py`, `resolution.py` | Reference kit for voice (QST-0062). Breath Weapon carries a line; Draconic Ancestry names the colour and its damage; Darkvision is chip-only; Draconic Flight has no line. |
| Names | `AtlasNomina/Races/Dragon.py` | Opens with the canon in one sentence: "Dragons are not born, they become." Draconic morphemes (*ji* wing, *-on* / *-in* dragonkin). Inspirations: real dragons, Chinese, Japanese. |
| Culture keys | `japan`, `aztec`; legends `eragon_dragons`, `wyrm_myth` | Two distinct wells, never fused. `wyrm_myth` is an open question (§5). |
| Prayer | `Map_of_Cleric_Prayers.py` | *Clan. Honor. Duty.* *Your word is your bond.* Light: *Fire spreads. We gather around it.* War: one typo. |
| Canon | `Documenta/Canon/Dragons-and-the-Overcoming.md` | The Ascending; the rules for writing dragons. |

---

## 2. Origin: what a dragon is, and what a Dragonborn is not

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

## 3. The vessel: physiology

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
sheet is Julio's: *"Never exasperate a Dragonborn, for they will sigh and you
will burn."*). **Draconic Flight** at 5: spectral wings made of the same energy
as the breath, ten minutes, once a day. **Darkvision** at sixty feet.

**Silhouettes.** The canon forbids an east/west split: every silhouette is one
tradition's answer. On the two Dragonborn keys that gives two: the Japanese
*ryū* (the serpentine sky-dragon of the `japan` well) and the **feathered
serpent** of the `aztec` well. A Dragonborn of the Aztec well is Quetzalcoatl's
child, and the sheet never says which silhouette a Dragonborn carries: the
colour is the only thing drawn, and the shape is the player's.

---

## 4. Society: the clan that learned its rules by watching

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

## 5. Culture and registers

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

## 6. Metaphysics: the Dragonborn and the classes that touch the Ascending

The Dragon canon runs through more classes than any other principle in the
setting, and the Dragonborn is where they all land.

| Class | The Dragonborn in it | The Ascending, unspoken |
|---|---|---|
| **Barbarian** | "A dragon has no rules." The Dragonborn who stopped translating. The World Tree's "if you can see through the veil, you can cross it" is the only Path text about crossing. | The roster's quietest Ascending candidate. |
| **Sorcerer** | Two sets of wings: Draconic Flight at 5 (species), Dragon Wings at 14 (Draconic Sorcery, lasting until dismissed). **Decided (Julio, general rule): the Sorcerer's ancestry is the species' ancestry, one draw, one colour.** | The mini-Ascension, then something more. |
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

**The Couatl** (Julio, Aasimar page). A dragon bound to an Ideal, or an Ideal
that came to wear a dragon's shape: the Celestial Dragons. The Dragonborn are
the people who would recognise a Couatl as *both* things, and would not say so.
See [Celestials.md](Celestials.md) §6.

---

## 7. Backgrounds

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

## 8. Decisions log

**Standing (canon)**

- Never explain the Ascending on the page. A dragon owes nobody anything. The
  Dragonborn are not a joke and not a failure: play the dignity, the cost and
  the nearness together. No east/west split.

**Decided (Julio, 2026-09-08, general)**

- Species-and-subclass synergies are drawn as one where they share a source:
  the Draconic Sorcerer's ancestry is the Dragonborn's ancestry.
- Physical traits are biological; the species law guards against monoculture,
  not against Breath Weapons.

**Open**

- **`wyrm_myth`**: leave it as a story, give it to the Goliaths, split it, or
  give it to the Ranger by Guild. The brief's own question, with a fourth
  option from the Ranger page.
- **Darkvision**: chip-only here and on the Aasimar, printed elsewhere. Julio
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

## 9. Lines

*Proposals. Second person, the clan's plain register (the entry's "we" becomes
the sheet's "you" in the traits), no proper nouns, no em-dashes. The Breath
Weapon's saying is Julio's and stands.*

| Entry | Line |
|---|---|
| **Darkvision** | *A dragon sees in the dark. So, a little, do you.* |
| **Draconic Ancestry** | Keep the current sentence (it names the colour and the damage; that is the whole feature). |
| **Breath Weapon** | Keep: *An ancient saying: Never exasperate a Dragonborn, for they will sigh and you will burn.* |
| **Draconic Flight** | *The ones who stayed home never grew these. You did not ask why. You went.* |

The Flight line is the closest the sheet may come to the tell: it says the
wings came with leaving, and stops.

---

## 10. Pointers

- **Dragon canon**: add the Couatl and the Ascendant Dragon's Order slot.
- **Goliath page**: dragon versus giant; the slayer's words.
- **Sorcerer page**: the ancestry synergy.
- **Monk page**: the jaguar knight; the Ascendant Dragon Order.
- **Cultural Inspirations**: `wyrm_myth`, and the two silhouettes.

---

## 12. Addendum (2026-09-08, appended): the one trait the page left bare

A level-5 sweep found every Dragonborn trait that opens on a rule already
drafted on this page except **Breath Weapon**. For symmetry:

| Trait | Line |
|---|---|
| Breath Weapon | *Everything you were taught to hold in, let out once, at something.* |
