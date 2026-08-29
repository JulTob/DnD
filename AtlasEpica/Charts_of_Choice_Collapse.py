"""
Charts of Choice Collapse — TOP choices on an Adventure.

Choices apply Theme Tags (TagKit) onto the Adventure. The next scene is
collapsed from Tag membership (Theme, Locus, Power, Plan) via Map_of_Prose_Adventure.
No Assign_Fact lodge, no parallel encounter API — same TOP view as Titles.

Tracked under QST-0037.3 · QST-0037.6 · QST-0037.7 · QST-0037.13 · QST-0037.15.
"""

from __future__ import annotations

from dataclasses import dataclass, field

try:
	from AtlasEpica.Grimoire_of_Adventure import (
		Adventure,
		Assign_Theme,
		Collapse_Axes,
		ROOT_THEMES,
		active_themes,
		open_themes,
	)
	from AtlasEpica.Map_of_Prose_Adventure import collapse_scene
except ImportError:
	from Grimoire_of_Adventure import (  # type: ignore
		Adventure,
		Assign_Theme,
		Collapse_Axes,
		ROOT_THEMES,
		active_themes,
		open_themes,
	)
	from Map_of_Prose_Adventure import collapse_scene  # type: ignore

MAX_EXITS = 4
CHOICES_PER_BEAT = MAX_EXITS
MAX_SCENES = 16


@dataclass
class Occupant:
	"""Person in the scene — why_here only; sheet holds trait/hook."""

	kind: str
	name: str
	why_here: str
	link_master: bool = False
	npc_seed: int | None = None
	npc_level: int | None = None
	npc_race: str | None = None
	npc_archetype: str | None = None
	npc_url: str | None = None

	@property
	def blurb(self) -> str:
		return self.why_here


@dataclass
class Exit:
	"""One choice: may apply a Theme Tag by name (TOP)."""

	index: int
	label: str
	dm_note: str
	theme: str | None = None  # Theme Tag name to Assign_Theme on select
	facts: list[str] = field(default_factory=list)  # unused; UI back-compat


@dataclass
class Scene:
	beat: int
	title: str
	kind: str
	prose: str
	occupants: list[Occupant] = field(default_factory=list)
	exits: list[Exit] = field(default_factory=list)
	theme: str = ""
	themes: list[str] = field(default_factory=list)
	path: list[int] = field(default_factory=list)
	finished: bool = False
	encounter_id: str = ""
	method: str = ""
	facts: list[str] = field(default_factory=list)
	master_stronger: bool = False

	@property
	def choices(self) -> list[Exit]:
		return self.exits


ChoiceOption = Exit
Passage = Scene


def _doors(adventure: Adventure, beat: int) -> list[str]:
	rng = adventure.fork_rng("doors", beat, adventure.theme, tuple(adventure.choice_path))
	pool = [
		"Take the left-hand door",
		"Take the right-hand door",
		"Descend the narrow stair",
		"Climb toward the sound of wind",
		"Follow the lit corridor",
		"Push into the darker passage",
		"Scout before committing",
		"Approach openly and speak",
	]
	rng.shuffle(pool)
	return pool


def crystallize_exits(adventure: Adventure, beat: int) -> list[Exit]:
	"""
	Open choices = Theme Tags still open on this Adventure (TOP open/close).

	Selecting one runs Assign_Theme. Doors pad to MAX_EXITS and may still
	lean a remaining open Theme.
	"""
	Collapse_Axes(adventure)
	opened = list(open_themes(adventure))
	rng = adventure.fork_rng("exits", beat, adventure.theme, tuple(opened), tuple(adventure.choice_path))
	rng.shuffle(opened)
	doors = _doors(adventure, beat)
	soft = "Applies a Theme Tag on the Adventure (TOP). Next scene collapses from membership."

	exits: list[Exit] = []
	# Prefer explicit Theme Tag choices first
	for name in opened:
		if len(exits) >= MAX_EXITS:
			break
		exits.append(
			Exit(
				index=len(exits) + 1,
				label=f"Theme: {name}",
				dm_note=f"Assign_Theme → {name}. Membership opens/closes later flavor.",
				theme=name,
			)
		)
	# Pad with doors that still apply an open Theme if any remain
	di = 0
	while len(exits) < MAX_EXITS:
		theme = opened[len(exits) % len(opened)] if opened else None
		label = doors[di % len(doors)]
		di += 1
		if theme:
			label = f"{label} — lean {theme}"
		exits.append(
			Exit(
				index=len(exits) + 1,
				label=label,
				dm_note=soft if theme else "Advance the crawl; Theme Tags already on the Adventure stay.",
				theme=theme,
			)
		)
	return exits


def _occupants_from(raw: list[dict]) -> list[Occupant]:
	return [
		Occupant(
			kind=o["kind"],
			name=o["name"],
			why_here=o["why_here"],
			link_master=bool(o.get("link_master")),
			npc_seed=o.get("npc_seed"),
			npc_level=o.get("npc_level"),
			npc_race=o.get("npc_race"),
			npc_archetype=o.get("npc_archetype"),
			npc_url=o.get("npc_url"),
		)
		for o in raw
	]


def _build_at(seed: int, level: int, party_size: int, path: list[int]) -> Adventure:
	"""
	Fresh Adventure + Theme Tags from path only.

	Needed so open_themes at beat N does not see Tags from later exits
	(TagKit does not un-apply). Same seed → same axes + same Theme collapse.
	"""
	built = Adventure(seed=seed, level=level, party_size=party_size)
	Collapse_Axes(built)
	for beat, exit_index in enumerate(path):
		prefix = path[:beat]
		_template, options = _exits_at(adventure, beat, prefix)
		match = next((e for e in options if e.index == exit_index), None)
		if match and match.theme:
			Assign_Theme(built, match.theme)
	built.choice_path = list(path)
	return built


def craft_scene(
	adventure: Adventure,
	path: list[int] | None = None,
	*,
	master_name: str = "the Master",
	master_seed: int | None = None,
) -> Scene:
	"""
	Rebuild Theme Tags from path (TOP), collapse scene from membership, sync onto adventure.
	"""
	path = list(path if path is not None else adventure.choice_path)
	built = _build_at(adventure.seed, adventure.level, adventure.party_size, path)
	for name in active_themes(built):
		Assign_Theme(adventure, name)
	adventure.choice_path = list(path)

	beat = len(path)
	themes = active_themes(built)
	finished = beat >= MAX_SCENES

	if finished:
		return Scene(
			beat=beat,
			title="Arc pause",
			kind="finished",
			prose=(
				f"Scene {beat + 1} — pause.\n"
				f"Theme Tags on this Adventure: {', '.join(themes) or 'none'}."
			),
			theme=getattr(built, "theme", "") or "",
			themes=themes,
			path=list(path),
			finished=True,
		)

	raw = collapse_scene(
		built,
		beat=beat,
		master_name=master_name,
		master_seed=master_seed,
	)
	exits = crystallize_exits(built, beat)
	return Scene(
		beat=beat,
		title=raw["title"],
		kind=raw["kind"],
		prose=raw["prose"],
		occupants=_occupants_from(raw["occupants"]),
		exits=exits,
		theme=getattr(built, "theme", "") or "",
		themes=themes,
		path=list(path),
		finished=False,
		encounter_id=raw["kind"],
		method=raw["method"],
		master_stronger=raw["kind"] == "master",
	)


def apply_exit(
	adventure: Adventure,
	exit_index: int,
	*,
	master_name: str = "the Master",
	master_seed: int | None = None,
) -> Scene:
	"""Append choice index; craft_scene applies the Theme Tag via path replay."""
	path = list(adventure.choice_path)
	if exit_index < 1:
		raise ValueError("exit_index must be >= 1")
	path.append(int(exit_index))
	return craft_scene(adventure, path, master_name=master_name, master_seed=master_seed)


def craft_passage(adventure: Adventure, path: list[int] | None = None, **kwargs) -> Scene:
	return craft_scene(adventure, path, **kwargs)


def apply_choice(adventure: Adventure, choice_index: int, **kwargs) -> Scene:
	return apply_exit(adventure, choice_index, **kwargs)


def adventure_path_url(adventure: Adventure, *, master_seed: int | None = None) -> str:
	ms = int(master_seed if master_seed is not None else adventure.seed)
	parts = [
		"dm",
		str(adventure.seed),
		str(adventure.level),
		str(adventure.party_size),
		str(ms),
		*[str(i) for i in adventure.choice_path],
	]
	return "/" + "/".join(parts)


def parse_adventure_path(pathname: str | None) -> dict | None:
	if not pathname:
		return None
	parts = [p for p in str(pathname).strip().split("/") if p]
	if not parts or parts[0] != "dm" or len(parts) < 5:
		return None
	try:
		return {
			"seed": int(parts[1]),
			"level": int(parts[2]),
			"party_size": int(parts[3]),
			"master_seed": int(parts[4]),
			"path": [int(x) for x in parts[5:]],
		}
	except ValueError:
		return None


if __name__ == "__main__":
	adv = Adventure(seed=11, level=5, party_size=4)
	s0 = craft_scene(adv, [], master_name="Vorath", master_seed=11)
	assert s0.theme in ROOT_THEMES
	assert len(s0.exits) == MAX_EXITS
	# Exits expose Theme Tags still open
	assert any(e.theme for e in s0.exits)

	# Applying a Theme Tag via choice → membership
	before = set(active_themes(adv))
	theme_exit = next(e for e in s0.exits if e.theme)
	apply_exit(adv, theme_exit.index, master_name="Vorath", master_seed=11)
	after = set(active_themes(adv))
	assert theme_exit.theme in after
	assert after >= before or theme_exit.theme in after

	# Same seed + path → same exits / themes
	adv2 = Adventure(seed=11, level=5, party_size=4)
	s0b = craft_scene(adv2, [])
	assert [e.label for e in s0.exits] == [e.label for e in s0b.exits]

	# Path replay restores Theme Tags
	path = list(adv.choice_path)
	adv3 = Adventure(seed=11, level=5, party_size=4)
	craft_scene(adv3, path, master_name="Vorath", master_seed=11)
	assert theme_exit.theme in active_themes(adv3)

	url = adventure_path_url(adv, master_seed=11)
	assert parse_adventure_path(url)

	print("AtlasEpica.Charts_of_Choice_Collapse self-test OK")
	print(s0.prose)
	print("Exits:", [(e.label, e.theme) for e in s0.exits])
	print("After choice Themes:", active_themes(adv))
