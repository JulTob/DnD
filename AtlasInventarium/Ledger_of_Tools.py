"""
Ledger_of_Tools — proficiency-driven kits: Artisan's Tools and the rest.

Split out of ``Ledger_of_Gear`` (2026-07-31, Julio's request): a tool is a
different axis from Adventuring Gear or a Pack — it is what a proficiency
LOOKS LIKE, tied to an ability score and (per Julio) to an evocative
``inspiration`` line: not what the kit is, but what a character does with it
at the table.

Data source: the 2024 equipment table (dnd2024.wikidot.com/equipment:tool),
transcribed 2026-07-31. Prices, weights, and governing abilities are game
FACTS and are reproduced as such; every inspiration line is our own wording.
"""

from __future__ import annotations

from AtlasInventarium.ItemKit import Build_Item, Item


def _tool(
		name: str,
		ability: str,
		weight: float,
		value: float,
		inspiration: str = "",
		) -> Item:
	"""
	Craft a tool.

	``inspiration`` is the point of the thing: not what it is, but what a
	character DOES with it at the table. A proficiency that reads
	"Ability: Dexterity" tells a player nothing; one that suggests reading a
	lock's tumblers by feel hands them a scene.
	"""
	item = Build_Item(
			name=name,
			value=value,
			weight=weight,
			description=(
				f"{inspiration} (Ability: {ability}.)"
				if inspiration
				else f"Ability: {ability}."
				),
			)
	item.ability = ability
	item.inspiration = inspiration
	return item


# ---------------------------------------------------------------------------
# Artisan's Tools — prices genuinely vary by trade (Weaver's 1 GP, Tinker's 50)
# ---------------------------------------------------------------------------

Alchemists_Supplies = _tool(
		"Alchemist's Supplies", "Intelligence", 8, 50,
		"You can tell what a residue was before it burned, neutralise a "
		"corrosive spill, and coax a reaction out of ingredients nobody else "
		"would put in the same jar.",
		)
Brewers_Supplies = _tool(
		"Brewer's Supplies", "Intelligence", 9, 20,
		"You can make foul water safe to drink, judge whether a cask has been "
		"tampered with, and buy an evening's goodwill in any taproom.",
		)
Calligraphers_Supplies = _tool(
		"Calligrapher's Supplies", "Dexterity", 5, 10,
		"You can spot a forged signature, match an unfamiliar hand, and set "
		"down a document that looks like it came from a chancery.",
		)
Carpenters_Tools = _tool(
		"Carpenter's Tools", "Strength", 6, 8,
		"You can bar a door so it holds, build a shelter that survives the "
		"night, and see at a glance which beam is about to give.",
		)
Cartographers_Tools = _tool(
		"Cartographer's Tools", "Wisdom", 6, 15,
		"You can draw a route others can follow, estimate a march from the "
		"lie of the land, and tell when a map has been quietly altered.",
		)
Cobblers_Tools = _tool(
		"Cobbler's Tools", "Dexterity", 5, 5,
		"You can keep a company walking, read where a boot's owner has been "
		"from its wear, and hide something small in a heel.",
		)
Cooks_Utensils = _tool(
		"Cook's Utensils", "Wisdom", 8, 1,
		"You can make hard rations worth eating, stretch supplies through a "
		"lean week, and notice when a dish has been meddled with.",
		)
Glassblowers_Tools = _tool(
		"Glassblower's Tools", "Intelligence", 5, 30,
		"You can shape a lens or a vessel, judge a flaw in a pane, and work "
		"out how a glass thing was made and therefore how it breaks.",
		)
Jewelers_Tools = _tool(
		"Jeweler's Tools", "Intelligence", 2, 25,
		"You can price a gem at a glance, spot paste passed off as stone, "
		"and prise a setting apart without ruining what it held.",
		)
Leatherworkers_Tools = _tool(
		"Leatherworker's Tools", "Dexterity", 5, 5,
		"You can repair armour in the field, cut a harness or sheath to fit, "
		"and tell tanned hide from something that was never an animal.",
		)
Masons_Tools = _tool(
		"Mason's Tools", "Strength", 8, 10,
		"You can find the seam in a wall, judge whether stonework will hold "
		"weight, and read the age and hand of an old construction.",
		)
Painters_Supplies = _tool(
		"Painter's Supplies", "Wisdom", 5, 10,
		"You can render a face from memory well enough to be recognised, "
		"copy a heraldry, and see where a picture has been painted over.",
		)
Potters_Tools = _tool(
		"Potter's Tools", "Intelligence", 3, 10,
		"You can date a shard, reconstruct a vessel from its pieces, and "
		"tell which kiln and which region a piece came out of.",
		)
Smiths_Tools = _tool(
		"Smith's Tools", "Strength", 8, 20,
		"You can beat a dent from a breastplate, judge a blade's temper "
		"before you swing it, and work a lock or hinge loose from its frame.",
		)
Tinkers_Tools = _tool(
		"Tinker's Tools", "Dexterity", 10, 50,
		"You can patch what others would throw away, improvise a small "
		"mechanism from scrap, and understand a device by taking it apart.",
		)
Weavers_Tools = _tool(
		"Weaver's Tools", "Dexterity", 5, 1,
		"You can mend and alter clothing, recognise a region or house by its "
		"weave, and turn cloth into rope, sail, or disguise.",
		)
Woodcarvers_Tools = _tool(
		"Woodcarver's Tools", "Dexterity", 5, 1,
		"You can shape an arrow or a splint, carve a likeness or a seal, and "
		"tell worm-eaten timber from sound wood before you trust it.",
		)

ARTISANS_TOOLS: tuple[Item, ...] = (
		Alchemists_Supplies, Brewers_Supplies, Calligraphers_Supplies,
		Carpenters_Tools, Cartographers_Tools, Cobblers_Tools, Cooks_Utensils,
		Glassblowers_Tools, Jewelers_Tools, Leatherworkers_Tools, Masons_Tools,
		Painters_Supplies, Potters_Tools, Smiths_Tools, Tinkers_Tools,
		Weavers_Tools, Woodcarvers_Tools,
		)


# ---------------------------------------------------------------------------
# Other tools, gaming sets, instruments
# ---------------------------------------------------------------------------

Disguise_Kit = _tool(
		"Disguise Kit", "Charisma", 3, 25,
		"You can pass for someone else — a different rank, a different age, "
		"a face the guards have been told to expect — and see through the "
		"same trick worn by another.",
		)
Forgery_Kit = _tool(
		"Forgery Kit", "Dexterity", 5, 15,
		"You can produce a writ, a seal, or a letter of passage convincing "
		"enough to survive a bored official, and spot one that will not.",
		)
Herbalism_Kit = _tool(
		"Herbalism Kit", "Intelligence", 3, 5,
		"You can identify a plant and what it does to a body, treat a fever "
		"or a poisoning on the road, and gather what you need as you travel.",
		)
Navigators_Tools = _tool(
		"Navigator's Tools", "Wisdom", 2, 25,
		"You can hold a course out of sight of land, find your position from "
		"the stars, and know when a guide is leading you astray.",
		)
Poisoners_Kit = _tool(
		"Poisoner's Kit", "Intelligence", 2, 50,
		"You can prepare and apply a dose without harming yourself, "
		"recognise a poisoning by its signs, and name the substance used.",
		)
Thieves_Tools = _tool(
		"Thieves' Tools", "Dexterity", 1, 25,
		"You can read a lock's tumblers by feel, disarm the mechanism a "
		"careful owner added, and leave no sign that either happened.",
		)

# A Gaming Set and a Musical Instrument are categories, not single items.
# These stand in for the category at a representative price; a later pass can
# roll the specific kind (Dice 1 SP … Dragonchess 1 GP; Flute 2 GP … Lute 35 GP).
Gaming_Set = _tool(
		"Gaming Set", "Wisdom", 0, 1,
		"You can read a table for cheats and tells, win a stranger's "
		"confidence over a wager, and know which game opens which door. "
		"(Dice and Playing Cards run 1 SP to 5 SP; Dragonchess and "
		"Three-Dragon Ante, 1 GP.)",
		)

Musical_Instrument = _tool(
		"Musical Instrument", "Charisma", 2, 30,
		"You can hold a room, earn a night's lodging with an hour's playing, "
		"and carry news or a message in a tune that outlives the teller. "
		"(A Flute or Shawm runs 2 GP, a Horn 3, a Drum 6, a Lyre or Viol 30, "
		"a Lute 35.)",
		)

OTHER_TOOLS: tuple[Item, ...] = (
		Disguise_Kit, Forgery_Kit, Herbalism_Kit, Navigators_Tools,
		Poisoners_Kit, Thieves_Tools, Gaming_Set, Musical_Instrument,
		)

TOOLS: tuple[Item, ...] = ARTISANS_TOOLS + OTHER_TOOLS

TOOLS_BY_NAME: dict[str, Item] = {
		tool.name: tool
		for tool in TOOLS
		}


__all__ = (
		"ARTISANS_TOOLS",
		"OTHER_TOOLS",
		"TOOLS",
		"TOOLS_BY_NAME",
		)


def _self_test():
	tool_names = [tool.name for tool in TOOLS]
	assert len(tool_names) == len(set(tool_names)), (
			"duplicate tool names in the ledger"
			)
	assert len(ARTISANS_TOOLS) == 17, len(ARTISANS_TOOLS)

	for tool in TOOLS:
		assert tool.ability, f"{tool.name} has no governing ability"
		assert tool.value > 0, f"{tool.name} is free"
		# A proficiency is only worth printing if it suggests something to DO.
		assert tool.inspiration, (
				f"{tool.name} has no inspiration — say what a character does with it"
				)
		assert len(tool.inspiration) > 40, (
				f"{tool.name}'s inspiration is too thin to be evocative"
				)

	# Artisan's tools genuinely vary in price — a uniform table would mean
	# the data was invented rather than transcribed.
	prices = {tool.value for tool in ARTISANS_TOOLS}
	assert len(prices) > 1, (
			"artisan tool prices are all identical — check the source table"
			)
	assert Weavers_Tools.value == 1 and Tinkers_Tools.value == 50

	print(
			f"OK — Ledger_of_Tools self-test ({len(TOOLS)} tools, evocative and priced)"
			)


if __name__ == "__main__":
	_self_test()
