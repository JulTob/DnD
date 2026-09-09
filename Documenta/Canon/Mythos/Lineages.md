# 🧬 Lineages: what a sub-identity is, people by people

> 🚧 **In flow.** 1 of 9 chapters are still proposals. 🔒 0 · 🧾 1 · 🔎 7 · 🚧 1

*Wiki entry for the design team. Every people page read its species whole. None
read the layer underneath: the Elf's six lineages, the Tiefling's three
legacies, the Gnome's two, the Goliath's six heritages, the Dragonborn's ten
ancestries, the Aasimar's three revelations and their Descents, the Human's
twelve cultures. This page reads them as literature and finds that the peoples
do not agree on what a lineage **is**. Compiled 2026-09-09 from
`AtlasActorLudi/SpeciesKit/`.*

> **In one sentence.** A lineage in this setting is a migration remembered, an
> ancestor's decision, a deed performed, a body described, a damage type, or a
> compass direction, depending on the people, and the ranking of those six
> answers is exactly the ranking of how well each people is written.

---

## 🔎 1. The seven answers

| People | A lineage is… | Count | Verdict |
|---|---|---|---|
| **Elf** | a migration remembered, with its temperament, its mark, and its counsel | 6 | ✅✅ the model |
| **Gnome** | a decision one ancestor made | 2 | ✅✅ the cleanest device |
| **Tiefling** | a body described, and nothing else | 3 | ✅ exactly canon-compliant |
| **Goliath** | a deed the ancestor performed | 6 | ✅ named as verbs |
| **Aasimar** | a choice re-made every time you transform | 3 (+ 7 Descents) | ✅ the only live choice |
| **Dragonborn** | a damage type | 10 | ⚠️ mechanics only |
| **Human** | a compass direction | 12 | ⚠️ placeholders |

That spread is not an accident of effort; it is a spectrum of **how much the
lineage is asked to carry**. Where the people's own idea is strong (Elf drift,
Gnome workshop, Tiefling belief) the lineage is an instrument of it. Where the
idea is thin, the lineage is a lookup.

---

## 🔎 2. Elf: six migrations, and the fourth slot nobody named

Each Elf lineage entry carries the same four things, in the same order, in the
first person plural the Elves canon requires:

1. **What our forebears did** (a migration or a refusal to migrate)
2. **The temperament it produced**
3. **The physical mark**
4. **Who we consult when it matters**

That fourth slot is the discovery. *"We consult our druids first in important
matters"* (Wood). *"We find our answers among the magi and the wizards"*
(High). *"Our own consult the priest and the cleric"* (Drow). *"When hardship
comes, we consult the oracles and mystics"* (Shadow). **Each lineage is defined
by its epistemology**: who a people asks is a sharper cultural fact than what a
people looks like, and no other species entry in the project does it.

| Lineage | The migration | The mark | Reading |
|---|---|---|---|
| **Wood** | *"Our forebears stayed where the trees were."* | hairier; some with little stag horns; some still paint their faces | ✅ The drift made literal and the canon's own example. The stag horns are the one detail that escapes Tolkien entirely and reaches Cernunnos and the Wild Hunt. |
| **High** | *"The ships were ours."* | golden hair; skin cold to the touch whatever its tone | ✅ *"We are still of the ice"* is the best line in the set: a people carrying the temperature of a migration their descendants never saw. The "whatever its tone" clause quietly refuses to make golden hair mean white skin. |
| **Drow / Dark** | *"Our people went to the Underdark, and stayed, and built something others feared: a meritocracy."* | silvery hair; skin like the stones of home | ✅✅ The strongest single inversion in the project. They are not evil; they are **slandered**: *"We thrived through unity, faith and strategy while others poisoned our legend. Now we defend a peace that others take for granted."* That reframes the most exhausted cliché in the hobby as a libel with a motive, and it costs one sentence. |
| **Fae** | stayed by the crossings, never came across | ears sometimes as long as the arms; *"the most beautiful of all elvenkind, even with our charms off"* | ✅ The vanity is stated in the collective voice and is funny because it is sincere. |
| **Shadow** | *"Our kind took what was left: the Shadow realm."* | grey to white to black skin; eyes all white | ✅✅ The temperament is **caused**, not asserted: *"Nightmares come true in the Shadow realm, so we learnt to be stoic, reflective and analytic, to discern dream from thought."* A people whose analytic habit is a survival adaptation to their own metaphysics. |

⚠️ **`Drow.py` and `Dark_Elf.py` hold the same entry text**, one described as
"the 2024 Drow Elf Heritage Shape" and the other as "the world-free 2024 Dark
Elf Heritage Shape". Two names for one culture, against the canon's one-key-one-
culture rule and against the Elf page's own reading. A player can be dealt
either. Decide which name the setting keeps; the *text* is right whichever wins.

---

## 🔎 3. Gnome: a lineage as an ancestor's decision

Two lineages, and they are two answers to a single question the species entry
poses without asking it: **did your family take the city offer?**

> **Rock.** *"Your family took the city offer and filled a workshop with it.
> Lenses, springs, a bird that sings on the hour and has done since your
> great-grandfather wound it."*
>
> **Forest.** *"Your family never took the city offer, but put down roots in
> the forest nearby… The fae, they say, are nearer out there. Some of it rubbed
> off."*

✅✅ This is the best structural device in the lineage layer, and it should be
copied. A lineage that is a **decision an ancestor made** cannot be read as
biological determinism, satisfies the species law without a word of argument,
and gives every Gnome a family history in nine words. The bird still running
since a great-grandfather wound it does more work than a paragraph of
worldbuilding: it dates the workshop, it establishes the craft, and it implies
that Gnomes measure time in generations of maintenance.

The Gnome page found the entries had left the joke-Gnome behind; the lineages
are where that happened.

---

## 🔎 4. Tiefling: three bodies, no personalities

| Legacy | The description |
|---|---|
| **Abyssal** | *"You descend from demons, chaotic beings with no defined shape. The chaos of the abyss reflects in your metallic fur of bright color, with spots and lines, sometimes shifting and moving from place to place or changing shape each time you wake up."* |
| **Chthonic** | *"Yours is the aspect of Hades, the most neutral of hells. No fire, no pain, only darkness… sometimes the colors of animals like foxes, wolves and bulls, and sometimes the tones of a corpse."* |
| **Infernal** | *"Yours is the aspect of the Nine Hells: fire and brimstone. Your horns are black like onyx… fur is either black or a bright color that resembles a flame… with a metallic, almost golden, shine."* |

✅✅ **All three describe an appearance and stop.** No temperament, no
inclination, no moral hint. That is the Tiefling canon's rule 1 obeyed exactly
(*"Describe what the legacy does and what the body looks like, and stop"*), and
it is the only lineage set in the project that obeys a rule by omission.

✅ **The fur is a real departure.** Published tieflings have skin; these have
fur, metallic and patterned, and the Abyssal's shifts overnight. That single
choice moves the species away from the red-skinned devil silhouette everyone
arrives expecting and toward something animal, which pairs with the canon's
buried Egyptian priesthood and its crown-horns better than the standard art
ever did.

✅ **Chthonic is the original of the three.** Hades read as *neutral* rather
than evil (*"No fire, no pain, only darkness"*) is a correction to the whole
infernal tradition, made in six words, and it gives the setting a hell that
was never a punishment. It is also the legacy that best fits the canon's
"belief made them" mechanism: a realm that only became lower when someone
called it that.

⚠️ One inherited phrase to watch: *"You descend from demons"* (Abyssal) is
ancestry language in a species whose canon says a tiefling is born to ordinary
parents. Abyssal, Chthonic and Infernal are **aspects**, not pedigrees, and the
other two say so. One word.

---

## 🔎 5. Goliath: heritages named as verbs

Cloud's Jaunt, Fire's Burn, Frost's Chill, Hill's Tumble, Stone's Endurance,
Storm's Thunder.

✅ Each is named for **what the giant did**, not what the giant was, which is
the grammatical form of the entry's own claim: *"Your ancestors did not command
the avalanche. They were the avalanche, and the mountain, and the thunder."*
A heritage the Goliath carries is a deed still being performed at small scale.
The entry's *"Before anyone had a word for Winter, she had a name and a
temper"* is the best sentence in the species layer and it earns the six verbs
under it.

The one thing missing is the fourth Elf slot: six heritages, six deeds, and no
line on what each kind of giant's descendants *do differently now*. The Elf
model would give each a counsel (who a Frost's Chill Goliath asks when it
matters) and cost six sentences.

---

## 🔎 6. Aasimar: the choice re-made

Inner Radiance, Necrotic Shroud, Talarian Wings, chosen at each
transformation, plus the seven Descents (Angel, Muse, Constellation, Star,
Planetar, Seraph, Sphinx) that say what marked you.

✅ This is the only sub-identity in the project that is **re-decided during
play**, and the Feature-Text canon explicitly protects it as the exception to
no-open-choice. It is also thematically exact: the Aasimar's Ideal is fixed and
their expression of it is not, which is the difference between the species and
its mark.

✅ The Descent supplies the identity the Revelation does not: a kind, a name,
and a manner (Draft-Tables §C). *"The marks suggest a tie to the Sphinx Aidos;
you may belong to its lineage."* The **may** is the whole design.

---

## 🔎 7. Dragonborn and Human: the two thin ones

**Dragonborn.** Ten colours, each resolving to a damage type and a resistance.
The species entry does the work (*"their origins do not determine their
destiny"*), and the ancestry itself carries no culture, no temperament and no
line. ⚠️ It is the largest sub-identity set in the project and the least
written: ten options, one variable. The Dragons canon offers the fix without
new lore, since a colour is what a tradition made of a dragon rather than what
the dragon was, so each ancestry could carry one sentence about the **story
told about that colour** rather than the colour itself.

**Human.** Twelve: Local, Foreigner, Highlander, Nomad, Islander, Forester,
Plainsfolk, Urbanite, Northerner, Southerner, Easterner, Westerner. ⚠️ These
are relative directions, not cultures: *Foreigner* is a description of the
observer, not the observed, and four of the twelve are compass bearings from an
unstated centre. The Names page found only `Islander` is read by the name
module. The Human page's compact (owed and owing) suggests the replacement:
twelve **relations to a place** rather than positions in it, keyed to the
Cultural-Inspirations rows the Human already holds.

---

## 🚧 8. What this page recommends

1. **Adopt the Elf's four-slot form** (migration, temperament, mark, counsel)
   as the house shape for a lineage entry. The Goliath's six heritages and the
   Dragonborn's ten ancestries are one sentence each away from it.
2. **Adopt the Gnome's device** (a lineage is a decision an ancestor made)
   wherever a new sub-identity is written. It disposes of determinism by
   construction.
3. **Resolve Drow versus Dark Elf**: one name, one file.
4. **Change one word in Abyssal** so a legacy is an aspect and not a pedigree.
5. **Give the Dragonborn ancestries the story, not the colour**, per the
   Dragons canon.
6. **Replace the Human's twelve directions** with twelve relations.

None of these is a rewrite. The lineage layer is close to finished in four
peoples and a sentence short in three.

---

## 🧾 9. Pointers

- **Elves-and-the-Dreaming canon**: lineages are cultures, drift is collective.
- **Tieflings-and-the-Shift canon**: describe the body and stop.
- **Dragons-and-the-Overcoming canon**: every silhouette is one tradition's
  answer.
- **Elf**, **Gnome**, **Tiefling**, **Goliath**, **Dragonborn**, **Human**,
  **Aasimar** pages: the species readings this sits under.
- **Celestials §3**: the Descents.
- **Names §4**: the Human cultures and the lineage-name collisions.
