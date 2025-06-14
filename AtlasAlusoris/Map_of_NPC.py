# AtlasLegends/Map_of_NPC.py

"""
Map of NPCs
Handles NPC generation for D&D 5e.
"""


''' Cartography'''
from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError

try:
	from AtlasAlusoris.Map_of_Races import Race
	from AtlasAlusoris.Map_of_Archetypes import Archetype
	from AtlasAlusoris.Grimoire_of_NPC import NPC
	Initialized("Atlas to Alusoris procured")
except ModuleNotFoundError as e:
	Alert(f"The Atlases for charting the Map of Non Player Characters (Alusoris) have not been found:\n {e}", e)

import random


def generate_npcs(
	selected_race="Random",
	selected_archetype="Random",
	count=10):
	"""
	Generate a list of NPCs based on the selected race, archetype, and count.

	Preconditions:
	>> 	<selected_race> should be a valid race string or "Random".
	>> 	<selected_archetype> should be a valid archetype string or "Random".
	>>	<count> should be an integer >= 1.

	Postconditions:
	<< 	Returns a list of tuples [(NPC, seed), ...] containing generated NPCs
		and their respective seeds.
	"""
	assert isinstance(selected_race, str), "Precondition failed: selected_race must be a string."
	assert isinstance(selected_archetype, str), "Precondition failed: selected_archetype must be a string."
	assert isinstance(count, int) and count >= 1, "Precondition failed: count must be an integer >= 1."

	npcs = []
	for _ in range(count):
		# Generate a random seed for each NPC
		seed = random.randint(0, 2**12)
		random.seed(seed)

		# Set race and archetype, defaulting to random selection if specified
		race = Race() if selected_race == "Random" else selected_race
		archetype = archetype() if selected_archetype == "Random" else selected_archetype

		# Instantiate NPC and store with seed
		npc = NPC.NPC(race=race, archetype=archetype, lvl=10, seed=seed)
		News(f"New NPC Created: {npc.name}, {npc.title} - {npc.archetype} {npc.race}: {npc.subrace}")
		npcs.append(npc)

	return npcs
