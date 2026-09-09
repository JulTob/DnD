# 🔤 Names: the first line of every sheet

> 🚧 **Draft.** Analysis and proposals, not yet authoritative. Under review.

*Wiki entry for the design team. `AtlasNomina/Map_of_Names.py` composes a name
from a per-people module in `AtlasNomina/Races/`, by list pick, syllable
mixing and phonotactic construction, on a ladder that ends in a roster that
cannot fail. Compiled 2026-09-08 from the code and ninety generated names
(ten peoples, three genders, three seeds).*

> **In one sentence.** The Dwarf module is the proof that a name can carry a
> whole culture; half the other modules carry a documented culture in their
> docstring and an English compound in their surname list.

---

## 1. The engine

Each people has a module offering four ingredients: `Names`, `Surnames`,
`Phonotactic` (onset, nucleus, coda) and `Surphonotactic`, gated by the genus
string (kind, gender, class, background). `NewName` builds a given name and a
surname by a ladder of methods (list pick, syllabic recomposition, weighted
phonotactics, Markov), each tried a bounded number of times, and steps aside to
`LastResortName` if every rung fails. A module that will not import is
**reported**, not silently replaced ("the sheet quietly filled with template
names and nobody was told which module was down").

✅ **The ladder is right, and it was learned the hard way.** The 2026-08-30 note
records that `Race_Ingredient` had been called but defined nowhere, so every
Character had fallen through to the last-resort roster for a while and nobody
saw it. The same lesson as the Titles' `Genus` bug: read the output.

⚠️ `NewName` and `Namer` call the **global** `random.seed(lusor.seed)`. A
Character's draws belong to its own Dice (Decree 0002). This has a side effect
worth knowing: it makes the level-19 Epic Boon's global `random.sample` (Feats
page) deterministic by accident, seeded by whichever name was drawn last.

---

## 2. The shape of a name, by people

| People | Module | Shape | Documented inspiration | Sample |
|---|---|---|---|---|
| **Dwarf** | Dwarf (2,277 lines) | given, given, surname, surname | Golden Age Spain, Renaissance Italy, Portuguese, Carthage | *Salvaro Esteban Herrero Eperta; Felicidad Igusti Sarehido Birremonte; Eorterina Pamona Forjablanca Forjado* |
| **Gnome** | Gnome (76) | given ×3, surname | Italian, Galician | *Serafina Zenlu Fiorgiora Ludutti; Hartwig Catania Casota Pietravalle* |
| **Elf** | Elf (665) | given, surname | Persian, Huldufólk, Iceland, Romani, Celtic Ireland; "th → s/t/z, elves don't show their tongues" | *Duillinen Ebonwood; Durgwen Moonlace; Thaeka Dawnbringerg* |
| **Human** | Human (191) | given, surname | "African, Native, Aboriginal origins"; Polynesian under `Islander` | *Jarar Elalale; Batuparay Coetahitanga; Mahanui Mahunti* |
| **Orc** | Orc (240) | given, surname | Britain, Celts, Vikings, Cowboy America, Native America, Precolumbian, "the Boyz of 40k"; "'S' would bite the tongue, 'z' instead" | *Ralig Drexadztone; Zavron Tresinmax; Ezarona Zerpentgaze* |
| **Halfling** | Halfling (86) | given, surname | Food, delights of life, Hobbits; names English, surnames French | *Macadamia Jus; Fejoa Noisette; Carric Salaise* |
| **Tiefling** | Fiend (986) | given only (empty surname) | Demonology; virtue names in English, Spanish, French; Egypt | *Luz; Nija; Calgonzon; Bababala* |
| **Aasimar** | Celestial (107) | given, surname | Latin, Greek, Hebrew, Kabbalah, planets, angels, Valkyries | *Anael Valizvaliz; Taurus Zeriana; Talinix Drakavir* |
| **Dragonborn** | Dragon (99) | given, surname | "Dragons are not born, they become"; Chinese, Japanese, real dragons | *Bakunawa Wolfrion; Tiamat Gralator; Dedanlok Astormor* |
| **Goliath** | Giant (942) | given, surname + **son** | "Giants (meaning)"; Wairimu, Ōga | *Drumax Lionenyivson; Ozustia Aquilason* |

---

## 3. Where the names carry the culture

✅✅ **Dwarf.** Four names in the Iberian shape, Golden Age given names
(Salvaro, Benicia, Felicidad, Octavia, Juanito), and surnames that translate the
trade (*Herrero* is smith; *Forjablanca* and *Luzoforja* are forge-compounds).
The soul-metal canon is in the surname without a word of explanation. This is
the standard the other nine should meet.

✅ **Gnome.** Italian and Galician, the workshop-city register the Gnome page
asked for. *Hartwig* and *Wunderblatt* are a German leak.

✅ **Orc.** The phonological law ("'S' would bite the tongue, 'z' instead") is
the kind of rule that makes a people audible: *Zavron, Zerpentgaze, Skildzorn*.
The wind-path canon has no key in the module yet; the inspirations list is the
old one (Vikings, cowboys, 40k).

✅ **Dragon.** The docstring restates the canon correctly and *Bakunawa* (the
Filipino moon-eater) shows the "every silhouette is one tradition's answer"
rule reaching the name pool.

✅ **Tiefling and Aasimar share a name.** *Luz* (Spanish, light) is in the
Celestial agender list and the Fiend virtue list, and surfaced as a Tiefling's
whole name. The two species are one mechanism seen from opposite ends, and here
the name pool says so by accident or design. Keep it.

---

## 4. Where the surname undoes the given name

⚠️ **Elf.** The given names come from the phonotactics and sound like the
documented cultures (*Duillinen, Hislin, Durgwen, Eofolin, Thaeka*). The
surname list is `Brightbrow, Nightshade, Astralborn, Autumnheart, Dawnpath,
Raingaze, Ravenflow, Ravenwatcherg…`: English compounds in the Tolkien-by-way-
of-Warcraft register, and none of the Persian, Icelandic, Romani or Irish
material the docstring names. *Ravenwatcherg* carries a stray `g` in source.
The Elf canon says lineages are cultures; the surname is where a culture would
show, and it shows Warcraft.

⚠️ **Halfling.** *Macadamia Jus, Fejoa Noisette, Cukiegina Deromel*: the food
given names are the joke register the Halfling page found in the species
entries, now on the name line too. The French surnames (*Noisette, Salaise,
Deromel*) are the good half: cuisine as a culture, not a punchline. Keep the
surnames, retire the literal foods.

⚠️ **Goliath.** `NewName` hard-codes `{surname}son` for every Giant. The
patronymic is Norse; the Giants' canon is Rome, Sparta and Homer, and
*Aquilason* (Latin eagle + Norse son) is the collision in one word. The
Goliath page's register wants a *gens* or a cognomen, not a patronymic.

⚠️ **Human.** The cultures drawn (`Local, Foreigner, Highlander, Nomad,
Islander, Forester, Plainsfolk, Urbanite, Northerner…`) are relative
geography, not the Cultural-Inspirations keys, and only `Islander` is read by
the module. `MALE = "Je" in Type` is a typo for `"He"`, so **no Human male name
list has ever fired**. Some Polynesian names carry diaereses that look like
mixer output baked into source (*Joekuelëa, Jalïa, Cäiulani, Cülei*).
`HumanLegacy.py` (7,105 lines) is imported by nothing.

⚠️ **Tiefling.** `Fiend.Surnames` returns `[""]`, so every Tiefling is
*"Bababala "* with a trailing space. Two readings, and the canon supports
either: a tiefling born to ordinary parents carries the **family's** name,
which is the most ordinary fact about them and the cruellest (the Tieflings
canon: "born to ordinary parents"); or the family's name was withheld, and the
single name is the grammar of the missing "we". Either is a decision. The
trailing space is a bug. The virtue list is strong (*Luz, Miedo, Recuerdo,
Calamidad, Désespoir, Chagrin, Submit, Remember, Forsaken*: Puritan virtue names
in three languages, the 2014 tradition done properly), and the Egyptian names
(*Sahura, Bubastis, Nenet, Sanura*) reach the canon's register. The same list
also holds *Watson, Harris, Coleman, Reynolds, Williams, Boston*, and *Doombringer,
Skullrend, Demonblood*. Two entries fuse for a missing comma (`"Honesty" "Zephyron"`,
`"Honesty" "Honor"`).

⚠️ **Aasimar.** *Taurus, Gemini, Leo, Orion, Perseus, Metatron, Elohim, Anubis*
as given names. The loaded-names rule keeps lore names in the pool; *Elohim*
is not a lore name, it is the word for God, in a setting whose Celestials
have no sender. Undecided. The orthography rule is half applied: *Ofiucus,
Casiopea* beside *Cassiopea, Athena, Nyx*. The `Valkyrie` gate adds Norse
material to a Latin-Greek pool.

---

## 5. Gender

For the same seed, Human, Aasimar, Goliath and Halfling produced the **same
name for He, She and They**. Dwarf, Gnome, Elf, Orc, Tiefling and Dragonborn
did not. Whether a name should respond to gender is a design question (the
Aasimar canon's "what is one" would argue it should not, for Aasimar); that it
responds for six peoples and not four is an accident of list order, not a
decision. Record which it should be per people.

The Noble prefix (*Lord, Lady, Noble*) is the only place gender is written on
the name line. *Noble Frazarme* for They reads as a rank, not an honorific.

---

## 6. Two copies of the Titles

`AtlasNomina/Map_of_Titles.py` (9,470 lines) and `AtlasEpica/Map_of_Titles.py`
(10,049 lines) are two divergent copies of the same vocabulary. Characters use
the Epica one; Biomes and NPCs import the Nomina one. One of them is the
record.

---

## 7. Proposals

1. **Elf surnames from the documented cultures**: Persian and Icelandic
   patronymic shapes, Irish *Ó* and *Ní*, Romani; drop the English compounds.
   The lineages-are-cultures canon can key them: Wood, High, Dark, Fae, Shadow
   each a drift of the same pool.
2. **Goliath**: replace `son` with a cognomen or *gens* form (*Ozustia of the
   Aquilae*; *Drumax Leonius*). One branch in `NewName`.
3. **Halfling**: keep the French surnames, replace the food given names with
   English rural given names (*Carric, Leggela* already work).
4. **Human**: fix `"Je"`; key the module to the Cultural-Inspirations keys the
   Humans table already draws (`nomina_culture`), and retire the relative-
   geography labels; decide HumanLegacy.
5. **Tiefling**: decide the surname (family's or none); strip the space.
6. **Aasimar**: apply the orthography rule to the list; decide *Elohim*,
   *Metatron*, *Anubis*.
7. **Names through the Character's Dice**, not the global seed.
8. **One Titles file.**

---

## 8. Decisions log

**Standing**: the ladder and its last-resort rosters; the Dwarf shape; the Orc
z-rule; the Dragon docstring.

**Open**: everything in §7; gender response per people (§5); the Tiefling
surname; *Elohim* and *Mestizo* (Stories page) as loaded names outside lore.

---

## 9. Pointers

- **Cultural-Inspirations canon**: the keys the modules should read.
- **Dwarf page**: why the four-name shape is the culture.
- **Elf page**: lineages as cultures, the surname as the drift's record.
- **Tiefling page**: born to ordinary parents; no "we".
- **Stories-and-Titles**: the title composed beside the name; hometowns with
  no culture key.
