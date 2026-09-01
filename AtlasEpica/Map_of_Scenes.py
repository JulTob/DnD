"""
Map of Scenes — DM Character Oracle inspiration cards (QST-0037.16).

Kin to Map_of_Stories / Map_of_Titles: collapse flavor from a host. The host is
the **DM Character** — not assumed evil (villain, Quest Master, contested
guardian, …). Area and Lair Lodges grow here. Wave collapse uses
Charts_of_The_Monomyth (If / Choice / render) — same actuators as Stories.
One Generate → one presentation card; always mint scene NPCs with sheet links;
soft party hooks from Tags.
"""

from __future__ import annotations

import random
from urllib.parse import quote

from AtlasEpica.Charts_of_The_Monomyth import Choice
from AtlasEpica.Charts_of_The_Monomyth import If
from AtlasEpica.Charts_of_The_Monomyth import Weighted_Choice
from AtlasEpica.Charts_of_The_Monomyth import render
from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Projections import Resolve_Legacy_Attribute

try:
	from AtlasEpica.Grimoire_of_Adventure import Adventure
	from AtlasEpica.Grimoire_of_Adventure import Area
	from AtlasEpica.Grimoire_of_Adventure import Collapse_Frame
	from AtlasEpica.Grimoire_of_Adventure import Forge_Oracle
	from AtlasEpica.Grimoire_of_Adventure import Lair
except ImportError:
	from Grimoire_of_Adventure import Adventure
	from Grimoire_of_Adventure import Area
	from Grimoire_of_Adventure import Collapse_Frame
	from Grimoire_of_Adventure import Forge_Oracle
	from Grimoire_of_Adventure import Lair


_AREA_SPEC = [
		(("ANY", "Druid", "Ranger", "Treant", "Dryad", "Elf"), "Forest", 12),
		(("ANY", "Criminal", "Thief", "Assassin", "Spy"), "Urban", 10),
		(("ANY", "Criminal", "Smuggler"), "Coast", 6),
		(("ANY", "Cultist", "Cleric", "Priest", "Paladin"), "Dungeon", 8),
		(("ANY", "Cultist", "Cleric"), "Urban", 4),
		(("ANY", "Wizard", "Sorcerer", "Warlock", "Mage", "Scholar"), "Urban", 8),
		(("ANY", "Vampire", "Undead", "Skeleton", "Ghost", "Lich", "Necromancer"), "Graveyard", 12),
		(("ANY", "Vampire", "Undead", "Lich"), "Dungeon", 8),
		(("ANY", "Dragon", "Wyrm"), "Mountain", 12),
		(("Dragon",), "Dungeon", 4),
		(("ANY", "Sailor", "Pirate", "Merfolk"), "Coast", 10),
		(("ANY", "Barbarian", "Giant"), "Mountain", 6),
		(("Barbarian",), "Forest", 4),
		(("ANY", "Fighter", "Knight", "Soldier"), "Urban", 5),
		(("Monk",), "Mountain", 5),
		(("Monk",), "Urban", 4),
		(("ANY", "Swamp", "Lizardfolk", "Bullywug"), "Swamp", 10),
		(("ANY", "Desert", "Yuan-ti"), "Desert", 8),
		("", "Dungeon", 3),
		("", "Urban", 3),
		("", "Forest", 2),
		]

_LAIR_BY_AREA = {
		"Forest": ("Circle", "Tower", "Cave", "Temple"),
		"Urban": ("Manor", "Tower", "Temple", "Port Den", "Castle"),
		"Dungeon": ("Catacomb", "Temple", "Cave", "Tower"),
		"Swamp": ("Circle", "Cave", "Temple"),
		"Mountain": ("Cave", "Castle", "Tower", "Temple"),
		"Desert": ("Temple", "Tower", "Cave", "Manor"),
		"Coast": ("Port Den", "Manor", "Temple", "Cave"),
		"Graveyard": ("Catacomb", "Temple", "Manor", "Tower"),
		}

_LAIR_SPEC = [
		(("ANY", "Druid", "Ranger"), "Circle", 14),
		(("ANY", "Wizard", "Sorcerer", "Warlock", "Mage"), "Tower", 14),
		(("ANY", "Cultist", "Cleric", "Priest"), "Temple", 14),
		(("ANY", "Vampire", "Knight", "Noble", "Fighter"), "Castle", 10),
		(("ANY", "Vampire", "Undead", "Lich"), "Catacomb", 12),
		(("ANY", "Criminal", "Smuggler", "Pirate"), "Port Den", 14),
		(("Dragon",), "Cave", 14),
		(("ANY", "Criminal", "Assassin"), "Manor", 8),
		(("Monk",), "Temple", 8),
		]

_PARTY_HOOKS = [
		(("ANY", "Paladin", "Knight"), "If a Paladin or knight is among you, this moment may call their oath into the light."),
		(("ANY", "Cleric", "Priest"), "If a Cleric is among you, the sacred (or formerly sacred) here may answer them first."),
		(("Monk",), "If a Monk is among you, a remnant of their order's discipline may be recognizable here."),
		(("ANY", "Fighter", "Soldier", "Barbarian"), "If a warrior is among you, a challenge of arms may find them before the others."),
		(("ANY", "Rogue", "Criminal", "Thief"), "If a Criminal or Rogue is among you, this face may have been looking for them specifically."),
		(("ANY", "Wizard", "Sorcerer", "Warlock"), "If an arcane caster is among you, a sigil here may itch behind their eyes."),
		(("ANY", "Druid", "Ranger"), "If a Druid or Ranger is among you, the land itself may prefer to speak through them."),
		(("ANY", "Dragonborn", "Dragon"), "If a Dragonborn is among you, this character may be related to their bloodline — or hunting it."),
		(("Elf",), "If an Elf is among you, an old kinship or grudge may surface in a glance."),
		(("Dwarf",), "If a Dwarf is among you, stonework or craft here may mean more to them than to the rest."),
		]

_PLOT_BEATS = (
		"People bound to {dm_character}'s cause move through the {area} — not yet the end, only pressure.",
		"Something belonging to {dm_character} is being taken, moved, or hidden near the {lair}.",
		"A rumor of {dm_character} draws steel and gossip alike; the {lair} feels closer than it should.",
		"{dm_character} appears — briefly — then leaves a thread the table can refuse to pull.",
		"Followers of {dm_character} ask a toll of silence, coin, or aid on the way toward the {lair}.",
		"Evidence of {dm_character}'s work marks the {area}: a ward, a wound, a warning — or a plea.",
		)

_INCIDENTAL_BEATS = (
		"A traveler's cart blocks the way — mundane goods, and one sealed thing that should not be for sale.",
		"A skill of patience, wit, or nerve is asked for by the place itself — no dice named; the table decides how.",
		"A face tied to {dm_character}'s past waits with a question, not a blade.",
		"Weather, crowd, or stone shifts — the {area} takes a side for a breath.",
		"Someone offers help that may be kindness, bait, or both.",
		)

_SETTING_LINES = {
		"Forest": "Leaves hush the path; the {lair} is a clearing the wood remembers.",
		"Urban": "Streets press close; the {lair} hides behind a polite door.",
		"Dungeon": "Below, the complex opens — corridors like held breath toward the {lair}.",
		"Swamp": "Mist and root; the {lair} sits where dry ground is a rumor.",
		"Mountain": "Wind shears the stone; the {lair} clings where maps go thin.",
		"Desert": "Heat and distance; the {lair} is a dark mouth in the glare.",
		"Coast": "Salt and rope; the {lair} smells of tar and secrets.",
		"Graveyard": "Names in stone; the {lair} keeps company with the quiet.",
		}


def npc_keys(
		npc,
		) -> str:
	"""Titles-style probe string: race, archetype, title, name."""
	bits = []
	for attr in (
			"race",
			"subrace",
			"archetype",
			"title",
			"name",
			):
		value = getattr(
				npc,
				attr,
				None,
				)
		if value:
			bits.append(
					str(
							value
							)
					)
	return " ".join(
			bits
			)


def pick_area(
		keys,
		rng,
		):
	"""Collapse Area from DM Character keys — Stories-style If + weighted Choice."""
	hits = [
			(area, weight)
			for conds, area, weight in _AREA_SPEC
			if conds not in (
					"",
					None,
					)
			and If(
					keys,
					conds,
					)
			]
	if not hits:
		hits = [
				(area, weight)
				for conds, area, weight in _AREA_SPEC
				if conds in (
						"",
						None,
						)
				]
	return Weighted_Choice(
			hits,
			rng=rng,
			)


def pick_lair(
		keys,
		area_name,
		rng,
		):
	"""Collapse Lair from keys + Area — gated by If, then weighted."""
	allowed = set(
			_LAIR_BY_AREA.get(
					area_name,
					("Tower", "Temple", "Cave", "Manor"),
					)
			)
	hits = [
			(lair, weight)
			for conds, lair, weight in _LAIR_SPEC
			if lair in allowed and If(
					keys,
					conds,
					)
			]
	for lair in allowed:
		hits.append(
				(lair, 2)
				)
	return Weighted_Choice(
			hits,
			rng=rng,
			)


def soft_party_hooks(
		keys,
		rng,
		at_most=2,
		):
	"""Optional lines the DM may use if the table fits — never verifies a party."""
	matched = [
			line
			for conds, line in _PARTY_HOOKS
			if If(
					keys,
					conds,
					)
			]
	if not matched:
		return []
	rng.shuffle(
			matched
			)
	return matched[:at_most]


def _npc_url(
		npc,
		):
	from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Paths import nonplayer_hash
	race = str(
			getattr(
					npc,
					"race",
					"Human",
					)
			)
	guild = str(
			getattr(
					npc,
					"char_class",
					"",
					) or ""
			)
	background = str(
			getattr(
					npc,
					"background",
					"",
					) or ""
			)
	level = int(
			getattr(
					npc,
					"level",
					1,
					)
			)
	seed = int(
			getattr(
					npc,
					"seed",
					getattr(
							npc,
							"_seed",
							0,
							),
					)
			)
	if guild and background:
		return "/" + nonplayer_hash(
				race=race,
				guild=guild,
				background=background,
				level=level,
				seed=seed,
				)
	legacy_identity = background or guild or "Commoner"
	return f"/npc/{quote(race, safe='')}/{quote(legacy_identity, safe='')}/{level}/{seed}"


def _occupant(
		npc,
		kind,
		why,
		link_dm_character=False,
		):
	return {
			"kind": kind,
			"name": str(
					getattr(
							npc,
							"name",
							"Someone",
							)
					),
			"why_here": why,
			"link_dm_character": link_dm_character,
			"link_bbeg": link_dm_character,
			"npc_seed": int(
					getattr(
							npc,
							"seed",
							getattr(
									npc,
									"_seed",
									0,
									),
							)
					),
			"npc_level": int(
					getattr(
							npc,
							"level",
							1,
							)
					),
			"npc_race": str(
					getattr(
							npc,
							"race",
							"Human",
							)
					),
			"npc_guild": str(
					getattr(
							npc,
							"char_class",
							"",
							) or ""
					),
			"npc_background": str(
					getattr(
							npc,
							"background",
							"",
							) or ""
					),
			"npc_url": _npc_url(
					npc
					),
			"trait": str(
					Resolve_Legacy_Attribute(
							npc,
							"trait",
							"",
							) or ""
					),
			"title": str(
					getattr(
							npc,
							"title",
							"",
							) or ""
					),
			}


def _mint_npc(
		adventure,
		rng,
		):
	try:
		from AtlasActorLudi.AtlasAlusoris import summon_nonplayer
	except ImportError:
		return None
	seed = rng.randint(
			1,
			65536,
			)
	level = max(
			1,
			adventure.level + rng.choice(
					[-1, 0, 0, 1]
					),
			)
	try:
		return summon_nonplayer(
				level=level,
				seed=seed,
				light=True,
				)
	except Exception:
		return None


def frame_briefing(
		adventure,
		):
	"""DM frame when a DM Character is set: who, Area, Lair — no plot graph."""
	if adventure.dm_character is None:
		raise ValueError(
				"frame_briefing requires adventure.dm_character"
				)
	if adventure not in Area or adventure not in Lair:
		Collapse_Frame(
				adventure
				)
	host = adventure.dm_character
	name = str(
			getattr(
					host,
					"name",
					"the figure",
					)
			)
	title = str(
			getattr(
					host,
					"title",
					"",
					) or ""
			)
	race = str(
			getattr(
					host,
					"race",
					"",
					)
			)
	guild = str(
			getattr(
					host,
					"char_class",
					"",
					)
			)
	background = str(
			getattr(
					host,
					"background",
					"",
					)
			)
	who = name if not title else f"{name}, {title}"
	bits = " ".join(
			part
			for part in (
					race,
					guild,
					background,
					)
			if part
			)
	lines = [
			"This is for the Dungeon Master eyes only.",
			"",
			f"Your DM Character is {who}" + (f" — {bits}." if bits else "."),
			"They frame the session — villain, Quest Master, contested guardian, or another role you choose.",
			f"Area: {adventure.area} (the wider place).",
			f"Lair: {adventure.lair} (their seat inside it).",
			"",
			"Generate a scene when you need inspiration. Each card is presentation only — the table owns what happens next.",
			]
	return "\n".join(
			lines
			)


def inspiration_card(
		adventure,
		):
	"""
	Collapse one inspiration card under the locked Area/Lair.
	Always includes at least one scene NPC (or the DM Character) with a sheet link.
	"""
	if adventure.dm_character is None:
		raise ValueError(
				"inspiration_card requires adventure.dm_character"
				)
	if adventure not in Area or adventure not in Lair:
		Collapse_Frame(
				adventure
				)
	host = adventure.dm_character
	host_name = str(
			getattr(
					host,
					"name",
					"the figure",
					)
			)
	keys = npc_keys(
			host
			)
	beat = adventure.card_index
	rng = adventure.fork_rng(
			"card",
			beat,
			adventure.area,
			adventure.lair,
			keys,
			)
	kind = "plot" if rng.random() < 0.55 else "incidental"
	myth = {
			"dm_character": host_name,
			"bbeg": host_name,
			"area": adventure.area,
			"lair": adventure.lair,
			"setting": _SETTING_LINES.get(
					adventure.area,
					"The place holds its breath around the {lair}.",
					),
			"beat": list(
					_PLOT_BEATS if kind == "plot" else _INCIDENTAL_BEATS
					),
			}
	setting = render(
			myth["setting"],
			myth,
			keys,
			rng=rng,
			)
	beat_line = render(
			Choice(
					myth["beat"],
					rng=rng,
					),
			myth,
			keys,
			rng=rng,
			)
	occupants = []
	if kind == "plot" and rng.random() < 0.35:
		why = Choice(
				(
						f"This is {host_name} — pressure, not necessarily a finale.",
						f"{host_name} is here to advance their will; leave the ending to the table.",
						),
				rng=rng,
				)
		occupants.append(
				_occupant(
						host,
						"DM Character",
						why,
						link_dm_character=True,
						)
				)
	else:
		npc = _mint_npc(
				adventure,
				rng,
				)
		label = Choice(
				("Merchant", "Witness", "Agent", "Rival", "Wanderer", "Petitioner"),
				rng=rng,
				)
		if kind == "plot" and label == "Merchant":
			label = "Agent"
		if npc is None:
			nseed = rng.randint(
					1,
					65536,
					)
			occupants.append(
					{
							"kind": label,
							"name": "A stranger",
							"why_here": f"They are tangled with {host_name}'s affairs in the {adventure.area}.",
							"link_dm_character": False,
							"link_bbeg": False,
							"npc_seed": nseed,
							"npc_level": adventure.level,
							"npc_race": "Human",
							"npc_guild": "",
							"npc_background": "Commoner",
							"npc_url": f"/npc/Human/Commoner/{adventure.level}/{nseed}",
							"trait": "",
							"title": "",
							}
					)
		else:
			name = str(
					getattr(
							npc,
							"name",
							"Someone",
							)
					)
			npc_keys_str = npc_keys(
					npc
					)
			why_options = [
					f"{name} is drawn into {host_name}'s cause — as ally, rival, or casualty.",
					f"{name} arrived because the {adventure.lair} draws the curious and the desperate.",
					f"{name} carries a rumor that points toward {host_name}, whether they know it or not.",
					]
			if If(
					npc_keys_str,
					"Criminal",
					) or If(
					keys,
					"Criminal",
					):
				why_options.append(
						f"If a Criminal is in your party, {name} may have been looking for them specifically."
						)
			why = Choice(
					why_options,
					rng=rng,
					)
			occupants.append(
					_occupant(
							npc,
							label,
							why,
							)
					)
	hooks = soft_party_hooks(
			keys,
			rng,
			)
	for occ in occupants:
		if occ.get(
				"link_dm_character"
				) or occ.get(
				"link_bbeg"
				):
			continue
		extra = soft_party_hooks(
				f"{occ.get('npc_race', '')} {occ.get('npc_guild', '')} {occ.get('npc_background', '')} {occ.get('name', '')}",
				rng,
				at_most=1,
				)
		for line in extra:
			if line not in hooks:
				hooks.append(
						line
						)
	title = f"{adventure.area} · {adventure.lair}"
	lines = [
			f"Inspiration — {title}",
			"",
			setting,
			beat_line,
			"",
			"Present:",
			]
	for occ in occupants:
		extra = f" ({occ['title']})" if occ.get(
				"title"
				) else ""
		lines.append(
				f"  • {occ['kind']}: {occ['name']}{extra}"
				)
		lines.append(
				f"    {occ['why_here']}"
				)
		if occ.get(
				"trait"
				):
			lines.append(
					f"    Trait: {occ['trait']}"
					)
		lines.append(
				"    (Open their sheet for the rest — join threads yourself.)"
				)
	if hooks:
		lines.append(
				""
				)
		lines.append(
				"Soft hooks (use only if they fit your table):"
				)
		for h in hooks:
			lines.append(
					f"  — {h}"
					)
	lines.append(
			""
			)
	lines.append(
			"Presentation only. No prescribed ending. Leave the rest to the players."
			)
	adventure.card_index += 1
	return {
			"title": title,
			"kind": kind,
			"prose": "\n".join(
					lines
					),
			"occupants": occupants,
			"area": adventure.area,
			"lair": adventure.lair,
			"hooks": hooks,
			}


def dm_briefing(
		adventure,
		master_name="the Master",
		master_blurb="",
		):
	return frame_briefing(
			adventure
			)


def collapse_scene(
		adventure,
		**_kwargs,
		):
	return inspiration_card(
			adventure
			)


if __name__ == "__main__":
	class StubDMCharacter:
		def __init__(
				self,
				guild="Druid",
				background="Guide",
				race="Elf",
				):
			self.seed = 7
			self.level = 5
			self.race = race
			self.subrace = ""
			self.char_class = guild
			self.background = background
			self.title = "The Green"
			self.name = "Alaxandar"
			self.trait = "Speaks to trees as equals."

	host = StubDMCharacter()
	adv = Forge_Oracle(
			host
			)
	text = frame_briefing(
			adv
			)
	assert "Area:" in text and "Lair:" in text
	assert "DM Character" in text
	assert adv.area == "Forest"
	card = inspiration_card(
			adv
			)
	assert card["occupants"]
	print(
			card["prose"]
			)
