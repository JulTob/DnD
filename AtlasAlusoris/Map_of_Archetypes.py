import random

Archetypes = [
		"Artist",
		"Bandit",
		"Barbarian",
		"Bard",
		"Berserker",
		"Charlatan",
		"Cleric",
		"Commoner",
		"Crafter",
		"Criminal",
		"Cultist",
		"Druid",
		"Expert",
		"Explorer",
		"Fighter",
		"Guardian",
		"Healer",
		"Hero",
		"Hunter",
		"Knight",
		"Mage",
		"Mentor",
		"Merchant",
		"Monk",
		"Ninja",
		"Noble",
		"Paladin",
		"Pirate",
		"Priest",
		"Ranger",
		"Rogue",
		"Scholar",
		"Shaman",
		"Soldier",
		"Sorcerer",
		"Spy",
		"Trickster",
		"Traveler",
		"Warlock",
		"Warrior",
		"Witch",
		"Wizard",
		]

def Archetype():

	return random.choice(Archetypes)


def AC_Archetype_modifier(
	archetype="",
	STR = 0,
	DEX = 0,
	CON = 0,
	INT = 0,
	WIS = 0,
	CHA = 0):
	AC_modifiers = {
		"Berserker": CON + STR,
		"Barbarian": CON,
		"Charlatan": CHA,
		"Cleric": 	WIS,
		"Crafter": 	INT,
		"Criminal": INT,
		"Cultist": 	WIS,
		"Druid": 	WIS + CON,
		"Expert": 	INT + WIS + CHA,
		"Explorer": WIS,
		"Fighter" : DEX + STR,
		"Guard": 	STR,
		"Hero":  	STR,
		"Hunter": 	DEX,
		"Knight": 	STR + CON,
		"Mage":  	INT,
		"Monk":		DEX + WIS,
		"Ninja": 	DEX + INT,
		"Noble": 	DEX,
		"Paladin": 	STR + CHA,
		"Pirate":  	DEX,
		"Priest": 	WIS,
		"Ranger": 	WIS,
		"Rogue": 	DEX,
		"Shaman": 	WIS,
		"Soldier": 	STR,
		"Sorcerer": CHA,
		"Spy": 		DEX,
		"Warlock": 	CHA,
		"Warrior": 	STR,
		"Witch": 	WIS,
		"Wizard": 	INT,
		}
	AC = AC_modifiers.get(archetype, 0)
	return AC


def AS_Archetype_modifier(npc):
	creature_type =  npc.archetype

	### Archetype-based Ability Score Adjustments

	if "Artist" in creature_type:
		npc.AS.CHA += Dice(6)
		npc.AS.WIS += Dice(6)
		npc.AS.STR -= Dice(6)

	if "Bandit" in creature_type:
		npc.AS.STR += Dice(6)

	if "Bard" in creature_type:
		npc.AS.CHA += Dice(6)

	if "Barbarian" in creature_type:
		npc.AS.STR += Dice(6,2)
		npc.AS.INT -= Dice(6)

	if "Berserker" in creature_type:
		npc.AS.STR += Dice(6)
		npc.AS.WIS += Dice(6)
		npc.AS.INT -= Dice(6)

	if "Charlatan" in creature_type:
		npc.AS.CHA += Dice(6,2)
		npc.AS.STR -= Dice(6)

	if "Cleric" in creature_type:
		npc.AS.WIS += Dice(6)

	if "Crafter" in creature_type:
		npc.AS.INT += Dice(6)

	if "Criminal" in creature_type:
		npc.AS.INT += Dice(6)
		npc.AS.STR += Dice(6)
		npc.AS.WIS -= Dice(6)

	if "Commoner" in creature_type:
		npc.AS.STR += Dice(6)

	if "Cultist" in creature_type:
		npc.AS.CHA += Dice(6)

	if "Druid" in creature_type:
		npc.AS.WIS += Dice(6)

	if "Expert" in creature_type:
		npc.AS.INT += Dice(6)

	if "Explorer" in creature_type:
		npc.AS.CON += Dice(6)

	if "Guard" in creature_type:
		npc.AS.STR += Dice(6)

	if "Healer" in creature_type:
		npc.AS.WIS += Dice(6)

	if "Hero" in creature_type:
		npc.AS.CHA += Dice(6)

	if "Hunter" in creature_type:
		npc.AS.WIS += Dice(6)

	if "Knight" in creature_type:
		npc.AS.CHA += Dice(3)
		npc.AS.STR += Dice(3)

	if "Scholar" in npc.archetype:
		# Bonus to intelligence and wisdom due to their pursuit of knowledge.
		npc.AS.INT += Dice(6)
		npc.AS.WIS += Dice(3)

	if "Traveler" in npc.archetype:
		# Bonus to intelligence and wisdom due to their pursuit of knowledge.
		npc.AS.CON += Dice(6)
