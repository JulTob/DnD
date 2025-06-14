# Shelf_of_Armors.py

from Compass_of_ArmorType import ArmorType, check_if_ArmorType
from Compass_of_Rarity import Rarity, check_if_Rarity
from Grimoire_of_Objects import Inventory
from Objects import Armor
import random

chain_mail = Armor(name = "Chain Mail",
	weight=55,
	value=75,
	quantity=1,
	rarity=Rarity.COMMON,
	armor_type =ArmorType.HEAVY,
	armor_class=16,
	Dex=0,
	description="The wearer has Disadvantage on Dexterity (Stealth) checks.")
plate_armor = Armor(name = "Plate Armor",
	weight=65,
	value=1500,
	quantity=1,
	armor_type =ArmorType.HEAVY,
	rarity=Rarity.COMMON,
	armor_class=18,
	Dex=0,
	description="The wearer has Disadvantage on Dexterity (Stealth) checks.")
ring_mail = Armor(name = "Ring Mail",
	weight=40,
	value=30,
	quantity=1,
	armor_type =ArmorType.HEAVY,
	rarity=Rarity.COMMON,
	armor_class=14,
	Dex=0,
	description="The wearer has Disadvantage on Dexterity (Stealth) checks.")
splint_armor = Armor(name = "Splint Armor",
	weight=60,
	value=200,
	quantity=1,
	rarity=Rarity.COMMON,
	armor_type = ArmorType.HEAVY,
	armor_class=17,
	Dex=0,
	description="The wearer has Disadvantage on Dexterity (Stealth) checks.")

Heavy_Armors = [
	chain_mail,
	plate_armor,
	ring_mail,
	splint_armor,
	]

scale_mail = Armor(name = "Scale Mail",
	weight=45,
	value=50,
	quantity=1,
	rarity=Rarity.COMMON,
	armor_type =ArmorType.MEDIUM,
	armor_class=14,
	Dex=min(2,Dex),
	description="The wearer has Disadvantage on Dexterity (Stealth) checks.")
hide_armor = Armor(name = "Hide Armor",
	weight=12,
	value=10,
	quantity=1,
	rarity=Rarity.COMMON,
	armor_type =ArmorType.MEDIUM,
	armor_class=12,
	Dex=min(2,Dex),
	description="")
half_plate_armor = Armor(name = "Half Plate Armor",
	weight=40,
	value=750,
	quantity=1,
	rarity=Rarity.COMMON,
	armor_type =ArmorType.MEDIUM,
	armor_class=15,
	Dex=min(2,Dex),
	description="The wearer has Disadvantage on Dexterity (Stealth) checks.")
chain_shirt = Armor(name = "Chain Shirt",
	weight=20,
	value=50,
	quantity=1,
	rarity=Rarity.COMMON,
	armor_type =ArmorType.MEDIUM,
	armor_class=13,
	Dex=min(2,Dex),
	description="")
breastplate = Armor(name = "Breastplate",
	weight=20,
	value=400,
	quantity=1,
	rarity=Rarity.COMMON,
	armor_type =ArmorType.MEDIUM,
	armor_class=14,
	Dex=min(2,Dex),
	description="")

Medium_Armors = [
	scale_mail,
	hide_armor,
	half_plate_armor,
	chain_shirt,
	breastplate,
	]

studded_leather_armor = Armor(name = "Studded Leather Armor",
	weight=13,
	value=45,
	quantity=1,
	rarity=Rarity.COMMON,
	armor_type =ArmorType.LIGHT,
	armor_class=12,
	Dex=Dex,
	description="")
padded_armor = Armor(name = "Padded Armor",
	weight=8,
	value=5,
	quantity=1,
	rarity=Rarity.COMMON,
	armor_type =ArmorType.LIGHT,
	armor_class=11,
	Dex=Dex,
	description="The wearer has Disadvantage on Dexterity (Stealth) checks.")
leather_armor = Armor(name = "Leather Armor",
	weight=8,
	value=5,
	quantity=1,
	rarity=Rarity.COMMON,
	armor_type =ArmorType.LIGHT,
	armor_class=11,
	Dex=Dex,
	description="")

Light_Armors = [
	studded_leather_armor,
	padded_armor,
	leather_armor,
	]

simple_clothes = Armor(name = "Simple Clothes",
			weight=5,
			value=10,
			quantity=1,
			rarity=Rarity.COMMON,
			armor_type =ArmorType.UNARMORED,
			armor_class=10,
			Dex=Dex,
			description="")

fancy_clothes = Armor(name = "Fancy Clothes",
			weight=5,
			value=15,
			quantity=1,
			rarity=Rarity.COMMON,
			armor_type =ArmorType.UNARMORED,
			armor_class=10,
			Dex=Dex,
			description="")
Clothes = [
	simple_clothes,
	fancy_clothes,
	]
def GetHeavyArmor(Inventory, Dex = 0):
	"""Selects a Heavy Armor item within budget and updates purse."""
	possible_armors = []
	for item in Heavy_Common_Armors:
		if item.value < Inventory.purse:
			possible_armors.append(item)
	if not possible_armors:
		print("\nDark Lord! No Heavy Armor is available in the shelf!\n")
		return None
	armor = random.choice(possible_armors)
	Inventory.purse -= armor.value
	return armor

def MediumArmor(Inventory, Dex = 0):
	armors = []
	for item in Medium_Armors:
		if item.value < Inventory.purse:
			armors.append(item)
	if not armors:
		print("\nDark Lord! No Medium Armor is available in the shelf!\n")
		return None
	armor = random.choice(armors)
	Inventory.purse -= armor.value
	return armor

def LightArmor(Inventory, Dex = 0):
	armors = []
	for item in Light_Armors:
		if item.value < Inventory.purse:
			armors.append(item)
	if not armors:
		print("\nDark Lord! No Light Armor is available in the shelf!\n")
		return None
	armor = random.choice(armors)
	Inventory.purse -= armor.value
	return armor

def Clothes(Inventory, Dex = 0):

	armors = []
	for item in Clothes:
		if item.value < Inventory.purse:
			armors.append(item)
	armor = random.choice(armors)
	Inventory.purse -= armor.value
	return armor
