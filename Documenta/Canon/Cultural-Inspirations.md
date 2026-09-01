# 🌍 Cultural Inspirations — the peoples and their sources

*Julio's setting brief, recorded 2026-08-03. This is intent, not implementation:
`AtlasInventarium/Map_of_Gear_Titles` is one consumer of it, and later work
(names, architecture, cuisine, story) should read from the same directions.*

---

## The law

**One culture key = one culture.** Never fuse two inspirations into a single
marker (`japonic_aztec`, `norse_steppe_celtic`, and the like are wrong).

A **species** may draw from many cultures. That is recorded as a *list of
separate keys*, not as a blended label. Overlap between peoples is modelled by
the influence network (`_INFLUENCES`), not by merging vocabulary pools.

Fiction registers (`wyrm_myth`, `grimdark`, `arthuriana`, …) are also separate
keys; they are not real-world cultures, and they do not merge real-world ones.

---

## The aim

Every people is a **real human culture cranked to romantic excess** — the
fantasy is the over-the-top version of a recognisable base, plus extra.

- Spain sought gold in America → **gold-fevered Dwarves**.
- Isolationist and imperial at once → **Dragonborn**, drawing on Japan **and**
  the Mexica as two distinct wells.
- Mysterious and exotic → **Fae**, orientalism multiplied by a thousand.

The point of anchoring on real cultures is that **every character comes from
somewhere a reader can understand**. It may be turned up loud, but it is
legible, and it deliberately avoids the default of fantasy where "the world is
Britain with magic Irish and barbarian Scots".

## The peoples

Each row lists **separate** culture keys the species may hold. Plus any fiction
register is listed on its own line of thought, not fused into a real-world key.

| People | Culture keys (each distinct) | Character |
|---|---|---|
| **Dragonborn** | `japan`, `aztec` (+ `eragon_dragons`, `wyrm_myth`) | Isolated from the rest, yet imperialist |
| **Kobold** | `japan`, `china`, `korea` (+ `wyrm_myth`) | A step to one side of the Dragonborn |
| **Fae** | `china` (+ `fairytale_fae`); India reached via influences | Mysterious and exotic; orientalism ×1000 |
| **Goblin** | `persia`, `levante` (+ `fairytale_fae`, `grimdark`) | Marginalised; no single real parallel claimed as identity |
| **Human** | `africa`, `egypt`, `maghreb`, `carthage` (+ `arthuriana`) | The baseline everyone else is measured from |
| **Elf** | `norse`, `rus`, `mongol`, `celt` (+ `tolkien_elves`, `fairytale_fae`) | A bit Fae and a bit "other people", in a colder nature |
| **Dwarf** | `iberia`, `andalus` (+ `folklore_dwarf`, `tolkien_dwarves`) | Gold-fevered |
| **Gnome** | `italy`, `germany`, `switzerland` (+ `folklore_dwarf`, `clockpunk`) | Middle point of the Renaissance pair |
| **Aasimar** | `rome` (+ `arthuriana`) | |
| **Giant / Goliath** | `greece` (+ `wyrm_myth`) | |
| **Monk** *(class)* | adds `ninja` (+ `anime`) on top of species cultures | Monks read as ninja across every people |

## Cultures overlap, and that is the point

**No people is sealed off.** The map is a *network of influences*, not a set of
boxes, and a weapon, a word or a custom may belong to several cultures at once.

- Dwarves and Gnomes trade and share settlements.
- Elves and Fae are close partners.
- Goblins live among Humans.
- Iberia is strongly shaped by the Umayyads — still `iberia` and `andalus`, not one key.
- Vikings reached Spain and North Africa — still `norse` influencing `iberia`, not a merge.
- Celts are part of Spain (Galicia) as well as the north — `celt` stays its own key.
- China and India both reach Arabia — separate keys, linked by `_INFLUENCES`.
- **Everyone** inherits Greece and Rome.

India is complex, mysterious and ancient all at once; all cultures are
relatable. Overlap should be modelled, not avoided.

## How this is implemented today

`Map_of_Gear_Titles` holds the first machine-readable version:

- `_CULTURES` — species (and Monk) → a **tuple of distinct culture keys**.
  Dragonborn is `japan` **and** `aztec`; Kobolds are `japan`, `china`, and
  `korea`; a Dragonborn Monk adds `ninja` on top of the species list.
- `_CULTURAL_NOUNS` — vocabulary **per culture key**. Katana lives under
  `japan`; Macuahuitl under `aztec`. No shared fused pool.
- `_INFLUENCES` — weighted neighbours between those same keys. Japan reaches
  China and Korea; Aztec stands as its own pool. A Dwarf's reach can touch
  Maghreb or Carthage without the Dwarf *becoming* those cultures.
- `cultures_of(hero)` / `influences_of(hero)` — assemble the list, then roll
  across the network. A Dragonborn may draw a Katana *or* a Macuahuitl —
  two cultures, one people.

Two rules that keep it legible:

1. **Culture-marked words live only in the culture that says them.** Generic
   pools hold the proper name plus plain English; Katana, Yari, Gladius and
   Targe are reachable only through a people who would use them. (Leaving a
   marked word in the generic pool leaks it to everyone — that is how a Dwarf
   once ended up carrying a Yari.)
2. **Famous names stand alone; unfamiliar ones carry their category** —
   *Katana* and *Shuriken* bare, but *Honda Sling*, *Khopesh Sabre*,
   *Akinakes Blade*. This keeps the weapon legible, and keeps its **Weapon
   Mastery** obviously applicable.

## Open directions

The same mapping should eventually inform names, places, cuisine, architecture,
prayer, and story vocabulary — not just gear. Consumers must keep the **one
key = one culture** law; if a species needs two inspirations, give it two keys.
