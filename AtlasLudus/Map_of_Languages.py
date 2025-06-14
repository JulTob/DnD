import random
from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError

try:
	from AtlasAlusoris.Map_of_NPC 	import generate_npcs, NPC
	from AtlasLudus.Map_of_Dice 	import Dice
except ImportError as e:
	Alert(f"Couldn't locate imports in the Map of Languages:", e)

def add_language(languages, language, chance=100, INT=0):
	"""Try to add a language based on a dice roll and chance."""
	if chance<=1 and language not in languages:
		languages.append(language)
	elif Dice(chance-INT) <= 1 and language not in languages:
		languages.append(language)

def Language(npc):
	"""
	The language : chance to know the language, as 1 out of "number"
	Represents the population's average chance of one element knowing
		the language.
	Substracting the inteligence modifier of the npc represents a
		higher (or lower) chance of knowing more languages than the average.
	"""
	race = npc.race
	archetype = npc.archetype
	INT = npc.ability_scores.int_mod
	if race == "":
		race = "base"
	if archetype == "":
		archetype = "base"

	languages = []


	if race == "base":
		langs = {
			"Common": 1,
			"Dwarvish": 20,
			"Elvish": 	20,
			"Giant": 	20,
			"Gnomish": 	20,
			"Goblin": 	20,
			"Halfling": 20,
			"Orc": 		20,
			"Abyssal": 	20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 	20,
			"Undercommon": 20,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)

	if race == "Human":
		langs = {
			"Common": 1,
			"Dwarvish": 7,
			"Elvish": 7,
			"Giant": 7,
			"Gnomish": 7,
			"Goblin":7,
			"Halfling": 7,
			"Orc": 7,
			"Abyssal": 25,
			"Celestial": 25,
			"Draconic": 25,
			"Deep Speech": 25,
			"Infernal": 25,
			"Primordial": 25,
			"Sylvan": 20,
			"Undercommon": 25,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)

	if race == "Aberration":
		langs = {
			"Common": 6,
			"Dwarvish": 19,
			"Elvish": 21,
			"Giant": 15,
			"Gnomish": 26,
			"Goblin": 13,
			"Halfling": 26,
			"Orc": 11,
			"Abyssal": 10,
			"Celestial": 10,
			"Draconic": 21,
			"Deep Speech": 1,
			"Infernal": 10,
			"Primordial": 26,
			"Sylvan": 50,
			"Undercommon": 3,
			"Telepathy (60 ft.) ": 11,
			}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Aven":
		langs = {
			"Common": 4,
			"Dwarvish": 26,
			"Elvish": 10,
			"Giant": 21,
			"Gnomish": 26,
			"Goblin": 26,
			"Halfling": 16,
			"Orc": 26,
			"Abyssal": 26,
			"Celestial": 7,
			"Draconic": 7,
			"Deep Speech": 100,
			"Infernal": 100,
			"Primordial": 4,
			"Sylvan": 1,
			"Undercommon": 100,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Beast":
		langs = {
			"Common": 4,
			"Beastly Speech":1,
			"Dwarvish": 20,
			"Elvish": 10,
			"Giant": 20,
			"Gnomish": 10,
			"Goblin": 10,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 10,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 10,
			"Sylvan": 2,
			"Undercommon": 20,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Beastfolk":
		langs = {
			"Common": 3,
			"Beastly Speech":3,
			"Dwarvish": 25,
			"Elvish": 8,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 15,
			"Celestial": 15,
			"Draconic": 10,
			"Deep Speech": 200,
			"Infernal": 15,
			"Primordial": 10,
			"Sylvan": 1,
			"Undercommon": 15,
			f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Catfolk":
		langs = {
			"Common": 5,
			"Dwarvish": 20,
			"Elvish": 	15,
			"Giant": 	20,
			"Gnomish": 	20,
			"Goblin": 	20,
			"Halfling": 25,
			"Orc": 		20,
			"Abyssal": 	15,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 15,
			"Primordial": 15,
			"Sylvan": 	1,
			"Undercommon": 5,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Celestial":
		langs = {
			"Common": 1,
			"Dwarvish": 11,
			"Elvish": 9,
			"Giant": 11,
			"Gnomish": 11,
			"Goblin": 11,
			"Halfling": 11,
			"Orc": 11,
			"Abyssal": 9,
			"Celestial": 1,
			"Draconic": 11,
			"Deep Speech": 22,
			"Infernal": 10,
			"Primordial": 25,
			"Sylvan": 7,
			"Undercommon": 22,
			"Understands All languages":10,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)

		if Dice(2)>1: add_language(languages, "Telepathy (60 feet)", 8)
		elif Dice(2)>1: add_language(languages, "Telepathy (120 feet)", 10)
	if race == "Construct":
		add_language(languages, "Understands the languages of its creator.", 1)
		add_language(languages, "Understands All languages.", 5)
	if race == "Dragon":
		langs = {
			"Common": 1,
			"Dwarvish": 8,
			"Elvish": 9,
			"Giant": 8,
			"Gnomish": 20,
			"Goblin": 15,
			"Halfling": 20,
			"Orc": 8,
			"Abyssal": 10,
			"Celestial": 15,
			"Draconic": 1,
			"Deep Speech": 12,
			"Infernal": 8,
			"Primordial": 10,
			"Sylvan": 5,
			"Undercommon": 10,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Dwarf":
		langs = {
			"Common": 1,
			"Dwarvish": 1,
			"Elvish": 10,
			"Giant": 8,
			"Gnomish": 17,
			"Goblin": 19,
			"Halfling": 10,
			"Orc": 22,
			"Abyssal": 21,
			"Celestial": 19,
			"Draconic": 14,
			"Deep Speech": 12,
			"Infernal": 14,
			"Primordial": 12,
			"Sylvan": 25,
			"Undercommon": 5,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Elf":
		langs = {
			"Common": 1,
			"Dwarvish": 6,
			"Elvish": 1,
			"Giant": 12,
			"Gnomish": 6,
			"Goblin": 18,
			"Halfling": 12,
			"Orc": 20,
			"Abyssal": 8,
			"Celestial": 8,
			"Draconic": 8,
			"Deep Speech": 16,
			"Infernal": 8,
			"Primordial": 6,
			"Sylvan": 4,
			"Undercommon": 6,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Elemental":
		values = [1, 20, 20, 20]
		random.shuffle(values)
		aq, ter, ign, aur = values
		langs = {
			"Common": 5,
			"Dwarvish": 8,
			"Elvish": 8,
			"Giant": 8,
			"Gnomish": 8,
			"Goblin": 18,
			"Halfling": 18,
			"Orc": 12,
			"Abyssal": 12,
			"Celestial": 12,
			"Draconic": 12,
			"Deep Speech": 20,
			"Infernal": 12,
			"Primordial": 1,
			"Sylvan": 4,
			"Undercommon": 10,
			"Ignan": ign,
			"Terran":ter,
			"Aquan": aq,
			"Auran": aur,
		}
		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Fey":
		langs = {
			"Common": 3,
			"Dwarvish": 14,
			"Elvish": 3,
			"Giant": 10,
			"Gnomish": 8,
			"Goblin": 4,
			"Halfling": 16,
			"Orc": 16,
			"Abyssal": 16,
			"Celestial": 16,
			"Draconic": 8,
			"Deep Speech": 20,
			"Infernal": 16,
			"Primordial": 8,
			"Sylvan": 1,
			"Undercommon": 20,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Fiend":
		langs = {
			"Common": 1,
			"Dwarvish": 4,
			"Elvish": 4,
			"Giant": 8,
			"Gnomish": 4,
			"Goblin": 2,
			"Halfling": 12,
			"Orc": 4,
			"Abyssal": 2,
			"Celestial": 25,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 2,
			"Primordial": 22,
			"Sylvan": 20,
			"Undercommon": 8,
			"Telepathy (60 ft.)": 10,
			}
		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Giant":
		langs = {
			"Common": 5,
			"Dwarvish": 4,
			"Elvish": 20,
			"Giant": 1,
			"Gnomish": 8,
			"Goblin": 8,
			"Halfling": 20,
			"Orc": 8,
			"Abyssal": 12,
			"Celestial": 12,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 12,
			"Primordial": 16,
			"Sylvan": 8,
			}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Gnome":
		langs = {
			"Common": 1,
			"Dwarvish": 3,
			"Elvish": 3,
			"Giant": 3,
			"Gnomish": 1,
			"Goblin": 6,
			"Halfling": 6,
			"Orc": 10,
			"Abyssal": 12,
			"Celestial": 12,
			"Draconic": 12,
			"Deep Speech": 12,
			"Infernal": 12,
			"Primordial": 12,
			"Sylvan": 4,
			"Undercommon": 12,
			}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Goblin":
		langs = {
			"Common": 	4 ,
			"Dwarvish": 20 ,
			"Elvish": 	16 ,
			"Giant": 	18 ,
			"Gnomish": 	18 ,
			"Goblin": 	1,
			"Halfling": 18 ,
			"Orc": 		6  ,
			"Abyssal": 	14 ,
			"Celestial":  20 ,
			"Draconic":   14 ,
			"Deep Speech": 14 ,
			"Infernal":   14 ,
			"Primordial": 20 ,
			"Sylvan": 4 ,
			"Undercommon": 4 ,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Halfling":
		langs = {
			"Common": 1,
			"Dwarvish": 4,
			"Elvish": 4,
			"Giant": 20,
			"Gnomish": 4,
			"Goblin": 20,
			"Halfling": 1,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 4,
			"Draconic": 6,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 18,
			"Sylvan": 18,
			"Undercommon": 20
			}
		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Kobold":
		langs = {
			"Common": 4,
			"Dwarvish": 8,
			"Elvish": 20,
			"Giant": 25,
			"Gnomish": 40,
			"Goblin": 10,
			"Halfling": 20,
			"Orc": 18,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 1,
			"Deep Speech": 20,
			"Infernal": 10,
			"Primordial": 22,
			"Sylvan": 14,
			"Undercommon": 3,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Lizardfolk":
		langs = {
			"Common": 4,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 10,
			"Gnomish": 20,
			"Goblin": 10,
			"Halfling": 20,
			"Orc": 4,
			"Abyssal": 4,
			"Celestial": 20,
			"Draconic": 1,
			"Deep Speech": 4,
			"Infernal": 4,
			"Primordial": 4,
			"Sylvan": 4,
			"Undercommon": 20,
			f"Beast Telepathy (Only Reptiles): The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3,

		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Monstrosity":
		langs = {
			"Common": 6,
			"Dwarvish": 10,
			"Elvish": 22,
			"Giant": 9,
			"Gnomish": 25,
			"Goblin": 11,
			"Halfling": 22,
			"Orc": 7,
			"Abyssal": 4,
			"Celestial": 22,
			"Draconic": 6,
			"Deep Speech": 1,
			"Infernal": 5,
			"Primordial": 12,
			"Sylvan": 9,
			"Undercommon": 1
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Ooze":
		add_language(languages, "Telepathy (60 ft.)", 1)
	if race == "Orc":
		langs = {
			"Common": 1,
			"Dwarvish": 12,
			"Elvish": 12,
			"Giant": 4,
			"Gnomish": 22,
			"Goblin": 2,
			"Halfling": 22,
			"Orc": 1,
			"Abyssal": 8,
			"Celestial": 8,
			"Draconic": 8,
			"Deep Speech": 22,
			"Infernal": 8,
			"Primordial": 8,
			"Sylvan": 8,
			"Undercommon": 8,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Plant":
		langs = {
			"Common": 		2 ,
			"Dwarvish": 	22,
			"Elvish": 		6 ,
			"Giant": 		22,
			"Gnomish": 		18,
			"Goblin": 		18,
			"Halfling": 	25,
			"Orc": 			22,
			"Abyssal": 		24,
			"Celestial": 	8 ,
			"Draconic": 	22,
			"Deep Speech": 	22,
			"Infernal": 	22,
			"Primordial": 	1 ,
			"Sylvan": 		1,
			"Undercommon": 	8 ,
			"Telepathy": 	5 ,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Snakefolk":
		langs = {
			"Common": 	5,
			"Dwarvish": 21,
			"Elvish": 	20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 21,
			"Halfling": 21,
			"Orc": 20,
			"Abyssal": 6,
			"Celestial": 20,
			"Draconic": 1,
			"Deep Speech": 6,
			"Infernal": 12,
			"Primordial": 6,
			"Sylvan": 9,
			"Undercommon": 20,
			f"Beast Telepathy (Only Snakes): The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3,

		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Undead":
		langs = {
			"Common": 	3,
			"Dwarvish": 18,
			"Elvish": 18,
			"Giant": 20,
			"Gnomish": 18,
			"Goblin": 16,
			"Halfling": 18,
			"Orc": 18,
			"Abyssal": 12,
			"Celestial": 12,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 12,
			"Primordial": 100,
			"Sylvan": 100,
			"Undercommon": 15,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if race == "Vampire":
		langs = {
			"Common": 1,
			"Dwarvish": 20,
			"Elvish": 	15,
			"Giant": 	20,
			"Gnomish": 	20,
			"Goblin": 	20,
			"Halfling": 20,
			"Orc": 		20,
			"Abyssal": 	5,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 10,
			"Infernal": 5,
			"Primordial": 20,
			"Sylvan": 	5,
			"Undercommon": 5,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)

	# BACKGROUNDS
	if archetype == "base":
		langs = {
			"Common": 1,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 20,
			}
		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)

	if archetype == "Druid":
		langs = {
			"Common": 1,
			"Druidic":1,
			"Dwarvish": 20,
			"Elvish": 5,
			"Giant": 20,
			"Gnomish": 10,
			"Goblin": 10,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 16,
			"Draconic": 4,
			"Deep Speech": 21,
			"Infernal": 20,
			"Primordial": 4,
			"Sylvan": 3,
			"Undercommon": 20,
			f"Beast Telepathy: {npc.title} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3,
			}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Bandit":
		langs = {
			"Common": 1,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 20,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Bard":
		langs = {
			"Common": 1,
			"Dwarvish": 6,
			"Elvish": 6,
			"Giant": 20,
			"Gnomish": 6,
			"Goblin": 6,
			"Halfling": 6,
			"Orc": 6,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 6,
			"Undercommon": 20
		}
		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Berserker":
		langs = {
			"Common": 	5,
			"Dwarvish": 6,
			"Elvish": 	20,
			"Giant": 	6,
			"Gnomish": 	20,
			"Goblin": 	20,
			"Halfling": 20,
			"Orc": 		6,
			"Abyssal": 	12,
			"Celestial": 	20,
			"Draconic": 	16,
			"Deep Speech": 	16,
			"Infernal": 	12,
			"Primordial": 	16,
			"Sylvan": 		20,
			"Undercommon": 	6,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Charlatan":
		langs = {
			"Common": 1,
			"Dwarvish": 6,
			"Elvish": 6,
			"Giant": 20,
			"Gnomish": 6,
			"Goblin": 6,
			"Halfling": 6,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Cultist":
		langs = {
			"Common": 3,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 8,
			"Celestial": 8,
			"Draconic": 8,
			"Deep Speech": 8,
			"Infernal": 8,
			"Primordial": 8,
			"Sylvan": 20,
			"Undercommon": 8,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Criminal":
		langs = {
			"Common": 5,
			"Thieve's Cant":1,
			"Dwarvish": 12,
			"Elvish": 12,
			"Giant": 20,
			"Gnomish": 12,
			"Goblin": 12,
			"Halfling": 12,
			"Orc": 12,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 4,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Expert":
		langs = {
			"Common": 1,
			"Dwarvish": 5,
			"Elvish": 5,
			"Giant": 5,
			"Gnomish": 5,
			"Goblin": 19,
			"Halfling": 19,
			"Orc": 19,
			"Abyssal": 19,
			"Celestial": 6,
			"Draconic": 19,
			"Deep Speech": 19,
			"Infernal": 19,
			"Primordial": 19,
			"Sylvan": 19,
			"Undercommon": 19,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Explorer":
		langs = {
			"Common": 1,
			"Dwarvish": 4,
			"Elvish": 4,
			"Giant": 4,
			"Gnomish": 4,
			"Goblin": 4,
			"Halfling": 4,
			"Orc": 4,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 4,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Fighter":
		langs = {
			"Common": 20,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 15,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 15,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 15,
			"Undercommon": 15,
			}
		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)

	if archetype == "Healer":
		langs = {
			"Common": 5,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 10,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 4,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 4,
			"Sylvan": 4,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Hero":
		langs = {
			"Common": 2,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 6,
			"Draconic": 6,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 6,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Hunter":
		langs = {
			"Common": 10,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 6,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 6,
			"Sylvan": 1,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Knight":
		langs = {
			"Common": 2,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 6,
			"Draconic": 6,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 6,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Mage":
		langs = {
			"Common": 3,
			"Dwarvish": 6,
			"Elvish": 6,
			"Giant": 6,
			"Gnomish": 6,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 6,
			"Celestial": 6,
			"Draconic": 6,
			"Deep Speech": 6,
			"Infernal": 6,
			"Primordial": 6,
			"Sylvan": 6,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Monk":
		langs = {
			"Common": 5,
			"Dwarvish": 10,
			"Elvish": 10,
			"Giant": 10,
			"Gnomish": 10,
			"Goblin": 10,
			"Halfling": 10,
			"Orc": 10,
			"Abyssal": 10,
			"Celestial": 6,
			"Draconic": 6,
			"Deep Speech": 10,
			"Infernal": 10,
			"Primordial": 6,
			"Sylvan": 10,
			"Undercommon": 10,
			f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":10,

		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Noble":
		langs = {
			"Common": 1,
			"Dwarvish": 6,
			"Elvish": 6,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 12,
			"Draconic": 12,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Priest":
		langs = {
			"Common": 1,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 6,
			"Celestial": 6,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 6,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Pirate":
		langs = {
			"Common": 1,
			"Thieve's Cant": 1,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 12,
			"Infernal": 20,
			"Primordial": 12,
			"Sylvan": 20,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Ranger":
		langs = {
			"Common": 1,
			"Dwarvish": 20,
			"Elvish": 4,
			"Giant": 4,
			"Gnomish": 20,
			"Goblin": 4,
			"Halfling": 20,
			"Orc": 4,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 6,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 6,
			"Sylvan": 6,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Scholar":
		langs = {
			"Common": 1,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 6,
			"Celestial": 6,
			"Draconic": 6,
			"Deep Speech": 6,
			"Infernal": 6,
			"Primordial": 6,
			"Sylvan": 6,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Shaman":
		langs = {
			"Common": 5,
			"Druidic":1,
			"Dwarvish": 20,
			"Elvish": 6,
			"Giant": 6,
			"Gnomish": 20,
			"Goblin": 6,
			"Halfling": 20,
			"Orc": 6,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 8,
			"Sylvan": 1,
			"Undercommon": 20,
			f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":10,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Spy":
		langs = {
			"Common": 1,
			"Thieve's Cant":1,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Traveler":
		langs = {
			"Common": 1,
			"Dwarvish": 5,
			"Elvish": 5,
			"Giant": 5,
			"Gnomish": 5,
			"Goblin": 5,
			"Halfling": 5,
			"Orc": 5,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 12,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 20,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Prankster":
		langs = {
			"Common": 1,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Warrior":
		langs = {
			"Common": 2,
			"Dwarvish": 6,
			"Elvish": 6,
			"Giant": 6,
			"Gnomish": 6,
			"Goblin": 6,
			"Halfling": 6,
			"Orc": 6,
			"Abyssal": 20,
			"Celestial": 20,
			"Draconic": 20,
			"Deep Speech": 20,
			"Infernal": 20,
			"Primordial": 20,
			"Sylvan": 20,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Warlock":
		langs = {
			"Common": 4,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 20,
			"Gnomish": 20,
			"Goblin": 20,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 6,
			"Celestial": 6,
			"Draconic": 6,
			"Deep Speech": 6,
			"Infernal": 6,
			"Primordial": 6,
			"Sylvan": 6,
			"Undercommon": 20
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)
	if archetype == "Witch":
		langs = {
			"Common": 1,
			"Dwarvish": 20,
			"Elvish": 20,
			"Giant": 12,
			"Gnomish": 20,
			"Goblin": 6,
			"Halfling": 20,
			"Orc": 20,
			"Abyssal": 6,
			"Celestial": 6,
			"Draconic": 6,
			"Deep Speech": 6,
			"Infernal": 6,
			"Primordial": 6,
			"Sylvan": 12,
			"Undercommon": 20,
			f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":10,
		}

		for lang, chance in langs.items():
			add_language(languages, lang, chance,INT)

	languages = [lang.strip() for lang in languages if lang.strip()]
		# Remove any empty strings and strip whitespace
	if not languages: return "<i>Common</i>"
	return f"<i> {'<br> '.join(languages)} </i>"
