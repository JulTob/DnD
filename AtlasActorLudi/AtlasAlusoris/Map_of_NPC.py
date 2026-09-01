"""
Map of NPCs
Handles NPC generation for D&D 5e.
"""

from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Generation import summon_nonplayer_list
from AtlasActorLudi.AtlasAlusoris.Grimoire_of_NPC import NPC


def generate_npcs(
		selected_race="Random",
		selected_background="Random",
		count=10,
		seed=None,
		level=10,
		):
	"""
	Generate NPCs from the selected Race and Background.

	Preconditions:
	>>	<selected_race> should be a valid race string or "Random".
	>>	<selected_background> should be a valid Background or "Random".
	>>	<count> should be an integer >= 1.

	Postconditions:
	<<	Returns generated Characters from the canonical NonPlayer route.
	"""
	assert isinstance(
			selected_race,
			str,
			), "Precondition failed: selected_race must be a string."
	assert isinstance(
			selected_background,
			str,
			), "Precondition failed: selected_background must be a string."
	assert isinstance(
			count,
			int,
			) and count >= 1, "Precondition failed: count must be an integer >= 1."
	return summon_nonplayer_list(
			race=None if selected_race == "Random" else selected_race,
			background=None if selected_background == "Random" else selected_background,
			count=count,
			seed=seed,
			level=level,
			)
