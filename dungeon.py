import random

BaseEncounterLevel = 5

def Dungeon():
	dungeon = f"Driven by your adventures, you come to a mysterious location: {Entrance()}\n"
	dungeon += f"If you decide to enter you find your way through a passage that {Passage()}\n"
	print(dungeon)

def Entrance():
	Entrances = [
		"A tower in a wild forest",
		"A ruined watchtower in a wild forest",
		"An old castle, long abandoned.",
		"A brand new castle, but seems abandoned.",
		"The ruins of a city.",
		"The ruins of a once-prosperous city.",
		"A destroyed temple.",
		"A destroyed shrine.",
		"A destroyed monastery.",
		"A destroyed temple devoted to an evil deity.",
		"A destroyed shrine devoted to an evil deity.",
		"A destroyed monastery devoted to an evil deity.",
		"The cellar of a ruined noble's manor.",
		"The cellar of a ruined noble's villa.",
		"The cellar of a ruined noble's palace.",
		"A desolated cemetery.",
		"A forgotten mausoleum.",
		"A road of stones.",
		"A trail in the forest.",
		"A path leading into the forest.",
		"A concealed entrance into an underground dungeon.",
		]
	return random.choice(Entrances)

def Passage():
	Passages = [
		f"continues Straight for 30 ft. Then the corridor {Corridor()}",
		f"continues Straight, but to the right there's a side passage. \nThis passage {Corridor()} \nThe main corridor {Corridor()}",
		f"continues Straight, but to the left there's a side passage. \nThis passage {Corridor()} \nThe main corridor {Corridor()}",
		f"comes to an intersection in T. \nTo the right it {Corridor()} \nTo the left it {Corridor()}",
		f"comes to an intersection in Y. \nTo the right it {Corridor()} \nTo the left it {Corridor()}",
		]
	return random.choice(Passages)

def Corridor():
	Corridors = [
		f"continues Straight, into darkness. It eventually dead-ends at a door. {Door()}",
		f"continues Straight, into darkness. It eventually dead-ends at a door.{Door()}",
		f"continues Straight, but to the right there's a door. {Door()}",
		f"continues Straight, but to the left there's a door. {Door()}",
		f"abruptly turns left, to a door: {Door()}",
		f"abruptly turns right, to a door: {Door()}",
		f"slightly turns left, eventually finding a door:\n {Door()}",
		f"slightly turns right, eventually finding a door:\n {Door()}",
		f"emerges into a chamber:\n {Room()}",
		f"ascends through stairs:\n {Stair()}",
		f"descends through stairs:\n {Stair()}",
		f"you get to a dead end.",
		f"as you advance through it, you come to find {Event()}",
		]
	return random.choice(Corridors)

def Door():
	Doors = [
		f"An open archway.",
		f"A wooden door that opens freely.",
		f"A wooden door. It is stuck. Roll a DC 16 Strength check to open it.",
		]
	return random.choice(Doors)

def Room():
	Rooms = [
		f"A circular hall.",
		]
	return random.choice(Rooms)

def Stair():
	Stairs = [
		f"Circular stairs.",
		]
	return random.choice(Stairs)

def Event():
	Events = [
		f"a goblin.",
		]
	return random.choice(Events)


def Condition():
	Conditions = [
		f"a goblin.",
		]
	return random.choice(Conditions)

def DifficultFloor():
	Floors = [
		f"uneven.",
		f"slippery.",
		]
	return random.choice(Floors)

Dungeon()
