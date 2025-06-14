"""
Great Grimoire of Characters.
Describes the creation of Characters and their operations.
Rules from D&D 5e.
"""

''' Cartography '''
import random
from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError

from AtlasActorLudi.Map_of_Size import Size
from AtlasActorLudi.Map_of_Gender import NewGender
# Import statements grouped for clarity and error checking
try: # Cartography
	from AtlasLudus.Map_of_Dice import Dice
	from AtlasActorLudi.Map_of_Scores import PB, Modifier
	from AtlasActorLudi.Grimoire_of_AbilityScores import AbilityScores
	from AtlasActorLudi.Grimoire_of_SavingThrows import SavingThrows
	from AtlasActorLudi.Grimoire_of_Skills import Char_Skills, get_other_proficiencies
	News("Atlas Mechanica succesfully procured")
	from AtlasLusoris.Map_of_Classes import classes, subclasses
	from AtlasLusoris.Map_of_Species import species, species_to_race_and_subrace
	from AtlasLusoris.Map_of_Backgrounds import backgrounds
	News("Atlas Lusoris succesfully procured")
	from AtlasAlusoris.Map_of_Races import race_weights as races
	from AtlasAlusoris.Map_of_Races import Race
	News("Atlas Alusoris succesfully procured")
	from AtlasInventarium import Grimoire_of_Objects
	from AtlasInventarium.Grimoire_of_Objects import Object, GenerateEquipment
	from AtlasLusoris.Map_of_Classes import (
		apply_class_proficiencies,
		GetFeatures,                 # main entry-point to get features list
		health_dice
		)

except ImportError as e:
	Fail(f"Import error!", e)

Inform("The Grimoire of Characters is ready to summon.")

class Character:
	def __init__(char,
		name=None,
		species=None,
		char_class=None,
		subclass=None,
		background=None,
		level=1,
		gender=None,
		alignment=None,
		seed=None,
		title = None):
		"""
		Invoke a new Character.
		"""
		# Set random seed if provided
		char.seed = seed if seed is not None else random.randint(0, 2**16)
		char.seed = int(char.seed )
		random.seed(char.seed)

		char.species = species or char.generate_species()
		char.race, char.subrace = species_to_race_and_subrace(char.species)
		char.gender = gender or char.generate_gender()

		char.char_class = char_class or char.generate_class()
		char.subclass = subclass or char.generate_subclass()

		char.background = background or char.generate_background()

		char.alignment = alignment or char.generate_alignment()

		char.lineage = None

		char.name = name or char.generate_name()
		char.title = title          # may be None
		if char.title is None:      # only generate if not supplied
			char.title = char.generate_title()

		char.features = []
		char.equipment = Grimoire_of_Objects.Inventory()
		char.level = level
		char.proficiency_bonus = PB(char.level)
		char.set_characteristics()
		char.set_Skills()
		apply_class_proficiencies(char)
		char.set_Objects()
		char.passive_perception = 10 + char.skills.Perception.calculate_modifier(char.proficiency_bonus)
		char.other_proficiencies = get_other_proficiencies(char.skills)
		char.apply_class_features()
		char.features = GetFeatures(char)
		GenerateEquipment(char)

	def __contains__(pc, text):
		if text in pc.genus: return True
		return False

	def set(char):
		random.seed(char.seed)

	def apply_class_features(character):
		from AtlasLusoris.Map_of_Classes import get_class_progression
		class_prog = get_class_progression(character.Class)
		if class_prog:
			character.features = class_prog.features(character.level, character.subclass)

	def set_characteristics(char):
		"""Set core stats and attributes based on species, class, and background."""
		char.set()
		char.abilities = AbilityScores()
		char.stats = char.generate_stats()
		char.saving_throws = SavingThrows(char.abilities, char.level)
		char.health = char.set_Health()
		char.AC = 10 + Modifier(char.abilities.DEX)

	def generate_alignment(char):
		""" Randomly select an Alignment. """
		return "True Neutral"

	def generate_species(char):
		""" Randomly select a species based on weights. """
		char.set()
		species_names = list(species.keys())
		species_weights = list(species.values())
		chosen_species = random.choices(species_names, weights=species_weights, k=1)[0]
		return chosen_species

	def generate_class(char):
		""" Randomly select a character class. """
		char.set()
		return random.choice(classes)

	@property
	def character_class(char):
		return char.char_class

	@property
	def Class(char):
		return char.char_class

	@property
	def Level(char):
		return char.level

	@property
	def Subclass(char):
		return char.subclass

	def generate_subclass(char):
		""" Randomly select a subclass if applicable. """
		char.set()
		return random.choice(subclasses.get(char.char_class, []))

	def generate_background(char):
		""" Randomly select a background. """
		char.set()
		return random.choice(backgrounds)

	def generate_gender(char):
		""" Randomly select a gender. """
		#from AtlasLore.Map_of_Gender import NewGender
		result = NewGender(char.race)
		return result

	def generate_name(char):
		""" Generate or assign a name. """
		from AtlasNomina.Map_of_Names import NewName
		char.set()
		# Use the existing name generation functions
		name = NewName(char)
		return name

	def generate_title(character):
		""" Generate or assign a name. """
		from AtlasNomina.Map_of_Titles import Title
		character.set()
		# Defensive: ensure the attribute exists
		if not hasattr(character, "title"):
			character.title = None
		return Title(character)

	def set_Health(char):
		""" Calculate character health
			based on level and constitution modifier.
		"""
		from AtlasLusoris.Map_of_Classes import health_dice
		from AtlasActorLudi.Map_of_Scores import Modifier, NewAbilityScore
		from AtlasLudus.Map_of_Dice import Dice

		dice_value = health_dice(char.char_class)
		health = char.level * Modifier(char.abilities.CON)
		health += Dice(D=dice_value-1, N = char.level)
		health += dice_value
		return health

	def to_dict(char):
		""" Convert character details to dictionary format. """
		return {
			'name': 		char.name,
			'title':		char.title,
			'Gender': 		char.gender,
			'Species': 		char.species,
			'Class': 		char.char_class,
			'Subclass': 	char.subclass,
			'Background': 	char.background,
			'Level': 		char.level,
			'Stats': 		char.stats,
			'Alignment': 	char.alignment,
			'Skills': 		char.skills,
			'equipment': 	char.equipment,
			'AC': 			char.AC,
			'Health': 		char.health,
			'PB':			char.proficiency_bonus,
			'size':			Size(char),
			'passive_perception':		char.passive_perception,
			'other_proficiencies':		char.other_proficiencies,
			'features':		[feat.to_dict() for feat in char.features]
			}

	def NPCfy(char):
		from AtlasHero.Grimoire_of_NPC import NPC
		pc_to_npc = NPC(
			race = char.race,
			archetype = char.char_class,
			lvl=char.level,
			seed= char.seed
			)
		return pc_to_npc

	@property
	def genus(char):
		"""
		Compute the Character (pc)'s genus as a string of tags.

		Mimics the NPC genus structure to maintain compatibility
		with functions like Title(), Descriptor(), etc.
		"""
		# For compatibility with NPCs
		archetype = getattr(char, "archetype", None) or getattr(char, "char_class", "")
		attributes = [
			str(char.race or ""),
			str(char.subrace or ""),
			str(archetype or ""),
			str(char.gender or ""),
			str(char.alignment or ""),
		]
		delimiter = " , "
		return delimiter.join(filter(None, attributes))


	@property
	def Type(char):
		# Build a string that includes species and other descriptors
		descriptors = [str(char.species)]
		descriptors.append(str(char.gender))
		descriptors.append(str(char.race))
		descriptors.append(str(char.subrace))
		#descriptors.append(str(char.background))
		# Combine descriptors into a single string
		return ' '.join(descriptors)

	def roll_stat(char):
		rolls = [random.randint(1, 6) for _ in range(4)]
		return sum(sorted(rolls)[1:])

	def generate_stats(char):
		char.set()
		class_stat_preferences = {
			'Barbarian':   {'primary': 'Strength', 		'secondary': 'Constitution'},
			'Bard':        {'primary': 'Charisma', 		'secondary': 'Dexterity'},
			'Cleric':      {'primary': 'Wisdom', 		'secondary': 'Strength'},
			'Druid':       {'primary': 'Wisdom', 		'secondary': 'Constitution'},
			'Fighter':     {'primary': 'Strength', 		'secondary': 'Constitution'},
			'Monk':        {'primary': 'Dexterity', 	'secondary': 'Wisdom'},
			'Paladin':     {'primary': 'Strength', 		'secondary': 'Charisma'},
			'Ranger':      {'primary': 'Dexterity', 	'secondary': 'Wisdom'},
			'Rogue':       {'primary': 'Dexterity', 	'secondary': 'Intelligence'},
			'Sorcerer':    {'primary': 'Charisma', 		'secondary': 'Constitution'},
			'Warlock':     {'primary': 'Charisma', 		'secondary': random.choice(['Dexterity', 'Wisdom', 'Strength', 'Intelligence', 'Constitution', 'Dexterity', 'Constitution', 'Dexterity', 'Constitution', 'Dexterity'])},
			'Wizard':      {'primary': 'Intelligence', 	'secondary': 'Wisdom'},
			}
		background_stat_boosts = {
			'Acolyte':    ['Intelligence', 	'Wisdom',  		'Charisma'],
			'Artisan':    ['Strength', 		'Dexterity', 	'Intelligence'],
			'Charlatan':  ['Dexterity', 	'Constitution', 'Charisma'],
			'Criminal':   ['Dexterity', 	'Constitution', 'Intelligence'],
			'Entertainer':['Strength', 		'Dexterity', 	'Charisma'],
			'Farmer':     ['Constitution', 	'Strength', 	'Wisdom'],
			'Guard':      ['Strength', 		'Intelligence', 'Wisdom'],
			'Guide':      ['Wisdom', 		'Dexterity', 	'Constitution'],
			'Hermit':     ['Wisdom', 		'Charisma', 	'Constitution'],
			'Merchant':   ['Constitution', 	'Intelligence', 'Charisma'],
			'Noble':      ['Strength', 		'Intelligence', 'Charisma'],
			'Sage':       ['Constitution', 	'Wisdom', 		'Intelligence'],
			'Sailor':     ['Strength', 		'Dexterity', 	'Wisdom'],
			'Scribe':     ['Dexterity', 	'Wisdom', 		'Intelligence'],
			'Soldier':    ['Strength', 		'Dexterity', 	'Constitution'],
			'Wayfarer':   ['Dexterity', 	'Charisma', 	'Wisdom'],
			}

		# Initialize stats dictionary


		# Roll six ability scores
		rolled_stats = [char.roll_stat() for _ in range(6)]
		rolled_stats.sort(reverse=True)
			# Sort from highest to lowest

		# Get class primary and secondary stats
		class_prefs = class_stat_preferences.get(char.char_class, {})
		primary_stat = class_prefs.get('primary')
		secondary_stat = class_prefs.get('secondary')

		# Get background stat boosts
		background_prefs = background_stat_boosts.get(char.background, [])

		stats = {
			'Strength': None,
			'Dexterity': None,
			'Constitution': None,
			'Intelligence': None,
			'Wisdom': None,
			'Charisma': None,
			}

		assigned_stats = set()
			# Keep track of which abilities have been assigned

		# Assign highest stat to primary ability
		if primary_stat:
			stats[primary_stat] = rolled_stats.pop(0)
			assigned_stats.add(primary_stat)

		# Assign next highest stat to secondary ability
		if secondary_stat and secondary_stat not in assigned_stats:
			stats[secondary_stat] = rolled_stats.pop(0)
			assigned_stats.add(secondary_stat)

		# Assign remaining stats randomly
		remaining_stats = [stat for stat in stats if stats[stat] is None]
		random.shuffle(remaining_stats)
		for stat in remaining_stats:
			if rolled_stats:
				stats[stat] = rolled_stats.pop(0)
			else:
				# In case there are more abilities than rolled stats (should not happen)
				stats[stat] = char.roll_stat()

		# Apply background stat boosts (+1 to each)
		for stat in background_prefs:
			if stat in stats and stats[stat] is not None:
				stats[stat] = stats[stat] + 1

		# Update the character's ability scores
		if char.abilities:
			char.abilities.STR = stats['Strength']
			char.abilities.DEX = stats['Dexterity']
			char.abilities.CON = stats['Constitution']
			char.abilities.INT = stats['Intelligence']
			char.abilities.WIS = stats['Wisdom']
			char.abilities.CHA = stats['Charisma']
		return stats

	def set_Skills(char):
		""" Assign skill proficiencies
			based on character background and class.
		"""

		char.skills = Char_Skills(AS = char.abilities, ProficiencyBonus=char.proficiency_bonus)
		char.seed += 1
		char.set()
		# Step 1: Adjust skills based on background
		if char.background:
			if char.background == "Acolyte":
				char.skills.Insight.set_proficiency()
				char.skills.Religion.set_proficiency()
				char.skills.Calligrapher_Supplies.set_proficiency()
			elif char.background == "Artisan":
				char.skills.Investigation.set_proficiency()
				char.skills.Persuasion.set_proficiency()
				char.skills.activate_proficiencies(1, [
					"Alchemist's Supplies",
					"Brewer's Supplies",
					"Calligrapher's Supplies",
					"Carpenter's Tools",
					"Cartographer's Tools",
					"Cobbler's Tools",
					"Cook's Utensils",
					"Glassblower's Tools",
					"Jeweler's Tools",
					"Leatherworker's Tools",
					"Mason's Tools",
					"Painter's Supplies",
					"Potter's Tools",
					"Smith's Tools",
					"Tinker's Tools",
					"Weaver's Tools",
					"Woodcarver's Tools",
					])
			elif char.background == "Charlatan":
				char.skills.Deception.set_proficiency()
				char.skills.Sleight_of_Hand.set_proficiency()
				char.skills.Forgery_Kit.set_proficiency()
			elif char.background == "Criminal":
				char.skills.Sleight_of_Hand.set_proficiency()
				char.skills.Stealth.set_proficiency()
				char.skills.Thieves_Tools.set_proficiency()
			elif char.background == "Entertainer":
				char.skills.Acrobatics.set_proficiency()
				char.skills.Performance.set_proficiency()
				char.skills.Musical_Instrument.set_proficiency()
			elif char.background == "Farmer":
				char.skills.Animal_Handling.set_proficiency()
				char.skills.Nature.set_proficiency()
				char.skills.Carpenter_Tools.set_proficiency()
			elif char.background == "Guard":
				char.skills.Athletics.set_proficiency()
				char.skills.Perception.set_proficiency()
				char.skills.Gaming_Set.set_proficiency()
			elif char.background == "Guide":
				char.skills.Stealth.set_proficiency()
				char.skills.Survival.set_proficiency()
				char.skills.Cartographer_Tools.set_proficiency()
			elif char.background == "Hermit":
				char.skills.Medicine.set_proficiency()
				char.skills.Religion.set_proficiency()
				char.skills.Herbalism_Kit.set_proficiency()
			elif char.background == "Merchant":
				char.skills.Animal_Handling.set_proficiency()
				char.skills.Persuasion.set_proficiency()
				char.skills.Navigator_Tools.set_proficiency()
			elif char.background == "Noble":
				char.skills.History.set_proficiency()
				char.skills.Persuasion.set_proficiency()
				char.skills.Gaming_Set.set_proficiency()
			elif char.background == "Sage":
				char.skills.History.set_proficiency()
				char.skills.Arcana.set_proficiency()
				char.skills.Calligrapher_Supplies.set_proficiency()
			elif char.background == "Sailor":
				char.skills.Acrobatics.set_proficiency()
				char.skills.Perception.set_proficiency()
				char.skills.Navigator_Tools.set_proficiency()
			elif char.background == "Scribe":
				char.skills.Investigation.set_proficiency()
				char.skills.Perception.set_proficiency()
				char.skills.Calligrapher_Supplies.set_proficiency()
			elif char.background == "Soldier":
				char.skills.Athletics.set_proficiency()
				char.skills.Intimidation.set_proficiency()
				char.skills.Gaming_Set.set_proficiency()
			elif char.background == "Wayfarer":
				char.skills.Insight.set_proficiency()
				char.skills.Stealth.set_proficiency()
				char.skills.Thieves_Tools.set_proficiency()

		# Step 3: Adjust skills based on subclass (if any)
		if char.subclass:
			if char.subclass == "Eldritch Knight":
				char.skills.Arcana.set_proficiency()
			elif char.subclass == "Battlemaster":
				char.skills.Intimidation.set_proficiency()
			# Add more subclasses

		# Step 2: Set default skills based on class
		if char.character_class:
			if char.character_class == "Fighter":
				char.skills.activate_proficiencies(2, [
					"Acrobatics",
					"Animal Handling",
					"Athletics",
					"History",
					"Insight",
					"Intimidation",
					"Survival",
					])
				char.skills.Simple_Weapons.set_proficiency()
				char.skills.Martial_Weapons.set_proficiency()
				char.skills.Light.set_proficiency()
				char.skills.Medium.set_proficiency()
				char.skills.Heavy.set_proficiency()
				char.skills.Shields.set_proficiency()


			elif char.character_class == "Wizard":
				char.skills.activate_proficiencies(2, [
					"Arcana",
					"History",
					"Insight",
					"Investigation",
					"Medicine",
					"Religion",
					])
				char.skills.Simple_Weapons.set_proficiency()
			elif char.character_class == "Rogue":
				char.skills.Thieves_Tools.set_proficiency()
				char.skills.activate_proficiencies(4, [
					"Acrobatics",
					"Athletics",
					"Deception",
					"Insight",
					"Intimidation",
					"Investigation",
					"Perception",
					"Persuasion",
					"Sleight of Hand",
					"Stealth",
					])
				char.skills.activate_expertise(
					2,
					char.skills.get_proficient_skills()
					)

				char.skills.Simple_Weapons.set_proficiency()
				char.skills.Finesse.set_proficiency()
				char.skills.Light_Weapons.set_proficiency()
				char.skills.Light.set_proficiency()
			elif char.character_class == "Cleric":
				char.skills.activate_proficiencies(2, [
					"History",
					"Insight",
					"Medicine",
					"Persuasion",
					"Religion",
					])
				char.skills.Simple_Weapons.set_proficiency()
				char.skills.Light.set_proficiency()
				char.skills.Medium.set_proficiency()
				char.skills.Shields.set_proficiency()
			elif char.character_class == "Ranger":
				char.skills.activate_proficiencies(3, [
					"Animal Handling",
					"Athletics",
					"Insight",
					"Investigation",
					"Nature",
					"Perception",
					"Stealth",
					"Survival",
					])
				char.skills.Simple_Weapons.set_proficiency()
				char.skills.Martial_Weapons.set_proficiency()
				char.skills.Light.set_proficiency()
				char.skills.Medium.set_proficiency()
				char.skills.Shields.set_proficiency()
			elif char.character_class == "Paladin":
				char.skills.activate_proficiencies(2, [
					"Athletics",
					"Insight",
					"Intimidation",
					"Medicine",
					"Persuasion",
					"Religion",
					])
				char.skills.Simple_Weapons.set_proficiency()
				char.skills.Martial_Weapons.set_proficiency()
				char.skills.Light.set_proficiency()
				char.skills.Medium.set_proficiency()
				char.skills.Heavy.set_proficiency()
				char.skills.Shields.set_proficiency()
			elif char.character_class == "Bard":
				char.skills.Simple_Weapons.set_proficiency()
				char.skills.Light.set_proficiency()

				char.skills.Musical_Instrument.set_proficiency()
				char.skills.activate_proficiencies(3, [
					"Athletics",
					'Acrobatics',
					'Sleight of Hand',
					'Stealth',
					'Arcana',
					'History',
					'Investigation',
					'Nature',
					'Religion',
					'Animal Handling',
					'Insight',
					'Medicine',
					'Perception',
					'Survival',
					'Deception',
					'Intimidation',
					'Performance',
					'Persuasion',

					])
				if char.level >= 2:
					char.skills.activate_expertise(
						2,
						char.skills.get_proficient_skills()
						)
					char.skills.activate_jack_of_all_trades()
					if char.level >= 9:
						char.skills.activate_expertise(
							2,
							char.skills.get_proficient_skills()
							)
			elif char.character_class == "Monk":
				char.skills.Unarmed_Monk.set_proficiency()
				char.skills.Simple_Weapons.set_proficiency()
				char.skills.Light_Weapons.set_proficiency()
				char.skills.activate_proficiencies(2, [
					"Acrobatics",
					"Athletics",
					"History",
					"Insight",
					"Religion",
					"Stealth",
					])

				char.skills.activate_proficiencies(1, [
					"Musical Instrument",
					"Alchemist's Supplies",
					"Brewer's Supplies",
					"Calligrapher's Supplies",
					"Carpenter's Tools",
					"Cartographer's Tools",
					"Cobbler's Tools",
					"Cook's Utensils",
					"Glassblower's Tools",
					"Jeweler's Tools",
					"Leatherworker's Tools",
					"Mason's Tools",
					"Painter's Supplies",
					"Potter's Tools",
					"Smith's Tools",
					"Tinker's Tools",
					"Weaver's Tools",
					"Woodcarver's Tools",
					])
			elif char.character_class == "Druid":
				char.skills.Light.set_proficiency()
				char.skills.Shields.set_proficiency()
				char.skills.Simple_Weapons.set_proficiency()
				char.skills.Herbalism_Kit.set_proficiency()
				char.skills.Unarmed_Monk.set_proficiency()
				char.skills.activate_proficiencies(2, [
					"Arcana",
					"Animal Handling",
					"Insight",
					"Medicine",
					"Nature",
					"Perception",
					"Religion",
					"Survival",
					])
			elif char.character_class == "Warlock":
				char.skills.Simple_Weapons.set_proficiency()
				char.skills.Light.set_proficiency()
				char.skills.activate_proficiencies(2, [
					"Arcana",
					"Deception",
					"History",
					"Intimidation",
					"Investigation",
					"Nature",
					"Religion",
					])
			elif char.character_class == "Sorcerer":
				char.skills.Simple_Weapons.set_proficiency()
				char.skills.activate_proficiencies(2, [
					"Arcana",
					"Deception",
					"Insight",
					"Intimidation",
					"Persuasion",
					"Religion",
					])
			elif char.character_class == "Barbarian":
				char.skills.activate_proficiencies(2, [
					"Animal Handling",
					"Athletics",
					"Intimidation",
					"Nature",
					"Perception",
					"Survival",
					])
				char.skills.Simple_Weapons.set_proficiency()
				char.skills.Martial_Weapons.set_proficiency()
				char.skills.Light.set_proficiency()
				char.skills.Medium.set_proficiency()
				char.skills.Shields.set_proficiency()
				char.skills.Unarmed_Barb.set_proficiency()

		return

	def set_Objects(char):
		from AtlasInventarium.Grimoire_of_Objects import setObjects
		return setObjects(char)



#        if char.skills.Heavy.is_proficient():
#            best_armor_class = max(best_armor_class, char.equipment.HeavyArmor().armor_class)
#        elif char.skills.Medium.is_proficient():
#            best_armor_class = max(best_armor_class, char.equipment.MediumArmor(Modifier(char.abilities.DEX)).armor_class)
#        elif char.skills.Light.is_proficient():
#            best_armor_class = max(best_armor_class, char.equipment.LightArmor(Modifier(char.abilities.DEX)).armor_class)
#        char.AC = best_armor_class
