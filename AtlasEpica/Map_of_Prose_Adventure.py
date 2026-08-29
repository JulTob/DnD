"""
Map of Prose Adventure — tables and collapse for Epica DM prose.

Style kin to Map_of_Titles / Map_of_Stories: functions that read a host and
return flavor text. The host is an Adventure (Grimoire_of_Adventure); axes
(Power, Locus, Plan) are TOP Tags. RNG is the adventure's own seed.

Review (2026-07-15) of the relocated dungeon.py sketch:
- Orphan prose prototype: module-level random, no seed, no Target.
- Entrance list was the only rich table; Room/Stair/Event were stubs.
- Corridor recursion via f-strings nested blindly (bag of sentences).
- Wrong RNG (stdlib global) vs Decree 0002 / adventure-owned Dice pattern.
- Now: Adventure + Tags collapse first; this Map speaks the result.

Tracked under QST-0037. Character/NPC Tags Epica assumes → QST-0037.11.
"""

from __future__ import annotations

import random

try:
	from AtlasEpica.Grimoire_of_Adventure import (
		Adventure,
		Collapse_Axes,
		Forest,
		Locus,
		Plan,
		Power,
		Theme,
		active_themes,
	)
except ImportError:
	from Grimoire_of_Adventure import (  # type: ignore  # running as a script
		Adventure,
		Collapse_Axes,
		Forest,
		Locus,
		Plan,
		Power,
		Theme,
		active_themes,
	)

def Area(genus: str, rng: random.Random) -> str:
	""" 
	Build the Area for the Adventure to happen in.

	If you can say "A tower in a X", then add it to the Areas list.

	Example of code to follow style.
	"""
	Areas = [
		"Dungeon",
		"Forest",
		"Catacomb",
		"Swamp",
		"Mountain",
		"Desert",
		"Island",
		"Sea",
		"Coastline",
		]

	if "Undead" in genus:
		Areas += [
			"Graveyard",
			"Cemetery",
			"Necropolis",
			"Crypt",
			"Catacombs",
		]


	return rng.choice(Areas)


# Locus → entrance lines (Map_of_Titles style: data keyed by meaning)
ENTRANCES_BY_LOCUS = {
	"Forest": (
		"A tower in a wild forest",
		"A ruined watchtower in a wild forest",
		"A trail in the forest",
		"A path leading into the forest",
	),
	"Castle": (
		"An old castle, long abandoned",
		"A brand new castle, but seems abandoned",
		"The cellar of a ruined noble's manor",
		"The cellar of a ruined noble's villa",
		"The cellar of a ruined noble's palace",
	),
	"Ruins": (
		"The ruins of a city",
		"The ruins of a once-prosperous city",
	),
	"Temple": (
		"A destroyed temple",
		"A destroyed shrine",
		"A destroyed monastery",
		"A destroyed temple devoted to an evil deity",
		"A destroyed shrine devoted to an evil deity",
		"A destroyed monastery devoted to an evil deity",
	),
	"Cemetery": (
		"A desolated cemetery",
		"A forgotten mausoleum",
	),
	"Road": (
		"A road of stones",
		"A trail in the forest",
		"A path leading into the forest",
	),
	"Underground": (
		"A concealed entrance into an underground dungeon",
		"The cellar of a ruined noble's manor",
	),
}

PLAN_HOOKS = {
	"Defensive": "keep outsiders out once and for all",
	"Expansionist": "claim what lies beyond and bind it to your will",
	"Vengeful": "settle an old score written in blood and ash",
	"Hidden": "keep a secret buried where no pilgrim should tread",
}

POWER_EVOCATION = {
	"Arcane": "sigils, secrets, and carefully hoarded lore",
	"Divine": "vows, relics, and a faith that will not yield",
	"Primal": "root, storm, and the old law of the wild",
}

# Scene-kind → room lines (narrative crawl; keyed for QST-0037.15)
ROOM_DETAILS = {
	"threshold": (
		"At the threshold, something watches — not yet hostile, not yet kind.",
		"Two ways open; the place has not chosen a side.",
	),
	"crossroads": (
		"The path splits: one way is lit, the other listens.",
		"Doors, stairs, and a chance to rest before the next truth.",
	),
	"hostile": (
		"Steel and intent — someone bound to the Plan bars the way.",
		"A fight, a chase, or a bad bargain waits here.",
	),
	"minion": (
		"A notable enforcer of the Plan — proud, loud, and memorable.",
		"Spare or finish: the crawl will remember.",
	),
	"hazard": (
		"The place itself takes a side: choke, collapse, flood, or snare.",
		"Terrain as adversary — victory / defeat / hanging still apply.",
	),
	"clue": (
		"Evidence of the Plan: a ward, a wound, a warning left behind.",
		"Reading it carefully may open denser Master scenes later.",
	),
	"npc": (
		"Someone who is not the Plan — wounded, rival, or witness.",
		"Aid, pressure, or pass by; Ally Marked is a soft door.",
	),
	"shrine": (
		"A quiet shrine or icon, unattended — Theme may flavor the god or none.",
		"Respect, plunder, or ignore; leave the theology to the table.",
	),
	"merchant": (
		"Travelers with a cart — mundane gear, and sometimes a sealed ward.",
		"Trade is open; price and haggling are the table's.",
	),
	"related": (
		"A face tied to prior memory Tags — kin, debt, or a token remembered.",
		"Listening costs little now and may mean everything later.",
	),
	"master": (
		"The Master — or their unmistakable pressure — enters the box.",
		"Prefer hanging threads early; final death can wait.",
	),
	"deepening": (
		"Deeper chambers: choke point, sanctuary, or stage.",
		"A chance figure might enter — only if the table invites them.",
	),
	"sanctuary": (
		"A brief nook that feels safe — maybe it is.",
		"Rest fiction; raise a hanging thread if you wish.",
	),
}

OCCUPANT_BLURBS = {
	"threshold": "Eyes in the dark — pressure without a name yet.",
	"crossroads": "Optional color — pilgrim, rival, or nobody.",
	"hostile": "Bound to the Plan; attack, flee, or bargain.",
	"minion": "Serves the Plan openly here.",
	"hazard": "No face — the room is the enemy.",
	"clue": "Object or mark; Clue Found densifies later Master scenes.",
	"npc": "A person — open their sheet for trait and hook.",
	"shrine": "Unattended sacred (or formerly sacred) space.",
	"merchant": "Trade on the road toward the Plan.",
	"related": "A person tied to the Master or the Plan — sheet has the rest.",
	"master": "Link the Master NPC sheet; prefer flee over final death early.",
	"deepening": "Optional color — let Theme pick the stranger's face.",
	"sanctuary": "Quiet — until it isn't.",
}

# Scene-only reason someone is here — trait/hook stay on the NPC sheet (QST-0037.15)
WHY_HERE = {
	"npc": (
		"Their father works for {master} and left home to join the Plan; they have not heard from him in quite some time.",
		"They are searching for someone who owes {master} a debt.",
		"They fled a place the Plan touched and are still catching their breath.",
		"They bring a rumor that points toward {master}'s work — whether they know it or not.",
		"They came to warn someone; the warning may already be too late.",
	),
	"minion": (
		"They serve {master} openly here — an enforcer of the Plan.",
		"They were sent to watch this place for {master}.",
		"They are collecting a due owed to {master}.",
	),
	"merchant": (
		"Their cart followed the same rumor that points toward {master}'s work.",
		"They sell to anyone — including people who work for {master}.",
		"They hope the party will buy before the Plan closes this road.",
	),
	"hostile": (
		"They answer to the Plan that {master} drives.",
		"They were hired (or compelled) to keep outsiders away from {master}'s business.",
	),
	"related": (
		"They are tied to {master}'s household, past, or Plan — the sheet holds who they are.",
		"Someone they love works for {master}; they are here because of that bond.",
	),
	"master": (
		"This is {master} — the opposition from your briefing.",
		"{master} is here to advance the Plan; prefer a hanging thread over final death early.",
	),
	"threshold": (
		"Something watches the approach — not yet named.",
	),
	"crossroads": (
		"The place offers doors; who fills them is yours to invite.",
	),
	"hazard": (
		"The room itself is the adversary.",
	),
	"clue": (
		"Evidence of {master}'s Plan was left here — ward, wound, or warning.",
	),
	"shrine": (
		"An unattended shrine; Theme may flavor which god, if any.",
	),
	"deepening": (
		"Deeper in; a chance figure only if the table invites one.",
	),
	"sanctuary": (
		"A brief nook that feels safe — maybe it is.",
	),
}


def why_here(
	adventure: Adventure,
	kind: str,
	*,
	master_name: str = "the Master",
	npc_name: str = "Someone",
) -> str:
	"""One scene-specific reason this person/place is here. Not trait or hook."""
	Collapse_Axes(adventure)
	options = WHY_HERE.get(kind) or WHY_HERE["npc"]
	rng = adventure.fork_rng("why", kind, adventure.theme, tuple(adventure.choice_path))
	line = rng.choice(list(options))
	return line.format(master=master_name, name=npc_name)


# Soft fiction methods — not Tags. How the place protects, how the Master returns.
CONFLICT_BY_LOCUS = {
	"Forest": "The forest is being cut, burned, or claimed — something living is dying for the Plan.",
	"Castle": "The castle's order is rotting from within — keys, oaths, and walls serve the Plan.",
	"Ruins": "The ruins are being emptied of what still remembers — stone, name, or bone.",
	"Temple": "A sacred place is being hollowed — faith twisted or silenced for the Plan.",
	"Cemetery": "The dead are being disturbed or pressed into the Plan's service.",
	"Road": "The road itself is becoming a trap — travelers fed into the Plan.",
	"Underground": "Something below is waking or being sealed — the Plan needs the dark.",
}

LOCUS_PROTECTION = {
	"Forest": (
		"The forest considers the party its protector: it will not let them die. "
		"After a few hours they resurrect, but a tree has died to save them.",
		"Roots close wounds once — then a sapling withers somewhere out of sight.",
		"Moss muffles a killing blow; a stag falls in their place far off.",
	),
	"Castle": (
		"An old oath in the stones still binds: once per crawl, a fallen hero wakes in a servant's alcove.",
		"The castle refuses a clean death for its guests — they wake in a locked room with a new debt.",
	),
	"Ruins": (
		"The ruins remember older laws: a fallen body rises once, marked with dust that never washes off.",
		"A collapsed arch takes the killing blow; the party lives, the way back is gone.",
	),
	"Temple": (
		"The last honest prayer here still works once: resurrection at a cost the god will name later.",
		"Holy ground rejects permanent death for pilgrims — they wake at the altar missing a memory.",
	),
	"Cemetery": (
		"The dead bargain: one life returned, one grave that will not stay closed.",
		"A ghostly hand pulls them back; something else sits up in a nearby plot.",
	),
	"Road": (
		"A traveler's mercy still walks this road: once, a stranger's cloak becomes a second chance.",
		"Mile-marker magic — they wake at the last stone they passed, hours later.",
	),
	"Underground": (
		"The dark is greedy but not yet finished with them: once, they wake deeper, colder, alive.",
		"A cave-in takes the blow; they dig out later with less light and less time.",
	),
}

MASTER_RETURN = (
	"If {master} falls or flees: they return later harder-eyed, with a new ward or wound that proves the Plan advanced.",
	"If this confrontation ends without {master}'s death: a lieutenant, vessel, or echo waits in a later chamber — stronger.",
	"Death here is not the end of {master} — the Plan has a second body, mask, or bargain ready.",
	"{master} may leave a hanging thread: a laugh, a key, a name — then appear again where it hurts more.",
)


def conflict_line(adventure: Adventure) -> str:
	"""What is at stake in this locus — for briefing / scene framing."""
	Collapse_Axes(adventure)
	return CONFLICT_BY_LOCUS.get(adventure.locus, "Something the Plan wants is being taken or broken here.")


def locus_method(adventure: Adventure) -> str:
	"""How the place may protect the party (soft fiction, not a Tag)."""
	Collapse_Axes(adventure)
	options = LOCUS_PROTECTION.get(adventure.locus) or LOCUS_PROTECTION["Underground"]
	rng = adventure.fork_rng("locus_method", adventure.locus, adventure.theme)
	return rng.choice(list(options))


def master_return_method(adventure: Adventure, master_name: str = "the Master") -> str:
	"""How the Master may come back — prose method, not Assign_Fact."""
	Collapse_Axes(adventure)
	rng = adventure.fork_rng("master_return", adventure.theme, tuple(adventure.choice_path))
	return rng.choice(list(MASTER_RETURN)).format(master=master_name)


def entrance(adventure: Adventure) -> str:
	"""Collapse an entrance line matching the adventure's Locus."""
	Collapse_Axes(adventure)
	locus = adventure.locus
	options = ENTRANCES_BY_LOCUS.get(locus) or ENTRANCES_BY_LOCUS["Underground"]
	return adventure.choose(options)


def plan_hook(adventure: Adventure) -> str:
	"""Short purpose clause for the DM briefing."""
	Collapse_Axes(adventure)
	return PLAN_HOOKS.get(adventure.plan, "see this through")


def power_evocation(adventure: Adventure) -> str:
	"""Evocative fragment for the Power tradition."""
	Collapse_Axes(adventure)
	return POWER_EVOCATION.get(adventure.power, "quiet force")


def room_detail(adventure: Adventure, kind: str) -> str:
	"""One room line for a scene kind (deterministic via adventure RNG fork)."""
	Collapse_Axes(adventure)
	options = ROOM_DETAILS.get(kind) or ROOM_DETAILS["deepening"]
	rng = adventure.fork_rng("room", kind, adventure.locus, adventure.theme)
	return rng.choice(list(options))


def occupant_blurb(adventure: Adventure, kind: str) -> str:
	"""Short occupant hint for a scene kind."""
	Collapse_Axes(adventure)
	return OCCUPANT_BLURBS.get(kind, "")


def dm_briefing(adventure: Adventure, master_name="the Master", master_blurb="") -> str:
	"""
	DM-eyes-only briefing: axes, conflict, and soft methods (not Story Fact Tags).
	"""
	Collapse_Axes(adventure)
	place = entrance(adventure)
	who = master_name if not master_blurb else f"{master_name}, {master_blurb}"
	themes = active_themes(adventure)
	theme_bit = (
		f" → {', '.join(themes)}"
		if len(themes) > 1
		else " (finer Theme Tags crystallize as the table chooses)"
	)
	lines = [
		"This is for the Dungeon Master eyes only!",
		"",
		f"Master, you are {who}.",
		(
			f"Through {power_evocation(adventure)}, you mean to "
			f"{plan_hook(adventure)}."
		),
		f"The story's Theme is {adventure.theme}{theme_bit}.",
		f"Conflict: {conflict_line(adventure)}",
		f"Locus method: {locus_method(adventure)}",
		f"If {master_name} is pressed hard: {master_return_method(adventure, master_name)}",
		f"Adventurers approach: {place}.",
		(
			f"(Level {adventure.level}, party of {adventure.party_size} — "
			f"{adventure.power} · {adventure.locus} · {adventure.plan} · {adventure.theme}.)"
		),
	]
	return "\n".join(lines)


# Flavor lines keyed by Theme Tag membership (TOP: adventure in Regret → …)
_FLAVOR_BY_THEME = {
	"Love": ("someone the Plan threatens that they care about", "a bond under strain"),
	"Bond": ("companions tested", "a vow that still holds"),
	"Regret": ("a path not taken made visible", "an apology arriving too late"),
	"Toxic Love": ("possession dressed as devotion", "jealousy in the room"),
	"Sacrifice": ("something precious that could be given", "a cost looking for a payer"),
	"Hubris": ("a warning ignored", "a limit about to be crossed"),
	"Overreach": ("one step past the safe edge", "a tower tipping"),
	"Fall": ("consequence landing", "a name spoken as a verdict"),
	"Defiance": ("a refusal to kneel", "a dare thrown at the Plan"),
	"Nest": ("home under siege", "the vulnerable at the center"),
	"Protection": ("someone who must be shielded", "a door that must hold"),
	"Invasion": ("the other is already inside", "a breach in the wall"),
	"Legacy": ("what must survive us", "a child, heir, or heirloom"),
	"Discovery": ("a sealed truth", "wonder with teeth"),
	"Forbidden Knowledge": ("lore that was locked for a reason", "a book that looks back"),
	"Wonder": ("awe before the unknown", "beauty that unsettles"),
	"Cost of Truth": ("knowing that changes the knower", "a secret that stains"),
	"Mastery": ("craft and obsession in the air", "a standard that cannot be met cleanly"),
	"Obsession": ("the work owns the worker", "a tool that will not be put down"),
	"Excellence": ("a clean hit of skill", "pride in the making"),
	"Burnout": ("the body failing the standard", "ash where fire was"),
	"Creation": ("something mid-making", "empire, art, or offspring of the Plan"),
	"Empire": ("borders being drawn", "order imposed"),
	"Art": ("a work that outlives the maker", "beauty as a weapon"),
	"Offspring": ("something new with its own will", "a creation that talks back"),
}

_PRESENCE = (
	"npc",
	"npc",
	"minion",
	"hostile",
	"merchant",
	"master",
	"none",
	"hazard",
)


def collapse_scene(
	adventure: Adventure,
	*,
	beat: int = 0,
	master_name: str = "the Master",
	master_seed: int | None = None,
) -> dict:
	"""
	Collapse one scene from Adventure Tag membership (Theme, Locus, Power, Plan).

	TOP: read who the adventure *is* (Tags), speak a scene. No Assign_Fact lodge.
	Returns a plain dict for Charts to wrap (title, prose, method, occupants…).
	"""
	from urllib.parse import quote

	Collapse_Axes(adventure)
	themes = active_themes(adventure)
	rng = adventure.fork_rng("scene", beat, adventure.theme, tuple(themes), tuple(adventure.choice_path))

	# Flavor from the most specific Theme Tags borne
	flavor_bits = []
	for name in reversed(themes):
		flavor_bits.extend(_FLAVOR_BY_THEME.get(name, ()))
	if not flavor_bits:
		flavor_bits = ("the Plan's pressure in the air",)
	flavor = rng.choice(flavor_bits)

	presence = rng.choice(_PRESENCE)
	# Master more likely under Hubris / Creation
	if adventure.theme in ("Hubris", "Creation") and rng.random() < 0.35:
		presence = "master"
	if adventure.theme in ("Love", "Nest") and presence == "hostile" and rng.random() < 0.5:
		presence = "npc"

	place = entrance(adventure)
	method = (
		master_return_method(adventure, master_name)
		if presence == "master"
		else locus_method(adventure)
	)
	title = f"{adventure.locus} — {flavor}"
	if len(title) > 72:
		title = title[:69] + "…"

	occupants: list[dict] = []
	npc = None
	if presence == "master":
		seed = int(master_seed if master_seed is not None else adventure.seed)
		why = why_here(adventure, "master", master_name=master_name, npc_name=master_name)
		try:
			from AtlasAlusoris.Grimoire_of_NPC import NPC
			npc = NPC(lvl=max(1, adventure.level), seed=seed, light=True)
		except Exception:
			npc = None
		if npc is not None:
			occupants.append(_occupant_dict(npc, "Master", why, link_master=True))
		else:
			occupants.append({
				"kind": "Master",
				"name": master_name,
				"why_here": why,
				"link_master": True,
				"npc_seed": seed,
				"npc_level": max(1, adventure.level),
				"npc_race": None,
				"npc_archetype": None,
				"npc_url": None,
			})
	elif presence in ("npc", "minion", "hostile", "merchant"):
		try:
			from AtlasAlusoris.Grimoire_of_NPC import NPC
			nseed = rng.randint(1, 2**16)
			npc = NPC(lvl=max(1, adventure.level), seed=nseed, light=True)
		except Exception:
			npc = None
		label = {"npc": "NPC", "minion": "Minion", "hostile": "Hostile", "merchant": "Merchant"}[presence]
		if npc is not None:
			name = str(getattr(npc, "name", "Someone"))
			why = why_here(adventure, presence, master_name=master_name, npc_name=name)
			occupants.append(_occupant_dict(npc, label, why))
		else:
			why = why_here(adventure, presence, master_name=master_name, npc_name="Someone")
			occupants.append({
				"kind": label,
				"name": "Someone",
				"why_here": why,
				"link_master": False,
				"npc_seed": None,
				"npc_level": None,
				"npc_race": None,
				"npc_archetype": None,
				"npc_url": None,
			})

	theme_line = ", ".join(themes) if themes else adventure.theme
	lines = [
		f"Scene {beat + 1} — {title}",
		f"Theme Tags: {theme_line}",
		f"Conflict: {conflict_line(adventure)}",
		"",
		f"The place leans toward: {flavor}.",
		(
			f"Setting: {place}. Power: {adventure.power} "
			f"({power_evocation(adventure)}). Plan: {adventure.plan} "
			f"— {plan_hook(adventure)}."
		),
		"",
		f"Method: {method}",
		"",
	]
	if occupants:
		lines.append("Present:")
		for occ in occupants:
			lines.append(f"  • {occ['name']} — {occ['why_here']}")
			lines.append("    (Open their sheet for trait, hook, and stats.)")
		lines.append("")
	lines.append(
		"Scene collapsed from Adventure Tags. Choices below apply Theme Tags "
		"(TOP) — then the next scene collapses again. Join threads yourself."
	)

	return {
		"title": title,
		"kind": presence,
		"prose": "\n".join(lines),
		"method": method,
		"occupants": occupants,
		"themes": themes,
	}


def _occupant_dict(npc, kind: str, why: str, link_master: bool = False) -> dict:
	from urllib.parse import quote
	race = str(getattr(npc, "race", "Human"))
	archetype = str(getattr(npc, "archetype", "Commoner"))
	level = int(getattr(npc, "level", 1))
	seed = int(getattr(npc, "seed", getattr(npc, "_seed", 0)))
	name = str(getattr(npc, "name", "Someone"))
	return {
		"kind": kind,
		"name": name,
		"why_here": why,
		"link_master": link_master,
		"npc_seed": seed,
		"npc_level": level,
		"npc_race": race,
		"npc_archetype": archetype,
		"npc_url": (
			f"/npc/{quote(race, safe='')}/"
			f"{quote(archetype, safe='')}/{level}/{seed}"
		),
	}


def prologue(adventure: Adventure | None = None) -> str:
	"""
	Legacy-shaped opener: mysterious location + invitation.
	Prefer dm_briefing() for the Epica product surface.
	"""
	if adventure is None:
		adventure = Adventure(seed=0)
	Collapse_Axes(adventure)
	place = entrance(adventure)
	return (
		f"Driven by your adventures, you come to a mysterious location: {place}.\n"
		f"If you decide to enter, the {adventure.locus.lower()} waits — "
		f"a {adventure.plan.lower()} design under {adventure.power} power.\n"
	)


# --- Thin passage grammar (kept light; full CYOA → QST-0037.3) ---

def passage(adventure: Adventure) -> str:
	"""One corridor beat; uses adventure RNG (not nested f-string chaos)."""
	Collapse_Axes(adventure)
	beats = [
		"continues straight for 30 ft., then ends at a door",
		"continues straight; a side passage opens to the right",
		"continues straight; a side passage opens to the left",
		"comes to a T intersection",
		"comes to a Y intersection",
		"emerges into a chamber",
		"ascends a stair",
		"descends a stair",
		"reaches a dead end",
	]
	return adventure.choose(beats)


def Dungeon(seed=0, level=5, party_size=4) -> str:
	"""Legacy entry: return a DM briefing for a seeded adventure."""
	adventure = Adventure(seed=seed, level=level, party_size=party_size)
	return dm_briefing(adventure)


if __name__ == "__main__":
	adv = Adventure(seed=0, level=5, party_size=4)
	text = dm_briefing(adv, master_name="Alaxandar Lorenlen", master_blurb="an Elf Druid")
	assert "Dungeon Master eyes only" in text
	assert "Alaxandar Lorenlen" in text
	assert adv in Power and adv in Locus and adv in Plan and adv in Theme

	again = Adventure(seed=0, level=5, party_size=4)
	text2 = dm_briefing(again, master_name="Alaxandar Lorenlen", master_blurb="an Elf Druid")
	assert text == text2, "same seed must yield the same briefing"

	# Locus filters entrances; Collapse_Axes must not replace an existing Locus
	wood = Adventure(seed=99, level=3, party_size=3)
	Forest(wood)
	Collapse_Axes(wood)
	assert wood in Forest and wood.locus == "Forest"
	ent = entrance(wood)
	assert ent in ENTRANCES_BY_LOCUS["Forest"]

	print("AtlasEpica.Map_of_Prose_Adventure self-test OK")
	print(text)
