"""Canonical typed Tool definitions used by Character training."""

from __future__ import annotations

from dataclasses import dataclass, field

from AtlasActorLudi.ProficiencyKit import (
	Capability_Definition,
	Is_Trained,
	)


@dataclass(
		frozen=True,
		slots=True,
		)
class Practice_Section:
	"""One rules-facing paragraph within a learned Practice."""

	title: str
	guidance: str

	def __post_init__(
			section,
			) -> None:
		if not section.title.strip():
			raise ValueError(
				"A Practice section requires a title."
				)

		if not section.guidance.strip():
			raise ValueError(
				"A Practice section requires usable guidance."
				)

	def to_dict(
			section,
			) -> dict[str, str]:
		return {
			"title": section.title,
			"guidance": section.guidance,
			}


@dataclass(
		frozen=True,
		slots=True,
		)
class Practice_Definition:
	"""Immutable guidance attached to one canonical Tool capability."""

	title: str
	flavour: str
	sections: tuple[Practice_Section, ...]
	subject_title: str = ""

	def __post_init__(
			practice,
			) -> None:
		object.__setattr__(
			practice,
			"sections",
			tuple(
				practice.sections
				),
			)

		if not practice.title.strip():
			raise ValueError(
				"A Practice requires a title."
				)

		if not practice.flavour.strip():
			raise ValueError(
				"A Practice requires flavour."
				)

		if not practice.sections:
			raise ValueError(
				"A Practice requires at least one guidance section."
				)

	def to_dict(
			practice,
			) -> dict:
		return {
			"title": practice.title,
			"flavour": practice.flavour,
			"sections": tuple(
				section.to_dict()
				for section in practice.sections
				),
			}


@dataclass(
		frozen=True,
		slots=True,
		)
class Resolved_Practice:
	"""One immutable Practice resolved for a character's trained Tools."""

	definition: Practice_Definition
	subjects: tuple[str, ...] = ()

	def to_dict(
			practice,
			) -> dict:
		data = practice.definition.to_dict()

		if (
			practice.definition.subject_title
			and practice.subjects
			):
			data[ "sections" ] = (
				{
					"title": practice.definition.subject_title,
					"guidance": ", ".join(
						practice.subjects
						),
					},
				*data[ "sections" ],
				)

		return data


@dataclass(
		frozen=True,
		slots=True,
		)
class Tool_Definition(Capability_Definition):
	"""One tool proficiency, separate from physical inventory ownership."""

	ability: str
	category: str
	variant: str = ""
	practice: Practice_Definition | None = field(
		default=None,
		compare=False,
		hash=False,
		repr=False,
		)


def _Practice(
		title: str,
		flavour: str,
		*sections: tuple[str, str],
		subject_title: str = "",
		) -> Practice_Definition:
	return Practice_Definition(
		title=title,
		flavour=flavour,
		sections=tuple(
			Practice_Section(
				title=section_title,
				guidance=guidance,
				)
			for section_title, guidance in sections
			),
		subject_title=subject_title,
		)


def _Tool(
		key: str,
		name: str,
		ability: str,
		category: str,
	*,
	legacy_attribute: str | None = None,
	variant: str = "",
	practice: Practice_Definition | None = None,
	) -> Tool_Definition:
	return Tool_Definition(
		key=key,
		name=name,
		legacy_attribute=(
			legacy_attribute
			or key
			),
		ability=ability,
		category=category,
		variant=variant,
		practice=practice,
		)


Alchemist_Supplies = _Tool(
	"Alchemist_Supplies",
	"Alchemist's Supplies",
	"INT",
	"Artisan",
	practice=_Practice(
		"Alchemy Proficiency",
		(
			"Matter can change. Poison can become medicine, stone can flow, "
			"and fire can be tamed. By the law of equivalence, every "
			"transformation demands something in return. You have learned how "
			"to invite the change without becoming the price."
			),
		(
			"Principles of Transformation",
			(
				"You can identify, separate, concentrate, preserve, neutralize, or "
				"combine substances and their properties. You usually recognize "
				"common materials, reactions, dangers, and potential uses. If "
				"uncertainty requires a check, the DM chooses the Ability and "
				"Difficulty Class. Add your Proficiency Bonus to your roll. If a "
				"relevant Skill proficiency supports your approach, you have "
				"Advantage. For example, identifying and separating an unknown "
				"poison from a noble's wine without destroying the evidence might "
				"require an Intelligence check with a DC of 15. Investigation or "
				"Medicine could support the attempt."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and materials, as determined by your "
				"DM, you might prepare acids, alchemist's fire, oils, perfumes, "
				"pigments, paper, spell components, medicines, poisons, potions, "
				"or elixirs. Your works might burn without air, dissolve only a "
				"chosen substance, preserve a breath or memory, or transform a "
				"creature. Rare elements, forbidden formulae, and the desperate "
				"search for a way to reverse a transformation gone horribly wrong "
				"may each become an adventure of its own."
				),
			),
		),
	)
Brewer_Supplies = _Tool(
	"Brewer_Supplies",
	"Brewer's Supplies",
	"INT",
	"Artisan",
	practice=_Practice(
		"Brewing Proficiency",
		(
			"Within the right vessel, time can spoil or ferment what rests "
			"inside. Time always awakens something. Grain remembers sunlight, "
			"fruit preserves a summer, and a shared cup can turn strangers into "
			"companions, promises into oaths, fear into fury, and waking thought "
			"into vision. You know how to tend that patient, dangerous magic."
			),
		(
			"Read the Cup",
			(
				"You understand fermentation, distillation, ageing, blending, "
				"dosage, and preservation. You usually recognize a drink's "
				"ingredients, origin, quality, adulteration, poison, and likely "
				"effects upon body and mind. If uncertainty requires a check, the "
				"DM chooses the Ability and Difficulty Class. Add your Proficiency "
				"Bonus to your roll. If a relevant Skill proficiency supports your "
				"approach, you have Advantage. For example, adjusting a ceremonial "
				"draught to induce a trance without poisoning its drinkers might "
				"require a Wisdom check with a DC of 15. Medicine or Religion could "
				"support the attempt."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and ingredients, as determined by your "
				"DM, you might prepare beers, wines, spirits, elixirs, antidotes, "
				"poisons, or stranger concoctions. Rare ingredients, forgotten "
				"recipes, and magical brews may become adventures of their own."
				),
			),
		),
	)
Calligrapher_Supplies = _Tool(
	"Calligrapher_Supplies",
	"Calligrapher's Supplies",
	"DEX",
	"Artisan",
	practice=_Practice(
		"Calligraphy Proficiency",
		(
			"Writing teaches words to wait. A spoken word has the life of a "
			"butterfly; once written, it may last forever. A name may outlive "
			"its bearer, and a prayer may cross generations. A single hand can "
			"reveal discipline, grief, authority, or defiance before its meaning "
			"is read. You have learned to give thought a form that endures."
			),
		(
			"The Living Hand",
			(
				"You can compose, copy, illuminate, restore, authenticate, conceal, "
				"or decipher written works. Your deliberate signatures and "
				"flourishes make your writing difficult to alter or imitate. You "
				"usually recognize a text's tradition, age, alterations, purpose, "
				"and what the hand reveals of its writer: discipline or haste, "
				"confidence or fear, coercion, injury, or an influence not entirely "
				"their own. If uncertainty requires a check, the DM chooses the "
				"Ability and Difficulty Class. Add your Proficiency Bonus to your "
				"roll. If a relevant Skill proficiency supports your approach, you "
				"have Advantage. For example, discovering where a dead prophet's "
				"own hand ended and another presence began might require a Wisdom "
				"check with a DC of 15. Insight or Arcana could support the "
				"examination."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and materials, as determined by your "
				"DM, you might create inks, manuscripts, ciphers, contracts, seals "
				"of authorship, sacred copies, or spell scrolls for spells you "
				"already have prepared. Rare inks, forgotten scripts, disputed "
				"contracts, forbidden books, and words someone tried to erase from "
				"history may become adventures of their own."
				),
			),
		),
	)
Woodworker_Tools = _Tool(
	"Woodworker_Tools",
	"Woodworker's Tools",
	"ANY",
	"Artisan",
	practice=_Practice(
		"Woodworking Proficiency",
		(
			"Wood lives many lives. It grows beneath the sun, carries ships "
			"across black water, holds roofs against storms, and bars gates "
			"against armies. It remembers every season and every hand that "
			"shaped it. You have learned to read those lives through grain, "
			"joint, strain, and scar, and to imagine what the wood might become "
			"next."
			),
		(
			"Shape the Grain",
			(
				"You can shape, carve, join, conceal, reinforce, dismantle, repair, "
				"or sabotage wooden objects and structures. Tell the DM what you "
				"want your work to achieve. If a check is needed, the DM chooses "
				"the Ability and Difficulty Class. Add your Proficiency Bonus to "
				"your roll. If a relevant Skill proficiency also supports your "
				"approach, you have Advantage. For example, forcing open a sturdy "
				"dungeon door might require a Strength check with a DC between 15 "
				"and 20. Athletics could support that approach, giving you "
				"Advantage."
				),
			),
		(
			"Woodwise",
			(
				"You usually recognize timber, workmanship, damage, alterations, "
				"structural purpose, and likely points of failure. Hidden, "
				"supernatural, or exceptionally subtle details may require a check."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and materials, as determined by your "
				"DM, you might create shelters, vehicles, vessels, weapons, "
				"shields, mechanisms, carvings, magical focuses, or enchanted "
				"works. Rare timber, forgotten techniques, and magical designs may "
				"become adventures of their own."
				),
			),
		),
	)

# The 2024 rules split structural and carved woodwork into two proficiencies.
# GenLegend treats both as one Practice so one choice cannot grant it twice.
Carpenter_Tools = Woodworker_Tools
Woodcarver_Tools = Woodworker_Tools
Cartographer_Tools = _Tool(
	"Cartographer_Tools",
	"Cartographer's Tools",
	"WIS",
	"Artisan",
	practice=_Practice(
		"Cartography Proficiency",
		(
			"A good map can mean the difference between months spent wandering "
			"and a direct route to the treasure room. Every map is a promise "
			"that something can be found. You have mastered the language in "
			"which that promise is written."
			),
		(
			"Read the Map",
			(
				"You can read maps, charts, symbols, landmarks, stars, and "
				"navigational instruments to determine where you are, where "
				"something leads, and how it might be reached. You maintain maps "
				"of familiar territory and can add new routes as you travel. Other "
				"cartographers and explorers may let you copy their maps in "
				"exchange for yours. In a mapped place, you usually know where to "
				"find settlements, routes, shelter, trade, worship, magic, and "
				"whatever else its symbols reveal. You can also identify known "
				"dangers, lairs, and possible escape routes. If uncertainty "
				"requires a check, the DM chooses the Ability and Difficulty Class. "
				"Add your Proficiency Bonus to your roll. If a relevant Skill "
				"proficiency supports your approach, you have Advantage. For "
				"example, following an ancient treasure map whose landmarks have "
				"vanished might require a Wisdom check with a DC of 15. History or "
				"Survival could support the attempt."
				),
			),
		(
			"Works of Wonder",
			(
				"*One does not simply walk into the villain's lair.* The right "
				"chart, instrument, sign, or celestial alignment might reveal "
				"vanishing roads, markets opened beneath certain stars, wandering "
				"cities, planar crossings, or magic items known only through "
				"cryptic maps. Such guidance may reveal not only where a "
				"destination lies, but how and when it can be reached: along a "
				"shore path uncovered by the tide, through a portal opened by "
				"forgotten instructions, or from the last place anyone saw the "
				"wandering library. Finding the map, completing its missing "
				"instructions, or surviving the route may become adventures of "
				"their own."
				),
			),
		),
	)

# Navigation is one application of Cartography, not a second proficiency.
# Keep the former key readable for existing saves and rule declarations.
Navigator_Tools = Cartographer_Tools
Cobbler_Tools = _Tool(
	"Cobbler_Tools",
	"Cobbler's Tools",
	"DEX",
	"Artisan",
	practice=_Practice(
		"Shoemaking Proficiency",
		(
			"An old saying warns you never to skimp on anything that keeps you "
			"from the ground: your shoes, your mattress, or your dreams. Every "
			"journey begins where the body meets the road. Shoes can carry a "
			"pauper into a palace, a messenger across seven leagues, a cat into "
			"a royal court, or a dancer toward a grim fate. You have learned "
			"the fine and sometimes enchanted art of shoemaking."
			),
		(
			"The Sole Purpose",
			(
				"You can make, fit, repair, reinforce, or alter footwear for its "
				"wearer and intended journey. You can prepare shoes for difficult "
				"terrain or silent movement, or add a concealed compartment for a "
				"small weapon, message, gem, or magical focus. Footwear and "
				"footprints usually reveal their wearer's size, gait, burden, "
				"direction, and terrain crossed. If uncertainty requires a check, "
				"the DM chooses the Ability and Difficulty Class. Add your "
				"Proficiency Bonus to your roll. If a relevant Skill proficiency "
				"supports your approach, you have Advantage. For example, following "
				"a fugitive by their footprints might require a Wisdom check with a "
				"DC of 15. Investigation or Survival could support the attempt."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and materials, as determined by your "
				"DM, you might create climber's kits, skates, or mundane and "
				"magical footwear or anklets. Your works might fit only one chosen "
				"wearer, cross seven leagues, walk upon clouds, leave no tracks, "
				"burst into dance without permission, or carry a sleeping traveller "
				"home. Cursed slippers might instead find every table leg in the "
				"dark. Lost enchantment patterns, magic items whose power could be "
				"transferred, and rare materials may become adventures of their own."
				),
			),
		),
	)
Cook_Utensils = _Tool(
	"Cook_Utensils",
	"Cook's Utensils",
	"WIS",
	"Artisan",
	practice=_Practice(
		"Cooking Proficiency",
		(
			"Hunger makes every journey honest. To cook is to understand what "
			"lives, what it consumes, what may consume it, and what remains "
			"useful after death. With blade, fire, and judgment, you can turn "
			"the dungeon itself into provision, knowledge, and opportunity."
			),
		(
			"Restorative Meal",
			(
				"During a Short Rest, with suitable food and cooking equipment, you "
				"can prepare a meal for yourself and up to five other creatures. "
				"Anyone who eats it and spends Hit Dice regains 1 extra Hit Point "
				"per Hit Die spent."
				),
			),
		(
			"Know Your Ingredients",
			(
				"You understand blades, butchery, preservation, herbs, poison, "
				"anatomy, and ecology. After inspecting food, plants, or fresh "
				"remains, you may ask the DM what they reveal about their useful or "
				"dangerous parts, health, diet, habitat, defenses, or anatomical "
				"weaknesses. The DM answers what practiced examination can reveal. "
				"If uncertainty requires a check, the DM chooses the Ability and "
				"Difficulty Class. Add your Proficiency Bonus to your roll. If a "
				"relevant Skill proficiency supports your approach, you have "
				"Advantage. For example, isolating a giant scorpion's venom gland "
				"and finding gaps in its carapace might require an Intelligence "
				"check with a DC of 15. Nature could support the examination, "
				"giving you Advantage."
				),
			),
		(
			"Works of Wonder",
			(
				"*The dungeon provides.* Nothing useful needs to be thrown away. "
				"When a work depends on anatomy, safe extraction, preservation, or "
				"the transformation of biological material, you may use Cooking "
				"Tools to harvest and craft from creatures and magical plants. With "
				"suitable equipment, time, and materials, you might make a shield "
				"from an exoskeleton, poison from a giant scorpion's venom, leather "
				"armour from dragon hide, or potions and elixirs from unusual "
				"organs and herbs, among other things. The DM determines what can "
				"be recovered, how much it yields, which properties survive the "
				"process, and what rare ingredients the work still requires. The "
				"search for rare ingredients and magical spices may become an "
				"adventure of its own."
				),
			),
		),
	)
Glassblower_Tools = _Tool(
	"Glassblower_Tools",
	"Glassblower's Tools",
	"INT",
	"Artisan",
	practice=_Practice(
		"Glassworking Proficiency",
		(
			"Glass has a magic of its own. Crystals grow in darkness and under "
			"pressure, following lines and angles no hand commanded. Glass and "
			"crystal catch light, divide it into colours, preserve images, and "
			"offer the unseen somewhere to appear. Magic behaves much the same."
			),
		(
			"Shape the Threshold",
			(
				"You can blow, cut, grind, polish, silver, repair, or carefully "
				"fracture glass and crystal. You understand how shape, material, "
				"inscription, and workmanship determine what a piece can reveal, "
				"conceal, focus, contain, or distort. You can usually recognize "
				"what a magical vessel was built to hold. If uncertainty requires "
				"a check, the DM chooses the Ability and Difficulty Class. Add your "
				"Proficiency Bonus to your roll. If a relevant Skill proficiency "
				"supports your approach, you have Advantage. For example, calling "
				"forth a message stored inside a glass pendant might require a "
				"Charisma check with a DC of 15. Arcana or Perception could support "
				"the attempt."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and materials, as determined by your "
				"DM, you might create lenses, mirrors, enchanted vessels, or "
				"magical foci such as crystal balls, amulets, and wands. Some may "
				"contain light, memories, messages, or spells. Others may become "
				"prisons for spirits and even extraplanar creatures. Such a work "
				"might require rare crystals, enchanted sands, a fragment of "
				"whatever it must hold, or a forgotten ritual. Finding any of them "
				"may become an adventure of its own."
				),
			),
		),
	)
Jeweler_Tools = _Tool(
	"Jeweler_Tools",
	"Jeweler's Tools",
	"INT",
	"Artisan",
	practice=_Practice(
		"Jewelcraft Proficiency",
		(
			"Jewels are small enough to hide in a pocket, yet powerful enough "
			"to carry an empire. Crowns remember rulers, signets command after "
			"their owners die, and gems may hold light, spells, souls, or curses "
			"waiting for a hand to wear them. You have learned to shape and read "
			"the powers gathered in precious things."
			),
		(
			"Read the Jewel",
			(
				"You can appraise, cut, polish, set, repair, resize, or alter gems "
				"and jewellery. From their materials, inscriptions, wear, and "
				"magical reactions, you usually recognize authenticity, value, "
				"provenance, alterations, enchantment, and signs of a curse. You "
				"can often tell whether a piece was intended to focus, store, "
				"conceal, bind, protect, command, or corrupt. If uncertainty "
				"requires a check, the DM chooses the Ability and Difficulty Class. "
				"Add your Proficiency Bonus to your roll. If a relevant Skill "
				"proficiency supports your approach, you have Advantage. For "
				"example, recognizing that an invisibility ring is cursed and bound "
				"to the will of a Dark Lord might require an Intelligence check "
				"with a DC of 15. Arcana or History could support the examination."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and materials, as determined by your "
				"DM, you might create rings, amulets, signets, crowns, diadems, "
				"talismans, or other jewellery from the Item List, including both "
				"mundane and magical pieces. These pieces may serve as Arcane Foci "
				"or Holy Symbols, bind a cantrip, hold a spell cast into them for "
				"another bearer to release, return a thrown weapon, or carry a "
				"curse. Recharging without a donated spell slot, creating items "
				"that allow unlimited casting of levelled spells, and other "
				"exceptional enchantments require special formulas, materials, or "
				"rituals. Specific gems, lost designs, and arcane materials may "
				"become adventures of their own."
				),
			),
		),
	)
Leatherworker_Tools = _Tool(
	"Leatherworker_Tools",
	"Leatherworker's Tools",
	"DEX",
	"Artisan",
	practice=_Practice(
		"Leatherworking Proficiency",
		(
			"Skin is the first and last armour every creature wears. It "
			"remembers what the creature endured: winter, flame, and fang. An "
			"invulnerable lion may become a hero's cloak, while a mighty dragon "
			"may rise again as armour. You have learned to preserve those "
			"memories and give them a second life."
			),
		(
			"A Second Skin",
			(
				"You can cure, tan, cut, stitch, fit, reinforce, repair, or alter "
				"hides and leather. From grain, scars, treatment, stitching, and "
				"magical reactions, you can usually recognize the creature a hide "
				"came from, what it endured, how the material was worked, and which "
				"of the creature's qualities might remain. If uncertainty requires "
				"a check, the DM chooses the Ability and Difficulty Class. Add your "
				"Proficiency Bonus to your roll. If a relevant Skill proficiency "
				"supports your approach, you have Advantage. For example, "
				"determining whether a lion's hide might grant Resistance to "
				"Piercing and Slashing damage if properly worked might require an "
				"Intelligence check with a DC of 15. History or Nature could support "
				"the examination."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and materials, as determined by your "
				"DM, you might create slings, whips, armour, cloaks, masks, packs, "
				"cases, parchment, pouches, quivers, waterskins, harnesses, saddles, "
				"or other mundane and magical works from the Item List. A creation "
				"might preserve something of its source: a dragon's resistance, a "
				"wolf's Pack Tactics, or a dungeon monstrosity's ability to "
				"disappear into the shadows. An enchanted cloak or suit of armour "
				"might even allow its wearer to assume the creature's form. Consult "
				"the creature's stat block with your DM to decide which trait the "
				"work preserves and what is required to craft it. Finding the "
				"creature, bringing it down without ruining its hide, and obtaining "
				"the magical treatment needed to preserve its power may become "
				"adventures of their own."
				),
			),
		),
	)
Mason_Tools = _Tool(
	"Mason_Tools",
	"Mason's Tools",
	"STR",
	"Artisan",
	practice=_Practice(
		"Masonry Proficiency",
		(
			"Stone holds. It holds empires, memories, and marvels. Every wall "
			"preserves the craft of its builders, and every crack records what "
			"tried to bring it down. A labyrinth can hold a monster for "
			"generations, while a perfect statue may blink back at an intruder. "
			"Kingdoms vanish while their foundations remain. You have learned "
			"the foundational language of stone."
			),
		(
			"Bones of Stone",
			(
				"You can quarry, cut, dress, carve, set, reinforce, dismantle, or "
				"repair stone. You can rig a Block and Tackle to move heavy stones "
				"or support a failing structure. You can also improvise levers, "
				"rollers, ramps, or sledges to move great weights with less effort. "
				"From joints, tool marks, cracks, and workmanship, you can usually "
				"recognize a structure's age, origin, alterations, load-bearing "
				"elements, hidden spaces, and likely points of failure. If "
				"uncertainty requires a check, the DM chooses the Ability and "
				"Difficulty Class. Add your Proficiency Bonus to your roll. If a "
				"relevant Skill proficiency supports your approach, you have "
				"Advantage. For example, opening a passage through a sealed tomb "
				"without bringing down the ceiling might require an Intelligence "
				"check with a DC of 15. Investigation or History could support the "
				"attempt."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and materials, as determined by your "
				"DM, you might create statues, monuments, altars, fountains, "
				"bridges, barricades, towers, tombs, walls, or other mundane and "
				"magical stonework, including suitable objects from the Item List. "
				"Your works might awaken as living statues, rise as golems bound to "
				"a command, guard forbidden chambers, conceal passages, or become "
				"portals to distant places. Your understanding of their "
				"construction may also help you open, bypass, or activate such "
				"wonders. Finding magical materials, crafting plans, and activation "
				"spells may become adventures of their own."
				),
			),
		),
	)
Painter_Supplies = _Tool(
	"Painter_Supplies",
	"Painter's Supplies",
	"WIS",
	"Artisan",
	practice=_Practice(
		"Painting Proficiency",
		(
			"Art imitates life, and life imitates art. In your hands, a single "
			"stroke can affect both. Paint an eye, and something may begin to "
			"watch. Mark your skin with a god's symbol, and they may watch over "
			"you. Paint a beast upon a shield, and its bearer may carry the "
			"creature's ferocity. Life is what you make of it."
			),
		(
			"The Living Image",
			(
				"You can sketch, paint, mix pigments, prepare surfaces, copy or "
				"restore images, and use paint to decorate or camouflage creatures, "
				"objects, and places. You can reproduce a recognizable person, "
				"creature, place, or object you have seen. From composition, "
				"symbols, pigments, layers, and brushwork, you can usually recognize "
				"a work's age, origin, alterations, purpose, and whether it was "
				"intended to commemorate, deceive, invite, command, protect, or "
				"curse. If uncertainty requires a check, the DM chooses the Ability "
				"and Difficulty Class. Add your Proficiency Bonus to your roll. If "
				"a relevant Skill proficiency supports your approach, you have "
				"Advantage. For example, determining why the painted eyes upon a "
				"sealed door follow only one of your companions might require a "
				"Wisdom check with a DC of 15. Arcana or Religion could support the "
				"examination."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable materials, time, and a physical surface to serve as "
				"your canvas, as determined by your DM, you can infuse an "
				"appropriate object, creature, or place with a magical property. A "
				"lasting work becomes part of the enchanted subject and can turn it "
				"into a specific magic item from the Item List, following its "
				"normal rules, including Attunement when appropriate. You can also "
				"create Magic Tattoos upon the skin using henna, ash, gold, blood, "
				"or other pigments. The Item List provides established designs and "
				"effects, including tattoos that fade after use or lasting tattoos "
				"that may require Attunement. Finding magical pigments, procuring "
				"the required design, and finding the right technique for the work "
				"may become adventures of their own."
				),
			),
		),
	)
Potter_Tools = _Tool(
	"Potter_Tools",
	"Potter's Tools",
	"INT",
	"Artisan",
	practice=_Practice(
		"Pottery Proficiency",
		(
			"Clay remembers. Softened by water, it accepts a face, a footprint, "
			"a key, or a wound. Hardened by fire, it refuses to forget. It may "
			"become a vessel, a porcelain likeness, a painted animal, or a small "
			"effigy through which someone distant can be reached. You have "
			"learned to teach earth a shape, and sometimes a purpose."
			),
		(
			"The Memory of Clay",
			(
				"You can prepare, throw, mould, sculpt, glaze, fire, seal, repair, "
				"or safely break clay and ceramic works. You can create vessels, "
				"tiles, ornaments, porcelain dolls, animal figurines, and moulds "
				"that reproduce the shape of a key, seal, face, fragment, or other "
				"mundane object. A mould copies form, not material or magic. You "
				"also understand the mineral clays used in wraps and restorative "
				"baths. You can usually recognize a work's age, origin, maker, "
				"former contents, alterations, and intended purpose. If uncertainty "
				"requires a check, the DM chooses the Ability and Difficulty Class. "
				"Add your Proficiency Bonus to your roll. If a relevant Skill "
				"proficiency supports your approach, you have Advantage. For "
				"example, quickly making a clay mould of a key might require an "
				"Intelligence check with a DC of 15. Sleight of Hand or "
				"Investigation could support the task."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, clay, a kiln, and time, as determined by your "
				"DM, you might create jugs, lamps, urns, porcelain dolls, "
				"figurines, effigies, moulds, or other mundane and magical ceramic "
				"works from the Item List. These include Alchemy Jugs, Pots of "
				"Awakening, Bowls of Commanding Water Elementals, ceramic Decanters "
				"of Endless Water, and Figurines of Wondrous Power. A work might "
				"awaken as a guardian, let magic reach someone through their "
				"likeness, draw poison or curses into healing clay, reproduce an "
				"object through an enchanted mould, or imprison something "
				"dangerous. With the appropriate Manual, a clay figure may rise as "
				"a Clay Golem. Finding magical clay, obtaining a likeness or "
				"fragment, and learning the required technique may become "
				"adventures of their own."
				),
			),
		),
	)
Smith_Tools = _Tool(
	"Smith_Tools",
	"Smith's Tools",
	"STR",
	"Artisan",
	practice=_Practice(
		"Smithing Proficiency",
		(
			"The forge is a trial by fire. Metal enters without purpose and "
			"leaves as a blade, a shield, or a suit of armour. A broken sword "
			"may restore a kingdom to its heir, while a single nail may seal a "
			"monster behind a door. You have learned to hear metal beneath the "
			"hammer and decide what it will become."
			),
		(
			"The Temper of Metal",
			(
				"You can smelt, alloy, forge, temper, sharpen, repair, or dismantle "
				"metalwork. You can make and alter weapons, armour, shields, chains, "
				"and other practical metal objects. Their colour, ring, sparks, "
				"grain, and tool marks usually reveal their composition, origin, "
				"maker, repairs, weaknesses, and enchantments. If uncertainty "
				"requires a check, the DM chooses the Ability and Difficulty Class. "
				"Add your Proficiency Bonus to your roll. If a relevant Skill "
				"proficiency supports your approach, you have Advantage. For "
				"example, reforging a shattered sword without destroying the runes "
				"along its blade might require an Intelligence check with a DC of "
				"15. Arcana or History could support the task."
				),
			),
		(
			"Works of Wonder",
			(
				"With a suitable forge, tools, time, and materials, as determined "
				"by your DM, you might create mundane and magical weapons, armour, "
				"shields, or metallic constructs from the Item List. A work may "
				"inherit qualities from its ore, the fire that shaped it, or the "
				"substance in which it was quenched. It might burn with elemental "
				"power, return when thrown, defend its bearer, or awaken with a will "
				"of its own. With the appropriate Manual, a forged body may rise as "
				"an Iron Golem. Finding metal fallen from the stars, rediscovering "
				"a lost dwarven forge, and recovering the pieces of a legendary "
				"weapon may become adventures of their own."
				),
			),
		),
	)
Tinker_Tools = _Tool(
	"Tinker_Tools",
	"Tinker's Tools",
	"DEX",
	"Artisan",
	practice=_Practice(
		"Tinkering Proficiency",
		(
			"Every mechanism begins as a pile of parts. A spring pulls, a gear "
			"turns, a lever answers, and suddenly the whole thing moves. Where "
			"others see scrap, you see a machine waiting to happen. You have "
			"learned to make unlikely things work together."
			),
		(
			"Make It Work",
			(
				"You can assemble, adjust, repair, disable, or repurpose mechanisms "
				"made from mixed parts. You can create firearms, lanterns, traps, "
				"locks, restraints, alarms, and other devices from the Item List. "
				"From their layout, movement, wear, and materials, you can usually "
				"tell what a device does, what powers it, and how it is controlled. "
				"If uncertainty requires a check, the DM chooses the Ability and "
				"Difficulty Class. Add your Proficiency Bonus to your roll. If a "
				"relevant Skill proficiency supports your approach, you have "
				"Advantage. For example, rebuilding a shattered trap into a one-use "
				"alarm before its makers return might require an Intelligence check "
				"with a DC of 15. Investigation or Sleight of Hand could support "
				"the task."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and materials, as determined by your "
				"DM, you might create magical mechanisms, firearms, vehicles, "
				"prosthetic limbs, traps, or mechanical constructs from the Item "
				"List. A work might move at a command, perform a task by itself, "
				"carry its maker, or imitate life. Finding lost plans, recovering a "
				"unique component, and securing a suitable source of power may "
				"become adventures of their own."
				),
			),
		),
	)
Weaver_Tools = _Tool(
	"Weaver_Tools",
	"Weaver's Tools",
	"DEX",
	"Artisan",
	practice=_Practice(
		"Weaving Proficiency",
		(
			"They say every life is a thread. One may guide a hero through a "
			"labyrinth, bind a promise, preserve a history, or be cut when its "
			"story ends. Alone, a thread breaks easily. Woven with others, it "
			"can clothe a king, shelter an army, catch a monster, or carry a "
			"traveller through the sky. You have learned to turn fragile fibres "
			"into forms that endure."
			),
		(
			"The Strength Between Threads",
			(
				"You can spin, weave, sew, embroider, dye, braid, knot, or mend "
				"fibres. You can create padded armour, clothing, robes, capes, "
				"ropes, nets, sails, tents, baskets, and other textiles from the "
				"Item List. Their fibres, weave, dyes, patterns, seams, wear, and "
				"repairs usually reveal their materials, origin, maker, age, "
				"alterations, and intended meaning. You can also conceal or "
				"recognize messages, maps, allegiances, and stories encoded through "
				"colour and pattern. If uncertainty requires a check, the DM chooses "
				"the Ability and Difficulty Class. Add your Proficiency Bonus to "
				"your roll. If a relevant Skill proficiency supports your approach, "
				"you have Advantage. For example, reconstructing a burned cape to "
				"identify the person who wore it might require an Intelligence check "
				"with a DC of 15. History or Investigation could support the task."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and materials, as determined by your "
				"DM, you might create magical clothing, armour, bags, capes, "
				"carpets, ropes, nets, banners, or tents from the Item List. A work "
				"might conceal or transform its wearer, hold more than its shape "
				"allows, move at a command, fly, entangle a monster, or preserve a "
				"story so faithfully that its scenes awaken. Harvesting a monster's "
				"silk, recovering a lost pattern, and obtaining thread spun from "
				"gold or moonlight may become adventures of their own."
				),
			),
		),
	)

ARTISAN_TOOLS: tuple[Tool_Definition, ...] = (
	Alchemist_Supplies,
	Brewer_Supplies,
	Calligrapher_Supplies,
	Woodworker_Tools,
	Cartographer_Tools,
	Cobbler_Tools,
	Cook_Utensils,
	Glassblower_Tools,
	Jeweler_Tools,
	Leatherworker_Tools,
	Mason_Tools,
	Painter_Supplies,
	Potter_Tools,
	Smith_Tools,
	Tinker_Tools,
	Weaver_Tools,
	)

Disguise_Kit = _Tool(
	"Disguise_Kit",
	"Disguise Kit",
	"CHA",
	"Kit",
	practice=_Practice(
		"Disguise Kit Proficiency",
		(
			"Most doors are guarded by expectations, not locks. People see the "
			"uniform before the face, the age before the eyes, and the role "
			"before the stranger beneath it. A little colour can hide a scar; "
			"the right posture can turn a beggar into a magistrate. You have "
			"learned to give expectation exactly what it wants."
			),
		(
			"Play the Part",
			(
				"With a Disguise Kit in hand, you can apply makeup, dress or dye "
				"hair, fit false features, alter a silhouette, and create or adapt "
				"costumes. You can usually recognize how a disguise was made, what "
				"identity it suggests, and where it might fail. Your work can let "
				"someone pass as a different profession, rank, age, origin, or "
				"plausible individual, but it changes what observers see, not what "
				"the wearer knows. If uncertainty requires a check, the DM chooses "
				"the Ability and Difficulty Class. Add your Proficiency Bonus to "
				"your roll. If a relevant Skill proficiency supports your approach, "
				"you have Advantage. For example, gaining entry to a guarded feast "
				"while disguised as a visiting noble might require a Charisma check "
				"with a DC of 15. History or Deception could support the attempt. "
				"Voice, manner, memory, touch, unexpected questions, and close "
				"inspection may still expose the deception."
				),
			),
		),
	)
Forgery_Kit = _Tool(
	"Forgery_Kit",
	"Forgery Kit",
	"DEX",
	"Kit",
	practice=_Practice(
		"Forgery Kit Proficiency",
		(
			"Power often travels on paper. A gate opens because of a seal, a "
			"prisoner walks free because of a signature, and soldiers march "
			"because ink says a ruler commanded it. Most people never meet "
			"authority; they meet its handwriting. You have learned to make ink "
			"speak in another person's voice."
			),
		(
			"Borrowed Authority",
			(
				"With a Forgery Kit in hand, you can imitate handwriting, reproduce "
				"seals, alter text, match inks and materials, or age and distress "
				"documents. You can usually recognize how a document was produced, "
				"whether it has been altered, what authority it imitates, and where "
				"the deception might fail. Your work can produce convincing "
				"letters, permits, orders, certificates, accounts, or other "
				"documents, but it cannot change official records or what witnesses "
				"remember. If uncertainty requires a check, the DM chooses the "
				"Ability and Difficulty Class. Add your Proficiency Bonus to your "
				"roll. If a relevant Skill proficiency supports your approach, you "
				"have Advantage. For example, forging a writ of passage convincing "
				"enough to cross a guarded border might require a Dexterity check "
				"with a DC of 15. History or Deception could support the attempt. "
				"Poor preparation, such as naming the wrong legion commander, using "
				"an incorrect title, or misrepresenting a house's heraldry, may "
				"still expose the forgery."
				),
			),
		),
	)
Herbalism_Kit = _Tool(
	"Herbalism_Kit",
	"Herbalism Kit",
	"INT",
	"Kit",
	practice=_Practice(
		"Herbalism Proficiency",
		(
			"The smallest leaf may close a wound, steal a memory, stop a heart, "
			"or pull a sleeper back from death. Every forest, marsh, garden, and "
			"ruined wall conceals a living apothecary. You have learned which "
			"growing things answer the body, and how to ask without taking the "
			"wrong dose."
			),
		(
			"The Living Apothecary",
			(
				"You can identify, gather, cultivate, preserve, and prepare plants, "
				"fungi, roots, seeds, sap, pollen, and other living ingredients. You "
				"usually recognize where they grow, when they are useful, whether "
				"they are medicinal or poisonous, and how they have affected a "
				"creature. Herbalism draws out properties already present in an "
				"ingredient rather than transforming its fundamental nature. If "
				"uncertainty requires a check, the DM chooses the Ability and "
				"Difficulty Class. Add your Proficiency Bonus to your roll. If a "
				"relevant Skill proficiency supports your approach, you have "
				"Advantage. For example, finding and preparing a remedy that "
				"suspends the effects of basilisk venom might require an "
				"Intelligence check with a DC of 19. Nature or Medicine could "
				"support the attempt."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and ingredients, as determined by your "
				"DM, you might prepare antitoxins, antivenoms, healer's kits, "
				"medicinal salves, incense, sleeping draughts, plant-based poisons, "
				"a Potion of Healing, or other potions and elixirs from the Item "
				"List. Finding a rare plant, learning when it flowers, or returning "
				"with a living specimen may become adventures of their own."
				),
			),
		),
	)
Poisoners_Kit = _Tool(
	"Poisoners_Kit",
	"Poisoner's Kit",
	"INT",
	"Kit",
	practice=_Practice(
		"Poisoncraft Proficiency",
		(
			"Every body is a fortress with gates: breath, blood, skin, and "
			"hunger. A poison is more than a substance. It is the right dose, "
			"the right path, and the moment nobody notices. Herbalists learn "
			"what helps life endure. You have learned where that endurance "
			"fails."
			),
		(
			"The Dose Makes the Poison",
			(
				"You can detect, identify, extract, preserve, combine, neutralize, "
				"or safely apply poisons, venoms, spores, and other toxins. You "
				"usually recognize their source, symptoms, potency, likely means "
				"of exposure, and what might slow or counteract their effects. You "
				"can also examine poisoned objects, wounds, food, or drink and "
				"safely harvest toxins from creatures. If uncertainty requires a "
				"check, the DM chooses the Ability and Difficulty Class. Add your "
				"Proficiency Bonus to your roll. If a relevant Skill proficiency "
				"supports your approach, you have Advantage. For example, "
				"determining which poison killed an ambassador and how it was "
				"administered might require an Intelligence check with a DC of 15. "
				"Investigation or Medicine could support the examination."
				),
			),
		(
			"Works of Wonder",
			(
				"With suitable tools, time, and ingredients, as determined by your "
				"DM, you might prepare weapon coatings, antidotes, or poisons from "
				"the Item List. Your creations might act through contact, "
				"ingestion, inhalation, or injury, and induce sleep, paralysis, "
				"visions, forgetfulness, petrification, or death. Finding a rare "
				"toxin, hunting the creature that produces it, or recovering its "
				"only known antidote may become adventures of their own."
				),
			),
		),
	)
Thieves_Tools = _Tool(
	"Thieves_Tools",
	"Thieves' Tools",
	"DEX",
	"Kit",
	practice=_Practice(
		"Thieves' Tools Proficiency",
		(
			"Every lock asks a question: Can **you** enter? Behind it lies an "
			"answer someone fears you will find. A trap asks the same question "
			"with sharper punctuation. You have learned to read the question "
			"carefully, and you came prepared to cheat."
			),
		(
			"The Quiet Answer",
			(
				"With Thieves' Tools in hand, you can pick locks, open manacles, "
				"and disarm, bypass, reset, or safely trigger traps. You can usually "
				"recognize a familiar mechanism, where it has been tampered with, "
				"and whether opening it will leave evidence. Unfamiliar or magical "
				"mechanisms may require a clue, special knowledge, or another "
				"approach before your tools can help."
				),
			),
		(
			"Read Before You Reach",
			(
				"Finding a trap and disarming it are separate tasks. Perception may "
				"reveal that something is wrong. Investigation may explain the "
				"mechanism. Sleight of Hand may support delicate manipulation. If "
				"uncertainty requires a check, the DM chooses the Ability and "
				"Difficulty Class. Add your Proficiency Bonus to your roll. If a "
				"relevant Skill proficiency supports your approach, you have "
				"Advantage. For example, opening a lock without disturbing the bell "
				"wired to its bolt might require a Dexterity check with a DC of 15. "
				"Sleight of Hand or Investigation could support the attempt."
				),
			),
		),
	)


MUSICIANSHIP_PRACTICE = _Practice(
	"Musicianship Proficiency",
	(
		"Music is older than most borders and travels where words cannot. A "
		"pipe may empty a city of vermin, a lyre may soften the rulers of "
		"death, a horn may call across worlds, and a flute may guide its "
		"bearer through fire. Fairy roads open to familiar tunes, armies "
		"remember the drum, and even monsters sometimes stop to listen. You "
		"have learned how to make the world lean closer."
		),
	(
		"Move the World",
		(
			"You can perform known music, improvise, reproduce a melody after "
			"hearing it, maintain your instruments, and recognize musical "
			"traditions. You might use music to attract a crowd, signal across "
			"a distance, conceal a message, accompany a ritual, guide a dance, "
			"or influence the mood of creatures willing to listen. Music cannot "
			"compel them without magic. If uncertainty requires a check, the DM "
			"chooses the Ability and Difficulty Class. Add your Proficiency "
			"Bonus to your roll. If a relevant Skill proficiency supports your "
			"approach, you have Advantage. For example, calming a frightened "
			"beast long enough to pass through its territory might require a "
			"Wisdom check with a DC of 15. Animal Handling or Nature could "
			"support the attempt."
			),
		),
	(
		"Music as Magic",
		(
			"Any Musical Instrument you are trained to use can serve as a "
			"Spellcasting Focus for spells you cast. Playing it satisfies a "
			"spell's Verbal component, provided the music can be heard. An "
			"enchantment may ride upon a melody, an illusion rise from the "
			"strings, a summoned creature answer a horn, or thunder follow a "
			"drumbeat. This changes how the magic manifests, but not its other "
			"components or effects."
			),
		),
	subject_title="Known Instruments",
	)


def _Instrument(
		key: str,
		name: str,
		) -> Tool_Definition:
	return _Tool(
		key,
		name,
		"CHA",
		"Musical Instrument",
		legacy_attribute="Musical_Instrument",
		variant=name,
		practice=MUSICIANSHIP_PRACTICE,
		)


Bagpipes = _Instrument( "Bagpipes", "Bagpipes" )
Drum = _Instrument( "Drum", "Drum" )
Dulcimer = _Instrument( "Dulcimer", "Dulcimer" )
Flute = _Instrument( "Flute", "Flute" )
Horn = _Instrument( "Horn", "Horn" )
Lute = _Instrument( "Lute", "Lute" )
Lyre = _Instrument( "Lyre", "Lyre" )
Pan_Flute = _Instrument( "Pan_Flute", "Pan Flute" )
Shawm = _Instrument( "Shawm", "Shawm" )
Viol = _Instrument( "Viol", "Viol" )

MUSICAL_INSTRUMENTS: tuple[Tool_Definition, ...] = (
	Bagpipes,
	Drum,
	Dulcimer,
	Flute,
	Horn,
	Lute,
	Lyre,
	Pan_Flute,
	Shawm,
	Viol,
	)


GAMBLING_PRACTICE = _Practice(
	"Gambling Proficiency",
	(
		"Every game is a world in miniature. Pieces become armies, cards "
		"become fortunes, and dice become judgement. Across the table, "
		"people wager more than gold: pride, secrets, promises, and maps "
		"they should never have possessed. You have learned that the game "
		"begins before the first throw and rarely ends when the winnings "
		"are counted."
		),
	(
		"Read the Table",
		(
			"With a Gaming Set you are trained to use, you can calculate odds, "
			"manage wagers, and recognize familiar forms of cheating. You can "
			"play one match as part of a Long Rest, making only one roll to "
			"determine its final outcome. Before rolling, determine the "
			"Difficulty Class, wager, and possible prize with the DM. You may "
			"wager gold or items you own for a proportional reward. Make a "
			"Luck check and add your Proficiency Bonus. On a success, you win "
			"the agreed prize; on a failure, you lose your wager. A natural 20 "
			"may reveal an exceptional prize, possibly a Wondrous Item chosen "
			"by the DM, if such a prize is available. If another uncertainty "
			"requires a check, the DM chooses the Ability and Difficulty Class. "
			"A relevant Skill proficiency can grant Advantage. For example, "
			"realizing that two smiling strangers are colluding might require a "
			"Wisdom check with a DC of 15. Insight or Investigation could "
			"support the examination."
			),
		),
	)


def _Gaming_Set(
		key: str,
		name: str,
		) -> Tool_Definition:
	return _Tool(
		key,
		name,
		"WIS",
		"Gaming Set",
		legacy_attribute="Gaming_Set",
		variant=name,
		practice=GAMBLING_PRACTICE,
		)


Dice_Set = _Gaming_Set( "Dice_Set", "Dice Set" )
Dragonchess_Set = _Gaming_Set( "Dragonchess_Set", "Dragonchess Set" )
Playing_Card_Set = _Gaming_Set( "Playing_Card_Set", "Playing Card Set" )
Three_Dragon_Ante_Set = _Gaming_Set(
	"Three_Dragon_Ante_Set",
	"Three-Dragon Ante Set",
	)

GAMING_SETS: tuple[Tool_Definition, ...] = (
	Dice_Set,
	Dragonchess_Set,
	Playing_Card_Set,
	Three_Dragon_Ante_Set,
	)

OTHER_TOOLS: tuple[Tool_Definition, ...] = (
	Disguise_Kit,
	Forgery_Kit,
	Herbalism_Kit,
	Poisoners_Kit,
	Thieves_Tools,
	)

TOOLS: tuple[Tool_Definition, ...] = (
	*ARTISAN_TOOLS,
	*OTHER_TOOLS,
	*GAMING_SETS,
	*MUSICAL_INSTRUMENTS,
	)

TOOLS_BY_KEY = {
	tool.key: tool
	for tool in TOOLS
	}
TOOLS_BY_KEY.update(
	{
		"Carpenter_Tools": Woodworker_Tools,
		"Woodcarver_Tools": Woodworker_Tools,
		"Navigator_Tools": Cartographer_Tools,
		}
	)


def Find_Practice_Entries(
		character,
		) -> tuple[Resolved_Practice, ...]:
	"""Find learned Practices once, in canonical Tool catalog order."""
	practices: list[Resolved_Practice] = []
	tools_by_practice: dict[
		Practice_Definition,
		list[Tool_Definition],
		] = {}

	for tool in TOOLS:
		practice = tool.practice

		if (
			practice is None
			or not Is_Trained(
				character,
				tool,
				)
			):
			continue

		tools_by_practice.setdefault(
			practice,
			[],
			).append( tool )

	for practice, trained_tools in tools_by_practice.items():
		practices.append(
			Resolved_Practice(
				definition=practice,
				subjects=(
					tuple(
						tool.name
						for tool in trained_tools
						)
					if practice.subject_title
					else ()
					),
				)
			)

	return tuple( practices )


def _self_test() -> None:
	from AtlasActorLudi.ProficiencyKit import (
		Provenance,
		Training_Batch,
		Training_Grant,
		Training_Record,
		)

	assert len( ARTISAN_TOOLS ) == 16
	assert len( MUSICAL_INSTRUMENTS ) == 10
	assert len(
		{
			tool.key
			for tool in TOOLS
			}
		) == len( TOOLS )
	assert Carpenter_Tools is Woodworker_Tools
	assert Woodcarver_Tools is Woodworker_Tools
	assert TOOLS_BY_KEY[ "Carpenter_Tools" ] is Woodworker_Tools
	assert TOOLS_BY_KEY[ "Woodcarver_Tools" ] is Woodworker_Tools
	assert ARTISAN_TOOLS.count( Woodworker_Tools ) == 1
	assert Navigator_Tools is Cartographer_Tools
	assert TOOLS_BY_KEY[ "Navigator_Tools" ] is Cartographer_Tools
	assert TOOLS.count( Cartographer_Tools ) == 1
	assert Cook_Utensils.legacy_attribute == "Cook_Utensils"
	assert Lute.legacy_attribute == "Musical_Instrument"

	practices = {
		tool.practice.title: tool.practice
		for tool in TOOLS
		if tool.practice is not None
		}
	assert len( practices ) == 23
	assert Poisoners_Kit.practice is not None
	assert (
		Poisoners_Kit.practice.title
		== "Poisoncraft Proficiency"
		)
	assert all(
		gaming_set.practice is GAMBLING_PRACTICE
		for gaming_set in GAMING_SETS
		)
	assert all(
		instrument.practice is MUSICIANSHIP_PRACTICE
		for instrument in MUSICAL_INSTRUMENTS
		)

	class Example_Feature:
		pass

	class Probe:
		pass

	probe = Probe()
	probe.training = Training_Record(
		gains=(
			Training_Batch(
				grant_id="ToolsKit:Cartography",
				feature=Example_Feature,
				grants=(
					Training_Grant(
						Navigator_Tools
						),
					Training_Grant(
						Dice_Set
						),
					Training_Grant(
						Playing_Card_Set
						),
					Training_Grant(
						Flute
						),
					Training_Grant(
						Lute
						),
					),
				provenance=Provenance(
					source="Self-test"
					),
				),
			),
		)
	probe.skills = None

	resolved = Find_Practice_Entries( probe )
	assert tuple(
		practice.definition
		for practice in resolved
		) == (
		Cartographer_Tools.practice,
		GAMBLING_PRACTICE,
		MUSICIANSHIP_PRACTICE,
		)
	assert resolved[ 2 ].subjects == (
		Flute.name,
		Lute.name,
		)
	assert resolved[ 2 ].to_dict()[ "sections" ][ 0 ] == {
		"title": "Known Instruments",
		"guidance": "Flute, Lute",
		}

	print( "OK — ToolsKit self-test" )


if __name__ == "__main__":
	_self_test()
