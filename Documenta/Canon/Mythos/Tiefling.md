# 😈 Tiefling

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from `Tieflings-and-the-Shift.md`, the Tiefling kit, the
class analyses and Julio's notes on the Aasimar page. Where Julio has decided,
the decision is stated as such; where this page proposes, it says so. The other
end of this entry is [Aasimar.md](Aasimar.md).*

> **In one sentence.** A Tiefling has never done anything, and that has never
> been the relevant fact. The legacy is power; what is decided about it is the
> sentence.

---

## 1. Where the Tiefling lives in the code

| What | Where | State |
|---|---|---|
| Species entry (Julio's) | `AtlasActorLudi/SpeciesKit/Tieflings/__init__.py` | Shipping. Second person only; no "we" by design. |
| Heritages | `Tieflings/Abyssal.py`, `Chthonic.py`, `Infernal.py` | Each carries a `HERITAGE_DESCRIPTION` paragraph (the body) and a spell list. |
| Traits and rules | `Tieflings/traits.py`, `resolution.py` | Rulebook voice (QST-0094). No inspiration lines on Darkvision, Otherworldly Presence or Fiendish Legacy. |
| Names | `AtlasNomina/Races/Fiend.py` | Demonology names, and a second pool of *virtue names* (Glory, Honor, Purity, Flame, Sinner). |
| Culture | legend `grimdark` only; no society key | Shared with the Warlock and the Fiend patron. |
| Prayer | `Map_of_Cleric_Prayers.py` | *Ash remembers the flame.* Plus Grave, Life and War lines (one typo). |
| Canon | `Documenta/Canon/Tieflings-and-the-Shift.md` | The mechanism, the five rules. |

---

## 2. Origin: the reading changed

The setting established how Celestials work: mortal belief is the fuel from
which they emerge. Apply the rule honestly and it runs both ways. **If belief
makes celestials, belief makes fiends.** A theological shift declared one half
of the cosmos the enemy, everyone believed it hard enough for long enough, and
the machinery obliged. The Lower Planes were made lower by being called it.

**The proof is retroactive.** The horns that once held a sacred flame became
evidence of damnation. Nothing about the horns changed; the reading did, and
the reading is what the world runs on.

**Before the shift they were gifts.** The species entry allows one sentence and
never explains it: *"Somebody there will tell you the horns are crowns that
used to hold a shining flame, and that we were the chosen, long before. It's a
beautiful fantasy."* Egypt is the register for what was there before, being the
one inspiration the setting had not spent. Never resolve it.

**The shared priesthood** (Julio, 2026-09-08; deep lore). The Aasimar and the
Tiefling once shared one priesthood. The Aasimar's side separated,
dichotomised, and rose above the local cultures; the Tiefling's side was left
holding the horns. The Aasimar's privilege and the Tiefling's exclusion are one
event, and the Manichaean shift (Principle against Punishment, reward absent)
is the theology that made it stick: a Celestial prevents or redeems, a fiend
tempts or punishes, and the Tiefling is the punished side's mortal without ever
having been offered the temptation. A Character may find an inscription that
says so. Nobody in authority confirms it.

---

## 3. The vessel: physiology

**Born to ordinary parents.** The structural fact that separates the Tiefling
from every other people. "The midwife went quiet, and that was how it began."
Some families hide the child; some report a stillbirth and mean it as mercy.

**Fur, horns, eyes, tail.** In this setting the Tiefling is furred, with a
metallic sheen, and the horns sit close to the head like a crown or a tiara.
This is a distinctive design and should be protected as such: not a human with
horns, and not the published red skin.

| Heritage | The hell | The body | Resistance | Legacy spells |
|---|---|---|---|---|
| **Abyssal** | The Abyss: chaos, "beings with no defined shape" | Metallic fur of bright colour with spots and lines that shift, sometimes changing shape overnight; the most intense colours and the hardest to hide; twisted, spiky, uneven horns; eyes that change colour with emotion | Poison | Poison Spray, Ray of Sickness, Hold Person |
| **Chthonic** | Hades: "the most neutral of hells. No fire, no pain, only darkness" | Eyes black except a vivid iris; fur in the colours of foxes, wolves and bulls, or the tones of a corpse; uncanny but the easiest to pass as human; horns of ivory, bone or metal, close to the head like a crown or tiara | Necrotic | Chill Touch, False Life, Ray of Enfeeblement |
| **Infernal** | The Nine Hells: fire and brimstone | Horns black as onyx; eyes black with a golden fiery iris; fur black or flame-coloured with a metallic, almost golden shine; an arrow-tipped tail | Fire | Fire Bolt, Hellish Rebuke, Darkness |

**Otherworldly Presence** (Thaumaturgy) and **Fiendish Legacy** cast from an
ability drawn once per Character (Intelligence, Wisdom or Charisma).
**Darkvision** at the common sixty feet.

**The parallels rule** (canon): several real experiences rhyme with this
(marked as evil while carrying none; marginalised and itinerant; a difference
treated as a defect by the environment), and none is named on the page. A
species that is explicitly one thing becomes a mascot and stops being a
people.

---

## 4. Society: a diaspora with no homeland

**There is no culture** in the sense every other people has one: no elder, no
quarter of the city, no festival where everyone has horns. Nobody hands down
what you are, because the people who made you do not have it either. A
Tiefling meets other Tieflings by accident, as adults, and every generation
invents everything from scratch.

**What there is instead:** the house. *"And then somebody like you finds you.
They pay the fine, or they feed you, or they simply say the word, but not as
the insult it is: Tiefling… Children in that house are nobody's, and they are
ours."* A found family, a network, a subculture recognisable on sight.

**The hated minority** (Julio). Against the Aasimar's model minority, the
Tiefling is the target of hate by default: the emo and the punk to the
Aasimar's quarterback and cheerleader. Same structure (born to ordinary
parents, a subculture recognisable across host peoples, "same symbols on
different hardware"), opposite integration: the Aasimar is praised upward, the
Tiefling is pushed out. Both stay distinct from each other and from their host
peoples; there is no host-culture draw for either (Julio, decided).

**The symbols.** `grimdark` is the register: Warglaive, Penitent's Flail,
Heretic's Star, Oath-Breaker's Knife, Chastening Lash, Witch-Hunter's Poleaxe.
Penitence and heresy, the vocabulary of the punished. It is shared with the
Warlock and the Fiend patron on purpose and should stay shared. Its influences
reach `germany` and `sword_and_sorcery` at 1.

**The names** (`AtlasNomina/Races/Fiend.py`). Two pools. Demonology names
(Abraxas, Agares, Mephistopheles), which the Tiefling took or was given by the
house. And **virtue names**: Glory, Honor, Purity, Law, Melody, Flame, Dawn,
Victoria, Sinner. A parent naming a horned newborn *Purity* is a whole story in
one word, and the pool already tells it. Protect the second pool; it is the
species' quietest device.

**Grammar.** The species entry is the only one written in the second person
alone, and the isolation is in the grammar rather than asserted. Julio's
reading refines the canon's "the only one with no we": the Tiefling is the only
people whose lack of a "we" is *hostile*. The Aasimar has no species "we"
either, but the Aasimar's subculture says "we" from above. The Tiefling house
says it from the floor of a squat.

**Two answers the house gives.** *"Somebody there will tell you the horns are
crowns… Others say we should claim our place in the Nine Hells, and hit back
harder. We carry fire, that's certain, but it can be used for a warm home or
for a burning inferno."* The species entry keeps both open and the wiki must
too. Neither is the correct one.

---

## 5. Metaphysics

**No biological determinism, ever** (canon rule 1). The legacy does things; it
never makes anyone a kind of person. The three heritage blocks describe bodies
and spells, and stop.

**The legacy is power, not impairment** (canon rule 5). A Tiefling is not
lessened by what they carry; they are lessened by what is decided about it.
"Which is a different sentence and the only true one."

**The Tiefling and the Ascending.** The Dragon canon says anyone can Ascend by
overcoming the culture that made them and arriving at a self genuinely their
own. The Tiefling inherits *nothing* but a reading: no elders, no observances,
no clan. Of every people in the setting, the Tiefling has the least culture to
overcome and the most *other people's* reading to overcome, which is the harder
kind. Deep lore, never on the page: the Tiefling is a strong candidate for a
real Ascending precisely because nobody handed them a self to be overcome, and
what they would become is what they always were, read correctly at last.

**Prevention against punishment** (Julio). The Manichaean shift put a
Celestial on the preventing side and a fiend on the punishing side. The
Tiefling is punished for a reading, which is the Aasimar's prevention seen from
below. A campaign whose antagonist is a Celestial "installing the Ideal" will
find the Tiefling in the party is the one it most wants to correct.

---

## 6. Relations with the other peoples

| People | The relation | Deep lore, never on the page |
|---|---|---|
| **Aasimar** | The mirror. One mechanism, opposite readings; model minority against hated minority. | The shared priesthood, split by the Aasimar's side (§2). Cousins told different stories about the same flame. |
| **Human** | The birth culture, most often. "The rate at the inn goes up." | Humans organise; the fine and the guard are Human institutions doing what institutions do to a reading. |
| **Elf** | The Elves' Shadow is the nightmare face of the Dream; the Tiefling's Lower Planes are a different substance. Two "others" that are not the same other. | A Shadow Elf and a Tiefling are the roster's two ways of being read as the dark, and they should not be conflated in gear or prose. |
| **Dragon / Dragonborn** | The self-authored against the self-condemned-by-others. | The Ascending candidate (§5). |
| **Goliath, Dwarf** | Peoples with a fallen or lost greatness that they *remember*. The Tiefling has a lost greatness nobody remembers. | The Stranger's "old ones" are the only people who might. |
| **Fiends** | The reading's other side. A Fiend Warlock patron is a being whose reading changed, like the Tiefling's. | A Tiefling who signs with a fiend may be signing with what was once their people's gift-giver. |

---

## 7. The classes: what the legacy does in each

| Class | The Tiefling in it |
|---|---|
| **Paladin** | The Oath of Vengeance's *Avenging Angel* puts wings on the condemned for an hour a day. The shift reversed by a vow; nobody in-world reads it correctly. Aura of Devotion ("nobody near you can be Charmed"): the one who cannot be told what they are. |
| **Ranger** | The Gloom Stalker's *Umbral Sight*: invisible to everything that sees in the dark, past the edge of the town that walked them out. The first time not being looked at is a power. |
| **Fighter** | *Indomitable*: reroll the failed save with your level added. The verdict was wrong; roll again, and this time the years count for you. |
| **Rogue** | *Elusive*: nobody gets the drop on the one who has been watched all their life. The Soulknife's Psychic Whispers: the first crew that speaks without speaking, for a people with no "we". |
| **Monk** | The Warrior of Shadow: "stories travel ahead of you and fight half the fight before you arrive". The species' whole life turned from a wound into a technique. The school is the first family. |
| **Warlock** | The Fiend patron, and the sheet cannot say which fiend. "You have never done anything" against "It saw you, broken, and promised." The pact as the first thing that ever chose them. |
| **Cleric** | Kept by something the shift condemned. *Ash remembers the flame.* Hagar in the desert named God "the one who sees me": the watcher fantasy first spoken by an outcast. |
| **Barbarian** | The Zealot, and the horror is which god: the old priesthood's fire, or a fiend. The sheet declines to say. |
| **Bard** | The only Bard who had to invent a tradition. The Glamour loan from the one court that took them. The host culture's instrument, by adoption. |
| **Druid** | The Land: a place that accepts them when no people would. "A place notices being known" is the first welcome the species entry describes without a fine attached. |
| **Sorcerer** | A mark on top of a mark. Wild Magic: "we carry fire, for a warm home or a burning inferno". Two readings of one body. |
| **Wizard** | The one who could read the carvings, and chooses every session whether to say. Scholar's Expertise in History. |
| **Artificer** | The Armorer's Infiltrator model is a hood built by hand: the thing the species needed and nobody would give. |

---

## 8. Backgrounds

- **Stranger.** The species' own background in all but name: "a diaspora with
  no homeland to be exiled from", the old ones as the last library, "the rites
  that were made illegal". The Stranger Tiefling's old ones might know what the
  horns held.
- **Renegade.** "A family that picked itself… Nobody sells out their own.
  Ever." The Tiefling house as a crew; the Renegade is what the house looks like
  from inside.
- **Inquisitor.** "There was a child… Iron blistered her hands, which is in the
  book. Some people are simply born unable to touch iron, which is in another
  book." The background never names her people. A Tiefling Inquisitor is the
  left hand that is what the book condemns, and knows both pages.
- **Exorcist.** "The procedure is much the same whether it is a fiend or a
  philosophy." The Tiefling Exorcist is the one everyone in the room assumes is
  the fiend, and charges anyway.
- **Bailiff.** "The guard walks you to the edge of town", from the guard's
  side. The Tiefling Bailiff carries the Badge that was used on them.
- **Herald.** "Harming a herald is how small quarrels become wars." The first
  immunity the species ever had.
- **Servant.** Owned twice: by the masters who still write, and by the reading.
- **Survivor.** "You know exactly what is out there, because it had you in its
  hands and let go." On a Tiefling the thing that let go may be the reading
  itself.
- **Fated.** "Promised to a witch, or a demonic entity, or a dark god." The
  Fated Tiefling *looks* like the promise, which is the joke and the wound.
- **Destined.** The horned chosen one. Comic, and the house's first answer
  ("we were the chosen, long before") taken literally.
- **Gambler.** "Somebody will stake you on your face alone, because your face
  is good and everybody has heard something." On a Tiefling, everybody has.
- **Debunker.** "There is always a reasonable explanation." The Tiefling
  Debunker has one for their own horns, and it is the shift.
- **Shadow.** Doubly read as the dark: the nightmare face and the Lower Planes
  in one body. Handle with the shadow budget in mind (Monk page).
- **Dragon Cultist.** The self-condemned in the cult of the self-authored; the
  cultist who would like, for once, to be told what to be.

---

## 9. Decisions log

**Decided (Julio, 2026-09-08)**

- The Tiefling stays distinct from the Aasimar and from host peoples; no
  host-culture draw. Subculture, recognisable on sight.
- The lack of a "we" stays, and its meaning is *hostile* isolation; the
  Aasimar's lack is upward. The Tiefling canon's "the only one" is read as "the
  only one whose isolation is hostile".
- The shared priesthood, split by the Aasimar's side, is deep lore for both
  entries and never on the page.

**Standing (canon)**

- No biological determinism; never state a parallel; never resolve the
  carvings; keep the "we" out; the legacy is power, not impairment.

**Open**

- The canon says "all that survives on the page is one sentence about carvings
  nobody can read any more". The current species entry has the crown-horns
  sentence and no carvings sentence. Either the carvings line was lost in a
  rewrite or the canon should read "one sentence about the crowns". Julio's
  call.
- The Fiendish Legacy ability is drawn from Intelligence, Wisdom and Charisma
  at random. A Cleric with a Charisma legacy is legal and a little odd; a
  synergy nudge toward the class's own ability (Decree 0005) would be
  consistent with the Aasimar's Warlock decision.
- The `grimdark` register is thin for a Tiefling without a greatsword (six
  weapons, no implement, no clothing); the *penitent* and *heretic* vocabulary
  could reach armour and focus.

**Repairs**

- Prayer ledger, Tiefling × War: *"War is doesn't ask."* Typo; *"War doesn't
  ask. You still have to answer."*

---

## 10. Lines

*Proposals for the three trait entries that have none. Second person, the
species entry's own register (plain, unsentimental, the fact and then the
sentence about the fact). No em-dashes.*

| Entry | Line |
|---|---|
| **Darkvision** | *Nobody ever lit a lamp for you. You learned to do without.* |
| **Otherworldly Presence** | *A little theatre. It is the one thing they expect from you, so you learned to use it.* |
| **Fiendish Legacy: Infernal** | *The fire was always there. What it is for was never decided by them.* |
| **Fiendish Legacy: Abyssal** | *The colours move while you sleep. So, some mornings, does what you can do.* |
| **Fiendish Legacy: Chthonic** | *No fire, no pain. Only the door, and you know which side of it you stand on.* |

The heritage paragraphs (§3) are Julio's and stand as the species' physical
voice; the lines above sit under the rules, not in place of the paragraphs.

---

## 11. Pointers

- **[Aasimar.md](Aasimar.md)** and **[Celestials.md](Celestials.md)**: the other
  end of the mechanism, and the beings who prevent.
- **Warlock page**: the Fiend patron; toxicity rather than malice; the shared
  `grimdark` register.
- **Paladin, Ranger, Fighter, Rogue pages**: the four features that reverse the
  reading for a round, a night, a save, a life.
- **Dragon canon**: the Tiefling as an Ascending candidate with nothing to
  overcome but a reading.
- **Cultural Inspirations**: Egypt as the register for what was there before;
  `grimdark`'s reach.
