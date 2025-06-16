
import random

from AtlasOfForge.Grimoire_of_Objects import Weapon

def Ranged(self, DEX_mod, STR_mod):
	Dart = Weapon(
		name = "Darts", weight=5, value=1, quantity=20,
		rarity="Common",
		Mod= max(DEX_mod,STR_mod),
		N = 1, D=4,
		description="",
		mastery = "Vex",
		Type = "Piercing. 20/60 thrown range. Light. Finesse.")

	Dagger = Weapon(
		name = "Daggers",
		weight=5, value=10, quantity=5,
		rarity="Common",
		Mod= max(DEX_mod,STR_mod),
		N = 1, D=4,
		description="",
		mastery = "Nick",
		Type = "Piercing. 20/60 thrown range. Light. Finesse.")

	Javelin = Weapon(
		name = "Javelins", weight=8, value=2, quantity=4,
		rarity="Common",
		Mod= STR_mod,
		N = 1, D=6,
		description="",
		mastery = "Slow",
		Type = "Piercing. 30/120 thrown range.")

	Light_hammer = Weapon(
		name = "Light Hammers",
		weight = 8,
		value = 8,
		quantity = 4,
		rarity = "Common",
		Mod= STR_mod,
		N = 1, D=4,
		description="",
		mastery = "Nick",
		Type = "Bludgeoning. 20/60 thrown range. Light.")
	Handaxe = Weapon(
		name = "Handaxes",
		weight = 8,
		value = 20,
		quantity = 4,
		rarity="Common",
		Mod= STR_mod,
		N = 1, D=6,
		description="",
		mastery = "Vex",
		Type = "Slashing. 20/60 thrown range. Light.")
	Spear = Weapon(
		name = "Spear",
		value = 1,
		weight = 3,
		quantity = 1,
		rarity="Common",
		Mod= STR_mod,
		N = 1, D=6,
		description="",
		mastery = "Sap",
		Type = "Piercing. 20/60 thrown range. Versatile(1d8).")

	Crossbow_light = Weapon(
		name = "Light Crossbow",
		N = 1, D=8,
		weight = 5,
		quantity = 1,
		value = 25,
		rarity="Common",
		Mod= STR_mod,
		description="",
		mastery = "Slow",
		Type = "Piercing. 80/320 range. Ammunition. Loading. Two-Handed. ")

	Shortbow = Weapon(
		name = "Shortbow",
		N = 1, D=6,
		weight = 2,
		quantity = 1,
		value = 25,
		rarity="Common",
		Mod= STR_mod,
		description="",
		mastery = "Vex",
		Type = "Piercing. 80/320 range. Ammunition. Two-Handed. ")

	Sling = Weapon(
		name = "Sling",
		N = 1, D = 4,
		weight = 0,
		quantity = 1,
		value = 0.1,
		rarity="Common",
		Mod= STR_mod,
		description="",
		mastery = "Slow",
		Type = "Bludgeoning. 30/120 range. Bullet. Two-Handed. ")

	rangeds = []
	for item in [Dart, Dagger, Javelin, Light_hammer, Handaxe, Spear, Crossbow_light, Shortbow, Sling]:
		if item.value < self.purse:
			rangeds.append(item)
	ranged = random.choice(rangeds)
	self.purse -= ranged.value
	return ranged

def Melee(self, DEX_mod, STR_mod):

	Dagger = Weapon(
		name = "Dagger",
		weight=1, value=2, quantity=1,
		rarity="Common",
		Mod= max(DEX_mod,STR_mod),
		N = 1, D=4,
		description="",
		mastery = "Nick",
		Type = "Piercing. 20/60 thrown range. Light. Finesse.")

	Greatclub = Weapon(
		name = "Greatclub",
		weight=10, value=0.2, quantity=1,
		rarity="Common",
		Mod= STR_mod,
		N= 1, D= 8,
		description="",
		mastery = "Push",
		Type = "Bludgeoning. Two-Handed.")

	Handaxe = Weapon(
		name = "Handaxe",
		weight = 2,
		value = 5,
		quantity = 1,
		rarity= "Common",
		Mod= STR_mod,
		N= 1, D= 6,
		description="",
		mastery = "Vex",
		Type = "Slashing. 20/60 thrown range. Light.")

	Javelin = Weapon(
		name = "Javelins", weight=8, value=2, quantity=4,
		rarity="Common",
		Mod= STR_mod,
		N= 1, D= 6,
		description="",
		mastery = "Slow",
		Type = "Piercing. 30/120 thrown range.")

	Light_hammer = Weapon(
		name = "Light Hammers",
		weight = 2,
		value = 2,
		quantity = 1,
		rarity = "Common",
		Mod= STR_mod,
		N = 1, D=4,
		description="",
		mastery = "Nick",
		Type = "Bludgeoning. 20/60 thrown range. Light.")

	Mace = Weapon(
		name= "Light Hammers",
		weight= 4,
		value= 0.2,
		quantity= 1,
		rarity= "Common",
		Mod= STR_mod,
		N= 1, D= 6,
		description= "",
		mastery= "Sap",
		Type= "Bludgeoning.")

	Quarterstaff = Weapon(
		name= "Quarterstaff",
		weight= 4,
		value= 0.2,
		quantity= 1,
		rarity= "Common",
		Mod= STR_mod,
		N= 1, D= 6,
		description= "Versatile (1d8)",
		mastery= "Topple",
		Type= "Bludgeoning.")

	Sickle = Weapon(
		name= "Sickle",
		N= 1, D= 4,
		weight= 2,
		value= 1,
		quantity= 1,
		rarity= "Common",
		Mod= STR_mod,
		description= "Versatile (1d8)",
		mastery= "Nick",
		Type= "Slashing. Light")

	Spear = Weapon(
		name = "Spear",
		value = 1,
		weight = 3,
		quantity = 1,
		rarity="Common",
		Mod= STR_mod,
		N = 1, D=6,
		description="",
		mastery = "Sap",
		Type = "Piercing. 20/60 thrown range. Versatile(1d8).")

	melees = []
	for item in [Dagger, Greatclub, Handaxe, Javelin, Light_hammer, Mace, Quarterstaff,
		Sickle, Spear]:
		if item.value < self.purse:
			melees.append(item)
	melee = random.choice(melees)
	self.purse -= ranged.value
	return melee

def Melee_Martial(self, DEX_mod, STR_mod):

	Dagger = Weapon(
		name = "Dagger",
		weight=1, value=2, quantity=1,
		rarity="Common",
		Mod= max(DEX_mod,STR_mod),
		N = 1, D=4,
		description="",
		mastery = "Nick",
		Type = "Piercing. 20/60 thrown range. Light. Finesse.")

	Greatclub = Weapon(
		name = "Greatclub",
		weight=10, value=0.2, quantity=1,
		rarity="Common",
		Mod= STR_mod,
		N= 1, D= 8,
		description="",
		mastery = "Push",
		Type = "Bludgeoning. Two-Handed.")

	Handaxe = Weapon(
		name = "Handaxe",
		weight = 2,
		value = 5,
		quantity = 1,
		rarity= "Common",
		Mod= STR_mod,
		N= 1, D= 6,
		description="",
		mastery = "Vex",
		Type = "Slashing. 20/60 thrown range. Light.")

	Javelin = Weapon(
		name = "Javelins", weight=8, value=2, quantity=4,
		rarity="Common",
		Mod= STR_mod,
		N= 1, D= 6,
		description="",
		mastery = "Slow",
		Type = "Piercing. 30/120 thrown range.")

	Light_hammer = Weapon(
		name = "Light Hammers",
		weight = 2,
		value = 2,
		quantity = 1,
		rarity = "Common",
		Mod= STR_mod,
		N = 1, D=4,
		description="",
		mastery = "Nick",
		Type = "Bludgeoning. 20/60 thrown range. Light.")

	Mace = Weapon(
		name= "Light Hammers",
		weight= 4,
		value= 0.2,
		quantity= 1,
		rarity= "Common",
		Mod= STR_mod,
		N= 1, D= 6,
		description= "",
		mastery= "Sap",
		Type= "Bludgeoning.")

	Quarterstaff = Weapon(
		name= "Quarterstaff",
		weight= 4,
		value= 0.2,
		quantity= 1,
		rarity= "Common",
		Mod= STR_mod,
		N= 1, D= 6,
		description= "Versatile (1d8)",
		mastery= "Topple",
		Type= "Bludgeoning.")

	Sickle = Weapon(
		name= "Sickle",
		N= 1, D= 4,
		weight= 2,
		value= 1,
		quantity= 1,
		rarity= "Common",
		Mod= STR_mod,
		description= "Versatile (1d8)",
		mastery= "Nick",
		Type= "Slashing. Light")

	Spear = Weapon(
		name = "Spear",
		value = 1,
		weight = 3,
		quantity = 1,
		rarity="Common",
		Mod= STR_mod,
		N = 1, D=6,
		description="",
		mastery = "Sap",
		Type = "Piercing. 20/60 thrown range. Versatile(1d8).")

	melees = []
	for item in [Dagger, Greatclub, Handaxe, Javelin, Light_hammer, Mace, Quarterstaff,
		Sickle, Spear]:
		if item.value < self.purse:
			melees.append(item)
	melee = random.choice(melees)
	self.purse -= ranged.value
	return melee

def Ranged_Martial(self, DEX_mod, STR_mod):
	Dart = Weapon(
		name = "Darts", weight=5, value=1, quantity=20,
		rarity="Common",
		Mod= max(DEX_mod,STR_mod),
		N = 1, D=4,
		description="",
		mastery = "Vex",
		Type = "Piercing. 20/60 thrown range. Light. Finesse.")

	Dagger = Weapon(
		name = "Daggers",
		weight=5, value=10, quantity=5,
		rarity="Common",
		Mod= max(DEX_mod,STR_mod),
		N = 1, D=4,
		description="",
		mastery = "Nick",
		Type = "Piercing. 20/60 thrown range. Light. Finesse.")

	Javelin = Weapon(
		name = "Javelins", weight=8, value=2, quantity=4,
		rarity="Common",
		Mod= STR_mod,
		N = 1, D=6,
		description="",
		mastery = "Slow",
		Type = "Piercing. 30/120 thrown range.")

	Light_hammer = Weapon(
		name = "Light Hammers",
		weight = 8,
		value = 8,
		quantity = 4,
		rarity = "Common",
		Mod= STR_mod,
		N = 1, D=4,
		description="",
		mastery = "Nick",
		Type = "Bludgeoning. 20/60 thrown range. Light.")
	Handaxe = Weapon(
		name = "Handaxes",
		weight = 8,
		value = 20,
		quantity = 4,
		rarity="Common",
		Mod= STR_mod,
		N = 1, D=6,
		description="",
		mastery = "Vex",
		Type = "Slashing. 20/60 thrown range. Light.")
	Spear = Weapon(
		name = "Spear",
		value = 1,
		weight = 3,
		quantity = 1,
		rarity="Common",
		Mod= STR_mod,
		N = 1, D=6,
		description="",
		mastery = "Sap",
		Type = "Piercing. 20/60 thrown range. Versatile(1d8).")

	Crossbow_light = Weapon(
		name = "Light Crossbow",
		N = 1, D=8,
		weight = 5,
		quantity = 1,
		value = 25,
		rarity="Common",
		Mod= STR_mod,
		description="",
		mastery = "Slow",
		Type = "Piercing. 80/320 range. Ammunition. Loading. Two-Handed. ")

	Shortbow = Weapon(
		name = "Shortbow",
		N = 1, D=6,
		weight = 2,
		quantity = 1,
		value = 25,
		rarity="Common",
		Mod= STR_mod,
		description="",
		mastery = "Vex",
		Type = "Piercing. 80/320 range. Ammunition. Two-Handed. ")

	Sling = Weapon(
		name = "Sling",
		N = 1, D = 4,
		weight = 0,
		quantity = 1,
		value = 0.1,
		rarity="Common",
		Mod= STR_mod,
		description="",
		mastery = "Slow",
		Type = "Bludgeoning. 30/120 range. Bullet. Two-Handed. ")

	rangeds = []
	for item in [Dart, Dagger, Javelin, Light_hammer, Handaxe, Spear, Crossbow_light, Shortbow, Sling]:
		if item.value < self.purse:
			rangeds.append(item)
	ranged = random.choice(rangeds)
	self.purse -= ranged.value
	return ranged
