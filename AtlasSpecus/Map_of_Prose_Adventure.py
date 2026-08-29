"""
Procedural prose sketch for a vague-ish DM-facing adventure opener.

Relocated from repo-root ``dungeon.py`` (2026-07-15). Full integration is tracked
under QST-0036 and sidequests in ``Curia/Questae/Open/``.
"""

import random

BaseEncounterLevel = 5


def prologue() -> str:
	"""Return a short random adventure opening (entrance + first passage)."""
	text = f"Driven by your adventures, you come to a mysterious location: {entrance()}\n"
	text += f"If you decide to enter you find your way through a passage that {passage()}\n"
	return text


def Dungeon() -> str:
	"""Legacy entry point — returns the prologue text (formerly printed only)."""
	return prologue()


def entrance() -> str:
	entrance_options = [
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
	return random.choice(entrance_options)


def passage() -> str:
	passage_options = [
		f"continues Straight for 30 ft. Then the corridor {corridor()}",
		f"continues Straight, but to the right there's a side passage. \nThis passage {corridor()} \nThe main corridor {corridor()}",
		f"continues Straight, but to the left there's a side passage. \nThis passage {corridor()} \nThe main corridor {corridor()}",
		f"comes to an intersection in T. \nTo the right it {corridor()} \nTo the left it {corridor()}",
		f"comes to an intersection in Y. \nTo the right it {corridor()} \nTo the left it {corridor()}",
	]
	return random.choice(passage_options)


def corridor() -> str:
	corridor_options = [
		f"continues Straight, into darkness. It eventually dead-ends at a door. {door()}",
		f"continues Straight, into darkness. It eventually dead-ends at a door. {door()}",
		f"continues Straight, but to the right there's a door. {door()}",
		f"continues Straight, but to the left there's a door. {door()}",
		f"abruptly turns left, to a door: {door()}",
		f"abruptly turns right, to a door: {door()}",
		f"slightly turns left, eventually finding a door:\n {door()}",
		f"slightly turns right, eventually finding a door:\n {door()}",
		f"emerges into a chamber:\n {room()}",
		f"ascends through stairs:\n {stair()}",
		f"descends through stairs:\n {stair()}",
		f"you get to a dead end.",
		f"as you advance through it, you come to find {event()}",
	]
	return random.choice(corridor_options)


def door() -> str:
	door_options = [
		"An open archway.",
		"A wooden door that opens freely.",
		"A wooden door. It is stuck. Roll a DC 16 Strength check to open it.",
	]
	return random.choice(door_options)


def room() -> str:
	room_options = [
		"A circular hall.",
	]
	return random.choice(room_options)


def stair() -> str:
	stair_options = [
		"Circular stairs.",
	]
	return random.choice(stair_options)


def event() -> str:
	event_options = [
		"a goblin.",
	]
	return random.choice(event_options)


def condition() -> str:
	condition_options = [
		"a goblin.",
	]
	return random.choice(condition_options)


def difficult_floor() -> str:
	floor_options = [
		"uneven.",
		"slippery.",
	]
	return random.choice(floor_options)


# Legacy PascalCase aliases (prototype API — retire under QST-0036.9)
Entrance = entrance
Passage = passage
Corridor = corridor
Door = door
Room = room
Stair = stair
Event = event
Condition = condition
DifficultFloor = difficult_floor


if __name__ == "__main__":
	random.seed(0)
	text = prologue()
	assert isinstance(text, str) and len(text) > 50, "prologue must return non-trivial text"
	assert "mysterious location" in text
	print("AtlasSpecus.Map_of_Prose_Adventure self-test OK")
	print(text)
