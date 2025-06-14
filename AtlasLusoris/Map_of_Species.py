# AtlasLusoris.Map_of_Species

from AtlasAlusoris.Map_of_Races import race_weights as races
# from AtlasAlusoris.Map_of_Races import *
from AtlasAlusoris.Map_of_Races import (
	Humans
	)
import random

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
		Alert(f"The species '{species_name}' wasn't found, returning default.")
		return ("Unknown", None)
	return mapping[species_name]
