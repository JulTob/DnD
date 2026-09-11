# 🌿 Druid: the Lent, read against the whole setting

> 📖 **In flow.** 2 of 8 chapters are still proposals. 📜 0 · 📚 3 · 📔 3 · 📖 2

*Mythos analysis, 2026-09-08. Design and literary criticism, not page text. Builds
on Dialog 0017 (core fantasy settled as the elder belonging, sharpened to
membership maintained through attention; the register is the walker's field
diary; Land keeps the covenant, Moon is change that stays itself, Sea signs
nothing, Stars is the wilderness overhead). This page does not re-litigate
that. It reads the Druid against the peoples and backgrounds, names the wells
the dialog left, records what the generated sheets actually do, and drafts the
feature lines. Nothing here is landed.*

**Where the text lives.** Class and Circle paragraphs: Dialog 0017's five
texts, provisional and unwired; `AtlasOfGuilds/DruidKit.py` is four bare
calls. Lessons: `AtlasOfTraining/Map_of_Druid_Training.py` (rules only, no
lines). A 2014-era layer in `Map_of_Classes/Training/Druid.py` still emits
*Number of Wild Shape*, *Known Forms of Wild Shape*, *Wild Shape: Rules While
Transformed*, and its own *Primal Order*. Seat in the theology table: **owed**
(from the Orders' Primal devotion, "the land itself, which is owed and does
the owing").

---

## 📚 1. What a Druid player is handed today

Four sheets were generated (Elf Land, Goliath Moon, Halfling Stars, Orc Sea).
All four: no class text, no Circle text, no line above any feature, and the
2014 layer beneath the 2024 one. Three findings that are not in the dialog:

1. ⚠️ **Two Primal Orders on one sheet.** The 2024 feature says *Primal
   Order: Magician*; a legacy feature with `source=None` says *Primal Order:
   Warden* (Elf, Goliath). The Orc has it the other way round. The legacy map
   draws its own Order from its own dice. A reader sees a contradiction in the
   first six entries. Three of four sampled sheets.
2. ⚠️ **The forms are never drawn.** *"You know four Beast forms for Wild
   Shapes chosen from among Beast stat blocks that have a maximum Challenge
   Rating of 1/2."* Open-choice language (Feature-Text canon), and worse: the
   dialog's whole class thesis is *"You watched the wolf until you could be
   the wolf. Every form you wear was learned like a friendship."* A sheet with
   no wolf on it cannot carry that sentence. The forms *are* the fantasy.
3. ⚠️ **Em-dashes in four rules entries** (Land's Aid, Wrath of the Sea,
   Cosmic Omen, Star Map).

The dialog's texts are excellent; the sheet today is a rules list with a
contradiction in it.

---

## 📚 2. The forms are the vocabulary, so draw them

Proposal, not landed. Wild Shape says the forms are *learned*; the generator
should learn them for the Character, the way it draws a Background's tool or
an Aasimar's Ideal. Four forms at level 2, seated once, growing with the
Circle's CR cap. The pool should be keyed the way everything else in the
project is keyed: **species culture and Circle terrain**.

| Key | Four forms | Why |
|---|---|---|
| default | wolf, hawk, bear, salmon | The Wild Heart's own lists (Bear, Eagle, Wolf, Owl, Panther, Salmon) already exist in the Barbarian map and can be reused as a pool |
| `celt`, `fairytale_fae` (Elf, Fae) | hare, salmon, wren, otter | The Taliesin chase, which the dialog names as the Moon's master text |
| `norse` (Elf) | wolf, bear, raven, seal | Odin's animals and the selkie |
| `aztec` (Dragonborn) | jaguar, eagle, coyote, hummingbird | The two knightly orders, and the sun's bird |
| `japan` (Dragonborn) | fox, crane, boar, carp | The kitsune and the koi that climbs the waterfall |
| `iberia`, `andalus` (Dwarf) | bear, lynx, ibex, stork | The Cantabrian bear, the Iberian lynx |
| steppe by temper (Orc) | horse, wolf, steppe eagle, marmot | The rider's animals |
| `africa`, `egypt` (Human) | lion, ibis, crocodile, jackal | The Nile's gods as beasts |
| Coast / Sea Circle | seal, gull, octopus, dolphin | |
| Underdark | bat, giant spider, cave fish, salamander | |

✅ The pool is the culture network's idea applied to Wild Shape, which is the
same move the exotic familiars already make with *Familial Preference*. It
also fixes the open choice, and it puts a wolf on the sheet under the
sentence about the wolf.

---

## 📚 3. Wells the dialog did not draw from

The dialog's shelf is long and good. These add *places* the culture map
already holds.

**Caesar's druids.** "They think it improper to commit their studies to
writing." That sentence is the Orders' Primal practice (*"nothing is written;
it is walked, and shown, and walked again"*), and the historical druid is
`celt`, which is an Elven key. ✅ In this setting the druid *as an
institution* is Elven; a Human Druid is a druid by trade, an Elf Druid by
culture. Druidic, the secret language, has an Elven home and an Elven prayer
already in the ledger (*"We live in one another's shadow"*, Irish).

**The Basajaun** (`iberia`; the wiki gives the Mountain Dwarves a Basque
inspiration). The lord of the woods, a hairy giant who guards flocks, warns
shepherds of storms, and taught humans to farm and to forge. ✅✅ A wild man
who *teaches*, on a Dwarf key, and who is the Wild Heart's Enkidu with the
tragedy reversed: Enkidu was tamed by the city; the Basajaun tamed the
farmers. A Dwarf Land Druid is his pupil, and the Dwarf entry's "Then the
Great Mountain fell" becomes the covenant's breach seen from the Dwarf side.
Beside him, **Mari of Anboto**, the Basque lady of the mountain who is the
weather: the Dwarf Sea or Storm Druid's well.

**Shinto's kami** (`japan`, Dragonborn). Every place has its spirit, and the
relationship is exactly the Land text's *"a place notices being known"*. A
Dragonborn Land Druid needs no new lore: the codified clan society "of rules"
extends to how you greet a river.

**The Sothic year** (`egypt`, Human). The rising of the dog star announced
the flood. The Stars Circle's almanac is Hesiod in the dialog; it is also the
Nile's calendar, and a Human Stars Druid reads the sky for the water.

**Zhuangzi's butterfly** (`china`, Fae). "I do not know whether I was a man
dreaming I was a butterfly, or am now a butterfly dreaming I am a man." ✅ The
Moon Circle's koan, from the Fae's own well: change that stays itself,
without the Western anxiety about losing the man in the hawk. A Fae Elf Moon
Druid has the calmest relationship with Wild Shape on the roster.

**Actaeon** (Ovid). The watcher turned into the stag by the moon-goddess, and
torn by his own hounds. The Moon Circle's Moonbeam already "forces false
shapes to confess"; Actaeon is what it does to the *watcher* who should not
have looked. The Moon's teeth, which the dialog kept, have a name.

**Ahab.** The one who tried to make the sea owe him. The Sea Circle's Ajax:
the failure mode of loving a wild that signs nothing is demanding a
signature. Hemingway's old man is the success case; Ahab is the warning, and
the Sea text's "with no hatred in it anywhere" is the line that keeps the
Druid on the right side of it.

**Al-Sufi's *Book of Fixed Stars*.** The Stars Druid's constellations carry
Arabic names, like the Aasimar's stars. The oldest literacy in the dialog's
phrase was, for the star catalogue this setting inherits, Arabic. `levante`
is a Goblin key. The sky is the one wilderness the Goblins named.

---

## 📔 4. The Druid inside the setting's metaphysics

**The Elves are Druids at species scale.** Canon: *"Dream of the forest for a
thousand years and you become a Wood Elf."* The dialog's class close: *"Keep
such company long enough and you begin to keep its calendar… So, in time,
will you."* ✅ Archdruid's slowed ageing is the Dream's drift, in one life,
on purpose. An Elf Druid is doing consciously what the species does
unconsciously. Never say so. ⚠️ And the Moon Circle changes shape nightly in
a species whose canon says "no elf transforms in a scene, and no elf
transforms alone". Wild Shape is a learned form, not a lineage drift, so the
rule is not broken; but an Elf Moon Druid's elders will *think* it is, which
is a story the Elf page should keep.

**The Goliath is talking to relatives.** *"The First Ones kept the world,
having never stopped being it. They are still here, if you know how to look
at a mountain."* ✅ The elder society the Druid never left is, for a Goliath,
literally the family. The Order of Things is the covenant. "Do you respect
and protect the land?" is the Land Circle asked by the species entry.

**The Orc is the covenant's plaintiff.** *"Then the dwarves came for the gold
underneath, the humans came to call it discovery, and the elves promised
trade and brought curses. No orc was asked."* The Land text's *"what may be
taken, what must be left"* is the Orc grievance as doctrine. ✅ And the Orc
Sea Druid (seed 31) found the one plain that cannot be fenced: the sea signs
nothing, and neither did the Orcs. The best species-Circle pairing on the
roster, and the generator found it by itself.

**The Dwarf owes the mountain.** *"Everything we dwarves ever built, we built
while chasing it: the mines."* Stonecunning is attention paid to stone. A
Dwarf Druid is the mountain's creditor among a people of debtors, and the
Basajaun (§3) is the teacher. The Great Mountain fell; somebody remembers
what it was owed.

**The Gnome owns nothing in land.** *"Your own keep their ways in things
rather than in land, because land can be taken."* ✅ Tension: the Druid's
craft is a place; the Gnome's wisdom is to carry your world in your pocket.
A Gnome Land Druid has chosen the one thing their grandmother said never to
love. A Gnome Stars Druid has found the one place that cannot be taken.

**The Halfling never had to ask.** The valley's soil "so generous nobody has
gone hungry in living memory". A Halfling Druid grew up inside a covenant
nobody negotiated, and the Stars (seed 29, *Apricot Pecan*) are the valley's
only wilderness: up.

**The Tiefling and the land that does not read horns.** *"A diaspora with no
homeland to be exiled from."* ✅ A Tiefling Land Druid chose a place and was
accepted by it when no people would. "A place notices being known" is the
first welcome the species entry ever describes without a fine attached.

**The Dragon's reserved ground.** The dialog kept self-authorship out of the
Druid; the forms are learned, not realised. One canon line should stay in
mind: *"Some come back down… will resume a humanoid shape."* A dragon in
mortal shape is Wild Shape in reverse, and a Moon Druid who can become an
Elemental at 10 is "not even flesh limits the vocabulary". The two never
touch on the page.

---

## 📔 5. Relationships: backgrounds × Druid

- **Herald × Sea** (seed 31). *"A herald carries power that is not their own:
  a council, a temple, a patron, a forest…"* ✅✅ The background lists **a
  forest** among the powers that send heralds. The Herald Druid is the elder
  society's ambassador, and the Herald *Sea* Druid is the ambassador of a
  power that signs nothing: "it comes home with you or it does not come home
  at all", with no treaty in the satchel. Nobody wrote this pairing; it is the
  best accident since the Servant of Mercy.
- **Naturalist.** *"With a board across your knees and the light already
  going… you picked up a little of what you were studying."* ✅ The dialog's
  register *is* this background: the walker's field diary. The Naturalist
  Stars Druid's Star Map is their plates. Reinforcement so exact it should be
  nudged apart by affinity so the generator does not say it twice.
- **Wildkeeper.** *"You did not tame anything. You stayed."* The class's own
  background; the Land Circle twice. ⚠️ Redundant; the interesting Wildkeeper
  is a Rogue or a Bard.
- **Archaeologist.** *"The marks on the lintel copied exactly, including the
  ones you cannot read yet."* ✅ Druidic: *"letters waiting for you out there,
  left in leaf and stone by people you will never meet."* The Archaeologist
  Druid can read the lintel. The Archaeologist who is not a Druid has been
  copying Druidic for years without knowing.
- **Stranger.** *"The true names, the rites that were made illegal… None of
  it was ever written down."* ✅ Druidic as the grandmother's tongue; the
  Stranger Druid is the last speaker, and the Orders' Word domain has a facet
  for exactly this ("the Last Speaker").
- **Fated × Land** (seed 23). *"A rope you did not tie gives way… milk
  spoils."* ✅ The land notices being known; does it notice the curse? A Land
  Druid whose covenant is with a place that keeps breaking around them.
  Nature's Ward says "poison forgets your name"; the Jinx says it does not.
- **Debunker × Moon** (seed 27). *"There is always a reasonable explanation."*
  ✅ The reasonable explanation for the wolf at the window is the Debunker.
- **Survivalist.** *"Rescue never came, so you learned to be your own."* The
  Druid without the friendship: survived the wild before befriending it. The
  hard version of the class.
- **Ice Nomad.** Arctic Land. *"The ice let you go."* The Land Druid whose
  land is the one that let go.
- **Exorcist.** *"A spore."* The Underdark Land Druid against what grows in
  the dark; or the Druid who knows the spore was only being a spore.
- **Tomb Raider.** Underdark; "which wall was built to keep something in
  rather than someone out". The land under the land.
- **Servant, Gambler.** The Druid in a drawing room: "Fog follows you like a
  dog" at a card table. Underrated.
- **Official backgrounds.** Guide (*Magic Initiate: Druid*, one sentence),
  Farmer (*Rustic Hospitality*, one sentence), Hermit, Sailor. ⚠️ The
  Druid's three most natural official backgrounds are the three thinnest
  texts on the roster (Cleric page §8).

---

## 📔 6. Flags

### ✅ Singular, and to be protected

1. **The class close.** "Mountains count in winters. Forests count in
   centuries. So, in time, will you." The Fighter precedent holds; keep it.
2. **"Fog follows you like a dog. Thunder waits behind your teeth."** The Sea
   text's two best sentences; the register at its warmest.
3. **The Moon's teeth**, and Actaeon behind them (§3).
4. **Starry Form spends Wild Shape**: the constellations are the class's
   beasts. The dialog's structural finding; the Stars line should say it.
5. **The Orc Sea Druid and the Herald of a forest** (§4, §5): two pairings
   the dice found and nobody wrote.
6. **The Basajaun** (§3): a teaching wild man on a Dwarf key, and the Wild
   Heart's missing cousin.

### ⚠️ Stock, contradictory, or thin

1. **Nothing is wired; no lines; the 2014 layer leaks** (§1).
2. **Two Primal Orders on one sheet** (§1). A visible contradiction.
3. **The forms are never drawn** (§1, §2). The fantasy's vocabulary is an
   open choice.
4. **Four em-dashes** in rules text.
5. **Wildkeeper and Naturalist** say the class twice; nudge by affinity.
6. **The Land's terrain** is re-chosen per Long Rest and may stay open, but
   the *current* one should be seated (the sheet knows what country it was
   generated in only if it says so).
7. **The official backgrounds** most natural to the class are the emptiest.

---

## 📖 7. Feature lines: drafts

*Italic inspiration line only. Register: the walker's field diary, concrete
senses, warmth without awe, no proper nouns, no dice, no em-dashes. Rule text
untouched except the em-dashes. Proposals.*

### Core lessons

| Lesson | Draft |
|---|---|
| **Spellcasting** (1) | *Most of it is listening. The rest the world does for you, because you asked the way it likes to be asked.* |
| **Druidic** (1) | *Letters in leaf and stone, from people you will never meet, in a language the cities never learned.* |
| **Primal Order: Magician** (1) | *You went further into the asking.* |
| **Primal Order: Warden** (1) | *You went further into the standing.* |
| **Wild Shape** (2) | *You watched until you could be the thing you watched. The wild lends its bodies the way a friend lends a coat.* |
| **Wild Companion** (2) | *The older house sends you company from its own.* |
| **Wild Resurgence** (5) | *Speaking with the wild and wearing it turned out to be one currency.* |
| **Elemental Fury** (7) | *Whichever hand you use, the same world is behind it.* |
| **Improved Elemental Fury** (15) | *The world behind your hand has grown heavier.* |
| **Beast Spells** (18) | *You kept your speech inside the borrowed body. The two halves of the craft stopped being halves.* |
| **Archdruid** (20) | *Mountains count in winters. You have started to.* |

### Circle of the Land

| Feature | Draft |
|---|---|
| **Circle Spells** (3) | *Each country teaches its own way of answering.* |
| **Land's Aid** (3) | *The ground feeds its own and turns on the rest, in one gesture.* |
| **Natural Recovery** (6) | *Rest in a place you have learned and it gives you back your reach.* |
| **Nature's Ward** (10) | *Poison forgets your name. Fear finds nothing in you to hold. Green things part.* |
| **Nature's Sanctuary** (14) | *Even the beast, even the briar, turns aside from the one who remembered the terms.* |

### Circle of the Moon

| Feature | Draft |
|---|---|
| **Circle Forms** (3) | *Not even flesh is the limit of the vocabulary.* |
| **Moon Spells** (3) | *The night's whole company: silver, and teeth.* |
| **Improved Circle Forms** (6) | *Moonlight in the claw.* |
| **Moonlight Step** (10) | *You move the way light moves.* |
| **Lunar Form** (14) | *Phases do not destroy the moon.* |

### Circle of the Sea

| Feature | Draft |
|---|---|
| **Sea Spells** (3) | *You came back with its weather in you.* |
| **Wrath of the Sea** (3) | *You do not aim the sea. You stand in it, and it happens around you.* |
| **Aquatic Affinity** (6) | *The border opened. Breath, and speed, and the cold not minding you.* |
| **Stormborn** (10) | *A storm spares its own.* |
| **Oceanic Gift** (14) | *One water. It feeds your people and breaks what stands against them, with no hatred in it anywhere.* |

### Circle of Stars

| Feature | Draft |
|---|---|
| **Star Map** (3) | *You watched until the watching became a map.* |
| **Starry Form** (3) | *The sky lends its figures the way the forest lends its beasts: from a higher pasture, by the same friendship.* |
| **Cosmic Omen** (6) | *Read the sky at rest. Then tell luck which way to lean, a breath before it lands.* |
| **Twinkling Constellations** (10) | *The figures burn brighter for being read.* |
| **Full of Stars** (14) | *Watch anything long enough, with enough love, and you take on its nature.* |

---

## 📖 8. Threads to pull in later cycles

- **Elf page**: the species as Druids at scale; the Moon Elf's elders.
- **Dwarf page**: the Basajaun and Mari; the mountain's creditor.
- **Orc page**: the Sea Druid as the unfenced plain.
- **Ranger**: the Druid notices; the Ranger *hunts*. Decide which Guild owns
  the field diary before the Ranger page (Beast Master and the Beast domain
  of the Orders are the pressure points).
- **Barbarian, Wild Heart**: the Basajaun as the teacher the Path lacks.
- **Rules work outside this page**: the Primal Order double, the forms draw,
  the em-dashes.


