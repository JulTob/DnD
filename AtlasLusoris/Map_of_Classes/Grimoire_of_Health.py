from AtlasLudus.Map_of_Dice import Dice

HIT_DIE_TABLE = {
	"Barbarian": 12,
	"Fighter": 10, "Paladin": 10, "Ranger": 10,
	"Bard": 8, "Cleric": 8, "Druid": 8, "Monk": 8,
	"Rogue": 8, "Warlock": 8,
	"Sorcerer": 6, "Wizard": 6,
	}

def roll_health(character):
	dice_value = health_dice(character.char_class)
	level = character.Level
	for lvl in range(1,character.Level):
		character.base_health += Dice(D=dice_value)


def hit_dice(character):
	if "Barbarian" in character: 	return 12

	elif "Fighter" in character: 	return 10
	elif "Paladin" in character: 	return 10
	elif "Ranger" in character: 	return 10

	elif "Bard" in character: 		return 8
	elif "Cleric" in character: 	return 8
	elif "Druid" in character: 		return 8
	elif "Monk" in character: 		return 8
	elif "Rogue" in character: 		return 8
	elif "Warlock" in character: 	return 8

	elif "Sorcerer" in character: 	return 6
	elif "Wizard" in character: 	return 6
	from AtlasLudus.Map_of_Dice import Dice
	return 5 + Dice(6)





def health_dice(class_name: str) -> int:
	"""
	Return the size of this class’s hit die (e.g. 10 → d10).
	If class not found, roll 6d2 (value 6–12) as a fallback.
	"""
	die = HIT_DIE_TABLE.get(class_name.title())
	if die is None:
		die = Dice(D=2, N=6)             # keeps your quirky fallback
	return die
