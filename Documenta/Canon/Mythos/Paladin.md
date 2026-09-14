# ⚔️ Paladin: the Sworn, read against the whole setting

> 📖 **In flow.** 1 of 12 chapters is still a proposal. 📜 4 · 📚 2 · 📔 5 · 📖 1

*Mythos analysis, 2026-09-08. Design and literary criticism, not page text. No
Dialog exists for the Paladin; this page does the archetypal read from a blank
sheet, in the shape the Barbarian, Monk and Cleric dialogs established, and then
goes on to the setting relationships and the feature lines. Because nothing was
written, it also drafted a class text and four Oath texts.*

*Landed 2026-09-13. The drafts in §9 are now the shipping text, the lessons
carry their lines, the 2014 layer no longer reaches the sheet, and the steed
is drawn (§12). §10 is the only chapter still in flow.*

**Where the text lives.** Class paragraph and the four Oath paragraphs:
`AtlasOfGuilds/PaladinKit.py`, seated on the Guild Tag by `bind_paladin_voice`
because the vaulted kit built the Paladin without a description, which is the
same repair `bind_cleric_voice` makes for the Cleric. Lessons and their lines:
`AtlasOfTraining/Map_of_Paladin_Training.py`. The steed:
`AtlasOfTraining/Map_of_Paladin_Steeds.py`. The 2014 layer in
`Map_of_Classes/Training/Paladin.py` is trimmed to the three grants that are
mutations rather than prose (health roll, Fighting Style draw, ASI and Epic
Boon feats). Legend register: `arthuriana`, granted by Guild. Oaths on the
roster: Devotion, Ancients, Glory, Vengeance.

---

## 📚 1. What a Paladin player is handed today

*Before (2026-09-08).* A level 11 Tiefling Vengeance Paladin (seed 8) received
the Tiefling entry, a Guard background printed as the wipe's stub (an old hook
title, *"Watcher's Eye"*, in the name slot, and no Hook), the 2024 lessons bare,
the 2014 lessons bare beside them, and a third-person story about "the Horde
League". No class fantasy, no Oath fantasy, no line above any feature. The
Paladin was, with the Monk, the emptiest sheet on the roster, and it is the
Guild with the most legend attached to its name.

*After (2026-09-13).* The same request receives the Guild paragraph, the Oath
paragraph under its own heading, a line above every lesson that reaches the
sheet, and a named steed. Five 2014 features stopped arriving: *Abjure Enemy*
(which printed the literal placeholder "CHA"), *Turn the Unholy*, *Purity of
Spirit*, and the `"Oath of {subclass} feature."` string that stood in for every
Ancients and Glory feature at levels 3, 7, 15 and 20. The Guard's stub is
untouched here and still open (§8, Repairs-Ledger B17).

Two lessons carry no line on purpose. `Spellcasting` and `Fighting Style`
awaken for identity and Pre gates but never render, because `TrainingKit`
suppresses them by name so the Spells section and the drawn Fighting Style feat
can own that prose. The §9 drafts wrote a line for each; both were dropped
rather than shipped into the dark.

---

## 📜 2. The core fantasy: a sentence that does what it says

**Candidate A, the holy knight.** Galahad, the Templar, the crusader, the
white harness. God's champion; the sword as sacrament. Its literature is late
Arthur and the Grail, which the canon has just assigned to the *Celestials* as
their legend register (`crusader`). This is the popular fantasy, and it fails
on two counts. It is the Cleric with a sword: "something watching over you"
plus Divine Smite, and the theology table in the Cleric page needs the two
Guilds to differ. And the 2024 rules cut its cord: a Paladin's power comes
from the Oath, not a god. Nothing on the class chassis requires a deity.

**Candidate B, the sworn one.** Power as the consequence of a word given. The
oath is a *performative*: "I swear" is a sentence that does the thing it names
(Austin, *How to Do Things with Words*). Its literature is older and harder
than Galahad's: Roland at Roncevaux, refusing to blow the horn; the Cid, exiled
by his king and still fighting in the king's name, *"Dios, qué buen vasallo, si
oviesse buen señor"* (God, what a good vassal, if he only had a good lord);
Bhishma, whose name means "he of the terrible vow", fighting on the wrong side
of the Kurukshetra war because he swore to the throne and not to the man on
it; the forty-seven rōnin, who waited two years to keep an oath to a dead
master and were sentenced for keeping it; Hannibal, nine years old at the altar,
swearing to be Rome's enemy for life, and being it. In every one of these the
oath *outlives its reason*, and the sworn one keeps it anyway. That is the
fantasy's hard edge, and it is where the discomfort lives (the Cleric page's
theology table, row four).

**Candidate C, the champion.** The chosen one who fights for others; the
tournament winner; the Superman reading. It is the Fighter's Champion with a
halo, and it has no theology of its own.

**The rules answer B**, and not gently:

| Feature (level) | What it proves |
|---|---|
| Lay on Hands (1) | A pool of healing from nothing but conviction. No spell, no god named. You said you would, so you can. |
| Spellcasting (1) | Charisma. Not Wisdom (listening) and not Intelligence (study): *force of self*. The magic is the strength of the person who swore. |
| Paladin's Smite (2) | Divine Smite is a spell now, cast on a hit with no action. The oath lands *through* the blade. |
| Channel Divinity (3) | Divine Sense: you can *feel* what the oath is against. The Oath feature at 3 names it. |
| Faithful Steed (5) | Celestial, Fey, or Fiendish, your choice. The oath's mount is whatever kind of thing you swore to; the rules refuse to say it must be holy. |
| **Aura of Protection** (6) | *The thesis.* Everyone within ten feet adds your Charisma to their saves. The oath shelters the people standing near the one who swore it. A vow is kept *for* others, and the rule makes that literal. |
| Abjure Foes (9) | The oath is frightening to what it is against. |
| Aura of Courage (10) | Nobody near you can be Frightened. You have already decided, and deciding is contagious. |
| Radiant Strikes (11) | Every hit carries the oath, not only the smite. |
| Restoring Touch (14) | Lay on Hands now ends Charmed, Frightened, Paralyzed: the sworn one's hand returns other people to themselves. |
| Aura Expansion (18) | The circle widens to thirty feet. The oath grows the more people it has held. |

Two verdicts. The holy knight is a *costume* the Oath of Devotion can wear
(and the Aasimar Paladin will, through `crusader`), but the class is the sworn
one. And the whole kit is *outward*: five of the eleven core features do
nothing for you and everything for whoever stands beside you. The Paladin is
the Guild whose power is a radius.

**Register.** The Cleric's is warm scripture; the Fighter's is the training
partner between drills; the Barbarian's is a chant. The Paladin's should be
**the oath, remembered**: second person, present tense, but with one sentence
in it that the character once *said*, never quoted, and everything else the
cost of having said it. Austere, not warm. No "watched over" (the Cleric's),
no "nobody gave you this" (the Fighter's), no "you will not be tamed" (the
Barbarian's).

---

## 📜 3. The name, and the oath-breaker next door

*Palatinus*: of the palace, from the Palatine Hill. The royal guard, the
imperial one. Charlemagne's Twelve Peers. By the pattern the Barbarian and Monk
pages found, the Guilds are named in somebody's vocabulary, and this one is the
**Goliaths'**: `rome` (the legion, the road, the Palatine) is theirs, while
`vatican` is the Celestials'. The Paladin is named by the Giants, and since the
Goliaths are the civilisation that fell, the class name means *the guard of a
palace that is gone*, which is the oath outliving its reason. The founding text is the *Song of Roland*, and the Song
of Roland happens at **Roncevaux, in the Pyrenees, against the Saracens of
Zaragoza**. In this setting that is the Dwarves' border, and the enemy in the
poem is the Dwarves' other half (`andalus`). ✅ The Paladin's founding myth is
set on the Dwarf frontier and its villain is the Dwarves' own second key.
Nothing on the page; a Dwarf Paladin's DM should know it.

And the Guild's *own* legend register is `arthuriana`, which the canon has
just defined as **early Arthur: the fallen garrison, the warlord, the caste of
knights that outlived the reason for it. A decline myth.** ✅ The register
agrees with the theology by accident: a generated Paladin carries a Kingsword
and a Questing Lance from the *aftermath* stratum, the knight of a garrison
whose empire is gone. The oath outlives its reason in the vocabulary too.
(The Aasimar Paladin alone adds `crusader`, the election stratum, and reads
as Galahad; everyone else reads as Bedivere.)

**The oath-breaker.** *Warlock* is Old English *wǣrloga*: oath-breaker,
covenant-liar. ✅✅ **In the setting's own vocabulary, a Paladin who breaks the
oath is, etymologically, a Warlock.** The 2024 PHB removed the Oathbreaker;
the language did not. The two Guilds are sworn and forsworn, and the Warlock's
whole fantasy (a pact, terms, "you, mine") is what an oath becomes when it is
made to something that will collect. This should never be stated on a sheet.
It should govern how the two class texts end: the Paladin's on the morning
the vow is not chosen, the Warlock's on the terms. Thread for the Warlock page
and for a page on the names of the Guilds.

---

## 📚 4. Four oaths, four wells

| Oath | The vow, in one line | Mythic well (Iberian and Eastern where martial) | Rules echo |
|---|---|---|---|
| **Devotion** | Sworn to a *way of being*, which has no enemy and therefore cannot be finished. | Galahad (crusader, Aasimar). The Cid's honesty. Yudhishthira, who cannot lie and is made to. The Dragonborn's "which hand takes the cup". | Sacred Weapon *sheds light* while you fight: the sworn one cannot bear to fight where nobody sees what they are doing. Aura of Devotion: nobody near you can be Charmed, talked into being someone else. Holy Nimbus: sunlight. |
| **Ancients** | Sworn to what was here first: the green that returns, the light, the laugh in the dark. Gods are newer than that. | *Sir Gawain and the Green Knight* (the oath kept with the fae; the beheading game; the girdle). Herne, the Wild Hunt. `fairytale_fae` (Elf, Fae, Goblin). The Goliath's First Ones. | Nature's Wrath restrains with vines. Aura of Warding: resistance to *spells*, the old things against the new art. **Undying Sentinel: "you suffer none of the drawbacks of old age"**, the oath gives the sworn one the old things' agelessness. Elder Champion: the Green Man, regenerating. |
| **Glory** | Sworn to be *worth telling*. Not to win; to be a story. | Achilles choosing the short life and the long name (`homeric`, Goliath). Guan Yu, who kept the Peach Garden oath and was made a god for it. **Don Quixote**, the Iberian knight errant (Dwarf). Roland's pride: the horn not blown. | Inspiring Smite: your deed gives *others* Temporary Hit Points, the story feeds the people watching it. Peerless Athlete: the games. Aura of Alacrity: the crowd runs with you. **Living Legend: "the legends, whether true or exaggerated, of your past deeds"**, which is Don Quixote as a level 20 feature. |
| **Vengeance** | Sworn *against*, not for. Everything else in the oath is instrument. | The forty-seven rōnin (Chūshingura: vengeance as duty, honoured and executed). Hannibal's oath at nine (`carthage`, Human). Nemesis, retribution as *balance*, distinct from the Furies' rage. The Count of Monte Cristo. The Cid on the Infantes of Carrión. | Vow of Enmity, transferable when the target drops: the vow does not end with one death. Relentless Avenger closes the retreat. Soul of Vengeance answers every swing. **Avenging Angel: you sprout wings.** |

⚠️ The Oaths are alignment-free in 2024 and must stay so on the page (the
project's backgrounds law extends naturally: never moral-lock a Guild). The
generator produced two Lawful Evil Paladins in two seeds. That is a story, not
a fault: a Lawful Evil Devotion Paladin is the Cid serving a bad lord, and a
Lawful Evil Vengeance Paladin is Hannibal. The texts below moral-lock nothing.

---

## 📔 5. The Paladin inside the setting's metaphysics

**Sworn, not kept.** The Cleric's greater thing loves first; the Paladin's is a
word the self gave. The Cleric's hand "was held out before you reached for
it"; the Paladin's power exists *because* they reached. This is the whole
class boundary, and the drafts in §9 keep it: nothing in the Paladin text
watches over anyone.

**The oath and the Ideal.** An Aasimar's Ideal is "fixed and incapable of
compromise". An oath is also fixed and incapable of compromise. ✅ The Aasimar
Paladin is the one Character on the roster for whom blood and vow *agree*,
which is exactly why the canon notes it reads flatter (five markers) and why
the interesting Aasimar Paladin is the one whose Oath *contradicts* the Ideal:
Mercy's spark sworn to Vengeance; Freedom's spark sworn to Devotion. The
aureola's tell will show the strain every session.

**The oath and the self-authored dragon.** A dragon "owes nobody anything" and
resists godhood because gods are bound by others' wills. A Paladin is bound by
their *own* will, once, forever. ✅ The Dragon and the Paladin are the two
purest self-authored beings in the setting and they answer the question
opposite ways: the dragon keeps authoring, the Paladin authored once and
stopped. A **Dragon Cultist Paladin** is the canon's failure case in one body:
"a self authored to someone else's specification is precisely the thing that
has to be overcome", sworn to a being who despises oaths. Story, not fault.

**The oath and the Dream.** An Elf sworn to the Ancients is sworn to what was
here first, and what was here first, for an Elf, is the Fae, which is the
Dream, which is *their own species' subconscious*. The Elf Ancients Paladin has
sworn fealty to the thing that is quietly shaping their body over centuries.
Never say so. ⚠️ One rules wrinkle: Undying Sentinel's "you suffer none of the
drawbacks of old age" gives an Elf nothing they did not have. The oath grants
what the blood already had, which is either a dead clause or a story ("the
oath asked for the one thing you could give without cost").

**The oath and the Order of Things.** The Goliath tends "everything they
made, for that is our duty". Duty is the Goliath's word before it is the
Paladin's, and `arthuriana` is the Goliath's register before it is the
Paladin's. ✅ The Goliath Paladin is the roster's most native pairing after the
Goliath Barbarian: the knight of the fallen garrison, from the fallen
civilisation. "The greater they fall."

**The oath and the theological shift.** A Tiefling Vengeance Paladin at 20
sprouts wings and becomes an *Avenging Angel* with horns. ✅ The canon says the
horns once held a flame and the reading changed, not the horns. The rules put
wings on the condemned. That is the shift reversed for one hour a day, by a
vow, and nobody in-world will read it correctly.

---

## 📔 6. Relationships: species × Paladin

| People | The seed | Oath that sings | Note |
|---|---|---|---|
| **Aasimar** | Blood and vow agree; five markers; Galahad. | Devotion (native), Vengeance (the strain). | The Ideal's tell shows the oath's cost. |
| **Goliath** | Duty is theirs; `arthuriana` is theirs. The Iliad gives Glory its hero. | Glory, Devotion. | ✅ Most native pairing. |
| **Dwarf** | The Cid; Roncevaux on their border; Santiago and Calatrava (the Iberian military orders are the crusader register on the Iberian key); **Don Quixote**. Metal given, proven by the oath. | Glory (Quixote), Devotion (Santiago). | ✅ The Dwarf Glory Paladin is the last knight errant, and Living Legend is his feature. |
| **Human** | `arthuriana` twice (species and Guild). **Hannibal's oath** on the `carthage` key: sworn at nine, kept for life. | Vengeance. | ⚠️ The default knight, and the cliché's landing zone. Carthage rescues it. |
| **Elf** | Gawain's girdle; the Wild Hunt; sworn to the Dream. | Ancients. | The Undying Sentinel wrinkle (§5). |
| **Orc** | "No orc was asked." The plains fenced. | Vengeance (the species grievance), Glory (the rider's kleos). | ✅ An Orc Vengeance Paladin's vow is the whole species entry. |
| **Dragonborn** | "How to greet a superior… which hand takes the cup." The oath as etiquette; the codified clan. | Devotion. | ✅ The class in species clothing; "expectation crushes people" is the cost. |
| **Tiefling** | Avenging Angel with horns (§5). Sworn to the thing that condemned them, or against it. | Vengeance, Devotion. | ✅ Aura of Devotion: "nobody near you can be Charmed", the one who cannot be told what they are. |
| **Halfling** | An oath sworn in a place where oaths were never needed. Aura of Courage as a species trait. | Ancients (the green valley). | ✅ The Halfling who swore because nobody else in paradise would. |
| **Gnome** | "Your own keep their ways in things." The oath as the thing carried; Sacred Weapon as heirloom. | Devotion. | The vow is in the object. |

---

## 📔 7. Relationships: backgrounds × Paladin

- **Squire.** "You stood where you were told and did not run." Reinforcement,
  and the Paladin's most obvious background. The interesting Squire Paladin
  swore *to the master*, and the master is gone: "a promise your master made
  and cannot keep" is now the oath.
- **Servant.** "Indentured… They still own you." ✅ **The false oath.** The
  Servant swore to the wrong household and Aura of Devotion says nobody near
  them can be Charmed. The Servant Paladin is the one person in the aura still
  hearing "my cup is empty".
- **Herald.** "Any means necessary." Against Devotion's honesty. ✅
  Contradiction that is a story: the Herald Paladin owes two masters, and the
  power's errands and the oath's tenets will collide, and the sheet promises
  nothing about which wins.
- **Renegade.** "There are rules. Yours. Nobody in the crew goes hungry."
  ✅ **The oath of the streets.** A Renegade Devotion Paladin swore to a gang,
  and the oath is as binding as any chapel's. The best proof the Oaths are
  alignment-free.
- **Sellsword.** "You never fought for a flag, only for a fair price and the
  good name that brings the next contract." ✅ The Glory oath in commercial
  clothes: the good name *is* the vow.
- **Survivor.** "So you went back. For revenge, and something more." Vengeance,
  obviously; the more interesting reading is the Survivor who swore Devotion
  *because* revenge was what it wanted from them.
- **Inquisitor.** "An instrument does not need to be clean, only sharp." The
  demanding parent's child (Cleric) or the sworn one (Paladin)? The Inquisitor
  Paladin swore to the left hand, and "you do not sleep well" is the oath's
  cost written down.
- **Bailiff.** "You served the law, not justice." ✅ Against Devotion's tenets,
  the Badge and the Oath are two authorities in one coat, and the Badge can be
  called back while the Oath cannot.
- **Gambler.** "You have never in your life left a table before it was
  finished." ✅ Glory: the oath as the refusal to fold.
- **Fated × Ancients.** "You were promised to a witch." ✅ The oath sworn *for*
  you by somebody else; the Fated Ancients Paladin swore back. The Fae claimed;
  the Paladin answered with a vow. Gawain, again.
- **Destined × Glory.** Reinforcement, and comic: "born under a star" plus
  Living Legend is a Character who is right about themselves.
- **Dragon Cultist.** The canon's failure case (§5). "Someday you will become
  your own Master" against an oath that was sworn to one.
- **Stranger × Vengeance.** "A shop burned, a permit revoked, a girl taken by
  men who will not show the warrant… You are the one who can go." ✅ Vow of
  Enmity as the diaspora's errand.
- **Guardian.** Reinforcement; fine.
- **Tomb Raider.** "Everyone says the dead should be left in peace. You are
  going back down tomorrow." A sworn one who swore to the wrong thing, or the
  Ancients Paladin who swore to what is under the ground. Story.

---

## 📔 8. Flags

### ✅ Singular, and to be protected

1. **Aura of Protection as thesis.** The Paladin is the Guild whose power is a
   radius. Every line keeps the oath *outward*.
2. **The register agrees with the theology.** `arthuriana` is the aftermath
   stratum; the oath outlives its reason in the vocabulary.
3. **Warlock = oath-breaker** (§3). Sworn and forsworn, next door.
4. **The Tiefling Avenging Angel** (§5). Already in the rules.
5. **Don Quixote is Living Legend** (§4). The Dwarf Glory Paladin.
6. **Hannibal's oath on the Human key** (§6).
7. **The unquoted sentence** is the Guild's device (§9). Five texts refer to
   the sentence the Character swore and none of them prints it. The blank is
   what the sheet hands back to the player, and it is the one line a generator
   must not write for them.
8. **The steed is drawn in the Oath's own nature** (§12). The first thing in
   the rules that answers the word rather than the person.

### ⚠️ Stock, contradictory, or thin

1. ~~**Nothing is written.**~~ ✅ Landed 2026-09-13: class text, four Oath
   texts, a line on every rendered lesson, and the five leaking 2014 features
   gone. `Spellcasting` and `Fighting Style` are the two lessons with no line,
   and that is deliberate (§1).
2. ~~**The holy-knight costume**~~ ✅ answered by the class text, which names
   no god and no deity anywhere in its three paragraphs. The feature list is
   still full of "Radiant", "Holy", "Sacred" and "Divine", because those are
   rules and rules keep their words; it now sits under prose that says the
   power came from a sentence.
3. **The Guard background** renders under an old hook title ("Watcher's Eye")
   where its name belongs. It is one of the stubs the 2026-08-29 wipe left in
   `BackgroundKit.py` (Repairs-Ledger B17); the settled Guard, with its Hook
   *Network of Favors*, is on Backgrounds-Official. **Still open.**
4. **The Human Paladin doubles `arthuriana`** and is the flattest pairing.
5. **Undying Sentinel gives an Elf nothing** (§5). The shipped Ancients text
   takes the second reading and says the oath asked for the one thing the Elf
   could give without cost: *"That was not asked for. It came with the word."*
6. **"Yolande's Regal Presence"** on the Glory list is a proper noun from the
   2024 book. Spell names are rules, and rules may keep them; but it is the
   only named person on the Paladin sheet, and it is a stranger.
7. **The Cleric's legacy module does not roll health** the way the Paladin's
   does, and the two were compared while trimming this one. Either the Cleric
   is short its per-level Hit Die or health arrives elsewhere for it. Not
   investigated here; recorded because the comparison was in hand.

---

## 📜 9. The texts, as shipped

*House rules: second person; no em-dashes; no proper nouns; no open choices; no
"watched over"; the oath is never quoted. Plain prose for the Guild block and
the four `extends=` texts, then italic lines for the features.*

**Landed 2026-09-13, as drafted.** The five paragraphs below are the shipping
text, word for word, in `AtlasOfGuilds/PaladinKit.py`; the feature lines are in
`AtlasOfTraining/Map_of_Paladin_Training.py`. Three notes on the crossing from
draft to code, because a later hand will want to know what moved:

1. **Two lines were dropped, not forgotten.** `Spellcasting` and `Fighting
   Style` never render (§1), so the lines drafted for them would have been
   written into the dark.
2. **The Faithful Steed line kept its wording and gained an object.** *"You did
   not ask what kind"* now stands over a sheet that names the kind, which is
   the point: the oath answered, and the answer was not a preference (§12).
3. **The device was named.** The register was already fixed as the oath
   remembered; what the text *does* is refuse to quote the sentence. Across the
   five texts the sentence is called a sentence, a word, a vow and the thing
   you said, and it is never given. The blank is what the sheet hands back to
   the player. Recorded in the Guilds table as the eleventh device.

### Class text (new)

```
You said something out loud once, and it has been true ever since. That is the whole of it. Others carry a god, or a grudge, or a gift they were born holding. You carry a sentence. You chose the words, and the words chose everything after.

Power came with it. Not as a reward. As a consequence. Your hand closes a wound because you said it would. Your blade burns because you said what it was for. Stand near you and the fear goes out of people, because you have already decided, and deciding is contagious.

The word does not care whether you still want it. That is the terrible thing about a vow, and the reason it works. Kings die. Causes rot. The reason you swore may be dust by now. The sentence stands, and you stand where it stands. Every morning you choose it again. One morning you will find out what happens if you do not.
```

### Oath of Devotion (new)

```
The oldest oath, and the hardest, because it has no enemy. You swore to nothing that can be killed. You swore to a way of being: honest when a lie would save you, brave where nobody would know you ran, kind when kindness is expensive.

So there is no finishing it. There is only this morning, and the next, and whether the thing you said is still true in the way you stand. Your blade gives light while you fight. You could not bear to fight where nobody can see what you are doing.

People near you cannot be talked into being someone else. You have never once been talked out of this.
```

### Oath of the Ancients (new)

```
You swore to what was here first. The green that comes back. The light that returns after the longest night. The laugh in the dark. Gods are newer than that, and you did not swear to gods.

The old things keep their side. Vines answer you. New magic breaks against the people you stand beside, because what you serve was here before spells were. And the old things do not age, so neither, quite, do you. That was not asked for. It came with the word.

There will be a night when the light is nearly gone and you are what is left of it. That is the oath. Kindle it, shelter it, and do not let it go out in you.
```

### Oath of Glory (new)

```
Others swore to a cause. You swore to be worth the telling.

Not to win. Winning is a fact, and facts are forgotten. You swore that when they tell it afterwards, it will be worth their breath: the leap that should have failed, the line held past sense, the deed that made the people watching it braver. When you strike, the ones around you stand straighter. That is the story feeding on itself, and you are the story.

The danger was always that you would prefer the telling to the deed. You know the sound of a horn not blown. You will not be that story.
```

### Oath of Vengeance (new)

```
You swore against. Everything else in the oath is instrument.

Somewhere there was a wrong big enough that a life is the right size of answer, and you gave the life. Not in fury. Fury runs out. This is a ledger, and you are the hand that closes it: the vow named on one enemy, and when that one falls, carried unspent to the next. They cannot run. You have made sure of that. They cannot swing without an answer.

Mercy is not forbidden to you. It is simply not what you promised, and you do not promise twice. One day the wings come, and you find out what the wrong made of you.
```

### Feature lines: core

| Lesson | Draft |
|---|---|
| **Lay on Hands** (1) | *A pool of mending from nothing but the word. You said you would. So you can.* |
| **Spellcasting** (1) | *The magic is the strength of the one who swore. It is exactly as strong as you are.* |
| **Weapon Mastery** (1) | *The vow needs a hand it can land through.* |
| **Fighting Style** (2) | *You chose a way to stand, and you have stood that way since.* |
| **Paladin's Smite** (2) | *The word goes into the blow. Whatever you hit finds out what you promised.* |
| **Channel Divinity** (3) | *You can feel what the oath is against. It is never far.* |
| **Extra Attack** (5) | *Twice, because once was a wish and the vow is not a wish.* |
| **Faithful Steed** (5) | *Something answered the oath and agreed to carry it. You did not ask what kind.* |
| **Aura of Protection** (6) | *Stand near you and the vow covers them too. That is what it was for.* |
| **Abjure Foes** (9) | *Whatever the oath is against knows it, and steps back.* |
| **Aura of Courage** (10) | *You have already decided. Deciding is contagious.* |
| **Radiant Strikes** (11) | *Every blow carries the word now, not only the ones you spend on.* |
| **Restoring Touch** (14) | *Your hand gives people back to themselves. Somebody once did that for you, and you swore.* |
| **Aura Expansion** (18) | *The circle widens. The vow has held more people than it was made for, and it grew.* |

### Oath of Devotion

| Feature | Draft |
|---|---|
| **Sacred Weapon** (3) | *Your blade gives light. You could not bear to fight in the dark.* |
| **Aura of Devotion** (7) | *Nobody near you can be talked into being someone else.* |
| **Smite of Protection** (15) | *The word lands, and it shields the one it struck through.* |
| **Holy Nimbus** (20) | *There is nowhere near you left to hide, including from yourself.* |

### Oath of the Ancients

| Feature | Draft |
|---|---|
| **Nature's Wrath** (3) | *What was here first still has hands.* |
| **Aura of Warding** (7) | *New magic breaks against the old. You are standing on the old.* |
| **Undying Sentinel** (15) | *The old things do not age. Neither, quite, do you. It was not asked for.* |
| **Elder Champion** (20) | *The green comes back. For a minute, it comes back through you.* |

### Oath of Glory

| Feature | Draft |
|---|---|
| **Inspiring Smite** (3) | *The deed feeds the ones who saw it.* |
| **Peerless Athlete** (3) | *Nine or lower is a number for people who are not being watched.* |
| **Aura of Alacrity** (7) | *The crowd runs with you. It always has.* |
| **Glorious Defense** (15) | *Another's failure, turned into your story, and their survival.* |
| **Living Legend** (20) | *Whether or not it happened that way, it is told that way, and the telling is armour.* |

### Oath of Vengeance

| Feature | Draft |
|---|---|
| **Vow of Enmity** (3) | *One name. When it falls, the vow does not; it moves.* |
| **Relentless Avenger** (7) | *They cannot run. You made sure of that a long time ago.* |
| **Soul of Vengeance** (15) | *They cannot swing without an answer.* |
| **Avenging Angel** (20) | *The wings come. You find out what the wrong made of you.* |

---

## 📖 10. Threads to pull in later cycles

- **Warlock**: sworn and forsworn (§3). The Warlock page must confirm
  "noticed" survives all four patrons, and should end on the terms, as this one
  ends on the morning.
- **Fighter**: the Champion vs the Glory Paladin. Two Guilds about being
  watched by a crowd; decide who owns the laurel.
- **Aasimar**: blood and vow agree; the interesting Aasimar Paladin has an Oath
  against the Ideal.
- **Dwarf**: Roncevaux, the Cid, Santiago, Quixote. The Dwarf page should
  record that the Paladin's whole founding literature happens on their border.
- **Official backgrounds**: the Guard's old hook title in the name slot goes
  when the settled records reach the sheet (Repairs-Ledger B17).
- **Names of the Guilds**: barbaros, monachos, palatinus, wǣrloga. A page on
  who names whom.
- **The steed and the background.** §12 keys the steed's kind to the Oath,
  because the Paladin page's own reading of Find Steed says the mount is
  whatever kind of thing you swore to. The alternative was the **background**,
  which is what the exotic familiars use: a Renegade's steed and a Squire's
  would not be the same animal, and the Servant Paladin's steed could be the
  one thing that is theirs. That is richer and it couples the module to the
  backgrounds; it was left unbuilt rather than rejected. If it is taken up, the
  kind should stay the Oath's and only the *shape* should answer the
  background, or the device stops saying what it currently says.
- **A Kit for drawn objects.** Three implementations now exist that share no
  code (Spellbook by tool, familiar by patron, steed by Oath). The third was
  written by reading the second. Guilds page §3 has wanted the Kit since it
  was compiled; the steed is the argument that it should be built before the
  Bard's instrument makes four.


---

## 📔 11. Oath Spells

| Feature | Line |
|---|---|
| Oath Spells | *The oath comes with a vocabulary. These are the words it lets you say.* |

---

## 📜 12. The steed

*Landed 2026-09-13. `AtlasOfTraining/Map_of_Paladin_Steeds.py`. This closes the
Paladin's row in the signature-objects table (Guilds page §3), which read
"Celestial, Fey, or Fiendish, your choice" and ⚠️ unbuilt.*

**Why it had to be drawn.** Find Steed offers the player three kinds. A
generated sheet may not print that offer: `Canon/Feature-Text` forbids
open-choice language, because every pick was made inside a seeded Dice Bag
before the page existed. The sheet was carrying "(your choice)" on a character
nobody will ever level up. So the lawful fix was to draw it.

**Why drawing it is the better fantasy, and not merely the legal one.** The
Paladin's power is downstream of a word. The steed is the first thing in the
rules that answers *the word* rather than the person: you did not summon a
servant, you said something once and something agreed with it. That is why the
kind follows the **Oath** and never the Character's alignment, species or
manners, and why the feature's line is *"You did not ask what kind."* The line
and the drawn kind are not in tension. They are the whole reading.

**The two rules of the pool**, in the shape `Map_of_Spellbooks` fixed for the
Wizard's book.

1. **The oath is answered in its own nature.** Devotion and Glory are met by
   the Celestial, Ancients by the Fey, Vengeance by the Fiendish. Devotion and
   Glory share one kind for different reasons: one swore to a way of being that
   keeps its word, the other swore to be worth telling, and a story gives its
   hero a white horse. This is the Pact of the Chain's *Familial Preference*
   asked of an Oath instead of a patron, and it reuses that module's weight.
2. **Nothing is excluded.** A weight is not a gate. Measured over sixty seeds
   per Oath, the oath's own nature answers about five times in six:

   | Oath | Celestial | Fey | Fiendish |
   |---|---|---|---|
   | Devotion | 50 | 4 | 6 |
   | Ancients | 6 | 48 | 6 |
   | Glory | 50 | 4 | 6 |
   | Vengeance | 6 | 7 | 47 |

   So roughly one Paladin in six is answered by something nobody expected, and
   the rules deliberately allow it: they refuse to say the steed must be holy.
   A Devotion Paladin carried by something Fiendish is a story, and the sheet
   states it without apology. Seed 42 at level 11 is one.

**Twelve shapes, four to a kind**, each completing *"and it came as ..."*. They
are written to be ridden rather than admired, and none of them is a monster: a
mare who will not cross running water until she is asked politely, a lion that
has never once roared in your hearing, a ram whose horns ring like struck iron.

**Where it is settled.** `Draw_Steed` runs from the lesson's `apply`, never
from its Entry, which is the Primal Order rule in `Canon/Feature-Text`: an
Entry that decides re-decides on every read of the sheet. Verified: five reads
of one sheet give one answer, and the same request replays to the same steed.
