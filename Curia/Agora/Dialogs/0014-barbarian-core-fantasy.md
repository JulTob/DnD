# Dialog 0014 — Barbarian core fantasy

- **Question:** What is the Barbarian's core fantasy, does the 2024 kit as implemented actually establish it, and do the recovered texts carry it in the house voice?
- **Commissioned by:** Julio, in chat, 2026-08-31 (provisional class and subclass descriptions for the beta generator).
- **Date:** 2026-08-31
- **Related:** QST-0072 (recovery), QST-0062 (voice sweep), `Canon/Feature-Text.md`, `Canon/Dragons-and-the-Overcoming.md`
- **Consuls called:** Lorekeeper (Elf Sage), Venustas (Bard), Rules (Paladin), Simplicity (Monk); Vox reports.
- **Status:** 🟡 provisional: texts pending Julio's word.

---

## 🧭 Framing

The commission asked for gap-fill: dump the vault `BarbarianKit` bytecode, map which texts
survive, and write only the missing ones. The dump came back fuller than the commission
expected.

**Every Barbarian text already exists, and the vault agrees with the restored source
byte for byte.** The four subclass constants were extracted from
`vault/guilds/BarbarianKit.cpython-314.pyc` (via `co_consts`, without executing the
module, which would have re-declared the Specializations) and each matches
`AtlasLusoris/AtlasOfGuilds/BarbarianKit.py` exactly. One correction to the
commission's own brief: the line it quoted as the class text ("Most people hold
something back...") is the **Berserker's** opening. The class text is
`BARBARIAN_DESCRIPTION` in `AtlasLusoris/GuildKit.py` (line 1138), and it was never
lost.

| Text | Where it lives | State |
|---|---|---|
| Class | `GuildKit.py` : `BARBARIAN_DESCRIPTION` | found, wired |
| Berserker | `BarbarianKit.py` : `BERSERKER_DESCRIPTION` | found, wired, matches vault |
| Wild Heart | `BarbarianKit.py` : `WILD_HEART_DESCRIPTION` | found, wired, matches vault |
| World Tree | `BarbarianKit.py` : `WORLD_TREE_DESCRIPTION` | found, wired, matches vault |
| Zealot | `BarbarianKit.py` : `ZEALOT_DESCRIPTION` | found, wired, matches vault (carries a `{name}` slot) |

So the gap is not the prose. The gap is the record. `WarlockKit.py` holds a worked
commentary above every patron explaining why each paragraph is written the way it is,
with a per-feature rules read; `BarbarianKit.py` holds one thin comment. This Dialog is
that missing record: the council names the fantasy the found texts embody, tests it
against the training map (`AtlasLusoris/AtlasOfTraining/Map_of_Barbarian_Training.py`,
real source, all four Paths), and presents the texts for Julio to bless as provisional.

### Constraints from Canon

- Second person; inspiration before rule; the description is identity and drive, never a
  mechanics summary (`Feature-Text.md`, the Fiend worked example).
- Death of the Author: no lore-dumps, no proper-noun worldbuilding; the reader keeps the
  responsibility of meaning.
- No em-dashes in authored prose; no open-choice language; dice stay notation.
- Martial and technique fantasy draws Iberian and Eastern rather than Germanic
  (standing ruling).
- Species traits are taught, not inherited: no moral determinism by blood or by
  upbringing.

---

## 🗣️ Deliberation

**Lorekeeper (Elf Sage):** Before anyone reads the found texts aloud, let us do this
properly and name the candidate fantasies as if the page were blank. The Barbarian
archetype in the wider culture is three different stories wearing one hide, and they
disagree about the most important question a player can ask: *who is driving?*

*Candidate A, possession.* Rage as something that takes you. The Ynglinga saga's
warriors of Odin who fight unarmoured and feel neither fire nor iron; Cú Chulainn's
ríastrad in the Táin Bó Cúailnge, the warp-spasm that turns the boy into a thing his
own allies flee; the Hulk, whose whole tragedy is that Banner is not home when it
matters. The fantasy is surrender: strength bought with the self as collateral.

*Candidate B, the wilderness against civilization.* Robert E. Howard's Conan, and the
essay hiding inside "Beyond the Black River": barbarism as mankind's natural state,
civilization as the aberration. Tarzan. Rousseau, badly read. The fantasy is contempt:
the walls are a lie and you are the truth that breaks them.

*Candidate C, total presence.* The untamed self, fully arrived. Kazantzakis' Zorba,
who dances what he cannot say and is the most alive man in every room he enters.
Whitman, who gave us the very word as a badge: "I too am not a bit tamed... I sound my
barbaric yawp over the roofs of the world." Nietzsche's Dionysian current in *The Birth
of Tragedy*: the intoxication that dissolves hesitation without dissolving the dancer.
The fantasy is wholeness: everyone else is holding something back, and you are not.

**Venustas (Bard):** Now I read the found texts against those three, because the answer
is not ambiguous. The class text says, in so many words: *"When it comes, you do not
lose control. You lose hesitation."* That sentence is a refusal of Candidate A written
into the page. And the Berserker, who by name ought to be A's home ground, ends on an
inversion I want on the record: *"You are the eye of the storm."* The popular berserker
stands inside the storm; ours **is the still center of it**. Fury, delight, grief and
dance are listed in one breath ("Furious in a fight. Delighted by a meal. Crying at a
poem."), which is Zorba exactly, not Banner. The found fantasy is Candidate C wearing
Candidate A's weather.

Candidate B is refused just as deliberately. Wild Heart ends: *"Now the world of
civilization calls, and you carry the wild things in your heart."* The character walks
toward the walls, carrying the wild in, not burning them down. There is no sneer
anywhere in the five texts, and there should not be: contempt for civilization would
moral-code the class, and our Canon forbids determinism of exactly that kind.

**Rules (Paladin):** My seat's question: does the 2024 kit, as this project implements
it, actually establish C and refuse A? I read the whole training map. It does, and in
places the alignment is word for word. The block follows this deliberation; the three
findings that decide the question are these.

First, **abandon is a decision**. Reckless Attack is an election made at the top of
each turn, one attack roll at a time. The rules make "losing hesitation" a choice, and
a choice is the proof that control was never lost. A possession fantasy would want a
compulsion; there is none anywhere in the class.

Second, **the Rage protects the mind rather than eroding it**. Mindless Rage grants
Immunity to Charmed and Frightened. The one feature whose *name* promises Candidate A
delivers its opposite: while raging, nothing external can grasp you. The name fights
the fantasy; the rule proves it. Our entry text already absorbs the blow ("pure flow:
nothing to grasp, nothing to tame"), but the rulebook name stays on the sheet, and I
log it as a finding rather than write around it.

Third, **presence must be fed**. The Rage ends unless you engage: attack, force a
save, or spend the bonus action to hold it. Read as bookkeeping this is the least
primal rule in the class; read as fantasy it is the fantasy: the moment lasts exactly
as long as you are in it. The entry already frames duration this way, so the tension
dissolves on the page, and I log it anyway for honesty.

**Lorekeeper (Elf Sage):** Two notes from the sources, one on register and one on
depth. The phrase the Paladin just quoted, "nothing to grasp, nothing to tame", is
practically Takuan Sōhō: *The Unfettered Mind* teaches that the mind that stops on
anything is the mind that is seized, and the swordsman's freedom is the mind that
flows past every grasp. That is **mushin**, and it means the found Barbarian already
draws Eastern rather than Germanic, in exact obedience to the standing ruling: our
berserk is flow, not fechtbuch fury. Wuxia knows this figure too; so does every shonen
protagonist who fights best when he finally stops thinking.

The deep note: Primal Champion raises Strength and Constitution to 25, past the mortal
cap. In this project's Canon, realisation actualises the body
(`Dragons-and-the-Overcoming.md`): a person who fully lives their own nature is
changed by it, in the flesh. The level 20 Barbarian is a quiet rhyme with the
Ascending: they have lived their inner nature so completely that the body followed.
Per Canon rule one, **never explain it on the page**, and the found text does not: "You
have mastered your path. Now you walk new horizons." The rhyme is for this room only.

And the class text's third paragraph ("Some name a spirit. Some name a blessing, or a
legacy... Maybe they are all right, maybe they are all wrong") is the
misunderstood-is-load-bearing principle applied to Rage itself. Nobody on the page
gets confirmation. Death of the Author, kept.

**Venustas (Bard):** Then the tone register, which is my seat to decide and I decide it
deliberately. The Fighter reads like a workman's plain report; the Ranger will read
like an adventure novel. The Barbarian's found register is a **chant**: short
declarative beats, drum-rhythm anaphora, a litany you could shout. Hear it: *"You rage
for life. Rage against death. Rage against being tamed. Rage to protect your people."*
Four strikes on one drum. The close breaks into the communal first person, "Barbarians
we are", the same device the Species texts use (the community speaking to the
character), held to a single line so the text stays second person where it lives.

And the register **modulates per Path without changing instrument**. The Berserker
keeps the war-drum. Wild Heart slows it to a listening rhythm: "You listen" struck
three times. World Tree lets the second paragraph run long and unbroken, boundaries
between clauses blurring exactly as the text says boundaries do, then lands on short
awe-beats: "It is beautiful. You are very small." The Zealot opens on three one-word
strikes: "Ecstasy. Fervor. Revelation." One chant, four tempos. That is a house voice
doing its job, and I would not touch a syllable of the rhythm.

One grammar item for Julio rather than for silent correction, since the texts are
his: World Tree's last line reads *"If you can see through the veil, you can cross
them."* Singular veil, plural them. Read generously, "them" reaches back to "all
boundaries" at the head of the paragraph, and the asymmetry may be deliberate: you see
through the one veil, you cross the many boundaries. If it is not deliberate, the
minimal repairs are "cross it" or "see through the veils". Flagged, not fixed.

**Simplicity (Monk):** Length calibration, my one job. Class text: three short
paragraphs, inside the two-to-four law, same density as the Fighter's. Each subclass:
two to three short paragraphs, matching the Fiend's weight class. No em-dashes in any
of the five. No open-choice language in any description; the "choose one option" lines
live in feature entries where the choice is genuinely re-made at the table (Rage of the
Wilds picks its animal each Rage), which `Feature-Text.md` explicitly permits. Dice
appear only in entries, as notation. The single formatting hazard is the Zealot's
`{name}` projection slot: that text is a template, not a constant, and whoever lifts it
must preserve the slot and the render-time fill. No objection from me; there is
nothing here to shrink.

**Rules (Paladin):** Then no unanswered objection stands, provided my two logged
tensions and the Bard's grammar item travel to Julio in the Vox report rather than
being smoothed over. The council's finding is that the found texts already embody the
strongest candidate, and the kit proves it feature by feature.

---

## 📖 The rules read

*Every key feature, and the one line of what it proves about the fantasy. Read from
`Map_of_Barbarian_Training.py` (real source, core plus all four Paths).*

**Core**

- **Rage** — Resistance to Bludgeoning, Piercing and Slashing, Advantage on Strength,
  and no Concentration, no spells: nothing mediated, nothing held at arm's length; the
  will expressed directly. Ends unless fed by engagement: the moment lasts exactly as
  long as you are in it.
- **Unarmored Defense** — AC from Dexterity and Constitution, no material: "You trust
  your reflexes more than any material" is untamed, literally uncovered.
- **Reckless Attack** — abandon is elected each turn, one roll at a time: losing
  hesitation is a choice, which proves control was never lost.
- **Danger Sense** — Advantage on Dexterity saves: instinct as heightened perception,
  not blindness.
- **Primal Knowledge** — while raging, Strength stands in for Acrobatics,
  Intimidation, Perception, Stealth, Survival: the Rage is whole-person, honing
  "agility, bearing, and senses", not a damage rider.
- **Feral Instinct / Instinctive Pounce** — Advantage on Initiative; half your Speed
  as part of entering Rage: "you see further, you move sooner" is mechanically
  literal, and you arrive fist first.
- **Brutal Strike** — forgo Advantage to break the enemy's position: even at its most
  violent the class is choosing, not flailing.
- **Relentless Rage** — the Constitution save at 0 Hit Points: "Rage against death" is
  a rule, not a metaphor.
- **Persistent Rage** — Rage holds ten minutes and survives everything short of
  Unconscious: presence so practiced it no longer needs feeding.
- **Indomitable Might** — the Strength score replaces a lesser total: the trained body
  acting below thought, unguided.
- **Primal Champion** — Strength and Constitution rise past the mortal cap to 25:
  living your inner nature actualises the body. (The Ascending rhyme; deep lore, never
  page text.)

**Berserker**

- **Frenzy** — extra d6s on the first reckless hit: everything committed to the moment
  of contact, nothing held back.
- **Mindless Rage** — Immunity to Charmed and Frightened: nothing external can grasp
  your mind. The 2024 name promises possession; the rule delivers self-possession.
- **Retaliation** — a Reaction attack the instant you are struck: action equals
  reaction with no deliberation between. Mushin as a mechanic.
- **Intimidating Presence** — a 30-foot Emanation of fear: the storm as others see it,
  from outside the eye.

**Wild Heart**

- **Rage of the Wilds** — Bear, Eagle or Wolf, chosen at each Rage: the beasts answer
  when the heart calls, and Wolf spends the Rage on the pack's advantage.
- **Animal Speaker / Nature Speaker** — Beast Sense, Speak with Animals, Commune with
  Nature, Rituals only, from Wisdom: listening, never commanding; the one Barbarian who
  talks with the wild does it slowly, as attention.
- **Aspect of the Wilds** — Owl, Panther or Salmon on a Long Rest: senses and movement
  borrowed from kin.
- **Power of the Wilds** — Falcon, Lion or Ram: Lion draws every nearby enemy's eye to
  you, the guardian's job; the pack fantasy completes.

**World Tree**

- **Vitality of the Tree** — Temporary Hit Points for you at Rage's start and for
  another creature every turn after: connection is the mechanic; the life force flows
  through you and out.
- **Branches of the Tree** — a Reaction that teleports an enemy to your side: space
  bends around your attention.
- **Battering Roots** — reach grows 10 feet, Push and Topple granted: the boundary of
  your arm's length is an illusion too.
- **Travel along the Tree** — a 60-foot teleport, once per Rage 150 feet carrying six
  willing creatures: "if you can see through the veil, you can cross" is the level 14
  rule text, and you carry your people across with you.

**Zealot**

- **Divine Fury** — extra damage, Radiant or Necrotic chosen each time: wrath and
  glory, the god's two hands.
- **Warrior of the Gods** — a pool of d12s spent as a Bonus Action to heal yourself:
  the god maintains its vessel.
- **Fanatical Focus** — a failed save rerolled with a bonus, once per Rage: the
  commandment steadies you at the exact moment your own will slips.
- **Zealous Presence** — a battle cry giving up to ten allies Advantage on attacks and
  saves: the vessel speaks, and the words are not yours.
- **Rage of the Gods** — flight, resistances, and Revivification, which spends a use
  of Rage to set a dying ally's Hit Points to your level: the god's wrath traded,
  directly, for a life. "Rage against death. Rage to protect your people," made into
  one Reaction.

No feature anywhere in the kit compels the Barbarian, removes the player's election,
or punishes the mind for raging. Candidate A is refuted by the rules themselves;
Candidate C is established by them.

---

## 🎭 Tone register

**Chant.** Short declarative beats, drum-rhythm anaphora, one communal line at the
close of the class text. The register modulates per Path (war-drum, listening rhythm,
unbroken cosmic run, ecstatic one-word strikes) without changing instrument. Decided
against: the workman's report (taken by the Fighter), the adventure novel (belongs to
the Ranger), and any archaic saga pastiche (a costume, where the chant is a voice).

---

## 🜂 Subclass analyses

**Berserker** — *Total presence: whatever the moment is, you are the whole of it; the
eye of the storm.* The class fantasy at its purest, undiluted: the Berserker is to the
Barbarian what the Champion is to the Fighter, the Path for a player who wants the
whole fantasy and no subsystem. Zorba the Greek is the register: fury, appetite, grief
and dance given equal rank in one list, so the Rage reads as intensity of *living*, not
of violence. The found text inverts the cliché (the berserker as still center, not
storm), and Frenzy, Retaliation and Mindless Rage all verify: total commitment, instant
response, a mind nothing can grasp.

**Wild Heart** — *Rage as harmony and attention: you listen to the beasts you hunt with
and the beasts you carry.* The class fantasy tuned outward to the living world.
Where the Berserker is the whole of the moment, the Wild Heart is the whole of the
*place*: San of Princess Mononoke, raised by the wild and standing between it and the
walls. The úlfhéðnar's wolf-shirt returns here as kinship rather than possession. The
rules verify a listener, not a commander: every speech with the wild is a Ritual, the
animal powers are answered calls (chosen each Rage, each rest), and half the options
spend the Rage on the pack. The final line walks the character toward civilization
carrying the wild in, which is the found refusal of Candidate B.

**World Tree** — *Rage as awe: every boundary is a veil, and one who sees through a
veil can cross it.* The class fantasy widened to the cosmos. The tree is every
tradition's world-axis at once (Yggdrasil of the Völuspá, the inverted aśvattha of the
Gita) and deliberately none of them by name, per Death of the Author. The nearest
modern kin is the overview effect: "It is beautiful. You are very small. You are part
of it. You are not alone." is an astronaut's sentence. The rules verify connection as
mechanics: life force channeled outward every turn, space folding around your
attention, and a level 14 teleport that brings six of your people across with you.
This Path proves the class text's "Rage to protect your people" is core, not Zealot
flavor.

**Zealot** — *Rage as ecstatic possession: a God fills the vessel, and facing you is
blasphemous.* The class fantasy surrendered upward, and the one Path that flirts with
Candidate A on purpose: someone else *is* driving, and the character is honored, not
erased ("you feel honored and moved" keeps the self present inside the ecstasy). The
lineage is the enthousiasmos of Euripides' Bacchae, Samson's gifted strength, Joan's
voices, the Sufi ecstatic spun past self-consciousness. The rules verify a maintained
vessel (a healing pool, a steadied save) and a conduit that pours outward (the battle
cry, and Revivification spending Rage itself to buy back a life). The `{name}` slot
makes the surrender personal: the sheet prints the character's own name as "nothing
more than a vessel".

Four Paths, one question: *what fills you, when hesitation leaves?* The moment
(Berserker), the living world (Wild Heart), the whole (World Tree), a God (Zealot).

---

## 📜 The proposed texts

*As found in source and vault, presented for Julio's blessing as provisional. Plain
prose, blank lines between paragraphs. The class text lives in `GuildKit.py`; the four
Path texts in `BarbarianKit.py`. Nothing here is newly authored; see the Vox report
for the two items awaiting his word.*

**CLASS_DESCRIPTION (Barbarian)**

```text
Rage is more than just anger. What you carry is more primal: the patience of a predator, the turn of a storm, the cold weight of a sea. You will not be tamed. Your Rage is your will, expressed. You rage for life. Rage against death. Rage against being tamed. Rage to protect your people. Barbarians we are, for we live out our inner nature.

When it comes, you do not lose control. You lose hesitation. You see further, you move sooner, you fixate on your enemy. You move by instinct, without thought, without grace, directly to where you want to hit. Then you run into danger fist first, because someone has to, and because you can.

Nobody agrees what this Rage is. Some name a spirit. Some name a blessing, or a legacy. Some say it is the world's own pain, finding a mouth at last. Maybe they are all right, maybe they are all wrong. You do not have to understand it. You have to feel it.
```

**BERSERKER_DESCRIPTION**

```text
Most people hold something back. You don't. You are a wild horse. Untamed.

When you go, you go all the way. Furious in a fight. Delighted by a meal. Crying at a poem. Dancing through a song. Whatever the moment is, you are the whole of it. Pain quiets. Fear vanishes. You belong in that moment. Nothing else exists. One purpose.

Some find that unsettling. But you could not be any other way. You are the eye of the storm.
```

**WILD_HEART_DESCRIPTION**

```text
Your heart beats to the rhythms of nature. Your rage is harmony, balance, and attention.

There is a bestial instinct that maybe all carry and few listen to. You listen. You listen to the wolves and to the bears. Both the ones you hunt with and the ones you carry in your spirit. You listen to your place in the wilds, and you know you belong.

Now the world of civilization calls, and you carry the wild things in your heart.
```

**WORLD_TREE_DESCRIPTION**

```text
Rage comes to you as awe. A cosmic connection. A veil being lifted from your eyes.

All boundaries are illusions. Now you see the whole: energy flowing under the sea, streams of light through the night skies, every living thing hanging from the same enormous tree. All connected through time and space. It is beautiful. You are very small. You are part of it. You are not alone. If you can see through the veil, you can cross them.
```

**ZEALOT_DESCRIPTION** *(template: the `{name}` slot is filled with the character's
name at render time, and must survive any lift verbatim)*

```text
Ecstasy. Fervor. Revelation.

You are taken by one of the Gods themselves. {name} is nothing more than a vessel for the divine, and a conduit for their wrath and their glory. Guided in your rage by a holy commandment. You can sense exactly what the God wants of you, and you feel honored and moved. You are no longer there, a God is. And facing you is blasphemous.
```

---

## 🕊️ Vox report

**The question.** The Barbarian's core fantasy, whether the 2024 kit establishes it,
and whether the recovered texts carry it.

**What the council found.** The commission expected gaps; there are none in the prose.
All five texts exist as real source, the vault bytecode matches them exactly, and the
commission's brief had misfiled the Berserker's opening line as the class text. What
was missing was this record.

**The choice made.** The found texts embody one fantasy and the council confirms it:
**untamed will, fully present. Rage is your inner nature expressed; you do not lose
control, you lose hesitation.** The evidence chain runs from Zorba, Whitman's barbaric
yawp and the Dionysian through Takuan's unfettered mind, and the rules read verifies
it feature by feature: abandon is always an election (Reckless Attack, Brutal Strike),
the Rage protects the mind rather than eroding it (Mindless Rage), presence must be
fed to last (Rage's duration), and the capstone actualises the body (Primal Champion,
rhyming quietly with the Ascending, never on the page). Tone register: a chant,
modulated per Path. The four Paths refract one question: what fills you when
hesitation leaves? The moment, the living world, the whole, a God.

**The strongest rival.** Candidate A, rage as possession (the sagas' berserkir, the
ríastrad, the Hulk). It is the popular reading and a genuinely great fantasy, but the
2024 rules refuse it at every mechanical joint, and the found texts refuse it in so
many words. Anyone re-opening this class should start by re-arguing A, and should
expect the rules read to defeat them again. Candidate B, wilderness against
civilization (Conan), was refused for moral-coding the class; Wild Heart's final line
is its deliberate counter-statement.

**Open questions for Julio.**

1. **World Tree's last line:** "If you can see through the veil, you can cross them."
   Singular veil, plural them. If deliberate (one veil seen through, many boundaries
   crossed), it stands; if not, the minimal repairs are "cross it" or "see through the
   veils". The council leaves the text as found.
2. **The design record's home:** should a condensed form of this Dialog's commentary
   live above the constants in `BarbarianKit.py` and `GuildKit.py`, the way the
   Warlock patrons carry theirs? The council recommends yes, after the kits leave
   recovery, citing this Dialog.
3. **Logged tensions, for awareness rather than action:** the 2024 name "Mindless
   Rage" fights the no-possession fantasy (the entry text already absorbs it), and
   Rage's round-to-round upkeep reads as bookkeeping unless framed as presence fed by
   engagement (the entry already frames it so).

→ Awaiting Julio's word. The five texts ship as provisional until he gives it.
