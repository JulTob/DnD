# Dialog 0026 — the Paladin's oath lines, reviewed

- **Question:** Which of the Paladin's oath lines (five registers, the species hearts and the background words) stay, go, or are rewritten, and how does an oath avoid echoing itself or another Oath?
- **Raised by:** Julio (in chat, 2026-09-15: "Start an agora to review the lines of the oaths"; the pools were pushed in full on his ruling "push the full pools and we'll review later")
- **Related Questae:** QST-0127 (echoes and leaks) · QST-0126 (the paragraphs, out of scope here) · QST-0130 (the steed, out of scope here) · PR #7
- **Consuls called:** Lorekeeper (Elf Sage), Venustas (Bard), Contracts (Warlock), Simplicity (Monk)
- **Status:** 🟡 open · framed 2026-09-15, register ruling added the same day, deliberation not yet run

---

## 🧭 Framing

**What is under review.** The Paladin's device is the oath recited: six lines
under each Oath paragraph, in a fixed shape (vow, heart, arm, word, refusal,
close), drawn per Character by `AtlasLusoris/AtlasOfTraining/Map_of_Paladin_Oaths.py`
from six pools per Oath. Exactly two lines are personal: the heart may come
from the species pool and the word from the background pool, each at grace
weight 3 against the Oath's own lines at 1. The frame line ("You swore an oath
to X. To be a paragon of Y:") is ruled and is not under review. The class text
and the Oath paragraphs are not under review (QST-0126 holds the paragraphs).

**How the pools were filled.** Julio wrote the first line of every Vengeance
slot and ruled every register's poets. Agents drafted the rest under those
rulings, in several passes: a Byron set, a Byron-led and a Bécquer-led set for
Vengeance (all three kept, on the ruling "all the options"); Psalms and King
James for Devotion, then Cavafy and Hesse; Twain, Espronceda, Moore and Gaiman
for Glory, then Cavafy; Shakespeare and the Green Knight for Ancients; Lorca,
Neruda's elemental odes and Scheherazade for Creation. Julio approved the
Creation lines with the note that "some are a bit off". The pools are
therefore full and unpruned by design. This Dialog is the pruning.

**Constraints from Canon and from the rulings.**

- `Canon/Feature-Text.md`: identity, never a mechanics summary; no open-choice
  language; no rule pre-explained ahead of the rules that print it.
- No proper nouns in game text. Every poet's line was written without the
  names its poem carries (Thermopylae, Ephialtes, Ithaka, the Coliseum).
- No em-dashes in authored prose.
- Death of the author: a line may state the Character's stance, never an event
  in their past or future. "I failed it, and I have come back" was cut for
  this before it shipped; "My heart was broken once" (Vengeance) is on the
  table for the same reason.
- Fidelity, not virtue: a line binds; it does not moralize. A Lawful Evil
  Devotion Paladin must be able to say every Devotion line.
- Register per Oath. Nothing in a Devotion oath may sound like Vengeance. The
  Aasimar owns "chosen". The Barbarian owns rage, which is emotion; the
  Paladin's oath is principle.
- Julio's bar for a line: "only pass awe inspiring lines"; the failure mode he
  named: "too formulaic. Too... AI." His own examples of the mark: "My sorrow
  will not stop the grass"; "If I fall, that's the life I chose. Nothing lost,
  but me."
- **Register ruling (Julio, 2026-09-15, after the framing; refined the same
  day).** A line has two layers: the idea and feeling, and the aesthetic and
  cadence. The poets are inspiration for the ideas; the aesthetic is the
  Oath's own epic form. In Julio's words: "we do not want a psalm. We want
  Hesse's Siddhartha or Steppenwolf as a Psalm. Lorca's with Arabian cadence,
  Byron and Bécquer sounding like Byron and Bécquer (in this case the
  aesthetic fits the meaning). And we want Cavafy in the structure of the epic
  poem of Homer. We need a specific Romanticist style by looking back at the
  past." Then, on Devotion: Hesse is withdrawn as a source ("probably the
  start of postmodernism so it rejects romanticism"). Devotion's ideas come
  from Espronceda, the Cid, the knights of the Round Table, Zorrilla's Don
  Juan Tenorio ("No es verdad, ángel de amor"), "a psalm of lovers, a romantic
  romance, a knight in pursuit of a princess' heart, probably not knowing her
  at all", and the boy at the start of Stardust: pure love is devotion, and
  anyone at the Round Table is a Devotion Paladin, oriented differently.
  Working reading (Claude, to be confirmed): Devotion = courtly love and
  knightly loyalty in the psalm's form (the psalm of lovers is the Song of
  Songs: parallelism, the seal, the beloved); Ancients = the Green Knight,
  Shakespearean, unchanged; Glory = Cavafy's and Espronceda's ideas in
  Homer's epic structure (epithet, simile, catalogue, the singers); Creation =
  Lorca's and Neruda's ideas in the Arabian cadence (the Nights, the casida);
  Vengeance = Byron and Bécquer as they are. A line that keeps its idea and
  changes its sound is a rewrite, not a cut. The Devotion flag below (three
  poets in one draw) is answered by the ruling rather than by weights.
- The mechanical lint (in session, to be moved to `scripts/` under QST-0127):
  84 characters at most; no modern or bureaucratic words; no hedges; no wry
  deflation; no explanatory connectives. Three flags are defended and stay:
  the Devotion refusal at 87 characters, "rather" in a Glory close, and
  "negotiates" in Julio's own Vengeance words line.

**What a good answer must satisfy.**

1. **A verdict per line**: keep, cut, or rewrite, with the reason, and every
   rewrite offered in the Oath's ruled voice (the register ruling above),
   keeping the poet's inspiration. Julio decides; the council recommends.
2. **The Lorekeeper's "ours to use" pass.** Byron, Bécquer, Cavafy, Lorca,
   Shakespeare, the Psalms, Twain and Espronceda are in the public domain.
   Hesse (d. 1962), Neruda (d. 1973), Moore and Gaiman (living) are not. A line
   in their *style* is ours; a line that is a *translation of one of their
   lines* is a quotation. Name which lines are which. The Hesse close ("Well
   then, heart. Take your leave, and be well.") and the Neruda salt line are
   the first to check.
3. **The Contracts pass.** Three invariants, and where each should live (data
   or composer): no line shared across Oaths; no line shared between a
   register and a grace pool (broken twice today: two Glory words lines sit in
   the `outside` and `wandering` background clusters); no phrase shared across
   slots of one oath (broken twice in Vengeance: the dead kept company in
   hearts and words; the pardon dying at the lip in words and refusals).
4. **The Simplicity pass.** Pool sizes are uneven (Vengeance 60, Devotion 36,
   Glory 30, Ancients 25, Creation 24). Say whether size alone is a problem,
   and whether Devotion, now drawing three poets into one six-line poem, needs
   weights or only pruning.
5. **The ear.** Venustas names which lines sing and which are formulaic, and
   says why in a way the next author can apply.

**Known flags, gathered in session, for the council to confirm or dismiss.**

- Creation: "My arm moves the world" and "My word was the first mover" repeat
  the feature lines of Force of Will ("You can move the world") and Event
  Horizon ("You become the mover") on the same sheet. The salt line is
  Neruda's ode and puzzles a reader who does not know it.
- Vengeance: the two cross-slot pairs above; "My heart was broken once, and
  what remained of it is iron" imposes a past.
- Glory: "I am sworn to the dark swallows that will not return" needs the poem
  to be understood (it is in Vengeance, from Bécquer; check placement).
- Devotion: three poets in one draw; whether the King James verbs and the
  plain modern lines read as one voice.
- Species: the Human heart line ("My heart is true, and my friends are my
  rest") reads generic beside every register.

**Out of scope.** The class text (ruled). The five Oath paragraphs
(QST-0126). The steed (QST-0130). The frame line. The six-slot shape.

---

## 🗣️ Deliberation
*Each Consul signs every line. Argue only from your lens. Objections must be constructive. End with a concrete proposal.*

Lorekeeper (Elf Sage): …

Venustas (Bard): …

Contracts Consul (Warlock): …

Simplicity Consul (Monk): …

---

## ✅ Convergence check
- [ ] Every called Consul has spoken.
- [ ] Every objection has been answered or conceded.
- [ ] At least one concrete proposal (a keep/cut/rewrite table, and the invariants' home) is on the table.

---

## 🕊️ Vox report
Vox: *(pending deliberation)*

→ Awaiting Julio's decision. To be recorded as Decree NNNN.

---

## 📜 Appendix: the corpus under review

Generated from `Map_of_Paladin_Oaths.py` at PR #7 head, 2026-09-15. The first
line of every Vengeance slot is Julio's. Species and background lines are the
grace pools.

### Devotion (36 lines) · poets: the Psalms; the King James; Cavafy; Hesse · paragon of constancy and truth

**vows**

- I am sworn to the Eternal Truth.
- I am sworn to stand unbent and unbroken.
- I am sworn unto the Truth; it is my rock and my high tower.
- I am sworn to walk uprightly, though the whole earth be moved.
- I am sworn to a narrow pass. I know how narrow passes end.
- I am sworn, and it asks little: I can think, I can wait, I can go without.

**hearts**

- My heart is set as a flint, and it shall not be turned.
- My heart is a lamp that goeth not out by night.
- My heart hath one law, and keepeth it, and seeketh no other.
- My heart is a stronghold, and the gates of it stand open.
- My heart had its Yes ready before anyone asked.
- My heart keeps ready for parting, and at every parting begins again.

**arms**

- My blade is bright. Nothing I do is done in the dark.
- My arm is lifted in the daylight, and my hand knoweth no secret work.
- My sword is girded on before all eyes, and it is a clean sword.
- My blade hath never once been drawn in secret.
- My blade is just and upright, and keeps its pity for the one it stops.
- My sword serves. Whoever would lead has first to serve.

**words**

- My word is yea, and my word is nay, and there is no third word in me.
- My word is given once; heaven and earth shall pass before it is taken back.
- My word hath been given to the unworthy, and kept. This word is kept likewise.
- My word standeth. Let the mountains be removed; my word standeth.
- My word is the truth, always, and without hatred for the one who lies.
- My word cannot be told to another. It can only be kept.

**refusals**

- I will not bow, though the seven hills bow down.
- I will not stand in the way of the crooked, nor sit where the mockers sit.
- I will not lie, though the lie would save me, nor flee, though the truth would slay me.
- I will not bend, not for the friend who begs, not for the king who commands.
- I will not degrade my life. This much, as much as I can: I will not degrade it.
- I will not say it left me. It does not leave. Only I can.

**closes**

- And if I am the last one keeping it, it is still kept.
- Though all the world forsake it, it shall not be forsaken.
- This is my portion, and I shall not want another.
- So it standeth, and so I stand.
- The traitor will come. The pass will fall. It will have been kept.
- Well then, heart. Take your leave, and be well.

### Ancients (25 lines) · poets: Shakespeare; the Green Knight · paragon of the green and the returning light

**vows**

- I am sworn to what was and what will be.
- I am sworn to the light. Even the night has stars.
- I am sworn to the green, which has outlasted every fire.
- I am sworn to the spring, that comes though no one bid it come.
- I am sworn to the sweet o' the year, and to its keeping.

**hearts**

- My heart is a wood in winter, and knows the green sleeps and is not dead.
- My heart keeps a garden no frost has ever taken.
- My heart is old as the oak and light as the leaf upon it.
- My heart is made of such stuff as springs are made on.

**arms**

- My blade is for the winter, and the winter is patient.
- My blade stands between the small green thing and the frost.
- My sword is a bough of the old tree, and it remembers the root.
- My blade is a young thing, and it serves a very old one.

**words**

- My word is kept as the year is kept: the spring comes because it was promised.
- My word is given as the oak gives shade, to whoever stands beneath.
- My word was whispered to the wood, and the wood has not forgotten.
- My word is a seed. Bury it, and see what comes up.

**refusals**

- I will not let the light go out, though the night be long as winter.
- I will not curse the frost. I will outlast it.
- I will not mistake one felled tree for the end of the forest.
- I will not weep for the fallen leaf while the bough still lives.

**closes**

- My sorrow will not stop the grass.
- Let it go out everywhere else. It will not go out in me.
- The green comes back. It always has. I am here to see that it does.
- Winter is a season. I am the one after.

### Glory (30 lines) · poets: Twain and Espronceda; Moore and Gaiman; Cavafy · paragon of valour and renown

**vows**

- I am sworn to valour.
- I am sworn to be worth the song.
- I am sworn to the deed that outlives the doer.
- I am sworn to the story, and the story is not finished with me.
- I am sworn to the road, not the island. The island only made me set out.

**hearts**

- My heart is a ship, my treasure the horizon, my only country the sea.
- My heart was built for a story bigger than a life, and has grown to fit it.
- My heart laughs at the odds. The odds have never once laughed back.
- My heart is the drum they march to, and it has never missed a beat.
- My heart wants no province from a king. It wants the crowd's hard-won well done.

**arms**

- My blade goes first. It has always gone first.
- My blade is for the moment the song will need.
- My blade writes the verse they will sing loudest.
- My sword is my law and the wind, and I answer to no other.
- My blade is on the first step. To have come this far is no small thing.

**words**

- My word is my name, and my name is not for sale.
- My word is the one thing I never sold, and I sold a great deal.
- My word is a promise to the poets: I will give them something worth the rhyme.
- My word travels ahead of me, and arrives before I do.
- My word is not a costume. When the theatre empties, I am still wearing it.

**refusals**

- I will not die in bed. I have been offered it.
- I will not be the footnote. I will be the chapter.
- I will not choose the long life. I have been offered it.
- I will not fold. I have never once folded.
- I will not hurry the road. Better it lasts for years, and I arrive old.

**closes**

- If I fall, that is the life I chose. Nothing lost, but me.
- Say it after me, and say it right.
- They will tell it wrong. Tell it wrong in my favour.
- I would rather be the story than the one who lived it.
- If I find the island poor, it did not fool me. I know now what islands are for.

### Creation (24 lines) · poets: Lorca; Neruda's Odas elementales; Scheherazade · paragon of making

**vows**

- I am sworn to what is not yet, and to making it so.
- I am sworn to the four elements, and to the fifth, the word.
- I am sworn to the first light, the one that came before the sun.
- I am sworn to make, and to answer for the made.

**hearts**

- My heart is a forge with no smith in it but me.
- My heart is the salt in the sea and the salt on the bread. It made both.
- My heart is clay that remembers the hands, and the hands were mine.
- My heart holds a word no page can hold. I say it.

**arms**

- My blade is earth, then air, then fire, then water, as I say.
- My sword was the first thing I made, and it is not finished yet.
- My arm moves the world. Give it a place to stand.
- My blade writes in four elements what no ink can write.

**words**

- My word is spoken, never written, and the world leans toward it.
- My word is the lamp and the light. I say it, and there is.
- My word is a seed dropped in the dark. It does not ask leave to grow.
- My word was the first mover. Everything since has been moved.

**refusals**

- I will not unmake what I have made. I will answer for it.
- I will not wait for a god to say it first.
- I will not leave the world as I found it.
- I will not call it finished. Nothing I have made is finished.

**closes**

- Let there be. And there was.
- I made this. Look at it.
- The seventh day is not for me. There is more to make.
- Say the word after me. Now watch the world.

### Vengeance (60 lines) · poets: Byron; Bécquer · paragon of retribution and justice

**vows**

- I am sworn against the perpetrators of injustice.
- I am sworn to the deep, and the deep gives back nothing it has taken.
- I am sworn to stand among them, and never of them.
- I am sworn to no king and no court. The debt is mine, and mine the keeping.
- I am sworn, torn but flying, to stream like the storm against the wind.
- I am sworn to be my own hereafter, and theirs.
- I am sworn to the dark swallows that will not return.
- I am sworn to the reckoning, and the reckoning wears my face.
- I am sworn to be the storm they prayed would never break.
- I am sworn to hunt what the law forgave.

**hearts**

- My heart rides the storm, and my arm wields the thunder.
- My heart knows why one weeps. My heart knows why one kills.
- My heart leaves the dagger in. Drawn out, the wound would only close.
- My heart keeps the dead company, and knows how alone they are left.
- My heart is a wound that does not bleed. It rides.
- My heart knows why we weep, and it knows why we kill.
- My heart has a dagger in it already. Let them bring another.
- My heart is a midnight that keeps one lamp burning.
- My heart was broken once, and what remained of it is iron.
- My heart keeps a ledger, written in a hand that does not shake.

**arms**

- My blade carries the names and balances their crimes.
- My sword outwears its sheath, and the sheath is the only thing that tires.
- My arm is the shore, and their power stops at the shore.
- My blade is the lightning, and the lightning knows where it falls.
- My blade is where my tears go. Not one of them reaches the sea.
- My sword is love with the tenderness torn out, and it is love still.
- My blade does not come from behind. They will see it coming.
- My blade is the last argument, and I have never lost it.
- My blade does not hate. Hatred tires. My blade remembers.
- My blade comes down like the wolf upon the fold.

**words**

- My word is fair, but never kind. It is strong, and it never negotiates.
- My word is not a pardon. The pardon rises to my lip, and dies there.
- My word is what remains when the sigh goes to the air and the tear to the sea.
- My word is given in a whisper, and the whole sky hears it kept.
- My word keeps the dead company, and the dead are left so alone.
- My word is today as yesterday, tomorrow as today, and always the same.
- My word is an arrow, and it knows where it will tremble and lodge.
- My word was given to the dead, and the dead do not release you.
- My word is the one debt I have never let run past its day.
- My word is a sentence passed, and I am its executioner.

**refusals**

- I will not be the one who put down my shield or my word.
- I will not be called off, not by the crown, not by the pit, not by the dead.
- I will not let the years plead for them. The years write no wrinkle on me.
- I will not take gold for it. There is not gold enough in the earth.
- I will not say the word of pardon. It comes to my lips, and dies there.
- I will not ask how they can laugh. I will be the answer.
- I will not sit alone with my grief. I carry it to their door.
- I will not forgive what was never confessed.
- I will not sleep while the guilty sleep soundly.
- I will not be told that it was long ago.

**closes**

- I am the rider that brings the storm.
- I am the deep, and I am dark, and I do not end.
- It is midnight, and I am awake, and I am coming.
- I am a ruin, and what a ruin. Kingdoms were quarried from less.
- They are the high tower, and I am the hurricane. One of us must fall.
- If I meet them after long years, how shall I greet them? With silence and steel.
- What was lost does not return. What returns is me.
- Let them run. The storm runs faster.
- It ends. I have decided that it ends.
- They made me. Let them look upon what they made.

### Species hearts (replace the heart line at grace weight 3)

- Aasimar: My heart carries a spark of greatness. I was chosen.
- Aasimar: I was chosen. I chose back, and mine was the louder yes.
- Aasimar: My heart holds the stars. My arm carries the might.
- Dwarf: My soul is golden, and gold never corrupts.
- Dwarf: My heart was made in the forge of my clan.
- Orc: My heart rides the storm, and the winds will carry me.
- Orc: My heart is the heart of a rider, and a rider does not turn back.
- Halfling: My heart is small, and there is no room in it for fear.
- Halfling: My heart carries the homeland, and the stories I will tell.
- Tiefling: My heart was alone. No more.
- Tiefling: My heart protects the ones like me: born alone.
- Human: My heart is true, and my friends are my rest.
- Human: My heart is brief, and burns the brighter for it.
- Elf: My heart has all the time there is, and spends it here.
- Goliath: My heart carries the weight of the world, and is not bent by it.
- Goliath: My heart came down from a fallen height, and kept the height.
- Dragonborn: My heart keeps the old courtesies, and keeps them to the death.
- Gnome: My heart is astonished by the world, and always was.

### Background words (replace the word line at grace weight 3, by cluster)

- sworn: My word was given before, to lesser things, and kept.
- held: My word was the only thing about me that nobody else owned.
- outside: My word is the one thing I never sold, and I sold a great deal.
- wandering: My word travels ahead of me, and arrives before I do.
- marked: My word is the part of my fate I got to write.
- alone: My word was given where nobody could hear it.
- lost: My word outlived everything else I had. It will outlive me too.
