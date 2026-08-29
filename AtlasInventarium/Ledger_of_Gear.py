"""
Ledger_of_Gear — tools, adventuring gear, and the seven equipment packs.

Built with ``Build_Item``; tools carry the governing ability as a plain
attribute (``item.ability``) so a Kit can look up which score a check uses
without a second lookup table.

Data source: the 2024 equipment tables (dnd2024.wikidot.com/equipment:tool
and :adventuring-gear), transcribed 2026-07-31. Prices and weights are game
FACTS and are reproduced as such; every description here is our own wording.

Costs are held in gold: 1 SP = 0.1 GP, 1 CP = 0.01 GP.
"""

from __future__ import annotations

from AtlasInventarium.Grimoire_of_Items import Build_Item, Item


# ---------------------------------------------------------------------------
# Artisan's Tools — prices genuinely vary by trade (Weaver's 1 GP, Tinker's 50)
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Adventuring Gear
# ---------------------------------------------------------------------------

def _gear(
		name: str,
		value: float,
		weight: float,
		description: str = "",
		) -> Item:
	return Build_Item(
			name=name,
			value=value,
			weight=weight,
			description=description,
			)


Backpack = _gear("Backpack", 2, 5, "Holds a cubic foot or 30 pounds of gear.")
Ball_Bearings = _gear("Ball Bearings", 1, 2, "Spilled across the ground to send pursuers sprawling.")
Bedroll = _gear("Bedroll", 1, 7)
Bell = _gear("Bell", 1, 0)
Blanket = _gear("Blanket", 0.5, 3)
Book = _gear("Book", 25, 5)
Bullseye_Lantern = _gear("Bullseye Lantern", 10, 2, "Casts a cone of bright light.")
Caltrops = _gear("Caltrops", 1, 2, "A bag of spikes strewn to slow a charge.")
Candle = _gear("Candle", 0.01, 0)
Case_Map_or_Scroll = _gear("Map or Scroll Case", 1, 1)
Chest = _gear("Chest", 5, 25)
Clothes_Fine = _gear("Fine Clothes", 15, 6)
Costume = _gear("Costume", 5, 4)
Crowbar = _gear("Crowbar", 2, 5, "Grants Advantage on Strength checks where leverage helps.")
Holy_Water = _gear("Holy Water", 25, 1, "A flask of blessed water, thrown as an improvised weapon.")
Hooded_Lantern = _gear("Hooded Lantern", 5, 2, "Its shutter dims the light without dousing it.")
Ink = _gear("Ink", 10, 0, "A one-ounce bottle.")
Ink_Pen = _gear("Ink Pen", 0.02, 0)
Lamp = _gear("Lamp", 0.5, 1, "Burns oil, shedding light in a 15-foot radius.")
Mirror = _gear("Mirror", 5, 0.5, "A polished steel hand mirror.")
Oil = _gear("Oil", 0.1, 1, "A flask of oil — fuel for a lamp, or thrown and lit.")
Paper = _gear("Paper", 0.2, 0, "One sheet.")
Parchment = _gear("Parchment", 0.1, 0, "One sheet.")
Perfume = _gear("Perfume", 5, 0)
Rations = _gear("Rations", 0.5, 2, "Dry food sufficient for one day.")
Robe = _gear("Robe", 1, 4)
Rope = _gear("Rope", 1, 5, "Fifty feet of it.")
Tinderbox = _gear("Tinderbox", 0.5, 1, "Flint, fire steel, and tinder for striking a spark.")
Torch = _gear("Torch", 0.01, 1, "Burns for 1 hour, shedding bright light in a 20-foot radius.")
Waterskin = _gear("Waterskin", 0.2, 5, "Holds 4 pints; the weight given is when full.")

ADVENTURING_GEAR: tuple[Item, ...] = (
		Backpack, Ball_Bearings, Bedroll, Bell, Blanket, Book, Bullseye_Lantern,
		Caltrops, Candle, Case_Map_or_Scroll, Chest, Clothes_Fine, Costume,
		Crowbar, Holy_Water, Hooded_Lantern, Ink, Ink_Pen, Lamp, Mirror, Oil,
		Paper, Parchment, Perfume, Rations, Robe, Rope, Tinderbox, Torch,
		Waterskin,
		)

ADVENTURING_GEAR_BY_NAME: dict[str, Item] = {
		item.name: item
		for item in ADVENTURING_GEAR
		}


# ---------------------------------------------------------------------------
# Valuables — wealth a hero wears instead of hauling
# ---------------------------------------------------------------------------
#
# Julio (2026-08-05): "for jewels it should be multi, instead of carrying a
# lot of money." Coin is heavy, conspicuous and easy to lose; anyone with
# means converts the surplus into something they can wear, and the Jewelry
# slot already holds three. These grant NOTHING — their whole worth is their
# resale value, which is exactly the point.
#
# Prices follow the 2024 gemstone and art-object bands (10 / 25 / 50 / 100 /
# 250 / 750 gp), so selling one back is never a surprise.

def _jewel(
		name: str,
		value: float,
		description: str = "",
		) -> Item:
	from AtlasInventarium.ItemKit import Build_Worn, Jewelry
	return Build_Worn(
			name=name,
			slot=Jewelry,
			value=value,
			weight=0,
			description=description,
			)


Copper_Band = _jewel(
		"Copper Band",
		10,
		"A twist of {material}, worn smooth. Worth a night's lodging.",
		)
Amber_Pendant = _jewel(
		"Amber Pendant",
		25,
		"A drop of {material} on a cord, with something small caught inside.",
		)
Signet_Ring = _jewel(
		"Signet Ring",
		50,
		"A {material} ring cut with a mark. It opens doors coin cannot.",
		)
Jade_Torc = _jewel(
		"Jade Torc",
		100,
		"A heavy collar of {material}. Wealth worn where everyone can see it.",
		)
Pearl_Chain = _jewel(
		"Pearl Chain",
		250,
		"Matched pearls on {material}. A merchant's fortune, worn at the throat.",
		)
Ruby_Circlet = _jewel(
		"Ruby Circlet",
		750,
		"A band of {material} set with a stone the colour of a slow fire.",
		)

VALUABLES: tuple[Item, ...] = (
		Copper_Band, Amber_Pendant, Signet_Ring,
		Jade_Torc, Pearl_Chain, Ruby_Circlet,
		)

VALUABLES_BY_NAME: dict[str, Item] = {
		item.name: item
		for item in VALUABLES
		}


# ---------------------------------------------------------------------------
# Packs — contents and prices as printed; weights are summed from the parts
# ---------------------------------------------------------------------------

_PACK_CONTENTS: dict[str, tuple[tuple[str, int], ...]] = {
		"Burglar's Pack": (
				("Backpack", 1), ("Ball Bearings", 1), ("Bell", 1),
				("Candle", 10), ("Crowbar", 1), ("Hooded Lantern", 1),
				("Oil", 7), ("Rations", 5), ("Rope", 1), ("Tinderbox", 1),
				("Waterskin", 1),
				),
		"Diplomat's Pack": (
				("Chest", 1), ("Fine Clothes", 1), ("Ink", 1), ("Ink Pen", 5),
				("Lamp", 1), ("Map or Scroll Case", 2), ("Oil", 4),
				("Paper", 5), ("Parchment", 5), ("Perfume", 1),
				("Tinderbox", 1),
				),
		"Dungeoneer's Pack": (
				("Backpack", 1), ("Caltrops", 1), ("Crowbar", 1), ("Oil", 2),
				("Rations", 10), ("Rope", 1), ("Tinderbox", 1), ("Torch", 10),
				("Waterskin", 1),
				),
		"Entertainer's Pack": (
				("Backpack", 1), ("Bedroll", 1), ("Bell", 1),
				("Bullseye Lantern", 1), ("Costume", 3), ("Mirror", 1),
				("Oil", 8), ("Rations", 9), ("Tinderbox", 1), ("Waterskin", 1),
				),
		"Explorer's Pack": (
				("Backpack", 1), ("Bedroll", 1), ("Oil", 2), ("Rations", 10),
				("Rope", 1), ("Tinderbox", 1), ("Torch", 10), ("Waterskin", 1),
				),
		"Priest's Pack": (
				("Backpack", 1), ("Blanket", 1), ("Holy Water", 1), ("Lamp", 1),
				("Rations", 7), ("Robe", 1), ("Tinderbox", 1),
				),
		"Scholar's Pack": (
				("Backpack", 1), ("Book", 1), ("Ink", 1), ("Ink Pen", 1),
				("Lamp", 1), ("Oil", 10), ("Parchment", 10), ("Tinderbox", 1),
				),
		}

_PACK_PRICES: dict[str, float] = {
		"Burglar's Pack": 16,
		"Diplomat's Pack": 39,
		"Dungeoneer's Pack": 12,
		"Entertainer's Pack": 40,
		"Explorer's Pack": 10,
		"Priest's Pack": 33,
		"Scholar's Pack": 40,
		}


def Build_Pack(
		name: str,
		contents: tuple[tuple[str, int], ...],
		value: float,
		) -> Item:
	"""
	Craft a pack as one purchasable Item that remembers what is inside it.

	``item.contents`` is ``((item_name, quantity), …)`` — a loadout policy
	resolves the names against ``ADVENTURING_GEAR_BY_NAME`` when it opens the
	pack into the bag.
	"""
	weight = sum(
			ADVENTURING_GEAR_BY_NAME[item_name].weight * quantity
			for item_name, quantity in contents
			)
	pack = Build_Item(
			name=name,
			value=value,
			weight=weight,
			description="A pack of standard adventuring gear.",
			)
	pack.contents = contents
	return pack


PACKS: tuple[Item, ...] = tuple(
		Build_Pack(
				name,
				_PACK_CONTENTS[name],
				_PACK_PRICES[name],
				)
		for name in sorted(
				_PACK_CONTENTS
				)
		)

PACKS_BY_NAME: dict[str, Item] = {
		pack.name: pack
		for pack in PACKS
		}

Explorers_Pack = PACKS_BY_NAME["Explorer's Pack"]


__all__ = (
		"ADVENTURING_GEAR",
		"ADVENTURING_GEAR_BY_NAME",
		"Build_Pack",
		"Explorers_Pack",
		"PACKS",
		"PACKS_BY_NAME",
		"VALUABLES",
		"VALUABLES_BY_NAME",
		)


def _self_test():
	gear_names = [item.name for item in ADVENTURING_GEAR]
	assert len(gear_names) == len(set(gear_names))

	assert len(PACKS) == 7, f"expected all seven packs, got {len(PACKS)}"

	for pack in PACKS:
		assert pack.contents, f"{pack.name} is empty"
		for item_name, quantity in pack.contents:
			assert item_name in ADVENTURING_GEAR_BY_NAME, (
					f"{pack.name} references unknown item {item_name!r}"
					)
			assert quantity > 0
		# A pack must never cost MORE than buying its parts loose.
		loose = sum(
				ADVENTURING_GEAR_BY_NAME[item_name].value * quantity
				for item_name, quantity in pack.contents
				)
		assert pack.value <= loose + 1e-6, (
				f"{pack.name} costs {pack.value} but its parts total {loose}"
				)

	# Valuables are wealth, not power: they must grant nothing at all, or
	# "carry your money as jewels" would quietly become a stat boost.
	from AtlasInventarium.ItemKit import Jewelry, Wearable

	values = [jewel.value for jewel in VALUABLES]
	assert values == sorted(
			values
			), "valuables must read cheapest-first, so a purse can be spent down"
	for jewel in VALUABLES:
		assert jewel in Jewelry and jewel in Wearable, jewel.name
		assert not jewel.grants, (
				f"{jewel.name} grants {jewel.grants} — valuables are wealth, "
				f"not equipment"
				)
		assert jewel.weight == 0, f"{jewel.name} should be lighter than coin"

	print(
			f"OK — Ledger_of_Gear self-test "
			f"({len(ADVENTURING_GEAR)} gear items, {len(PACKS)} packs, "
			f"{len(VALUABLES)} valuables)"
			)


if __name__ == "__main__":
	_self_test()
