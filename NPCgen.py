# NPC creator 
import random

def Title():
    descriptor = [
        "The Air",
        "The Alcoholic",
        "The Alpha", 
        "The Aberrant",
        "The Aprendice of",
        "The Archfey",
        "The Awakened",
        "The Autumn",
        "The Angry",
        "The Avatar",
        "The Arcane",
        "The Badger",
        "The Battle",
        "The Baron of",
        "The Bat"
        "The Bearded", 
        "The Beholder",
        "The Blending",
        "The Black",
        "The Blue",
        "The Blood",
        "The Bone",
        "The Bursting",
        "The Brass",
        "The Bronce",
        "The Brain",
        "The Butterfly",
        "The Cat",
        "The Camel",
        "The Climate",
        "The Chain",
        "The Champion",
        "The Chief",
        "The Chimera",
        "The Circus",
        "The Collector",
        "The Conjurer",
        "The Coral",
        "The Clokwork",
        "The Cursed",
        "The Crab",
        "The Deadly",
        "The Death",
        "The Dawning",
        "The Dark",
        "The Devourer of",
        "The Doctor", 
        "The Deep",
        "The Deer",
        "The Divine",
        "The Diviner",
        "The Dream",
        "The Eagle",
        "The Equinox",
        "The Equivalence",
        "The Emphasising",
        "The Emmerald", 
        "The Enchanted",
        "The Engine",
        "The Energy",
        "The Errant",
        "The Earth",
        "The Fleshwork",
        "The Fire",
        "The Fool",
        "The Forest",
        "The Fullmetal",
        "The Flying",
        "The Flame",
        "The Giant",
        "The Gas",
        "The Green",
        "The Golden",
        "The Great",
        "The Gladiator",
        "The Guard",
        "The Guardian",
        "The Hell",
        "The High",
        "The Hive",
        "The Hunter",
        "The Hungry",
        "The Hyena",
        "The Impulse",
        "The Inkwork",
        "The Iron",
        "The Ironbark",
        "The Ice",
        "The Icicle",
        "The Ink",
        "The Intellect",
        "The Illusionist",
        "The Jewelcraft",
        "The Jackal",
        "The Jewel",
        "The Kraken",
        "The Life",
        "The Lightning",
        "The Lizard",
        "The Lord Of the",
        "The Lord Of",
        "The Master",
        "The Mad",
        "The Mage",
        "The Mind",
        "The Mirror",
        "The Mist",
        "The Minotaur",
        "The Moon",
        "The Mutant",
        "The Mummy",
        "The Night",
        "The Nightmare",
        "The Necromancer",
        "The New",
        "The Noble",
        "The Ocean",
        "The Orange",
        "The Old",
        "The Owl",
        "The Pack",
        "The Pain",
        "The Paladin",
        "The Plague",
        "The Poisonous",
        "The Powder",
        "The Power",
        "The Purifying",
        "The Protector",
        "The Rat",
        "The Rainstorm",
        "The Red",
        "The River",
        "The Rogue",
        "The Ruby",
        "The Rune",
        "The Sad",
        "The Science",
        "The Shadow",
        "The Silver",
        "The Skelleton",
        "The Smiling",
        "The Spring",
        "The Storm",
        "The Stone",
        "The Starting",
        "The Stars",
        "The Strong",
        "The Spark",
        "The Spell",
        "The Speaker",
        "The Sphinx",
        "The Solar",
        "The Summer",
        "The Tender",
        "The Tiger",
        "The True",
        "The Troll",
        "The Undead",
        "The Unicorn",
        "The Vampiric",
        "The Veteran",
        "The Void",
        "The War",
        "The Warlord",
        "The Warping",
        "The Water",
        "The White",
        "The Wind" ,
        "The Winter",
        "The Wolf",
        "The Young",
        "The Zombie",
        "The",
        ""
        ]
    rank = [
        " Abomination",
        " Alchemist",
        "Aprentice",
        " Arrow",
        "Archer",
        "Archfey",
        "Archdruid",
        "Archmage",
        "Armour",
        "Ash",
        " Assassin",
        "Baboon",
        "Band",
        " Bard", 
        " Baron",
        "Basilisk",
        " Battle", 
        " Benefactor",
        " Berserker",
        "Bear",
        "Beholder",
        " Blade",
        "Bow",
        "Bringer",
        "Breeder",
        "Butterfly",
        "Beetle",
        "Cat",
        "Crab",
        " Chemist",
        "Champion",
        " Collector",
        "Collosus",
        "Commander",
        "Cultist",
        " Darkness",
        " Diamond",
        "Dino",
        "Deer",
        " Death",
        " Devil",
        " Doctor",
        " Doom",
        " Dragon",
        " Drake",
        " Druid",
        "Dream",
        "Devourer",
        "Eagle",
        " Eater",
        "Eclipse",
        "Enforcer",
        "Elite",
        "Elk",
        "Elemental",
        "Farmer",
        " Fire", 
        "Fury",
        " Flutist",
        "Flame",
        "Freedomfighter",
        "Gargoyle",
        " Genius",
        " Geneticist", 
        "Giant",
        " Grandmaster",
        "Ghost",
        "Golem",
        "Goat",
        "Guard",
        " Hand",
        "Hag",
        "Hawk",
        "Hive",
        " Horror",
        "Hound",
        " Hunter",
        "Hunger",
        "Hyena",
        "Hydra",
        " Inquisitor",
        "Incubus",
        "Intellect",
        "Jackal",
        " Knight",
        " Killer",
        " Knife",
        "King",
        "Kiss",
        " Leader",
        " Licht",
        "Lion",
        "Lizard",
        " Lotus",
        " Lord",
        " Machine",
        " Mage",
        " Master",
        "Mastermind",
        "Mastiff",
        " Martyr",
        " Mind",
        "Mist",
        " Monk",
        " Monster",
        " Moon",
        "Mule",
        "Necromancer",
        " Nightmare",
        " Nomad",
        " Of Justice",
        "Of The Abyss",
        "Of the Autumn",
        "Of The Crown"
        " Of The Desert",
        "Of The Dead",
        " Of The East",
        " Of The Forest",
        "Of The Fiends"
        " Of the Kingdom",
        " Of The Hills",
        "Of the Hells",
        " Of The North",
        " Of The Mountain",
        " Of the Old One",
        " Of The Plains",
        " Of the Pack",
        " Of The Sands",
        " Of The Sea",
        " Of The South",
        "Of The Summer",
        "Of The Spring",
        " Of The West",
        " Of The Winter",
        " Oni",
        "One",
        "Oracle",
        " Outlaw",
        "Owl",
        " Pathologist",
        " Paw",
        "Pirate",
        " Poet",
        "Priest",
        "Prince",
        "Princess",
        " Prophet",
        "Queen",
        "Ranger",
        "Rat",
        "Raven",
        "Revenant",
        " Reptile", 
        "Rider",
        " Ruby",
        " Rune",
        "Saurius",
        "Salamander",
        " Scientist",
        "Scarecrow",
        "Scorpion",
        " Shadow",
        "Shark",
        "Shaman",
        "Sorcerer",
        "Snake",
        "Skeleton",
        " Skull",
        " Surgeon",
        "Sucubus",
        " Spirit",
        "Spider",
        "Specter",
        "Swashbuckler",
        "Swarm",
        " Terror",
        "Trapper",
        "Trapecist",
        "Troll",
        "Thief",
        " Void",
        "Vampire",
        "Vulture",
        "Walker",
        " Warlock",
        "Werewolf",
        "Wolf",
        " Wizard",
        " Witch",
        " Witchhunter",
        " Writter" ,
        "Zombie",
        ""
        ] 
    
    title = random.choice(descriptor) + " " + random.choice(rank)
    return title
   
   
   
   
   
   
   
   
   
   
def Background():
    Backgrounds = [
        "Acolyte",
        "Alchemist",
        "Archmage",
        "Archaeologist",
        "Assassin",
        "Bandit",
        "Bard",
        "Berserker",
        "Charlatan",
        "Commoner",
        "Courtesan",
        "Cultist",
        "Criminal",
        "Druid",
        "Entertainer",
        "Expert",
        "Gladiator",
        "Guard",
        "Hero",
        "Hunter",
        "Knight", 
        "Mage",
        "Mercenary",
        "Noble", 
        "Outlander",
        "Priest",
        "Pirate",
        "Ranger",
        "Sage",
        "Scout",
        "Scholar",
        "Shaman",
        "Soldier",
        "Student",
        "Spy",
        "Spellcaster",
        "Thug", 
        "Traveler",
        "Tribal Warrior",
        "Veteran",
        "Warrior",
        "Warlock",
        "Witch",
        ""
        ]
    return random.choice(Backgrounds)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
def Race():
    Races = [
        "Human","Human","Human","Human","Human","Human","Human",
        "Aberration",
        "Aven(Birdfolk)",
        "Beast", "Beast",
        "Beastfolk",
        "Catfolk",
        "Celestial", 
        "Centaur",
        "Construct",
        "Demon",
        "Devil",
        "Dragon",
        "Dragonborn", "Dragonborn",
        "Dwarf","Dwarf","Dwarf",
        "Elf","Elf","Elf","Elf","Elf","Elf",
        "Elemental",
        "Fey", "Fey",
        "Fiend",
        "Giant",
        "Genasi",
        "Gnoll",
        "Gnome",
        "Goblin",
        "Hag",
        "Halfling",
        "Hobgoblin",
        "Kenku",
        "Kobold",
        "Lizardfolk",
        "Lycan",
        "Merfolk",
        "Minotaur",
        "Monstrosity",
        "Nymph",
        "Ogre",
        "Ooze",
        "Orc",
        "Plant",
        "Snakefolk",
        "Spirit",
        "Tiefling",
        "Undead",
        "Vampire",
        "Werewolf",
        ""
        ]
    return random.choice(Races)














def BeastName():
    Names = [
        "Baboon",
        "Badger",
        "Bat",
        "Blood Hawk",
        "Boar",
        "Cat",
        "Camel",
        "Dog",
        "Crab",
        "Deer", "Elk",
        "Eagle", "Hawk",
        "Frog",
        "Giant Insect", "Giant Beetle", "Giant Centipede",
        "Goat",
        "Horse", "Mule", "Pony",
        "Hyena",
        "Jackal",
        "Lizard",
        "Octopus",
        "Owl",
        "Piranna",
        "Rat",
        "Raven",
        "Sea Horse",
        "Shark", "Hunter Shark",
        "Spider",
        "Snake", "Flying Snake", "Boa", 
        "Vulture",
        "Wolf",
        ""]
    return random.choice(Names)

def MonstrosityName():
    Names = [
        "Griffon",
        ""]
    return random.choice(Names)

def AberrationName():
    Names = [
        "Intellect Devourer",
        ""]
    return random.choice(Names)

def PlantName():
    Names = [
        "Awakened Plant",
        "Myconid",
        ""]
    return random.choice(Names)
    
def UndeadName():
    Names = [
        "Crawling Limb",
        ""]
    return random.choice(Names)
    
def ConstructName():
    Names = [
        "Drone",
        "Homunculus",
        "Flying Sword",
        ""]
    return random.choice(Names)
    
def Name(Type):
    if Type == "Beast": return BeastName()
    if Type == "Monstrosity": return MonstrosityName()
    if Type == "Aberration": return AberrationName()
    if Type == "Plant": return PlantName()
    if Type == "Construct": return ConstructName()
    if Type == "Undead": return UndeadName()
    Names = [
        ""]
    return random.choice(Names)

   
   
   
def Dice(D=6):
    roll = random.randint(1,D)
    return roll
    
def AbilityScore():
    d1 = Dice()
    d2 = Dice() 
    d3 = Dice()
    d4 = Dice()
    return d1+d2+d3+d4 - min(d1,d2,d3,d4) + Dice(3)-1 +Dice()- Dice()
    
def Modifier(AS):
    return int((AS-10)/2)

def Proficiency(AS):
    return Dice(Modifier(AS)*2)

        


def Attack(Type):
    SimpleMeleeWeapons = [
        "Rock, 1d6 + %STR Bludgeoning, 25/50 thrown", 
        "Fists or Claws, 1d4 + %STR Bludgeoning",
        "Bite, 1d4 + %STR Piercing",
        "Club, 1d4 + %STR Bludgeoning",
        "Dagger, 1d4 + %STR Piercing, 20/60 thrown",
        "Dagger, 1d4 + %DEX Piercing, 20/60 thrown",
        "GreatClub, 1d8 + %STR Bludgeoning",
        "Handaxe, 1d6 + %STR Slashing, 20/60 thrown",
        "Javelin, 1d6 + %STR Piercing, 30/120 thrown",
        "Light Hammer, 1d4 + %STR Bludgeoning, 20/60 thrown",
        "Mace, 1d6 + %STR Bludgeoning",
        "Quarterstaff, 1d6 + %STR Bludgeoning",
        "Quarterstaff, 1d8 + %STR Bludgeoning",
        "Sickle, 1d4 + %STR Slashing",
        "Spear, 1d6 + %STR Piercing, 20/60 thrown",
        "Spear, 1d8 + %STR Piercing, 20/60 thrown",
        ""
        ]
    SimpleRangedWeapons = [
        "Rock, 1d6 + %STR Bludgeoning, 25/50 thrown", 
        "Light Crossbow, 1d8 + %DEX Piercing, 80/320 range",
        "Dart, 1d4 + %DEX Piercing, 20/60 range",
        "Dart, 1d4 + %STR Piercing, 20/60 range",
        "Shortbow, 1d6 + %DEX Piercing, 80/320 range",
        "Sling, 1d4 + %DEX Bludgeoning, 30/120 range",
        ""
        ]
    MartialMeleeWeapons = [
        "Battleaxe, 1d8 + %STR Slashing",
        "Battleaxe, 1d10 + %STR Slashing",
        "Flail, 1d8 + %STR Bludgeoning",
        "Glaive, 1d10 + %STR Bludgeoning, reach",
        "Greataxe, 1d12 + %STR Slashing, reach",
        "Greatsword, 2d6 + %STR Slashing",
        "Halberd, 1d10 + %STR Slashing, reach",
        "Lance, 1d12 + %STR Piercing, reach",
        "Longsword, 1d8 + %STR Slashing",
        "Longsword, 1d10 + %STR Slashing",
        "Maul, 2d6 + %STR Bludgeoning",
        "Morningstar, 1d8 + %STR Piercing",
        "Pike, 1d10 + %STR Piercing, reach",
        "Rapier, 1d8 + %STR Piercing, Finesse",
        "Rapier, 1d8 + %DEX Piercing, Finesse",
        "Scimitar, 1d6 + %STR Slashing, Finesse, light",
        "Scimitar, 1d6 + %DEX Slashing, Finesse, light",
        "Shortsword, 1d6 + %STR Slashing, Finesse, light",
        "Shortsword, 1d6 + %DEX Slashing, Finesse, light",
        "Trident, 1d6 + %STR Piercing, 20/60 thrown",
        "Trident, 1d8 + %STR Piercing, 20/60 thrown",
        "War pick, 1d8 + %STR Bludgeoning",
        "Warhammer, 1d8 + %STR Bludgeoning",
        "Warhammer, 1d10 + %STR Bludgeoning",
        "Whip, 1d4 + %STR Slashing, Finesse, reach",
        ""
        ]
    MartialRangedWeapons = [
        "Blowgun, 1 + %DEX piercing, 25/100 range",
        "Hand Crossbow, 1d6 + %DEX piercing, 30/120 range",
        "Heavy Crossbow, 1d10 + %DEX piercing, 100/400 range",
        "Longbow, 1d8 + %DEX piercing, 150/600 range",
        "Net, Special, 5/15 range",
        ""
        ]
    
    if Type == "Melee" or Type == 1:
        return random.choice(SimpleMeleeWeapons)
    elif Type == "Ranged" or Type == 2:
        return random.choice(SimpleRangedWeapons)
    elif Type == "Martial" or Type == "MartialMelee" or Type == 3:
        return random.choice(MartialMeleeWeapons)
    elif Type == "RangedMartial" or Type == 4:
        return random.choice(MartialRangedWeapons)
    else:
        return random.choice(SimpleMeleeWeapons)

def Damage():
    DamageTypes = [
        "Slashing",
        "Piercing",
        "Bludgeoning",
        "Poison",
        "Acid",
        "Fire",
        "Cold",
        "Radiant",
        "Necrotic",
        "Lightning",
        "Force",
        "Psychic",
        "Thunder",
        ""
        ]
    return random.choice(DamageTypes)







    

def Actions(Type=Dice(60)):
    r = ""
    if Type=="Healer" or Type ==1:
        r = r+ "\n Cantrips (at will): guidance, sacred flame \n    1st level (2 slots): cure wounds"
        
    elif Type == "Mage" or Type == 2:
        r = r+ "\n Cantrips (at will): firebolt, light \n    1st level (2 slots): Sleep"
        
    elif Type == "Acolyte" or Type == 3:
        r = r+ "\n Cantrips (at will): light, sacred flame, thaumaturgy \n    1st level (3 slots): bless, cure wounds, sanctuary"
        
    elif Type == "Celestial" or Type == 4:
        r = r+ "\n Cantrips (at will): light, sacred flame, thaumaturgy \n    1st level (3 slots): bless, cure wounds, sanctuary"
        
    elif Type == "Tribal Warrior" or Type == 5:
        r = r + "\n- Pack Tactics \n\t The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated."
        if Dice(2)==1:
            r= r + "\n- Wounded Fury"
        
    elif Type == "Plant" or Type == 6: 
        if Dice() == 1:
            r = r+ "\n- False Appereance: \n\t While the plant remains motionless, it is indistinguishable from a normal plant."
        if Dice() == 1:
            r = r+ "\n- Damage Vulnerabilities fire"
        if Dice() == 1:
            r = r+ "\n- Entangling Plants"
        if Dice() == 1:
            r = r+ "\n Damage Immunities: poison"
        if Dice() == 1:
            r = r+ "\n Condition Immunities:  blinded"
        if Dice() == 1:
            r = r+ "\n Condition Immunities:  charmed"
        if Dice() == 1:
            r = r+ "\n Condition Immunities:   poisoned"
        if Dice() == 1:
            r = r+ "\n Condition Immunities:  frightened"
        if Dice() == 1:
            r = r + "\n-Distress Spores. \n\t When the plant takes damage, all other plants within 240 feet of it can sense its pain."  
        if Dice() == 1:
            r = r + "\n-Sun Sickness. \n\t While in sunlight, the plant has disadvantage on ability checks, attack rolls, and saving throws. The plant dies if it spends more than 1 hour in direct sunlight."
        if Dice() == 1:
            r = r + "\n-Animating Spores"  
        if Dice() == 1:
            r = r + "\n-Hallucination Spores"  
        if Dice() == 1:
            r = r + "\n-Pacifying Spores"   
        if Dice() == 1:
            r = r + "\n-Rapport Spores (3/Day).\n\t A 10-foot radius of spores extends from the plant. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour."   
        if Dice() == 1:
            r = r + "\n-Caustic Spores"   
        if Dice() == 1:
            r = r + "\n-Infestation Spores"   
        if Dice() == 1:
            r = r + "\n-Euphoria Spores"   
        if Dice() == 1:
            r = r + "\n Condition Immunities\n\t blinded, deafened, frightened"
        if Dice() == 1:
            r = r + "\n Blindsight\n\t 30 ft"        
        
    elif Type == "Nymph" or Type == 7: 
        r = r+ "\n- Teleport"
        r = r+ "\n- Magic Resistance"
        r = r+ "\n- Speak with Beasts and Plants"
        r = r+ "\n- At will: druidcraft\n 3/day each: entangle, goodberry \n 1/day each: barkskin, pass without trace, shillelagh"
        r = r+ "\n- Fey Charm"
        
        
    elif Type == "Beast" or Type == "Beastfolk" or Type == 8: 
        if Dice() == 1:
            r = r+ "\n- Speed. \n\t 50 ft."
        if Dice() == 1:
            r = r+ "\n- Climb. \n\t 30 ft."
        if Dice() == 1:
            r = r+ "\n- Burrow. \n\t 10 ft."  
        if Dice() == 1:
            r = r+ "\n- Fly. \n\t 60 ft."  
            if Dice(2)==1:
                r = r+ "\n Flyby. \n\t The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach."
        if Dice(4) == 1:
            r = r+ "\n- Darkvision." 
            if Dice()==1:
                r = r+ "\n\t 60 ft."
            else:
                r = r+ "\n\t 30 ft."
        if Dice() == 1:
            r = r+ "\n- Blindsight." 
            if Dice()==1:
                r = r+ "\n\t 60 ft."
            else:
                r = r+ "\n\t 30 ft."
            if Dice()==1:
                r = r+ "\nEcholocation. \n\t The Beast can't use its blindsight while deafened."
                r = r+ "\nKeen Hearing. \n\t The beast has advantage on Wisdom (Perception) checks that rely on hearing."
        if Dice() == 1:
            r = r+ "\n- Keen Smell. \n\t The Beast has advantage on Wisdom (Perception) checks that rely on smell."    
        if Dice() == 1:
            r = r+ "\n- Keen Senses\n\t The beast has advantage on Wisdom (Perception) checks that rely on senses."
        if Dice() == 1:
            r = r+ "\n- Keen Sight. \n\tThe beast has advantage on Wisdom (Perception) checks that rely on sight."
        if Dice() == 1:
            r = r+ "\n- Keen Hearing. \n\tThe beast has advantage on Wisdom (Perception) checks that rely on hearing."
        if Dice(2) == 1:
            r = r+ "\n-  Pack Tactics. \n\t The Beast has advantage on an attack roll against a creature if at least one of the beast's allies is within 5 feet of the creature and the ally isn't incapacitated."
        if Dice(2) == 1:
            r = r+ "\n-  Multiattack. \n\t The Beast makes two attacks."

        if Dice() == 1:
            r = r+ "\n - Grappler. \n\t On an attack, the target is grappled,  [DC 10+%STR]"
            if Dice(2) == 1:
                r = r+ "\n - Constrict. \n\t Until the grapple ends, the creature is restrained. The creature can't constrict another creature."
        if Dice() == 1:
            r = r+ "\n - Charge \n\t If the Beast moves at least 20 feet straight toward a target and then hits it with an attack on the same turn, the target takes an extra [2d6+%STR] bludgeoning damage. If the target is a creature, it must succeed on a DC=[10+%STR] Strength saving throw or be knocked prone."
        if Dice() == 1:
            r = r+ "\n - Relentless \n\t Recharges after a Short or Long Rest). \n\t If the boar takes 7 damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."
        if Dice() == 1:
            r = r+ "\n- Water Breathing. The beast can breathe underwater"
            r = r+ "\n- Swim. \n\t 60 ft."  
            if Dice(2) == 1:
                r = r + "\n- Underwater Camouflage. \n\t The beast has advantage on Dexterity (Stealth) checks made while underwater."
        if Dice() == 1:
            r = r+ "\n- Blood Frenzy \n\t The beast has advantage on melee attack rolls against any creature that doesn't have all its hit points."
        if Dice() == 1:
            r = r+ "\n- Amphibious"
            r = r+ "\n- Swim. \n\t 30 ft."  
            if Dice(2) == 1:
                r = r+ "\n- Standing Leap. \n\t The Beast's long jump is up to half his speed in feet and its high jump is up to quarter his speed, with or without a running start."  
        if Dice() == 1:
            r = r+ "\n- Standing Leap. \n\t The Beast's long jump is up to 10 feet and its high jump is up to 5 feet, with or without a running start." 
        if Dice() == 1:
            r = r + "\n- SpiderClimb \n\t The beast can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."  
            if Dice(2) == 1:
                r = r + "\n- Web Sense \n\t While in contact with a web, the spider knows the exact location of any other creature in contact with the same web."
                r = r + "\n- Web Walker \n\t The spider ignores movement restrictions caused by webbing."
        if Dice() == 1:
            r = r+ "\n - Running Leap"
        if Dice() == 1:
            r = r+ "\n - Pounce"
        if Dice() == 1:
            r = r+ "\n - Constrict (restrained, 2d8 + %STR, escape DC 10+%STR)"
        if Dice() == 1:
            r = r+ "\n Blinsight \n\t 60 ft"
            r = r+ "\n Echolocation \n\t The Beast can't use its blindsight while deafened."
            r = r+ "\n Keen Hearing. \n\t The bat has advantage on Wisdom (Perception) checks that rely on hearing."
        if Dice() == 1:
            r = r+ "\nIllumination.\n\tThe beetle sheds bright light in a 10-foot radius and dim light for an additional 10 ft."
        if Dice() == 1:
            r = r+ "\n-Sure-Footed \n\t The beast has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
        if Dice() == 1:
            r = r + "\n- Hold Breath. \n\t The beast can hold its breath for 30 minutes."
        if Dice() == 1:
            r = r+ "\n- Mimicry \n\t The Raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."
        if Dice() == 1:
            r = r+ "\n- Beast of Burden \n\t The mule is considered to be a Large animal for the purpose of determining its carrying capacity."
        if Dice() == 1:
            r = r+ "\n- Swamp Camouflage \n\t The Beast has advantage on Dexterity (Stealth) checks made to hide in swampy terrain."
            
    elif Type == "Elf" or Type == 9:
        r = r+ "\nFey Ancestry.\n\t The Elf has advantage on saving throws against being charmed, and magic can't put the Elf to sleep."
        
        if Dice(4) <= 3:
            r = r+ "\n Darkvision \n\t 60ft"
        else:
            r = r+ "\n Darkvision \n\t 120ft"
            r = r+ "\nSunlight Sensitivity. \n\t While in sunlight, the Elf has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
        if Dice() == 1:
            r = r+ "\n At will: dancing lights\n    1/day each: darkness, faerie fire"

    elif Type == "Aven(Birdfolk)" or Type == 10:
        r = r+ "\n- Fly \n\t 50ft"
        
    elif Type == "Construct" or Type == 11:
        r = r+ "\n- Damage Immunities: Poison"
        r = r+ "\n- Condition Immunities: Poisoned, Charmed"
        if Dice(2)==1:
            r = r+ "\n- Damage Immunities: psychic"
        if Dice()==1:
            r = r+ "\n Condition Immunities: blinded \n"
        if Dice()==1:
            r = r+ "\n Condition Immunities: deafened \n"
        if Dice()==1:
            r = r+ "\n Condition Immunities: exhaustion \n"
        if Dice()==1:
            r = r+ "\n Condition Immunities: frightened \n"
        if Dice()==1:
            r = r+ "\n Condition Immunities:  petrified \n"
        if Dice()==1:
            r = r+ "\n Condition Immunities: , paralyzed \n"
        if Dice()==1:
            r = r+ "\n- Axiomatic Mind. \n\t The Construct can't be compelled to act in a manner contrary to its nature or its instructions."
        if Dice() == 1:
            r = r+"\n- Disintegration. \n\t If the duodrone dies, its body disintegrates into dust, leaving behind its weapons and anything else it was carrying."
        if Dice()==1:
            r = r+ "\n- False Apperance \n\t While the Construct remains motionless in rest, it is indistinguishable from a normal object"
        if Dice()==1:
            r = r+ "\n- Dark Vision:\n\t 60 ft"
        elif Dice()==1:
            r = r+ "\n- Truesight:\n\t 60 ft"
        elif Dice()==1:
            r = r+ "\n- Truesight:\n\t 120 ft"
        if Dice()==1:
            r = r+ "\n- Telepathic Bond:\n\t While the Construct is on the same plane of existence as its master, it can magically convey what it senses to its master, and the two can communicate telepathically."
        if Dice()==1:
            r = r+ "\n- Antimagic Susceptibility:\n\t The Construct is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the Construct must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute."

    elif Type == "Goblin" or Type == 12:
        r = r+ "\n- Nimble Scape"
        
    elif Type == "Aberration" or Type == 13:
        if Dice()==1: 
            r = r+"\nDamage Resistances:  \n\t bludgeoning, piercing, and slashing from nonmagical attacks"
        if Dice()==1: 
            r = r+"\nDamage Resistances:  \n\t acid"
        if Dice()==1: 
            r = r+"\nDamage Resistances:  \n\t cold"
        if Dice()==1: 
            r = r+"\nDamage Resistances:  \n\t lightning"
        if Dice(2)==1: 
            r = r+"\nDamage Resistances:  \n\t thunder"
        if Dice(2)==1: 
            r = r+ "\n- Blindsight: \n\t 60ft"
        else: 
            r = r+ "\n- Darkvision: \n\t 60ft"
        if Dice(2)==1: 
            r = r+ "\n- Telepathy: \n\t 60ft"
            if Dice(2)==1:
                r = r+ "\n-Advanced Telepathy: \n\t The Aberration can perceive the content of any telepathic communication used within 60 feet of it, and it can't be surprised by creatures with any form of telepathy."
            if Dice(2)==1:
                r = r+ "\n-Telepathic Shroud. \n\t The flumph is immune to any effect that would sense its emotions or read its thoughts, as well as all divination spells."
        if Dice(2)==1: 
            r = r+ "\n- Detect Sentience: \n\t It can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by a mind blank spell."
        if Dice(2)==1: 
            r = r+ "\n- Detect Sentience: \n\t It can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by a mind blank spell."
        if Dice(2)==1: 
            r = r+ "\n- Devour Intellect: \n\t It targets one creature it can see within 10 feet of it that has a brain. The target must succeed on a DC [10+%DEX] Intelligence saving throw against this magic or take 11 (2d10) psychic damage. Also on a failure, roll 3d6: If the total equals or exceeds the target's Intelligence score, that score is reduced to 0. The target is stunned until it regains at least one point of Intelligence."
        if Dice(2)==1: 
            r = r+ "\n- Body Thief. \n\t The intellect devourer initiates an Intelligence contest with an incapacitated humanoid within 5 feet of it that isn't protected by protection from evil and good. If it wins the contest, the intellect devourer magically consumes the target's brain, teleports into the target's skull, and takes control of the target's body. While inside a creature, the intellect devourer has total cover against attacks and other effects originating outside its host. The intellect devourer retains its Intelligence, Wisdom, and Charisma scores, as well as its understanding of Deep Speech, its telepathy, and its traits. It otherwise adopts the target's statistics. It knows everything the creature knew, including spells and languages. \n\t If the host body dies, the intellect devourer must leave it. A protection from evil and good spell cast on the body drives the intellect devourer out. The intellect devourer is also forced out if the target regains its devoured brain by means of a wish. By spending 5 feet of its movement, the intellect devourer can voluntarily leave the body, teleporting to the nearest unoccupied space within 5 feet of it. The body then dies, unless its brain is restored within 1 round."
        if Dice() == 1:
            r = r+ "\n- Damage Vulnerabilities: \n\t psychic"
        if Dice() == 1:
            r = r+ "\n- Stench Spray (1/Day). \n\t Each creature in a 15-foot cone originating from the flumph must succeed on a DC 10 Dexterity saving throw or be coated in a foul-smelling liquid. A coated creature exudes a horrible stench for 1d4 hours. The coated creature is poisoned as long as the stench lasts, and other creatures are poisoned while with in 5 feet of the coated creature. A creature can remove the stench on itself by using a short rest to bathe in water, alcohol, or vinegar."
        if Dice() == 1:
            r = r+ "\n- Magic Resistance: \n\t The Aberration has advantage on saving throws against spells and other magical effects."
        
    elif Type == "Kenku"  or Type == 14:
        r = r+ "\n- Ambusher"
        r = r+ "\n- Mimicry \n\t The Raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."
        
        
    elif Type == "Elemental" or Type == 15:
        r = "\n- False Appereance \n- Death Burst \n- Damage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks"
        rdm = Dice(4)
        if rdm == 1:
            r = "\n- Heated Body \n- Damage Immunities: fire  \n- Damage Vulnerabilities: cold"
        
    elif Type == "Fey" or Type == 16:
        if Dice() == 1:
            r = "\n At will: druidcraft \n    1/day each: confusion, dancing lights, detect evil and good, detect thoughts, dispel magic, entangle, fly, phantasmal force, polymorph, sleep"
        if Dice() == 1:
            r = r + "\n - Invisibility"
        if Dice() == 1:
            r = r + "\n - Heart Sight"
        if Dice() == 1:
            r = r + "\n -  Teleport (Recharge 4–6). \n\t The Fey magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the Fey can make one attack."
        return r
        
    elif Type == "Assassin" or Type == 17:
        return "\n- Superior Invisibility"
        
    elif Type == "Undead" or Type == 18:
        r = r + "\nDamage Immunities: poison"+"\n Condition Immunities: exhaustion, poisoned, charmed"
        if Dice(2) == 1:
            r = r + "\n - Undead Fortitude"
        if Dice(2) == 1:
            r = r + "\n -Stench"
        if Dice(2) == 1:
            r = r + "\n -Turn Defiance"
        if Dice() == 1:
            r = r + "\n - Turn Immunity \n\t The Undead is immune to effects that turn undead."


    elif Type == "Lizardfolk" or Type == 19:
        r = r+"\n\n- Hold Breath"
        rdm = Dice(2)
        if rdm == 1:
            r = r + "\n - Chameleon Skin\n"
        return r
        
    elif Type == "Vampire" or Type == 20:
        r = r + "\n - Sunlight Sensitivity"
        return r
        
    elif Type == "Gnome" or Type == 22:
        r = r + "\n - Gnome Cunning"
        r = r + "\n\n At will: nondetection (self only) \n   1/day each: blindness/deafness, blur, disguise self"
            
    elif Type == "Ooze" or Type == 23:
        if Dice() == 1:
            r = r+ "\n- Amorphous"
        if Dice() == 1:
            r = r+ "\n- Corrode Material"
            if Dice() == 1:
                r = r+ "\n\t Wood"
            if Dice() == 1:
                r = r+ "\n\t Metal"
            if Dice() == 1:
                r = r+ "\n\t Meat & Leather"
            if Dice() == 1:
                r = r+ "\n\t "


        if Dice() == 1:
            r = r+ "\n- False Appearance"
        if Dice() == 1:
            r = r+ "\n- Engulf"
        if Dice() == 1:
            r = r+ "\n- Gelatinous Cube"
        if Dice() == 1:
            r = r+ "\n- Transparent"
        if Dice() == 1:
            r = r+ "\n- Spider Climb"
        if Dice() == 1:
            r = r+ "\n- Split(Yellow): Lightning or Slashing"
        return r
        
    elif Type == "Hobgoblin" or Type == 24:
        r = r+"\n- Martial Advantage"
        
    elif Type == "Lycan" or Type ==25:
        r = r+ "\n- Shapechanger"
        r = r+"\n-Pack Tactics"
        
    elif Type == "Orc" or Type == 25:
        r = r+ "\n- Aggressive"
        
    elif Type == 26:
        r = r + "\n- Blood Frenzy"
    
    elif Type == "Scout" or Type == 27:
        r = r+ "\n- Keen Senses\n\t The beast has advantage on Wisdom (Perception) checks that rely on senses."   
        
        
    elif Type == "Spirit" or Type == 28:
        if Dice(2) == 1:
            r = r+"\n- Damage Resistances: acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks"
        if Dice(2) == 1:
            r = r+"\n- Damage Immunities: necrotic, poison "
        if Dice(2) == 1:
            r = r+"\n- Condition Immunities: charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious"
        rdm = Dice(2)
        if rdm == 1:
            r = r+"\n- Amorphous"
            r = r+"\n- Shadow Stealth"
            r = r+"\n- Sunlight Weakness"
        elif rdm == 2:
            r = r + "\n- Incorporeal Movement"
            r = r + "\n- Sunlight Sensitivity"
            r = r + "\n- Life Drain"
        if Dice(2) == 1:
            r = r + "\n- Invisibility"
        if Dice(2) == 1:
            r = r + "\n- Telekinetic Thrust"

    elif Type == "Thug" or Type == 29:
        r = r+ "\n- Pack Tactics"
        
    elif Type == "Dragon" or Type == 30:
        r = r+ "\n- Flight"
        r = r+ "\n- Breath Weapons"
        rdm = Dice(10)
        if rdm == 1:
            r = r + "\n - Fire Breath"
        elif rdm == 2:
            r = r + "\n - Sleep Breath"
        elif rdm == 3:
            r = r + "\n - Acid Breath"
        elif rdm == 4:
            r = r + "\n - Slowing Breath"
        elif rdm == 5:
            r = r + "\n - Euphoria Breath"
        elif rdm == 6:
            r = r + "\n - Repulsion Breath"
        elif rdm == 7:
            r = r + "\n - Poison Breath"
        if Dice(2) == 1:
            r = r + "\n - Amphibious"


    elif Type == "Dwarf" or Type == 31:
        r = r + "\n- Resilience"
        if Dice(2) == 1:
            r = r + "\n- Sunlight Sensitivity"
        if Dice(2) == 1:
            r = r + "\n- Enlarge"
        if Dice(2) == 1:
            r = r + "\n- Invisibility"
            
    elif Type == 32:
        r = r+ "\n- Luring Song"
    
    elif Type == "Cultist" or Type == 33:
        r = r+ "\n- Cantrips (at will): light, sacred flame, thaumaturgy \n 1st level (4 slots): command, inflict wounds, shield of faith. \n 2nd level (3 slots): hold person, spiritual weapon"
        if Dice(2)==1:
            r = r+ "\n Dark Devotion.\n\t The cultist has advantage on saving throws against being charmed or frightened."
        
        
    elif Type == "Fiend" or Type == 34:
        if Dice()==1:
            r = r + "\nDamage Resistances cold"
        if Dice()==1:
            r = r + "\nDamage Resistances: fire"
        if Dice()==1:
            r = r + "\nDamage Resistances: lightning"
        if Dice()==1:
            r = r + "\nDamage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks" 
        if Dice()==1:
            r = r + "\nDamage Immunities: poison"
        if Dice()==1:
            r = r + "\nDamage Immunities: fire"
        if Dice()==1:
            r = r + "\nCondition Immunities: charmed"
        if Dice()==1:
            r = r + "\nCondition Immunities: frightened"
        if Dice()==1:
            r = r + "\nCondition Immunities: poisoned"
        if Dice(2)==1:
            r = r + "\n Darkvision \n\t 60 ft."
        else: 
            if Dice(2)==1:
                r = r + "\n Darkvision \n\t 120 ft."
        if Dice(2)==1:
            r = r + "\n Devil's Sight. \n\t Magical darkness doesn't impede the lemure's darkvision."
        if Dice()==1:
            r = r +"\nMagic Resistance"
        if Dice(2) == 1:
            r = r + "\n- Shapechanger"
        if Dice(2) == 1:
            r = r + "\n- Scare (1/Day)."
        if Dice(2) == 1:
            r = r + "\n- Invisibility."
        if Dice()==1:
            r = r + "\n Hellish Rejuvenation. \n\t A Fiend that dies in the Nine Hells comes back to life with all its hit points in", Dice(10), "days unless it is killed by a good-aligned creature with a bless spell cast on that creature or its remains are sprinkled with holy water."
            
    elif Type== "Demon" or Type == 35:
        r = r + "\n Language. \n\t Abyssal"
        if Dice()==1:
            r = r + "\n Damage Resistances. \n\t cold"
        if Dice()==1:
            r = r + "\n Damage Resistances. \n\t fire"
        if Dice()==1:
            r = r + "\n Damage Resistances. \n\t lightning"
        if Dice()==1:
            r = r + "\n Damage Immunities. \n\t poison"
        if Dice()==1:
            r = r + "\n Darkvision. \n\t cold"
        if Dice()==1:
            r = r + "\n Telepathy. \n\t 60 ft. Only in Abyssal."
        if Dice()==1:
            r = r + "\nFetid Cloud (1/Day).\n\t A 10-foot radius of disgusting sulfuric gas extends out from the Demon. The gas spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a strong wind disperses it. Any creature that starts its turn in that area must succeed on a DC 11 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target can take either an action or a bonus action on its turn, not both, and can't take reactions."



   
    elif Type == "Spy" or Type == 36:
        r = r + "\n- Skills: Deception +5, Insight +4, Investigation +5, Perception +6, Persuasion +5, Sleight of Hand +4, Stealth +4"
        r = r + "\n- Cunning Action \n- Sneak Attack (1/Turn)."
        
    elif Type == "Berserker" or Type == 35:
        r = r + "\n- Multiattack"
        r = r + "\n- Reckless"
        
    elif Type == 36:
        r = r+"\n    At will: animal friendship (snakes) \n 3/day each: poison spray, suggestion"

    elif Type == "Centaur" or Type == 37:
        r = r + "\nSkills Athletics +6, Perception +3, Survival +3\n- Charge\n- Multiattack"
        
    elif Type == 38:
        r = r+ "\n    Cantrips (at will): sacred flame, thaumaturgy \n 1st level (3 slots): bane, shield of faith"
        
    elif Type == "Druid" or Type == 39:
        r = r + "\n- Cantrips (at will): druidcraft, produce flame, shillelagh \n 1st level (4 slots): entangle, longstrider, speak with animals, thunderwave \n2nd level (3 slots): animal messenger, barkskin\n"
        
    elif Type == 40:
        r = r + "\n-At will: mage hand (the hand is invisible) \n 3/day each: feather fall, jump, see invisibility, shield"

    elif Type == "Monstrosity" or Type == 41:
        r = r + "\n-Shapechanger"   
        if Dice(2) == 1:
            r = r + "\n-False Appearance"  
        if Dice(2) == 1:
            r = r + "\n-Stone Camouflage.\n\t The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.\n"  
        if Dice(2) == 1:
            r = r + "\n- Keen Sight.\n\t The griffon has advantage on Wisdom (Perception) checks that rely on sight.\n"  
        if Dice(2) == 1:
            r = r + "\n- Flight.\n\t 60 ft.\n"  


    elif Type == "Giant" or Type == 42:
        r = r + "\n-STR +" + str(Dice(12))  

    elif Type == 43:
        r = r + "\n-Cantrips (at will): guidance, resistance, thaumaturgy\n 1st level (4 slots): bless, command\n 2nd level (2 slots): augury, spiritual weapon (spear) "

    elif Type == "Priest" or Type == 45:
        r = r + "\nDivine Eminence"
        r = r + "\nCantrips (at will): light, sacred flame, thaumaturgy\n 1st level (4 slots): cure wounds, guiding bolt, sanctuary \n 2nd level (3 slots): lesser restoration, spiritual weapon \n 3rd level (2 slots): dispel magic, spirit guardians"
        
    elif Type == "Gnoll" or Type == 46:
        r = r + "\n Rampage.\n\t When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."
 
    elif Type == "Shaman" or Type == 47:
        r = r + "\n Cantrips (at will): druidcraft, produce flame, thorn whip \n\t 1st level (4 slots): entangle, fog cloud \n\t 2nd level (3 slots): heat metal, spike growth \n\t 3rd level (2 slots): conjure animals, plant growth"
        if Dice(2)==1:
            r = r + "\n Change Shape: \n\t The Shaman magically polymorphs into a Beast, remaining in that form for up to 1 hour. It can revert to its true form as a bonus action. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
            
    elif Type == "Ranger" or Type == 48:
        r = r + Attack(4)
        r = "\n Multiattack."
        
    elif Type == "Bandit" or Type == 49:
        r = r + "\n- Parry \n\t The Bandit adds 2 to its AC against one melee attack that would hit it. To do so, the bandit must see the attacker and be wielding a melee weapon."
        
    elif Type =="Guard" or Type == 50:
        r = r + "\n- Parry \n\t The Guard adds 2 to its AC against one melee attack that would hit it. To do so, the Guard must see the attacker and be wielding a melee weapon."
        
    elif Type == "Kobold" or Type == 51:    
        r = r + "\n- Darkvision \n\t 60ft."
        r = r + "\n- Pack Tactics \n\t The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated."
        r = r + "\n- Sunlight Sensitivity \n\t While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
    
    elif Type == "Noble" or Type == 52:
        r = r + "\n- Parry \n\t The noble adds 2 to its AC against one melee attack that would hit it. To do so, the noble must see the attacker and be wielding a melee weapon."
    
    elif Type == "Beastfolk" or Type == 8:
        r = r + "\n- Speak with Animal \n\t The Beastfolk can communicate simple concepts to his affinity animal when it speaks in Beast language."
    else :
        r = r + "Multiattack"
    return r
    




def Legendary(Type=Dice(10)):
    r = ""
    if Type == "Human" or Type == 1:
        r = r+ "\n- Attack"
    else:
        r = r+ "\n- Attack"
        r = r+ "\n- Move: \n\t The creature moves half its speed."
    return r
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def NPC():
    """NPC creator"""
    STR = AbilityScore()
    DEX = AbilityScore()
    CON = AbilityScore()
    INT = AbilityScore()
    WIS = AbilityScore()
    CHA = AbilityScore()
    
    bg = Background()
    
    Lvl = Dice(20)+Dice(20)
    rc = Race()
    
    
    print(Title())
    print(bg)
    print(rc)
    print(Name(rc))
    print("\n")

    print("Lvl:", Lvl, "   HP:", Lvl*(Dice(12) + Dice(2)*Modifier(CON)))
    print("AC:", 10 + Modifier(DEX) + Modifier(Dice(Lvl+10)))
    print("\n\t"," STR:", STR,"\t", Modifier(STR),"\n\t",
        "DEX:", DEX," \t", Modifier(DEX),"\n\t"
        "CON:", CON," \t",  Modifier(CON),"\n\t"
        "INT:", INT," \t",  Modifier(INT),"\n\t"
        "WIS:", WIS," \t", Modifier(WIS),"\n\t"
        "CHA:", CHA," \t",  Modifier(CHA),"\n\t")
 
    print("Saving Throws:")
    if Dice(3) == 1: print("Str:+",Modifier(STR), end=" ")
    if Dice(3) == 1: print("Dex:+",Modifier(DEX), end=" ")
    if Dice(3) == 1: print("Con:+",Modifier(CON), end=" ")
    if Dice(3) == 1: print("Int:+",Modifier(INT), end=" ")
    if Dice(3) == 1: print("Wis:+",Modifier(WIS), end=" ")
    if Dice(3) == 1: print("Cha:+",Modifier(CHA), end=" ")
    print("\n")
   
    print("Skills:")
    if Dice(6) <= Modifier(STR): print("Athletics:+",Proficiency(STR), end=" ")
    if Dice(6) <= Modifier(DEX): print("Acrobatics:+",Proficiency(DEX), end=" ")
    if Dice(6) <= Modifier(DEX): print("Sleight of Hand:+",Proficiency(DEX), end=" ")
    if Dice(6) <= Modifier(DEX): print("Stealth:+",Proficiency(DEX), end=" ")
    if Dice(6) <= Modifier(INT): print("Arcana:+",Proficiency(INT), end=" ")
    if Dice(6) <= Modifier(INT): print("History:+",Proficiency(INT), end=" ")
    if Dice(6) <= Modifier(INT): print("Investigation:+",Proficiency(INT), end=" ")
    if Dice(6) <= Modifier(INT): print("Nature:+",Proficiency(INT), end=" ")
    if Dice(6) <= Modifier(INT): print("Religion:+",Proficiency(INT), end=" ")
    if Dice(6) <= Modifier(WIS): print("Animal Handling:+",Proficiency(WIS), end=" ")
    if Dice(6) <= Modifier(WIS): print("Insight:+",Proficiency(WIS), end=" ")
    if Dice(6) <= Modifier(WIS): print("Medicine:+",Proficiency(WIS), end=" ")
    if Dice(6) <= Modifier(WIS): print("Perception:+",Proficiency(WIS), end=" ")
    if Dice(6) <= Modifier(WIS): print("Survival:+",Proficiency(WIS), end=" ")
    if Dice(6) <= Modifier(CHA): print("Deception:+",Proficiency(CHA), end=" ")
    if Dice(6) <= Modifier(CHA): print("Intimidation:+",Proficiency(CHA), end=" ")
    if Dice(6) <= Modifier(CHA): print("Performance:+",Proficiency(CHA), end=" ")
    if Dice(6) <= Modifier(CHA): print("Persuasion:+",Proficiency(CHA), end=" ")
    print("\n")
    
    print("Passive Perception:", 10 + Modifier(WIS) + Modifier(Lvl/2) )

    
    print("\n")
    print("SPELLCASTING:\n Spellsave DC:", 10+ Modifier(max(INT,WIS,CHA)))
    print(" To hit: +", Modifier(max(INT,WIS,CHA)+ Lvl/5))


    print("\n")
    print("COMBAT ACTIONS:")
    print (Attack("Melee"))

    print (Attack(Dice(4)), "+", Dice(Dice(int(Lvl/2))) , random.choice(["d4 ","d6 ","d8 ", "d10 ", "d12 "]) + Damage() +" dmg on a failed Saving Throw at DC ", 10 + Modifier(random.choice([STR,DEX,CON,INT,WIS,CHA ])), random.choice(["STR","DEX","CON","INT","WIS","CHA" ]), "saving throw.")

    print("\n")
    print(Actions(bg))
    print(Actions(rc))
    print(Actions())
    print("\n")

    if Lvl >= 15:
        print("LEGENDARY ACTIONS:")
        print(Legendary(bg))
        print(Legendary(rc))


NPC()
