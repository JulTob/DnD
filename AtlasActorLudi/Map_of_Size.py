
import random
from AtlasLudus.Map_of_Dice import Dice

def Sizing(n=3):
	if n <= 1: 	return "Tiny"
	if n == 2:	return "Small"
	if n == 3:	return "Medium"
	if n == 4:	return "Large"
	if n == 5:	return "Huge"
	if n >= 6:	return "Gargantuan"
	return "Medium"

def Sizer(n):
	if n == "Tiny":		return "Small"
	elif n == "Small":	return "Medium"
	elif n == "Medium":	return "Large"
	elif n == "Large":	return "Huge"
	elif n <= "Huge":	return "Gargantuan"
	elif n <= "Gargantuan":	return "Gargantuan"
	else: 				return "Gargantuan"

def Desizer(n):
	if n == "Tiny":		return "Tiny"
	elif n == "Small":	return "Tiny"
	elif n == "Medium":	return "Small"
	elif n == "Large":	return "Medium"
	elif n <= "Huge":	return "Large"
	elif n <= "Gargantuan":	return "Huge"
	else: 				return "Tiny"

def Size(Type):

	size = 3

	if "Halfling" in Type:
		size = 2
	if "Goblin" in Type:
		size = 2

	if "Giant" in Type:
		size = random.randrange(3, 5)

	return Sizing(size)
