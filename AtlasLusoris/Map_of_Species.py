# AtlasLusoris.Map_of_Species

from Minion import guardian

from AtlasAlusoris.Map_of_Races import race_weights as races
# from AtlasAlusoris.Map_of_Races import *
from AtlasAlusoris.Map_of_Races import (
	Humans
	)
import random

from AtlasLusoris.Grimoire_of_Features import  *

species = {
	"Human":           	120, #
	"Dwarf":        	100, #
	"Elf":            	100,
	"Dragonborn":   	100,
	"Gnome":        	80,
	"Orc":            	80,
	"Halfling":        	80,
	"Tiefling":        	75,
	"Goliath":        	75,
	"Aasimar":        	75,
#	"Githyanki":    	40,
#	"Githerai":        	40,
#	"Goblin":        	30,
#	"Kobold":        	30,
#	"Lizardfolk":    	30,
#	"Satyr":        	30,
#	"Minotaur":        	30,
#	"Shifter":        	30,
#	"Aarakocra":    	25,
#	"Changeling":    	25,
#	"Deep Gnome":    	25,
#	"Duergar":        	25,
#	"Eladrin":        	25,
#	"Fairy":        	25,
#	"Firbolg":        	25,
#	"Air Genasi":    	25,
#	"Earth Genasi":    	25,
#	"Fire Genasi":    	25,
#	"Water Genasi":    	25,
#	"Yuan Ti":        	25,
#	"Warforged":    	25,
#	"Centaur":        	20,
#	"Harengon":        	15,
#	"Kenku":        	15,
#	"Locathah":        	15,
#	"Owlin":        	15,
#	"Sea Elf":        	15,
#	"Shadar Kai":    	15,
#	"Tabaxi":        	15,
#	"Tortle":        	15,
#	"Triton":       	15,
#	"Verdan":        	15,
#	"Bugbear":        	15,
#	"Grung":        	15,
#	"Hobgoblin":    	15,
#	"Kender":        	15,
#	"Kalashtar":    	15,
#	"Dhampire":        	15,
#	"Hexblood":        	15,
#	"Reborn":        	15,
#	"Aetherborn":    	10,
#	"Aven":            	10,
#	"Khenra":        	10,
#	"Kor":            	10,
#	"Merfolk":        	10,
#	"Naga":            	10,
#	"Siren":        	10,
#	"Vampire":        	10,
#	"Loxodon":        	10,
#	"Simic Hybrid":    	10,
#	"Vedalken":        	10,
#	"Astral Elf":    	10,
#	"Autognome":    	10,
#	"Giff":            	10,
#	"Hadozee":        	10,
#	"Plasmoid":        	10,
#	"Thri Kreen":    	10,
#	"Leonin":        	10,
						}

def random_species():
	return random.choices(list(species_weights.keys()), weights=species_weights.values(), k=1)[0]

@guardian
def species_to_race_and_subrace(species_name):
	mapping = {
		"Human"     : ("Human",      Humans()),
		"Dwarf": ("Dwarf", None),
		"Elf": ("Elf", None),
		"Dragonborn": ("Dragon", "Dragonborn"),
		"Gnome": ("Gnome", None),
		"Orc": ("Orc", None),
		"Halfling": ("Halfling", None),
		"Tiefling": ("Fiend", "Tiefling"),
		"Goliath": ("Giant", "Goliath"),
		"Aasimar": ("Celestial", "Aasimar"),
		# Add others if needed.
		}
	if species_name not in mapping:
		return ("Unknown", None)
	return mapping[species_name]


def species_features(species_name):

	species = {
		"Human": [
			Resourceful(),                       # always-on Inspiration
			Feat(                                # Origin feat choice at 1st level
				name="Origin Feat",
				apply=lambda c: None,            # the feat-picking logic lives elsewhere
				description=(
					"You gain one feat of your choice at 1st level. "
					"You must still meet its prerequisites."
					),
				source="Species Feature",
				),
			],


		"Aasimar": [
			Darkvision(),
			CelestialResistance(),
			HealingHands(),
			LightBearer()
			],
		"Dwarf": [
			Darkvision(),
			DwarvenResilience(),
			DwarvenWeaponTraining(),
			DwarvenToughness()
			],
			}
	if species_name == "Elf":
		return ElvenFeats()
	if species_name == "Dragonborn":
		return DragonbornFeats()

	if species_name == "Gnome":
			lineage_choice = random.choice(["Forest", "Rock"])
			features = [
				Darkvision(),
				GnomishCunning(),
				]
			if lineage_choice == "Forest":
				features.append(ForestGnomeLineage())
			if lineage_choice == "Rock":
				features.append(RockGnomeLineage())
			return features
	return species.get(species_name, [])


def apply_species_features(char, species_name):
	for feature in species_features(species_name):
		feature(char)  # Will only run if `apply` exists
		char.features.append(feature)

def DragonbornFeats():
	colors = ["Black",	"Blue",	"Brass" ,	"Bronze", "Copper", 	"Gold", "Green", 	"Red", "Silver", "White"]
	damage = {
		"Black":	"Acid",
		"Blue":		"Lightning",
		"Brass":	"Fire",
		"Bronze":	"Lightning",
		"Copper":	"Acid",
		"Gold":		"Fire",
		"Green":	"Poison",
		"Red":		"Fire",
		"Silver":	"Cold",
		"White":	"Cold"}
	color = random.choice(colors)
	dragonborn = Feature(name="Dragonborn",
		description="""The ancestors of dragonborn hatched from the eggs of chromatic and metallic dragons. One story holds that these eggs were blessed by the dragon gods Bahamut and Tiamat, who wanted to populate the multiverse with people created in their image. Another story claims that dragons created the first dragonborn without the gods' blessings. Whatever their origin, dragonborn have made homes for themselves on the Material Plane.
		<br>
		Dragonborn look like wingless, bipedal dragons: Scaly, bright eyed, and thick boned with horns on their heads, and their coloration and other features are reminiscent of their draconic ancestors.""",
		source="Species Feature")
	DraconicAncestry = Feature(name="Draconic Ancestry",
		description=f"""
		Your lineage stems from a {color} Dragon progenitor. <br>
		You have Resistance to {damage[color]} damage.
		""",
		source="Species Feature")
	BreathWeapon  = Feature(name="Breath Weapon",
			description=f"""
When you take the Attack action on your turn, you can replace one of your attacks with an exhalation of magical energy in either a 15-foot Cone or a 30-foot Line that is 5 feet wide (choose the shape each time).
Each creature in that area must make a Dexterity saving throw (DC 8 plus your Constitution modifier and Proficiency Bonus).
On a failed save, a creature takes 1d10 {damage[color]} damage.
On a successful save, a creature takes half as much damage.
This damage increases by 1d10 when you reach character levels 5 (2d10), 11 (3d10), and 17 (4d10).

You can use this Breath Weapon a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.
			""",
			source="Species Feature")
	DraconicFlight = Feature(name="Draconic Flight.",
			description=f"""
When you reach character level 5, you can channel draconic magic to give yourself temporary flight. As a Bonus Action, you sprout spectral wings on your back that last for 10 minutes or until you retract the wings (no action required) or have the Incapacitated condition. During that time, you have a Fly Speed equal to your Speed. Your wings appear to be made of the same energy as your Breath Weapon. Once you use this trait, you can't use it again until you finish a Long Rest.
			""",
			source="Species Feature")
	return [Humanoid(),	dragonborn, DraconicAncestry, BreathWeapon, Darkvision(), DraconicFlight]

def ElvenFeats():
	features =  [
		Humanoid(),
		Darkvision(),
		Feature(name="Keen Senses", description="You have proficiency in the Perception skill.", source="Species Feature"),
		Feature(name="Fey Ancestry", description="You have advantage on saving throws against being charmed.", source="Species Feature")
		]
	return features


def Humanoid():
	return Feature(name="Creature Type", description="Humanoid", source="Species Feature")


def creature_type_label(features=None, default="Humanoid"):
	"""Return the Creature Type string from species features, if present."""
	for feature in features or []:
		if getattr(feature, "name", "") == "Creature Type":
			return getattr(feature, "description", default) or default
	return default
