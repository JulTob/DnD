# 🔥 Sorcerer: the Marked, read against the whole setting

> 🚧 **In flow.** 3 of 10 chapters are still proposals. 🔒 1 · 🧾 2 · 🔎 4 · 🚧 3

*Mythos analysis, 2026-09-08. Design and literary criticism, not page text. No
Dialog exists for the Sorcerer. The Aasimar and Cleric pages flagged this class
as a collision with the species law (traits are taught or gifted, never
inherited) and gave it the "born" seat in the theology table. This page argues
that seat is misnamed, reads the four Origins against the Dragon canon, and
drafts what the sheet lacks: class text, Origin texts, feature lines. Nothing
here is landed.*

**Where the text lives.** Class and Origin paragraphs: *nowhere*. Lessons:
`AtlasOfTraining/Map_of_Sorcerer_Training.py` (rules only, no lines). A 2014-era
layer in `Map_of_Classes/Training/Sorcerer.py` still prints *"You gain the
Draconic Sorcery sorcerous origin; see PHB '24 pp145-150"* and a Metamagic
block in markdown asterisks. Origins on the roster: Aberrant, Clockwork,
Draconic, Wild Magic. No legend register of its own.

---

## 🧾 1. What a Sorcerer player is handed today

A level 11 Dragonborn Draconic Sorcerer (seed 9) receives: the Dragonborn
entry; a Criminal background that is one sentence; *Innate Sorcery* as a
bullet list; *Metamagic* that says "Choose 4 Metamagic options", which the
generator was supposed to have chosen; *Elemental Affinity* keyed to "the
damage type of your draconic ancestry", which for a Dragonborn the sheet
already knows and does not say, and which for any other species is never
drawn at all; and a closing line that sends the player to a page number in a
book. A Halfling Wild Magic Sorcerer (seed 16) is told a Surge "occurs" and
to "roll on the Wild Magic Surge table", which does not exist in the codebase.

⚠️ Three of these are rules failures before they are fantasy failures: the
unresolved Metamagic choice (QST-0055 names it), the undrawn ancestry, and the
missing table. The Sorcerer's whole fantasy lives in *what the magic does
when it gets out*, and the sheet cannot say.

---

## 🔒 2. The core fantasy: not born. Marked.

**Candidate A, the bloodline.** The dragon-blooded, the child of a god, the
mutant. Merlin's incubus father; the Nephilim; Harry Potter's "born wizard";
the 2014 book's own framing. The popular reading, and **"born different" is a
legitimate Sorcerer fantasy in this setting**: the species law guards against
monoculture and moral determinism, not against biology, and nobody cultures
themselves into darkvision. A class or a subclass is not a species trait in any
case, so the question never arises. What weakens the bloodline is not the law
but the 2024 text, which moved: Spellcasting now opens *"An event in your past
left an indelible mark, flooding you with raw magic."* An event, not a parent.

**Candidate B, the marked.** Something happened, and afterwards the magic was
in you the way a fever is in you. Not learned (Wizard), not lent (Warlock),
not sworn (Paladin), not kept (Cleric). *Yours*, and not entirely under your
control. The literature is metamorphosis rather than genealogy: Ovid, where
every body that changes was struck first; Carrie, where the talent erupts;
the Arcane Mutant background's "a spark that got into you and never went
out"; and, in this setting, the Dragon canon's own sentence: *realisation
actualises the body.*

**Candidate C, the weather.** Magic as a force of nature that happens to have
a person attached. The Wild Magic reading generalised. It is B with the self
removed, and the rules refuse it: Charisma is force of self, and Metamagic is
the self *editing* magic that others recite.

**The rules answer B**, and the shape is a body, not a lineage:

| Feature (level) | What it proves |
|---|---|
| Spellcasting (1) | "An event… an indelible mark." Charisma: the magic is exactly as strong as the person. |
| Innate Sorcery (1) | "Unleash the sorcerous power *within*." A minute of the self turned up. Not summoned, not invoked: released. |
| Font of Magic (2) | Sorcery Points convert to slots and back. Magic as a *reservoir* in the body, not a list on a page. The Wizard has a book; the Sorcerer has a tide. |
| Metamagic (2) | Careful, Distant, Twinned, Subtle: the Sorcerer *bends the shape* of a spell. Nobody else can. The magic was never anybody else's, so it has no fixed form. |
| Sorcerous Restoration (5) | The reservoir refills on a short rest. A body recovering. |
| Sorcery Incarnate (7) | Two Metamagics on one spell while the self is turned up. The bending compounds. |
| Origin features (3 to 18) | Every Origin ends in a *change of body*: Dragon Wings, Revelation in Flesh, Trance of Order, Controlled Chaos. The mark keeps marking. |
| Arcane Apotheosis (20) | A free Metamagic every turn while Innate Sorcery is up. The self and the magic stop being two things. |

**Register.** The Barbarian chants; the Monk accelerates; the Cleric is warm
scripture; the Paladin is the oath remembered; the Warlock is the terms. The
Sorcerer's register should be **sensation**: present tense, physical, the
magic felt in the body before it is understood (heat behind the sternum,
copper on the tongue, hair standing). The device: **each Origin text ends on
what the body is turning into, without naming it.** That is the Dragon
canon's rule ("never explain it on the page") applied to a class.

**Rename the seat.** The Cleric page's theology table gave the Sorcerer
*born*. Make it **marked**: the greater thing did not make you; it *struck*
you, and what it left is still moving. Six seats: kept, noticed, ridden,
sworn, marked, owed.

---

## 🔎 3. The Sorcerer is the Dragon canon's second class

The Barbarian page found *ziran* in "we live out our inner nature": the
Barbarian *embodies* the Dragon's principle. The Sorcerer *casts* it.

- **"Realisation actualises the body."** Dragon Wings at 14 sprout from a
  Sorcerer who is not a Dragonborn. Revelation in Flesh (Aberrant, 6) alters
  the body on demand. Trance of Order (Clockwork, 14) makes the body a
  mechanism for a minute. The canon says the Ascending "is not spiritual only:
  what they understood themselves to be, they become." Every Origin capstone
  is that sentence, small.
- ✅ **The Draconic Sorcerer is the Ascending starting early and sideways.**
  Not a person with dragon blood: a person in whom the dragon "they were
  always carrying" has begun to leak out before the self-overcoming that is
  supposed to earn it. The canon already describes this from outside: *"Seen
  from outside this looks like a curse, and the family will describe it that
  way."* Never say so. Let the text say "something in you is becoming
  something" and stop.
- ✅ **Aberrant Sorcery's level 6 feature is literally called *Revelation in
  Flesh*.** In this setting that is the Ascending's mechanism (the body
  follows the realised self) with an alien self at the wheel. The canon's
  failure case, "a self authored to someone else's specification", has a
  subclass. Story, not fault; never confirm.
- **The five dragon positions** in the canon (Promethean, Mainländer,
  Laozian, Nietzschean, Mythopoeic) are not a one-to-one map, but two land
  cleanly: Draconic is *Nietzschean* (become what you are), Wild Magic is
  *Laozian* ("parables and weather rather than swords"). Clockwork is the
  *anti*-ziran, order imposed on the self, and Aberrant is the outside
  getting in. The four Origins are four answers to "who is doing the
  becoming", which is the canon's question.

**Species law, resolved.** *Taught, not inherited* guards moral determinism.
A mark is neither taught nor inherited: it is *suffered*. The Sorcerer can
say "it happened to you" without saying "you were born to it", and the
Aasimar Sorcerer (Aasimar page §6) stops being a contradiction: the spark is
gifted, the magic is the event the spark had.

---

## 🧾 4. Wells

**Ovid.** The Metamorphoses are the Sorcerer's book: nobody in them chooses
to change, and every change is the truth of the person made physical. Daphne,
Actaeon, Arachne. The register of sensation comes from here.

**Prometheus, reversed.** The canon's Promethean position is "fire belongs to
all". The Wizard steals fire; the Warlock borrows it; the Sorcerer *is* it.
The one who has what everyone else has to take.

**The nahual** (`aztec`, Dragonborn). A person born on a day that binds them
to an animal double, and who can become it. ✅ A Dragonborn Draconic Sorcerer
of the Aztec well is a *nahualli* whose animal is the feathered serpent, and
Dragon Wings at 14 are Quetzalcoatl's. The two wells the Dragonborn hold give
the Origin two silhouettes, which is what the canon asks ("no two traditions
produce the same silhouette").

**Kepler's clockwork.** "The celestial machine is not a divine organism but a
clockwork." The Renaissance pair (Gnome: `italy`, `germany`, `switzerland`;
`clockpunk`) is the Clockwork Origin's home, and the Hermeticist background's
*as above, so below* is its creed. The Clockwork Sorcerer is the person in
whom the clockwork universe runs, and Restore Balance is the correction of an
anomaly. ✅ Kepler, not Mechanus: the setting has no Modrons and needs none.

**Carrie, and the Aberrant Mutant.** The talent that erupts and the family
that hides the child. The Tiefling entry already has the family that "reports
a stillbirth and means it as mercy". The Aberrant Origin should not repeat the
Aberrant Mutant background's "There is a word for what you are"; the
background owns the wound, the Origin owns the *change*.

**Merlin**, kept for what he is not. The half-fiend prophet who *sees*. Not the
Sorcerer's father-story but the Sorcerer's *sight*: Clairvoyance and Detect
Thoughts on the Aberrant list, Fear on the Draconic. The mark sees.

---

## 🔎 5. Relationships: species × Sorcerer

| People | The seed | Origin that sings | Note |
|---|---|---|---|
| **Dragonborn** | Nearest the thing; "not the ones who missed it". Two sets of wings: Draconic Flight at 5, Dragon Wings at 14. | Draconic. | ✅ The wings come twice, and the second pair "last until you dismiss them". The mini-Ascension the canon names, then something more. Never confirmed. ⚠️ The sheet must name the ancestry's damage type. |
| **Dwarf** | *"A dwarf who spends ninety years on one gem may Ascend through the obsession itself… the family will describe it as a curse."* | Draconic. | ✅✅ The canon wrote the Dwarf Draconic Sorcerer before the class did. Metal given and proven, and then something that was neither. |
| **Elf** | The Dream drifting fast in one elf. | Wild Magic. | ⚠️ Canon: "no elf transforms in a scene, and no elf transforms alone". A Wild Magic Surge that changes an elf's body is that rule broken by dice. Story: the Dream leaking through one person, and the elders' horror. Keep the surge; know the cost. |
| **Aasimar** | Gifted spark, marked magic (§3). "A Celestial is certain, and argues methodology." | Clockwork (the certain kind), Wild Magic (the strain). | The Ideal cannot bend; Metamagic bends. An Aasimar Sorcerer bends *around* the thing that cannot. |
| **Tiefling** | A mark on top of a mark. "We carry fire, that's certain." | Wild Magic, Aberrant. | ✅ The Tiefling who was condemned for what the horns *meant* and now carries something that actually does things. Two readings of one body. |
| **Gnome** | "A bird that sings on the hour and has done since your great-grandfather wound it." | Clockwork. | ✅ Native; the class in species clothing. The interesting Gnome Sorcerer is Wild Magic: curiosity that will not wait. |
| **Goliath** | Storm's Thunder; dragon versus giant in the myth layer. | Wild Magic (the storm), Draconic (the traitor). | ✅ A Goliath with dragon magic is the myth layer's defector, and the gear register will hand them a Labrys and a dragon's breath in one kit. |
| **Orc** | "Every soul walks a wind path… If we fall, we carry on." | Wild Magic. | The storm as the mark. |
| **Halfling** | "Nothing bad ever happens to us." Then a Surge. | Wild Magic. | ✅ The valley's one accident, comic and true. |
| **Human** | The Servant (seed 15): *"You heard it all again, coming from inside you."* | Aberrant. | ✅ Telepathic Speech is the channel that did not close. |

---

## 🔎 6. Relationships: backgrounds × Sorcerer

- **Arcane Mutant.** "Magic comes to you and does not pass through. When a
  spell hits you, part of it stays." That is Font of Magic as a background.
  ⚠️ Redundant with the class; the interesting Arcane Mutant is a Fighter.
  When they do coincide, the hook's "the only people alive who can tell you
  what you are turning into" is the Sorcerer's §3 question asked aloud.
- **Aberrant Mutant × Aberrant.** Redundant twice over ("There is a word for
  what you are"). Let the background keep the wound and the Origin keep the
  change (§4).
- **Fated × Wild Magic.** "You break things… milk spoils as you touch the
  glass… You may jinx something every day." ✅ The curse and the Surge are one
  figure. Jinx plus Tides of Chaos is a Character who *aims* the accident.
- **Gambler × Wild Magic.** Bend Luck: a d4 added or subtracted from anyone's
  roll. ✅ "You were counting." The Gambler who can cheat reality, and knows
  exactly when the mark stops enjoying himself.
- **Debunker.** "There is always a reasonable explanation." ✅ A Sorcerer who
  explains their own magic as nerves and adrenaline, until the d20 comes up 1.
- **Naturalist.** "Somewhere along the way, from watching too closely for too
  long, you picked up a little of what you were studying. You still cannot say
  how." ✅ Magic caught like a fever. The best "marked" background not written
  for the class.
- **Survivor × Aberrant.** "It has your face… One day you will be allowed all
  the way in." Against Revelation in Flesh. ✅ The thing is not out there. It
  is the mark.
- **Hermeticist × Clockwork.** "As above, so below… the laws of
  correspondence." ✅ The creed of the Origin; the Hermeticist Clockwork
  Sorcerer is the only one with a *theory* of the clockwork.
- **Investigator × Clockwork.** "Whatever remains, however unwelcome, is the
  truth." Trance of Order: nine or lower is a ten. ✅ The world made
  reasonable by force.
- **Bailiff × Clockwork.** Restore Balance as the law that "up close there is
  no oversight" was missing.
- **Dragon Cultist × Draconic.** "Someday you will become your own Master."
  ✅ The cultist who is *actually changing*, and the canon's failure case
  (worshipping the man who despised movements) with the added horror that it
  might be working.
- **Spirit Medium × Aberrant.** "First you noticed them; then they noticed
  you." Telepathic Speech from the other direction.
- **Fortune Teller.** "Every so often a vision arrives unbidden." The mark
  that sees (§4).
- **Ice Nomad × Draconic.** "The ice let you go." A white or silver ancestry
  that did not.
- **Sellsword × Wild Magic** (seed 16). ✅ Comic: the mercenary whose spells
  explode, "danger became just another day's labor".

---

## 🔎 7. Flags

### ✅ Singular, and to be protected

1. **The Dragon canon already contains the Draconic Sorcerer** ("the family
   will describe it as a curse") and the Aberrant one (*Revelation in Flesh*).
   Two Origins have setting-native readings without a word of new lore.
2. **"Marked" as the seat** (§2). It dissolves the species-law collision.
3. **Metamagic as the class thesis.** The Sorcerer edits what others recite.
   Every line should keep the magic *shapeless until the self shapes it*.
4. **The nahual and Kepler** as the two Origin homes the culture map already
   holds (§4).

### ⚠️ Stock, contradictory, or thin

1. **Nothing is written.** No class text, no Origin text, no lines.
2. **A page number on the sheet.** "See PHB '24 pp145-150" is a citation in
   the one register where every other line is a fact about the character.
   Retire the 2014 layer.
3. **"Choose 4 Metamagic options."** The generator did not choose; the sheet
   offers a choice that does not exist (QST-0055). The four should be named,
   with their costs, and the Options block should go.
4. **No ancestry is drawn** for a Draconic Sorcerer who is not a Dragonborn,
   and for a Dragonborn the known type is not printed. Elemental Affinity
   refers to nothing. One draw from the same ten colours, seated once.
5. **The Wild Magic Surge table does not exist** in the codebase. The Origin's
   entire content is the table. Without it, "a Surge occurs" is a sentence
   about nothing.
6. **Markdown in HTML.** The Metamagic block prints `**Careful Spell (1)**`
   and en-dashes; the em-dash law is broken in three Sorcerer features.
7. **The bloodline reading will win by default** because the only Origin name
   with a noun in it is "Draconic", and the sheet currently says "lineage"
   three times. A class text is the only thing that can stop it.

---

## 🚧 8. Drafts

*House rules: second person; sensation before rule; no proper nouns; no
em-dashes; no open choices. Each Origin text ends on what the body is turning
into, unnamed. Proposals.*

### Class text (new)

```
Nobody taught you. Something happened, and afterwards the magic was in you the way a fever is in you: not learned, not lent, not sworn. Yours. Not entirely under your control.

Others keep their magic in a book, or at the far end of a bargain, or in the hands of something that loves them. You keep it behind your sternum. It runs hot when you are angry and cold when you are afraid, and when you let it out it does not arrive as a formula. It arrives as you: your shape, your temper, your accent. You do not recite a spell. You bend it, because it was never anybody else's.

The event left a mark. The mark has not stopped. Something in you is becoming something, slowly, and you are the only person alive who can feel which way it is going.
```

### Draconic Sorcery (new)

```
It was in your mouth before you had a word for it. Heat, or frost, or the sour edge of acid, or the taste a storm leaves. Your skin took it next: nothing anyone can see, but a blade finds you harder than it should, and you have not been cold since.

You did not inherit this. Inheritance is a thing families do on purpose. This is a thing that is happening to you, and the family, if they know, have a word for it that is not a kind one.

One day the wings come. Later, something answers when you call that is shaped like what you are turning into.
```

### Wild Magic Sorcery (new)

```
Magic is weather in you. Most days it is fine. Some days the sky does something nobody asked for, and you are standing under it, and so is everyone else.

You have stopped apologising. The surge is not a mistake and it is not a punishment; it is the honest version of what every spell would do if it were not being held to a shape. You can lean on it. You can tilt a stranger's luck a finger's width. You can, with practice, choose which storm arrives.

Something in you is turning into a season. You do not yet know which.
```

### Clockwork Sorcery (new)

```
Somewhere underneath everything there is a mechanism, and you can hear it. Not the gods and not the weather: the wheel under the wheel, the count that always comes out, the reason a dropped cup falls the same way twice.

You were made a part of it, or made too precisely for anything else. Luck offends you. Where somebody's roll is being helped or hindered, you can make it plain again. You can put a wall of pure order between a friend and the next blow. For a minute at a time you can be the mechanism outright, and nine or lower simply stops being a number that happens.

Something in you is turning into a part of the machine. The machine, so far, has not said what part.
```

### Aberrant Sorcery (new)

```
Something from outside looked in, once, and you were the window it looked through. It has not stopped looking. You can hear other people's thoughts the way you hear a room next door, and you can speak into a mind without opening your mouth, and none of your magic makes a sound any more.

Your body has ideas. Ask it, and for a while it will see what is invisible, breathe water, take to the air, fit through a crack an inch wide. It knows how to do these things. You did not teach it.

Something in you is turning into what looked in. You are trying to find out whether that is a bad thing.
```

### Feature lines: core

| Lesson | Draft |
|---|---|
| **Spellcasting** (1) | *It happened once, and it keeps happening. The magic is exactly as strong as you are.* |
| **Innate Sorcery** (1) | *For one minute you stop holding it in.* |
| **Font of Magic** (2) | *Not a list. A tide. You can pour it into a shape or pour the shape back into the tide.* |
| **Metamagic** (2) | *A spell is a shape somebody else decided on. Yours was never anybody else's, so it bends.* |
| **Sorcerous Restoration** (5) | *A body recovers. So does this.* |
| **Sorcery Incarnate** (7) | *Turned up, it bends twice.* |
| **Arcane Apotheosis** (20) | *You and the magic stopped being two things. It shows.* |

### Draconic

| Feature | Draft |
|---|---|
| **Draconic Resilience** (3) | *Scales nobody can see. A blade finds you harder than it should.* |
| **Draconic Spells** (3) | *The spells arrive in the same colour as the taste in your mouth.* |
| **Elemental Affinity** (6) | *Your own element does more in your hands, and less to you.* |
| **Dragon Wings** (14) | *They come. They stay until you say otherwise.* |
| **Dragon Companion** (18) | *Something answers that is shaped like what you are turning into.* |

### Wild Magic

| Feature | Draft |
|---|---|
| **Wild Magic Surge** (3) | *Some days the sky does something nobody asked for.* |
| **Tides of Chaos** (3) | *Lean on the weather. It will lean back, soon, on its own terms.* |
| **Bend Luck** (6) | *A finger's width on somebody else's fortune.* |
| **Controlled Chaos** (14) | *Two storms offered. You take the one you like.* |
| **Tamed Surge** (18) | *You choose which storm arrives. Tamed is the wrong word, and it is the word.* |

### Clockwork

| Feature | Draft |
|---|---|
| **Clockwork Spells** (3) | *The wheel under the wheel lends you what it uses to keep turning.* |
| **Restore Balance** (3) | *Where luck is being helped or hindered, you make it plain again.* |
| **Bastion of Law** (6) | *A wall of pure order, exactly as thick as you paid for.* |
| **Trance of Order** (14) | *For a minute, nine or lower is not a number that happens.* |
| **Clockwork Cavalcade** (18) | *The mechanism sweeps through, and everything is put back where it goes.* |

### Aberrant

| Feature | Draft |
|---|---|
| **Psionic Spells** (3) | *None of it makes a sound any more.* |
| **Telepathic Speech** (3) | *Into a mind, without opening your mouth. It learned that first.* |
| **Psychic Defenses** (6) | *What looked in cannot be looked into. Neither, now, can you.* |
| **Revelation in Flesh** (6) | *Your body has ideas. You did not teach it.* |
| **Warping Implosion** (14) | *You leave, and the place you left comes with you.* |

---

## 🚧 9. Threads to pull in later cycles

- **Cleric page, theology table**: rename *born* to *marked*.
- **Dragon canon**: add a line that the Draconic and Aberrant Origins are
  the Ascending seen early and seen hijacked, never to be confirmed.
- **Wizard**: the stolen fire against the fire itself. The Wizard page must
  keep Athens (the academy) as the Wizard's, not the Sorcerer's.
- **Backgrounds**: Arcane Mutant and Aberrant Mutant are class-shaped;
  consider an affinity nudge away from their own Origins so the generator
  does not say the same thing twice.
- **Rules work outside this page**: the ancestry draw, the Metamagic
  resolution, the Surge table.

---

## 🚧 10. Synergies, and the open question

**Synergies are welcome and independent.** The Origin is drawn separately from
species and background, and where two axes agree the sheet should say so once
rather than twice: a Dragonborn Draconic Sorcerer draws the **same** ancestry as
the species (one draw, one colour), the way an Aasimar Celestial Warlock's
patron is the descent ancestor (Aasimar §8). A Human Draconic Sorcerer still
needs an ancestry drawn, and the sheet still must name it.

**For an Aasimar Sorcerer**, the spark from the Ideal awakens something, or it
may have been a way for something else to get in. Only a Celestial-flavoured
Origin draws on the spark; a Draconic or Aberrant Origin needs another
explanation, and the player supplies it.

❓ **Open: is the core fantasy Talent rather than the mark?** The reading under
discussion is that the Sorcerer is not blood, lineage or being born with magic,
but **talent**: you still level up, you still gain experience, and talent has to
be polished. Under it the Origin answers *what kind of talent* and the species,
the background, or nothing at all answers *why you have it*, which is the
Aasimar's Ideal-and-Descent shape. The mechanics favour it (Innate Sorcery is
rationed and expands, Font of Magic is conversion, Metamagic is bending), and it
completes a set: the six casters as six relationships to the source, taken by
the Wizard, granted to the Cleric, lent to the Druid, contracted by the Warlock,
performed by the Bard, and simply **had** by the Sorcerer, who is the only
caster with no counterparty. It would rename the seat, since *marked* would
become one *why* among several. Undecided; no Dialog exists for this class.
