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

def Genus(lusor):
	"""
	Returns a descriptive genus string for a lusor (NPC or PC).

	- If lusor is already a string, return it.
	- If it has a `.genus` property, use that.
	- Else, build it manually from attributes.
	"""
	# Case 1: already a string
	if isinstance(lusor, str):
		return lusor

	# Case 2: has a genus property
	if hasattr(lusor, "genus"):
		try:
			return lusor.genus
		except Exception as e:
			pass  # fallback to manual if it fails

	# Case 3: build manually (best-effort fallback)
	archetype = getattr(lusor, "archetype", None) or getattr(lusor, "char_class", "")
	attributes = [
		str(getattr(lusor, "race", "") or ""),
		str(getattr(lusor, "subrace", "") or ""),
		str(archetype),
		str(getattr(lusor, "gender", "") or ""),
		str(getattr(lusor, "alignment", "") or ""),
	]
	return " , ".join(filter(None, attributes))
