# AtlasLusoris/Classes/data.py

def classes():
	return [
	'Fighter',	'Wizard',	'Rogue',	'Cleric',
	'Ranger',	'Paladin',	'Bard',		'Monk',
	'Druid',	'Warlock',	'Sorcerer',	'Barbarian',
	]

CLASSES = classes()

def subclasses():
	return {
	'Fighter': [
		"Champion", "Battle Master", "Eldritch Knight", "Samurai"],
	'Wizard': [
		"Evoker", "Illusion", "Necromancy", "Divination",
		"Abjuration",
		],
	'Rogue': [
		"Assassin",	 "Arcane Trickster", "Thief", "Swashbuckler",	],
	'Cleric': [
		"Knowledge", "War", "Tempest", "Life",
		"Light", "Trickery", "Nature", "Forge",
		"Grave", ],
	'Ranger': [
		"Hunter", "Beast Master", "Gloom Stalker",	"Horizon Walker" ],
	'Paladin': [
		"Devotion", "Oathbreaker", "Ancients",	 "Vengeance", ],
	'Bard': [
		"Lore",	 "Valor", "Glamour", "Swords", ],
	'Monk': [
		"Elements", "Open Hand", "Shadow", "Mercy", ],
	'Druid': [
		"Moon", "Land", "Sea",	"Stars", ],
	'Warlock': [
		"Great Old One", "Fiend", "Archfey", "Celestial", "Genie" ],
	'Sorcerer': [
		"Draconic",	"Wild Magic", "Divine Soul", "Shadow Magic", ],
	'Barbarian': [
		"Berserker", "Wild Heart", "Storm Herald", ],
	}

SUBCLASSES = subclasses()
