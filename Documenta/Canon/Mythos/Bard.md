# 🎭 Bard: the Told, read against the whole setting

> 📖 **In flow.** 2 of 11 chapters are still proposals. 📜 0 · 📚 2 · 📔 7 · 📖 2

*Mythos analysis, 2026-09-08. Design and literary criticism, not page text. Builds
on Dialog 0015 (core fantasy settled as "the world listens; your art can move
it", with the collector as supporting current and the persona refracted into
Glamour and Dance; the register is the told tale; Lorca's duende guards against
whimsy). This page does not re-litigate that. It finds that the setting makes
the Bard's thesis literally true, follows the Muses thread the Aasimar page
opened, names the instrument gap, and drafts the feature lines. Nothing here is
landed.*

**Where the text lives.** Class and College paragraphs: Dialog 0015's five
texts, provisional and unwired; `AtlasOfGuilds/BardKit.py` is four bare calls.
Lessons: `AtlasOfTraining/Map_of_Bard_Training.py` (rules only, no lines, and
five open-choice or retraining clauses the canon says to cut). A 2014-era layer
in `Map_of_Classes/Training/Bard.py` prints the four College paragraphs from the
2024 rulebook *verbatim*, with `source=None`. Instruments: none drawn, none
named; `Ledger_of_Tools` holds one generic "Musical Instrument" category. No
legend register of its own.

---

## 📚 1. What a Bard player is handed today

Four sheets (Aasimar Dance, Gnome Lore, Dwarf Valor, Elf Glamour). No class
text; no College text of the project's; every College entry is the rulebook's
paragraph word for word ("Bards of the College of Dance know that the Words of
Creation can't be contained within speech or song…"); *Expertise* says "Choose
two skills" twice; *Bonus Proficiencies* says "three skills of your choice";
*Magical Discoveries* and *Magical Secrets* say "of your choice" and "you can
replace"; and nowhere on any of the four sheets is there an instrument.

⚠️ **The verbatim rulebook paragraphs are the first thing on this roster that
is an IP question rather than a voice question.** The Vademecum says
IP-adjacent design "always opens a discussion first". Four paragraphs of the
2024 PHB are on the product sheet under a heading. Retire them when 0015's
texts land, and before that if the sheet ships.

---

## 📔 2. In this setting, the world really does listen

Dialog 0015's thesis is *art as literal power*. It reached that by reading the
rules. The setting's canon reaches it from the other side, three times, and
nobody has yet put the two together.

1. **The Dragon canon.** *"A single sighting births generations of myth. The
   story changes the people who tell it, and that story changes the next
   dragon born out of it."* The Mythopoeic position ("the story is
   everything") is one of the five dragon positions. The shape of the next
   dragon is decided by what the tellers told.
2. **The Elf canon.** *"Every legend the people tell shapes them a little."*
   The lineages are collective drift, and the drift is fed by story.
3. **The Celestial canon.** Celestials "change only as mortal understanding of
   the Ideal changes" (QST-0050), and belief is "the fuel from which
   celestials emerge"; run backward, belief made the Lower Planes lower "by
   being called it" (Tiefling canon).

✅✅ **The Bard is the class that operates the setting's three plastic
metaphysics from the outside.** A Bard's tale about a dragon changes the next
dragon. A Bard's ballad about the woods drifts the Wood Elves. A Bard's hymn
moves an Ideal, and a Bard's satire is how a heaven becomes a hell. In most
settings the Bard is support. Here the Bard is the engine of the cosmology's
plasticity, and the Cleric's "something watching over you" is downstream of
what Bards have been singing for centuries. Words of Creation at 20 is not a
metaphor in this world; it is the job description arriving.

None of this goes on a sheet. It goes in the canon, one paragraph, so that the
next author of a Bard text knows the stakes and does not write whimsy. It also
answers 0015's open question 2 (Words of Creation is verbal even for the
dancer): in a world where belief makes gods, the deepest layer of every art is
the *Word*, and the dialog was right to find that beautiful.

---

## 📔 3. The Muses: two open slots

The Aasimar's Ideals each answer to a Muse (`Map_of_Ideals.py`): Justice to
History (Clio), Sacrifice to Tragedy (Melpomene), Truth to Astronomy (Urania),
Beauty to Love Poetry (Erato), Hope to Comedy (Thalia), Honor to Epic
(Calliope), Mercy to Sacred Song (Polyhymnia). Freedom answers to nobody, by
design. That leaves **Euterpe** (music, lyric) and **Terpsichore** (dance)
unassigned, and Muses are Celestials, and the Bard is the Muses' class.

✅ **Two Ideals are waiting to be named, and the Bard is the class to name
them.** Candidates, offered in the shape the map already uses
(alignment-independent, twistable, tell never naming the Ideal):

| Ideal | Muse | Form of the aureola | Metal / gem | Tell |
|---|---|---|---|---|
| **Grace** | Euterpe | a soft line that follows the shape of your head like a second hairline of light | pale gold / pearl | *It steadies when you are forgiven, and it does not care whether you deserved it.* |

**Terpsichore belongs to Freedom, and Dance is Freedom's college.** Dance is an
expression of freedom, so the College of Dance is where an Aasimar of Freedom
finds spark and profession in the same place: the compass-rose halo that
"twinkles when you run, and harder when you fly" is its tell. Grace is
twistable in the canon's sense ("grace is what I decide you deserve"), and
Euterpe, music and lyric, holds **Harmony**. Grace is the harder Ideal and
the better one: the setting has Mercy (the open hand) and Hope (the star in
the dark) and nothing for *unearned ease*, which every Bard's art is.

---

## 📚 4. Wells the dialog did not draw from

The dialog's shelf is the longest in the series. These are the ones that sit
on culture keys the setting already assigns, so a species' Bard has a home.

**The skald** (`norse`, Elves). Egil again: sentenced to die at dawn by Eirik
Bloodaxe, he composes *Höfuðlausn*, the head-ransom, overnight, and is spared
for the poem. ✅ Scheherazade with an axe, in the Elves' own well. And the
skald's *níð*, the shaming verse that was legally a weapon, is Cutting Words
in Norse. Kennings are the collector's toolkit: a word made of other words.

**The cantigas** (`iberia`, `andalus`, Dwarves). The Galician-Portuguese
*cantigas de escarnio* are satire as high art; the *Cantigas de Santa Maria*
are a king's own songbook; the *romancero* is the anthology of a whole people
carried by memory. ✅ A Dwarf Lore Bard sings *escarnio* in a bank-cathedral,
and the Dwarf Valor Bard's book is the Cid's, which the dialog already named.
Lorca is Iberian; the duende was always the Dwarf's.

**Flower and song** (`aztec`, Dragonborn). *In xochitl in cuicatl*: the Nahua
name for poetry, and for the only truth on earth. ✅ The Cleric ledger already
carries *"Flower and song: that is our offering"* and Nezahualcóyotl's *"Not
forever on earth"*. A Dragonborn Bard's art has a name in its own culture, and
the poet-king of Texcoco is the Dragonborn Valor Bard: the ruler who was a
singer first.

**The pipa player** (`china`, Fae). Bai Juyi's *Song of the Pipa*: the boat at
night, the fallen court musician playing for strangers. ✅ The Glamour text's
"a court that does not admit mortals twice" has an Eastern face, and it is a
sadder one: the court that let you go.

**Noh** (`japan`, Dragonborn). The mask is not worn by the actor; the god
wears the actor. Glamour's "unearthly appearance" and the Zealot's vessel are
cousins here, and the Dragonborn Glamour Bard is where they meet.

**Tyrtaeus** (`sparta`, Goliaths). The war-elegist whose verses were sung to
the phalanx, which marched to the aulos. ✅ The Goliath Valor Bard is the
dialog's aoidos with the shield line put back in: the Spartans went into
battle to a *flute*.

**The manaschi** (steppe by temper, Orcs). Reciters of the *Manas* epic, half a
million lines, no book. ✅ The Orc Lore Bard is the horde's memory, and the
Orc entry's "No orc was asked" is the first line of that epic.

**Commedia dell'arte** (`italy`, Gnomes). Arlecchino, Pulcinella, the mask,
the *lazzo*, the improvised scene on a fixed skeleton. ✅ The Gnome Glamour or
Lore Bard is the masked improviser, and the Gnome's instrument (§5) is a
hurdy-gurdy, which is a machine.

**The kora** (`africa`, Humans). The griot's twenty-one strings. The dialog
has the griot; the instrument is the Human Bard's (§5).

**Plainchant** (`vatican`, Aasimar). The Celestial familiar already "hums
plainchant". The Aasimar Bard's art is the office sung.

---

## 📔 5. The instrument is the character, and it is never named

⚠️ A Bard sheet never says what the Bard plays. The tool ledger holds
"Musical Instrument (a Flute or Shawm runs 2 GP, a Horn 3, a Drum 6, a Lyre
or Viol 30, a Lute 35)". That is a price list, and the one item on a Bard's
sheet a player would draw a picture of is absent.

✅ **Proposal: `Map_of_Instruments`, keyed by the same culture markers as
`Map_of_Gear_Titles`,** drawn once at level 1 and seated on the sheet as the
Spellcasting Focus. The double mapping already exists; instruments are its
most legible consumer after weapons, because everybody knows what a lute
sounds like and nobody knows what a Kusarigama does.

| Key | Instruments |
|---|---|
| `iberia`, `andalus` | vihuela, guitar, castanets, oud |
| `norse`, `rus` | lyre (kravik), gusli, tagelharpa |
| `mongol` | morin khuur, the throat itself |
| `celt` | harp, bodhrán, uilleann pipes |
| `japan` | shamisen, biwa, shakuhachi, taiko |
| `aztec` | huehuetl, teponaztli, the bone flute |
| `china` | pipa, guqin, erhu |
| `korea` | gayageum |
| `athens` | kithara, aulos, lyre |
| `vatican` | organ portative, the voice in chant |
| `sangha` | the singing bowl, the conch, the khakkhara's rings |
| `sparta`, `homeric` | aulus, salpinx, phorminx |
| `rome` | cornu, tibia |
| `africa` | kora, djembe, mbira, balafon |
| `egypt` | sistrum, harp |
| `maghreb`, `levante`, `persia` | oud, ney, daf, rebab |
| `italy`, `germany`, `switzerland` | hurdy-gurdy, mandolin, alphorn, clavichord |
| `clockpunk` | a music box, a mechanical organ, a bird that sings on the hour |
| `fairytale_fae` | a fiddle nobody else can tune, a reed cut from the wrong river |
| `grimdark` | a drum with a skin you do not ask about |
| `anime` (Monk) | none; the Monk does not play |

The Halfling, who has no marker, gets the fiddle and the spoon. The Tiefling,
who has no marker by canon, gets whatever the host culture plays (Aasimar
page §5), which is the whole point of the Tiefling.

---

## 📔 6. Relationships: species × Bard

| People | The seed | College | Note |
|---|---|---|---|
| **Aasimar** | The Muses' children (§3). Plainchant; the kithara. | Dance (Freedom, Terpsichore), Lore (Clio, History). | ✅ The one species whose spark is an art. |
| **Elf** | Egil's head-ransom; the skald's *níð*; the harp. And the Dream drifts on story. | Lore, Glamour. | ✅ An Elf Glamour Bard "performed for a court that does not admit mortals twice"; the Elf *came out of* that court. ⚠️ The Glamour text assumes a mortal outsider; on an Elf, the loan reads as family, and the closing line ("still counts you as part of the show") is truer than it knows. Worth one sentence's care. |
| **Dwarf** | *Escarnio*, the *romancero*, the Cid's juglar, the vihuela, the duende. | Lore, Valor. | ✅ The Dwarf Bard is the richest well on the roster and the least expected. "Gold never corrupts" against a satirist who is paid in it. |
| **Dragonborn** | Flower and song; Noh; the shamisen and the huehuetl. Two silhouettes. | Valor (Nezahualcóyotl), Glamour (the mask). | ✅ A codified society "of rules" and an art whose name means the only truth: the Dragonborn Bard is the clan's one licensed liar. |
| **Goliath** | Tyrtaeus; the phalanx marched to a flute. | Valor. | ✅ The war-elegist, on a people whose civilisation fell: "The greater they fall" is the song. |
| **Orc** | The manaschi; the morin khuur. | Lore. | ✅ The horde's memory, no book. |
| **Gnome** | Commedia; the hurdy-gurdy; "a joke that only works in the Sylvan tongue". | Glamour, Lore. | ✅ The masked improviser with a mechanical instrument. |
| **Halfling** | "All of it written down in recipe books." | Lore. | ✅ The anthology is cookery; Countercharm is a lullaby. The Halfling Lore Bard's repertoire is the most comforting on the roster and the least useful in a dungeon, which is the species. |
| **Human** | The griot; the kora; institutions ("there is always a human kingdom") means there is always a court to play. | Any. | The default Bard; the Egyptian and Carthaginian wells (the sistrum, the sea-shanty) rescue it. |
| **Tiefling** | "Nobody teaches you what you are." | Glamour (the loan from the one court that took them), Lore. | ✅ The only Bard who had to invent a tradition, and the host-culture instrument is theirs by adoption. |

---

## 📔 7. Relationships: backgrounds × Bard

- **Revolutionary.** *"A song can do what a sword can't: fill a room with
  courage, then empty it into the streets."* ✅✅ The Bard's thesis in the
  background's first sentence; the Revolutionary is the class's own
  background, and "a folded pamphlet finds a stranger's palm" is Cutting
  Words on paper. The class text should never restate it; the background
  already sang it.
- **Squire × Valor.** *"You served someone the songs are about… you know the
  part the legends leave out."* Against Valor's *"When they tell this one, you
  will not need to exaggerate."* ✅ Tension worth having: the Squire Valor
  Bard knows the truth and sings the legend anyway, and decides every night
  which one the room gets.
- **Stranger.** *"A language fewer people speak each year, a handful of
  songs, the way it was cooked at home."* ✅ The Stranger is a Bard by
  default: the last songs of a scattered people, and the Long Memory's old
  ones are the anthology.
- **Servant × Lore** (seed 43). *"You stood at the sideboard… and learned the
  entire register."* ✅ The sommelier as collector; the Cupbearer feat; "you
  poured" as the performance. The Gnome Lore Servant catalogued the masters'
  taste the way the Lore Bard catalogues everything.
- **Fated × Dance** (seed 41). *"If you fall, you roll over and jump back up.
  If you break a mirror, you make a new one even fancier."* ✅ The cursed
  dancer. Jinx on a College whose whole art is partners moving when you move:
  the partner's rope gives way. Comic-tragic, and the Aasimar of it had Joy's
  halo spinning.
- **Dragon Cultist.** ✅✅ The Mythopoeic loop (§2): a Cultist Bard who sings
  dragons is *making* the dragon they worship. The canon's rule that nobody
  explains it correctly and is believed holds hardest here. Never say.
- **Wildkeeper.** Orpheus proper: "the crows and the foxes and the old boar
  began to answer". ✅ The beasts that listen.
- **Naturalist.** *"Give you a crowd and a specimen and you can hold them for
  an hour."* Already half a Bard; the Naturalist Lore Bard is the lecture as
  performance.
- **Fortune Teller.** *"A patter that hands them back their own secrets
  dressed as prophecy."* The Bard's craft named by a rival trade.
- **Investigator.** *"It was a rude interruption of your detailed
  explanation, and it ruined the moment, the mystery, and the whole process of
  revelation."* ✅ The Lore Bard's monologue, spoiled. Comic.
- **Debunker.** *"The medium's table lifts because of a very strong left
  knee."* The performer who knows every trick, in a class whose tricks work.
- **Gambler.** *"Standing up smiling is the job. The cards were never the
  job."* The performer at the table.
- **Herald.** "The mouth and the hand." Any College; the Herald Bard's word
  opens gates because the world listens.
- **Vagabond.** *Bearer of News.* The minstrel's oldest function; the
  official Entertainer (*Musician*, one sentence) is the thin version.
- **Shadow × Glamour.** *"You have been kind, and funny, and useful, and none
  of it ever quite closes the gap."* ✅ The Glamour loan on someone who
  performs to be accepted; the light that "rubbed off" on a thing with no
  shadow.
- **Destined.** *"A prophecy with a gap exactly your shape."* The Bard who
  wrote it.
- **Sellsword × Valor.** The juglar for hire.

---

## 📔 8. Flags

### ✅ Singular, and to be protected

1. **"The world listens" is canon, three times** (§2). Record it.
2. **"Play like lives depend on it. They do."** The class close; the duende in
   six words.
3. **"Other mages guard their secrets. You find that adorable."** Lore's
   voice.
4. **"You are quickest exactly where you are most seen."** Dance's thesis.
5. **The Glamour echo of the Archfey poem** ("part of the show"): keep. One
   substance, two doors, and the Elf Glamour Bard makes it literal.
6. **Two Muses unassigned, two Ideals waiting** (§3).

### ⚠️ Stock, contradictory, or thin

1. **Rulebook paragraphs verbatim on the sheet** (§1). An IP question.
2. **Five open-choice or retraining clauses** in the training map; the
   2026-08-27 sweep did not re-land.
3. **No instrument, ever** (§5).
4. **No lines.**
5. **Glamour on an Elf** reads "mortal" at someone who came out of the court
   (§6).
6. **Countercharm** is smaller than its image (0015's finding); the line
   below stays inside the rule.

---

## 📖 9. Feature lines: drafts

*Italic inspiration line only. Register: the told tale, second person, a
drummed cadence kept as seasoning, no proper nouns, no dice, no em-dashes. Rule
text untouched except the open choices, which are rules work. Proposals for
proposals.*

### Core lessons

| Lesson | Draft |
|---|---|
| **Bardic Inspiration** (1) | *You have seen what a song does to a room. Now you can aim it.* |
| **Spellcasting** (1) | *The act is the spell. There was never anything behind the curtain but you.* |
| **Expertise** (2) | *Two things you do the way other people breathe.* |
| **Jack of All Trades** (2) | *Half of every trade you ever crossed, because everything is material.* |
| **Font of Inspiration** (5) | *The show goes on. It always has.* |
| **Countercharm** (7) | *Play louder than the thing that is trying to get in.* |
| **Expertise** (9) | *Two more. You were always going to collect them.* |
| **Magical Secrets** (10) | *Other people's magic, overheard, kept.* |
| **Superior Inspiration** (18) | *You are never actually out of material.* |
| **Words of Creation** (20) | *At the bottom of every art there is a word. You have two of them now, and one of them is no.* |

### College of Dance

| Feature | Draft |
|---|---|
| **Dazzling Footwork** (3) | *Being watched is armour. Being watched is the blow.* |
| **Inspiring Movement** (6) | *You move, and because you moved, so do they.* |
| **Tandem Footwork** (6) | *You set the tempo of the whole room before anyone has drawn.* |
| **Leading Evasion** (14) | *Your partners share your step, including the one out of the fire.* |

### College of Glamour

| Feature | Draft |
|---|---|
| **Beguiling Magic** (3) | *Loveliness, and the threat under it. Two faces of one light.* |
| **Mantle of Inspiration** (3) | *You dress your friends in a little of the loan.* |
| **Mantle of Majesty** (6) | *You speak, and it is done. Try not to enjoy it.* |
| **Unbreakable Majesty** (14) | *Too beautiful to strike. They find that out mid-swing.* |

### College of Lore

| Feature | Draft |
|---|---|
| **Bonus Proficiencies** (3) | *Three more things went in the bag.* |
| **Cutting Words** (3) | *A word placed exactly, subtracted from the world's roll.* |
| **Magical Discoveries** (6) | *You watched how the priests, the druids and the wizards do it. Two of their tricks are yours now, and they have not noticed.* |
| **Peerless Skill** (14) | *You have read how this is done. Now you do it.* |

### College of Valor

| Feature | Draft |
|---|---|
| **Combat Inspiration** (3) | *The war-chant turns the axe, or drives it.* |
| **Martial Training** (3) | *The sword is an instrument. You tuned it.* |
| **Extra Attack** (6) | *A verse, then a blow, in one measure.* |
| **Battle Magic** (14) | *Spell, then steel, before the echo dies.* |

---

## 📖 10. Threads to pull in later cycles

- **Canon**: one paragraph recording that the Bard operates the setting's
  plastic metaphysics (§2), placed in the Dragon or Elf canon where the loop
  is already stated.
- **Aasimar**: Grace as a candidate Ideal (§3). Euterpe is settled: she holds Harmony.
- **Gear**: `Map_of_Instruments` (§5), and the Bard's Spellcasting Focus
  seated as a named instrument.
- **Tiefling**: the host-culture instrument as the species' first inheritance.
- **Rogue**: Cutting Words and Sneak Attack are two theories of the placed
  blow; keep the wit with the Bard and the knife with the Rogue.
- **Rules work outside this page**: the five open choices, the verbatim
  paragraphs.


---

## 📔 11. The Tiefling's instrument

There is no host-culture draw for the Aasimar or the Tiefling; both stay
distinct peoples. So the Tiefling's instrument comes from their own register
rather than from whatever the host culture plays. The carvings nobody can read
are the one inheritance the canon allows them, and the register behind those is
Egypt: a sistrum, or a frame drum, drawn from the `grimdark` pool with one
Tiefling-only entry. That keeps the species distinct without saying why. The
Halfling's fiddle and spoon stand.
