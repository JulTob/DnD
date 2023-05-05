# NPC creator 
import random
from math import floor

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
        "The Ancient",
        "The Badger",
        "The Battle",
        "The Baron of",
        "The Bat",
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
        "The Brown",
        "The Brain",
        "The Bringer",
        "The Butterfly",
        "The Cat",
        "The Camel",
        "The Climate",
        "The Chain",
        "The Champion",
        "The Chief",
        "The Circus",
        "The Collector",
        "The Conjurer",
        "The Coral",
        "The Clokwork",
        "The Copper",
        "The Cursed",
        "The Crab",
        "The Crimson",
        "The Crown",
        "The Deadly",
        "The Death",
        "The Dawning",
        "The Dark",
        "The Devourer of",
        "The Doctor", 
        "The Deep",
        "The Divine",
        "The Diviner",
        "The Dream",
        "The Dust",
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
        "The Errant",
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
        "The Impulse",
        "The Inkwork",
        "The Iron",
        "The Ironbark",
        "The Ice",
        "The Icicle",
        "The Ink",
        "The Intellect",
        "The Innoble",
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
        "The Long",
        "The Master",
        "The Mad",
        "The Mage",
        "The Magma",
        "The Mental",
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
        "The Sand",
        "The Science",
        "The Shadow",
        "The Silver",
        "The Skelleton",
        "The Smiling",
        "The Smoke",
        "The Spring",
        "The Steam",
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
        "The Trival",
        "The Vampiric",
        "The Veteran",
        "The Violet",
        "The Voice",
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
        "Acolyte",
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
        " Chemist",
        "Champion",
        "Chimera",
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
        "Drone",
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
        "Hermit",
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
        "Man",
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
        "Of Death",
        "Of The Abyss",
        "Of the Autumn",
        "Of The Crown",
        " Of The Desert",
        "Of The Dead",
        " Of The East",
        " Of The Forest",
        "Of The Fiends",
        " Of the Kingdom",
        " Of The Hills",
        "Of the Hells",
        " Of The North",
        " Of The Mountain",
        " Of the Old One",
        " Of The Plains",
        " Of the Pack",
        "Of The People",
        " Of The Sands",
        " Of The Sea",
        " Of The South",
        "Of The Summer",
        "Of The Spring",
        "Of The Storm"
        " Of The West",
        " Of The Winter",
        " Oni",
        "One",
        "Oracle",
        " Outlaw",
        "Owl",
        " Pathologist",
        " Paw",
        "Pixie",
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
        "Rune",
        "Sabertooth",
        "Saurius",
        "Salamander",
        "Satyr",
        " Scientist",
        "Scarecrow",
        "Scorpion",
        "Shadow",
        "Shark",
        "Shaman",
        "Sorcerer",
        "Snake",
        "Skeleton",
        "Skull",
        "Surgeon",
        "Sucubus",
        "Spirit",
        "Spider",
        "Specter",
        "Swashbuckler",
        "Swarm",
        "Sword",
        "Terror",
        "Trapper",
        "Trapecist",
        "Troll",
        "Thief",
        "Void",
        "Vampire",
        "Vulture",
        "Walker",
        " Warlock",
        "Warrior",
        "Werewolf",
        " Wizard",
        " Witch",
        " Witchhunter",
        " Writter" ,
        "Willow",
        "Wolf",
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
        "Healer",
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
        "Traveler",
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
        "Aven",
        "Beast", "Beast", "Beast",
        "Beastfolk", "Beastfolk",
        "Celestial", 
        "Construct",
        "Dragon", "Dragon", "Dragon",
        "Dwarf","Dwarf","Dwarf",
        "Elf","Elf","Elf","Elf",
        "Elemental",
        "Fey", "Fey",
        "Fiend",
        "Giant",
        "Genasi",
        "Gnome",
        "Goblin",
        "Hag",
        "Halfling",
        "Kobold",
        "Lizardfolk",
        "Monstrosity",
        "Ogre",
        "Ooze",
        "Orc",
        "Plant",
        "Snakefolk",
        "Tiefling",
        "Undead",
        "Unicorn",
        ""
        ]
    return random.choice(Races)












def AberrationName():
    Names = [
        "Intellect Devourer",
        "Illithid",
        ""]
    return random.choice(Names)

def AvenName():
    Names = [
        "Birdfolk",
        "Kenku",
        "Aarakocra",
        ""]
    return random.choice(Names)

def BeastName():
    Names = [
        "Ape", "Baboon", "Monkey",
        "Badger",
        "Bat",
        "Blood Hawk",
        "Boar",
        "Cat",
        "Camel",
        "Dino", "TRex", "Triceratops", "Velocirraptor", "Pteranodon",
        "Dodo",
        "Dog",
        "Crab",
        "Deer", "Elk",
        "Eagle", "Hawk",
        "Frog",
        "Giant Insect", "Giant Beetle", "Giant Centipede",
        "Goat",
        "Horse", "Mule", "Pony",
        "Hyena",
        "Insect", "Wasp", "Beetle",
        "Jackal",
        "Lion",
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
        "Tiger", "Sabertooth",
        "Vulture",
        "Wolf",
        ""]
    return random.choice(Names)
    
def BeastfolkName():
    Names = [
        "Centaur",
        "Gnoll",
        "Jackalmen",
        "Kitsune",
        "Lycan", 
        "Merfolk",
        "Minotaur",
        "Sharkfolk",
        "Werewolf",
        ""]
    return random.choice(Names)

def ConstructName():
    Names = [
        "Drone",
        "Homunculus",
        "Flying Sword",
        "Living Rug",
        "Animated Armor",
        ""]
    return random.choice(Names)

def DragonName():
    Names = [
        "Dragonborn",
        "Wyrmling",
        ""]
    return random.choice(Names)


def FiendName():
    Names = [
        "Devil",
        "Demon",
        "Imp",
        ""]
    return random.choice(Names)

def FeyName():
    Names = [
        "Pixie",
        "Satyr",
        "Sprite",
        "Nymph",
        "Dryad",
        ""]
    return random.choice(Names)

def GiantName():
    Names = [
        "Ogre",
        ""]
    return random.choice(Names)

def GoblinName():
    Names = [
        "Goblin",
        "Hobgoblin",
        "Bugbear",
        ""]
    return random.choice(Names)

def MonstrosityName():
    Names = [
        "Griffon",
        "Harpy",
        "Worg",
        "Kerberus",
        ""]
    return random.choice(Names)

def OrcName():
    Names = [
        ""]
    return random.choice(Names)

def PlantName():
    Names = [
        "Awakened Plant",
        "Fungus",
        "Myconid",
        "Spore",
        "Willow",
        ""]
    return random.choice(Names)
    
def UndeadName():
    Names = [
        "Crawling Limb",
        "Ghoul",
        "Skelleton",
        "Shadow",
        "Vampire",
        "Zombie",
        ""]
    return random.choice(Names)
    
    
def Name(Type):
    if Type == "Aberration": return AberrationName()
    if Type == "Aven": return AvenName()
    if Type == "Beast": return BeastName()
    if Type == "Beastfolk": return BeastfolkName()
    if Type == "Construct": return ConstructName()
    if Type == "Dragon": return DragonName()
    if Type == "Fey": return FeyName()
    if Type == "Fiend": return FiendName()
    if Type == "Giant": return GiantName()
    if Type == "Goblin": return GoblinName()
    if Type == "Monstrosity": return MonstrosityName()
    if Type == "Plant": return PlantName()
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
    return d1+d2+d3+d4 - min(d1,d2,d3,d4) + Dice(3)-1 + Dice(6)-Dice(6)
    
def Modifier(AS):
    if AS >= 10:
        return int((AS-10)/2)
    else:
        return int((AS-11)/2)

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

def Condition(dmg):
    ConditionsTypes = [
        "Blinded",
        "Charmed",
        "Deafened",
        "Exhaustion",
        "Frightened",
        "Grappled",
        "Incapacitated",
        "Invisible",
        "Paralyzed",
        "Petrified",
        "Poisoned",
        "Prone",
        "Restrained",
        "Stunned",
        "Unconscious",
        ""
        ]
    if dmg == "Slashing":
        return random.choice(["Exhaustion","Incapacitated", "Poisoned", "Prone" ])
    elif dmg == "Piercing":
        return random.choice(["Blinded","Exhaustion", "Incapacitated", "Poisoned", "Grappled" ])
    elif dmg == "Bludgeoning":
        return random.choice(["Blinded","Deafened","Exhaustion", "Incapacitated", "Prone", "Stunned","Uncoscious", "Grappled", "Restrained" ])
    elif dmg == "Poison":
        return random.choice(["Blinded", "Charmed", "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Restrained", "Unconscious"])
    elif dmg == "Acid":
        return random.choice(["Blinded", "Exhaustion", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Restrained","Unconscious"])
    elif dmg == "Fire":
        return random.choice(["Blinded", "Charmed", "Incapacitated", "Paralyzed", "Stunned", "Unconscious"])
    elif dmg == "Cold":
        return random.choice(["Exhaustion", "Incapacitated", "Paralyzed", "Petrified", "Restrained", "Grappled"])
    elif dmg == "Radiant":
        return random.choice(["Blinded", "Charmed", "Deafened", "Frightened", "Incapacitated", "Paralyzed", "Prone", "Stunned", "Unconscious"])
    elif dmg == "Necrotic":
        return random.choice([ "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Lightning":
        return random.choice(["Blinded", "Charmed", "Deafened", "Exhaustion", "Frightened", "Grappled", "Incapacitated", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Force":
        return random.choice(["Blinded","Deafened", "Exhaustion", "Incapacitated", "Prone", "Stunned", "Unconscious", "Grappled" ])
    elif dmg == "Psychic":
        return random.choice(["Blinded", "Charmed", "Deafened", "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Thunder":
        return random.choice(["Blinded", "Deafened", "Exhaustion", "Incapacitated", "Paralyzed", "Prone", "Stunned"])
    else:
        return random.choice(ConditionsTypes)
    
def SavingThrow(dmg):
    if dmg == "Slashing":
        st = random.choice(["STR","DEX"])
    elif dmg == "Piercing":
        st = random.choice(["STR","DEX","CON" ])
    elif dmg == "Bludgeoning":
        st = random.choice(["STR","DEX","CON"])
    elif dmg == "Poison":
        st = "CON"
    elif dmg == "Acid":
        st = random.choice(["STR","DEX","CON" ])
    elif dmg == "Fire":
        st = random.choice(["STR","DEX","CON", "CHA"])
    elif dmg == "Cold":
        st = random.choice(["STR","DEX","CON" ])
    elif dmg == "Radiant":
        st = random.choice(["DEX","CON","WIS","CHA" ])
    elif dmg == "Necrotic":
        st = random.choice(["STR","CON","WIS","CHA" ])
    elif dmg == "Lightning":
        st = random.choice(["DEX","CON","WIS", "INT" ])
    elif dmg == "Force":
        st = random.choice(["STR","CON","CHA" ])
    elif dmg == "Psychic":
        st = random.choice(["INT","WIS","CHA" ])
    elif dmg == "Thunder":
        st = random.choice(["STR","DEX","CON" ])
    else:
        st = "DEX"
    return st

def Recovery(con):
    if con == "Unconscious":
        st = random.choice(["CON","INT","WIS","CHA" ])
    elif con == "Stunned":
        st = random.choice(["CON","INT","WIS","CHA" ])
    elif con == "Restrained":
        st = random.choice(["STR","DEX","CON"])
    elif con == "Poisoned":
        st = random.choice(["CON", "WIS"])
    elif con == "Prone":
        st = random.choice(["STR","DEX","CON"])
    elif con == "Petrified":
        st = random.choice(["STR", "CON","INT","WIS","CHA" ])
    elif con == "Paralyzed":
        st = random.choice(["STR", "CON","WIS","CHA" ]) 
    elif con == "Invisible":
        st = random.choice(["CON","INT","WIS","CHA" ])      
    elif con == "Incapacitated":
        st = random.choice(["STR","CON","WIS","CHA" ]) 
    elif con == "Grappled":
        st = random.choice(["STR","DEX"]) 
    elif con == "Blinded":
        st = random.choice(["CON","INT","WIS","CHA"]) 
    elif con == "Frightened":
        st = random.choice(["CON","INT","WIS","CHA"]) 
    elif con == "Exhaustion":
        st = random.choice(["STR","CON","CHA"]) 
    elif con == "Deafened":
        st = random.choice(["STR","CON","WIS"]) 
    elif con == "Charmed":
        st = random.choice(["CHA","WIS"]) 
    else:
        st = "CON"
    return st

def SpecialAttack(Lvl,Mod ):
    dmg = Damage()
    con = Condition(dmg)
    r = ""

    r = r+ Attack(Dice(4)) + " +"
    r = r+"{}".format(Dice(Dice(1+int(Lvl/4))))
    r = r+random.choice(["d4 ","d6 ","d8 ", "d10 ", "d12 "])
    r = r + dmg
    r = r + " dmg" 
    r = r + " on a failed Saving Throw at DC "
    r = r + str((10 + Mod)) +" "
    r = r + SavingThrow(dmg) +  "."
    if Dice(40) <= Dice(10+Lvl):
        r = r + " The target is then affected by the " + con + " condition. "
        r = r + "The Condition may be countered with a succesful " + str((10 + Mod)) + " "+ Recovery(con) + " Saving Throw at the beggining of the target's turn."
    return r






























def Language(race = Race(), background = Background()):
    if race == "":
        race = Race()
    if background == "":
        background = Background()
    l = ""
    if race == "Human":
        l += "Common. "
    if race == "Aberration":
        l += ""
        
    if race == "Aven":
        l += "Common. "
        
    if race == "Beast":
        if Dice()==1:
            l += "Understands Common. "
        if Dice()==1:
            l += "Beastly Speech. "
        if Dice()==1:
            l += "Sylvan. "

    if race == "Beastfolk":
        l += "Common. Beastly Speech. "
        if Dice()==1:
            l += "Sylvan. "
        if Dice()==1:
            l += "Undercommon. "

    if race == "Celestial": 
        l += ""
    if race == "Construct":
        l += "Understands the languages of its creator. "
    if race == "Dragon":
        l += "Draconic. "
        if Dice(3)==1:
            l += "Common. "
        if Dice()==1:
            l += "Sylvan. "
    if race == "Dwarf":
        l += "Dwarvish. "
        if Dice(3)==1:
            l += "Common. "
        if Dice(3)==1:
            l += "Undercommon. "

    if race == "Elf":
        l += ""
        
    if race == "Elemental":
        l += ""
        if Dice(4)==1:
            l += "Ignan. "

        
    if race == "Fey":
        l += "Sylvan. "
        if Dice(3) == 1:
            l += "Common. "
        if Dice(3) == 1:
            l += "Elvish. "
            
    if race == "Fiend":
        l += "Common. "
        if Dice(2) == 1:
            l += "Infernal. "
        if Dice(2) == 1:
            l += "Abyssal. "

    if race == "Giant":
        l += "Common. Giant."
    if race == "Genasi":
        l += ""
    if race == "Gnome":
        l += ""
    if race == "Goblin":
        l += "Goblin. "
        if Dice(2)==1:
            l += "Common. "
    if race == "Hag":
        l += ""
    if race == "Halfling":
        l += ""
    if race == "Kobold":
        l += "Draconic. "
        if Dice(3)==1:
            l += "Common. "
    if race == "Lizardfolk":
        l += "Draconic. "
        if Dice(2)==1:
            l += "Common. "
    if race == "Monstrosity":
        if Dice(2)==1:
            l += "Common"
    if race == "Ooze":
        l += ""
    if race == "Orc":
        l += ""
    if race == "Plant":
        if Dice(3)==1:
            l += "Common. "
    if race == "Snakefolk":
        l += "Draconic, "
        if Dice(3)==1:
            l += "Common. "
    if race == "Tiefling":
        l += ""
    if race == "Undead":
        l += "Understands languages it knew in life. "
        if Dice(2)==1:
            l += "Common. "

    return l



def Magic(Lvl, race = Race(), background = Background()):
    if race == "":
        race = Race()
    if background == "":
        background = Background()

    cantrip = "Cantrips (at will): "
    first = "1st Level Spells: "
    second = "2nd Level Spells: "
    third = "3rd Level Spells: "
    fourth = "4th Level Spells: "

    slots1 = 0
    slots2 = 0
    slots3 = 0
    slots4 = 0
    
    one = "1/Day each: "
    two = "2/Day each: "
    three = "3/Day each: "

    for L in range(int(1+Lvl/4)):

                
                
        if background == "Acolyte":
            if Dice(2) == 1:
                cantrip +=  "\n- Light"
                
        if background == "Acolyte":
            if Dice(2) == 1:
                cantrip +=  "\n- Sacred flame"
                
        if background == "Acolyte":
            if Dice(2) == 1:
                cantrip +=  "\n- Thaumaturgy"
            
        if background == "Acolyte":
            if Dice(2) == 1:
                first += "\n- Bless"
                slots1 += Dice(3)
                
        if background == "Acolyte":
            if Dice(2) == 1:
                first += "\t cure wounds"  
                slots1 += Dice(3)
                
        if background == "Acolyte":
            if Dice(2) == 1:
                first += "\t sanctuary"   
                slots1 += Dice(3)
    
    
        if background == "Cultist":
            if Dice(2) == 1:
                cantrip +=  "\t Light"

        if background == "Cultist":
            if Dice(2) == 1:
                cantrip += "\t Sacred flame"

        if background == "Cultist":
            if Dice(2) == 1:
                cantrip += "\t Thaumaturgy" 

            
        if background == "Cultist":
            if Dice(3) == 1:
                first += "\t Command"
                slots1 += Dice(3)

        if background == "Cultist":
            if Dice(3) == 1:
                first += "\t inflict wounds"
                slots1 += Dice(4)

        if background == "Cultist":
            if Dice(3) == 1:
                first += "\t shield of faith"
                slots1 += Dice(4)
            

        if background == "Cultist":
            if Dice(5) == 1:
                second += "\t hold person" 
                slots2 += Dice(3)

        if background == "Cultist":
            if Dice(5) == 1:
                second += "\t spiritual weapon"
                slots2 += Dice(3)

        if background=="Healer":
            if Dice(2) == 1:
                cantrip +=  "\t guidance" 

        if background=="Healer":
            if Dice(2) == 1:
                cantrip +=  "\t sacred flame"

        if background=="Healer":
            if Dice(2) == 1:
                first +=  "\t cure wounds"
                slots1 += Dice(2)
            
        if background == "Mage":
            if Dice(2) == 1:
                cantrip +=  "\n - Firebolt" 

        if background == "Mage":
            if Dice(2) == 1:
                cantrip +=  "\n - Light" 

        if background == "Mage":
            if Dice(2) == 1:
                first +=  "\n - Sleep"
                slots1 += Dice(2)

    
        if background == "Priest":
            if Dice() == 1:
                cantrip += "\t Guidance"

        if background == "Priest":
            if Dice() == 1:
                cantrip += "\n- Light"
                
        if background == "Priest":
            if Dice() == 1:
                cantrip += "\n- Sacred Flame"
                
        if background == "Priest":
            if Dice() == 1:
                cantrip += "\n- Thaumaturgy"
             
        if background == "Priest":
            if Dice() == 1:
                first += "cure wounds"
                slots1 += Dice(4)
                
        if background == "Priest":
            if Dice() == 1:
                first += "guiding bolt"
                slots1 += Dice(4)
        if background == "Priest":
            if Dice() == 1:
                first += "sanctuary" 
                slots1 += Dice(4)
        if background == "Priest":
            if Dice() == 1:
                second += "lesser restoration"
                slots2 += Dice(3)
        if background == "Priest":
            if Dice() == 1:
                second += "spiritual weapon"
                slots2 += Dice(3)
        if background == "Priest":
            if Dice() == 1:
                third += "dispel magic"
                slots3 += Dice(2)
        if background == "Priest":
            if Dice() == 1:
                third += "spirit guardians"
                slots3 += Dice(2)
   
        if background == "Shaman":
            if Dice(2) == 1:
                cantrip +=  "\t druidcraft" 
            if Dice(2) == 1:
                cantrip +=  "\t produce flame" 
            if Dice(2) == 1:
                cantrip +=  "\t thorn whip" 
            slots1 += Dice(4)
            if Dice(2) == 1:
                first +=  "\t entangle"
            if Dice(2) == 1:
                first +=  "\t fog cloud"
            slots2 += Dice(3)
            if Dice(2) == 1:
                second +=  "\t heat metal"
            if Dice(2) == 1:
                second +=  "\t spike growth"
            slots3 += Dice(2)
            if Dice(2) == 1:
                third +=  "\t conjure animals"
            if Dice(2) == 1:
                third +=  "\t plant growth"
  
  
  
        if race == "Aberration":
            if Dice() == 1:
                one += "\n- Stench Spray (1/Day). \n\t Each creature in a 15-foot cone originating from the Aberration must succeed on a DC 10 Dexterity saving throw or be coated in a foul-smelling liquid. A coated creature exudes a horrible stench for 1d4 hours. The coated creature is poisoned as long as the stench lasts, and other creatures are poisoned while with in 5 feet of the coated creature. A creature can remove the stench on itself by using a short rest to bathe in water, alcohol, or vinegar."

        if race == "Aven":
            if Dice(8) == 1:
                cantrip +=  "\n- Summon Air Elemental. \n\t Five aarakocra within 30 feet of each other can magically summon an air elemental. Each of the five must use its action and movement on three consecutive turns to perform an aerial dance and must maintain concentration while doing so (as if concentrating on a spell). When all five have finished their third turn of the dance, the elemental appears in an unoccupied space within 60 feet of them. It is friendly toward them and obeys their spoken commands. It remains for 1 hour, until it or all its summoners die, or until any of its summoners dismisses it as a bonus action. A summoner can't perform the dance again until it finishes a short rest. When the elemental returns to the Elemental Plane of Air, any aarakocra within 5 feet of it can return with it."



        if race == "Beastfolk":
            if Dice(10) == 1:
                cantrip +=  "\n- Sleep Gaze. \n\t The Beastfolk gazes at one creature it can see within 30 feet of it. The target must make a DC [10+%Wis] Wisdom saving throw. On a failed save, the target succumbs to a magical slumber, falling unconscious for 10 minutes or until someone uses an action to shake the target awake. A creature that successfully saves against the effect is immune to this Beastfolk's gaze for the next 24 hours. Undead and creatures immune to being charmed aren't affected by it."

        if race == "Beastfolk":
            if Dice() == 1:
                cantrip +=  "\n- Sacred Flame."

        if race == "Beastfolk":
            if Dice() == 1:
                cantrip +=  "\n- Thaumaturgy."

        if race == "Beastfolk":
            if Dice() == 1:
                first +=  "\n- Bane"
                slots1 += Dice(3)
                
        if race == "Beastfolk":
            if Dice() == 1:
                first +=  "\n- Shield Of Faith"
                slots1 += Dice(3)


        if race == "Celestial":
            if Dice(2) == 1:
                cantrip +=  "\n- Light" 
        if race == "Celestial":
            if Dice(2) == 1:
                cantrip +=  "\n- Sacred flame" 
        if race == "Celestial":
            if Dice(2) == 1:
                cantrip +=  "\n- Thaumaturgy" 
        if race == "Celestial":
            if Dice(2) == 1:
                first +=  "\n- Bless" 
                slots1 += Dice(3)
        if race == "Celestial":
            if Dice(2) == 1:
                first +=  "\n- Cure wounds" 
                slots1 += Dice(3)
        if race == "Celestial":
            if Dice(2) == 1:
                first +=  "\n- Sanctuary"
                slots1 += Dice(3)

               
        if race == "Dragon":
            cantrip += "\n- Breath Weapons"
            cantrip += "(Recharge 5-6) \t The dragon uses one of the following breath weapons:"
            if Dice(10) == 1:
                cantrip += "\n  - Fire Breath \n\t The dragon exhales fire in a 20-foot line that is 5 feet wide. Each creature in that line must make a DC [10+%Con] Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one."
            elif Dice(10) == 2:
                cantrip += "\n  - Sleep Breath \n\t The dragon exhales sleep gas in a 15-foot cone. Each creature in that area must succeed on a DC [10+%Con] Constitution saving throw or fall unconscious for 1 minute. This effect ends for a creature if the creature takes damage or someone uses an action to wake it."
            elif Dice(10) == 3:
                cantrip += "\n  - Acid Breath \n\t . The dragon exhales acid in a 20-foot line that is 5 feet wide. Each creature in that line must make a DC [10+%Con] Dexterity saving throw, taking 18 (4d8) acid damage on a failed save, or half as much damage on a successful one"
            elif Dice(10) == 4:
                cantrip += "\n  - Slowing Breath \n\t The dragon exhales gas in a 15-foot cone. Each creature in that area must succeed on a DC [10+%Con] Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the start of each of its turns, ending the effect on itself with a successful save."
            elif Dice(10) == 5:
                cantrip += "\n  - Euphoria Breath \n\t The dragon exhales a puff of euphoria gas at one creature within 5 feet of it. The target must succeed on a DC [10+%Con] Wisdom saving throw, or for 1 minute, the target can't take reactions and must roll a d6 at the start of each of its turns to determine its behavior during the turn: \n\t\t 1–4. The target takes no action or bonus action and uses all of its movement to move in a random direction. \n\t\t 5–6. The target doesn't move, and the only thing it can do on its turn is make a DC [10+%Con] Wisdom saving throw, ending the effect on itself on a success."
            elif Dice(10) == 6:
                cantrip += "\n  - Repulsion Breath"
            elif Dice(10) == 7:
                cantrip += "\n  - Poison Breath"

        if race == "Dragon":
            if Dice(10) == 1:
                cantrip += "\n- Change Shape \n\t The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice).In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."

        if race == "Dragon":
            if Dice() == 1:
                cantrip += "\n- Color Spray"

        if race == "Dragon":
            if Dice() == 1:
                cantrip += "\n- Dancing Lights"

        if race == "Dragon":
            if Dice() == 1:
                cantrip += "\n- Mage Hand"

        if race == "Dragon":
            if Dice() == 1:
                cantrip += "\n- Minor Illusion"

        if race == "Dragon":
            if Dice(8) == 1:
                cantrip += "\n- Mirror Image"



        if race == "Dwarf":
            if Dice() == 1:
                cantrip += "\n- Enlarge (Recharges after a Short or Long Rest). \n\t For 1 minute, the Dwarf magically increases in size, along with anything it is wearing or carrying. While enlarged, the Dwarf is Large, doubles its damage dice on Strength-based weapon attacks (included in the attacks), and makes Strength checks and Strength saving throws with advantage. If the Dwarf lacks the room to become Large, it attains the maximum size possible in the space available."

        if race == "Dwarf":
            if Dice() == 1:
                cantrip += "\n- Invisibility (Recharges after a Short or Long Rest). \n\t The dwarf magically turns invisible until it attacks, casts a spell, or until its concentration is broken, up to 1 hour (as if concentrating on a spell). Any equipment the Dwarf wears or carries is invisible with it."


        if race == "Elemental":
            if Dice() == 1:
                cantrip += "\n dancing lights"
                
        if race == "Elemental":
            if Dice() == 1:
                one += "\t blur"

        if race == "Elemental":
            if Dice() == 1:
                one += "\t Sleep"

        if race == "Elemental":
            if Dice() == 1:
                cantrip += "\n Cinder Breath \t (Recharge 6). The Elemental exhales a 15-foot cone of smoldering ash. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw or be blinded until the end of the Elemental's next turn."

        if race == "Elemental":
            if Dice() == 1:
                cantrip += "\n Blinding Breath \t (Recharge 6). The Elemental exhales a 15-foot cone of blinding dust. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw or be blinded for one minute."

        if race == "Elemental":
            if Dice() == 1:
                cantrip += "\n Steam Breath \t (Recharge 6). The Elemental exhales a 15-foot cone of scalding steam. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw, taking 4 (1d8) fire damage on a failed save, or half as much damage on a successful one."

        if race == "Elemental":
            if Dice(7) == 1:
                cantrip += "\n - Frost Breath \n\t (Recharge 6). The Elemental exhales a 15-foot cone of cold air. Each creature in that area must succeed on a DC [10+%Con] Dexterity saving throw, taking 5 (2d4) cold damage on a failed save, or half as much damage on a successful one."

        if race == "Elemental":
            if Dice() == 1:
                cantrip += "\n - Fire Breath \t (Recharge 6). The Elemental exhales a 15-foot cone of cold air. Each creature in that area must succeed on a DC [10+%Con] Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one."
                
        if race == "Elemental":
            if Dice(3) == 1:
                one += "\n - Summon Mephits (1/Day) \n\t The Elemental has a 25 percent chance of summoning 1d4 mephits. A summoned mephit appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other mephits. It remains for 1 minute, until it or its summoner dies, or until its summoner dismisses it as an action."

        if race == "Elemental":
            if Dice() == 1:
                one += "\n Innate Spellcasting (1/Day) \n\t The Elemental can innately cast fog cloud, requiring no material components. Its innate spellcasting ability is Charisma."
                
        if race == "Elemental":
            if Dice() == 1:
                one += "\n Innate Spellcasting (1/Day) \n\t The Elemental can innately cast heat metal, requiring no material components. Its innate spellcasting ability is Charisma."
            
        if race == "Elf":
            if Dice() == 1:
                cantrip += "\t dancing lights"

        if race == "Elf":
            if Dice() == 1:
                one += "\t darkness"

        if race == "Elf":
            if Dice() == 1:
                one += "\t faerie fire"
                
        if race == "Fey":
            if Dice() == 1:
                cantrip += "\n Teleport (Recharge 4–6). \n\t The Fey magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the Fey can make one bite attack."

        if race == "Fae": 
            if Dice() == 1:
                cantrip +=  "\n- Druidcraft"

        if race == "Fae": 
            if Dice(3) == 1:
                three += "\n-Entangle" 

        if race == "Fae": 
            if Dice(3) == 1:
                three += "\n-Goodberry"
   
        if race == "Fae": 
            if Dice() == 1:
                one += "\n-Barkskin"

        if race == "Fae": 
            if Dice() == 1:
                one += "\n- Pass without trace"

        if race == "Fae": 
            if Dice() == 1:
                one += "\n- Shillelagh"

        if race == "Fey":
            if Dice() == 1:
                cantrip += "\n Heart Sight. \n\t The Fey touches a creature and magically knows the creature's current emotional state. If the target fails a DC [10+%Cha] Charisma saving throw, the Fey also knows the creature's alignment. Celestials, fiends, and undead automatically fail the saving throw."

        if race == "Fey":
            if Dice() == 1:
                cantrip += "\n Invisibility. \n\t The Fey  magically turns invisible until it attacks or casts a spell, or until its concentration ends (as if concentrating on a spell). Any equipment the Fey wears or carries is invisible with it."

                
        if race == "Fey":
            if Dice(3) == 1:
                cantrip += "\t druidcraft"
                
        if race == "Fey":
            if Dice() == 1:
                one += "\t confusion"
                
        if race == "Fey":
            if Dice() == 1:
                one += "\t dancing lights"
                
        if race == "Fey":
            if Dice() == 1:
                one += "\t detect evil and good"   
                
        if race == "Fey":
            if Dice() == 1:
                one += "\t detect thoughts"   
                
        if race == "Fey":
            if Dice() == 1:
                one += "\t dispel magic"   
                
        if race == "Fey":
            if Dice() == 1:
                one += "\t entangle"   
                
        if race == "Fey":
            if Dice() == 1:
                one += "\t fly"   
                
        if race == "Fey":
            if Dice() == 1:
                one += "\n - phantasmal force"   
                
        if race == "Fey":
            if Dice() == 1:
                one += "\n polymorph"   
                
        if race == "Fey":
            if Dice() == 1:
                one += "\n sleep"   

        if race == "Fey":
            if Dice() == 1:
                one += "\n Charming Melody [DC 10+%Cha Wisdom saving throw]\n\t The creature is charmed by the Fey for 1 minute. If the Fey or any of its companions harms the creature, the effect on it ends immediately."   

        if race == "Fey":
            if Dice() == 1:
                one += "\n - Frightening Strain [DC 10+%Cha Wisdom saving throw] \n\t The creature is charmed by the Fey for 1 minute. If the Fey or any of its companions harms the creature, the effect on it ends immediately."   

        if race == "Fey":
            if Dice() == 1:
                one += "\n Gentle Lullaby [DC 10+%Cha Wisdom saving throw] \n\t The creature falls asleep and is unconscious for 1 minute. The effect ends if the creature takes damage or if someone takes an action to shake the creature awake."   

        if race == "Fiend":
            if Dice() == 1:
                one += "\n Scare \n\t One creature of the Fiend's choice within 20 feet of it must succeed on a DC 10 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, with disadvantage if the Fiend is within line of sight, ending the effect on itself on a success."   


        if race == "Gnome":
            if Dice()==1:
                cantrip += "\t Nondetection (self only)"

        if race == "Gnome":
            if Dice()==1:
                one += " \t Blindness/Deafness"

        if race == "Gnome":
            if Dice()==1:
                one += " \n- Blur"

        if race == "Gnome":
            if Dice()==1:
                one += " \t Disguise Self"


        if race == "Monstrosity":
            if Dice() == 1:
                one += "\n - Darkness Aura: \n\t A 15-foot radius of magical darkness extends out from the Monstrosity, moves with it, and spreads around corners. The darkness lasts as long as the Monstrosity maintains concentration, up to 10 minutes (as if concentrating on a spell). Darkvision can't penetrate this darkness, and no natural light can illuminate it. If any of the darkness overlaps with an area of light created by a spell of 2nd level or lower, the spell creating the light is dispelled."
                
        if race == "Monstrosity":
            if Dice() == 1:
                cantrip += "\n - Luring Song: \n\t The monstrosity sings a magical melody. Every humanoid and giant within 300 feet of the harpy that can hear the song must succeed on a DC [10+%Cha] Wisdom saving throw or be charmed until the song ends. The monstrosity must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the monstrosity is incapacitated. While charmed by the monstrosity, a target is incapacitated and ignores the songs of other monstrosities. If the charmed target is more than 5 feet away from the monstrosity, the target must move on its turn toward the monstrosity by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the monstrosity, a target can repeat the saving throw. A creature can also repeat the saving throw at the begguining of each of its turns. If a creature's saving throw is successful, the effect ends on it. A target that successfully saves is immune to this monstrosity's song for the next 24 hours."
           
        if race == "Ooze":
            if Dice()==1:
                cantrip += " \t Psychic Crush (Recharge 5–6). \n\t The ooze targets one creature that it can sense within 60 feet of it. The target must make a DC 10 Intelligence saving throw, taking 10 (3d6) psychic damage on a failed save, or half as much damage on a successful one."
                
        if race == "Plant": 
            if Dice() == 1:
                three += "\n - Pacifying Spores \n\t The Plant ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC [10+%CON] Constitution saving throw or be stunned for 1 minute. The target can repeat the saving throw at the start of each of its turns, ending the effect on itself on a success."   

        if race == "Plant": 
            if Dice() == 1:
                cantrip += "\n - Rapport Spores \n\t A 20-foot radius of spores extends from the plant. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour."   
                
        if race == "Plant": 
            if Dice(8) == 1:
                one += "\n - Caustic Spores \n\t The Plant releases spores in a 30-foot cone. Each creature inside the cone must succeed on a DC [10+%Con] Dexterity saving throw or take 3 (1d6) acid damage at the start of each of the plant's turns. A creature can repeat the saving throw at the start of its turn, ending the effect on itself on a success. The save DC is 8 + the plant's Constitution modifier + the plant's proficiency bonus."  

        if race == "Plant": 
            if Dice(10) == 1:
                one += "\n - Infestation Spores \n\t The plant releases spores that burst out in a cloud that fills a 10-foot-radius sphere centered on it, and the cloud lingers for 1 minute. Any flesh-and-blood creature in the cloud when it appears, or that enters it later, must make a DC [10+%CON] Constitution saving throw. The save DC is 8 + the plant's Constitution modifier + the plant's proficiency bonus. On a successful save, the creature can't be infected by these spores for 24 hours. On a failed save, the creature is infected with a disease called the spores of Zuggtmoy and also gains a random form of indefinite madness (determined by rolling on the Madness of Zuggtmoy table) that lasts until the creature is cured of the disease or dies. While infected in this way, the creature can't be reinfected, and it must repeat the saving throw at the end of every 24 hours, ending the infection on a success. On a failure, the infected creature's body is slowly taken over by fungal growth, and after three such failed saves, the creature dies and is reanimated as a spore servant if it's a humanoid or a Large or smaller beast. \n d100 \t	Flaw (lasts until cured) \n 01-20 \t I see visions in the world around me that others do not. \n 21-40 \t I periodically slip into a catatonic state, staring off into the distance for long stretches at a time. \n 41-60 \t I see an altered version of reality, with my mind convincing itself that things are true even in the face of overwhelming evidence to the contrary. \n 61-80 \t My mind is slipping away, and my intelligence seems to wax and wane. \n  81-00 \t I am constantly scratching at unseen fungal infections." 
                
        if race == "Plant": 
            if Dice(8) == 1:
                one += "\n - Euphoria Spores \n\t The plant releases a cloud of spores in a 20-foot-radius sphere centered on itself. Other creatures in that area must each succeed on a DC [10+%Con] Constitution saving throw or become poisoned for 1 minute. The save DC is 8 + the plant's Constitution modifier + the plant's proficiency bonus. A creature can repeat the saving throw at the start of each of its turns, ending the effect early on itself on a success. When the effect ends on it, the creature gains one level of exhaustion."  

        if race == "Undead": 
            if Dice(8) == 1:
                cantrip += "\n - Strength Drain \n\t On an attack hit the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. \n\t If a non-evil humanoid dies from this attack, a new shadow rises from the corpse 1d4 hours later."  

        if Dice() == 1: 
            background = Background()
        if Dice() == 1: 
            race = Race()

    r = "\n"
    if not(cantrip == "Cantrips (at will): "):
        r += cantrip + "\n"
    if not(first == "1st Level Spells: "):
        r += "[{}]".format(Dice(slots1)) + first + "\n"
    if not( second == "2nd Level Spells: "):
        r += "[{}]".format(Dice(slots2)) + second + "\n"
    if not(third == "3rd Level Spells: "):
        r += "[{}]".format(Dice(slots3)) + third + "\n"
    if not(fourth == "4th Level Spells: "):
        r += "[{}]".format(Dice(slots4)) + fourth + "\n"
    if not(one == "1/Day each: "):
        r += one
    if not(two == "2/Day each: "):
        r += two
    if not(three == "3/Day each: "):
        r += three
    return  r
























def Actions(Type=""):
    r = ""

    if Type == "Assassin":
        r = r + "\n- Superior Invisibility"

    if Type == "Beast" or Type == "Beastfolk": 
        if Dice() == 1:
            r = r+ "\n- Speed. \n\t 50 ft."

    if Type == "Beast" or Type == "Beastfolk": 
        if Dice() == 1:
            r = r+ "\n- Climb. \n\t 30 ft."

    if Type == "Beast" or Type == "Beastfolk": 
        if Dice() == 1:
            r = r+ "\n- Burrow. \n\t 10 ft."  

    if Type == "Beast" or Type == "Beastfolk": 
        if Dice() == 1:
            r = r+ "\n- Fly. \n\t 60 ft."  
            if Dice(3)==1:
                r = r+ "\n Flyby. \n\t The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach."
        elif Dice() == 1: 
            r = r+ "\n- Fly. \n\t 80 ft."  
            if Dice()==1:
                r = r+ "\n Flyby. \n\t The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach."

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(2) == 1:        
            if Dice(4) == 1:
                r = r+ "\n- Darkvision." 
                if Dice(2)==1:
                    r = r+ "\n\t 30 ft."
                elif Dice(2) == 1:
                    r = r+ "\n\t 60 ft."
                else:
                    r = r+ "\n\t 120 ft."
        else: 
            if Dice() == 1:
                r = r+ "\n- Blindsight." 
                if Dice()==1:
                    r = r+ "\n\t 60 ft."
                else:
                    r = r+ "\n\t 30 ft."
                if Dice()==1:
                    r = r+ "\nEcholocation. \n\t The Beast can't use its blindsight while deafened."
                    r = r+ "\nKeen Hearing. \n\t The beast has advantage on Wisdom (Perception) checks that rely on hearing."

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice() == 1:
            r = r+ "\n- Keen Senses\n\t The beast has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell."
        else:
            if Dice() == 1:
                r = r+ "\n- Keen Smell. \n\t The Beast has advantage on Wisdom (Perception) checks that rely on smell."    
            if Dice() == 1:
                r = r+ "\n- Keen Sight. \n\tThe beast has advantage on Wisdom (Perception) checks that rely on sight."
            if Dice() == 1:
                r = r+ "\n- Keen Hearing. \n\tThe beast has advantage on Wisdom (Perception) checks that rely on hearing."
                
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice() == 1:
            r = r+ "\n-  Pack Tactics. \n\t The Beast has advantage on an attack roll against a creature if at least one of the beast's allies is within 5 feet of the creature and the ally isn't incapacitated."

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice() == 1:
            r = r+ "\n-  Multiattack. \n\t The Beast makes two attacks."

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n - Grappler. \n\t On an attack, the target is grappled,  [DC 10+%STR]"
            if Dice(2) == 1:
                r = r+ "\n - Constrict. \n\t Until the grapple ends, the creature is restrained. The creature can't constrict another creature."

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n - Charge \n\t If the Beast moves at least 20 feet straight toward a target and then hits it with an attack on the same turn, the target takes an extra [2d6+%STR] bludgeoning damage. If the target is a creature, it must succeed on a DC=[10+%STR] Strength saving throw or be knocked prone."

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n - Relentless \n\t Recharges after a Short or Long Rest). \n\t If the beast takes 7 damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n- Water Breathing. The beast can breathe underwater"
            r = r+ "\n- Swim. \n\t 60 ft."  
            if Dice(2) == 1:
                r = r + "\n- Underwater Camouflage. \n\t The beast has advantage on Dexterity (Stealth) checks made while underwater."
                
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n- Hold Breath. \n\t The beast can hold its breath for 15 minutes"
            r = r+ "\n- Swim. \n\t 30 ft."  
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice() == 1:
            r = r+ "\n- Blood Frenzy \n\t The beast has advantage on melee attack rolls against any creature that doesn't have all its hit points."

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n- Amphibious"
            r = r+ "\n- Swim. \n\t 30 ft."  
            if Dice() == 1:
                r = r+ "\n- Standing Leap. \n\t The Beast's long jump is up to half his speed in feet and its high jump is up to third his speed, with or without a running start."  

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r + "\n- Spider Climb \n\t The beast can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."  
            if Dice(2) == 1:
                r = r + "\n- Web Sense \n\t While in contact with a web, the spider knows the exact location of any other creature in contact with the same web."
            if Dice(2) == 1:
                r = r + "\n- Web Walker \n\t The spider ignores movement restrictions caused by webbing."

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice() == 1:
            r = r+ "\n - Running Leap"
 
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice() == 1:
            r = r+ "\n - Fly \n\t 60 ft"
            if Dice() == 1:
                r = r+ "\n - Flyby \n\t The beast doesn't provoke opportunity attacks when it flies out of an enemy's reach."


    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(10) == 1:
            r = r+ "\n - Pounce \n\t If the beast moves at least 20 feet straight toward a creature and then hits it with an attack on the same turn, that target must succeed on a DC [10+%STR] Strength saving throw or be knocked prone. If the target is prone, the Beast can make one attack against it as a bonus action."
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n- Illumination.\n\tThe beast sheds bright light in a 10-foot radius and dim light for an additional 10 ft."
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n-Sure-Footed \n\t The beast has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice() == 1:
            r = r + "\n- Hold Breath. \n\t The beast can hold its breath for 30 minutes."
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(10) == 1:
            r = r+ "\n- Mimicry \n\t The Raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n- Beast of Burden \n\t The Beast is considered to be a Large animal for the purpose of determining its carrying capacity."
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n- Swamp Camouflage \n\t The Beast has advantage on Dexterity (Stealth) checks made to hide in swampy terrain."
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(4) == 1:
            r = r+ "\n- Bite. \n\t  Melee Weapon Attack: reach 5 ft., one target. Hit: 4 (1d6 + %STR) piercing damage, and the target is grappled (escape DC 10 + %STR). Until this grapple ends, the target is restrained, and the beast can't bite another target."
            if Dice() == 1:
                r = r+ "\n- Swallow. \n\t  The beast makes one bite attack against a target creature smaller than themselves it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the beast, and it takes 6 (2d4+%CON) acid damage at the start of each of the beast's turns. The beast can have only one target swallowed at a time. If the beast dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 feet of movement, exiting prone."
                
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(12) == 1:
            r = r+ "\n-  Hold Breath. \n\t  The beast can hold its breath for 15 minutes.\n-  swimming \n\t  speed of 30 feet.)"
            r = r+ "\n-  Spider Climb. \n\t  The beast can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(12) == 1:
            r = r+ "\n-  Hold Breath. \n\t  The beast can hold its breath for 1 hour."
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(12) == 1:
            r = r+ "\n-  Rampage. \n\t When the Beast reduces a creature to 0 hit points with a melee attack on its turn, the beast can take a bonus action to move up to half its speed and make a bite attack."

    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(12) == 1:
            r = r+ "\n-  Slippery. \n\t The beast has advantage on ability checks and saving throws made to escape a grapple."
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice() == 1:
            r = r + "\n - Sunlight Sensitivity.  \n\t While in sunlight, the lizardfolk has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    if Type == "Beastfolk":
        r = r + "\n- Speak with Animal \n\t The Beastfolk can communicate simple concepts to his affinity animal when it speaks in Beast language."

    if Type == "Beastfolk":
        if Dice()==1:
            r = r + "\n- Damage Immunities \n\t Bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered."

    if Type == "Beastfolk":
        r = r + "\n- Beast Telepathy \n\t The Beastfolk can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy."

    if Type == "Beastfolk":
        if Dice()==1:
            r = r+ "\n - Shapechanger \n\t The Beastfolk can use its action to polymorph into a specific Medium human or a Beast-humanoid hybrid, or back into its beast form. Other than its size, its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."

    if Type == "Beastfolk":
        if Dice()==1:
            r = r+"\n - Pack Tactics \n\t The Beastfolk has advantage on an attack roll against a creature if at least one of the Beastfolk's allies is within 5 feet of the creature and the ally isn't incapacitated."

    if Type == "Beastfolk":
        if Dice()==1:
            r = r+"\n - Otherworldly Perception \n\t The Beastfolk can sense the presence of any creature within 30 feet of it that is invisible or on the Ethereal Plane. It can pinpoint such a creature that is moving."

    if Type == "Criminal":
        if Dice()==1:
            r = r+"\n - Pack Tactics \n\t The Criminal has advantage on an attack roll against a creature if at least one of the Criminal's allies is within 5 feet of the creature and the ally isn't incapacitated."

    if Type == "Dragon":
        if Dice(2) == 1:
            r = r+ "\n- Fly: 60 ft"
            if Dice() == 1:
                r = r+ "\n- Flyby \n\t The dragon is an agile flier, quick to fly out of enemies' reach.The dragon doesn't provoke an opportunity attack when it flies out of an enemy's reach."

    if Type == "Dragon":
        if Dice() == 1:
            r = r+ "\n- Burrow: 15 ft"

    if Type == "Dragon":
        if Dice() == 1:
            r = r+ "\n- Climb: 30 ft"

    if Type == "Dragon":
        if Dice(2) == 1:
            r = r+ "\n- Darkvision: 60 ft"
        elif Dice() == 1:
                r = r+ "\n- Blindsight: 10 ft"
        elif Dice() == 1:
                r = r+ "\n- Blindsight: 60 ft"
        elif Dice(12) == 1:
                r = r+ "\n- Truesight: 60 ft"


            
    if Type == "Dragon":
        if Dice() == 1:
            r = r + "\n - Amphibious"

    if Type == "Dragon":
        if Dice() == 1:
            r = r + "\n - Blindsight \n\t 10 ft"

    if Type == "Dragon": 
        if Dice() == 1:
            r = r+ "\n- Keen Senses \n\t The Dragon has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell."
            
    if Type == "Dragon": 
        if Dice() == 1:
            r = r+ "\n- Limited Telepathy \n\t The Dragon can magically communicate simple ideas, emotions, and images telepathically with any creature within 100 feet of it that can understand a language. It can also communicate with any Dragon"
            
    if Type == "Dragon": 
        if Dice() == 1:
            r = r+ "\n- Magic Resistance \n\t The Dragon has advantage on saving throws against spells and other magical effects."           

    if Type == "Dragon": 
        if Dice() == 1:
            r = r+ "\n- Damage Immunities: Fire"           

    if Type == "Dragon": 
        if Dice() == 1:
            r = r+ "\n- Damage Immunities: Acid"           

    if Type == "Dragon": 
        if Dice(2) == 1:
            r = r+ "\n- Superior Invisibility \n\t  The Dragon magically turns invisible until its concentration ends (as if concentrating on a spell). Any equipment the Dragon wears or carries is invisible with it."

    if Type == "Fey": 
        if Dice(3) == 1:
            r = r+ "\n- Magic Resistance \n\t The Fae has advantage on saving throws against spells and other magical effects."

    if Type == "Fey": 
        if Dice(2) == 1:
            r = r+ "\n- Superior Invisibility \n\t  The Fae magically turns invisible until its concentration ends (as if concentrating on a spell). Any equipment the Fae wears or carries is invisible with it."

    if Type == "Giant":
        if Dice(2) == 1:
            r = r + "\n Darkvision: 60ft"
        
    if Type == "Beastfolk":
        if Dice()==1:
            r = r + "\n Rampage.\n\t When the beastfolk reduces a creature to 0 hit points with a melee attack on its turn, the beastfolk can take a bonus action to move up to half its speed and make a bite attack."
        

    if Type == "Gnome":
        r = r + "\n - Gnome Cunning \n\t The gnome has advantage on Intelligence, Wisdom, and Charisma saving throws against magic."

    if Type == "Gnome":
        r = r + "\n - Stone Camouflage \n\t The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."

        
        

    if Type == "Elf":
        r = r+ "\nFey Ancestry.\n\t The Elf has advantage on saving throws against being charmed, and magic can't put the Elf to sleep."
        
        if Dice(4) <= 3:
            r = r+ "\n Darkvision \n\t 60ft"
        else:
            r = r+ "\n Darkvision \n\t 120ft"
            r = r+ "\nSunlight Sensitivity. \n\t While in sunlight, the Elf has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."


    if Type == "Aven(Birdfolk)" or Type == 7:
        r = r+ "\n- Fly \n\t 50ft"
        
    if Type == "Construct":
        r = r+ "\n- Damage Immunities: Poison"

    if Type == "Construct":
        r = r+ "\n- Condition Immunities: Charmed"

    if Type == "Construct":
        r = r+ "\n- Condition Immunities: Poisoned"

    if Type == "Construct":
        if Dice(2)==1:
            r = r+ "\n- Damage Immunities: psychic"
            
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n Condition Immunities: blinded \n"
            
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n Condition Immunities: deafened \n"
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n Condition Immunities: exhaustion \n"
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n Condition Immunities: frightened \n"
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n Condition Immunities:  petrified \n"
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n Condition Immunities: paralyzed \n"
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n Condition Immunities: charmed \n"

    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n- Axiomatic Mind. \n\t The Construct can't be compelled to act in a manner contrary to its nature or its instructions."

    if Type == "Construct":
        if Dice() == 1:
            r = r+"\n- Disintegration. \n\t If the Construct dies, its body disintegrates into dust, leaving behind its weapons and anything else it was carrying."
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n- False Apperance \n\t While the Construct remains motionless in rest, it is indistinguishable from a normal object"
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n- Dark Vision:\n\t 60 ft"
        elif Dice()==1:
            r = r+ "\n- blindsight:\n\t 60 ft"
        elif Dice()==1:
            r = r+ "\n- Truesight:\n\t 60 ft"
        elif Dice()==1:
            r = r+ "\n- Truesight:\n\t 120 ft"
            
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n- Telepathic Bond:\n\t While the Construct is on the same plane of existence as its master, it can magically convey what it senses to its master, and the two can communicate telepathically."
            
    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n- Antimagic Susceptibility:\n\t The Construct is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the Construct must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute."

        
    if Type == "Aberration":
        if Dice()==1: 
            r = r+"\nDamage Resistances:  \n\t bludgeoning, piercing, and slashing from nonmagical attacks"
    if Type == "Aberration":
        if Dice()==1: 
            r = r+"\nDamage Resistances:  \n\t acid"
    if Type == "Aberration":
        if Dice()==1: 
            r = r+"\nDamage Resistances:  \n\t cold"
    if Type == "Aberration":
        if Dice()==1: 
            r = r+"\nDamage Resistances:  \n\t lightning"
    if Type == "Aberration":
        if Dice(2)==1: 
            r = r+"\nDamage Resistances:  \n\t thunder"
    if Type == "Aberration":
        if Dice(2)==1: 
            r = r+ "\n- Blindsight: \n\t 60ft"
        else: 
            r = r+ "\n- Darkvision: \n\t 60ft"
    if Type == "Aberration":
        if Dice()==1: 
            r = r+ "\n- Telepathy: \n\t 60ft"
            if Dice(3)==1:
                r = r+ "\n-Advanced Telepathy: \n\t The Aberration can perceive the content of any telepathic communication used within 60 feet of it, and it can't be surprised by creatures with any form of telepathy."
            if Dice(3)==1:
                r = r+ "\n-Telepathic Shroud. \n\t The Aberration is immune to any effect that would sense its emotions or read its thoughts, as well as all divination spells."
    if Type == "Aberration":
        if Dice(2)==1: 
            r = r+ "\n- Detect Sentience: \n\t It can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by a mind blank spell."
            if Dice()==1: 
                r = r+ "\n- Devour Intellect: \n\t It targets one creature it can see within 10 feet of it that has a brain. The target must succeed on a DC [10+%DEX] Intelligence saving throw against this magic or take 11 (2d10) psychic damage. Also on a failure, roll 3d6: If the total equals or exceeds the target's Intelligence score, that score is reduced to 0. The target is stunned until it regains at least one point of Intelligence."
    if Type == "Aberration":
        if Dice(2)==1: 
            r = r+ "\n- Body Thief. \n\t The intellect devourer initiates an Intelligence contest with an incapacitated humanoid within 5 feet of it that isn't protected by protection from evil and good. If it wins the contest, the intellect devourer magically consumes the target's brain, teleports into the target's skull, and takes control of the target's body. While inside a creature, the intellect devourer has total cover against attacks and other effects originating outside its host. The intellect devourer retains its Intelligence, Wisdom, and Charisma scores, as well as its understanding of Deep Speech, its telepathy, and its traits. It otherwise adopts the target's statistics. It knows everything the creature knew, including spells and languages. \n\t If the host body dies, the intellect devourer must leave it. A protection from evil and good spell cast on the body drives the intellect devourer out. The intellect devourer is also forced out if the target regains its devoured brain by means of a wish. By spending 5 feet of its movement, the intellect devourer can voluntarily leave the body, teleporting to the nearest unoccupied space within 5 feet of it. The body then dies, unless its brain is restored within 1 round."
    if Type == "Aberration":
        if Dice() == 1:
            r = r+ "\n- Damage Vulnerabilities: \n\t psychic"

    if Type == "Aberration":
        if Dice() == 1:
            r = r+ "\n- Magic Resistance: \n\t The Aberration has advantage on saving throws against spells and other magical effects."
        
    if Type == "Aven(Birdfolk)":
        r = r+ "\n- Ambusher"
        r = r+ "\n- Mimicry \n\t The Raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."
        
    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n - Fly : 30ft."

    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n - Darkvision : 60ft."

    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n - False Appereance"

    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n - Death Burst: \t When the Elemental dies, it leaves behind a burst of elemental essence that fills a 5-foot-radius sphere centered on its space." 
        rdm = Dice(4)
        if rdm == 1:
            r = r + "The sphere is heavily obscured. Wind disperses the cloud, which otherwise lasts for 1 minute."
        if rdm == 2:
            r = r + "Each creature in range must succeed on a DC [10+%Cha] Constitution Saving Throw or be blinded for 1 minute."
        if rdm == 3:
            r = r + "Each creature in range must succeed on a DC [10+%Cha] Constitution Saving Throw or take 4 (1d8) slashing damage on a failed save, or half as much on a successful one."  
        if rdm == 4:
            r = r + "Each creature in range must succeed on a DC [10+%Con] Constitution Saving Throw or take 7 (2d6) fire damage on a failed save, or half as much on a successful one. Flammable objects that aren't being worn or carried in that area are ignited."  
        
    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n - Damage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks"

    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n - Ignited Illumination. \n\t As a bonus action, the Elemental can set itself ablaze or extinguish its flames. While ablaze, the Elemental sheds bright light in a 10-foot radius and dim light for an additional 10 feet."

    if Type == "Elemental":
        if Dice() == 1:
            r = r+  "\n- Heated Body \n\t A creature that touches the Elemental or hits it with a melee attack while within 5 feet of it takes 3 (1d6) fire damage"

    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n- Damage Immunities: fire" 
            
    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n- Damage Vulnerabilities: cold"
            
    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n- Damage Vulnerabilities: fire"
        
    if Type == "Fey":
        if Dice() == 1:
            r = r + "\n - Invisibility \n\t The Fey magically turns invisible until it attacks, or until its concentration ends (as if concentrating on a spell). Any equipment the Fey wears or carries is invisible with it."
            
    if Type == "Fey":
        if Dice() == 1:
            r = r + "\n -  Teleport (Recharge 4–6). \n\t The Fey magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the Fey can make one attack."

    if Type == "Goblin":
        if Dice()==1:
            r = r+ "\n- Nimble Scape \n\t The goblin can take the Disengage or Hide action as a bonus action on each of its turns."

    if Type == "Goblin":
        if Dice()==1:
            r = r+ "\n- Martial Advantage \n\t Once per turn, the Goblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the goblin that isn't incapacitated."

    if Type == "Goblin":
        if Dice()==1:
            r = r+ "\n- Brute \n\t A melee weapon deals one extra die of its damage when the Goblin hits with it (included in the attack)."

    if Type == "Goblin":
        if Dice()==1:
            r = r+ "\n- Surprise Attack \n\t If the Goblin surprises a creature and hits it with an attack during the first round of combat, the target takes an extra 7 (2d6) damage from the attack."
            
    if Type == "Goblin":
        if Dice()==1:
            r = r+ "\n- Redirect Attack (Reaction) \n\t When a creature the goblin can see targets it with an attack, the goblin chooses another goblin within 5 feet of it. The two goblins swap places, and the chosen goblin becomes the target instead."

    if Type == "Goblin":
        if Dice()==1:
            r = r+ "\n- Multiattack \n\t The goblin makes two Simple Attacks attacks. The second attack has disadvantage."
            
    if Type == "Lizardfolk":
        r = r+"\n- Hold Breath \n\t The lizardfolk can hold its breath for 15 minutes."

    if Type == "Lizardfolk":
        if Dice(2) == 1:
            r = r + "\n - Chameleon Skin \n\t The lizard has advantage on Dexterity (Stealth) checks made to hide."

    if Type == "Lizardfolk":
        if Dice(2) == 1:
            r = r + "\n -  Spider Climb. \n\t The lizard can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
            
    if Type == "Lizardfolk":
        if Dice() == 1:
            r = r + "\n - Stench.  \n\t Any creature other than a Lizardfolk that starts its turn within 5 feet of the Lizardfolk must succeed on a DC [10+%CON] Constitution saving throw or be poisoned until the start of the creature's next turn. On a successful saving throw, the creature is immune to the stench of all Lizardfolk for 1 hour."

    if Type == "Lizardfolk":
        if Dice() == 1:
            r = r + "\n - Sunlight Sensitivity.  \n\t While in sunlight, the lizardfolk has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
      
    if Type == "Fey": 
        if Dice() == 1:
            r = r+ "\n- Teleport"

    if Type == "Fey": 
        if Dice() == 1:
            r = r+ "\n- Speak with Beasts and Plants \n\t The Fey can communicate with beasts and plants as if they shared a language."

    if Type == "Fey": 
        if Dice() == 1:
            r = r+ "\n- Tree Stride \n\t Once on her turn, the Fey can use 10 feet of her movement to step magically into one living tree within her reach and emerge from a second living tree within 60 feet of the first tree, appearing in an unoccupied space within 5 feet of the second tree. Both trees must be large or bigger."
          
            
    if Type == "Fey": 
        if Dice() == 1:
            r = r+ "\n- Fey Charm \n\t The Fey targets one humanoid or beast that she can see within 30 feet of her. If the target can see the dryad, it must succeed on a DC [10+Cha] Wisdom saving throw or be magically charmed. The charmed creature regards the Fey as a trusted friend to be heeded and protected. Although the target isn't under the Fey's control, it takes the Fey's requests or actions in the most favorable way it can. Each time the Fey or its allies do anything harmful to the target, it can repeat the saving throw, ending the effect on itself on a success. Otherwise, the effect lasts 24 hours or until the Fey dies, is on a different plane of existence from the target, or ends the effect as a bonus action. If a target's saving throw is successful, the target is immune to the Fey's Fey Charm for the next 24 hours. The Fey can have no more than one humanoid and up to three beasts charmed at a time."

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Amorphous \n\t The ooze can move through a space as narrow as 1 inch wide without squeezing."

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Corrode Material: Any nonmagical weapon made of the material that hits the ooze corrodes. After dealing damage, the weapon takes a permanent and cumulative −1 penalty to damage rolls. If its penalty drops to −5, the weapon is destroyed. Nonmagical ammunition made of the material that hits the ooze is destroyed after dealing damage. The ooze can eat through 2-inch-thick, nonmagical material in 1 round. On a hit from the Ooze, if the target is wearing nonmagical armor of the material, its armor is partly corroded and takes a permanent and cumulative −1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10."
            if Dice() == 1:
                r = r+ "\n\t Wood"
            if Dice() == 1:
                r = r+ "\n\t Metal"
            if Dice() == 1:
                r = r+ "\n\t Meat & Leather"
            if Dice() == 1:
                r = r+ "\n\t Iron"
            if Dice() == 1:
                r = r+ "\n\t Gold"
            if Dice() == 1:
                r = r+ "\n\t Silver"


    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- False Appearance \n\t While the ooze remains motionless, it is indistinguishable from an oily pool or wet rock."
    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Engulf"
    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Gelatinous Cube"
    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Transparent"
    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Spider Climb"
    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Split(Yellow): Lightning or Slashing"

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Damage Resistance: Acid"

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Damage Resistance: Cold"

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Damage Resistance: Fire"

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Condition Immunities: Blinded"

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Condition Immunities: Charmed"

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Condition Immunities: Deafened"

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Condition Immunities: Exhaustion"

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Condition Immunities: Frightened"

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Condition Immunities: Prone"

    if Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Blindsight: 60 ft"




    if Type == "Undead":
        r = r + "\n Darkvision: 60ft"

    if Type == "Undead":
        if Dice(3) == 1:
            r = r + "\n Damage Immunities: poison"

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n Damage Vulnerabilities: bludgeoning"

    if Type == "Undead":
        if Dice(3) == 1:
            r = r + "\n Damage Vulnerabilities: Radiant"

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n Damage Resistances: Acid"

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n Damage Resistances: Cold"

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n Damage Resistances: Fire"

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n Damage Resistances: lightning"

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n Damage Resistances: thunder"

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n Damage Resistances: bludgeoning, piercing and slashing from nonmagical attacks"


    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n Condition Immunities: exhaustion"

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n Condition Immunities: poisoned"
            
    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n Condition Immunities: charmed"
            
    if Type == "Undead":
        if Dice(2) == 1:
            r = r + "\n - Undead Fortitude"
            
    if Type == "Undead":
        if Dice(2) == 1:
            r = r + "\n -Stench"

    if Type == "Undead":
        if Dice(2) == 1:
            r = r + "\n -Turn Defiance"

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n - Turn Immunity \n\t The Undead is immune to effects that turn undead."

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n - Sunlight Sensitivity  \n\t While in sunlight, the undead has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n - Undead Fortitude. \n\t If damage reduces the Undead to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the Undead drops to 1 hit point instead."

            

    if Type == "Hobgoblin" or Type == 24:
        r = r+"\n- Martial Advantage"
        
        
    if Type == "Orc":
        r = r+ "\n- Darkvision \n\t 60ft."
        
    if Type == "Orc":
        r = r+ "\n- Aggressive \n\t As a bonus action, the orc can move up to its speed toward a hostile creature that it can see."
        
    if Type == "Undead":
        r = r + "\n- Blood Frenzy"
    
    if Type == "Scout":
        r = r+ "\n- Keen Senses\n\t The Scout has advantage on Wisdom (Perception) checks that rely on senses."   
        
    if Type == "Plant": 
        r = r+ "\n- Damage Vulnerabilities: fire"
        
    if Type == "Plant": 
        if Dice(3) == 1:
            r = r+ "\n- False Appereance: \n\t While the plant remains motionless, it is indistinguishable from a normal plant."
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n- Entangling Plants"

    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Damage Immunities: poison"

    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Condition Immunities:  blinded"

    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Condition Immunities:  deafened"

    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Condition Immunities: charmed"
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Condition Immunities:  frightened"

    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Condition Immunities:   poisoned"

    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Condition Immunities:   prone"

    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Condition Immunities:   paralyzed"

        
    if Type == "Undead":
        if Dice(2) == 1:
            r = r+"\n- Damage Resistances: acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks"

    if Type == "Undead":
        if Dice(2) == 1:
            r = r+"\n- Damage Immunities: necrotic, poison "

    elif Type == "Undead":
        if Dice(12) == 1:
            r = r+"\n- Condition Immunities: charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious"

    if Type == "Undead":
        if Dice() == 1:
            r = r+"\n- Amorphous \n\t The Undead can move through a space as narrow as 1 inch wide without squeezing."
            
    if Type == "Undead":
        if Dice() == 1:
            r = r+"\n- Shadow Stealth \n\t While in dim light or darkness, the Undead can take the Hide action as a bonus action. Its stealth bonus is also improved to +6."

    if Type == "Undead":
        if Dice() == 1:
            r = r+"\n- Sunlight Weakness \n\t While in sunlight, the shadow has disadvantage on attack rolls, ability checks, and saving throws."
            
    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n- Incorporeal Movement"
    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n- Sunlight Sensitivity"
    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n- Life Drain"

    if Type == "Undead":
        if Dice(2) == 1:
            r = r + "\n- Invisibility \n\t The Undead magically turns invisible until it attacks, or until its concentration ends (as if concentrating on a spell). Any equipment the undead wears or carries is invisible with it."

    if Type == "Undead":
        if Dice(2) == 1:
            r = r + "\n- Telekinetic Thrust"

    if Type == "Bandit":
        r = r+ "\n- Pack Tactics"
        


    if Type == "Dwarf":
        r = r + "\n- Damage Resistance: Poison"

    if Type == "Dwarf":
        if Dice() == 1:
            r = r + "\n- Darkvision 120ft"
        else:
            r = r + "\n- Darkvision 60ft"

    if Type == "Dwarf":
        if Dice() == 1:
            r = r + "\n- Duergar Resilience. \n\t The Dwarf has advantage on saving throws against poison, spells, and illusions, as well as to resist being charmed or paralyzed."
            r = r + "\n- Sunlight Sensitivity \n\t While in sunlight, the Dwarf has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
            

    elif Type == 32:
        r = r+ "\n- Luring Song"
    
    elif Type == "Cultist" or Type == 33:
        if Dice(2)==1:
            r = r+ "\n Dark Devotion.\n\t The cultist has advantage on saving throws against being charmed or frightened."
        
        
    if Type == "Fiend":
        if Dice(3)==1:
            r = r + "\n- Damage Resistances cold"
        if Dice(3)==1:
            r = r + "\n- Damage Resistances: fire"
        if Dice(3)==1:
            r = r + "\n- Damage Resistances: lightning"
        if Dice(3)==1:
            r = r + "\n- Damage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons" 

    if Type == "Fiend":
        if Dice(3)==1:
            r = r + "\n- Damage Immunities: poison"
        if Dice(3)==1:
            r = r + "\n- Damage Immunities: fire"

    if Type == "Fiend":
        if Dice(3)==1:
            r = r + "\nCondition Immunities: charmed"
        if Dice(3)==1:
            r = r + "\nCondition Immunities: frightened"
        if Dice(3)==1:
            r = r + "\nCondition Immunities: poisoned"
            
    if Type == "Fiend":
        if Dice(2)==1:
            r = r + "\n Darkvision \n\t 60 ft."
        else: 
            if Dice(2)==1:
                r = r + "\n Darkvision \n\t 120 ft."
        if Dice(2)==1:
            r = r + "\n Devil's Sight. \n\t Magical darkness doesn't impede the Fiend's darkvision."

    if Type == "Fiend":
        if Dice()==1:
            r += "\n Speed 20"
            r += "\n Fly 40"
        else:
            r += "\n Speed: 30 ft."
            
    if Type == "Fiend":
        if Dice()==1:
            r = r +"\n- Magic Resistance \n\t The fiend has advantage on saving throws against spells and other magical effects."
            
    if Type == "Fiend":
        if Dice() == 1:
            r = r + "\n- Shapechanger \n\t The fiend can use its action to polymorph into a beast form that resembles a rat (speed 20 ft.), a raven (20 ft., fly 60 ft.), or a spider (20 ft., climb 20 ft.), or back into its true form. Its statistics are the same in each form, except for the speed changes noted. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
        elif Dice() == 1:
            r = r + "\n- Shapechanger \n\t The fiend can use its action to polymorph into a beast form that resembles a bat (speed 10 feet fly 40 ft.), a centipede (40 ft., climb 40 ft.), or a toad (40 ft., swim 40 ft.), or back into its true form. Its statistics are the same in each form, except for the speed changes noted. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
            
    if Type == "Fiend":
        if Dice(2) == 1:
            r = r + "\n- Invisibility. \n\t The fiend magically turns invisible until it attacks, or until its concentration ends (as if concentrating on a spell). Any equipment the fiend wears or carries is invisible with it."

    if Type == "Fiend":
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
        if Dice(2) == 1:
            r = r + "\n- Cunning Action"
        if Dice(2) == 1:
            r = r + "\n- Sneak Attack (1/Turn)."
        
    elif Type == "Berserker" or Type == 37:
        r = r + "\n- Multiattack"
        r = r + "\n- Reckless"
        
    elif Type == 38:
        r = r+"\n    At will: animal friendship (snakes) \n 3/day each: poison spray, suggestion"

    elif Type == 40:
        r = r+ "\n    Cantrips (at will): sacred flame, thaumaturgy \n 1st level (3 slots): bane, shield of faith"
        
    elif Type == "Druid" or Type == 41:
        r = r + "\n- Cantrips (at will): druidcraft, produce flame, shillelagh \n 1st level (4 slots): entangle, longstrider, speak with animals, thunderwave \n2nd level (3 slots): animal messenger, barkskin\n"
        
    if Type == "Monstrosity":
        if Dice() == 1:
            r += "\n - Speed: 50 ft"
        elif Dice() == 1:
            r += "\n - Speed: 40 ft"
        else:
            r += "\n - Speed: 30 ft"

    if Type == "Monstrosity":
        if Dice() == 1:
            r += "\n - Fly: 30 ft"
        elif Dice() == 1:
            r += "\n - Fly: 40 ft"
        elif Dice() == 1:
            r += "\n - Fly: 60 ft"

    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n - Shapechanger"   
            
    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n-False Appearance \n\t While the Monstrosity remains motionless, it is indistinguishable from a natural element."  
            
    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n-Two-Headed. \n\t The monstrosity has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious."

    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n- Multiattack. \n\t The monstrosity makes two Simple attacks."

    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n- Stone Camouflage.\n\t The monstrosity has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.\n"  
            
    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n- Keen Sight.\n\t The monstrosity has advantage on Wisdom (Perception) checks that rely on sight.\n"  

    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n- Flight.\n\t 60 ft.\n"  

    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n- Darkvision.\n\t 60 ft.\n"  

    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n- Blindsight.\n\t 30 ft.\n"  

    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n- Spider Climb.\n\t The Monstrosity can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.\n"  

    if Type == "Priest":
        r = r + "\nDivine Eminence"


 
    if Type == "Shaman":
        if Dice(2)==1:
            r = r + "\n Change Shape: \n\t The Shaman magically polymorphs into a Beast, remaining in that form for up to 1 hour. It can revert to its true form as a bonus action. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
            
    elif Type == "Ranger" or Type == 48:
        r = r + Attack(4)
        r = "\n - Multiattack."
        
    elif Type == "Bandit" or Type == 49:
        r = r + "\n- Parry \n\t The Bandit adds 2 to its AC against one melee attack that would hit it. To do so, the bandit must see the attacker and be wielding a melee weapon."
        
    elif Type =="Guard" or Type == 50:
        r = r + "\n- Parry \n\t The Guard adds 2 to its AC against one melee attack that would hit it. To do so, the Guard must see the attacker and be wielding a melee weapon."
        
    if Type == "Kobold":    
        r = r + "\n- Darkvision \n\t 60ft."
        r = r + "\n- Pack Tactics \n\t The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated."
        r = r + "\n- Sunlight Sensitivity \n\t While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    if Type == "Kobold":    
        if Dice() == 1:
            r = r+ "\n Fly \t 30ft."

    if Type == "Noble":
        r = r + "\n- Parry \n\t The noble adds 2 to its AC against one melee attack that would hit it. To do so, the noble must see the attacker and be wielding a melee weapon."
    

    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Condition Immunities:  frightened"
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n-Distress Spores. \n\t When the plant takes damage, all other plants within 240 feet of it can sense its pain."  
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n-Sun Sickness. \n\t While in sunlight, the plant has disadvantage on ability checks, attack rolls, and saving throws. The plant dies if it spends more than 1 hour in direct sunlight."
            

    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n Condition Immunities\n\t blinded, deafened, frightened"

    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n Blindsight\n\t 30 ft"  
        elif Dice() == 1:
            r = r + "\n Blindsight\n\t 60 ft (Blind Beyond this radius)."  

    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n Darkvision\n\t 120 ft"        
   
    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n Death Burst\n\t The Plant explodes when it drops to 0 hit points. Each creature within 20 feet of it must succeed on a DC 15 Constitution saving throw or take 10 (3d6) poison damage and become infected with a disease on a failed save. Creatures immune to the poisoned condition are immune to this disease. Spores invade an infected creature's system, killing the creature in a number of hours equal to 1d12 + the creature's Constitution score, unless the disease is removed. In half that time, the creature becomes poisoned for the rest of the duration. After the creature dies, it sprouts 2d4 Tiny gas spores that grow to full size in 7 days."        


    if Type == "Warrior":
        r = r + "\n- Pack Tactics \n\t The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated."
        
    if Type == "Warrior":
        if Dice(2)==1:
            r= r + "\n- Multiattack \n\t The Warrior can attack an additional time on his turn."

    if Type == "":
        if Dice(2)==1:
            return Actions(Race())
        else:
            return Actions(Background())
    return r
    













def Legendary(Type=Dice(10)):
    r = ""
    if Type == "Human" or Type == 1:
        r = r+ "\n- Attack"
    else:
        if Dice(2)==1:
            r = r + "\n- Attack: \n\t It can do a simple attack to any creature" 
        if Dice(2)==1:
            r += "\n- Move: \n\t It can move half their movement"
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
    nm = Name(rc)
    if rc == "Giant": STR += Dice(12)
    
    print(Title())
    print(bg)
    print(rc)
    print(nm)
    print("\n")

    print("Lvl:", Lvl, "   HP:", Lvl*(Dice(12) + Dice(2)*Modifier(CON)))
    print("AC:", 10 + Modifier(DEX) + Modifier(Dice(Lvl+10)))
    print("\n\n\t"," STR:", STR,"\t", Modifier(STR),"\n\t",
        "DEX:", DEX," \t", Modifier(DEX),"\n\t"
        "CON:", CON," \t",  Modifier(CON),"\n\t"
        "INT:", INT," \t",  Modifier(INT),"\n\t"
        "WIS:", WIS," \t", Modifier(WIS),"\n\t"
        "CHA:", CHA," \t",  Modifier(CHA),"\n\t")
 
    print("Saving Throws:")
    if Dice(3) == 1: print("Str:+",Modifier(STR) + int(Lvl/5), end=" ")
    if Dice(3) == 1: print("Dex:+",Modifier(DEX)+ int(Lvl/5), end=" ")
    if Dice(3) == 1: print("Con:+",Modifier(CON)+ int(Lvl/5), end=" ")
    if Dice(3) == 1: print("Int:+",Modifier(INT)+ int(Lvl/5), end=" ")
    if Dice(3) == 1: print("Wis:+",Modifier(WIS)+ int(Lvl/5), end=" ")
    if Dice(3) == 1: print("Cha:+",Modifier(CHA)+ int(Lvl/5), end=" ")
    print("\n")
   
    print("Skills:")
    if Dice() <= Modifier(STR): print("\tAthletics:+",Proficiency(STR), end=" ")
    if Dice() <= Modifier(DEX): print("\tAcrobatics:+",Proficiency(DEX), end=" ")
    if Dice() <= Modifier(DEX): print("\tSleight of Hand:+",Proficiency(DEX), end=" ")
    if Dice() <= Modifier(DEX): print("\tStealth:+",Proficiency(DEX), end=" ")
    if Dice() <= Modifier(INT): print("\tArcana:+",Proficiency(INT), end=" ")
    if Dice() <= Modifier(INT): print("\tHistory:+",Proficiency(INT), end=" ")
    if Dice() <= Modifier(INT): print("\tInvestigation:+",Proficiency(INT), end=" ")
    if Dice() <= Modifier(INT): print("\tNature:+",Proficiency(INT), end=" ")
    if Dice() <= Modifier(INT): print("\tReligion:+",Proficiency(INT), end=" ")
    if Dice() <= Modifier(WIS): print("\tAnimal Handling:+",Proficiency(WIS), end=" ")
    if Dice() <= Modifier(WIS): print("\tInsight:+",Proficiency(WIS), end=" ")
    if Dice() <= Modifier(WIS): print("\tMedicine:+",Proficiency(WIS), end=" ")
    if Dice() <= Modifier(WIS): print("\tPerception:+",Proficiency(WIS), end=" ")
    if Dice() <= Modifier(WIS): print("\tSurvival:+",Proficiency(WIS), end=" ")
    if Dice() <= Modifier(CHA): print("\tDeception:+",Proficiency(CHA), end=" ")
    if Dice() <= Modifier(CHA): print("\tIntimidation:+",Proficiency(CHA), end=" ")
    if Dice() <= Modifier(CHA): print("\tPerformance:+",Proficiency(CHA), end=" ")
    if Dice() <= Modifier(CHA): print("\tPersuasion:+",Proficiency(CHA), end=" ")
    print("\n")
    
    print("Passive Perception:", 10 + Modifier(WIS) + Modifier(Lvl/2) )
    
    print("\n")
    print("Languages: ", Language(rc,bg))
    print("\n")
    print("COMBAT ACTIONS:")
    print("\tTo hit: +", Modifier(max(STR,DEX)+ Lvl/5))
    print("\n\t- Simple Attacks:")
    print (Attack("Melee"))
    print (Attack(Dice(4)))
    print("\n\t- Special Attack: {} Charges/Combat".format(Dice( 1 + int(Lvl/3))))
    print (SpecialAttack(Lvl, Modifier(random.choice([STR,DEX,CON,INT,WIS,CHA ]))))

    print("\n\n")
    print("SPELLCASTING:\n\t Spellsave DC:", 10+ Modifier(max(INT,WIS,CHA)))
    print("\t To hit: +", Modifier(max(INT,WIS,CHA)+ Lvl/5))
    print(Magic(Lvl,rc,bg))
    
    print("\n\n")
    print(Actions(bg))
    print(Actions(rc))
    print(Actions(""))
    print("\n")

    if Dice(Lvl) >= 15:
        print("LEGENDARY ACTIONS:")
        print(Legendary(bg))
        print(Legendary(rc))


NPC()
