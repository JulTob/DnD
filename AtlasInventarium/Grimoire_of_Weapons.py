import random
from Minion import Initialized, Alert, Inform, Warning, News

try:
	from AtlasScriptum.Map_of_Formats import Entry
	from AtlasLudus.Map_of_Dice import Dice
	from AtlasActorLudi.Map_of_Scores import PB
	from AtlasAlusoris.Grimoire_of_NPC import NPC
	News("Atlas for the Grimoire of Weapons [Inventarium] procured")
except ImportError as e:
	Alert(f"Couldn't locate imports in the Grimoire of Weapons:", e)


class Weapon:
	def __init__(self,name,damage_intensity=1,damage_dice='d4',attack_modifier= 0,damage_type= "Bludgeoning",range_distance="",properties=""):
		self.name = name
		self.damage_intensity = damage_intensity
		self.damage_dice = 		damage_dice
		self.attack_modifier = 	attack_modifier
		self.damage_type = 		damage_type
		self.range_distance = 	range_distance
		self.properties = 		properties

	def __str__(self):
		result = f"{self.damage_intensity}{self.damage_dice}"
		if self.attack_modifier:
			result += f"{self.attack_modifier:+}"
		result += f" {self.damage_type}"
		if self.range_distance:
				result += f", {self.range_distance}"
		if self.properties:
				result += f", {self.properties}."
		else:
				result += "."
		return Entry(self.name, result)
