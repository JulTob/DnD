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
        "The Climate",
        "The Chain",
        "The Champion",
        "The Chief",
        "The Circus",
        "The City",
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
        "The Emphasis",
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
        "The Fury",
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
        "The Ignoble",
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
        "The Love of",
        "The Master",
        "The Mad",
        "The Magic",
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
        "The Punk",
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
        "The Tomb",
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
        "The Wise",
        "The Wind" ,
        "The Winter",
        "The Wolf",
        "The Young",
        "The Zombie",
        "The",
        ""
        ]
    rank = [
        "Abomination",
        "Acolyte",
        "Alchemist",
        "Aprentice",
        "Arrow",
        "Archer",
        "Archfey",
        "Archmage",
        "Armour",
        "Ash",
        "Assassin",
        "Anarchist",
        "Anthropologist",
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
        "Burglar",
        "Cat",
        "Camel",
        "Captain",
        " Chemist",
        "Champion",
        "Charlatan",
        "Chimera",
        " Collector",
        "Collosus",
        "Commander",
        "Cultist",
        "Darkness",
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
        "Fanatic",
        " Fire", 
        "Fury",
        " Flutist",
        "Flame",
        "Freedomfighter",
        "Gargoyle",
        " Genius",
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
        "Hero",
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
        "Lion",
        "Light",
        "Lizard",
        " Lotus",
        " Lord",
        "Lover",
        "Man",
        "Machine",
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
        "Punk",
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
        "Spy",
        "Swashbuckler",
        "Swarm",
        "Sword",
        "Tiger",
        "Terror",
        "Trapper",
        "Trapecist",
        "Troll",
        "Thief",
        "Void",
        "Vampire",
        "Vulture",
        "Walker",
        "Warlock",
        "Warrior",
        "Watch",
        "Werewolf",
        "Wizard",
        "Witch",
        "Witchhunter",
        "Writter" ,
        "Willow",
        "Wolf",
        "Zombie",
        ""
        ] 
    
    title = random.choice(descriptor) + " " + random.choice(rank)
    return title
   
   
   


def Alignment():
    Alignments = [
        "Lawful Good",
        "Neutral Good",
        "Chaotic Good",
        "Lawful Neutral",
        "True Neutral",
        "Chaotic Neutral",
        "Lawful Evil",
        "Neutral Evil",
        "Chaotic Evil",
        "Unaligned",
        ""
        ]
    return random.choice(Alignments)


   
   
   
   
   
   
   
   
def Background():
    Backgrounds = [
        "Bandit",
        "Bard",
        "Berserker",
        "Charlatan",
        "Commoner",
        "Cultist",
        "Criminal",
        "Druid",
        "Expert",
        "Explorer",
        "Gladiator",
        "Guard",
        "Healer",
        "Hermit",
        "Hero",
        "Hunter",
        "Knight", 
        "Mage",
        "Monk",
        "Noble", 
        "Priest",
        "Pirate",
        "Ranger",
        "Scholar",
        "Shaman",
        "Soldier",
        "Spy",
        "Traveler",
        "Urchin",
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
        "Ooze",
        "Orc",
        "Plant",
        "Snakefolk",
        "Tiefling",
        "Undead",
        ""
        ]
    return random.choice(Races)












def AberrationName():
    Names = [
        "Intellect Devourer",
        "Illithid",
        "A Thing",
        "Croningberrian",
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
        "Insectfolk",
        "Jackalmen",
        "Kitsune",
        "Lycan", 
        "Merfolk",
        "Minotaur",
        "Sharkfolk",
        "Werewolf",
        ""]
    return random.choice(Names)

def CelestialName():
    Names = [
        "Angel",
        "Planetar",
        "Seraph",
        ""]
    return random.choice(Names)


def ConstructName():
    Names = [
        "Animated Armor",
        "Drone",
        "Homunculus",
        "Flying Sword",
        "Living Rug",
        "Scarecrow",
        ""]
    return random.choice(Names)

def DragonName():
    Names = [
        "Dragonborn",
        "Wyrmling",
        "Black", "Blue", "Green", "Purple", "Red", "White",
        "Bronce", "Silver", "Gold",
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

def OozeName():
    Names = [
        "Gelatinous Cube",
        "Ooze",
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
        "Crawling Limbs",
        "Ghoul",
        "Ghast",
        "Licht",
        "Skelleton",
        "Shadow",
        "Specter",
        "Vampire",
        "Zombie",
        ""]
    return random.choice(Names)
    
    
def Name(Type):
    if Type == "Aberration": return AberrationName()
    if Type == "Aven": return AvenName()
    if Type == "Beast": return BeastName()
    if Type == "Beastfolk": return BeastfolkName()
    if Type == "Celestial": return CelestialName()
    if Type == "Construct": return ConstructName()
    if Type == "Dragon": return DragonName()
    if Type == "Fey": return FeyName()
    if Type == "Fiend": return FiendName()
    if Type == "Giant": return GiantName()
    if Type == "Goblin": return GoblinName()
    if Type == "Monstrosity": return MonstrosityName()
    if Type == "Orc": return OrcName()
    if Type == "Ooze": return OozeName()
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
    return d1+d2+d3+d4 - min(d1,d2,d3,d4)
    
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
    if dmg == "Slashing": return random.choice(["Exhaustion","Incapacitated", "Poisoned", "Prone" ])
    elif dmg == "Piercing": return random.choice(["Blinded","Exhaustion", "Incapacitated", "Poisoned", "Grappled" ])
    elif dmg == "Bludgeoning": return random.choice(["Blinded","Deafened","Exhaustion", "Incapacitated", "Prone", "Stunned","Uncoscious", "Grappled", "Restrained" ])
    elif dmg == "Poison": return random.choice(["Blinded", "Charmed", "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Restrained", "Unconscious"])
    elif dmg == "Acid": return random.choice(["Blinded", "Exhaustion", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Restrained","Unconscious"])
    elif dmg == "Fire": return random.choice(["Blinded", "Charmed", "Incapacitated", "Paralyzed", "Stunned", "Unconscious"])
    elif dmg == "Cold": return random.choice(["Exhaustion", "Incapacitated", "Paralyzed", "Petrified", "Restrained", "Grappled"])
    elif dmg == "Radiant": return random.choice(["Blinded", "Charmed", "Deafened", "Frightened", "Incapacitated", "Paralyzed", "Prone", "Stunned", "Unconscious"])
    elif dmg == "Necrotic": return random.choice([ "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Lightning": return random.choice(["Blinded", "Charmed", "Deafened", "Exhaustion", "Frightened", "Grappled", "Incapacitated", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Force": return random.choice(["Blinded","Deafened", "Exhaustion", "Incapacitated", "Prone", "Stunned", "Unconscious", "Grappled" ])
    elif dmg == "Psychic": return random.choice(["Blinded", "Charmed", "Deafened", "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Thunder": return random.choice(["Blinded", "Deafened", "Exhaustion", "Incapacitated", "Paralyzed", "Prone", "Stunned"])
    else: return random.choice(ConditionsTypes)
    
def SavingThrow(dmg):
    if dmg == "Slashing": st = random.choice(["STR","DEX"])
    elif dmg == "Piercing": st = random.choice(["STR","DEX","CON" ])
    elif dmg == "Bludgeoning": st = random.choice(["STR","DEX","CON"])
    elif dmg == "Poison": st = "CON"
    elif dmg == "Acid": st = random.choice(["STR","DEX","CON" ])
    elif dmg == "Fire": st = random.choice(["STR","DEX","CON", "CHA"])
    elif dmg == "Cold": st = random.choice(["STR","DEX","CON" ])
    elif dmg == "Radiant": st = random.choice(["DEX","CON","WIS","CHA" ])
    elif dmg == "Necrotic": st = random.choice(["STR","CON","WIS","CHA" ])
    elif dmg == "Lightning": st = random.choice(["DEX","CON","WIS", "INT" ])
    elif dmg == "Force": st = random.choice(["STR","CON","CHA" ])
    elif dmg == "Psychic": st = random.choice(["INT","WIS","CHA" ])
    elif dmg == "Thunder": st = random.choice(["STR","DEX","CON" ])
    else: st = "DEX"
    return st

def Recovery(con):
    if con == "Unconscious": st = random.choice(["CON","INT","WIS","CHA" ])
    elif con == "Stunned": st = random.choice(["CON","INT","WIS","CHA" ])
    elif con == "Restrained": st = random.choice(["STR","DEX","CON"])
    elif con == "Poisoned": st = random.choice(["CON", "WIS"])
    elif con == "Prone": st = random.choice(["STR","DEX","CON"])
    elif con == "Petrified": st = random.choice(["STR", "CON","INT","WIS","CHA" ])
    elif con == "Paralyzed": st = random.choice(["STR", "CON","WIS","CHA" ]) 
    elif con == "Invisible": st = random.choice(["CON","INT","WIS","CHA" ])      
    elif con == "Incapacitated": st = random.choice(["STR","CON","WIS","CHA" ]) 
    elif con == "Grappled": st = random.choice(["STR","DEX"]) 
    elif con == "Blinded": st = random.choice(["CON","INT","WIS","CHA"]) 
    elif con == "Frightened": st = random.choice(["CON","INT","WIS","CHA"]) 
    elif con == "Exhaustion": st = random.choice(["STR","CON","CHA"]) 
    elif con == "Deafened": st = random.choice(["STR","CON","WIS"]) 
    elif con == "Charmed": st = random.choice(["CHA","WIS"]) 
    else: st = "CON"
    return st

def SpecialAttack(Lvl,Mod ):
    dmg = Damage()
    con = Condition(dmg)
    r = ""
    r += Attack(Dice(4)) + " +"
    r += "{}".format(Dice(Dice(1+int(Lvl/4))))
    r += random.choice(["d4 ","d6 ","d8 ", "d10 ", "d12 "])
    r += dmg
    r += " dmg" 
    r += " on a failed Saving Throw at DC "
    r += str((10 + Mod)) +" "
    r += SavingThrow(dmg) +  "."
    if Dice(10)+Dice(10)+Dice(10) <= Dice(Lvl):
        r += " The target is then affected by the " + con + " condition. "
        r += " The Condition may be countered with a succesful " + str((10 + Mod)) + " "+ Recovery(con) + " Saving Throw at the beggining of the target's turn."
    return r






























def Language(race = Race(), background = Background()):
    if race == "": race = Race()
    if background == "": background = Background()
    l = ""
    if race == "Human": 
        l += "Common. "
        if Dice()==1: l += "Dwarvish. "
        if Dice()==1: l += "Elvish. "
        if Dice()==1: l += "Giant. "
        if Dice()==1: l += "Gnomish. "
        if Dice()==1: l += "Goblin. "
        if Dice()==1: l += "Halfling. "
        if Dice()==1: l += "Orc. "
        if Dice(20)==1: l += "Abyssal. "
        if Dice(20)==1: l += "Celestial. "
        if Dice(20)==1: l += "Draconic. "
        if Dice(20)==1: l += "Deep Speech. "
        if Dice(20)==1: l += "Infernal. "
        if Dice(20)==1: l += "Primordial. "
        if Dice(20)==1: l += "Sylvan. "
        if Dice(20)==1: l += "Undercommon. "
    if race == "Aberration": 
        l += "Deep Speech. "
        if Dice()==1: l += "Undercommon. "
        if Dice(20)==1: l += "Telepathy. "
    if race == "Aven": 
        l += "Common. "
        if Dice()==1: l += "Primordial. "
    if race == "Beast":
        if Dice()==1: l += "Understands Common. "
        if Dice()==1: l += "Beastly Speech. "
        if Dice()==1: l += "Sylvan. "
    if race == "Beastfolk": 
        l += "Common. Beastly Speech. "
        if Dice()==1: l += "Sylvan. "
        if Dice()==1: l += "Undercommon. "
        if Dice()==1: l += "Elvish. "
    if race == "Celestial": l += "Celestial. Common."
    if race == "Construct": 
        l += "Understands the languages of its creator. "
        if Dice(100)==1: l += "All Languages. "
    if race == "Dragon":
        l += "Draconic. "
        if Dice(3)==1: l += "Common. "
        if Dice()==1: l += "Sylvan. "
    if race == "Dwarf":
        l += "Dwarvish. "
        if Dice(3)==1: l += "Common. "
        if Dice(3)==1: l += "Undercommon. "
    if race == "Elf":
        l += "Elvish. "
        if Dice(3)==1: l += "Common. "
        if Dice(3)==1: l += "Sylvan. "
    if race == "Elemental" or race == "Genasi":
        l += "Primordial"
        if Dice()==1: l += "Common. "
        if Dice(4)==1: l += "Ignan. "
        if Dice(4)==1: l += "Terran. "
    if race == "Fey":
        l += "Sylvan. "
        if Dice(3) == 1: l += "Common. "
        if Dice(3) == 1: l += "Elvish. "
    if race == "Fiend" or "Tiefling":
        l += "Common. "
        if Dice(2) == 1: l += "Infernal. "
        if Dice(2) == 1: l += "Abyssal. "
    if race == "Giant": l += "Common. Giant. "
    if race == "Gnome":
        l += "Gnomish"
        if Dice(3) == 1: l += "Common. "
        if Dice(3) == 1: l += "Elvish. "
        if Dice(3) == 1: l += "Dwarvish. "
        if Dice(3) == 1: l += "Giant. "
        if Dice(3) == 1: l += "Halfling. "
        if Dice() == 1: l += "Sylvan. "
    if race == "Goblin":
        l += "Goblin. "
        if Dice(2)==1: l += "Common. "
    if race == "Hag": l += "Common. Sylvan. "
    if race == "Halfling": l += "Common. Halfling. "
    if race == "Kobold":
        l += "Draconic. "
        if Dice(3)==1: l += "Common. "
    if race == "Lizardfolk":
        l += "Draconic. "
        if Dice(2)==1: l += "Common. "
    if race == "Monstrosity":
        if Dice(2)==1: l += "Common. "
        if Dice(2)==1: l += "Undercommon. "
    if race == "Ooze": l += "Telepathy. "
    if race == "Orc":
        l += "Orc. "
        if Dice(2)==1: l += "Common. "
    if race == "Plant":
        if Dice(3)==1: l += "Common. "
        if Dice(3)==1: l += "Sylvan. "
    if race == "Snakefolk":
        l += "Draconic. "
        if Dice(3)==1: l += "Abyssal. "
        if Dice(3)==1: l += "Common. "
    if race == "Undead":
        l += "Understands languages it knew in life. "
        if Dice(2)==1: l += "Common. "
        if Dice(8)==1: l += "Infernal. "
        
    if background ==  "Druid": l += "Druidic. " + random.choice(["Sylvan. ", "Primordial. ", "Draconic. ", "Elvish. "])
    if background ==  "Bandit": l += "Common. Thieve's Cant. "
    if background ==  "Bard": l += "Common. " + random.choice(["Dwarvish. ", "Elvish. ", "Gnomish. ", "Halfling. ", "Sylvan. "])
    if background ==  "Berserker": l += "Common." + random.choice(["Dwarvish. ", "Giant. ", "Orc. ", "Undercommon. "])
    if background ==  "Charlatan": l += "Common." + random.choice(["Elvish. ", "Gnomish. ", "Halfling"])
    if background ==  "Commoner": l += random.choice(["Elvish. ", "Gnomish. ", "Common. ", "Dwarvish. ", "Giant. ", "Goblin. ", "Halfling. ", "Orc. "])
    if background ==  "Cultist": l += random.choice(["Abyssal. ", "Celestial. ", "Draconic. ", "Deep Speech. ", "Infernal. ", "Primordial. ", "Sylvan. ", "Undercommon. "])
    if background ==  "Criminal": l += "Thieve's Cant. Common. " + random.choice(["Dwarvish. ", "Giant. ", "Goblin. ", "Orc. ", "Undercommon. "])
    if background ==  "Expert": l += random.choice(["Dwarvish. ", "Elvish. ", "Giant. ", "Gnomish. ", "Celestial. "])
    if background ==  "Explorer": l += random.choice(["Elvish. ", "Giant. ", "Goblin. ", "Orc. "]) + random.choice(["Draconic. ", "Primordial. ", "Sylvan. "])
    if background ==  "Gladiator": l += "Common. "
    if background ==  "Guard": l += "Common. "
    if background ==  "Healer": l += random.choice(["Celestial. ", "Primordial. ", "Sylvan. "])
    if background == "Hermit": l += ""
    if background == "Hero": l += "Common. " + random.choice(["Celestial. ", "Draconic. ", "Sylvan. "])
    if background == "Hunter": l += "Sylvan. "
    if background == "Knight": l += "Common. " + random.choice(["Celestial. ", "Draconic. ", "Sylvan. "])
    if background == "Mage": l += "Common. " + random.choice(["Dwarvish. ", "Elvish. ", "Giant. ", "Gnomish. "])
    if background == "Monk": l += "Common. " + random.choice(["Celestial. ", "Draconic. ", "Primordial. "])
    if background == "Noble": l += "Common. " + random.choice(["Dwarvish. ", "Elvish. "])
    if background == "Priest": l += "Common. " + "Celestial. "
    if background == "Priest": l += "Common. " + random.choice(["Dwarvish. ", "Elvish. "])
    if background == "Pirate": l += "Common. Thieves' Cant. "
    if background ==  "Ranger": l += random.choice(["Elvish. ", "Giant. ", "Goblin. ", "Orc. "]) + random.choice(["Draconic. ", "Primordial. ", "Sylvan. "])
    if background == "Scholar": l += random.choice(["Abyssal. ", "Celestial. ", "Draconic. ", "Deep Speech. ", "Infernal. ", "Primordial. ", "Sylvan. "])
    if background == "Shaman": l += "Sylvan" + random.choice(["Elvish. ", "Giant. ", "Goblin. ", "Orc. ", "Primordial. "]) 
    if background == "Soldier": l += "Common. "
    if background == "Spy": l += "Common. Thieves' Cant. "
    if background == "Traveler": l += "Common." + random.choice(["Elvish. ", "Gnomish. ", "Halfling", "Dwarvish", "Giant. ", "Goblin. ", "Orc. "])
    if background == "Urchin": l += "Common. "
    if background == "Veteran": l += "Common. " + random.choice(["Elvish. ", "Gnomish. ", "Halfling", "Dwarvish", "Giant. ", "Goblin. ", "Orc. "])
    if background == "Warrior": l += "Common. " + random.choice(["Elvish. ", "Gnomish. ", "Halfling", "Dwarvish", "Giant. ", "Goblin. ", "Orc. "])
    if background == "Warlock": l += random.choice(["Abyssal. ", "Celestial. ", "Draconic", "Deep Speech. ", "Infernal. ", "Primordial. ", "Sylvan. "])
    if background == "Witch": l += "Common. " + random.choice(["Goblin. ", "Gnomish. ", "Sylvan"])
    return l



def Magic(Lvl, race = Race(), background = Background()):
    if race == "": race = Race()
    if background == "": background = Background()

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
        if background== "Fiend" and Dice()==1: one += "\nFetid Cloud (1/Day).\n\t A 10-foot radius of disgusting sulfuric gas extends out from the Fiend. The gas spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a strong wind disperses it. Any creature that starts its turn in that area must succeed on a DC 11 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target can take either an action or a bonus action on its turn, not both, and can't take reactions."
        if background == "Priest" and Dice(2) == 1: cantrip +=  "\n- Light. "
        if background == "Priest" and Dice(2) == 1: cantrip +=  "\n- Sacred flame. "
        if background == "Priest" and Dice(2) == 1: cantrip +=  "\n- Thaumaturgy"
        if background == "Priest" and Dice(2) == 1:
            first += "\n- Bless"
            slots1 += Dice(3)
        if background == "Priest" and Dice(2) == 1:
            first += "\n- Cure wounds"  
            slots1 += Dice(3)
        if background == "Priest" and Dice(2) == 1:
            first += "\n- Sanctuary"   
            slots1 += Dice(3)
        if background == "Cultist" and Dice(3) == 1: cantrip +=  "\n- Light."
        if background == "Cultist" and Dice(3) == 1: cantrip += "\n- Sacred flame"
        if background == "Cultist" and Dice(3) == 1: cantrip += "\n- Thaumaturgy" 
        if background == "Cultist" and Dice() == 1:
            first += "\n- Command"
            slots1 += Dice(4)
        if background == "Cultist" and Dice() == 1:
            first += "\n- Inflict wounds"
            slots1 += Dice(4)
        if background == "Cultist" and Dice() == 1:
            first += "\n- Shield of faith"
            slots1 += Dice(4)
        if background == "Cultist" and Dice(8) == 1:
            second += "\n hold person" 
            slots2 += Dice(3)
        if background == "Cultist" and Dice(8) == 1:
            second += "\n spiritual weapon"
            slots2 += Dice(3)
        if background == "Druid": cantrip += "\n- Druidcraft."
        if background == "Druid" and Dice() == 1: cantrip += "\n- Produce Flame."
        if background == "Druid" and Dice() == 1: cantrip += "\n- Shillelag."
        if background == "Druid" and Dice() == 1:
            first += "\n Entangle"
            slots1 += Dice(4)
        if background == "Druid" and Dice() == 1:
            first += "\n Longstrider"
            slots1 += Dice(4)
        if background == "Druid" and Dice() == 1:
            first += "\n Thunderwave"
            slots1 += Dice(4)
        if background == "Druid" and Dice() == 1:
            second += "\n Animal Messenger"
            slots2 += Dice(3)
        if background == "Druid"and Dice() == 1:
            second += "\n Barkskin"
            slots2 += Dice(3)
        if background == "Druid" and Dice() == 1:
            first += "\n Speak With Animals"
            slots1 += Dice(4)
        if background=="Healer" and Dice(2) == 1: cantrip +=  "\n- Guidance" 
        if background=="Healer" and Dice(2) == 1: cantrip +=  "\n- Sacred flame"
        if background=="Healer" and Dice(2) == 1:
            first +=  "\n- Cure wounds"
            slots1 += Dice(2)
        if background == "Mage" and Dice(2) == 1: cantrip +=  "\n - Firebolt" 
        if background == "Mage" and Dice(2) == 1: cantrip +=  "\n - Light" 
        if background == "Mage" and Dice(2) == 1:
            first +=  "\n - Sleep"
            slots1 += Dice(2)
        if background == "Priest" and Dice() == 1: cantrip += "\n- Guidance"
        if background == "Priest" and Dice() == 1: cantrip += "\n- Light"
        if background == "Priest" and Dice() == 1: cantrip += "\n- Sacred Flame"
        if background == "Priest" and Dice() == 1: cantrip += "\n- Thaumaturgy"
        if background == "Priest" and Dice() == 1:
            first += "\n- Cure wounds"
            slots1 += Dice(4)
        if background == "Priest" and Dice() == 1:
            first += "\n- Guiding bolt"
            slots1 += Dice(4)
        if background == "Priest" and Dice() == 1:
            first += "\n- Sanctuary" 
            slots1 += Dice(4)
        if background == "Priest" and Dice() == 1:
            second += "\n- Lesser restoration"
            slots2 += Dice(3)
        if background == "Priest" and Dice() == 1:
            second += "\n- Spiritual weapon"
            slots2 += Dice(3)
        if background == "Priest" and Dice() == 1:
            third += "\n- Dispel magic"
            slots3 += Dice(2)
        if background == "Priest" and Dice() == 1:
            third += "\n- Spirit guardians"
            slots3 += Dice(2)
        if background == "Shaman" and Dice() == 1: cantrip +=  "\n- druidcraft" 
        if background == "Shaman" and Dice() == 1: cantrip +=  "\n-  Produce flame" 
        if background == "Shaman" and Dice() == 1: cantrip +=  "\n-  thorn whip" 
        if background == "Shaman" and Dice() == 1:
            first +=  "\n-  entangle"
            slots1 += Dice(4)
        if background == "Shaman" and Dice() == 1:
            first +=  "\n-  fog cloud"
            slots1 += Dice(4)
        if background == "Shaman" and Dice(2) == 1:
            second +=  "\n-  heat metal"
            slots2 += Dice(3)
        if background == "Shaman" and Dice(2) == 1:
            second +=  "\n-  spike growth"
            slots2 += Dice(3)
        if background == "Shaman" and Dice(2) == 1:
            third +=  "\n-  conjure animals"
            slots3 += Dice(2)
        if background == "Shaman" and Dice(2) == 1:
            third +=  "\n-  plant growth"
            slots3 += Dice(2)
        if race == "Aberration" and Dice() == 1: one += "\n- Stench Spray (1/Day). \n\t Each creature in a 15-foot cone originating from the Aberration must succeed on a DC 10 Dexterity saving throw or be coated in a foul-smelling liquid. A coated creature exudes a horrible stench for 1d4 hours. The coated creature is poisoned as long as the stench lasts, and other creatures are poisoned while with in 5 feet of the coated creature. A creature can remove the stench on itself by using a short rest to bathe in water, alcohol, or vinegar."
        if race == "Aven" and Dice(8) == 1: cantrip +=  "\n- Summon Air Elemental. \n\t Five Aven within 30 feet of each other can magically summon an air elemental. Each of the five must use its action and movement on three consecutive turns to perform an aerial dance and must maintain concentration while doing so (as if concentrating on a spell). When all five have finished their third turn of the dance, the elemental appears in an unoccupied space within 60 feet of them. It is friendly toward them and obeys their spoken commands. It remains for 1 hour, until it or all its summoners die, or until any of its summoners dismisses it as a bonus action. A summoner can't perform the dance again until it finishes a short rest. When the elemental returns to the Elemental Plane of Air, any Aven within 5 feet of it can return with it."
        if race == "Beastfolk" and Dice(10) == 1: cantrip +=  "\n- Sleep Gaze. \n\t The Beastfolk gazes at one creature it can see within 30 feet of it. The target must make a DC [10+%Wis] Wisdom saving throw. On a failed save, the target succumbs to a magical slumber, falling unconscious for 10 minutes or until someone uses an action to shake the target awake. A creature that successfully saves against the effect is immune to this Beastfolk's gaze for the next 24 hours. Undead and creatures immune to being charmed aren't affected by it."
        if race == "Beastfolk" and Dice() == 1: cantrip +=  "\n- Sacred Flame."
        if race == "Beastfolk" and Dice() == 1: cantrip +=  "\n- Mage Hand (invisible)."
        if race == "Beastfolk" and Dice() == 1: cantrip +=  "\n- Thaumaturgy."
        if race == "Beastfolk" and Dice() == 1: one +=  "\n- Invisibility (self only)."
        if race == "Beastfolk" and Dice() == 1: two +=  "\n- Blur."
        if race == "Beastfolk" and Dice() == 1: two +=  "\n- Magic Weapon."
        if race == "Beastfolk" and Dice() == 1:
            first +=  "\n- Bane"
            slots1 += Dice(3)
        if race == "Beastfolk" and Dice() == 1:
            first +=  "\n- Shield Of Faith"
            slots1 += Dice(3)
        if race == "Celestial" and Dice(2) == 1: cantrip +=  "\n- Light" 
        if race == "Celestial" and Dice(2) == 1: cantrip +=  "\n- Sacred flame" 
        if race == "Celestial" and Dice(2) == 1: cantrip +=  "\n- Thaumaturgy" 
        if race == "Celestial" and Dice(2) == 1:
            first +=  "\n- Bless" 
            slots1 += Dice(3)
        if race == "Celestial" and Dice(2) == 1:
            first +=  "\n- Cure wounds" 
            slots1 += Dice(3)
        if race == "Celestial" and Dice(2) == 1:
            first +=  "\n- Sanctuary"
            slots1 += Dice(3)
        if race == "Dragon" and Dice(3)==1: 
            cantrip += "\n- Breath Weapons " + "(Recharge 5-6)."
            if Dice(8) == 1: cantrip += "\n  - Fire Breath \n\t The dragon exhales fire in a 20-foot line that is 5 feet wide. Each creature in that line must make a DC [10+%Con] Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one."
            elif Dice(8) == 2: cantrip += "\n  - Sleep Breath \n\t The dragon exhales sleep gas in a 15-foot cone. Each creature in that area must succeed on a DC [10+%Con] Constitution saving throw or fall unconscious for 1 minute. This effect ends for a creature if the creature takes damage or someone uses an action to wake it."
            elif Dice(8) == 3: cantrip += "\n  - Acid Breath \n\t . The dragon exhales acid in a 20-foot line that is 5 feet wide. Each creature in that line must make a DC [10+%Con] Dexterity saving throw, taking 18 (4d8) acid damage on a failed save, or half as much damage on a successful one"
            elif Dice(8) == 4: cantrip += "\n  - Slowing Breath \n\t The dragon exhales gas in a 15-foot cone. Each creature in that area must succeed on a DC [10+%Con] Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the start of each of its turns, ending the effect on itself with a successful save."
            elif Dice(8) == 5: cantrip += "\n  - Euphoria Breath \n\t The dragon exhales a puff of euphoria gas at one creature within 5 feet of it. The target must succeed on a DC [10+%Con] Wisdom saving throw, or for 1 minute, the target can't take reactions and must roll a d6 at the start of each of its turns to determine its behavior during the turn: \n\t\t 1–4. The target takes no action or bonus action and uses all of its movement to move in a random direction. \n\t\t 5–6. The target doesn't move, and the only thing it can do on its turn is make a DC [10+%Con] Wisdom saving throw, ending the effect on itself on a success."
            elif Dice(8) == 6: cantrip += "\n  - Repulsion Breath \n\t The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC 12 Strength saving throw. On a failed save, the creature is pushed 30 feet away from the dragon."
            elif Dice(8) == 7: cantrip += "\n  - Poison Breath"
            elif Dice(8) == 8: cantrip += "\n  - Lightning Breath \n\t The dragon exhales lightning in a 40-foot line that is 5 feet wide. Each creature in that line must make a DC [10+%Con] Dexterity saving throw, taking 16 (3d10) lightning damage on a failed save, or half as much damage on a successful one."
 
        if race == "Dragon" and Dice(12) == 1: cantrip += "\n- Change Shape \n\t The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice).In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."
        if race == "Dragon" and Dice() == 1:  cantrip += "\n- Color Spray"
        if race == "Dragon" and Dice() == 1: cantrip += "\n- Dancing Lights"
        if race == "Dragon" and Dice() == 1: cantrip += "\n- Mage Hand"
        if race == "Dragon" and Dice() == 1: one += "\n- Minor Illusion"
        if race == "Dragon" and Dice(8) == 1: one += "\n- Major Image"
        if race == "Dragon" and Dice(8) == 1: one += "\n- Mirror Image"
        if race == "Dragon" and Dice(8) == 1: one += "\n- Polymorph"
        if race == "Dragon" and Dice(8) == 1: one += "\n- Suggestion"
        if race == "Dwarf" and Dice() == 1: cantrip += "\n- Enlarge (Recharges after a Short or Long Rest). \n\t For 1 minute, the Dwarf magically increases in size, along with anything it is wearing or carrying. While enlarged, the Dwarf is Large, doubles its damage dice on Strength-based weapon attacks (included in the attacks), and makes Strength checks and Strength saving throws with advantage. If the Dwarf lacks the room to become Large, it attains the maximum size possible in the space available."
        if race == "Dwarf" and Dice() == 1: cantrip += "\n- Invisibility (Recharges after a Short or Long Rest). \n\t The dwarf magically turns invisible until it attacks, casts a spell, or until its concentration is broken, up to 1 hour (as if concentrating on a spell). Any equipment the Dwarf wears or carries is invisible with it."
        if race == "Elemental" and Dice() == 1: cantrip += "\n- Dancing lights"
        if race == "Elemental" and Dice() == 1: one += "\n- blur"
        if race == "Elemental" and Dice() == 1: one += "\n- Sleep"
        if race == "Elemental" and Dice() == 1: cantrip += "\n Cinder Breath \t (Recharge 6). The Elemental exhales a 15-foot cone of smoldering ash. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw or be blinded until the end of the Elemental's next turn."
        if race == "Elemental" and Dice(7) == 1: cantrip += "\n Blinding Breath \t (Recharge 6). The Elemental exhales a 15-foot cone of blinding dust. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw or be blinded for one minute."
        if race == "Elemental" and Dice(7) == 1: cantrip += "\n Steam Breath \t (Recharge 6). The Elemental exhales a 15-foot cone of scalding steam. Each creature in that area must succeed on a DC [10+%Cha] Dexterity saving throw, taking 4 (1d8) fire damage on a failed save, or half as much damage on a successful one."
        if race == "Elemental" and Dice(8) == 1: cantrip += "\n - Frost Breath \n\t (Recharge 6). The Elemental exhales a 15-foot cone of cold air. Each creature in that area must succeed on a DC [10+%Con] Dexterity saving throw, taking 5 (2d4) cold damage on a failed save, or half as much damage on a successful one."
        if race == "Elemental" and Dice() == 1: cantrip += "\n - Fire Breath \t (Recharge 6). The Elemental exhales a 15-foot cone of cold air. Each creature in that area must succeed on a DC [10+%Con] Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one."
        if race == "Elemental" and Dice(3) == 1: one += "\n - Summon Mephits (1/Day) \n\t The Elemental has a 25 percent chance of summoning 1d4 mephits. A summoned mephit appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other mephits. It remains for 1 minute, until it or its summoner dies, or until its summoner dismisses it as an action."
        if race == "Elemental" and Dice() == 1: one += "\n Innate Spellcasting (1/Day) \n\t The Elemental can innately cast fog cloud, requiring no material components."
        if race == "Elemental" and Dice() == 1: one += "\n Innate Spellcasting (1/Day) \n\t The Elemental can innately cast heat metal, requiring no material components."
        if race == "Elf" and Dice() == 1: cantrip += "\n- Dancing lights"
        if race == "Elf" and Dice() == 1: one += "\n- Darkness"
        if race == "Elf" and Dice() == 1: one += "\n- Faerie fire"
        if race == "Fey" and Dice() == 1: cantrip += "\n Teleport (Recharge 4–6). \n\t The Fey magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the Fey can make one bite attack."
        if race == "Fey" and Dice() == 1: cantrip +=  "\n- Druidcraft"
        if race == "Fey" and Dice(3) == 1: three += "\n- Entangle" 
        if race == "Fey" and Dice(3) == 1: three += "\n- Goodberry"
        if race == "Fey" and Dice() == 1: one += "\n- Barkskin"
        if race == "Fey" and Dice() == 1: one += "\n- Pass without trace"
        if race == "Fey" and Dice() == 1: one += "\n- Shillelagh"
        if race == "Fey" and Dice() == 1: cantrip += "\n Heart Sight. \n\t The Fey touches a creature and magically knows the creature's current emotional state. If the target fails a DC [10+%Cha] Charisma saving throw, the Fey also knows the creature's alignment. Celestials, fiends, and undead automatically fail the saving throw."
        if race == "Fey" and Dice() == 1: cantrip += "\n Invisibility. \n\t The Fey  magically turns invisible until it attacks or casts a spell, or until its concentration ends (as if concentrating on a spell). Any equipment the Fey wears or carries is invisible with it."
        if race == "Fey" and Dice(3) == 1: cantrip += "\n- Druidcraft"
        if race == "Fey" and Dice() == 1: one += "\n- Confusion"
        if race == "Fey" and Dice() == 1: one += "\n- Dancing lights"
        if race == "Fey" and Dice() == 1: one += "\n- Detect evil and good"   
        if race == "Fey" and Dice() == 1: one += "\n- Detect thoughts"   
        if race == "Fey" and Dice() == 1: one += "\n- Dispel magic"   
        if race == "Fey" and Dice() == 1: one += "\n- Entangle"   
        if race == "Fey" and Dice() == 1: one += "\n - Fly"   
        if race == "Fey" and Dice() == 1: one += "\n - phantasmal force"   
        if race == "Fey" and Dice() == 1: one += "\n polymorph"   
        if race == "Fey" and Dice() == 1: one += "\n- Sleep"   
        if race == "Fey" and Dice() == 1: one += "\n Charming Melody [DC 10+%Cha Wisdom saving throw]\n\t The creature is charmed by the Fey for 1 minute. If the Fey or any of its companions harms the creature, the effect on it ends immediately."   
        if race == "Fey" and Dice() == 1: one += "\n - Frightening Strain [DC 10+%Cha Wisdom saving throw] \n\t The creature is charmed by the Fey for 1 minute. If the Fey or any of its companions harms the creature, the effect on it ends immediately."   
        if race == "Fey" and Dice() == 1: one += "\n Gentle Lullaby [DC 10+%Cha Wisdom saving throw] \n\t The creature falls asleep and is unconscious for 1 minute. The effect ends if the creature takes damage or if someone takes an action to shake the creature awake."   

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
                
        if race == "Monstrosity" and Dice() == 1:
            cantrip += "\n - Luring Song: \n\t The monstrosity sings a magical melody. Every humanoid and giant within 300 feet of the harpy that can hear the song must succeed on a DC [10+%Cha] Wisdom saving throw or be charmed until the song ends. The monstrosity must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the monstrosity is incapacitated. While charmed by the monstrosity, a target is incapacitated and ignores the songs of other monstrosities. If the charmed target is more than 5 feet away from the monstrosity, the target must move on its turn toward the monstrosity by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the monstrosity, a target can repeat the saving throw. A creature can also repeat the saving throw at the begguining of each of its turns. If a creature's saving throw is successful, the effect ends on it. A target that successfully saves is immune to this monstrosity's song for the next 24 hours."
                
        if race == "Monstrosity":
            if Dice() == 1:
                cantrip += "\n - Acid Spray (Recharge 6): \n\t The Monstrosity spits acid in a line that is 30 feet long and 5 feet wide, provided that it has no creature grappled. Each creature in that line must make a DC [10+%Str] Dexterity saving throw, taking 10 (3d6) acid damage on a failed save, or half as much damage on a successful one."

        if race == "Ooze":
            if Dice()==1:
                cantrip += " \n Psychic Crush (Recharge 5–6). \n\t The ooze targets one creature that it can sense within 60 feet of it. The target must make a DC 10 Intelligence saving throw, taking 10 (3d6) psychic damage on a failed save, or half as much damage on a successful one."
                
        if race == "Snakefolk":
            if Dice()==1:
                cantrip += "\n- animal friendship (snakes only)"

        if race == "Snakefolk":
            if Dice()==1:
                three += "\n- Poison Spray"

        if race == "Snakefolk":
            if Dice()==1:
                three += "\n- Suggestion"

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
            if Dice(11) == 1:
                one += "\n - Infestation Spores \n\t The plant releases spores that burst out in a cloud that fills a 10-foot-radius sphere centered on it, and the cloud lingers for 1 minute. Any flesh-and-blood creature in the cloud when it appears, or that enters it later, must make a DC [10+%CON] Constitution saving throw. The save DC is 8 + the plant's Constitution modifier + the plant's proficiency bonus. On a successful save, the creature can't be infected by these spores for 24 hours. On a failed save, the creature is infected with a disease called the spores of Zuggtmoy and also gains a random form of indefinite madness (determined by rolling on the Madness of Zuggtmoy table) that lasts until the creature is cured of the disease or dies. While infected in this way, the creature can't be reinfected, and it must repeat the saving throw at the end of every 24 hours, ending the infection on a success. On a failure, the infected creature's body is slowly taken over by fungal growth, and after three such failed saves, the creature dies and is reanimated as a spore servant if it's a humanoid or a Large or smaller beast. \n d100 \t	Flaw (lasts until cured) \n 01-20 \t I see visions in the world around me that others do not. \n 21-40 \t I periodically slip into a catatonic state, staring off into the distance for long stretches at a time. \n 41-60 \t I see an altered version of reality, with my mind convincing itself that things are true even in the face of overwhelming evidence to the contrary. \n 61-80 \t My mind is slipping away, and my intelligence seems to wax and wane. \n  81-00 \t I am constantly scratching at unseen fungal infections." 
                
        if race == "Plant": 
            if Dice(8) == 1:
                one += "\n - Euphoria Spores \n\t The plant releases a cloud of spores in a 20-foot-radius sphere centered on itself. Other creatures in that area must each succeed on a DC [10+%Con] Constitution saving throw or become poisoned for 1 minute. The save DC is 8 + the plant's Constitution modifier + the plant's proficiency bonus. A creature can repeat the saving throw at the start of each of its turns, ending the effect early on itself on a success. When the effect ends on it, the creature gains one level of exhaustion."  

        if race == "Undead": 
            if Dice(8) == 1:
                cantrip += "\n - Strength Drain \n\t On an attack hit the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. \n\t If a non-evil humanoid dies from this attack, a new shadow rises from the corpse 1d4 hours later."  

        if race == "Undead": 
            if Dice(8) == 1:
                cantrip += "\n - Life Drain \n\t On an attack hit the target's Hit Points Maximum is reduced by the damage dealt. The target dies if this reduces its Hit Points Maximum to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. "  
                
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
        r += "\n" + one
    if not(two == "2/Day each: "):
        r +=  "\n" + two
    if not(three == "3/Day each: "):
        r +=  "\n" + three
    return  r
























def Actions(Type=""):
    r = ""

    if Type == "Spy":
        r = r + "\n- Superior Invisibility"

    if Type == "Aberration":
        if Dice() == 1:
            r += "\n- Blinding Spittle (Recharge 5–6). \n\t The Aberration spits a chemical glob at a point it can see within 15 feet of it. The glob explodes in a blinding flash of light on impact. Each creature within 5 feet of the flash must succeed on a DC 13 Dexterity saving throw or be blinded until the end of the aberration's next turn."

    if Type == "Beast" or Type == "Beastfolk": 
        if Dice() == 1:
            r = r+ "\n- Speed. \n\t 50 ft."

    if Type == "Beast" or Type == "Beastfolk": 
        if Dice() == 1:
            r = r+ "\n- Climb. \n\t 30 ft."

    if Type == "Beast" or Type == "Beastfolk": 
        if Dice(7) == 1:
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
            r = r+ "\n - Relentless \n\t (Recharges after a Short or Long Rest). \n\t If the beast takes 7 damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."

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
        if Dice(9) == 1:
            r = r + "\n- Spider Climb \n\t The beast can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."  
            if Dice(2) == 1:
                r = r + "\n- Web Sense \n\t While in contact with a web, the spider knows the exact location of any other creature in contact with the same web."
            if Dice(2) == 1:
                r = r + "\n- Web Walker \n\t The spider ignores movement restrictions caused by webbing."
            if Dice(2) == 1:
                r += "Web (Recharge 5–6). \n\t Ranged Weapon Attack: +4 to hit, range 30/60 ft., one Large or smaller creature. Hit: The creature is restrained by webbing. As an action, the restrained creature can make a DC 11 Strength check, escaping from the webbing on a success. The effect ends if the webbing is destroyed. The webbing has AC 10, 5 hit points, is vulnerable to fire damage and immune to bludgeoning, poison and psychic damage."

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
            
    if Type=="Elemental": 
        if Dice(8) == 1:
            r = r+ "\n- Illumination.\n\tThe beast sheds bright light in a 10-foot radius and dim light for an additional 10 ft."
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(8) == 1:
            r = r+ "\n-Sure-Footed \n\t The beast has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(7) == 1:
            r = r + "\n- Hold Breath. \n\t The beast can hold its breath for 30 minutes."
            
    if Type=="Beast" or Type=="Beastfolk": 
        if Dice(10) == 1:
            r = r+ "\n- Mimicry \n\t The Beast can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."
            
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
            r = r + "\n - Amphibious \n\t The dragon can breathe air and water."

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
            r = r+ "\n- Magic Resistance \n\t The Fey has advantage on saving throws against spells and other magical effects."

    if Type == "Fey": 
        if Dice(2) == 1:
            r = r+ "\n- Superior Invisibility \n\t  The Fey magically turns invisible until its concentration ends (as if concentrating on a spell). Any equipment the Fey wears or carries is invisible with it."

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

    if Type == "Construct":
        if Dice()==1:
            r = r+ "\n- Terrifying Glare:\n\t The Construct is incapacitated while in the area of an antimagic field. If targeted by dispel magic, the Construct must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute."

        
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
            r = r+"\Condition Immunities:  \n\t prone"


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

    if Type == "Aberration":
        if Dice() == 1:
            r = r+ "\n- Aberrant Ground: \n\t The ground in a 10-foot radius around the Aberration is doughlike difficult terrain. Each creature that starts its turn in that area must succeed on a DC 10 Strength saving throw or have its speed reduced to 0 until the start of its next turn."

    if Type == "Aberration":
        if Dice() == 1:
            r += "\n- Gibbering. \n\t The Aberration babbles incoherently while it can see any creature and isn't incapacitated. Each creature that starts its turn within 20 feet of the Aberration and can hear the gibbering must succeed on a DC 10 Wisdom saving throw. On a failure, the creature can't take reactions until the start of its next turn and rolls a d8 to determine what it does during its turn. On a 1 to 4, the creature does nothing. On a 5 or 6, the creature takes no action or bonus action and uses all its movement to move in a randomly determined direction. On a 7 or 8, the creature makes a melee attack against a randomly determined creature within its reach or does nothing if it can't make such an attack."
        
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
            r = r + "\n - False Appereance. While motionless, the elemental is indistinguishable from a natural feature, such as ponds, rocks, statues, etc"

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
            r = r + "\n- Damage Immunities: poison" 
            
    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n- Damage Vulnerabilities: cold"
            
    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n- Damage Vulnerabilities: fire"
            
    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n- Condition Immunities: Exhaustion" 

    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n- Condition Immunities: Petrified" 

    if Type == "Elemental":
        if Dice() == 1:
            r = r + "\n- Condition Immunities: Poisoned" 

        
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

    if Type == "Beastfolk":
        if Dice() == 1:
            r = r + "\n - Chameleon Skin \n\t The beastfolk has advantage on Dexterity (Stealth) checks made to hide."
            
    if Type == "Lizardfolk":
        if Dice(2) == 1:
            r = r + "\n -  Spider Climb. \n\t The lizard can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
            
    if Type == "Lizardfolk":
        if Dice() == 1:
            r = r + "\n - Stench.  \n\t Any creature other than a Lizardfolk that starts its turn within 5 feet of the Lizardfolk must succeed on a DC [10+%CON] Constitution saving throw or be poisoned until the start of the creature's next turn. On a successful saving throw, the creature is immune to the stench of all Lizardfolk for 1 hour."

    if Type == "Undead":
        if Dice() == 1:
            r = r + "\n - Stench.  \n\t Any creature that starts its turn within 5 feet of the undead must succeed on a DC 10 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creature is immune to the undead's Stench for 24 hours."


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
        elif Dice() == 1:
            r += "\n- Ooze Cube \n\t The cube takes up its entire space. Other creatures can enter the space, but a creature that does so is subjected to the cube's Engulf and has disadvantage on the saving throw. Creatures inside the cube can be seen but have total cover. A creature within 5 feet of the cube can take an action to pull a creature or object out of the cube. Doing so requires a successful DC 12 Strength check, and the creature making the attempt takes 10 (3d6) acid damage. The cube can hold only one Large creature or up to four Medium or smaller creatures inside it at a time."
            r += " Engulf. \n\t The cube moves up to its speed. While doing so, it can enter Large or smaller creatures' spaces. Whenever the cube enters a creature's space, the creature must make a DC 12 Dexterity saving throw. On a successful save, the creature can choose to be pushed 5 feet back or to the side of the cube. A creature that chooses not to be pushed suffers the consequences of a failed saving throw. On a failed save, the cube enters the creature's space, and the creature takes 10 (3d6) acid damage and is engulfed. The engulfed creature can't breathe, is restrained, and takes 21 (6d6) acid damage at the start of each of the cube's turns. When the cube moves, the engulfed creature moves with it. An engulfed creature can try to escape by taking an action to make a DC 12 Strength check. On a success, the creature escapes and enters a space of its choice within 5 feet of the cube."


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

    if Type == "Snakefolk":
        r += "\n- Darkvision: 60 ft"

    if Type == "Snakefolk":
        if Dice(3) == 1:
            r += "\n- Magic Resistance \n\t The Snakefolk has advantage on saving throws against spells and other magical effects."



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
        if Dice() == 1:
            r = r + "\n -Turn Defiance \n\t The undead and any undeads within 30 feet of it have advantage on saving throws against effects that turn undead."

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
    
    if Type == "Explorer" and Dice()==1:
        r = r+ "\n- Keen Senses\n\t The Explorer has advantage on Wisdom (Perception) checks that rely on senses."   
        
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
            r = r+ "\n Damage Resistance: Bludgeoning"

    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Damage Resistance: Piercing"

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
        if Dice(2) == 1:
            r = r+ "\n- Pack Tactics \n\t The Bandit has advantages on attack on targets within 5ft of an ally of the bandit."

    if Type == "Bandit":
        if Dice(2) == 1:
            r = r+ "\n- Multiattack \n\t The Bandit makes three simple melee attacks. Or the Bandit makes two ranged or special attacks."
        
    if Type == "Bandit":
        if Dice(2) == 1:
            r = r+ "\n- Parry (Reaction) \n\t The Bandit adds 2 to its AC against one melee attack that would hit it. To do so, the bandit must see the attacker and be wielding a melee weapon."

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
            
    if Type == "Cultist":
        if Dice(2)==1:
            r = r+ "\n Dark Devotion.\n\t The cultist has advantage on saving throws against being charmed or frightened."
            
    if Type == "Cultist":
        if Dice(2)==1:
            r = r+ "\n Multiattack.\n\t The cultist makes two simple melee attacks."
        
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

    if Type == "Fiend" and Dice()==1:
        r = r + "\n Hellish Rejuvenation. \n\t A Fiend that dies in the Nine Hells comes back to life with all its hit points in", Dice(10), "days unless it is killed by a good-aligned creature with a bless spell cast on that creature or its remains are sprinkled with holy water."
            
    if Type== "Fiend" and Dice()==1:
        r += "\n Damage Resistances. \n\t cold"
    if Type== "Fiend" and Dice()==1:
        r += "\n Damage Resistances. \n\t fire"
    if Type== "Fiend" and Dice()==1:
        r += "\n Damage Resistances. \n\t lightning"
    if Type== "Fiend" and Dice()==1:
        r += "\n Damage Immunities. \n\t poison"
    if Type== "Fiend" and Dice()==1:
        r += "\n Darkvision. \n\t cold"
    if Type== "Fiend" and Dice()==1:
        r += "\n Telepathy. \n\t 60 ft. Only in Abyssal."

    if Type == "Spy":
        if Dice(2) == 1:
            r = r + "\n- Cunning Action \n\t On each of its turns, the spy can use a bonus action to take the Dash, Disengage, or Hide action."

    if Type == "Spy":
        if Dice(2) == 1:
            r = r + "\n- Sneak Attack (1/Turn). \n\t The spy deals an extra 7 (2d6) damage when it hits a target with a weapon attack and has advantage on the attack roll, or when the target is within 5 feet of an ally of the spy that isn't incapacitated and the spy doesn't have disadvantage on the attack roll." 
            
    if Type == "Spy":
        if Dice(2) == 1:
            r = r + "\n- Multiattack. \n\t The spy makes two simple melee attacks." 

    if Type == "Berserker":
        if Dice(2) == 1:
            r = r + "\n- Multiattack"

    if Type == "Berserker":
        if Dice(2) == 1:
            r = r + "\n- Reckless \n\t At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn."
        
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
            r += "\n - Borrow: 10 ft"

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
            r = r + "\n- Keen Smell.\n\t The monstrosity has advantage on Wisdom (Perception) checks that rely on smell.\n"  
            
    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n- Fly: 60 ft.\n"  

    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n- Darkvision.\n\t 60 ft.\n"  

    if Type == "Monstrosity":
        if Dice() == 1:
            r = r + "\n- Tremorsense.\n\t 60 ft.\n"  

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
            
    elif Type == "Ranger":
        r = r + Attack(4)
        r = "\n - Multiattack."
        
    elif Type == "Bandit":
        r = r + "\n- Parry \n\t The Bandit adds 2 to its AC against one melee attack that would hit it. To do so, the bandit must see the attacker and be wielding a melee weapon."
        
    elif Type =="Warrior" and  Dice()==1:
        r = r + "\n- Parry \n\t The warrior adds 2 to its AC against one melee attack that would hit it. To do so, the warrior must see the attacker and be wielding a melee weapon."
        
    if Type == "Kobold":    
        r = r + "\n- Darkvision \n\t 60ft."
        r = r + "\n- Pack Tactics \n\t The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated."
        r = r + "\n- Sunlight Sensitivity \n\t While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    if Type == "Kobold" and Dice() == 1:
            r = r+ "\n Fly \t 30ft."

    if Type == "Noble" and Dice()==1:
        r = r + "\n- Parry \n\t The noble adds 2 to its AC against one melee attack that would hit it. To do so, the noble must see the attacker and be wielding a melee weapon."
    
    if Type == "Plant" and Dice() == 1:
        r = r+ "\n Condition Immunities:  frightened"
            
    if Type == "Plant" and Dice() == 1:
        r = r + "\n-Distress Spores. \n\t When the plant takes damage, all other plants within 240 feet of it can sense its pain."  
            
    if Type == "Plant" and Dice() == 1:
        r = r + "\n-Sun Sickness. \n\t While in sunlight, the plant has disadvantage on ability checks, attack rolls, and saving throws. The plant dies if it spends more than 1 hour in direct sunlight."
            
    if Type == "Plant" and Dice() == 1:
        r = r + "\n Condition Immunities\n\t blinded, deafened, frightened"

    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n Blindsight\n\t 30 ft"  
        elif Dice() == 1:
            r = r + "\n Blindsight\n\t 60 ft (Blind Beyond this radius)."  

    if Type == "Plant" and Dice() == 1:
        r = r + "\n Darkvision\n\t 120 ft"        
   
    if Type == "Plant" and Dice() == 1:
        r = r + "\n Death Burst\n\t The Plant explodes when it drops to 0 hit points. Each creature within 20 feet of it must succeed on a DC 15 Constitution saving throw or take 10 (3d6) poison damage and become infected with a disease on a failed save. Creatures immune to the poisoned condition are immune to this disease. Spores invade an infected creature's system, killing the creature in a number of hours equal to 1d12 + the creature's Constitution score, unless the disease is removed. In half that time, the creature becomes poisoned for the rest of the duration. After the creature dies, it sprouts 2d4 Tiny gas spores that grow to full size in 7 days."        


    if Type == "Warrior":
        r = r + "\n- Pack Tactics \n\t The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated."
        
    if Type == "Warrior" and Dice(2)==1:
        r= r + "\n- Multiattack \n\t The Warrior can attack an additional time on his turn."

    if Type == "":
        if Dice(2)==1:
            return Actions(Race())
        else:
            return Actions(Background())
    return r
    













def Legendary(Type):
    r = ""
    if Type == "Human" or Type == 1:
        r = r+ "\n- Attack"
    else:
        if Dice(2)==1:
            r = r + "\n- Attack: \n\t It can do a simple attack to any creature" 
        if Dice(2)==1:
            r += "\n- Move: \n\t It can move half their movement"
    return r

def Lair(Type):
    r = ""
    
    if Type == "Dragon":
        if Dice() == 1:
            r = r+ "\n- Chaotic Aura \n\t The dragon creates misdirecting currents of air and magic around itself. Until initiative count 20 on the next round, whenever a ranged attack roll misses the dragon, reroll the attack against a random creature within 30 feet of the dragon that doesn't have total cover against the attack."

    if Type == "Fey":
        if Dice() == 1:
            r = r+ "\n- Chaotic Aura \n\t The Fey creates misdirecting currents of air and magic around itself. Until initiative count 20 on the next round, whenever a ranged attack roll misses the Fey, reroll the attack against a random creature within 30 feet of the dragon that doesn't have total cover against the attack."
            
    if Type == "Dragon":
        if Dice() == 1:
            r = r+ "\n- Grasping Plants \n\t The dragon causes roots and vines to temporarily grow around it; until initiative count 20 on the next round, the ground within 20 feet of the dragon is difficult terrain."

    if Type == "Fey":
        if Dice() == 1:
            r = r+ "\n- Grasping Plants \n\t The fey causes roots and vines to temporarily grow around it; until initiative count 20 on the next round, the ground within 20 feet of the fey is difficult terrain."
            
    if Type == "Plant":
        if Dice() == 1:
            r = r+ "\n- Grasping Plants \n\t The fey causes roots and vines to temporarily grow around it; until initiative count 20 on the next round, the ground within 20 feet of the fey is difficult terrain."
    return r
    
    

def Region(Type):
    r = ""
    if Type == "Fey":
        if Dice() == 1:
            r += "\n- Compulsory Offering \n\t The first time a creature comes within 1 mile of the faerie dragon's lair, the creature must succeed on a DC 15 Wisdom saving throw or feel an overwhelming compulsion to leave an offering worth at least 5 gp stashed in an out-of-the-way place. The dragon immediately senses the location of this gift. A creature can be affected only once by this compulsion."
            
    if Type == "Fey":
        if Dice() == 1:
            r += "\n- Malleable Time \n\t Time is fluid within 1 mile of the fey's lair, flowing somewhere between half and twice its normal speed."
    return r    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def PlotHook():
    Hooks = [
        "Someone I love was killed by a rival faction, and I will have revenge."
        "I love someone from another house, but the relationship is forbidden.",
        "I was exiled for a crime I didn't commit.",
        "I keep my thoughts and discoveries in a journal. My journal is my legacy. I just lost it!",
        "A monster that slaughtered dozens of innocent people spared my life, and I don’t know why. I am certain it follows me since.",
        "I protect those who cannot protect themselves.",
        "I have a family, but I have no idea where they are. One day, I hope to see them again.",
        "Recruited into a lord's army, I rose to leadership and was commended for my heroism. Now I fight for them."
        "A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.",
        "I'm breaking into a tyrant's castle to steal weapons to arm the people.",
        "I lead a militia to fight off an invading army.",
        "I steal from merchants to help the poor.",
        "I'm the last hope against a terrible monster.",
        "I want to save people of a comming disaster.",
        "I stand up to a tyrant's agents.",
        "I must repay my village's debt.",
        "My destiny awaits me at the bottom of a particular pond in the Feywild.",
        "The gods saved me during a terrible storm, and I will honor their gift.",
        "I will hunt the many famous beasts of this land.",
        "I will fish the many famous waters of this land.",
        "Someone else's greed destroyed my livelihood, and I will be compensated.",
        "I lost something important in the deep sea, and I intend to find it.",
        "I have a tail like that of a dog or another animal, as a punishment from a Fey for an accidental insult.",
        "I have a weakness for the exotic beauty of the people of these lands.",
        "I do everything for those who were taken from me.",
        "I am exceptional. I do this because no one else can, and no one can stop me.",
        "I stand in opposition, lest the wicked go unopposed.",
        "I've seen too many in need. I must not fail them as everyone else has.",
        "What I do, I do for the world. The people don't realize how much they need me.",
        "I do everything for my family. My first thought is keeping them safe.",
        "I once satirized a noble who still wants my head. It was a mistake that I will likely repeat.",
        "I would do anything for the other members of my old troupe.",
        "I will do anything to prove myself superior to my hated rival.",
        "I want to be famous, whatever it takes.",
        "Someone stole an object precious to me, and someday I'll get it back.",
        "Someone I loved died because of I mistake I made. That will never happen again.",
        "I'm guilty of a terrible crime. I hope I can redeem myself for it.",
        "I will become the greatest thief that ever lived.",
        "Something important was taken from me, and I aim to steal it back.",
        "My ill-gotten gains go to support my family.",
        "I'm trying to pay off an old debt I owe to a generous benefactor.",
        "I swindled and ruined a person who didn't deserve it. I seek to atone for my misdeeds but might never be able to forgive myself.",
        "A powerful person killed someone I love. Some day soon, I'll have my revenge.",
        "I come from a noble family, and one day I'll reclaim my lands and title from those who stole them from me.",
        "Somewhere out there, I have a child who doesn't know me. I'm making the world better for him or her.",
        "I owe everything to my mentor – a horrible person who's probably rotting in jail somewhere.",
        "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.",
        "I hope to bring prestige to a library, a museum, or a university.",
        "I won't sell an art object or other treasure that has historical significance or is one of a kind.",
        "I have a friendly rival. Only one of us can be the best, and I aim to prove it's me.",
        "I want to find my mentor, who disappeared on an expedition some time ago.",
        "Ever since I was a child, I've heard stories about a lost city. I aim to find it, learn its secrets, and earn my place in the history books.",
        "Is under a curse.",
        "Is the Protector of the Land",
        "Is guarding something of great importance.",
        "Is protecting someone of great importance.",
        "Is looking for a special thing",
        "Just wants to have fun",
        "Is looking for someone",
        "Wants to get rich",
        "Is selling something",
        "Is buying something",
        "Wants to ammend a mistake.",
        "Wants to recuperate his honor",
        "Is protecting their family",
        "Wants to prove himself",
        "Is curious",
        "Is protecting their interests",
        "They are lost",
        "They are a freedomfighter.",
        "They want to topple a tyrant.",
        "They fight to preserve order",
        "They are in pilgrimage",
        "I lost my home, and I'm looking for a new life.",
        "A higher power commanded a very important mission.",
        "Is following orders.",
        "I am injured. ",
        "I'm in a forbidden or impossible relationship. ",
        "I have a legacy to mantain",
        "I have a great rival",
        "I pursue a goal that breaks tradition or law",
        "They are in debt.",
        "They lead an uprising.",
        "Feels loyalty to two opposing causes or people",
        "Has a crisis of faith.",
        "Is looking for revenge",
        "Is trying to solve a failure or tragedy",
        "Is standing up for those who are not equipped to stand up for themselves.",
        "They keep a great secret.",
        "They need to unveil a great secret.",
        "They are bored.",
        "They are hungry.",
        "They are trapped.",
        "They want to create something.",
        "They are running from justice.",
        "They are running from justice for a crime they didn't commit.",
        "They are optimistic, seeing events in the most positive light.",
        "They have to make a very difficult choice",
        "I serve an unethical and corrupt organization.",
        "They would die to recover an ancient relic of their faith that was lost long ago.",
        "They will someday get revenge on the corrupt temple hierarchy who branded them a heretic.",
        "They owe their life to the priest who took them in when their parents died.",
        "Everything I do is for the common people.",
        "I will do anything to protect the holy site where I serve.",
        "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.",
        "My mentor gave me a journal filled with lore and wisdom. Losing it would devastate me.",
        "Having lived among the people of a primeval tribe or clan, I long to return and see how they are faring.",
        "Years ago, tragedy struck the members of an isolated society I befriended, and I will honor them.",
        "I want to learn more about a particular humanoid culture that fascinates me.",
        "I seek to avenge a clan, tribe, kingdom, or empire that was wiped out.",
        "I have a trinket that I believe is the key to finding a long-lost society.",
        "I will overcome a rival and prove myself their better.",
        "My mistake got someone hurt. Ill never make that mistake again.",
        "I will be the best for the honor and glory of my home.",
        "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.",
        "The tyrant who rules my land will stop at nothing to see me killed.",
        "Your family has a history of practicing the dark arts. You dabbled once and felt something horrible clutch at your soul, whereupon you fled in terror.",
        "An apparition that has haunted your family for generations now haunts you. You don’t know what it wants, and it won’t leave you alone.",
        "An oni took your sibling one cold, dark night, and you were unable to stop it.",
        "You were cursed with lycanthropy. You are now haunted by the innocents you slaughtered.",
        "My torment drove away the person I love. I strive to win back the love I’ve lost.",
        "I have a child to protect. I must make the world a safer place for them.",
        "I am searching for spiritual enlightenment.",
        "I am the caretaker of an ancient ruin or relic.",
        "I have great insight into a great evil that only I can destroy.",
        "Should my discovery come to light, it could bring ruin to the world.",
        "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.",
        "I am a pilgrim in search of a person, place, or relic of spiritual significance.",
        "A fiend possessed you as a child. You were locked away but escaped. The fiend is still inside you, but now you try to keep it locked away.",
        ""]
    return random.choice(Hooks)
    
    
    
    
    
def Trait(background=""):
    Traits = [
        "My secret could get me expelled from my house.",
        "My house and blood line make me the best!",
        "I'm obsessed with conspiracy theories and worried about secret societies and hidden demons.",
        "I'm fixated on following official protocols.",
        "I'm determined to impress the leaders of my faction, and to become a leader myself.",
        "My organization must evolve, and I'll lead the evolution.",
        "I don't care about the organization as a whole, but I would do anything for my old mentor.",
        "I never forget an insult against me.",
        "I'm always looking to improve efficiency.",
        "I like keeping secrets and won't share them with anyone.",
        "I'd risk too much to uncover a lost bit of knowledge.",
        "I let my need to win arguments overshadow friendships and harmony.",
        "I am dogmatic in my thoughts and philosophy.",
        "I harbor dark, bloodthirsty thoughts that my isolation and meditation failed to quell.",
        "Now that I've returned to the world, I enjoy its delights a little too much.",
        "I entered seclusion because I loved someone I could not have.",
        "I'm still seeking the enlightenment I pursued in my seclusion, and it still eludes me.",
        "I am working on a grand philosophical theory and love sharing my ideas.",
        "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings.",
        "I connect everything that happens to me to a grand, cosmic plan.",
        "I'm oblivious to etiquette and social expectations.",
        "I feel tremendous empathy for all who suffer.",
        "The leader of my community had something wise to say on every topic, and I am eager to share that wisdom.",
        "I am utterly serene, even in the face of disaster.",
        "I've been isolated for so long that I rarely speak, preferring gestures and the occasional grunt.",
        "I needed to commune with nature, far from civilization.",
        "I needed a quiet place to work on my art, literature, music, or manifesto.",
        "I retreated from society after a life-altering event.",
        "I talk to spirits that no one else can see.",
        "I am a purveyor of doom and gloom who lives in a world without hope.",
        "I have an addiction.",
        "I feel no compassion for the dead. They’re the lucky ones.",
        "I assume the worst in people.",
        "I have certain rituals that I must follow every day. I can never break them.",
        "There’s evil in me, I can feel it. It must never be set free.",
        "A terrible guilt consumes me. I hope that I can find redemption through my actions.",
        "I would sacrifice my life and my soul to protect the innocent.",
        "I put no trust in divine beings.",
        "I refuse to become a victim, and I will not allow others to be victimized.",
        "I expect danger around every corner.",
        "I don’t talk about the thing that torments me. I’d rather not burden others with my curse.",
        "I live for the thrill of the hunt.",
        "I spend money freely and live life to the fullest, knowing that tomorrow I might die.",
        "I like to read and memorize poetry. It keeps me calm and brings me fleeting moments of happiness.",
        "I don't run from evil. Evil runs from me.",
        "You did terrible things to avenge the murder of someone you loved. You became a monster, and it haunts your waking dreams.",
        "You opened an eldritch tome and saw things unfit for a sane mind. You burned the book, but its words and images are burned into your psyche.",
        "A hag kidnapped and raised you. You escaped, but the hag still has a magical hold over you and fills your mind with evil thoughts.",
        "I was born under a dark star. I can feel it watching me, coldly and distantly. Sometimes it beckons me in the dead of night.",
        "I'm well known for my work, and I want to make sure everyone appreciates it. I'm always taken aback when people haven't heard of me.",
        "I don't part with my money easily and will haggle tirelessly to get the best deal possible."
        "I like to talk at length about my profession.",
        "I'm rude to people who lack my commitment to hard work and fair play.",
        "I'm full of witty aphorisms and have a proverb for every occasion.",
        "I always want to know how things work and what makes people tick.",
        "I'm a snob who looks down on those who can't appreciate fine art.",
        "I believe that anything worth doing is worth doing right. I can't help it – I'm a perfectionist.",
        "I change my mood or my mind as quickly as I change key in a song.",
        "I'll settle for nothing less than perfection.",
        "I get bitter if I'm not the center of attention.",
        "I love a good insult, even one directed at me.",
        "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
        "I'm a hopeless romantic, always searching for that 'special someone'."
        "Whenever I come to a new place, I collect local rumors and spread gossip.",
        "I know a story relevant to almost every situation.",
        "I have trouble trusting in my allies.",
        "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
        "I have a weakness for the vices of the city, especially hard drink.",
        "The people who knew me when I was young know my shameful secret, so I can never go home again.",
        "I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.",
        "I wish my childhood sweetheart had come with me to pursue my destiny.",
        "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
        "I worked the land, I love the land, and I will protect the land.",
        "I get bored easily. When am I going to get on with my destiny?",
        "I misuse long words in an attempt to sound smarter.",
        "Thinking is for other people. I prefer action.",
        "I'm confident in my own abilities and do what I can to instill confidence in others.",
        "I have a strong sense of fair play and always try to find the most equitable solution to arguments.",
        "When I set my mind to something, I follow through no matter what gets in my way.",
        "If someone is in trouble, I'm always ready to lend help.",
        "I judge people by their actions, not their words.",
        "I am obsessed with catching an elusive beast, often to the detriment of other pursuits.",
        "I work hard, but I play harder.",
        "I am inclined to tell long-winded stories at inopportune times.",
        "I have lived a hard life and find it difficult to empathize with others.",
        "I become depressed and anxious if I'm away from the sea too long.",
        "I am judgmental, especially of those I deem homebodies or otherwise lazy.",
        "Luck favors me, and I take risks others might not.",
        "I dislike bargaining; state your price and mean it.",
        "I work hard; nature offers no handouts.",
        "I laugh heartily, feel deeply, and fear nothing.",
        "Rich folk don't know the satisfaction of hard work.",
        "I need long stretches of quiet to clear my head.",
        "My friends are my crew; we sink or float together.",
        "I am unmoved by the wrath of nature.",
        "I'm always changing my mind-well, almost always.",
        "I have many vices and tend to indulge them.",
        "I never give away anything for free and always expect something in return.",
        "I'm forgetful. Sometimes I can't remember even the simplest things.",
        "I'm a kleptomaniac who covets shiny, sparkling treasure.",
        "I'm always operating under a tight timeline, and I'm obsessed with keeping everything on schedule.",
        "I think the whole multiverse is out to get me.",
        "I easily lose track of time. My poor sense of time means I'm always late.",
        "I feel indebted to a witch or fae for giving me a home and a purpose.",
        "I'm drawn to the Feywild and long to return there, if only for a short while.",
        "The Witchlight Carnival (Halloween) feels like home to me.",
        "I can't bring myself to harm a Fey creature, either because I consider myself one or because I fear the repercussions.",
        "A trusted friend is the most important thing in the multiverse to me.",
        "I do what I can to protect the natural world.",
        "I find magic in all its forms to be compelling. The more magical a place, the more I am drawn to it.",
        "I would never break my word.",
        "Rule of Three. Everything in the multiverse happens in threes. I see the 'rule of three' everywhere.",
        "I can't bring myself to trust most adults.",
        "I live by my own set of weird and wonderful rules.",
        "When I have a new idea, I get wildly excited about it until I come up with another, better idea.",
        "I have never lost my childlike sense of wonder.",
        "Wherever I go, I try to bring a little of the warmth and tranquility of home with me.",
        "Good music makes me weep like a baby.",
        "Like a nomad, I can't settle down in one place for very long.",
        "I'm haunted by fey laughter that only I can hear, though I know it's just my mind playing tricks on me.",
        "Flowers wilt in my presence.",
        "Flowers bloom in my presence.",
        "My skin sparkles in sunlight.",
        "My skin sparkles in moonlight.",
        "I have a sweet scent, like that of nectar or honey",
        "My eyes swirl with iridescent colors.",
        "I consider the adherents of other gods to be deluded innocents at best, or ignorant fools at worst.",
        "I don't take kindly to some of the actions and motivations of the people of this land, because these folk are different from me.",
        "I have a weakness for the new intoxicants and other pleasures of this land.",
        "I pretend not to understand the local language in order to avoid interactions I would rather not have.",
        "I am secretly (or not so secretly) convinced of the superiority of my own culture over that of this foreign land.",
        "Though I had no choice, I lament having to leave my loved ones behind. I hope to see them again one day.",
        "I'm fascinated by the beauty and wonder of this new land.",
        "My freedom is my most precious possession. I'll never let anyone take it from me again.",
        "I hold no greater cause than my service to my people.",
        "The gods of my people are a comfort to me so far from home.",
        "So long as I have this token from my homeland, I can face any adversity in this strange land.",
        "I begin or end my day with small traditional rituals that are unfamiliar to those around me.",
        "I honor my deities through practices that are foreign to this land.",
        "I express affection or contempt in ways that are unfamiliar to others.",
        "I have a strong code of honor or sense of propriety that others don't comprehend.",
        "I have my own ideas about what is and is not food, and I find the eating habits of those around me fascinating, confusing, or revolting.",
        "I have different assumptions from those around me concerning personal space, blithely invading others' space in innocence, or reacting to ignorant invasion of my own.",
        "I see morality entirely in black and white.",
        "I think far ahead, a detachedness often mistaken for daydreaming.",
        "I overexert myself, sometimes needing to recuperate for a day or more.",
        "I have no sense of humor. Laughing is uncomfortable and embarrassing.",
        "I never make eye contact or hold it unflinchingly.",
        "I an callous about death. It comes to us all eventually.",
        "I am ever learning how to be among others—when to stay quiet, when to laugh.",
        "I cultivate a single obscure hobby or study and eagerly discuss it at length.",
        "I think far ahead, a detachedness often mistaken for daydreaming.",
        "I sleep just as much as I need to and on an unusual schedule.",
        "I treasure a memento of a person or instance that set me upon my path.",
        "I strive to have no personality—it's easier to forget what's hardly there.",
        "I'm earnest and uncommonly direct.",
        "Despite my best efforts, I am unreliable to my friends.",
        "I have trouble keeping my true feelings hidden. My sharp tongue lands me in trouble.",
        "A scandal prevents me from ever going home again. That kind of trouble seems to follow me around.",
        "I'm a sucker for a pretty face.",
        "I'll do anything to win fame and renown.",
        "I idolize a hero of the old tales and measure my deeds against that person's.",
        "I change my mood or my mind as quickly as I change key in a song.",
        "I'll settle for nothing less than perfection.",
        "I get bitter if I'm not the center of attention.",
        "I love a good insult, even one directed at me.",
        "Nobody stays angry at me or around me for long, since I can defuse any amount of tension.",
        "I'm a hopeless romantic, always searching for that 'special someone.'",
        "Whenever I come to a new place, I collect local rumors and spread gossip.",
        "I know a story relevant to almost every situation.",
        "An innocent person is in prison for a crime that I committed. I'm okay with that.",
        "I turn tail and run when things look bad.",
        "I have a 'tell' that reveals when I'm lying.",
        "If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.",
        "When faced with a choice between money and my friends, I usually choose the money.",
        "When I see something valuable, I can't think about anything but how to steal it.",
        "I blow up at the slightest insult.",
        "The best way to get me to do something is to tell me I can't do it.",
        "I don't pay attention to the risks in a situation. Never tell me the odds.",
        "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
        "I would rather make a new friend than a new enemy.",
        "The first thing I do in a new place is note the locations of everything valuable – or where such things could be hidden.",
        "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.",
        "I always have a plan for what to do when things go wrong.",
        "I hate to admit it and will hate myself for it, but I'll run and preserve my own hide if the going gets tough.",
        "I can't resist swindling people who are more powerful than me.",
        "I'm too greedy for my own good. I can't resist taking a risk if there's money involved.",
        "I'm convinced that no one could ever fool me the way I fool others.",
        "I'm always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.",
        "I can't resist a pretty face.",
        "I pocket anything I see that might have some value.",
        "I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.",
        "Sarcasm and insults are my weapons of choice.",
        "I lie about almost everything, even when there's no good reason to.",
        "I'm a born gambler who can't resist taking a risk for a potential payoff.",
        "Flattery is my preferred trick for getting what I want.",
        "I have a joke for every occasion, especially occasions where humor is inappropriate.",
        "I fall in and out of love easily, and am always pursuing someone.",
        "I convince people that worthless junk is worth their hard-earned money.",
        "I run sleight-of-hand cons on street corners.",
        "I put on new identities like clothes.",
        "I insinuate myself into people's lives to prey on their weakness and secure their fortunes.",
        "I shave coins or forge documents.",
        "I cheat at games of chance.",
        "I must be the captain of any group I join.",
        "Any defeat or failure on my part is because my opponents cheated.",
        "I have lingering pain of old injuries.",
        "I ignore anyone who doesn't compete and anyone who loses to me.",
        "I'll do absolutely anything to win.",
        "I indulge in a habit that threatens my reputation or health.",
        "I strive to live up to a specific hero's example.",
        "The person who trained me is the most important person in my world.",
        "My teammates are my family.",
        "I get irritated if people praise someone else and not me.",
        "Anything worth doing is worth doing best.",
        "I love to trade banter and gibes.",
        "When I see others struggling, I offer to help.",
        "Obstacles exist to be overcome.",
        "I have a daily exercise routine I refuse to break.",
        "I don't like to sit idle.",
        "I feel most at peace during physical exertion, whether exercise or battle.",
        "I can't sleep except in total darkness.",
        "When given the choice of going left or right, I always go left.",
        "I have no time for friends or family. I spend every waking moment thinking about and preparing for my next expedition.",
        "When I'm not exploring dungeons or ruins, I get jittery and impatient.",
        "I can't leave a room without searching it for secret doors.",
        "I have a secret fear of some common wild animal – and in my work, I see them everywhere.",
        "You might think I'm a scholar, but I love a good brawl. These fists were made for punching.",
        "I might fail, but I will never give up.",
        "I have no qualms about stealing from the dead.",
        "I love a good puzzle or mystery.",
        "I'm a pack rat who never throws anything away.",
        "I wear a tribal mask and never take it off.",
        "I complain about everything.",
        "I've picked up some unpleasant habits living among races such as goblins, lizardfolk, or orcs.",
        "I believe that I'm intellectually superior to people from other cultures and have much to teach them.",
        "Boats make me seasick.",
        "I talk to myself, and I don't make friends easily.",
        "When I arrive at a new settlement for the first time, I must learn all its customs.",
        "I would risk life and limb to discover a new culture or unravel the secrets of a dead one.",
        "By living among violent people, I have become desensitized to violence.",
        "I would rather observe than meddle.",
        "I prefer the company of those who aren't like me, including people of other races.",
        "I'm a stickler when it comes to observing proper etiquette and local customs.",
        "I judge others harshly, and myself even more severely.",
        "I put too much trust in those who wield power within my temple's hierarchy.",
        "My piety sometimes leads me to blindly trust those that profess faith in my god.",
        "I am inflexible in my thinking.",
        "I am suspicious of strangers and expect the worst of them.",
        "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.",
        "Adaptable: Shows flexibility and versatility regardless of the situation. Thinks quickly.",
        "Since no one else is stepping up, I will.",
        "Adventurous. Willing to try new experiences and take risks.",
        "Affectionate: Shows open fondness for others",
        "Compassionate. Will prevent damage to others. ",
        "In Alert. Aware of and watchful for possible change or danger.",
        "They plan ahead. Always having an exit strategy", 
        "They are highly observant",
        "They are Ambitious.",
        "They are Confident and prideful",
        "They are Analytical, Logical, Rational.",
        "They are highly curious.",
        "They fear making a mistake.",
        "They are bold and intrepid.",
        "They desire to prove oneself",
        "They are driven by a strong sense of righteousness The belief in a higher power or purpose",
        "They are calmed, and inclined toward tranquility and serenity",
        "They have a higher purpose.",
        "They have a boring personality.",
        "They enjoy simple pleasures",
        "I am cautious, given to prudent forethought before acting.",
        "They are wise.",
        "They are charming",
        "They are confident, fully assured of themself",
        "They are cooperative.",
        "They are courageous.",
        "They are courteous, friendly, and have good maners.",
        "They are curious. Marked by the desire to investigate and learn",
        "They have the ability to make quick, efficient decisions; lacking hesitation.",
        "They are diplomatic: Skilled at handling people while respecting their needs",
        "They are disciplined: Exhibiting willpower and self-control.",
        "They are strongly dedicated to a goal or belief",
        "They are Carefree and relaxed.",
        "They are enthusiastic: Frequently feeling or exhibiting much excitement.",
        "They are generous, altruistic, philanthropic.",
        "They are harsh, brusque, and violent.",
        "They are honorable, having noble principles and displaying integrity.",
        "They are passionate, capable of or expressing deep feeling.",
        "They are patient. Exhibiting self-control and composure under trial or strain.",
        "They are patriotic. Having love for or loyalty to their country.",
        "They are persistent: Stubbornly continuing on despite opposition, difficulty, or danger.",
        "They are playful, immature, and cheerful.",
        "They are protective.",
        "Traps don't make me nervous. Idiots who trigger traps make me nervous.",
        "I'm happier in a dusty old tomb than I am in the centers of civilization.",
        "Fame is more important to me than money.",
        "I pursue wealth to secure someone's love.",
        "I'll do anything to get my hands on something rare or priceless.",
        "I'm quick to assume that someone is trying to cheat me.",
        "I'm never satisfied with what I have – I always want more.",
        "I would kill to acquire a noble title.",
        "My faction is my family. I would do anything for it.",
        ""
        ]
        
    if background == "Expert":
        return random.choice(Traits + [
            "I'm horribly jealous of anyone who can outshine my handiwork. Everywhere I go, I'm surrounded by rivals.",
            "No one must ever learn that I once stole money from guild coffers.",
            "One day I will return to my guild and prove that I am the greatest artisan of them all.",
            "The workshop where I learned my trade is the most important place in the world to me.",
            "I created a great work for someone, and then found them unworthy to receive it. I'm still looking for someone worthy.",
            "I owe my guild a great debt for forging me into the person I am today.",
            "I will get revenge on the evil forces that destroyed my place of business and ruined my livelihood."
            ])
        
    if background == "Priest" or background == "Cultist":
        return random.choice(Traits + [
            "I was partaking of communal living in accordance with the dictates of a religious order.",
            "They idolize a particular hero of my faith, and constantly refer to that person's deeds and example.",
            "I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.",
            "I see omens in every event and action. The gods try to speak to us, we just need to listen.",
            "Nothing can shake my optimistic attitude.",
            "I quote (or misquote) sacred texts and proverbs in almost every situation.",
            "I am tolerant  of other faiths and respect the worship of other gods.",
            "I am intolerant of other faiths and condemn the worship of other gods.",
            "I've enjoyed fine food, drink, and high society among my temple's elite. Rough living grates on me.",
            "I've spent so long in the temple that I have little practical experience dealing with people in the outside world.",
            "Nothing is more important than the other members of my hermitage, order, or association.",
            ""]) 
    if background=="Bard":
        return random.choice( Traits + [
            "My instrument is my most treasured possession, and it reminds me of someone I love."
            ])


    return random.choice(Traits)
    



def Ideal(background, alignment):
    
    if background == "Priest":
        if "Lawful" in alignment and Dice()==1:
            return random.choice([
                "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld.",
                "Faith. I trust that my deity will guide my actions. I have faith that if I work hard, things will go well."
                ])
        if "Good" in alignment and Dice()==1:
            return random.choice( 
                ["Charity. I always try to help those in need, no matter what the personal cost."
                ])
        if "Chaotic" in alignment and Dice()==1:
            return random.choice([
                "Change. We must help bring about the changes the gods are constantly working in the world."
                ])

    if background == "Charlatan":
        if "Chaotic" in alignment and Dice()==1:
            return random.choice([
                "Independence. I am a free spirit – no one tells me what to do.",
                "Creativity. I never run the same con twice."
                ])
        if "Lawful" in alignment and Dice()==1:
            return random.choice([
                "Fairness. I never target people who can't afford to lose a few coins."
                ])
        if "Good" in alignment and Dice()==1:
            return random.choice([
                "Fairness. I never target people who can't afford to lose a few coins.",
                "Charity. I distribute the money I acquire to the people who really need it.",
                "Friendship. Material goods come and go. Bonds of friendship last forever."
                ])
    if background == "Commoner":
        if "Good" in alignment and Dice()==1:
            return random.choice([
                "Camaraderie. Good people make even the longest voyage bearable."
                ])
        if "Lawful" in alignment and Dice()==1:
            return random.choice([
                "Luck. Our luck depends on respecting its rules—now throw this salt over your shoulder."
                ])
        if "Chaotic" in alignment and Dice()==1:
            return random.choice([
                "Daring. The richest bounty goes to those who risk everything."
                ])
        if "Neutral" in alignment and Dice()==1:
            return random.choice([
                "Balance. Do not fish the same spot twice in a row; suppress your greed, and nature will reward you."
                ])
                
    if background == "Criminal":
        if "Lawful" in alignment and Dice()==1:
            return random.choice([
                "Honor. I don't steal from others in the trade.",
                ])
        if "Chaotic" in alignment and Dice()==1:
            return random.choice([
                "Freedom. Chains are meant to be broken, as are those who would forge them.",
                ])
        if "Good" in alignment and Dice()==1:
            return random.choice([
                "Charity. I steal from the wealthy so that I can help people in need.",
                "Redemption. There's a spark of good in everyone",
                ])
        if "Evil" in alignment and Dice()==1:
            return random.choice([
                "Greed. I will do whatever it takes to become wealthy.",
                "Plunder. Take all that you can and leave nothing for the scavengers.",
                ])
        if "Neutral" in alignment and Dice()==1:
            return random.choice([
                "People. I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care."
                ])
                
                
    if background == "Gladiator":
        if "Chaotic" in alignment and Dice()==1:
            return random.choice([
                "Competition. I strive to test myself in all things."
                ])
        if "Evil" in alignment and Dice()==1:
            return random.choice([
                "Triumph. The best part of winning is seeing my rivals brought low."
                ])
        if "Good" in alignment and Dice()==1:
            return random.choice([
                "Camaraderie. The strongest bonds are forged through struggle."
                ])
        if "Neutral" in alignment and Dice()==1:
            return random.choice([
                "People. I strive to inspire my spectators."
                ])
        if "Lawful" in alignment and Dice()==1:
            return random.choice([
                "Tradition. Every game has rules, and the playing field must be level."
                ])
                
    if background == "Scholar":
        if "Lawful" in alignment and Dice()==1:
            return random.choice( 
                ["Distance. One must not interfere with the affairs of another culture – even one in need of aid.", 
                "Power. Common people crave strong leadership, and I do my utmost to provide it.",
                "Dignity. The dead and their belongings deserve to be treated with respect."
                ])
        if "Good" in alignment and Dice()==1:
            return random.choice( 
                ["Protection. I must do everything possible to save a society facing extinction.",
                "Preservation. That artifact belongs in a museum."
                ])
        if "Evil" in alignment and Dice()==1:
            return random.choice([
                "Indifferent. Life is cruel. What's the point in saving people if they're going to die anyway?"
                ])
        if "Chaotic" in alignment and Dice()==1:
            return random.choice([
                "Death Wish. Nothing is more exhilarating than a narrow escape from the jaws of death."
                ])
                
    if background=="Bard":
        if "Good" in alignment and Dice()==1:
            return random.choice([
                "Beauty. When I perform, I make the world better than it was."
                ])
        if "Lawful" in alignment and Dice()==1:
            return random.choice([
                "Tradition. The stories, legends, and songs of the past must never be forgotten, for they teach us who we are."
                ])
        if "Chaotic" in alignment and Dice()==1:
            return random.choice([
                "Creativity. The world is in need of new ideas and bold action."
                ])
        if "Evil" in alignment and Dice()==1:
            return random.choice([
                "Greed. I'm only in it for the money and fame."
                ])
        if "Neutral" in alignment and Dice()==1:
            return random.choice([
                "People. I like seeing the smiles on people's faces when I perform. That's all that matters."
                ])               
        if Dice()==1:
            return random.choice([
                "Honesty. Art should reflect the soul; it should come from within and reveal who we really are."
                ])   

    if background == "Traveler":
        if "Good" in alignment and Dice()==1:
            return random.choice([
                "Open. I have much to learn from the kindly folk I meet along my way."
                ])
        if "Lawful" in alignment and Dice()==1:
            return random.choice([
                "Reserved. As someone new to these strange lands, I am cautious and respectful in my dealings."
                ])
        if "Chaotic" in alignment and Dice()==1:
            return random.choice([
                "Wanderlust. I prefer to take the less traveled path",
                "Adventure. I'm far from home, and everything is strange and wonderful!"
                ])
        if "Evil" in alignment and Dice()==1:
            return random.choice([
                " Cunning. Though I may not know their ways, neither do they know mine, which can be to my advantage."
                ])
        if "Neutral" in alignment and Dice()==1:
            return random.choice([
                "Inquisitive. Everything is new, but I have a thirst to learn."
                ])


    if "Good" in alignment and Dice()==1:
        return random.choice([
            "Common Good. My organization serves a vital function, and its prosperity will help everyone.",
            "Greater Good. My gifts are meant to be shared with all, not used for my own benefit.",
            "Greater Good. I kill monsters to make the world a safer place, and to exorcise my own demons.",
            "Selflessness. I try to help those in need, no matter what the personal cost.",
            "Generosity. My talents were given to me so that I could use them to benefit the world.",
            "Empathy. No creature should be made to suffer.",
            "Respect. People deserve to be treated with dignity and respect.",
            "Friendship. I never leave a friend behind. "
            ])
    if "Chaotic" in alignment and Dice()==1:
        return random.choice([
            "Innovation. Abandon old traditions and find better ways to do things.",
            "Free Thinking. Inquiry and curiosity are the pillars of progress.",
            "Freedom. I have a dark calling that puts me above the law.",
            "Freedom. Everyone should be free to pursue his or her own livelihood.",
            "Freedom. Tyrants must not be allowed to oppress the people.",
            "Changeability. Change is good, which is why I live by an ever-changing set of rules."
            ])
    if "Lawful" in alignment and Dice()==1:
        return random.choice([
            "Tradition. I uphold traditions of my house and bring honor to my family.",
            "Logic. Emotions must not cloud our sense of what is right and true, or our logical thinking.",
            "Logic. I like to know my enemy’s capabilities and weaknesses before rushing into battle.",
            "Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization.",
            "Fairness. No one should get preferential treatment before the law, and no one is above the law.",
            "Honor. A deal is a deal, and I would never break one."
            ])
    if "Evil" in alignment and Dice()==1:
        return random.choice([
            "Power. I want to ensure the prosperity of my house and wield its power myself.",
            "Destruction. I’m a monster that destroys other monsters, and anything else that gets in my way.",
            "Greed. I'm only in it for the money.",
            "Might. If I become strong, I can take what I want – what I deserve.",
            "Obsession. I won't let go of a grudge",
            "Greed. I will do whatever it takes to get what I want, regardless of the harm it might cause.",
            "Confusion. Deception is a weapon. Strike from where your foes won't expect."
            ])
    if "Neutral" in alignment and Dice()==1:
        return random.choice([
            "People. I'm committed to the people I care about, not to ideals.",
            "Danger. With every great discovery comes grave danger. The two walk hand in hand.",
            "Sincerity. There's no good in pretending to be something I'm not."
            ])    
    return random.choice([
        "Comfort. I want to ensure that me and mine enjoy the best things in life.",
        "Discovery. I want to learn all I can, both for my organization and for my own curiosity.",
        "Self-Knowledge. If you know yourself, there's nothing left to know.",
        "Live and Let Live. Meddling in the affairs of others only causes trouble.",
        "Power. Solitude and contemplation are paths toward mystical or magical power.",
        "Determination. I’ll stop the spirits that haunt me or die trying.",
        "Aspiration. I work hard to be the best there is at my craft.",
        "Suspicious. I must be careful, for I have no way of telling friend from foe here.",
        "Destiny. Nothing and no one can steer me away from my higher calling.",
        "Anonymity. It's my deeds that should be remembered, not their instrument.",
        "Incorruptibility. Be a symbol, and leave your flawed being behind.",
        "Infamy. My name will be a malediction, a curse that fulfills my will.",
        "Security. Doing what must be done can't bring the innocent to harm.",
        "Justice. Place in society shouldn't determine one's access to what is right. ",
        "Discovery. I want to be the first person to discover a lost culture.",
        "Knowledge. By understanding other races and cultures, we learn to understand ourselves.",
        "Immortality. All my exploring is part of a plan to find the secret of everlasting life.",
        "Aspiration. I seek to prove myself worthy of my god's favor by matching my actions against their teachings.",
        "Greed. I won't risk my life for nothing. I expect some kind of payment.",
        "Growth. Lessons hide in victory and defeat",
        "Aspiration. I'm determined to make something of myself.",
        "Hard Work. No wave can move a soul hard at work.",
        ""
        ])
                

    
    
    
    
    
    
def NPC():
    """NPC creator"""
    STR = AbilityScore()
    DEX = AbilityScore()
    CON = AbilityScore()
    INT = AbilityScore()
    WIS = AbilityScore()
    CHA = AbilityScore()
    
    bg = Background()
    
    Lvl = Dice(30)
    rc = Race()
    nm = Name(rc)
    al = Alignment()
    
    if rc == "Giant": STR += Dice(12)
    if rc == "Fey": CHA += Dice(12)
    if rc == "Human": 
        STR += Dice(2)
        DEX += Dice(2)
        CON += Dice(2)
        INT += Dice(2)
        WIS += Dice(2)
        CHA += Dice(2)
    if rc == "Aberration": CON += Dice(12)
    if rc == "Aven": DEX += Dice(12)
    if rc == "Beast": CON += Dice(12)
    if rc == "Beastfolk":
        CON += Dice()
        WIS += Dice()
    if rc == "Celestial":
        WIS += Dice()
        CHA += Dice()
    if rc == "Construct":
        STR += Dice()
        CON += Dice()
    if rc == "Dragon": 
        STR += Dice()
        DEX += Dice()
        CON += Dice()
        INT += Dice()
        WIS += Dice()
        CHA += Dice()
    if rc == "Dwarf": 
        STR += Dice(4)
        CON += Dice(4)
        WIS += Dice(4)
    if rc == "Elf":
        DEX += Dice(4)
        INT += Dice(4)
        WIS += Dice(4)
    if rc == "Elemental":
        CON += Dice(6)
        WIS += Dice(6)
    if rc == "Fiend": CHA += Dice(12)
    if rc == "Genasi":
        CON += Dice(6)
        WIS += Dice(6)
    if rc == "Gnome":
        DEX += Dice(4)
        INT += Dice(4)
        CHA += Dice(4)
    if rc == "Goblin":
        DEX += Dice(4)
        INT += Dice(4)
        CHA += Dice(4)
    if rc == "Hag":
        CON += Dice(3)
        INT += Dice(3)
        WIS += Dice(3)
        CHA += Dice(3)
    if rc == "Halfling":
        DEX += Dice(4)
        INT += Dice(4)
        CHA += Dice(4)
    if rc == "Kobold":
        DEX += Dice()
        INT += Dice()
    if rc == "Lizardfolk":
        STR += Dice(2)
        DEX += Dice(2)
        CON += Dice(2)
        INT += Dice(2)
        WIS += Dice(2)
        CHA += Dice(2)
    if rc == "Monstrosity":
        STR += Dice()
        CON += Dice()
    if rc == "Ooze":
        CON += Dice(12)
    if rc == "Orc":
        STR += Dice(3)
        DEX += Dice(2)
        CON += Dice(3)
        WIS += Dice(2)
        CHA += Dice(2)
    if rc == "Plant":
        STR += Dice(4)
        CON += Dice(4)
        WIS += Dice(4)
    if rc == "Snakefolk":
        DEX += Dice(4)
        CON += Dice(4)
        INT += Dice(4)
    if rc == "Tiefling":
        CON += Dice(3)
        INT += Dice(3)
        WIS += Dice(3)
        CHA += Dice(3)
    if rc == "Undead":
        STR += Dice(4)
        CON += Dice(4)
        CHA += Dice(4)
    
    print(Title())
    print("-", al, "- ", random.choice(["♀", "♂", "⚥", "⚬", "?", ""]))
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
    print("SPELLCASTING:\t", random.choice(["INT","WIS","CHA"])  ,"\n\t Spellsave DC:", 10+ Modifier(max(INT,WIS,CHA)) )
    print("\t To hit: +", Modifier(max(INT,WIS,CHA)+ Lvl/5))
    print(Magic(Lvl,rc,bg))
    
    print("\n\n")
    print(Actions(bg))
    print(Actions(rc))
    print(Actions(""))
    print("\n")

    if Dice(Lvl) >= 15:
        print("\nLEGENDARY ACTIONS:")
        print(Legendary(bg))
        print(Legendary(rc))

        print("\nLAIR ACTIONS:")
        print(Lair(bg))
        print(Lair(rc))

        print("\nREGIONAL EFFECTS:")
        print(Region(bg))
        print(Region(rc))


    print("========== Their Story ===========")
    print(" - Traits -")
    print(Trait())
    print(Trait(bg))
    print(" - Ideal -")
    print(Ideal(bg,al))    
    print(" - Story Hook -")
    print(PlotHook())

NPC()
