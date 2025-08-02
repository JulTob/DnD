from ..Grimoire_of_Health  import roll_health, HIT_DIE_TABLE
from ..Codex_of_Progression import Progression

from AtlasLusoris.Grimoire_of_Features import (
	Feature,
	BuildAvailableInvocations,
	ApplyRandomFeats,
	ApplyEpicBoon
	)
import random


class Warlock(Progression):
	HIT_DIE = 8

	def __init__(self, character):
		self.character = character

	HIT_DIE = 8

	@staticmethod
	def warlock_invocations_known(level):
		# These tables match 2024 PHB progression
		if level <= 1: return 1
		if level < 5: return 3
		if level < 7: return 5
		if level < 9: return 6
		if level <= 11: return 7
		if level <= 14: return 8
		if level < 17: return 9
		return 10

	def prepare_invocations(self):
		n = Warlock.warlock_invocations_known(self.character.level)
		available = list(BuildAvailableInvocations(self.character))
		chosen = random.sample(available, min(n, len(available)))

		self.character.invocations = []

		# Here is the magic:
		for inv in chosen:
			inv(self.character)  # applies effect if needed
			self.character.invocations.append(inv)

	def features(self, character):
		features = []
		# Assign subclass if not already set
		if not character.Subclass:
			subclass = choice(subclasses["Warlock"])
			character.Subclass = subclass
		else:
			subclass = character.Subclass

		level = character.level
		n_inv = Warlock.warlock_invocations_known(level)


		# Level 1:
		if level >= 1:
			features.append(Feature("Eldritch Invocations",
				f"You have unearthed Eldritch Invocations, pieces of forbidden knowledge that imbue you with an abiding magical ability or other lessons.",
				f"Class: Warlock – {subclass}"))

			features.append(Feature("Pact Magic",
				"""Through occult ceremony, you have formed a pact with a mysterious entity to gain magical powers. The entity is a voice in the shadows-its identity unclear—but its boon to you is concrete: the ability to cast spells.""",
				"Class: Warlock"))

		# Level 2:
		if level >= 2:
			roll_health(character)
			features.append(Feature("Magical Cunning",
				f"You can perform an esoteric rite for 1 minute. At the end of it, you regain expended Pact Magic spell slots but no more than a number equal to half your maximum (round up). Once you use this feature, you can't do so again until you finish a Long Rest.",
				"Class: Warlock"))

		# Level 3:
		if level >= 3:

			if subclass == "Celestial":
				patron = random.choice([
					"Solinar, the Sunforged Champion",         # an Empyrean who led the Bright Legion
					"Seraphiel, the Radiant Guard",            # a six-winged seraph of Mount Celestia
					"Mariel, the Trumpet Voice",               # trumpet-bearing Archon of the Fourth Spire
					"Cavoriel, the Golden Sentinel",           # Planetar captain of the Celestial Host
					"Aurius, the Dawnbringer",                 # Deva herald of the first light

					# Celestial Beasts & Uncommon Fiends of Light
					"Lumiel, the Lightweaver Unicorn",         # a star-born unicorn of the Seven Heavens
					"Astreon, the Starmantle Couatl",           # cosmic serpent-guardian
					"Helion, the Daystar Ki-rin",               # dragon-steed of the Sun Throne
					"Caelius, the Cloudstrider Pegasus",       # winged steed of the Serene Aerie
					"Sylvaran, the Forest’s Radiance",     # elk-noble of the Verdant Sphere

					# Archon & Fatebinders
					"Zephyria, the Auroral Dancer",            # Skypiercer Archon of Wind’s Grace
					"Avitor, the Guiding Star",                 # celestial archer who steers lost souls
					"Juniel, the Dawnwatcher",                 # watchful Archon at the Gate of Days
					"Radiatus, the Beaconheart",               # living lighthouse of the Celestial Sea
					"Seluna, the Silver Light",                # Moon-archon of the Constant Vigil

					# Empyreal & Astral Mystics
					"Celestria, the Starweaver",               # astral spirit who threads reality’s web
					"Astrion, the Empyrean Host",               # crown-bearer of the Astral Realm
					"Elunara, the Starlit Path",               # guide through the Midnight Vale
					"Veloria, the Luminous Fount",             # wellspring of celestial grace
					"Serenus, the Calm Radiance",              # mediator between light and shadow

					# Dawn & Twilight Wardens
					"Nymera, the Twilight Wing",               # dusk-bound protector of veiled portals
					"Lunara, the Moon’s Embrace",              # guardian spirit of lunar tides
					"Galara, the Empyreal Shield",             # fortress-spirit of the Celestial Keep
					"Serulen, the Lightwarden",                # archon who polices the planar borders
					"Auradora, the Battle Muse",            # inspirer of hope in mortal hearts

					"Orcax, the Black Sun",
					"Cihuacouatl, The Soul Recollector",
					"Crassistriga, The First Sphinx",
					"Orion, the Constellation",
					"The Forgotten God",
					"Thorondor, Monarch of the Giant Eagles",
					"Demigod",
					"Burning Seraph",
					"Calliope, Muse of Adventures",
					"Clio, Muse of Historians",
					"Erato, Muse of Poets",
					"Euterpe, Muse of Music",
					"Melpomene, Muse of Tragedy",
					"Polyhymnia, Muse of Hymns",
					"Terpsichore, Muse of Dance",
					"Thalia: Muse of comedy",
					"Urania, Muse of astronomy",
					"Ophanim, The Last Angelic Throne",
					"Ophiuchus, Archon of the Zodiac",
					#"Eclipsar",
					# "Planetar", "Dark Sun",
					 #"Seraph", "Phoenix",
					#"Oracle", "Avatar", "Guardian",
					#"Avatar", "Gate Guardian", "Ki-rin"
					])
				features.append(Feature("Celestial Patron",
					f"""Your pact draws on the Upper Planes, the realms of
					everlasting bliss. You entered, willingly or not,
					in a pact with a Celestial: {patron}.
					Your pact allows you to experience
					a hint of the holy light that illuminates
					the multiverse.""",
					"Class: Warlock"))
				features.append(Feature("Healing Light",
					f"""You gain the ability to channel celestial energy to heal wounds. You have a pool of d6s to fuel this healing. The number of dice in the pool equals 1 plus your Warlock level.
					<br>
					As a Bonus Action, you can heal yourself or one creature you can see within 60 feet of yourself, expending dice from the pool. The maximum number of dice you can expend at once equals your Charisma modifier (minimum of one die). Roll the dice you expend, and restore a number of Hit Points equal to the roll's total. Your pool regains all expended dice when you finish a Long Rest.
					""",
					"Class: Warlock"))
			if subclass == "Fiend":
				patron = random.choice([
					"The Infernal Librarian",	"The Hell Duke",	"The Throne of Chains",
					"The Whisperer Beneath the Ashes", "The Lord of Flies", "The Soul Collector",
					"The King of Rot",	"The Vermilion Herald", "The Sovereign",
					"The Baron of Infinite Flesh", "The Flesh Architect",
					"The Prince of Blood", "The Lord of the Ashes", "The God Butcher",
					"The Hellgate Warden", "The Pestilent", "The Black Sulfur",
					"The Corruptor", "Asmodeus, Lord of the Nine Hells",
					"Demogorgon, Prince of Demons", "Orcus, Prince of Undeath",
					"Yeenoghu, Lord of Gnolls",
					])

				features.append(Feature("Fiend Patron",
					f"""Your pact draws on the Lower Planes, the realms of
					perdition. You forged a bargain with {patron}.
					{patron}'s aims are certainly evil, but ultimately unknown
					to you.
					""",
					"Class: Warlock"))
				features.append(Feature("Dark One's Blessing",
					f"""
					When you reduce an enemy to 0 Hit Points, you gain
					<i>Temporary Hit Points equal to your Charisma modifier plus your Warlock level</i>
					(minimum of 1 Temporary Hit Point).
					You also gain this benefit if someone else reduces an enemy within 10 feet of you to 0 Hit Points.
					""",
					"Class: Warlock"))
			if subclass == "Great Old One":
				patron = random.choice([
					"Tharizdun, the Chained God", "Zargon, the Returner",
					"Hadar, the Dark Hunger", 'Cthulhu, The Great One',
					"Yugiax, the Sleeper", "Karunash, The Fractured One",
					"Ouroboric, The Fractal of Madness",
					"Krigon, The Dream Eater",
					"Oneric, The Unfinished",
					"Ol, the Darkness", "Falaxus, The Vortex",
					"Dharana, The Permanent Storm",
					"Mokshada, The Eye Who Watches"
					"Koshal, The Unbirther", "Vajrak, The Legion of One",
					"Raktash, The White Blood","Jvaran, The Will Eater",
					"Yamraka, The Fate Unwaver", "Kushara, the Death Blossom",
					"Tharaka, the Star Eater", "Utpala, The Forgotten",
					"Dendar, the Night Serpent", "Tharizdûn, the Chained God",
					"Atropus, the World Born", "The Infinite Library"
					])

				features.append(Feature("Great Old One Patron",
					f"""You found your bind is to an unspeakable being
					from the Far Realm: {patron}. <br>
					Your Patron's aims are beyond comprehension. But you always
					feel the gaze of {patron} watching you.
					""",
					"Class: Warlock"))
				features.append(Feature("Awakened Mind",
					f"""
					You can form a telepathic connection between your mind and the mind of another. As a Bonus Action, choose one creature you can see within 30 feet of yourself. You and the chosen creature can communicate telepathically with each other while the two of you are within a number of miles of each other equal to your Charisma modifier (minimum of 1 mile). To understand each other, you each must mentally use a language the other knows.
					<br>
					The telepathic connection lasts for a number of minutes equal to your Warlock level. It ends early if you use this feature to connect with a different creature.
					""",
					"Class: Warlock"))
				features.append(Feature("Psychic Spells",
					f"""
					When you cast a Warlock spell that deals damage, you can change its damage type to Psychic. In addition, when you cast a Warlock spell that is an Enchantment or Illusion, you can do so without Verbal or Somatic components.
					""",
					"Class: Warlock"))
			if subclass == "Genie":
				random.seed(character.seed)
				patron = random.choice([
					"Dao", "Djinni", "Efreeti", "Marid"
					])

				features.append(Feature("Genie Patron",
					f"""You have made a pact with one of the rarest kinds of genie, a noble {patron} genie. Such entities rule vast fiefs on the Elemental Planes and have great influence over lesser genies and elemental creatures. Noble genies are varied in their motivations, but most are arrogant and wield power that rivals that of lesser deities. They delight in turning the table on mortals, who often bind genies into servitude, and readily enter into pacts that expand their reach.
					""",
					"Class: Warlock"))
				if patron == "Djinni":
					extra_damage = "thunder"
					vessel = random.choice([
						"ring", "necklace", "lamp", "bottle", "horn",
						'bone flute', 'pan flute', 'astrolabe',
						'mirror', 'vial of sand', 'perfume bottle',
						'silver mirror', 'quill', 'music box',
						'hourglass',   'compass', 'sundial',
						'diadem',	'tiara', 'crown', 'amulet', 'pendant',
						'coin amulet'
						])
				if patron == "Efreeti":
					extra_damage = "fire"
					vessel = random.choice([
						"ring", "necklace", "lamp", "bottle", 'incense censer',
						'lantern', 'lighter', 'spice censer', 'snuffbox',
						'spice jar', 'teapot', 'spice grinder', 'grinder',
						'medallion', "brazier",  'amulet', 'sundial', 'pendant',
						'dice', 'rosary', 'coin', 'spice shaker', 'skeleton key',
						'coin amulet', 'figurine'
						])
				if patron == "Marid":
					extra_damage = "cold"
					vessel = random.choice([
						"ring", "necklace", "lamp", "bottle", 'conch shell',
						'chalice', 'calligraphy pen', 'goblet', 'coral',
						'teapot', 'flask', 'shell horn', 'mirror',
						'locket',  'amulet', 'snowball',
						])
				if patron == "Dao":
					extra_damage = "bludgeoning"
					vessel = random.choice([
						"ring", "necklace", "lamp", "bottle", "diamond",
						'hourglass', 'game piece', 'vial of sand', 'diadem',
						'tiara', 'crown', 'book',  'amulet', 'coin', 'salt shaker',
						'dice', 'skeleton key', 'figurine'
						])
				features.append(Feature(f"Genie's Vessel",
					f"""
					Your {patron} patron gifts you an ornate {vessel}.
					A magical vessel that grants you a measure of the genie's power.
					<br>The {vessel} is a Tiny object, and you can use it
					as a spellcasting focus for your warlock spells.
					<br> While you are touching the vessel, you can use any one of its magic features.
					""",
					"Class: Warlock"))
				features.append(Feature("Bottled Respite",
					f"""
					As an action, you can magically vanish and enter your {vessel},
					which remains in the space you left. The interior of the
					vessel is an extradimensional space in the shape of a
					20-foot-radius cylinder, 20 feet high, and resembles
					your {vessel}. The interior is appointed with
					cushions and low tables and is a comfortable temperature.
					While inside, you can hear the area around your {vessel} as if you were in its space. You can remain inside the vessel up to a number of hours equal to twice your proficiency bonus. You exit the vessel early if you use a bonus action to leave, if you die, or if the vessel is destroyed. When you exit the vessel, you appear in the unoccupied space closest to it. Any objects left in the vessel remain there until carried out, and if the vessel is destroyed, every object stored there harmlessly appears in the unoccupied spaces closest to the vessel's former space. Once you enter the vessel, you can't enter again until you finish a long rest.
					""",
					"Class: Warlock"))
				features.append(Feature("Genie's Wrath.",
					f"""
					Once during each of your turns when you hit with an
					attack roll, you can deal extra {extra_damage} damage to
					the target equal to your proficiency bonus.
					""",
					"Class: Warlock"))
				features.append(Feature("The Vessel",
					f"""
					The {vessel}'s AC equals your spell save DC.
					Its hit points equal your warlock level plus your
					proficiency bonus, and it is immune to poison and
					psychic damage. <br>
					If the vessel is destroyed or you lose it, you can
					perform a 1-hour ceremony to receive a replacement
					from your patron. This ceremony can be performed
					during a short or long rest, and the previous
					vessel is destroyed if it still exists. The vessel
					vanishes in a flare of elemental power when you die.
					""",
					"Class: Warlock"))
			if subclass == "Archfey":
				patron = random.choice([
	"Aranella, the Spring Warden",
	"Sylvenor, the Summer Flame",
	"Cormora, the Autumn Harbinger",
	"Hyfira, the Winter Queen",
	"Veravor, the Leafcaller",
	"Thesmora, the Seedbinder",
	"Zarariel, the Harvest Lord",
	"Odryss, the Falling Leaf",
	"Melanth, the Frost Whisper",
	"Lethora, the Blossom Muse",

	# Twilight & Celestial
	"Duskryn, the Twilight Dancer",
	"Selvaris, the Gloaming Bard",
	"Nyxora, the Night Bloom",
	"Noctifer, the Midnight Refrain",
	"Elyndra, the Moonlit Veil",
	"Solara, the Dawn Chorus",
	"Vespera, the Evening Star",
	"Aurinel, the Morning Dew",
	"Cyranth, the Starweaver",
	"Lunora, the Silver Mirror",

	# Dreamweavers
	"Somnora, the Dreamspinner",
	"Oneira, the Sleep Maiden",
	"Morphelis, the Slumber King",
	"Hypnara, the Restless Echo",
	"Reveria, the Vision Giver",
	"Fantelis, the Reverie Keeper",
	"Euphoron, the Joyous Lapse",
	"Nemoris, the Dreaming Woods",
	"Lythara, the Wandering Sleep",
	"Viscel, the Nightshade Poet",

	# Floral Courts
	"Thalinor, the Vine Lord",
	"Mimora, the Petal Rain",
	"Brythos, the Bloom King",
	"Sylphine, the Whispering Grass",
	"Oakrath, the Ancient Bough",
	"Ivoria, the Hanging Moss",
	"Faylira, the Thorn Queen",
	"Roselorn, the Blush Blossom",
	"Bramoth, the Brambleheart",
	"Fernara, the Spore Dancer",

	# Bestial Lieges
	"Bramorin, the Deer Prince",
	"Lupell, the Wolf Stalker",
	"Fayhune, the Fox Trickster",
	"Ravelen, the Crow Mystic",
	"Serpentis, the Snake Charmer",
	"Hawkris, the Sky Hunter",
	"Wollara, the Bear Guardian",
	"Staglyn, the Antlered Sage",
	"Tigrisi, the Owl Seer",
	"Falinox, the Night Panther",

	# Watersprites
	"Aqualis, the River Singer",
	"Marinth, the Ocean Embrace",
	"Coralyn, the Reef Enchantress",
	"Tideon, the Sea Wanderer",
	"Pearlion, the Depth Whisperer",
	"Ebbryl, the Flowing Veil",
	"Brinora, the Salt Dream",
	"Surian, the Shore Guardian",
	"Druelon, the Wavecaller",
	"Nimora, the Tide Weaver",

	# Windsingers
	"Breezea, the Cloud Dancer",
	"Zephyros, the Gale Singer",
	"Stormora, the Tempest Herald",
	"Mistran, the Wind Whisperer",
	"Gustael, the North Wind",
	"Sirenae, the Whispering Draft",
	"Cyclonis, the Spinning Puff",
	"Vaylora, the Updraft Weaver",
	"Ciros, the Zephyr Scout",
	"Aeralis, the Sighing Sky",

	# Light & Shadow
	"Luminar, the Dawnbringer",
	"Shadeha, the Night Veil",
	"Eclipser, the Shadow Kiss",
	"Radiant, the Sunblade",
	"Umbrae, the Shade Siren",
	"Glisara, the Gleam Maiden",
	"Veloris, the Velvet Dark",
	"Photalis, the Light Warden",
	"Shadera, the Twilight Shard",
	"Aurorix, the Radiant Crown",

	# Fire & Frost
	"Scorchor, the Flameborne",
	"Frosthen, the Iceheart",
	"Embera, the Wildfire",
	"Glacior, the Frost Herald",
	"Ashrono, the Cinder Muse",
	"Chillara, the Winter Song",
	"Blazara, the Blazeheart",
	"Snowtal, the Crystal Frost",
	"Pyronis, the Ember Lash",
	"Icelyn, the Snow Veil",

	# Cosmic & Arcane
	"Starforgia, the Celestial Smith",
	"Cometra, the Sky Dart",
	"Orbiona, the Sphere Maiden",
	"Nebulina, the Mistborn",
	"Galactra, the Dreamsilver",
	"Solandra, the Sun Thread",
	"Meteora, the Falling Star",
	"Auroriel, the Polar Flame",
	"Cosmora, the Vast Song",
	"Astronyx, the Starshard",

	"Titania, Queen of the Summer Court",
	"Oberon, King of the Gloaming",
	"The Queen of Air and Darkness",
	"Hyrsam, Prince of Fools",
	"The Green Lord",

						])
				features.append(Feature("Archfey Patron",
					f"""Your pact draws on the power of the Feywild.
					 You forged a bargain with {patron}.
					{patron} is often inscrutable and whimsical.
					""",
					"Class: Warlock"))
				features.append(Feature("Steps of the Fey",
					f"""
{patron} grants you the ability to move between the boundaries of the planes.
You can cast <i>Misty Step</i> without expending a spell slot a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.
					""",
					"Class: Warlock"))
				features.append(Feature("Steps of the Fey Option",
					f"""
					Whenever you cast <i>Misty Step</i> you can choose one additional effect:
1>
<li><b> Refreshing Step.</b> Immediately after you teleport, you or one creature you can see within 10 feet of yourself gains 1d10 Temporary Hit Points.
</ul>					""",
					"Class: Warlock"))
				features.append(Feature("Steps of the Fey Option",
					f"""
					Whenever you cast <i>Misty Step</i> you can choose one additional effect.
<ul>
<li><b> Taunting Step.</b> Creatures within 5 feet of the space you left must succeed on a Wisdom saving throw against your spell save DC or have Disadvantage on attack rolls against creatures other than you until the start of your next turn.
</ul>					""",
					"Class: Warlock"))


		if level >= 6:
			if subclass == "Archfey":
				features.append(Feature("Misty Escape",
					f"""
You can cast <i>Misty Step</i> as a <b>Reaction</b> in response to taking damage.
					""",
					"Class: Warlock"))
				features.append(Feature("Steps of the Fey Option",
					f"""
					Whenever you cast <i>Misty Step</i> you can choose one of the following additional effects.
<ul>
<li><b>Disappearing Step.</b> You have the <i>Invisible</i> condition until the start of your next turn or until immediately after you make an attack roll, deal damage, or cast a spell.
</ul>					""",
					"Class: Warlock"))
				features.append(Feature("Steps of the Fey Option",
					f"""
					Whenever you cast <i>Misty Step</i> you can choose one additional effects.
<ul style="list-style-type: '🪬'">
<li><b>Dreadful Step.</b> Creatures within 5 feet of the space you left or the space you appear in (your choice) must succeed on a Wisdom saving throw against your spell save DC or take 2d10 Psychic damage.
</ul>					""",
					"Class: Warlock"))
			if subclass == "Fiend":
				features.append(Feature("Dark One's Own Luck",
					f"""
You can call on your fiendish patron to alter fate in your favor.
When you make an ability check or a saving throw, you can use this
feature to <b>add 1d10 to your roll</b>. You can do so after seeing the
 roll but before any of the roll's effects occur.
<br>
You can use this feature a number of times equal to your
Charisma modifier (minimum of once), but you can use it
no more than once per roll. You regain all expended uses
when you finish a Long Rest.					""",
					"Class: Warlock"))
			if subclass == "Great Old One":
				features.append(Feature("Clairvoyant Combatant",
					f"""
When you form a telepathic bond with a creature using your
Awakened Mind, you can force that creature to make a Wisdom
saving throw against your spell save DC. On a failed save,
the creature has Disadvantage on attack rolls against you,
and you have Advantage on attack rolls against that creature
for the duration of the bond.
<br>
Once you use this feature, you can't use it again until you
finish a Short or Long Rest unless you expend a Pact Magic
spell slot (no action required) to restore your use of it.					""",
					"Class: Warlock"))
			if subclass == "Genie":
					features.append(Feature("Elemental Resistance",
						f"""
						You have resistance to {extra_damage} damage.
						""",
						"Class: Warlock"))
					features.append(Feature("Elemental Gift",
						f"""
As a bonus action, you can give yourself a flying speed of 30 feet that lasts for 10 minutes, during which you can hover.
<br> You can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.
						""",
						"Class: Warlock"))
			if subclass == "Celestial":
				features.append(Feature("Radiant Soul",
					f"""
					Your link to your patron allows you to serve as a conduit for radiant energy. You have Resistance to Radiant damage. Once per turn, when a spell you cast deals Radiant or Fire damage, you can add your Charisma modifier to that spell's damage against one of the spell's targets.

					""",
					"Class: Warlock"))

		if level >= 9:
			from AtlasMagia.Lodge_of_Spells import ContactOtherPlane
			features.append(Feature("Contact Patron",
				f"""
In the past, you usually contacted your patron through intermediaries. Now you can communicate directly; you always have the Contact Other Plane spell prepared. With this feature, you can cast the spell without expending a spell slot to contact your patron, and you automatically succeed on the spell's saving throw.
<br>
Once you cast the spell with this feature, you can't do so in this way again until you finish a Long Rest.
<div class="npc-textbox">{ContactOtherPlane}</div>
				""",
				"Class: Warlock"))
		if level >= 10:
			if subclass == "Archfey":
				features.append(Feature("Beguiling Defenses",
					f"""
Your patron teaches you how to guard your mind and body. You are immune to the Charmed condition.

In addition, immediately after a creature you can see hits you with an attack roll, you can take a Reaction to reduce the damage you take by half (round down), and you can force the attacker to make a Wisdom saving throw against your spell save DC. On a failed save, the attacker takes Psychic damage equal to the damage you take. Once you use this Reaction, you can't use it again until you finish a Long Rest unless you expend a Pact Magic spell slot (no action required) to restore your use of it.
					""",
					"Class: Warlock"))
			if subclass == "Celestial":
				features.append(Feature("Celestial Resilience",
f"""
You gain Temporary Hit Points whenever you use your Magical Cunning feature or finish a Short or Long Rest.
These Temporary Hit Points equal your Warlock level plus your Charisma modifier.
Additionally, choose up to five creatures you can see when you gain the points.
Those creatures each gain Temporary Hit Points equal to half your Warlock level
plus your Charisma modifier.
""",
					"Class: Warlock"))
			if subclass == "Great Old One":
				from AtlasMagia.Lodge_of_Spells import Hex
				features.append(Feature("Eldritch Hex",
					f"""
Your alien patron {patron} grants you a powerful curse.
You always have the Hex spell prepared. When you cast Hex
and choose an ability, the target also has Disadvantage on
saving throws of the chosen ability for the duration of the spell.
<div class="npc-textbox">{Hex}</div>

""",
					"Class: Warlock"))
				features.append(Feature("Thought Shield",
					f"""
Your thoughts can't be read by telepathy or other means unless you allow it.
You also have Resistance to Psychic damage, and whenever a creature deals
Psychic damage to you, that creature takes the same amount of damage that you take.
					""",
					"Class: Warlock"))
			if subclass == "Fiend":
				features.append(Feature("Fiendish Resilience",
					f"""
					Choose one damage type, other than Force, whenever you finish a Short or Long Rest. You have Resistance to that damage type until you choose a different one with this feature.
					"""
					"Class: Warlock"))

			if subclass == "Genie":
				features.append(Feature("Sanctuary Vessel",
					f"""
When you enter your Genie's Vessel, the {vessel} via the Bottled Respite
feature, you can now choose up to five willing creatures that you
can see within 30 feet of you, and the chosen creatures are
drawn into the vessel with you.
<br>
As a bonus action, you can eject any number of creatures from
the vessel, and everyone is ejected if you leave or die or
if the vessel is destroyed.
<br>
In addition, anyone (including you) who remains within the {vessel}
for at least 10 minutes gains the benefit of finishing
a short rest, and anyone can add your proficiency bonus
 to the number of hit points they regain if they spend any
  Hit Dice as part of a short rest there.
					""",
					"Class: Warlock"))

		if level >= 14:
			if subclass == "Archfey":
				features.append(Feature("Bewitching Magic",
					f"""
Your patron grants you the ability to weave your magic with teleportation. Immediately after you cast an Enchantment or Illusion spell using an action and a spell slot, you can cast Misty Step as part of the same action and without expending a spell slot.
""",
					"Class: Warlock"))
			if subclass == "Celestial":
				features.append(Feature("Searing Vengeance",
f"""
When you or an ally within 60 feet of you is about to make a Death Saving Throw, you can unleash radiant energy to save the creature.
The creature regains Hit Points equal to half its Hit Point maximum and can end the Prone condition on itself.
Each creature of your choice that is within 30 feet of the creature takes Radiant damage equal to 2d8 plus your Charisma modifier,
and each has the Blinded condition until the end of the current turn. <br>
Once you use this feature, you can't use it again until you finish a Long Rest.
""",
					"Class: Warlock"))
			if subclass == "Great Old One":
				features.append(Feature("Create Thrall",
					f"""
When you cast Summon Aberration, you can modify it so that it doesn't require Concentration. If you do so, the spell's duration becomes 1 minute for that casting, and when summoned, the Aberration has a number of Temporary Hit Points equal to your Warlock level plus your Charisma modifier.
<br>
In addition, the first time each turn the Aberration hits a creature under the effect of your Hex, the Aberration deals extra Psychic damage to the target equal to the bonus damage of that spell.""",
					"Class: Warlock"))
			if subclass == "Fiend":
				features.append(Feature("Hurl Through Hell",
					f"""
Once per turn when you hit a creature with an attack roll, you can
try to instantly transport the target through the Lower Planes.
The target must succeed on a Charisma saving throw against your
spell save DC, or the target disappears and hurtles through a
nightmare landscape. The target takes <b>8d10 Psychic damage</b> if it
isn't a Fiend, and it has the Incapacitated condition until the
end of your next turn, when it returns to the space it previously
occupied or the nearest unoccupied space.
<br>
Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a Pact Magic spell slot (no action required) to restore your use of it.
					"""
					"Class: Warlock"))
			if subclass == "Genie":
				features.append(Feature("Limited Wish",
					f"""
You entreat your patron to grant you a small wish. As an action,
 you can speak your desire to your Genie's Vessel, requesting
 the effect of one spell that is 6th level or lower and has
 a casting time of 1 action. The spell can be from any class's
 spell list, and you don't need to meet the requirements in
 that spell, including costly components; the spell simply
 takes effect as part of this action.
<br>
Once you use this feature, you can't use it again until you
finish 1d4 long rests.
""",
					"Class: Warlock"))

		if level >= 19:
			feats = ApplyEpicBoon(character)
			features.extend(feats)

		if level >= 20:
			features.append(Feature("Eldritch Master", 
				"""When you use your Magical Cunning feature, you regain all your expended Pact Magic spell slots.""",
				"Class: Warlock"))

		self.prepare_invocations()
		features.extend(getattr(character, "invocations", []))

		for asi_level in [4,8,12,16,19]:
			if level >= asi_level:
				features.extend(ApplyRandomFeats(character, n=1))

		return features
