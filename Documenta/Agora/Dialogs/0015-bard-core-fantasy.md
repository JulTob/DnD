# Dialog 0015 : the Bard's core fantasy

- **Question:** What is the Bard's core fantasy, does the 2024 ruleset actually establish it, and what should the provisional class and College descriptions say?
- **Raised by:** Julio (commissioned in chat, 2026-08-31, for the beta character generator)
- **Consuls called:** Lorekeeper (Elf Sage), Venustas (Bard), Contracts (Warlock), Simplicity (Monk)
- **Status:** 🟡 converged; texts are **provisional pending Julio's word**

---

## 🧭 Framing

The Fighter is done and sets the bar: its core fantasy (training to beat the limits) was named first, verified against the rules second, and only then written, in second person, inspiration before rule, no mechanics restated, no em-dashes, no open choices. This Dialog does the same for the Bard and its four Colleges in the generator's roster: **Dance, Glamour, Lore, Valor**.

Julio gave no seed. The council must derive the fantasy. Three candidates are on the table:

- **A. Art as literal power over the world.** The song the stones obey.
- **B. The performer who is always on stage.** The persona as armor and weapon.
- **C. The collector of everything worth retelling.** The walking anthology.

Constraints from Canon: `Feature-Text.md` (breaks explicit, dice as notation, no open-choice language, description is identity while the feature entries carry the rules), the alignment-independence every Shape must keep, and the standing ruling that martial and technique fantasy draws on Iberian and Eastern traditions rather than Germanic fechtbücher.

One declaration before we begin. The Venustas seat is embodied by the Bard, and today the council deliberates the Bard. The bias is named so it can be watched.

---

## 🗣️ Deliberation

**Lorekeeper (Elf Sage):** Begin with the oldest evidence, because the Bard is the oldest class in the game in the truest sense: it predates the game by three thousand years. Candidate A is the deep root. Orpheus plays and Hades, who bargains with nobody, bargains (Ovid, *Metamorphoses* X). In the *Argonautica* he does not fight the Sirens, he **outplays** them: a louder, better song, and the crew rows on. Amphion raises the walls of Thebes by lyre, stone moving to keep the beat. Väinämöinen, in the third runo of the *Kalevala*, does not duel young Joukahainen, he **sings him into the swamp**. Tolkien, who knew all these sources, gives the image its purest modern form: Lúthien sings before the dark throne and the mightiest being in the world falls asleep. The recent screen version is *Kubo and the Two Strings*, where a shamisen chord folds paper into armies and tears a leviathan apart. In every one of these, art is not persuasion. It is **physics**.

**Venustas (Bard):** And I will argue candidates B and C before I concede anything, because both are real fantasies players come to this class for. B is the persona: Cyrano composing a ballade *while* duelling and landing the thrust on the envoi's last line; Bowie building Ziggy Stardust, the mask that plays the man; the Fool in *Lear*, the only one licensed to tell the king the truth. B says: the self is the instrument, and it is always tuned. C is Scheherazade, who tells stories for one thousand and one nights because **the telling is literally survival**; the griots of Mali carrying the Sundiata epic for seven centuries of nights; Herodotus writing down every marvel anyone would tell him; Kvothe in *The Name of the Wind*, who is simultaneously A, B and C and is the closest thing this class has to a patron novel.

**Lorekeeper (Elf Sage):** All true, and observe what B and C are made of. Cyrano's ballade only matters because the sword lands **with** it: performance that changes the outcome of the fight. Scheherazade's stories only matter because the sultan's sword does not fall: telling that changes the outcome of the night. Strip candidate A out of B or C and what remains is an actor, or an archivist. Fine people. Not adventurers. A and only A explains why this person walks into a dragon's cave: because the world listens, and they have something to say to it.

**Contracts (Warlock):** My lens is what the rules actually promise, so here is the rules read. Sources: `AtlasLusoris/AtlasOfTraining/Map_of_Bard_Training.py`, `AtlasLusoris/GuildKit.py` (the Bard Guild block), `AtlasLusoris/AtlasOfGuilds/BardKit.py`, all 2024 text.

```
rules read : Bard core
  Bardic Inspiration (1)    your performance edits another creature's d20, up to an
                            hour later, after the roll fails: art retroactively
                            rewrites an outcome.  Candidate A, at level one.
  Spellcasting (1)          "through performance and wit", Charisma: the act itself
                            is the spell.  The medium of the magic is the art.
  Expertise (2, 9)          mastery doubled, twice: the polymath is real.
  Jack of All Trades (2)    half proficiency to every untrained check: candidate C
                            is on the sheet as arithmetic.
  Font of Inspiration (5)   the well refills on a Short Rest: the show goes on.
  Countercharm (7)          your performance shields minds against Charm and Fear:
                            Orpheus against the Sirens, as an Action.
  Magical Secrets (10)      "plundered magical knowledge from a wide spectrum of
                            disciplines", any class's list: the rules call the
                            Bard a collector in so many words.
  Superior Inspiration (18) roll Initiative empty and you regain a use: the
                            performer is never actually out of material.
  Words of Creation (20)    the capstone: Power Word Heal and Power Word Kill.
                            At the top of the class, a word IS life and death.
```

The arc settles the vote. At level 1 your song bends a friend's luck; at level 20 you say a word and someone lives, or dies. The class **begins and ends** on candidate A, and the capstone's own name, Words of Creation, is Väinämöinen's fantasy stated as a feature heading. Candidate C is genuinely present (Jack of All Trades, both Expertises, Magical Secrets) but it is the toolkit, not the drive: it says what you gathered, never why. Candidate B has exactly one class-level hook, Superior Inspiration, and everything else that pays "being watched" lives in two specific Colleges. So: **A is the spine, C is the supporting current, B refracts into the Colleges.**

**Simplicity (Monk):** Then say it in one line before anyone writes a paragraph, or the paragraph will try to be all three.

**Lorekeeper (Elf Sage):** *The world listens. Your art can move it.*

**Venustas (Bard):** Conceded, and gladly, because A gives me the register. But I hold one objection before the tone is set, and it is a rules objection dressed as a voice objection. Say "song" and the class breaks.

**Contracts (Warlock):** Explain.

**Venustas (Bard):** The College of Dance is a full Bard who may never speak, sing, or play a note. If the class description names music as **the** medium, the generator will one day print it above Dazzling Footwork and the sheet will contradict itself. Is a mute dancer rules-legal all the way up?

**Contracts (Warlock):** Verified, and yes. Bardic Inspiration targets a creature that "can see **or** hear you": either sense suffices, so a wordless performance inspires by rules text, not by our indulgence. The class prose must therefore say *art*, and offer song, story, rhythm and word as instances, never as the definition. One honest tension does survive: Words of Creation is verbal even for the dancer. At level 20 the rules say the deepest layer of the art is the Word, whoever you are. I flag it rather than write around it; it is a finding for Julio, and privately I think it is beautiful.

**Venustas (Bard):** Then the register. The Ranger reads like an adventure novel; the Fighter like a training yard at dawn. The Bard's register must be **the told tale**: oral-performance prose, direct address, sentences with a drummed cadence, the rhythm doing quietly what the text claims art does loudly. The description should *demonstrate* the fantasy it names. And I rule out verse now, before anyone is tempted: the Archfey patron is the project's only poem, its commentary says the uniqueness is the device, and I will not spend that coin twice.

**Simplicity (Monk):** Agreed on prose, and I add the discipline: cadence is seasoning, not structure. If a sentence exists for its rhythm alone, cut it. Second, the Death of the Author rule holds with special force here, because this class *invites* lore-dumping: no named courts, no famous ballads, no potted history of minstrelsy. Name the drive; leave the meaning to the player. Third, Lorca.

**Venustas (Bard):** Lorca?

**Simplicity (Monk):** Your candidate A has a failure mode: whimsy. A class about magic songs can come out *cute*, and cute is not a drive. García Lorca's *Juego y teoría del duende* is the corrective, and it is an Iberian source, which the Canon prefers: the duende only arrives, he says, where death is possible. Art that risks nothing moves nothing. Put that edge in the class text and the whimsy problem dies. It also explains, better than any rulebook, why this artist is in the dungeon at all.

**Lorekeeper (Elf Sage):** Seconded, and it closes the circle: Orpheus in the underworld, Scheherazade under the sword, Cyrano on the duelling ground. Every founding image of this class is an artist performing where death is possible. The three candidates were one candidate seen from three seats.

**Contracts (Warlock):** Two more honest findings for the record, then I am content. First: 2024 Countercharm is far smaller than the Siren image it evokes (Advantage against two conditions, for a turn, at the cost of your Action). The class text must not promise that your song silences enchantment; it promises the world listens, which the rules do keep. Second, an editorial drift rather than a design tension: `Feature-Text.md` records seven retraining clauses removed on 2026-08-27, Bard Spellcasting and Magical Secrets among them, yet `Map_of_Bard_Training.py` still carries "you can replace one known spell", "Choose two spells... of your choice", and Lore's "three skills of your choice". Mid-recovery state, not this Dialog's to fix, but Julio should know the sweep has to land again.

---

## 🎭 The Colleges: four refractions

Each College bends the class fantasy (*the world listens; your art can move it*) through a different medium, and the rules were read for every claim below.

### Dance : art that needs no words

**One line:** *You say it by moving, and the fight becomes a dance the whole room ends up dancing.*

The wordless proof of the class thesis. Sources: flamenco and the cante jondo tradition Lorca wrote the duende essay about; the Sufi sema, dance as prayer that reaches something; capoeira, the fight hidden inside a festival; every wuxia sequence where combat is indistinguishable from choreography. The rules are astonishingly coherent here, every feature is *shared movement*: Dazzling Footwork (AC from Dexterity **and Charisma**: being watched is armor, and Bardic damage rides the Inspiration die, art as impact), Inspiring Movement (an enemy steps close, you move, **and an ally moves because you did**), Tandem Footwork (you set the tempo of the whole Initiative), Leading Evasion (partners literally share your evasion). The College's register is kinetic: short beats, movement verbs, almost no abstraction.

### Glamour : beauty as command

**One line:** *Loveliness so complete it is obeyed, worn on loan from a court that still counts you as part of the show.*

Candidate B lands here, transfigured: not the performer's mask but the Fae glamour, beauty with a threat under it. Sources: Titania's court in *A Midsummer Night's Dream*, the terrible splendor of the Sidhe, Galadriel's "all shall love me and despair" refused a ring but kept as a register. The rules say obedience, not affection: Beguiling Magic (your art Charms **or Frightens**, the two faces of glamour), Mantle of Inspiration (your splendor wraps your companions, and they move untouchable, an entourage swept along), Mantle of Majesty (an unearthly appearance and the *Command* spell, every turn: you speak and it is done), Unbreakable Majesty (the attacker **recoils from your majesty** and the blow misses: too beautiful to strike). The register is gilded and slightly dangerous, flattery that turns its edge outward on the last line. The proposed text's closing deliberately half-rhymes with the Archfey patron's poem ("part of the show"): one substance, two doors, flagged for Julio in case he prefers no echo.

### Lore : the collector, whose word cuts

**One line:** *You kept everything worth retelling, and a word placed exactly is a blade.*

Candidate C lands here and gets its teeth. Sources: Scheherazade, the griots, Herodotus, Kvothe in the University archives; and for the cutting edge, the Irish filí, whose formal satire was feared like a weapon (a poet's verse was said to raise blisters on a king's face), together with Sun Tzu: supreme excellence is breaking the enemy without fighting. The rules deliver both halves: Bonus Proficiencies stacked on the class's Expertise (the polymath completed), Magical Discoveries reaching into Cleric, Druid and Wizard lists (the magpie, again named by the rules), Cutting Words (a Reaction that **subtracts your art from reality's roll**: satire as physics), Peerless Skill (the anthology turned inward: you already read how this is done). The register is the wry scholar, wit with an inventory.

### Valor : the deed and the telling are one craft

**One line:** *You keep the beat with a blade: you went where the songs come from.*

The class fantasy carried into the shield line. Sources, per the Iberian-and-Eastern ruling: the juglar of the *Cantar de Mio Cid*, a war epic sung **to** fighting men about a fighting man; the biwa hōshi chanting the *Tale of the Heike*, war remembered as performed rhythm; behind both, the Homeric aoidos singing the glories of men to the men themselves. The rules alternate verse and blow: Martial Training (the weapon **is** the spellcasting focus: sword as instrument, stated as a rule), Combat Inspiration (your die becomes an ally's armor or edge: the war-chant deflects the axe or drives it), Extra Attack with a cantrip woven between the swings, Battle Magic (spell then strike in one measure). The register is the war-drum: heavier stresses, shorter lines, the cadence of marching.

---

## 📜 The proposed texts

*Ready to lift verbatim. Plain prose, paragraphs separated by blank lines; they become Python constants at wiring time. Per `Feature-Text.md`: identity only, the feature entries below them carry every rule.*

**CLASS_DESCRIPTION**

```
You have seen what a song does to a room. The tired sit up. The frightened breathe. The stranger at the back stops reaching for the door. Most people call that a trick of the evening. You knew better, and you went looking for where it comes from.

Here is what you found: the world listens. Stone keeps time. Luck leans toward a voice that means it. What everyone calls art, you learnt as a craft with edges: a rhythm placed where a heart wants to follow it, a word placed where the world is thin. And it answers only when you risk something real. So you risk it, every time.

You gathered everything on the way, because everything is material. A sailor's knot, a court's manners, a surgeon's stitch, half of every trade and the best line of every story you crossed. Other people pack supplies. You pack repertoire.

Play like lives depend on it. They do.
```

**DANCE_DESCRIPTION**

```
Words were never your instrument. You say it with your weight, your line, the turn taken at exactly the right beat. Anyone can watch you and understand.

You learnt that a room follows whoever owns the rhythm. Set the tempo and the fight is a partner dance: the sword arrives where you already were, your friends step when you step, and nobody who watches your feet can find your throat. Some styles hide a war inside a festival. Yours never bothered to hide it.

Armor would only slow the answer. You are quickest exactly where you are most seen.
```

**GLAMOUR_DESCRIPTION**

```
Once, somewhere you can no longer quite find on any road, you performed for a court that does not admit mortals twice. They kept the encore. You kept what rubbed off.

Since then there is a shine on you that practice never earned. Rooms arrange themselves around your entrance. Hearts open a breath before you ask, and what you ask in that breath tends to be done. You dress your friends in a little of the same light, and they walk through arrows like guests of honor.

Be careful how much of it you spend. Beauty of that kind is not a gift, it is a loan, and something in the deep of the woods still counts you as part of the show.
```

**LORE_DESCRIPTION**

```
You never met a piece of knowledge you were willing to leave behind. Ballads, blueprints, funeral rites, the tax code of a drowned kingdom: it all went in the bag, because sooner or later everything is useful, and everything is a story.

The deadliest thing you carry is timing. You know the word that punctures a champion mid-swing, the fact that unravels a sermon, the joke that costs a tyrant the room. Wars have turned on a well-placed verse, and you have an anthology.

Other mages guard their secrets. You find that adorable.
```

**VALOR_DESCRIPTION**

```
Every hall you played had a wall with a sword on it, and a story about the sword that grew with each telling. One night you understood the trade you had actually inherited: the deed and the telling are one craft, and half of it is done in the field.

So you went where the songs come from. You keep the beat with a blade now, verse and blow in the same measure, and the line holds because you are in it, singing. Courage is catching when somebody carries the tune.

When they tell this one, you will not need to exaggerate.
```

---

## 🕊️ Vox report

**The choice made.** The council converged on candidate **A: art as literal power over the world** (*the world listens; your art can move it*) as the Bard's core fantasy, with C (the collector) as the supporting current that explains the toolkit, and B (always on stage) refracted into Glamour and Dance rather than held at class level. The rules read supports this at both ends of the class: Bardic Inspiration rewrites a failed roll at level 1, and the level 20 capstone is literally named Words of Creation. Lorca's duende was adopted as the guard against whimsy: the art in these texts works because something real is at risk. Tone register: the told tale, oral-performance prose in second person with a drummed cadence, no verse (the Archfey poem stays unique), modulated per College (kinetic, gilded, wry, martial). College fantasies: Dance, art that needs no words; Glamour, beauty as command on loan; Lore, the collector whose word cuts; Valor, the deed and the telling as one craft, on Iberian and Eastern war-epic sources per the standing ruling.

**The strongest rival.** Candidate C as the *class* spine: Scheherazade and the griots make the collector a genuine drive (telling as survival), and Jack of All Trades plus Magical Secrets are its rules. It lost because it explains what the Bard gathered and never why the Bard walks toward danger, and because it is exactly the College of Lore's own heart: promoting it to the class would leave that College nothing to refract.

**Open questions for Julio.**
1. The Glamour text's last line deliberately echoes the Archfey poem ("part of the show"). Keep the rhyme between College and patron, or sever it?
2. Words of Creation is verbal even for a College of Dance character: at level 20 the rules make the Word the deepest layer of even a wordless art. The council finds this beautiful rather than broken, but it is a divergence between one College's fantasy and the class capstone, and it is Julio's to bless.
3. Countercharm's 2024 text is much smaller than the Orpheus-versus-Sirens image; the proposed prose stays inside what the rules keep, but if Julio wants the Siren image on the sheet it would need a house rule, not a sentence.
4. Editorial, out of this Dialog's scope: `Map_of_Bard_Training.py` still carries open-choice and retraining language (Spellcasting, Magical Secrets, Magical Discoveries, Bonus Proficiencies) that the 2026-08-27 sweep recorded as removed; the recovery should re-land it.

→ These texts ship as **provisional** pending Julio's word.
