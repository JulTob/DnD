# ⛏️ Dwarf

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from the Dwarf kit, the species entry, `Cultural-Inspirations.md`,
the old wiki's Dwarf paragraph, the class analyses, and QST-0094. Where Julio
has decided, the decision is stated as such; where this page proposes, it says so.*

> **In one sentence.** Dwarves remember. They ruled the world once, the Great
> Mountain fell, and they spread across it carrying their ledgers and their
> grudges; metal is holy to them because a soul is a metal, given, and it must
> be proven.

---

## 1. Where the Dwarf lives in the code

| What | Where | State |
|---|---|---|
| Species entry (Julio's) | `AtlasActorLudi/SpeciesKit/Dwarves/__init__.py` | Shipping. First person plural ("we remember"). Closes on what to do with the gold. |
| Traits and rules | `Dwarves/traits.py`, `resolution.py` | Rule voice landed (QST-0094). **No inspiration lines yet**; four were proposed in QST-0094 and await Julio (§9). Darkvision 120, Resilience, Toughness, Stonecunning. |
| Names | `AtlasNomina/Races/Dwarf.py` | Inspirations: the Golden Age of Spain (conquistadores), Renaissance Italy, Portuguese, the Carthaginian empire (Hannibal). |
| Culture keys | `iberia`, `andalus`; legends `folklore_dwarf`, `tolkien_dwarves` | Toledo steel in the Materials map; mithril through the Tolkien register. Dwarves lean to metals through extra weight, never a closed door. |
| Prayer | `Map_of_Cleric_Prayers.py` | *Metal shapes in the forge. People in the challenge.* *A saint is a sinner trying to be better.* *Forgetting is hard, but harder is forgiving.* Plus Life, Knowledge (Cervantes), War (*No hay atajo sin trabajo*), Grave (Teresa of Ávila, Quevedo). |
| Old wiki | `app/Wiki/Lore.html` | The conquistador paragraph: Bank Templars, Basque-inspired Mountain Dwarves, goldsaints and silversaints, the Missing Crown and the Holy Gold. Unedited and repetitive; the source of the lore, not its final form. |
| Metaphysic | `Dragons-and-the-Overcoming.md`, the peoples table | *Platonic soul-metal; Sainthood as transcendence into one's own pure substance.* |

---

## 2. Origin: soul-metal

Each people has one organising idea. The Dwarf's: **a soul is a metal, given,
and it must be proven.** The Celestial's Ideal is fixed and cannot bend; the
Elf drifts by collective consent; the Dragon authors itself alone; the Dwarf's
metal is handed down and then tested, in the forge and in the challenge, until
it is pure or it is not. *"Metal shapes in the forge. People in the
challenge."*

**Sainthood** is the transcendence into one's own pure substance: a Dwarf who
proved the metal all the way down. The goldsaints and silversaints of the old
halls are Dwarves who did. Saints belong to the Dwarves and stay out of the
Celestials' system (QST-0050): two things that look alike from a distance, on
purpose, and are not the same. *"A saint is a sinner trying to be better."*

**The metal shows.** The Aasimar's talaria shine like metals (black iron, gold,
red iron, silver, verdigris, bronze) and confirm nothing; the ambiguity is
deliberate DM space. A Dwarf who notices would say the Celestials borrowed
the idea. A Celestial would say nothing.

**Physical traits.** Darkvision to 120 feet (the deepest on the roster),
resistance to poison, one Hit Point per level, and Stonecunning (tremorsense
on stone). The species law permits biology; these are the mines in the body.

---

## 3. History: the Great Mountain fell

*"Our people ruled the world once. Then the Great Mountain fell, the Gilded Era
ended with it, and the dwarves spread out across the world instead, carrying
their ledgers and their grudges."*

The old wiki fills the shape and the entry keeps the shape only, which is
right: the Gilded Era was an empire of holy rites, engineering, pageantry and
gold, devoted to divine monarchs and its own destiny; hubris and spiritual
fervour shattered it; the people scattered into rival kingdoms and enclaves.
Two survive as names:

- **The Bank Templars**: merchant-keepers of vaults, the bank-cathedrals, the
  fleets and the long terrible expeditions. Commerce and faith in one house.
- **The Mountain Dwarves**: isolationist redoubts, Basque-inspired, keeping the
  old ways and a hard-won solitude.

Two prayers survive as politics: some pray for the **Missing Crown** (the
restoration), some for the **Holy Gold** (the faith without the throne). The
species entry gives the player the third: *"what will you do with the gold you
carry home? Raise a shrine to a Saint? Open a Bank Temple? Or spend it on
spices and mead?"*

**The clan absolves.** *"Come back home with enough gold, and your clan will
hail you as a hero, no matter your past transgressions."* This is the most
consequential sentence in the entry: it forgives the thief, the mercenary and
the exile in advance, and it makes the Dwarf the one people whose adventurer
has a guaranteed homecoming with one condition attached. Every Dwarf
adventurer's story has an accountant at the end of it.

**Others call it greed.** *"They do not understand. Gold never corrupts. A gilded
prayer to our Saints and Ancestors will never weaken."* The Dwarf does not
argue the point; the sentence is doctrine, and the Life prayers argue the other
side from inside (*"Gold held is not living. Gold earned is gold spent."*
*"The real gold is in your soul."*). The species holds both.

---

## 4. Culture: Iberia and Andalus, two keys, one people

**The law:** one key, one culture; Iberia and al-Andalus are two keys, not a
blend, and the overlap is modelled by influence, not by merging. The wiki names
the well: the Spanish-speaking world as an analogy to the old Spanish empire,
itself shaped by Carthage, Rome, the Umayyads, Sefarad, and the Reconquista.
"History is messy."

**Iberia**: Toledo steel, the Cid, Roncevaux on the Dwarf border (the Song of
Roland is set in the Pyrenees against Zaragoza: the Paladin's founding poem
happens at a Dwarf pass), Santiago and Calatrava (the Iberian military orders
are the crusader register on the Iberian key), La Verdadera Destreza (the sword
as geometry: the Open Hand Monk, the Battle Master's *tretas*), the tercio's
*alférez* (the Banneret), Don Quixote (the Glory Paladin: *Living Legend* is
"the legends, whether true or exaggerated"), the picaresque (Lazarillo: the
Rogue's register), the cantigas de escarnio and the romancero (the Bard), the
*Libro de la montería* and the montero (the Ranger), Juanelo Turriano's
*artificio* (the Artificer), the Cueva de Salamanca (the Occultist Warlock;
the Shadow background's lost shadow), Teresa of Ávila, Quevedo and Machado in
the prayers, the Basajaun and Mari of Anboto on the Basque side (the Druid's
teaching wild man and the lady who is the weather).

**Andalus**: Abbas ibn Firnas, who flew over Córdoba (the Artificer), Andalusi
falconry (the Beast Master's falcon), the *baratero*'s navaja (the Shadow
Monk), *"This world is a bridge. We all must cross"* in the Grave prayers, and
the whole register of a civilisation that was the other half of the same
peninsula. The Song of Roland's enemy is this key; the Dwarves carry both sides
of Roncevaux.

**Legends**: `tolkien_dwarves` (rune-axes, delving, mithril mail) and
`folklore_dwarf` (knockers, nisse, the tapping hammer), the latter shared with
the Gnomes.

**Names**: the Golden Age of Spain, Renaissance Italy, Portuguese, Carthage.
The generator's Dwarves are called Elidio Gabibir Elora Martinez, Vivian
Valleja Pedraferra Minacorazón, Etebar Santanitán Ardorerojo Abecero: long,
compound, Iberian and Italianate, a surname like a ledger line.

**Materials**: metals through extra weight (Toledo steel, and mithril through
the Tolkien register); gems lean to the Gnomes. "Leanings, not laws."

---

## 5. Metaphysics: given, proven, spent

**Against the Celestials.** Fixed against given-and-proven: an Aasimar cannot
change the spark; a Dwarf must change the metal. The two peoples are the
setting's two Platonisms and they disagree about whether the Form is finished.
A Dwarf Cleric of Life ("the real gold is in your soul") is the argument said
aloud.

**Against the Dragons.** *"A dwarf who spends ninety years on one gem may
Ascend through the obsession itself, because the obsession was the only thing
in that life that was truly theirs. Seen from outside this looks like a curse,
and the family will describe it that way."* The canon wrote the Dwarf Draconic
Sorcerer before the class did. The Dwarf who proves the metal all the way is a
Saint; the Dwarf who proves *one thing* all the way, alone, is a dragon, and
the clan cannot tell the difference from outside, which is the tragedy.

**Against the Elves.** Given against dreamt. A Dwarf is what the forge made; an
Elf is what the people imagined. "Dwarves and Gnomes trade and share
settlements", and the Gnome is the middle point of the Renaissance pair: the
Dwarf's metals and the Gnome's jewels are one trade route.

**The mountain is owed.** *"Everything we dwarves ever built, we built while
chasing it: the mines."* The Dwarf and the land are in a debt relationship, and
the Great Mountain fell. A Dwarf Druid is the mountain's creditor among a
people of debtors; Stonecunning is attention paid to stone, and the Basajaun
taught the farmers to forge. Deep lore, never on the page: the fall of the
Great Mountain as the covenant's breach.

---

## 6. The classes: what the metal does in each

| Class | The Dwarf in it |
|---|---|
| **Fighter** | *"Metal shapes in the forge. People in the challenge."* The class thesis in the species' mouth. The Banneret is the tercio's alférez, sworn not to let the banner fall: Iberian before anyone's. |
| **Paladin** | The Cid, exiled by his king and still fighting in the king's name ("what a good vassal, if he only had a good lord"); Santiago and Calatrava; Roncevaux on the border. The Glory Paladin is Don Quixote, and *Living Legend* is his feature. |
| **Rogue** | The pícaro: the Thief the clan absolves in advance. A Dwarf who robs a bank-cathedral and brings the gold home is the species' own kind of hero. |
| **Bard** | The cantigas de escarnio in a bank-cathedral; the romancero as the people's memory; the vihuela; Lorca's duende was always the Dwarf's. |
| **Monk** | Destreza without the sword (Open Hand): the circle on the floor is Iberian. The baratero's knife (Shadow). A Monk needs no food; the clan's "come back with enough gold" has no purchase, which is the character. |
| **Wizard** | The ledger. The Spellbook map already draws "a sheaf of steel leaves on a ring, each leaf a page struck rather than written" for Smith's Tools. A Bank Templar who keeps this book. |
| **Artificer** | Juanelo's *artificio*; Abbas ibn Firnas's wings; the Armorer who builds the given metal into armour and steps inside ("what you make with your own hands is yours in a way no gift will ever be" against "metal is holy": the Dwarf who made what the Saints say was given). |
| **Cleric** | The demanding parent is the Dwarf's default: the metal was given so it could be proven. The Dwarf War Cleric needs no reconciliation; the Dwarf Life Cleric argues *"Gold, like life, must be shared and passed on"* against a people who count everything. |
| **Barbarian** | The Zealot taken by a **Saint**, not a god (the Zealot's god should be species-drawn, Barbarian page). Rage as the crucible. |
| **Sorcerer** | The ninety-year gem (§5). Draconic Sorcery as the family's curse. |
| **Druid** | The mountain's creditor; the Basajaun's pupil; Mari's weather. |
| **Ranger** | The montero; the falconer of al-Andalus. |
| **Warlock** | The Cueva de Salamanca: the Devil's school where the last student out pays, and one escaped by leaving his shadow. The Occultist (Intelligence) variant has an Iberian home; a Dwarf with the Shadow background is the Salamanca student. A Dwarf Warlock's gold has a lien on it. |

---

## 7. Backgrounds

- **Squire.** "You served someone the songs are about." Sancho. A Dwarf Squire
  Paladin who *became* the one the songs are about is a Quixote who won.
- **Servant.** The Bank Templar's sideboard; "you knew where the silver was
  hidden." The Servant Dwarf knows exactly what the silver weighs.
- **Gambler.** "You have been rich. Twice in one night you have been nothing."
  A Dwarf who has been nothing has an accountant waiting at home.
- **Sellsword.** "A fair price and the good name that brings the next
  contract." The tercio for hire; the good name is the clan's.
- **Hermeticist.** The alchemist-jeweller: "gold to the sun, silver to the
  moon." A Dwarf Hermeticist treats correspondence as metallurgy.
- **Stranger.** A people who remember, among a people who forgot: the Dwarf
  Stranger's old ones keep the Missing Crown.
- **Inquisitor.** "You still believe. That is the part nobody outside ever
  understands." The Dwarf Inquisitor of a faith that is also a bank.
- **Bailiff.** The law that serves the vault. Forgery Kit against a ledger.
- **Archaeologist.** The record of the Gilded Era; "an accurate account… buys
  you the rest of your life": a Dwarf Archaeologist is paid twice, once by the
  college and once by the clan.
- **Tomb Raider.** The Great Mountain's tombs. A Dwarf who robs their own
  ancestors and is hailed for the gold.
- **Guardian, Soldier.** The tercio's rank and file.
- **Artisan, Merchant (official).** The Dwarf's most natural officials are one
  sentence each.

---

## 8. Decisions log

**Decided (Julio)**

- Iberia and al-Andalus are two keys, never fused (the law).
- Saints are Dwarven and stay out of the Celestials' table.
- The species entry speaks as "we" (`a1221a1`).
- Rule voice for the four traits (QST-0094).

**Awaiting Julio (QST-0094)**

- The four inspiration lines proposed there (§9).
- Whether Darkvision prints or is chip-only; Julio decided *print, with a
  line* for the Aasimar, which settles the convention if applied here.

**Open (this page proposes)**

- The Zealot's god for a Dwarf is a Saint; the draw should be species-keyed.
- The old wiki's Dwarf paragraph is the lore's source and is repetitive; this
  page should replace it as the reference, and the wiki's public text should
  be cut to the entry plus one paragraph.
- Materials: Toledo steel by the `iberia` key is in place; the Dwarf Wizard's
  steel-leaf spellbook should draw it.

---

## 9. Lines

*QST-0094's four proposals, in the taught-or-gifted register the Species traits
use, awaiting Julio. Kept here so the page is the reference.*

| Entry | Proposed line (QST-0094) |
|---|---|
| **Darkvision** | *The mines taught our eyes to work where the lamps do not reach.* |
| **Dwarven Resilience** | *Every dwarf grows up tasting the mine air and the smelter's fumes. What did not kill our ancestors does not poison us.* |
| **Dwarven Toughness** | *A dwarf is built like a ledger: every year adds a line, and none is ever struck out.* |
| **Stonecunning** | *Lay a hand on the stone and listen. The mountain still keeps our accounts.* |

The Toughness line is the best of the four and the species' voice exactly: the
ledger as a body.

---

## 10. Pointers

- **Paladin page**: Roncevaux, the Cid, Quixote.
- **Fighter page**: the alférez and the tercio.
- **Sorcerer page**: the ninety-year gem.
- **Druid page**: the Basajaun, Mari, the mountain's creditor.
- **Artificer page**: Juanelo and Abbas ibn Firnas.
- **Gnome page**: the Renaissance pair, one trade route.
- **Celestials page**: Saints and Celestials, two systems that look like one.
