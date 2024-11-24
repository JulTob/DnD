import random



def Player_Species():
	result = random.choices(list(player.keys()), weights=player.values(), k=1)[0]
	return result

race_weights = {
"Aberration":   150, #
"Aven":         150, #
"Beast":        110,
"Beastfolk":    170,
"Catfolk":      130,
"Celestial":    151,
"Construct":    150,
"Dragon":       150,
"Dwarf":        170, # Based on the Spanish Golden Age (Conquistadores), Italians, Portuguese and Latino and Criollo Culture.
"Elemental":    150,
"Elf":          170, # Based on Nordic Fae, Vikings, Iceland, Romani, Celtic Ireland, Persian
"Fey":          150,
"Fiend":        150,
"Giant":        150,
"Gnome":        160,
"Goblin":       160,
"Halfling":     190, # Based on English and French Medieval Peasants
"Human":        200,
"Kobold":       160,
"Lizardfolk":   150,
"Monstrosity":  150,
"Ooze":         150,
"Orc":          180,
"Plant":        150,
"Snakefolk":    150,
"Undead":       180,
"": 			  0,
		}




def Race():
	result = random.choices(list(race_weights.keys()), weights=race_weights.values(), k=1)[0]
	return result

def Aberrations():

	Names = {
		"Aboleth": 5,			# Immortal creatures of the Depths of the Sea and the Astral Sea
		"Beholder": 12,          # Known for their paranoia and individualism.
		"Shapeshifters": 3,     # Unique appearance as Mimics and shapeshifters with horrible true forms.
		"Illithid": 9,          # A highly intelligent race known for their psionic powers.
		"Old One": 	7,          # Ancient beings with vast knowledge and a desire to dominate other species.
		"Mindhive": 4,          # They seek knowledge and union by asimilation.
		"Depth Dominators": 5,  # Slave traders with a unique hierarchy.
		"Living Spell": 7,      # Former wizards transformed into monstrous forms.
		"Chaos Warper": 5,      # Cosmic horror element. Representing pure chaos, they're unpredictable.
		"Alien Spawn": 5,       # Cosmic horror element.
		"Parasyte": 4,          # Parasitic entities that can control other beings.
		"Symbioid": 4,          # Simbioit entities that can enhance and commune with other beings.
		"Destiny Devouers": 4,  # Time-traveling and body-swapping aliens.
		"Githyanki": 7,         # Raiders and conquerors.
		"Githzerai": 7,         # More enlightened.
		"Eldritch Horror": 7,	# Cuthulhu inspired civilization
		}

	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Avens():
	Names = {
		"Birdfolk": 7,    # Generic birdfolk, versatile in nature.
		"Kenku": 11,      # Unique mimicry ability and urban setting.
		"Aarakocra": 8,   # High-flying and more spiritual.
		"Tengu": 6,       # Martial arts and japanese folklore connections.
		"Raptoran": 5,    # Mountain dwellers with a unique fast flight.
		"Owlin": 5,       # Owl-like Nocturnal and wise.
		"Harpy": 17,      # Half-bird, half-woman, often seen as omens.
	}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Beasts():
	'''
	Are nonhumanoid creatures that are a natural
	part of the fantasy ecology. Some of them have magical
	powers, but most are unintelligent and lack any society
	or language. Beasts include all varieties of ordinary
	animals, dinosaurs, and giant versions of animals.
	'''
	Names = {
		"Armored Bear": 8,          # From Philip Pullman's His Dark Materials series.
		"Monkey King": 9,
		"Kong": 7,
		"Kaiju": 7,
		"Giant Eagle": 8,
		"Golden Lion": 7,
		"White Tiger": 6,
		"Vulture Spirit": 5,
		"Kitsune Fox": 10,
		"Deer Spirit": 6,           # Associated with gentleness and intuition in various cultures.
		"Giant Owl": 8,
		"Primal Stag": 7,        # Stags are often seen as messengers or connected to the otherworld in various mythologies.
		"Fenrir Wolf": 7,
		"Forest God": 5,            # A guardian of the forests, revered for its bravery.
		"Star Whale": 6,
		"Kaiju Dinosaur": 6,
		"Kerberus Dog": 7,
		"Sun Scarab": 9,
		"Moon Jackal": 6,
		"Spider Queen": 7,
		"Ouroboros' Spawn": 7,
		"Elder Elephant": 8 ,
		"Pandamonium": 7 ,
		"":0}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Beastfolks():
	Names = {
		"Arachnidfolk": 16,     # Spiders are often associated with trickery and weaving fate.
		"Centaur": 19,          # Classic mythological creature, representing the wild side of humanity.
		"Elephantian": 13,		# Elephant and mammoth folks.
		"Gnoll": 16,            # Often seen as savage and chaotic, inspired by hyenas.
		"Insectfolk": 15,       # Unique and diverse, representing both hive minds and individuality.
		"Jackalmen": 16,        # Often seen in Egyptian mythologies, associated with the afterlife.
		"Kitsune": 18,          # Japanese fox spirits, both mischievous and wise.
		"Lycan": 17,            # General term for were-creatures, known for their cursed transformations.
		"Merfolk": 19,          # Classic creatures of the sea, representing both beauty and danger.
		"Minotaur": 18,         # The embodiment of the labyrinth's mystery and challenge.
		"Ratfolk": 17,          # Clever, opportunistic, and often seen in urban settings.
		"Scorpionfolk": 15,     # Dangerous and venomous, often used as guardians in myths.
		"Sharkfolk": 17,        # Predators of the sea, representing both fear and respect.
		"Skinwalker": 15,
		"Werebear": 16,         # A more noble version of lycanthropes, often associated with strength and protection.
		"Werewolf": 20,         # One of the most recognized lycanthropes, representing the untamed side of humanity.
		"Satyr": 18,            # Revelers and musicians, representing the carefree side of nature.
		"": 0
		}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Catfolks():
	Names = {
		"Leonid": 		15,
		"Pantherian": 	12,
		"Felinian": 	11,
		"Lynxen": 		13,
		"Leopardian": 	12,
		"Tigrisian": 	12,
		'Jaguarfolk':	10,
		'Puman': 8,
		"": 0
		}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Celestials():
	'''
	Celestials are creatures native to the Upper Planes.
	Many of them are the servants of deities, employed
	as messengers or agents in the mortal realm and
	throughout the planes. Celestials tend to be good by nature,
	so the exceptional celestial who strays from a good
	alignment is a horrifying rarity. Celestials include
	angels, couatls, and pegasi.
	'''
	Names = {
		"Angelic Bloodline": 32,   # Mortals with celestial ancentry
		"Half-Angel": 22,          # Mortals with a celestial parent
		"Angel": 19,               # Classic representatives of good, messengers of deities.
		"Ascended": 18,            # Mortals who have risen to a divine or semi-divine status.
		"Saint": 18,               # Mortals with trascendent connections with the divine.
		"Couatl": 17,              # Feathered serpents, often seen as guardians or protectors.
		"Forgotten God": 16,       # Once powerful, now forgotten. Represents the ebb and flow of faith.
		"Lesser God": 18,          # Deities of minor aspects or domains.
		"Tutelar": 18,         	   # Local deities with limited influence.
		#"Pegasus": 17,            # The majestic winged horse, symbol of purity and grace.
		"Planetar": 19,            # High-ranking angels, often seen as warriors of good.
		"Seraph": 19,              # Burning ones, highest order of angels.
		"Throne": 18,              # Angels associated with celestial justice and maintaining the cosmic order.
		"Unicorn": 17,             # Pure and gentle creatures, often associated with forests and healing.
		"Celestial Serpent": 18,   # Serpentine creatures that reside in the heavens, symbols of power and majesty.
		"Valkyrie": 28,            # Choosers of the slain, guiding heroes to the afterlife.
		"Solar": 19,               # Extremely powerful celestial beings, champions of deities.
		"Ki-rin": 17,              # Eastern counterpart to unicorns, symbols of wisdom.
		"Deva": 18,                # Divine beings in Hindu mythology, often in conflict with Asuras.
		"Asura": 18,               # Divine beings in Zoroastrian mythology, often in conflict with Devas.
		"Archon": 18,              # Beings of pure law and good, often in opposition to demons and devils.
		"Archangel": 15,
		"Avatar": 15,              # Mortal form of a God
		}

	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Constructs():
	'''
	Constructs are made, not born. Some are
	programmed by their creators to follow a simple set of
	instructions, while others are imbued with sentience
	and capable of independent thought. Golems are the
	iconic constructs. Many creatures native to the outer
	plane of Mechanus, such as modrons, are constructs
	shaped from the raw material of the plane by the will of
	more powerful creatures.
	'''
	Names = {
		"Animated Armor": 8,         # Empty suits of armor brought to life, often as guardians.
		"Drone": 7,                  # Modern or futuristic unmanned devices, often for reconnaissance.
		"Golem": 9,                  # Beings made from inanimate material, like clay or stone. Classic magic constructs.
		"Homunculus": 7,             # Full Metal Alchemist's style created humanoids.
		"Robot": 7,                  # Mechanical Slave
		"Android": 6,                # Homanoid Constructs
		"Scarecrow": 7,              # Animated scarecrows, often created to protect crops but can be sinister.
		"Clockwork": 8,              # Intricate mechanical beings, often steampunk-inspired.
		"Warforged": 9,              # Sentient constructs made for war, often searching for purpose after conflict.
		"Modron": 8,                 # Geometrically inspired beings from a plane of utter order.
		"Shield Centinel": 8,        # Created to protect its creator, often bound by an amulet.
		"Origami Spell": 7,          # Animated books or beings made of paper, protecting knowledge.
		"Effigy": 8                  # Ritualistic statues or figures, animated for various purposes.
		}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


DragonColors = {
		"Black": 18,               # Chromatic, acid breath.
		"Blue": 18,                # Chromatic, electric breath.
		"Green": 18,               # Chromatic, poison breath.
		"Red": 18,                 # Chromatic, fire breath.
		"White": 18,               # Chromatic, cold breath.
		"Bronze": 17,              # Metallic, good-aligned, lightning breath.
		"Silver": 17,              # Metallic, cold/paralyzing breath.
		"Gold": 17,                # Metallic, fire/weakening breath.
		"Brass": 17,               # Metallic, fire/sleep breath.
		"Copper": 17,              # Metallic, acid/slowing breath.
		"Shadow": 16,              # Tainted by Shadowfell, necrotic breath.
		"Gem": 16,                 # Rare, associated with gemstones and psionics.
		"Ethereal": 15,            # From the Ethereal Plane.
		"Planar": 15,              # Associated with specific planes.
		"Prismatic": 13 ,           # Rare and extremely powerful, known for multi-colored, rainbow-like powers.
		}

def Dragons():
	'''
	Dragons are large reptilian creatures of ancient origin
	and tremendous power. True dragons, including the
	good metallic dragons and the evil chromatic dragons,
	are highly intelligent and have innate magic. Also in this
	category are creatures distantly related to true dragons,
	but less powerful, less intelligent, and less magical, such
	as wyverns and pseudodragons.
	'''
	DragonTypes = {
		"Dragonborn": 33,         # Dragon-like humanoids.
		"Wyrm": 20,
		"Drake": 17,
		"Draco": 16,
		"Dragon": 18,
		"Sky Serpent": 15,
		"Half Dragon": 14,
		"Dragon Turtle": 14,
		"Centenary": 11,        # Old Dragons
		"Millenary": 11,        # Ancient Dragons
		"Wyvern": 15,           # 2 leged Dragons
		"Long": 13,             # Dragons of asian mythology
		"Drakon": 13,           # Dragons of greek mythology
		}


	# Pick one from each category
	chosen_type = random.choices(list(DragonTypes.keys()), weights=DragonTypes.values(), k=1)[0]
	chosen_color = random.choices(list(DragonColors.keys()), weights=DragonColors.values(), k=1)[0]

	return f"{chosen_color} {chosen_type}"

def Elementals():
	'''
	Elementals are creatures native to the elemental
	planes. Some creatures of this type are little more than
	animate masses of their respective elements, including
	the creatures simply called elementals. Others have
	biological forms infused with elemental energy. The
	races of genies, including djinn and efreet, form the
	most important civilizations on the elemental planes.
	Other elemental creatures include azers, invisible
	stalkers, and water weirds.
	'''
	Names = {
		"Atlantian": 10,     # Connection to water and ancient crystal technology.
		"Chronian": 7,       # Time elementals
		"Cronusian": 6,      # Representing time and age.
		"Eosian": 	9,       # Tied to the rising sun.
		"Etherian": 9,       # Ether and the heavenly shine.
		"Gaian": 	10,      # Essence of the earth.
		"Galaxian": 9,       # Elemental related to constellations and stars.
		"Genasi": 	21,      # Representing air, earth, fire, and water.
		"Genie": 	11,      # Powerful primordial entities.
		"Hyperian": 8,       # Radiant, solar-powered.
		"Magmaforged": 10,   # Fusion of earth and fire.
		"Oceanians": 10,     # Depths, tides, storms.
		"Primordial": 8,     # Fundamental forces of reality.
		"Promethean": 9,     # Fire, electricity, and energy, with spirit of innovation.
		"Salamandrian": 4,   # Associated with fire.
		"Nymphian":		4,	 # Water elementals
		"Sylphians": 	4,   # Air elementals
		"Pigmians":		4,	 # Earth Elementals
		"Tartarian": 9,      # Dark ocean depths.
		"Titan": 9,          # Raw elemental power.
		"Tundran": 9,        # Harsh icy landscapes.
		"Uranians": 9,       # Sky, stars, celestial magic.
		"Zephyrian": 10,     # Gentle airs.
		"Djinn": 4,			 # Beings with fire in their eyes, they live in the dessert and ride cyclons.
		}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Fiends():
	'''
	Fiends are creatures that are native
	to the Lower Planes. A few are the servants of deities,
	but many more labor under the leadership of archdevils
	and demon princes. Evil priests and mages sometimes
	summon fiends to the material world to do their bidding.
	Fiends include demons, devils, rakshasas...
	Devils are are related to Guilt, Sin, Desire, Punishment, and Retrivution.
	Demons are related to Chaos, Vanity, Ego, Lust, Change, Sickness, and War.
	Devils are the
	'''
	Names = {
		"Tiefling": 30,
		"Devil": 17,
		"Demon": 17,
		"Imp": 		13,
		"Cubus": 8,
		"Incubus": 8,
		"Succubus": 8,
		"Concubus": 7,
		"Dwarvendevil": 5,
		"Elvendevil": 5,
		"Gnolldevil": 5,
		"Orkishdevil": 5,
		"Goblindevil": 5,
		"Dwarvendemon": 4,
		"Elvendemon": 4,
		"Demongnoll": 4,
		"Orkishdemon": 4,
		"Goblindemon": 4,
		"Nightmare": 8,
		"Rakshasa": 10,
		"Fallen Angel": 11,
		"Hellbound Hunter": 9,
		"Leviathan": 7,
		"Behemoth": 7,
		"Shinigami":10,
		"Hell's Rider": 10,
		"Soul Collector": 8,
		"Infinder": 7,
		"Sinvestigator": 6,
		"Chaoslord": 7,
		"Justiciar": 8,
		"Vengeance Spirit": 7,
		"Retributioner": 7,
		"Pact Enforcer": 8,
		"Soulclaimer": 8,
		"Infernal Enforcer": 8,
		"Inforcer": 8,
		"Dark Gods": 1
		}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Feys():
	'''
	Fey are magical creatures closely tied to the realm of Dreams.
	They dwell in twilight groves and misty forests, merging From
	both the personal and the collective uncunscious. Some may
	produce nightmares, such as hags, while other bliss and joy,
	as Pixies do. From daydreaming to life-long dreams, they take
	a part on all of mortal's fantasies.
	They are closely tied to folklore, legends, and mythology.
	In some worlds, they are closely tied to the Feywild, also
	called The Dream.
	Fey include dryads, pixies, and satyrs.
	'''
	Names = {
		"Hag": 10,       # Witches often associated with dark magic
		"Nymph": 12,     # Spirits of nature: water, forest, etc.
		"Pixie": 10,     # Tiny, mischievous spirits
		"Satyr": 12,     # Half-man, half-goat
		"Sprite": 9,    # Airy spirits similar to pixies but usually less mischievous
		"High Fae": 7,  # Powerful fey lords and ladies
		"Redcap": 6,    # Malicious goblin-like creatures
		"Banshee": 6,   # Spirits heralding death
		"Leprechaun": 8,  # Mischievous little fey associated with pots of gold
		"Changeling": 6,  # Fey child left in place of a stolen human child
		"Nexus Fey": 7,       # Fey connected to a connection point
		"Duende": 6,          # Fey of the arts, beauty, and nature. Tricksters.
		"Home Lares": 5,      # Guardians of homes and families
		"Fata": 2,          # Fae that intervine in someone's fate, providing luck
		"Moira": 2,         # Fae guide someone's fate, spinning the fabric of life
		"Parcae": 2,         # Fae omen of death, they come to cut the thread of life.
		"Archfey": 1,       # Fae of Enormous significance, akin to gods in the feywild
	}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Giants():
	Names = {
		"Goliath": 20,				# Half Giants
		"Firbolg": 12,				# Tree hugging semigiants
		"Cyclops":  9,              # Greek one-eyed giants
		"Ogre":     11,             # Brutish man-eaters
		"Troll":    10,             # Norse mountain dwellers
		"Jotunn (Frost Giant)": 8,  # Norse primal giants
		"Fire Giant": 8,            # Inhabitants of Muspelheim
		"Gigantes": 7,              # Giants from Greek mythology
		"Nephilim": 6,              # Biblical giants
		"Oni":      10,             # Japanese ogre-like giants
		"Ettin (Two headed)": 7,        # English two-headed giants
		"Fomorians (Sea Giants)": 6,    # Irish sea giants
		"Cloud Giant": 8,           # Noble sky dwellers
		"Stone Giant": 8,           # Earthy, rocky giants
		"Storm Giant": 7,               # Majestic tempest giants
	}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Gnomes():
	Names = {
		"Mountain": 9,
		"Forest": 9,
		"Garden": 2,
		"Tinker": 5,
		"Crossroad": 4,
		"Wandering": 4,
		"Leprechaun": 2,
	}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Goblins():
	Names = {
		"Goblin": 17,                       # Mischievous green-skinned creatures
		"Hobgoblin": 10,                     # Disciplined, militant goblinoids
		"Bugbear": 9,                       # Stealthy brutes of the goblinoid family
		"Gremlin (Tecnogoblin)": 8,         # Saboteurs of machinery
		"Redcap": 7,                        # Bloodthirsty goblin-like fey
		"Nyk (Watergoblin)": 8,             # Slavic water-dwelling goblins
		"Trow (Dark goblin)": 7,            # Orcadian mischief-makers
		"Knocker (Underdark goblin)": 8,    # Cornish mine-dwelling creatures
		"Domovoi (House Goblin)": 7,         # Slavic house spirits
		}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Humans():
	Types = {
		"Local":        30,
		"Foreigner": 	25,
		"Highlander": 	20,
		"Nomad": 		20,
		"Islander": 16,
		"Forester": 16,
		"Plainsfolk": 15,
		"Urbanite":14,
		"Northerner":20,
		"Southerner": 20,
		"Easterner":20,
		"Westerner":20,
		}

	chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]

	return f"{chosen_type} "

def Monstrosities():
	Names = {
		"Chimera": 	18,
		"Doppelganger": 18,
		"Shapeshifter": 10,
		"Gorgon": 17,
		"Horror": 16,
		"Sphynx": 17,
		"Wendigo": 13,
		"Kraken": 15,
		"Nightmare": 10
	}
	chosen_type = random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]
	return chosen_type

def Oozes():
	Types = {
		"Plasmoid": 18,      # Ooze people from space
		"Abominational": 18, # From the Abomi-Nation. Owl House's Darius Deamonne and alike.
		"Globkin": 18,       # Standard, amorphous entity.
		"Blobfolk": 18,      # Standard, amorphous entity.
		"Slimeling": 18,     # Slightly more fluidic, might move faster
		"Gelatoid": 17,      # More gelatinous and transparent
		"Waxian": 15,        # Thicker, more aggressive.
		"Adhesians": 14,     # Sticky and adhesive, might trap prey.
		"Cuborg": 19,        # Shaped as squares, minecraft style
	}

	Properties = {
		"Gray": 7,
		"Ochre": 5,
		"Black": 6,
		"Magma": 4,
		"Crystal": 4,
		"Corrosive": 7,
		"Frost": 5,
		"Eldritch": 3,
		"Luminous": 6,
		"Toxic": 6,
	}

	chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]
	chosen_property = random.choices(list(Properties.keys()), weights=Properties.values(), k=1)[0]

	return f"{chosen_property} {chosen_type}"

def Orcs():
	Names = {
		"Mountain": 5,
		"Desert": 5,
		"Swamp": 6,
		"Snow": 4,
		"Uruk": 6,
		"Half-Orc": 7,
		"Orog (Underdark)": 5,
		"Cave": 6,
		"Forest": 6,
		"Nomadic": 7,
		"Island": 6,
		"Urbanite": 9,
		"Feral": 7

	}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Plants():
	Names = {
		"Willow Guardian": 10,
		"Treant": 12,
		"Awakened Tree": 12,
		"Forefather Oak": 10,
		"Myconid Sovereign": 10,
		"Ent": 12,
		"Treefolk": 10,
		"Floral Walkers": 10,
		"Living Totem": 10,
		"Walker Vine": 12,
		"Singing Lotus": 10,
		"Lichen Gravetaker": 10,
		"Cactoid Nomad": 9,
		"Vegetation Abomination":9,
		"Dryad":18,
		"Fungical Intellectual": 8,
		"Myceliumanoid": 8,

	}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Undeads():
	Names = {
			"Cursed Eternal": 12,        # Mindless undead, driven by a hunger for the living.
			"Death Knight": 10,          # Elite undead warriors, remnants of former knights or warlords.
			"Despair Specter": 14,       # Souls that suffered tremendous despair, wishing the same for the living.
			"Fear Shadow": 12,           # Undead born from intense fear, lurking in darkness.
			"Honor Phantom": 12,         # Ethereal spirits bound by duty or a promise made in life.
			"Lich": 20,                  # Undying mages who sought eternal life through dark rituals.
			"Mischief Poltergeist": 12,  # Playful spirits, causing disturbances to attract attention.
			"Penance Wraith": 10,        # Souls seeking atonement for sins committed in life.
			"Pride Mummy": 12,           # Preserved dead, animated to guard ancient tombs and relics.
			"Protector Spirit": 14,      # Benevolent spirits still guarding a place, object, or person.
			"Ungone Ghost": 13,       # Souls trapped due to unfinished business or profound regrets.
			"Skeleton Protector": 14,    # Animated skeletal guardians, defending locations or treasures.
			"Thinker Skull": 12,         # Knowledgeable remnants, often used by dark mages for counsel.
			"Tomb's Hoarder": 10,        # Guardians of burial sites, obsessed with their treasures.
			"Vampire": 22,               # Bloodsucking undead, intelligent and driven by hunger and desire.
			"Vengeful Revenant": 10,     # Resurrected by sheer force of will to enact revenge.
			"Weeping Howler": 10,        # Spirits that mourn and wail, often announcing death.
			"Wrathful Wraith": 12,                # Souls consumed by anger, seeking to draw others into death.
			}
	return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Elves():
	Types = {
		"High Elf": 18,
		"Sylvan Elf": 18,
		"Wood Elf": 18,
		"Dark Elf": 18,
		"Night Elf": 11,
		"Feywild Elf": 8,
		"Shadow Elf": 8,
		"Sea Elf": 13,
		"Nomad Elf": 13,
		"Snow Elf":8,
		"Sun Elf": 6,
		"Eclipse Elf":4,
		"Moon Elf": 6,
		"Wild Elf": 6,
		"Urban Elf": 13,
		"Sands Elf": 10,
		"Eladrin": 3,
		}

	chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]

	return f"{chosen_type} "

def Halflings():
	Types = {
		"Hill": 16,         # Traditional, close to nature
		"Stout": 16,        # Hardy, often living near dwarves
		"Riverfolk": 12,    # Skilled in fishing and water navigation
		"Ghostwise": 8,     # Mysterious, telepathic abilities
		"Wanderlust": 6,    # Always traveling, rarely settle
		"Treetop": 6,       # Live in trees, skilled climbers
		"Urban": 10,        # Adapted to city life
		"Desert": 6,        # Survive in arid climates, resourceful
		"Frost": 4,         # Resilient in cold environments
		"Island": 4,        # Island dwellers, adept at swimming
		"Sky": 3,           # Dreamers, good with birds and heights
		"Solarpunks": 3,    # Anarchists, Live in harmony with flora, great herbalists and tinkerers
		"Sunrise": 2,       # Optimistic, early risers
		"Collectivians": 2, # “Together, we thrive.”. Strength by unions. Democratic.
		"Libertarians": 2,  # 'Personal responsibility'
		
		}

	chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]

	return f"{chosen_type} "

def Dwarfs():
	Types = {
		"Mountain": 	20,
		"Conquistador": 10,
		"Seawolf": 		10,
		"Tinkerer": 	10,
		"Roadbarter": 	10,
		"Urbanite": 	12,
		"Stonemason": 	7,
		"Darkin":		5,
		"Crystal Cavern": 3,
		"Canyon Dweller":5,
		"Bank Templar":5,
		"Forgeclan": 5
		}

	chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]

	return f"{chosen_type} "

def Lizardfolks():
	Types = {
		"Swamp Crocfolk": 8,
		"Jungle Guanafolk": 7,
		"Desertic Horned": 5,
		"Dune Dino":4,
		"White Albino": 1,
		"Feathered Dinofolk":5,
		"Colored Chamalfolk":3,
		"Titan Rex": 3,
		"Tundra Saurius": 3,
		"Turtlefolk":6,
		"Frogfolk": 4,
		"Silurian": 	5,
		}

	chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]

	return f"{chosen_type} "

def Kobolds():

	Kobold = {
		"Kobold":  10,
		"Winged Kobold":  1,
		}

	# Pick one from each category
	chosen_type = random.choices(list(Kobold.keys()), weights=Kobold.values(), k=1)[0]
	chosen_color = random.choices(list(DragonColors.keys()), weights=DragonColors.values(), k=1)[0]

	return f"{chosen_color} {chosen_type}"

def Snakefolks():
	Types = {
		"Arboreasps": 4,        # In lush forests, possibly skilled in herbalism and natural resources.
		"Iciconda": 2,          # Powerful, adapted to cold climates, resilient against extreme cold.
		"Titanboa": 3,          # Native to island ecosystems, they have a build of extraordinary size.
		"Nightscale": 3,        # Adapted to night and subterranean life, blending in the dark.
		"Aspisian": 4,          # Traveling across terrains, known for adaptability and diverse cultural knowledge.
		"Gorgonian": 2,         # Descended from mythical Gorgons, characterized by strong presence and traits.
		"Hydrakin": 1,          # Rare, revered, connected to multi-headed serpent deities.
		"Mounty Python": 3,     # A jovial and humorous society, known for their wit and good-natured humor. They tend to kill parrots.
		"Coatlfolk": 5,         # Mythical resonance, possibly linked to spiritual practices.
		"Cobraclan": 6,         # Resilient in desert environments.
		"Vipertongue": 5,       # Known for their naturally venomous abilities.
		"Ophidian": 4,          # Adapted to jungle environments, skilled in stealth and survival.
		"Naga": 4,              # Respected for their swimming abilities and connection to aquatic environments.
		"Lamia": 4,				# Greek mythical snake-ladies with  taste for human flesh
		}

	chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]

	return f"{chosen_type} "

def Monster(Type):
	return Subrace(Type)

def Creature(Type):
	return Subrace(Type)

def Subrace(Type):
	type_function_map = {
		"Aberration": Aberrations,
		"Aven": Avens,
		"Beast": Beasts,
		"Beastfolk": Beastfolks,
		"Catfolk":  Catfolks,
		"Celestial": Celestials,
		"Construct": Constructs,
		"Dragon": Dragons,
		"Dwarf": Dwarfs,
		"Elemental": Elementals,
		"Elf": Elves,
		"Fey": Feys,
		"Fiend": Fiends,
		"Giant": Giants,
		"Goblin": Goblins,
		"Gnome": Gnomes,
		"Human": Humans,
		"Halfling": Halflings,
		"Kobold": Kobolds,
		"Lizardfolk":Lizardfolks,
		"Monstrosity": Monstrosities,
		"Orc": 	Orcs,
		"Ooze": Oozes,
		"Plant": Plants,
		"Snakefolk":Snakefolks,
		"Undead": Undeads
	}

	if Type in type_function_map:
		subrace = type_function_map[Type]()
	else:
		subrace = f"{Type} of an enigmatic lineage."

	return subrace
