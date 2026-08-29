"""
Map_of_Materials — what a hero's gear is MADE of, drawn from their Tags.

Julio's idea (2026-08-01): a Cleric of the Tomb should carry something of
giant bone; a wood elf, something of oak. The stock line "a wooden or metal
shield" is true of every shield ever made and therefore says nothing about
this one.

Shape follows ``AtlasEpica/Map_of_Titles``: vocabulary accumulated by reading
the Character's ``genus`` (its comma-joined Tag string — species, guild,
background, subclass, …), then one pick. Unlike that Map, this one takes an
explicit stream rather than seeding the global RNG, per
``Canon/Modus-Operandi`` ("Explicit randomness. Character-owned named
streams; no hidden global state.").

A material is FLAVOUR ONLY. It never changes a price, a weight, or a grant —
so no balance decision is hiding inside a describing word.
"""

from __future__ import annotations

import random


# Each entry: the Tag words that summon it, and the materials they suggest.
# Order matters only in that every match contributes; the pick is uniform
# across everything summoned.
_THEMES: tuple[tuple[tuple[str, ...], tuple[str, ...]], ...] = (
		(
				(
						"Elf",
						"Druid",
						"Ranger",
						"Wildkeeper",
						"Forest",
						"Wood",
						"Fey",
						),
				(
						"oak",
						"yew",
						"living heartwood",
						"green-bound ash",
						),
				),
		(
				(
						"Dwarf",
						"Mason",
						"Mountain",
						"Smith",
						),
				(
						"deep iron",
						"granite-inlaid steel",
						"hammered bronze",
						),
				),
		(
				(
						"Undead",
						"Vampire",
						"Tomb",
						"Grave",
						"Haunted",
						"Death",
						"Necro",
						),
				(
						"grave-iron",
						"barrow bone",
						"tomb silver",
						"coffin oak",
						),
				),
		(
				(
						"Giant",
						"Goliath",
						"Ogre",
						"Titan",
						),
				(
						"giant bone",
						"boulder hide",
						"mammoth ivory",
						),
				),
		(
				(
						"Dragon",
						"Dragonborn",
						"Drake",
						),
				(
						"dragonbone",
						"drake scale",
						"wyrm-lacquered steel",
						),
				),
		(
				(
						"Fiend",
						"Tiefling",
						"Warlock",
						"Infernal",
						"Abyssal",
						"Cultist",
						),
				(
						"black iron",
						"brimstone brass",
						"pact-scored steel",
						),
				),
		(
				(
						"Celestial",
						"Aasimar",
						"Cleric",
						"Paladin",
						"Acolyte",
						"Priest",
						),
				(
						"silvered steel",
						"dawn bronze",
						"psalm-etched iron",
						),
				),
		(
				(
						"Orc",
						"Barbarian",
						"Berserker",
						"Bandit",
						),
				(
						"hide-bound iron",
						"scarred oak",
						"rough-forged steel",
						),
				),
		(
				(
						"Sailor",
						"Pirate",
						"Mariner",
						"Islander",
						"Sea",
						),
				(
						"salt-bleached ash",
						"whalebone",
						"tar-black oak",
						),
				),
		(
				(
						"Ice",
						"Frost",
						"Winter",
						"Northerner",
						"Nomad",
						),
				(
						"walrus ivory",
						"frost-hardened pine",
						"antler and hide",
						),
				),
		(
				(
						"Wizard",
						"Sorcerer",
						"Scholar",
						"Sage",
						"Mage",
						"Arcane",
						),
				(
						"rune-cut walnut",
						"star-iron",
						"glass-veined ash",
						),
				),
		)

# When a Character's Tags suggest nothing in particular.
_PLAIN: tuple[str, ...] = (
		"wood",
		"iron",
		"steel",
		"bronze",
		"boiled leather",
		)


# ---------------------------------------------------------------------------
# What a people works in — the third arm of the species/society/gear mapping
# ---------------------------------------------------------------------------
#
# Julio (2026-08-05): "it would be cool to add 'materials', like 'obsidian
# sword' or 'silver katana' that also speak to the culture: Dwarves may focus
# more on metals, and gnomes on jewels."
#
# Keyed by the SAME atomic society names as ``Map_of_Gear_Titles._CULTURES``,
# so the species → society mapping is written once and both the name and the
# substance of a thing follow from it. Fixing a species' society fixes both.
#
# Every entry must read sensibly on a blade, a haft AND a coat, because the
# placeholder does not know what it is filling. Gems therefore appear as
# settings ("emerald-set steel"), never as a whole object.
_CULTURAL_MATERIALS: dict[str, tuple[str, ...]] = {
		"japan": (
				"folded steel",
				"lacquered silver",
				"black-lacquered wood",
				),
		"aztec": (
				"obsidian",
				"volcanic glass",
				"feather-bound wood",
				),
		"china": (
				"jade-set bronze",
				"nine-fold steel",
				"cinnabar-lacquered wood",
				),
		"korea": (
				"celadon-glazed steel",
				"ox-horn and sinew",
				"pine-tar iron",
				),
		"india": (
				"wootz steel",
				"watered damask steel",
				"sandalwood and brass",
				),
		"oceania": (
				"greenstone",
				"shark-tooth and koa wood",
				"coral-inlaid bone",
				),
		"persia": (
				"crucible steel",
				"turquoise-set silver",
				"cedar and gold leaf",
				),
		"levante": (
				"cedar and bronze",
				"lapis-set copper",
				"date-palm and iron",
				),
		"egypt": (
				"gilded bronze",
				"carnelian-set gold",
				"acacia and electrum",
				),
		"africa": (
				"bloomery iron",
				"ebony and brass",
				"cowrie-set ironwood",
				),
		"maghreb": (
				"nickel-silver",
				"cedar and camel bone",
				"coral-set brass",
				),
		"carthage": (
				"Tyrian-dyed bronze",
				"esparto and iron",
				"ivory-inlaid bronze",
				),
		"norse": (
				"pattern-welded steel",
				"ash and walrus ivory",
				"bog iron",
				),
		"rus": (
				"amber-set iron",
				"birch and bronze",
				"river-forged steel",
				),
		"mongol": (
				"horn and sinew",
				"felt-bound iron",
				"steppe-hardened bronze",
				),
		"celt": (
				"spiral-chased bronze",
				"blackthorn and iron",
				"enamelled copper",
				),
		"iberia": (
				"Toledo steel",
				"olive wood and steel",
				"damascened gold on steel",
				),
		"andalus": (
				"damascened silver",
				"ivory-inlaid steel",
				"filigreed brass",
				),
		"italy": (
				"Milanese steel",
				"gilt-etched steel",
				"walnut and mother-of-pearl",
				),
		"germany": (
				"Solingen steel",
				"blued steel",
				"boxwood and blackened iron",
				),
		"switzerland": (
				"garnet-set steel",
				"rock-crystal and silver",
				"alpine pine and brass",
				),
		"rome": (
				"Noric steel",
				"tinned bronze",
				"legion-stamped iron",
				),
		"greece": (
				"hoplite bronze",
				"olive wood and bronze",
				"marble-inlaid iron",
				),
		"ninja": (
				"soot-blacked steel",
				"unpolished iron",
				"charcoal-dyed wood",
				),
		# --- legends work in substances history never had -------------------
		# Julio (2026-08-05): the fantasy-canon markers exist "for items like
		# Mithril and such". Keyed by the same marker names as the legend half
		# of ``Map_of_Gear_Titles._CULTURES``, so one species row drives the
		# name AND the substance.
		#
		# These stay FLAVOUR, exactly like the rest of this file: mithril
		# costs nothing and grants nothing. The moment a material should be
		# lighter or stronger it stops being a describing word and belongs in
		# the Ledger as its own item.
		"tolkien_elves": (
				"mithril",
				"star-silver",
				"moonlit ithildin",
				),
		"tolkien_dwarves": (
				"mithril",
				"deep-delved iron",
				"rune-graven steel",
				),
		"folklore_dwarf": (
				"knocker's tin",
				"hearth-forged iron",
				"mountain copper",
				),
		"fairytale_fae": (
				"cold iron",
				"blackthorn and dew",
				"glass and briar",
				),
		"eragon_dragons": (
				"brightsteel",
				"scale-set steel",
				"rider's blue steel",
				),
		"wyrm_myth": (
				"dragonbone",
				"hoard-gold",
				"serpent-scale steel",
				),
		"arabian_nights": (
				"brass and bound smoke",
				"moon-silver",
				"lamp-black bronze",
				),
		"arthuriana": (
				"lake-tempered steel",
				"chapel silver",
				"blazoned white steel",
				),
		"sword_and_sorcery": (
				"black meteor iron",
				"beast-hide and bronze",
				"unquenched steel",
				),
		"grimdark": (
				"pitted iron",
				"reliquary-bone and steel",
				"rust-scored steel",
				),
		"clockpunk": (
				"clockwork brass",
				"spring steel",
				"geared bronze",
				),
		"anime": (
				"impossible steel",
				"folded thousand-layer steel",
				"black-lacquered alloy",
				),
		}

# What a people cannot stop reaching for. This is the "Dwarves focus on metals,
# Gnomes on jewels" lean: extra copies of the matching materials, so the bias
# shows without ever closing the door on the rest.
_LEAN: tuple[tuple[tuple[str, ...], tuple[str, ...], int], ...] = (
		(
				(
						"Dwarf",
						"Mason",
						"Smith",
						),
				(
						"iron",
						"steel",
						"bronze",
						"brass",
						"copper",
						"electrum",
						),
				2,
				),
		(
				(
						"Gnome",
						),
				(
						"garnet",
						"crystal",
						"amber",
						"jade",
						"lapis",
						"turquoise",
						"carnelian",
						"emerald",
						"pearl",
						"gilt",
						"gold",
						"silver",
						),
				2,
				),
		)

_CULTURAL_WEIGHT = 2


def _genus_of(
		target,
		) -> str:
	"""The Tag string to read, whether given a Character or a plain string."""
	genus = getattr(
			target,
			"genus",
			None,
			)
	if genus is None:
		return str(
				target
				)
	return str(
			genus
			)


def materials_for(
		target,
		) -> tuple[str, ...]:
	"""Every material this Character's Tags suggest, best-themed first."""
	genus = _genus_of(
			target
			).lower()

	found: list[str] = []
	for words, materials in _THEMES:
		if any(
				word.lower() in genus
				for word in words
				):
			for material_name in materials:
				if material_name not in found:
					found.append(
							material_name
							)

	return tuple(
			found
			) or _PLAIN


def cultural_materials(
		target,
		) -> tuple[str, ...]:
	"""
	What this Character's peoples work in — a WEIGHTED list.

	Reads the society mapping in ``Map_of_Gear_Titles`` rather than keeping a
	second copy of it, so a species whose societies are corrected here is
	corrected everywhere at once. A material repeats once per point of reach,
	so a Dragonborn is usually obsidian or folded steel and only occasionally
	reaches a neighbour's wootz.
	"""
	try:
		from AtlasInventarium.Map_of_Gear_Titles import influences_of
	except Exception:
		return ()

	weighted: list[str] = []
	for culture, weight in influences_of(
			target
			).items():
		for material_name in _CULTURAL_MATERIALS.get(
				culture,
				(),
				):
			weighted.extend(
					[
							material_name,
							] * weight
					)
	return tuple(
			weighted
			)


def _leaned(
		target,
		pool: list[str],
		) -> list[str]:
	"""Extra copies of whatever this people cannot stop working in."""
	genus = _genus_of(
			target
			).lower()
	leaned = list(
			pool
			)
	for words, substances, extra in _LEAN:
		if not any(
				word.lower() in genus
				for word in words
				):
			continue
		for entry in pool:
			if any(
					substance in entry.lower()
					for substance in substances
					):
				leaned.extend(
						[
								entry,
								] * extra
						)
	return leaned


def material(
		target,
		rng: random.Random | None = None,
		) -> str:
	"""
	One material suiting this Character.

	Three voices, all weighting one pool rather than overriding each other:
	the hero's own Tags, the societies they belong to, and their people's
	lean (Dwarves toward metals, Gnomes toward jewels).

	``rng`` should be a Character-owned stream so the same hero always carries
	the same oak. Falls back to a stream seeded from the Character, never to
	the global RNG.
	"""
	choices = _leaned(
			target,
			list(
					materials_for(
							target
							)
					) * _CULTURAL_WEIGHT + list(
					cultural_materials(
							target
							)
					),
			)

	if rng is None:
		seed = getattr(
				target,
				"seed",
				None,
				)
		if seed is None:
			seed = _genus_of(
					target
					)
		rng = random.Random(
				f"{seed}:material"
				)

	return rng.choice(
			choices
			)


def personalise(
		item,
		target,
		rng: random.Random | None = None,
		) -> object:
	"""
	Fill an item's ``{material}`` placeholder for this Character.

	Ledger descriptions carry the placeholder so the catalogue stays generic;
	only the copy handed to a hero learns what it is made of.
	"""
	description = getattr(
			item,
			"description",
			"",
			) or ""
	if "{material}" not in description:
		return item

	item.description = description.replace(
			"{material}",
			material(
					target,
					rng,
					),
			)
	return item


__all__ = (
		"cultural_materials",
		"material",
		"materials_for",
		"personalise",
		)


def _self_test():
	class Dummy:
		def __init__(
				self,
				genus,
				seed=1,
				):
			self.genus = genus
			self.seed = seed

	# --- Tags steer the vocabulary ---------------------------------------
	elf = Dummy(
			"Elf , Druid , Farmer , Moon , She , True Chaotic"
			)
	assert "oak" in materials_for(
			elf
			), materials_for(
			elf
			)

	tomb_cleric = Dummy(
			"Human , Cleric , Mulhorandi Tomb Raider , Light , He , True Legal"
			)
	suggested = materials_for(
			tomb_cleric
			)
	assert "grave-iron" in suggested or "tomb silver" in suggested, suggested
	# A Cleric also draws on the celestial theme — both axes contribute.
	assert "silvered steel" in suggested, suggested

	giant = Dummy(
			"Goliath , Barbarian , Guide , World Tree , They , True Neutral"
			)
	assert "giant bone" in materials_for(
			giant
			)

	# --- an untagged target still gets something ordinary ----------------
	nobody = Dummy(
			"Human , Commoner , He , True Neutral"
			)
	assert materials_for(
			nobody
			) == _PLAIN

	# --- deterministic per Character -------------------------------------
	assert material(
			elf
			) == material(
			elf
			), "same hero must always carry the same material"

	# --- the society mapping reaches the substance too ---------------------
	# Julio's own examples: an obsidian sword, a silver katana.
	dragonborn = Dummy(
			"Dragonborn , Fighter , Soldier , Champion , He , True Neutral"
			)
	draconic = set(
			cultural_materials(
					dragonborn
					)
			)
	assert "obsidian" in draconic, sorted(
			draconic
			)
	assert "lacquered silver" in draconic, sorted(
			draconic
			)
	# Reach, not a wall: a neighbour's word is available, just rarer.
	assert draconic & {
			"jade-set bronze",
			"nine-fold steel",
			}, sorted(
			draconic
			)

	def share(
			who,
			words,
			rolls=200,
			):
		picks = [
				material(
						who,
						random.Random(
								i
								),
						)
				for i in range(
						rolls,
						)
				]
		return sum(
				1
				for pick in picks
				if any(
						word in pick.lower()
						for word in words
						)
				) / len(
				picks
				)

	# --- each people leans toward its own craft ----------------------------
	dwarf = Dummy(
			"Dwarf , Fighter , Smith , Champion , She , True Legal"
			)
	gnome = Dummy(
			"Gnome , Wizard , Sage , Evocation , He , True Neutral"
			)
	metals = (
			"iron",
			"steel",
			"bronze",
			"brass",
			"copper",
			"electrum",
			)
	jewels = (
			"garnet",
			"crystal",
			"amber",
			"jade",
			"lapis",
			"turquoise",
			"carnelian",
			"pearl",
			"gilt",
			"gold",
			"silver",
			)
	dwarf_metal = share(
			dwarf,
			metals,
			)
	gnome_jewel = share(
			gnome,
			jewels,
			)
	assert dwarf_metal > 0.6, f"Dwarves work metal: {dwarf_metal:.0%}"
	assert gnome_jewel > 0.2, f"Gnomes work jewels: {gnome_jewel:.0%}"
	assert gnome_jewel > share(
			dwarf,
			jewels,
			), "the jewel lean must be a Gnome's, not everyone's"

	# --- legends supply substances history never had ----------------------
	elf_stuff = set(
			cultural_materials(
					Dummy(
							"Elf , Ranger , Guide , Hunter , They , True Neutral"
							)
					)
			)
	assert "mithril" in elf_stuff, sorted(
			elf_stuff
			)
	assert "pattern-welded steel" in elf_stuff, (
			"the real people must still speak beside the legend"
			)
	assert "mithril" in set(
			cultural_materials(
					dwarf
					)
			), "Dwarves delve mithril too"

	# Every marker the title map can hand us must have materials, or a hero
	# reaches for a substance that does not exist.
	from AtlasInventarium.Map_of_Gear_Titles import _CULTURES

	for row in _CULTURES:
		for marker in row[1] + row[2]:
			assert marker in _CULTURAL_MATERIALS, (
					f"{marker} names gear but nothing to make it from"
					)

	# --- placeholder filling ----------------------------------------------
	class FakeItem:
		description = "A {material} shield strapped to one arm."

	shield = FakeItem()
	personalise(
			shield,
			elf,
			)
	assert "{material}" not in shield.description
	assert shield.description.startswith(
			"A "
			) and shield.description.endswith(
			"strapped to one arm."
			), shield.description

	# an item with no placeholder is left exactly as it was
	class Plain:
		description = "A plain thing."

	plain = Plain()
	personalise(
			plain,
			elf,
			)
	assert plain.description == "A plain thing."

	print(
			f"OK — Map_of_Materials self-test "
			f"({len(_THEMES)} Tag themes + {len(_CULTURAL_MATERIALS)} peoples "
			f"and legends; "
			f"deterministic, flavour-only)"
			)


if __name__ == "__main__":
	_self_test()
