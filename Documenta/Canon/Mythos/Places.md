# 🗺 Places: the map that names things, and the story that needs names

> 📖 **In flow.** 1 of 5 chapters are still proposals. 📜 0 · 📚 1 · 📔 3 · 📖 1

*Wiki entry for the design team. `AtlasWorldBuild/AtlasOfMapmaking` is a
standalone world-map generator (height field by wave-function collapse on a
triangular or hexagonal grid, biomes by height, parchment SVG output). It is
not wired into the app. Compiled 2026-09-08 from source; the module does not
import from the repository root today (a bare `AtlasOfMapmaking` import).*

> **In one sentence.** The Stories engine sends every character home to
> *Stormkirk*; the map atlas already knows how to name a town, a mine, a
> shrine and a crossroads by biome, and nobody has introduced them.

---

## 📔 1. What the atlas does

- **Height to biome**: Hell (below -20), Underdark, Sea, Water, Sand, Plains,
  Forest, Mountain, Snow. A geography with a Hell at the bottom of the height
  field is a setting statement made in a constant: the Lower Planes are
  literally lower, which is what the Tieflings canon says they were made to be.
- **Icons per biome**, drawn as Egyptian hieroglyphs, Tibetan letters and
  alchemical signs (𓄶, 𖤘, ⌂, 🜌): the wordless atmosphere layer the Lenses page
  found missing everywhere else.
- **A name per icon**, composed from the Titles vocabulary and the Names
  engine through a stub NPC: *Town of {Namer}*, *Library of {Title of a
  Scholar}*, *Fortress of the {Rank}*, *Castle of {Title}*, *Shrine of
  {Title}*, *Crossroads of {Title}*, *Mines of {Title of a Dwarf}*, *Forge of
  {Title of a Dwarf}*, *Lands of {Title of a Ranger}*, *Beast of {Title of a
  Beast}*, *{Descriptor} Wizardtower*, *{Descriptor} Throne*.

✅ **The Underdark is already keyed**: mines and forges are named for a Dwarf.
That is the one place in the repository where a place name reads a people, and
it is the pattern the rest should follow.

---

## 📔 2. Where the story needs it

The Stories page found the hometowns: *Stormtor, Stormkirk, Raingate, Rainglade,
Rockspring, Rockcross, Rockspire*: Weather plus Anglo suffix, for every people,
while the Names engine gives the same character an Iberian or Berber name. The
kingdoms: *United Nation, Free Court, Hollow Kingdoms*.

The map atlas has the engine for the fix and the Cultural-Inspirations canon
has the keys. **A hometown is a biome and a culture**:

| People | Biome the canon implies | Place shape |
|---|---|---|
| Dwarf | Underdark, Mountain | *Mines of…*, *Forge of…* (built), a Sierra town |
| Elf | Forest (Wood), Plains (High), Underdark (Dark), Snow (Shadow) | the lineage's place: the drift made literal |
| Aasimar | Plains, Mountain | *Shrine of…*, *Sanctum of…* (built) |
| Tiefling | Plains, Sand | an ordinary town: the point is that it is nobody's |
| Dragonborn | Mountain | *Throne of…*, *Fortress of…* (built) |
| Orc | Plains, Sand | *Camp of…*, *Crossroads of…* (built): the wind path stops, never stays |
| Goliath | Mountain, Snow | *Keep*, *Watchtower* (built) |
| Halfling | Plains, Forest | *Mill town of…*, *Rest of…* (built) |
| Gnome | Plains, Forest | *Library of…*, *{Descriptor}tower* (built) |
| Human | anywhere | *Town of…*, *Market of…*, *Crossing* (built) |

Nine of ten rows have a built pattern. The missing piece is the culture key on
the name inside the pattern: *Town of {Namer}* draws the town's name from a
stub NPC with a random race, so *Town of Salvaro* and *Town of Zavron* are
equally likely for an Elf's hometown. Passing the Character (or its culture
key) instead of a fresh stub makes the town speak the character's language.

---

## 📔 3. State

- ⚠️ Not wired into the app; `Helm_of_Mapmaking.main()` writes SVG files to
  disk. No page or route reaches it.
- ⚠️ `Compass_of_Biomes` imports `AtlasNomina.Map_of_Titles` (the second copy
  of the Titles) and a bare `AtlasOfMapmaking` package that does not resolve
  from the repository root, so the module does not import there today.
- ⚠️ Its NPC stub seeds from `map_rng.randint`, not a Character's Dice.
- ✅ The doctrine note in the Epica files is right to keep the two collapses
  apart: this is the grid WFC; the Stories' "wave collapse" is Tag-gated
  seeded choice. Same word, different machines, and the docstrings say so.

---

## 📖 4. Proposals

1. **Hometown from the atlas**: the Stories' `hometown` and `kingdom` tokens
   drawn from the biome patterns, keyed to the Character's culture, through the
   Character's Dice.
2. **The Underdark rule everywhere**: every pattern's inner name drawn from the
   people the biome implies (§2).
3. **The icons as the sheet's atmosphere**: a hieroglyph beside the hometown,
   the way the header chips carry emoji.
4. A DM Companion gateway: the Adventure's Area Tags (Urban, Forest, Dungeon,
   Swamp, Mountain, Desert, Coast, Graveyard) and the atlas's biomes are one
   list spelled twice; the BBEG's Lair could be placed on a generated map.

---

## 📚 5. Pointers

- **Stories-and-Titles §6**: the hometowns that need this.
- **Names**: the culture keys the inner names should use.
- **NPCs-and-Villains §5**: the Adventure's Areas and Lairs.
- **Lenses §10**: atmosphere.
- **Tiefling canon**: the Lower Planes made lower by being called it; the
  height field agrees.
