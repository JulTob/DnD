import random

def Race():
    race_weights = {
        "Human": 26,
        "Aberration": 16,
        "Aven": 16,
        "Beast": 18,
        "Beastfolk": 17,
        "Celestial": 16,
        "Construct": 16,
        "Dragon": 17,
        "Dwarf": 20,
        "Elf": 20,
        "Elemental": 17,
        "Fey": 16,
        "Fiend": 16,
        "Giant": 16,
        "Gnome": 17,
        "Goblin": 20,
        "Halfling": 19,
        "Kobold": 20,
        "Lizardfolk": 16,
        "Monstrosity": 17,
        "Ooze": 16,
        "Orc": 21,
        "Plant": 17,
        "Snakefolk": 16,
        "Undead": 19,
        "": 0
    }
    
    return random.choices(list(race_weights.keys()), weights=race_weights.values(), k=1)[0]

def Aberrations():
    Names = {
        "Beholder": 8,          # Known for their paranoia and individualism.
        "Shapeshifters": 3,     # Unique appearance as Mimics and shapeshifters with horrible true forms.
        "Illithid": 9,          # A highly intelligent race known for their psionic powers.
        "Old One": 7,           # Ancient beings with vast knowledge and a desire to dominate other species. 
        "Mindlinker": 4,        # They are benevolent and seek knowledge.
        "Dominators": 5,        # Slave traders with a unique hierarchy.
        "Living Spell": 6,      # Former wizards transformed into monstrous forms.
        "Chaotic": 6,           # Representing pure chaos, they're unpredictable.
        "Star Titan": 5,        # Cosmic horror element.
        "Alien Spawn": 5,       # Cosmic horror element.
        "Parasyte": 4,          # Parasitic entities that can control other beings.
        "Destiny Devouers": 4,  # Time-traveling and body-swapping aliens.
        "Githyanki": 7,         # Raiders and conquerors.
        "Githzerai": 7,         # More enlightened.
        }

    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]



def Avens():
    Names = {
        "Birdfolk": 7,    # Generic birdfolk, versatile in nature.
        "Kenku": 9,       # Unique mimicry ability and urban setting.
        "Aarakocra": 8,   # High-flying and more spiritual.
        "Tengu": 6,       # Martial arts and folklore connections.
        "Raptoran": 5,    # Mountain dwellers with a unique flight lifecycle.
        "Owlin": 5,       # Owl-like Nocturnal and wise.
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Beasts():
    Names = {
        "Armored Bear": 8,          # From Philip Pullman's His Dark Materials series.
        "Monkey King": 9,
        "Guardian Kong": 7,
        "Giant Eagle": 8,           
        "Golden Lion": 7, 
        "White Tiguer": 6,
        "Vulture Spirit": 5,
        "Kitsune Fox": 10,
        "Deer Spirit": 6,           # Associated with gentleness and intuition in various cultures.
        "Giant Owl of Wisdom": 8,   # A universal symbol of knowledge.
        "Celestial Stag": 7,        # Stags are often seen as messengers or connected to the otherworld in various mythologies.
        "Fenrir Wolf": 7,
        "Forest-God Boar": 5,       # A guardian of the forests, revered for its bravery.
        "Cosmic Whale": 6, 
        "Kaiju Dinosaur": 6, 
        "Kerberus Dog": 7,
        "Sun Scarab": 9,
        "Moon Jackal": 6,
        "Spider Queen": 7,
        "World Serpent's Spawn": 7,
        "Elder Elephant": 8 ,
        "":1}
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Beastfolks():
    Names = {
        "Arachnidfolk": 6,     # Spiders are often associated with trickery and weaving fate.
        "Catfolk":15,
        "Centaur": 9,          # Classic mythological creature, representing the wild side of humanity.
        "Gnoll": 6,            # Often seen as savage and chaotic, inspired by hyenas.
        "Insectfolk": 5,       # Unique and diverse, representing both hive minds and individuality.
        "Jackalmen": 6,        # Often seen in Egyptian mythologies, associated with the afterlife.
        "Kitsune": 8,          # Japanese fox spirits, both mischievous and wise.
        "Lycan": 7,            # General term for were-creatures, known for their cursed transformations.
        "Leonid": 5,
        "Merfolk": 9,          # Classic creatures of the sea, representing both beauty and danger.
        "Minotaur": 8,         # The embodiment of the labyrinth's mystery and challenge.
        "Ratfolk": 7,          # Clever, opportunistic, and often seen in urban settings.
        "Scorpionfolk": 5,     # Dangerous and venomous, often used as guardians in myths.
        "Sharkfolk": 7,        # Predators of the sea, representing both fear and respect.
        "Skinwalker": 5,
        "Werebear": 6,         # A more noble version of lycanthropes, often associated with strength and protection.
        "Werewolf": 9,         # One of the most recognized lycanthropes, representing the untamed side of humanity.
        "Harpy": 7,          # Half-bird, half-woman, often seen as omens.
        "Satyr": 8,            # Revelers and musicians, representing the carefree side of nature.
        "": 0
        }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Celestials():
    Names = {
        "Angelic Bloodline": 17,  # Mortals with celestial ancentry 
        "Half-Angel": 12,         # Mortals with a celestial parent
        "Angel": 9,               # Classic representatives of good, messengers of deities.
        "Ascended": 8,            # Mortals who have risen to a divine or semi-divine status.
        "Couatl": 7,              # Feathered serpents, often seen as guardians or protectors.
        "Forgotten God": 6,       # Once powerful, now forgotten. Represents the ebb and flow of faith.
        "Lesser God": 8,          # Deities of minor aspects or domains.
        "Minor God": 8,           # Similar to Lesser God, deities with limited influence.
        "Pegasus": 7,             # The majestic winged horse, symbol of purity and grace.
        "Planetar": 9,            # High-ranking angels, often seen as warriors of good.
        "Seraph": 9,              # Burning ones, highest order of angels.
        "Throne": 8,              # Angels associated with celestial justice and maintaining the cosmic order.
        "Unicorn": 7,             # Pure and gentle creatures, often associated with forests and healing.
        "Celestial Serpent": 8,   # Dragons that reside in the heavens, symbols of power and majesty.
        "Valkyrie": 7,            # Choosers of the slain, guiding heroes to the afterlife.
        "Solar": 9,               # Extremely powerful celestial beings, champions of deities.
        "Ki-rin": 7,              # Eastern counterpart to unicorns, symbols of wisdom.
        "Deva": 8,                # Divine beings in Hindu mythology, often in conflict with Asuras.
        "Archon": 8,              # Beings of pure law and good, often in opposition to demons and devils.
        "Archangel": 5,
        "Avatar": 5,
        "": 1}

    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Constructs():
    Names = {
        "Animated Armor": 8,         # Empty suits of armor brought to life, often as guardians.
        "Drone": 7,                  # Modern or futuristic unmanned devices, often for reconnaissance.
        "Golem": 9,                  # Beings made from inanimate material, like clay or stone. Classic magic constructs.
        "Homunculus": 7,             # Full Metal Alchemist's style created humanoids.
        "Flying Sword": 7,           # Enchanted weapons that move on their own.
        "Living Furniture": 6,       # Animated carpets, wardroves, and anything at beast's castle, often serving as traps.
        "Scarecrow": 7,              # Animated scarecrows, often created to protect crops but can be sinister.
        "Clockwork Construct": 8,    # Intricate mechanical beings, often steampunk-inspired.
        "Warforged": 9,              # Sentient constructs made for war, often searching for purpose after conflict.
        "Modron": 8,                 # Geometrically inspired beings from a plane of utter order.
        "Shield Guardian": 8,        # Created to protect its creator, often bound by an amulet.
        "Tome Guardian": 7,          # Animated books or beings made of paper, protecting knowledge.
        "Effigy": 8                  # Ritualistic statues or figures, animated for various purposes.
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Dragons():
    DragonTypes = {
        "Dragonborn": 22,         # Dragon-like humanoids.
        "Wyrmling": 10,            # Baby dragons.
        "Young Dragon": 9,        # Adolescent dragons, coming into their power.
        "Dragon": 8,              # Fully grown, mature dragons.
        "Drake": 7,               
        "Draco": 6,               
        "Sky Serpent": 5,       
        "Half Dragon": 4,
        "Dragon Turtle": 4
    }

    DragonColors = {
        "Black": 8,               # Chromatic, acid breath.
        "Blue": 8,                # Chromatic, electric breath.
        "Green": 8,               # Chromatic, poison breath.
        "Red": 8,                 # Chromatic, fire breath.
        "White": 8,               # Chromatic, cold breath.
        "Bronze": 7,              # Metallic, good-aligned, lightning breath.
        "Silver": 7,              # Metallic, cold/paralyzing breath.
        "Gold": 7,                # Metallic, fire/weakening breath.
        "Brass": 7,               # Metallic, fire/sleep breath.
        "Copper": 7,              # Metallic, acid/slowing breath.
        "Shadow": 6,              # Tainted by Shadowfell, necrotic breath.
        "Gem": 6,                 # Rare, associated with gemstones and psionics.
        "Ethereal": 5,            # From the Ethereal Plane.
        "Planar": 5,              # Associated with specific planes.
        "Prismatic": 3            # Rare and extremely powerful, known for multi-colored, rainbow-like powers.
    }

    # Pick one from each category
    chosen_type = random.choices(list(DragonTypes.keys()), weights=DragonTypes.values(), k=1)[0]
    chosen_color = random.choices(list(DragonColors.keys()), weights=DragonColors.values(), k=1)[0]

    return f"{chosen_color} {chosen_type}"


def Elementals():
    Names = {
    "Atlantian": 9,      # Connection to water or ancient technology.
    "Cronusian": 5,      # Representing time and age.
    "Eosian": 8,         # Tied to the rising sun.
    "Genasi": 20,        # Representing air, earth, fire, and water.
    "Genie": 10,         # Powerful primordial entities.
    "Gaians": 9,         # Essence of the earth.
    "Hyperian": 7,       # Radiant, solar-powered.
    "Oceanians": 9,      # Depths, tides, storms.
    "Primordial": 7,     # Fundamental forces of reality.
    "Promethean": 8,     # Fire, electricity, and energy, with spirit of innovation.
    "Salamandrian": 10,  # Associated with fire.
    "Titan": 8,          # Raw elemental power.
    "Uranians": 8,       # Sky, stars, celestial magic.
    "Magmaforged": 9,    # Fusion of earth and fire.
    "Zephyrian": 9,      # Gentle airs.
    "Tartarian": 8,      # Dark ocean depths.
    "Etherian": 8,        # Ether and the heavenly shine.
    "Galaxian": 8,       # Elemental related to constellations and stars.
    "Chronian": 6,       # Time elementals
    "Tundran": 8         # Harsh icy landscapes.
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Fiends():
    Names = {
        "Tiefling": 22,
        "Devil": 12,
        "Demon": 12,
        "Imp": 10,
        "Cubus": 6,
        "Incubus": 6,
        "Succubus": 6,
        "Concubus": 3,
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
        "Rakshasa": 7,
        "Fallen Angel": 10,
        "Hellbound Hunter": 9,
        "Leviathan": 7,
        "Behemoth": 7,
        "Shinigami":6,
        "Hell's Rider": 10,
        "Soul Collector": 8,
        "Infernal Finder": 7,
        "Sin Investigator": 6,
        "Infernal Warlord": 7,
        "Infernal Justiciar": 8,
        "Vengeance Spirit": 7,
        "Retributioner": 7,
        "Pact Enforcer": 8,
        "Soulclaimer": 8,
        "Infernal Enforcer": 8
        }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Feys():
    Names = {
        "Hag": 8,       # Witches often associated with dark magic
        "Nymph": 9,     # Spirits of nature: water, forest, etc.
        "Pixie": 8,     # Tiny, mischievous spirits
        "Satyr": 9,     # Half-man, half-goat
        "Sprite": 7,    # Airy spirits similar to pixies but usually less mischievous
        "High Fae": 6,  # Powerful fey lords and ladies
        "Redcap": 5,    # Malicious goblin-like creatures
        "Banshee": 5,   # Spirits heralding death
        "Leprechaun": 7,  # Mischievous little fey associated with pots of gold
        "Changeling": 5,  # Fey child left in place of a stolen human child
        "Nexus Fey": 6,       # Fey connected to a connection point
        "Duende": 5,          # Fey of the arts, beauty, and nature. Tricksters.
        "Home Lares": 4,      # Guardians of homes and families
        "Fata": 5              # Fae that intervine in someone's fate
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Giants():
    Names = {
        "Cyclops": 8,                # Greek one-eyed giants
        "Ogre": 10,                  # Brutish man-eaters
        "Troll": 9,                  # Norse mountain dwellers
        "Jotunn (Frost Giant)": 7,   # Norse primal giants
        "Fire Giant": 7,             # Inhabitants of Muspelheim
        "Gigantes": 6,               # Giants from Greek mythology
        "Nephilim": 5,               # Biblical giants
        "Oni": 7,                    # Japanese ogre-like giants
        "Ettin (Two headed)": 6,     # English two-headed giants
        "Fomorians (Sea Giants)": 5, # Irish sea giants
        "Goliath": 5,                # Half Giants
        "Cloud Giant": 7,            # Noble sky dwellers
        "Stone Giant": 7,            # Earthy, rocky giants
        "Storm Giant": 6             # Majestic tempest giants
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Gnomes():
    Names = {
        "Mountain": 8,
        "Forest": 8,
        "Garden": 1,
        "Tinker": 4,
        "Crossroad": 3,
        "Trickster": 3,
        "Wandering": 3
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Goblins():
    Names = {
        "Goblin": 15,                       # Mischievous green-skinned creatures
        "Hobgoblin": 8,                     # Disciplined, militant goblinoids
        "Bugbear": 7,                       # Stealthy brutes of the goblinoid family
        "Gremlin (Tecnogoblin)": 6,         # Saboteurs of machinery
        "Redcap": 5,                        # Bloodthirsty goblin-like fey
        "Nyk (Watergoblin)": 6,             # Slavic water-dwelling goblins
        "Trow (Dark goblin)": 5,            # Orcadian mischief-makers
        "Knocker (Underdark goblin)": 6,    # Cornish mine-dwelling creatures
        "Domovoi (House Goblin)": 5         # Slavic house spirits
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Monstrosities():
    Names = {
        "Basilisk": 7,        
        "Chimera": 8,         
        "Displacer Beast": 9,
        "Doppelganger": 8,    
        "Gorgon": 7,          
        "Griffon": 9,         
        "Harpy": 8,           
        "Horror": 6,          
        "Kerberus": 8,        
        "Sphynx": 7,           
        "Manticore": 9,       
        "Yeti": 7,            
        "Worg": 8,
        "Wendigo": 3,
        "Kraken": 5,
        "Chupacabra":3,
        "Land Shark":3,
        "":1
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Oozes():
    Types = {
        "Blob": 8,      # Standard, amorphous entity.
        "Slime": 6,     # Slightly more fluidic, might move faster
        "Jelly": 7,     # More gelatinous and transparent
        "Pudding": 5,   # Thicker, more aggressive.
        "Goo": 4,       # Sticky and adhesive, might trap prey.
        "Mold": 3,      # Fungus-like, possibly releasing spores or gases.
        "Cube": 9       # Perfectly square, often large enough to engulf adventurers.
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
        "Toxic": 6
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
        "Willow Guardian": 7,
        "Treant": 9,
        "Awakened Tree": 9,
        "Forefather Oak": 7,
        "Myconid Sovereign": 8,
        "Ent": 9,
        "Treefolk": 7,
        "Floral Walkers": 7,
        "Living Totem": 7,
        "Walker Vine": 9,
        "Singing Lotus": 7,
        "Lichen Gravetaker": 7,
        "Cactoid Nomad": 6,
        "Vegetation Abomination":3,
        "Dryad":12,
        "Fungical Intellectual": 5
        
    }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]


def Undeads():
    Names = {
            "Death Knight": 8,           # Elite undead warriors, remnants of former knights or warlords.
            "Honor Phantom": 10,         # Ethereal spirits bound by duty or a promise made in life.
            "Regret Ghost": 11,          # Souls trapped due to unfinished business or profound regrets.
            "Lich": 7,                   # Undying mages who sought eternal life through dark rituals.
            "Pride Mummy": 9,            # Preserved dead, animated to guard ancient tombs and relics.
            "Mischief Poltergeist": 10,  # Playful spirits, causing disturbances to attract attention.
            "Vengeful Revenant": 8,      # Resurrected by sheer force of will to enact revenge.
            "Skeleton Protector": 12,    # Animated skeletal guardians, defending locations or treasures.
            "Thinker Skull": 10,         # Knowledgeable remnants, often used by dark mages for counsel.
            "Fear Shadow": 10,           # Undead born from intense fear, lurking in darkness.
            "Despair Specter": 11,       # Souls that suffered tremendous despair, wishing the same for the living.
            "Vampire": 18,               # Bloodsucking undead, intelligent and driven by hunger and desire.
            "Prideful Wight": 9,         # Powerful undead often found leading other lesser undead.
            "Cursed Eternal": 10,        # Mindless undead, driven by a hunger for the living.
            "Wraith": 9,                 # Souls consumed by anger, seeking to draw others into death.
            "Lone Lover": 9,             # Animated by profound love or loss, searching for their beloved.
            "Weeping Howler": 8,         # Spirits that mourn and wail, often announcing death.
            "Tomb's Hoarder": 8,         # Guardians of burial sites, obsessed with their treasures.
            "Penance Wraith": 8,         # Souls seeking atonement for sins committed in life.
            "Protector Spirit": 10       # Benevolent spirits still guarding a place, object, or person.
        }
    return random.choices(list(Names.keys()), weights=Names.values(), k=1)[0]

def Humans():
    Types = {
        "Local": 30,       
        "Foreigner": 20,
        "Highlander": 15,
        "Nomad": 15,
        "Islander": 12,
        "Forester": 11,
        "Plainsfolk": 10,
        "Humble":10,
        "Urbanite":9,
        "Exotic": 3,       
        "Wealthy":2,
        }
    
    chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]
    
    return f"{chosen_type} "


def Elves():
    Types = {
        "High": 16,       
        "Sylvan": 16,    
        "Wood": 16,    
        "Dark": 16,
        "Night": 9,
        "Feywild": 6,       
        "Shadow": 6,       
        "Sea": 11,       
        "Nomadic": 11,       
        "Snow":6,
        "Sun": 4,
        "Eclipse":2,
        "Moon": 4,
        "Wild": 4,
        "Urban": 11,
        "Sands": 8
        }
    
    chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]
    
    return f"{chosen_type} "

def Dwarfs():
    Types = {
        "Mountain": 20,
        "Conquistador": 10,        
        "Seawolf": 10,        
        "Tinkerer": 10,        
        "Roadbarter": 10,        
        "Urbanite": 12,        
        "Stonemason": 7,        
        "Dark":5,
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
        "Frogfolk": 4
        }
    
    chosen_type = random.choices(list(Types.keys()), weights=Types.values(), k=1)[0]
    
    return f"{chosen_type} "

def Kobolds():
    DragonColors = {
        "Black": 8,               # Chromatic, acid breath.
        "Blue": 8,                # Chromatic, electric breath.
        "Green": 8,               # Chromatic, poison breath.
        "Red": 8,                 # Chromatic, fire breath.
        "White": 8,               # Chromatic, cold breath.
        "Bronze": 7,              # Metallic, good-aligned, lightning breath.
        "Silver": 7,              # Metallic, cold/paralyzing breath.
        "Gold": 7,                # Metallic, fire/weakening breath.
        "Brass": 7,               # Metallic, fire/sleep breath.
        "Copper": 7,              # Metallic, acid/slowing breath.
        "Shadow": 6,              # Tainted by Shadowfell, necrotic breath.
        "Gem": 6,                 # Rare, associated with gemstones and psionics.
        "Prismatic": 3            # Rare and extremely powerful, known for multi-colored, rainbow-like powers.
        }
    
    Kobold = {
        "Kobold":  1         
        }

    # Pick one from each category
    chosen_type = random.choices(list(Kobold.keys()), weights=Kobold.values(), k=1)[0]
    chosen_color = random.choices(list(DragonColors.keys()), weights=DragonColors.values(), k=1)[0]

    return f"{chosen_color} {chosen_type}"

def Monster(Type):
    return Creature(Type)

def Creature(Type):
    type_function_map = {
        "Aberration": Aberrations,
        "Aven": Avens,
        "Beast": Beasts,
        "Beastfolk": Beastfolks,
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
        "Kobold": Kobolds,
        "Lizardfolk":Lizardfolks,
        "Monstrosity": Monstrosities,
        "Orc": Orcs,
        "Ooze": Oozes,
        "Plant": Plants,
        "Undead": Undeads
    }

    if Type in type_function_map:
        subrace = type_function_map[Type]()
    else:
        subrace = f"Is an unknown type of {Type}!"

    if Type == "Undead":
        Dead = Race()
        if Dead in type_function_map:
            subrace += f" - Undead {Dead}: {type_function_map[Dead]()}"

    return subrace
