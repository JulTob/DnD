# 🌍 Cultural Inspirations — the peoples and their sources

*Julio's setting brief, recorded 2026-08-03. This is intent, not implementation:
`AtlasInventarium/Map_of_Gear_Titles` is one consumer of it, and later work
(names, architecture, cuisine, story) should read from the same directions.*

---

## The aim

Every people is a **real human culture cranked to romantic excess** — the
fantasy is the over-the-top version of a recognisable base, plus extra.

- Spain sought gold in America → **gold-fevered Dwarves**.
- Isolationist and imperial at once → **Dragonborn**, Japan crossed with the Mexica.
- Mysterious and exotic → **Fae**, orientalism multiplied by a thousand.

The point of anchoring on real cultures is that **every character comes from
somewhere a reader can understand**. It may be turned up loud, but it is
legible, and it deliberately avoids the default of fantasy where "the world is
Britain with magic Irish and barbarian Scots".

## The peoples

| People | Primary inspiration | Character |
|---|---|---|
| **Dragonborn** | Shinto and Daoist Japan, crossed with Mexica/Aztec (the Coatl) | Isolated from the rest, yet imperialist |
| **Kobold** | Draconic too, so Japan/China — plus **Korea**, between its neighbours and its own thing | A step to one side of the Dragonborn |
| **Fae** | Qing China, Buddhism and Confucianism, tied through to India | Mysterious and exotic; orientalism ×1000 |
| **Goblin** | Ancient Indo-Israeli-Persian, exclusively | Not dangerous, but treated as a pest — a marginalised people, **without an explicit parallel** to any single real one |
| **Human** | Africa — the birthplace, the default continent | The baseline everyone else is measured from |
| **Elf** | Norse, Rus and Mongol (east to west), with Celts for mysterious magic-nature and aesthetic | A bit Fae and a bit "other people", in a colder nature |
| **Dwarf** | Iberian conquistadors, deeply shaped by the Umayyads (Omeya) | Gold-fevered |
| **Gnome** | Italian and German Renaissance, with **Switzerland** between them | The middle point of the two |
| **Aasimar** | The Roman Empire | |
| **Giant / Goliath** | The Greeks | |
| **Monk** *(class, not species)* | A ninja register on top of whatever species gives | Monks read as ninja across every people |

## Cultures overlap, and that is the point

**No people is sealed off.** The map is a *network of influences*, not a set of
boxes, and a weapon, a word or a custom may belong to several cultures at once.

- Dwarves and Gnomes trade and share settlements.
- Elves and Fae are close partners.
- Goblins live among Humans.
- Iberia is strongly shaped by the Umayyads.
- Vikings reached Spain and North Africa.
- Celts are part of Spain (Galicia) as well as the north.
- China and India both reach Arabia.
- **Everyone** inherits Greece and Rome.

India is complex, mysterious and ancient all at once; all cultures are
relatable. Overlap should be modelled, not avoided.

## How this is implemented today

`Map_of_Gear_Titles` holds the first machine-readable version:

- `_CULTURES` — species (and Monk) to a **primary** culture. A people may hold
  more than one: Kobolds are `japonic_aztec` + `korean`; a Dragonborn Monk is
  `japonic_aztec` + `ninja`.
- `_INFLUENCES` — the network above, as weighted neighbours. A Dwarf reaches
  `indo_persian_levantine` and `african` at 2, `norse_steppe_celtic`, `roman`
  and `hellenic` at 1.
- `influences_of(hero)` sums both into a reach map, so the generator **rolls
  across the network** instead of looking up one box. A Dwarf mostly names
  things in Iberian, and sometimes reaches for the Andalusi or Punic word.

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

The same mapping should eventually inform names, places, cuisine, architecture
and story vocabulary — not just gear. Nothing outside `Map_of_Gear_Titles`
reads it yet.
