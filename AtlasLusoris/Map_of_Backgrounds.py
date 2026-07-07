# AtlasLusoris.Map_of_Backgrounds
import random
from AtlasLusoris.Grimoire_of_Features import Feature
from AtlasActorLudi.Grimoire_of_Skills import Char_Skills
from Minion import guardian

from AtlasLusoris.Grimoire_of_Features import (
		Feature,
		Lucky,
		Crafter,
		SkilledFeat,
		AlertFeat,
		Musician,
		ToughFeat,
		HealerFeat,
		MagicInitiateCleric,
		MagicInitiateDruid,
		MagicInitiateWizard,
		TavernBrawler,
		SavageAttacker,
		)

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
		description=(
			"You grew up on the streets surrounded by similarly ill-fated castoffs, a few of them friends and a few of "
			"them rivals. You slept where you could and did odd jobs for food. At times, when the hunger became "
			"unbearable, you resorted to theft. Still, you never lost your pride and never abandoned hope. Fate is not "
			"yet finished with you."
		),
		source="Background",
		level=1,
	),
}


class Background:
	"""Container for background data and application logic."""

	def __init__(self, 
		name, 
		skills=None, 
		tools_or_languages=None, 
		feat=None, 
		feature=None
		):
		self.name = name
		self.skills = skills or ()
		self.tools_or_languages = tools_or_languages or ()
		self.feat = feat
		self.feature = feature

	def apply(self, char):
		boosts = random.choice([(2, 1), (1, 1, 1)])
		abilities = random.sample(["STR", "DEX", "CON", "INT", "WIS", "CHA"], len(boosts))
		for ability, bonus in zip(abilities, boosts):
			setattr(char.AS, ability, getattr(char.AS, ability) + bonus)

		for skill in self.skills:
			prof = getattr(char.skills, skill, None)
			if prof:
				prof.set_proficiency()

		if self.tools_or_languages:
			choice = random.choice(self.tools_or_languages)
			prof = getattr(char.skills, choice, None)
			if prof:
				prof.set_proficiency()

		if self.feature:
			self.feature(char)
			char.features.append(self.feature)

		if self.feat:
			feat_obj = self.feat()
			feat_obj(char)
			char.features.append(feat_obj)

origin_feat_map = {
	"Acolyte": MagicInitiateCleric,
	"Artisan": Crafter,
	"Charlatan": SkilledFeat,
	"Criminal": AlertFeat,
	"Entertainer": Musician,
	"Farmer": ToughFeat,
	"Guard": AlertFeat,
	"Guide": MagicInitiateDruid,
	"Hermit": HealerFeat,
	"Merchant": Lucky,
	"Noble": SkilledFeat,
	"Sage": MagicInitiateWizard,
	"Sailor": TavernBrawler,
	"Scribe": SkilledFeat,
	"Soldier": SavageAttacker,
	"Wayfarer": Lucky,
}


BACKGROUND_REGISTRY = {
	name: Background(
		name=name,
		feat=origin_feat_map.get(name),
		feature=BACKGROUND_FEATURES.get(name),
	)
	for name in backgrounds
}

BACKGROUND_REGISTRY["Wayfarer"] = Background(
	name="Wayfarer",
	skills=("Stealth", "Survival"),
	tools_or_languages=("Thieves_Tools", "Gaming_Set", "Language"),
	feat=origin_feat_map["Wayfarer"],
	feature=BACKGROUND_FEATURES["Wayfarer"],
)

@guardian
def ApplyBackground(char):
	"""
	Apply full background configuration based on the character's background.
	"""
	background_name = getattr(char, "background", None)
	if not background_name:
		raise Exception("No background name found")

	background = BACKGROUND_REGISTRY.get(background_name)
	if not background:
		raise Exception("No background found")

	background.apply(char)
