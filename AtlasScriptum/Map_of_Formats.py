from Minion import Inform, Warning, Initialized, News

Initialized("Map of Formats initialized")

def Entry(
	title: str = "",
	definition: str = "",
	description: str = "",
	speech: str = ""
	) -> str:
	"""
	Creates an HTML-formatted entry
		with a title, definition, and description.
	"""

	if not title:
		Warning("<Entry<>: Title is empty. Entry may not render as intended.")
		result = ""
	else:
		result = f"<b>{title}</b>"
	if definition:
		if not description:
			result = f"<b>{result}:</b> <i>{definition}</i>"
		else:
			result = (f"<b>{result}:</b>\n" +
			f'<div class="bc4">{description}</div>' +
			f"<i>{definition}</i>")

	#News(f"Creating an entry for '{title}' with definition and description: \n\t{result}")

	return result

def Type(npc) -> str:
	#Initialized("<< Map of Formats: <Type<>")
	""" Generate a description string
	rom NPC details. """
	try:
		pc = npc.NPCfy
	except:
		pc = npc
	text = f"{pc.race} {pc.subrace} {pc.archetype} {pc.alignment}"
	text = " ".join(text.split()).title()

	#Inform(f"Generating type description from NPC details: {text}")

	return text
