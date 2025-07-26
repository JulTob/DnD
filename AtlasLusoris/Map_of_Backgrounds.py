# AtlasLusoris.Map_of_Backgrounds

import random
from AtlasLusoris.Grimoire_of_Features import Feature
from AtlasActorLudi.Grimoire_of_Skills import Char_Skills

# Weighted table
backgrounds = [
				"Acolyte",
				"Artisan",
				"Charlatan",
				"Criminal",
				"Entertainer",
				"Farmer",
				"Guard",
				"Guide",
				"Hermit",
				"Merchant",
				"Noble",
				"Sage",
				"Sailor",
				"Scribe",
				"Soldier",
				"Wayfarer",
				]

BACKGROUND_FEATURES = {
	"Acolyte": Feature(
		name="Shelter of the Faithful",
		description="You and your companions can expect free healing and care at temples.",
		source="Background",
		level=1,
	),
	"Artisan": Feature(
		name="Craftsperson",
		description="You have connections within craft guilds, allowing you access to workshops and specialized tools.",
		source="Background",
		level=1,
	),
	"Charlatan": Feature(
		name="False Identity",
		description="You maintain a convincing second identity, complete with documents, friends, and disguises.",
		source="Background",
		level=1,
		),
	"Criminal": Feature(
		name="Criminal Contact",
		description="You have a reliable contact who acts as a liaison to the criminal underworld.",
		source="Background",
		level=1,
	),
	"Entertainer": Feature(
		name="By Popular Demand",
		description="You can always find a place to perform, earning food and lodging in exchange.",
		source="Background",
		level=1,
	),
	"Farmer": Feature(
		name="Rustic Hospitality",
		description="Common folk gladly offer you food and shelter in exchange for simple labour.",
		source="Background",
		level=1,
	),
	"Guard": Feature(
		name="Watcher’s Eye",
		description="You recognise criminals and law-enforcement factions—and they recognise you.",
		source="Background",
		level=1,
	),
	"Guide": Feature(
		name="Pathfinder",
		description="You can always find safe routes through the wilderness and locate food, water, or shelter.",
		source="Background",
		level=1,
	),
	"Hermit": Feature(
		name="Discovery",
		description="During your isolation you uncovered a unique and powerful secret.",
		source="Background",
		level=1,
	),
	"Merchant": Feature(
		name="Business Acumen",
		description="You can find trade contacts and secure favourable deals, transport, or information.",
		source="Background",
		level=1,
		),
	"Noble": Feature(
		name="Position of Privilege",
		description="People of high birth treat you with deference. You have access to high society.",
		source="Background",
		level=1,
	),
	"Sage": Feature(
		name="Researcher",
		description="If you don’t know a piece of lore, you usually know where to find it.",
		source="Background",
		level=1,
	),
	"Sailor": Feature(
		name="Ship’s Passage",
		description="You can secure free passage on a vessel for yourself and companions in exchange for work.",
		source="Background",
		level=1,
	),
	"Scribe": Feature(
		name="Scholarly Insight",
		description="You have easy access to libraries, archives, and institutions of knowledge.",
		source="Background",
		level=1,
	),
	"Soldier": Feature(
		name="Military Rank",
		description="Your rank lets you invoke authority in military organisations and secure aid or shelter.",
		source="Background",
		level=1,
	),
	"Wayfarer": Feature(
		name="Wayfarer",
		description="You grew up on the streets surrounded by similarly ill-fated castoffs, a few of them friends and a few of them rivals. You slept where you could and did odd jobs for food. At times, when the hunger became unbearable, you resorted to theft. Still, you never lost your pride and never abandoned hope. Fate is not yet finished with you.",
		source="Background",
		level=1,
	),
}

def background_features(name: str):
	"""Return features associated with a specific background."""
	feat = BACKGROUND_FEATURES.get(name)
	return [feat] if feat else []


def ApplyBackground(char):
		"""Apply full background configuration based on character's background."""
		from AtlasLusoris.Grimoire_of_Features import Lucky

		background_name = char.background

		# Background data configuration
		background_data = {
		"Wayfarer": {
				"ability_scores": {"DEX": 1, "WIS": 1, "CHA": 1},
				"feat": Lucky(),
				"skills": ["Insight", "Stealth"],
				"tools": ["Thieves_Tools"],
				"equipment_choices": [
					{
						"description": "Option A",
						"items": ["Dagger", "Dagger", "Thieves' Tools", "Gaming Set", "Bedroll", "Pouch", "Pouch", "Traveler's Clothes"],
						"gold": 16,
						},
					{
						"description": "Option B",
						"items": [],
						"gold": 50,
						},
					],
				},
			}
		bg = background_data.get(background_name)

		if not bg:
			from Minion import Warning
			Warning(f"Background '{background_name}' not found.")
			return

		# Apply Ability Score increases
		for stat, bonus in bg.get("ability_scores", {}).items():
			setattr(char.AS, stat, getattr(char.AS, stat) + bonus)

		# Apply Feat
		feat = bg.get("feat")
		if feat:
			char.features.append(feat)

		# Set Skill Proficiencies
		for skill_name in bg.get("skills", []):
			getattr(char.skills, skill_name).set_proficiency()

		# Set Tool Proficiencies
		for tool_name in bg.get("tools", []):
			if hasattr(char.skills, tool_name):
				getattr(char.skills, tool_name).set_proficiency()

		from Minion import Inform
		Inform(f"{char.name} gains background '{background_name}' with features: "
			   f"{feat.name if feat else 'None'}, Skills: {bg.get('skills')}.")
