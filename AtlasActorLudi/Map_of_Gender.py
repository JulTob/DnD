# AtlasActorLudi/Map_of_Gender.py

''' Cartography for Gender Selection '''
import random


def NewGender(assigned=""):
	"""
    Determine the gender of an NPC.
    """
	if "Genasi" in assigned or "Elemental" in assigned:
		return ElementalGender(assigned)

	# Handle assigned values with flexibility for different cases
	if assigned.lower() in ["male", "he", "he/him", "masculine", "him"]:
		return "He"
	if assigned.lower() in ["female", "she", "she/her", "feminine", "her"]:
		return "She"
	if assigned.lower() in ["agender", "fluid", "they", "they/them", "them",
	 	"other"]:
		return "They"
	# Default to a random gender if no valid assigned value
	return random.choice(["He", "She", "They"])

def ElementalGender(genus):
	ATLANTIAN = "Atlantian" in genus
	ZEPHYRIAN = "Zephyrian" in genus
	CRONUSIAN = "Cronusian" in genus

	if ATLANTIAN:
		return random.choice(["Water", "Crystal", "Energy", "Electric"])
	if ZEPHYRIAN:
		return random.choice(["Air", "Wind"])
	if CRONUSIAN:
		return random.choice(["Time", "Energy" , "Sand"])
	if "Chronian" in genus:
		return random.choice(["Time", "Energy" , "Fire", "Earth"])
	if "Eosian" in genus:
		return random.choice(["Air", "Storm", "Wind"])
	if "Etherian" in genus:
		return random.choice(["Electric", "Ether", "Energy", "Plasma"])
	if "Gaian" in genus:
		return random.choice(["Earth", "Nature", "Life"])
	if "Galaxian" in genus:
		return random.choice(["Earth", "Rock", "Time", "Space", "Plasma", "Light"])
	if "Genasi" in genus:
		return random.choice(["Earth", "Fire", "Air", "Water"])
	if "Genie" in genus:
		return random.choice(["Earth", "Fire", "Air", "Water"])
	if "Hyperian" in genus:
		return random.choice(["Sun", "Fire", "Light", "Energy", "Aurean"])
	if "Magmaforged" in genus:
		return random.choice(["Earth", "Fire", "Magma", "Lava", "Metal", "Sulfur"])
	if "Oceanians" in genus:
		return random.choice(["Water", "Depth", "Storm", "Sea"])
	if "Primordial" in genus:
		return random.choice(["Gravity", "Nuclear", "Electric"])
	if "Promethean" in genus:
		return random.choice(["Earth", "Fire", "Electric", "Energy"])
	if "Salamandrian" in genus:
		return random.choice(["Magma", "Fire", "Sulfur", "Smoke"])
	if "Nymphian" in genus:
		return random.choice(["Earth", "Water", "Nature", "Lake"])
	if "Sylphians" in genus:
		return random.choice(["Wind", "Storm", "Air"])
	if "Pigmians" in genus:
		return random.choice(["Earth", "Rock", "Crystal"])
	if "Tartarian" in genus:
		return random.choice(["Depth", "Rock", "Water", "Darkness"])
	if "Titan" in genus:
		return random.choice(["Earth", "Gold", "Silver", "Quicksilver", "Steal", "Iron", "Metalic", "Uranium", "Crystal", "Carbon"])
	if "Tundran" in genus:
		return random.choice(["Water", "Ice", "Snow", "Storm"])
	if "Uranians" in genus:
		return random.choice(["Stars", "Plasma", "Ether", "Light"])
	if "Djinn" in genus:
		return random.choice(["Sand", "Fire", "Nature", "Wind", "Storm", "Sea", "Water" ])
