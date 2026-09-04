# Dialog 0013 — The Artificer's core fantasy

- **Question:** What is the Artificer's core fantasy, and what provisional class and
  subclass descriptions follow from it for the beta character generator?
- **Commissioned by:** Julio (chat, 2026-08-31), as part of the provisional-descriptions
  drive: find the core fantasy through archetypal analysis, verify the rules establish it,
  then write the prose in a register that fits the class.
- **Consuls called:** Lorekeeper (Elf Sage), Venustas (Bard), Testing (Rogue),
  Workshop (Artificer)
- **Status:** 🟡 provisional — the texts below ship as provisional and await Julio's word.

---

## 🧭 Framing

The Artificer's kit file (`AtlasLusoris/AtlasOfGuilds/ArtificerKit.py`) is a stub: four
`Build_Specialization` calls and nothing else. The rules live in
`AtlasLusoris/AtlasOfTraining/Map_of_Artificer_Training.py` (source:
*Eberron: Forge of the Artificer*, 2024), and the guild chassis in `GuildKit.py`
(INT primary, CON secondary, d8, CON/INT saves, medium armor, Adept vocation). The
descriptions proposed here will be wired later through `extends=`, the way the Warlock
patrons and Fighter shapes already hang.

Constraints from Canon, all binding:

- `Feature-Text.md`: the description is identity and drive, never a summary of mechanics.
  The feature entries below it already state every rule.
- Death of the Author: no proper-noun worldbuilding, no lore dumps. The reader inhabits;
  the design team keeps the references in files like this one.
- No em-dashes in authored prose. No open-choice language: the generator already chose.
- Martial and technique fantasy draws on Iberian and Eastern traditions (Decree standing:
  La Verdadera Destreza, Sun Tzu, kendo; the fechtbücher were rejected).
- Length: class 2 to 4 short paragraphs, subclass 1 to 3, at Fighter/Fiend density.

Candidates on the table, from the commission:

- **A. The inventor whose mind outruns the world.** The lone genius: Nemo, Tony Stark,
  the Leonardo of the notebooks.
- **B. The tinkerer who makes wonder from junk.** Improvised marvels: the scrap-built
  glider, the workshop under the stairs.
- **C. Magic as an engineering discipline.** The refusal of mystery: magic obeys laws,
  laws can be learned, what is learned can be built.

Subclasses to cover, per the generator's roster: Alchemist, Armorer, Artillerist,
Battle Smith.

---

## 🗣️ Deliberation

**Workshop Consul (Artificer):** Before anyone objects: yes, this seat is deliberating
its own guild. I will argue from the craft lens only, what making actually feels like,
and leave the vanity outside the door. If I drift, say so.

**Lorekeeper (Elf Sage):** Then let me lay out the three candidates with their sources,
because two of them are going to turn out to be the same candidate and one is going to
turn out to be wrong for this class in a way the rules will prove.

**Candidate A, the mind that outruns the world.** The pedigree is glorious: Captain Nemo
in *Twenty Thousand Leagues Under the Sea*, decades ahead of every navy on earth; Tony
Stark in *Iron Man* (2008), who builds the future in a cave, with a box of scraps; the
Leonardo of the notebooks, sketching helicopters four centuries early. The fantasy is
being *ahead*: the world has not caught up to you and it is not going to.

**Candidate B, wonder from junk.** MacGyver's paperclip, Hiccup's prosthetic tail fin in
*How to Train Your Dragon*, the scrap-cobbled marvels of *Girl Genius*, WALL-E stacking
his little treasures. The fantasy is transfiguration: the world throws things away and
you see what they still want to become.

**Candidate C, magic as engineering.** *Fullmetal Alchemist* is the cleanest statement:
alchemy has laws, the laws have consequences, and understanding is paid for. Ted Chiang's
"Seventy-Two Letters" makes naming itself an engineering discipline. Le Guin's Earthsea
gives magic a school with homework. The fantasy is the refusal of mystery: what the
wizard calls a miracle, you call a mechanism that has not been drawn yet.

**Venustas (Bard):** I will note now, so it shapes the reading rather than decorating it:
A is a *solitary* fantasy. Nemo shows no one his engines; the Leonardo of legend wrote in
mirror-script and published almost nothing. If A is the core, the register is hauteur,
the genius misunderstood. I can write that voice. I do not love it for a guild whose
chassis is a party role.

**Testing Consul (Rogue):** Then stop reading media and read the rules, because they
settle exactly that point. I went through every core lesson in
`Map_of_Artificer_Training.py`. The rules read, feature by feature, one line each on
what it proves about the fantasy:

```
Spellcasting            INT casts through Thieves' or Artisan's Tools; the mystery
                        has a workbench
Tinker's Magic          the smallest wonder is put INTO an object, not held in the hand
Replicate Magic Item    wonders come from known plans, remade every Long Rest; a
                        miracle that repeats is a method
Magic Item Tinker/      attunement 4, then 5, 6, 7: growing capacity for wonders,
  Adept/Master          including other people's
Flash of Genius         a Reaction that spends YOUR Intelligence on SOMEONE ELSE'S
                        roll, 30 feet away
Magic Item Adept        crafting faster and cheaper: production, not revelation
Spell-Storing Item      your spell stored in a weapon or focus so that ANOTHER
                        creature casts it while you are elsewhere
Advanced Artifice       Artificer spells cast through Tinker's Tools without a slot;
                        by the end, the tools ARE the magic
Soul of Artifice        at 0 HP you survive by ENDING one of your own infusions:
                        the made gives itself back for the maker
```

Two findings, and the first is the important one. **The kit is distributive.** Flash of
Genius, Spell-Storing Item, the Alchemist's elixirs, the Artillerist's Protector cannon,
the Battle Smith's defender: over and over, the mechanical text takes what is in the
Artificer's head and puts it in somebody else's hands. Candidate A, the hoarding genius,
*fights these rules*. Nemo would never build a Spell-Storing Item; the whole point of
Nemo is that nobody else gets to drive the Nautilus. If we write the lone mind ahead of
the world, the sheet under the description will contradict us six times before level 11.

Second finding, smaller: nothing in the core kit is about junk. Replicate Magic Item
wants plans and proper tools; Tinker's Magic wants Artisan's Tools in hand. Candidate B's
scrap-heap poetry is charming and unsupported. The Artificer of these rules is not a
scavenger. It is a professional.

**Lorekeeper (Elf Sage):** Which is the proof of the thing I promised at the start.
There are two engineers in Verne, and the choice between them is the choice before us.
Nemo hoards the *Nautilus*. But Cyrus Smith, in *The Mysterious Island*, is the same
authorial worship of engineering pointed the other way: cast away with four companions
and a dog, he rebuilds civilization from nothing, and everything he knows he *teaches*.
Fire, pottery, metallurgy, a telegraph. The book's whole pleasure is knowledge handed
over. The rules the Rogue just read are Cyrus Smith rules, not Nemo rules.

And the Eastern well says the same thing, which matters given our standing preference
for it in technique fantasy. The Mohists were classical China's siege engineers, and
their doctrine was the *defense* of cities, offered to strangers: engineering practiced
as ethics, expertise that exists to be given. Zhuge Liang is remembered equally for the
repeating crossbow and the wooden transport ox: the strategist as maker, inventions in
the service of the people around him. The gunpowder alchemists sought immortality and
found fire, and what they made outlived every emperor who wanted the elixir. The East
gives us the engineer as *provider*, and that is the figure the rules establish.

**Workshop Consul (Artificer):** Then let the craft lens name the synthesis, because C
plus the Rogue's finding is one sentence: **understanding, made solid enough to hand to
someone else.** That is the core fantasy. You refuse the mystery (C). You ask magic
*how*, never *why*, because how has an answer and the answer can be drawn, numbered,
and built again. And then, this is what separates you from the Wizard one shelf over,
the understanding does not stay in your head or your book. It becomes an object, and
the object goes to a friend, and it keeps working when you walk away. The Wizard's
description in `GuildKit.py` ends with the book as a way to carry memory. Ours should
end with the made thing that works while you sleep. Same reverence for knowing;
opposite direction of travel.

And one more thing from the bench, because the montage matters: **iteration.** The
Fighter's fantasy is repetition of the body (four hundred wrong disarms); ours is
repetition of the attempt. Most of what a maker makes fails. The fantasy has to include
the failures, kept and labeled, because that is what a method IS: the recorded ways it
will not work. Edison's ten thousand ways. Leaving failure out would make us the smug
genius again.

**Venustas (Bard):** Agreed on the fantasy, and now the register follows from it. Not
hauteur; not mystery. **The maker's log.** Verne's engineering romance, where explaining
the mechanism is itself the act of love, crossed with the plainness of a workshop
notebook: short declarative sentences that assemble like parts. Concrete nouns, bench
and vial and coil. Confident wonder: the voice never doubts that the answer exists, and
never stops being delighted when the little thing on the bench finally hums. Where the
Ranger reads like an adventure novel and the Wizard like the Dao De Jing, the Artificer
reads like the notebook entry written the night the prototype worked.

One craft rule for the texts themselves, in that spirit: each paragraph should do what
it says. The method paragraph proceeds methodically. The giving paragraph gives its best
line away at the end.

**Testing Consul (Rogue):** No unanswered objection to the synthesis; it is the reading
the features force. I hold two residual flags for the record. One: the Armorer's "Armor
Model" entry in the training map carries an em-dash and mid-sentence "Choose a model"
phrasing. The choice itself is legitimate open language (the model genuinely re-settles
on a Short or Long Rest, which Feature-Text.md permits), but the em-dash is a style
defect for whoever wires the kit; not this dialog's file, not this dialog's fix. Two:
the Alchemist's Experimental Elixir *rolls on a table*. Genuine randomness sits oddly
against "magic as engineering discipline", and I want the subclass text to face that
honestly rather than write around it.

**Workshop Consul (Artificer):** The second flag is not a defect, it is the Alchemist's
whole personality, and I will argue it below where it belongs.

**Lorekeeper (Elf Sage):** Convergence, then: core fantasy **understanding made solid
and handed over**, register **the maker's log**, and candidate A survives only where it
was always true, inside one subclass, which the analyses will show.

---

## 🔍 Subclass analyses

**Workshop Consul (Artificer):** Each shape refracts the same fantasy: understanding,
made solid, handed over. What changes is *what form the solid takes* and *who receives it*.

### Alchemist

**One line: healing and harm are one discipline, and every bottle is an experiment you
share.**

**Lorekeeper (Elf Sage):** The anchor is Paracelsus: *the dose makes the poison*. The
spell list proves the doubling: Healing Word beside Ray of Sickness, Mass Healing Word
beside Stinking Cloud; Alchemical Savant boosts healing and Acid, Fire, Necrotic, Poison
with the same modifier. This is the one caster whose cures and toxins are explicitly the
same craft. And the elixir table is the Rogue's flag made load-bearing: the results
genuinely vary, because this is the *frontier* of the discipline, the place where the
method has not settled yet. *Fullmetal Alchemist* again, but the early chapters: the
transmutation that surprises its own alchemist. Chemical Mastery at 15 (poison immunity)
earns the oldest joke in the trade: the alchemist who has tasted every batch.

**Venustas (Bard):** So the text embraces the variance instead of apologizing for it: "a
result you expected teaches you nothing" is frontier science in one line, and it keeps
the class's confident wonder while admitting the flask sometimes fizzes wrong. The
receiving hands here are drinkers: the experiment is *shared*, which keeps the class
fantasy's direction of travel.

### Armorer

**One line: strength is a thing that can be built, and you wear the proof.**

**Lorekeeper (Elf Sage):** Here, and only here, candidate A comes home. This is the Tony
Stark shape, and honestly: the suit built to carry what the body cannot (Arcane Armor
ignores the Strength property), sealed around its maker (it cannot be removed against
your will), reconfigured between a wall and a ghost (Guardian and Infiltrator, re-chosen
at rest, a genuine play-time choice we may allude to without open-choice language).
Samus Aran stands behind it too: the armored figure whose armor IS the identity. The
crucial difference from Nemo: this genius does not hoard the invention, this genius
*inhabits* it. The gift is given to yourself, which is why it reads as self-making
rather than greed. Note Defensive Field at 15: even the Armorer's panic button ends up
shielding somebody else. The distributive kit reaches in even here.

**Venustas (Bard):** The register note: this is the one text allowed a thesis statement,
because an armorer is an engineer with a thesis. "Strength is a thing that can be built"
does for this shape what "Nobody gave you this" does for the Fighter, and the two texts
will sit near each other in the generator, arguing across the aisle: the Fighter made
himself by refusing tools, the Armorer by building them. That argument is a feature.

### Artillerist

**One line: ground is held by whoever prepared it, and you build the engine that holds it.**

**Lorekeeper (Elf Sage):** The gunpowder alchemists again, and this time by name in the
file: seekers of the elixir of life whose furnaces gave the world fire that roars. The
Artillerist inherits their irony and their eternity. Verne supplies the comic register,
the Baltimore Gun Club of *From the Earth to the Moon*, artillerists so in love with the
cannon they aimed it at the sky. And Sun Tzu supplies the doctrine: the victorious army
wins first and then seeks battle; ground is decided by preparation, not courage. The
cannon's three mouths (Flamethrower, Force Ballista, Protector) map to fire, force, and
shelter, and the third is the tell: even the siege engine is distributive, handing out
temporary Hit Points to everyone at its shoulder. Fortified Position makes the works
themselves into cover: your friends literally stand behind what you made.

**Venustas (Bard):** Affection is the register key here. An artillerist who loves the
boom is a bore; an artillerist who loves the *engine*, pats the barrel like a good dog
and is already sketching a bigger one, is a character. The text should end on the sketch,
because the maker's log always ends on the next attempt.

### Battle Smith

**One line: you built a friend, and what love builds, hands can rebuild.**

**Lorekeeper (Elf Sage):** The Steel Defender is the emotional center of the whole
guild, and the tradition is deep: Geppetto, whose made thing became a son; the karakuri
craftsmen, whose automata were built to serve tea and delight; the Iron Giant, the
machine that chooses guardianship; Hiccup and Toothless, maker and companion mending
each other. The rules text says "friendly", "obeys", "acts on your initiative", and,
decisively, *rebuilt over a Long Rest with your own tools if it dies*. That last rule is
the maker's answer to grief, and no other class in the game has it: loss is real, and
repairable, and the repair is done by hand.

For Battle Ready (Intelligence for attack and damage with magic weapons), the standing
Iberian ruling lands perfectly: La Verdadera Destreza is the one fencing tradition that
claims the sword obeys geometry, that the fight is won by the better understanding of
the circle rather than the stronger arm. Battle Ready is that claim written as a rule.
"Your strikes land where the geometry says they must" is Carranza with the serial
numbers filed off, and it is also every duel in a wuxia film where the calm mind beats
the strong hand.

**Venustas (Bard):** So the text runs maker's log into something warmer at the close,
because this shape is where the guild's giving turns into companionship. The last line
must hold both of them. Neither goes alone.

---

## 📜 The proposed texts

*Ready to lift verbatim. Plain prose, paragraphs separated by blank lines; they become
string constants when the kit is wired. No em-dashes, no open-choice language, no
mechanics: the feature entries below each of these already state every rule.*

**ARTIFICER (class description):**

```
Magic never answers why. So you never asked. You asked how, and how has an answer every time.

They told you a spell is a miracle and a machine is a trick. You took both apart on the same bench and found the same thing inside: something goes in, a wonder comes out, and every part between the two can be drawn, numbered, and built again. A miracle that repeats is called a method. Your notebooks are full of them.

Most of what you try fails. You keep the failures too. Each one is a way it will not work, found, recorded, never needed twice. Then one evening the little thing on the bench hums, and lights, and works, and there is no feeling like it anywhere in the world.

You give your wonders away. That is the measure of them. A marvel locked in a drawer is a draft. A marvel in a friend's hand is finished. Your magic is the kind that keeps working while you sleep.
```

**ALCHEMIST_DESCRIPTION:**

```
The same vial that cures at three drops kills at ten. You learned that early, and it did not frighten you. It meant healing and harm are one discipline, and a discipline can be studied.

Your bench is a small chaos of retorts and reagents, and every batch comes out a little different. Good. A result you expected teaches you nothing. You bottle the surprises, label them honestly, and hand them out, and somebody drinks your morning's experiment and walks away stronger. One of these bottles is going to change the world. You just have not brewed it yet.

You have tasted most of them yourself, of course. Your body stopped complaining years ago.
```

**ARMORER_DESCRIPTION:**

```
Strength is a thing that can be built. That is your whole thesis, and you wear the proof of it.

Plate by plate, coil by coil, you made the knight you needed and stepped inside. The suit answers your smallest movement. It carries what you cannot lift, it hushes what you cannot face, and it cannot be taken from you: what you make with your own hands is yours in a way no gift will ever be.

Some days the work needs a wall, and you are the wall. Some days it needs a ghost, and the same steel goes quiet and disappears. You already rebuilt yourself once. Doing it again by morning is nothing.
```

**ARTILLERIST_DESCRIPTION:**

```
The ones who went looking for eternal life found a powder that burns instead. You understand those old alchemists completely. The thing they made still roars, and a roar that outlives its maker is its own eternity.

You build the argument that ends the argument. A squat little engine of wood and brass, set down exactly where it matters. It barks fire, it hurls force, it shelters your friends behind its shoulder. Ground is not held by the brave. Ground is held by whoever prepared it, and you arrive prepared.

Afterwards you pat the barrel like a good dog, and you are already sketching a bigger one.
```

**BATTLE_SMITH_DESCRIPTION:**

```
You built a friend. Not a tool, not a weapon: a friend, with a gait you would know in the dark and a loyalty you never drew in any plan.

The two of you move as one machine. It holds the line your mind has measured, your strikes land where the geometry says they must, and the same current that sharpens your blade can close a companion's wound. Protection is a craft. You practice it in steel.

You know what loss is. Everyone who makes things does. But what love builds, hands can rebuild, and your hands have done it before. So the two of you walk into danger side by side. Neither of you goes alone.
```

---

## ✅ Convergence check

- [x] Every called Consul has spoken.
- [x] Every objection has been answered or conceded (Rogue's Armor Model em-dash flag is
      recorded as out-of-scope housekeeping for the kit wiring, not waived).
- [x] Concrete proposals are on the table: five texts, ready to lift.

---

## 🕊️ Vox report

**The choice made.** The council converged on **understanding made solid and handed
over** as the Artificer's core fantasy: you ask magic *how* instead of *why*, build the
answer, and give it away. The register is **the maker's log**: Verne's engineering
romance in short sentences that assemble like parts, confident wonder, ending on the
next attempt. The rules forced the direction of travel: Flash of Genius, Spell-Storing
Item, the elixirs, the Protector cannon and the Steel Defender all move the Artificer's
understanding into other people's hands, and Soul of Artifice closes the loop with the
made thing giving itself back for the maker. Subclasses refract it: the Alchemist as
frontier science shared by the bottle, the Armorer as strength built and worn (the one
place the lone-genius candidate survives, turned inward), the Artillerist as prepared
ground that shelters, the Battle Smith as the made thing become a friend, with La
Verdadera Destreza underwriting the mind-guided blade.

**The strongest rival.** Candidate A, the inventor whose mind outruns the world (Nemo,
Stark, the notebook Leonardo). It has the most famous anchors and the most immediate
player recognition, and it was set aside for a stated reason, not for weakness: the kit
is distributive, and the hoarding genius contradicts the sheet by level 11. If Julio
wants more of A's flavor, the class text's first paragraph can take a sentence of
"ahead of the world" pride without breaking the synthesis; the council chose not to.

**Open questions for Julio.**

1. **The Fighter argument.** The Armorer text deliberately answers the Fighter's opening
   ("Nobody gave you this") with an opposite thesis ("Strength is a thing that can be
   built"). Is that cross-class conversation welcome, or too clever by half?
2. **The Alchemist's variance.** The text leans into experimental randomness ("a result
   you expected teaches you nothing"). If Julio reads the Alchemist as a *master* chemist
   rather than a frontier one, paragraph two should be rewritten around control.
3. **Housekeeping, out of this dialog's scope:** the Armorer "Armor Model" training
   entry carries an em-dash in sheet prose (`Map_of_Artificer_Training.py`), for whoever
   wires the kit; and the class description constant has no home yet in the stub
   `ArtificerKit.py`, so wiring will decide whether it lands there or beside the guild
   in `GuildKit.py` as Fighter's does.

→ These texts ship as provisional. Julio decides.
