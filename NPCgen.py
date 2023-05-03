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
        "The Brain",
        "The Bringer",
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
        "The Trival",
        "The Undead",
        "The Unicorn",
        "The Vampiric",
        "The Veteran",
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
        "Vandit",
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
        "Beast", "Beast", "Beast"
        "Beastfolk", "Beastfolk"
        "Celestial", 
        "Construct",
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
        "Kobold",
        "Lizardfolk",
        "Merfolk",
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
        "Baboon",
        "Badger",
        "Bat",
        "Blood Hawk",
        "Boar",
        "Cat",
        "Camel",
        "Dino", "TRex", "Triceratops", "Velocirraptor",
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
        "Tiger", "Sabertooth",
        "Vulture",
        "Wolf",
        ""]
    return random.choice(Names)
    
def BeastfolkName():
    Names = [
        "Centaur",
        "Lycan", 
        "Minotaur",
        "Werewolf",
        ""]
    return random.choice(Names)

def ConstructName():
    Names = [
        "Drone",
        "Homunculus",
        "Flying Sword",
        "Living Rug",
        ""]
    return random.choice(Names)

def DragonName():
    Names = [
        ""]
    return random.choice(Names)

def FiendName():
    Names = [
        "Devil",
        "Demon",
        ""]
    return random.choice(Names)

def FeyName():
    Names = [
        "Pixie",
        ""]
    return random.choice(Names)

def MonstrosityName():
    Names = [
        "Griffon",
        ""]
    return random.choice(Names)


def PlantName():
    Names = [
        "Awakened Plant",
        "Myconid",
        "Willow"
        ""]
    return random.choice(Names)
    
def UndeadName():
    Names = [
        "Crawling Limb",
        "Vampire"
        ""]
    return random.choice(Names)
    
    
def Name(Type):
    if Type == "Aberration": return AberrationName()
    if Type == "Aven": return AvenName()
    if Type == "Beast": return BeastName()
    if Type == "Beastfolk": return BeastfolkName()
    if Type == "Construct": return ConstructName()
    if Type == "Dragon": return DragonName()
    if Type == "Dragonborn": return DragonName()
    if Type == "Fey": return FeyName()
    if Type == "Fiend": return FiendName()
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
    return d1+d2+d3+d4 - min(d1,d2,d3,d4) + Dice(3)-1 + Dice(8)-Dice(8)
    
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
        return random.choice(["Blinded","Exhaustion", "Incapacitated", "Poisoned" ])
    elif dmg == "Bludgeoning":
        return random.choice(["Blinded","Deafened","Exhaustion", "Incapacitated", "Prone", "Stunned","Uncoscious" ])
    elif dmg == "Poison":
        return random.choice(["Blinded", "Charmed", "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Restrained", "Unconscious"])
    elif dmg == "Acid":
        return random.choice(["Blinded", "Exhaustion", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Restrained","Unconscious"])
    elif dmg == "Fire":
        return random.choice(["Blinded", "Charmed", "Incapacitated", "Paralyzed", "Stunned", "Unconscious"])
    elif dmg == "Cold":
        return random.choice(["Exhaustion", "Incapacitated", "Paralyzed", "Petrified", "Restrained"])
    elif dmg == "Radiant":
        return random.choice(["Blinded", "Charmed", "Deafened", "Frightened", "Incapacitated", "Paralyzed", "Prone", "Stunned", "Unconscious"])
    elif dmg == "Necrotic":
        return random.choice([ "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Lightning":
        return random.choice(["Blinded", "Charmed", "Deafened", "Exhaustion", "Frightened", "Grappled", "Incapacitated", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Force":
        return random.choice(["Blinded","Deafened", "Exhaustion", "Incapacitated", "Prone", "Stunned", "Unconscious" ])
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



































def Magic(Lvl, race = Race(), background = Background()):

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

    for L in range(Lvl):

                
                
        if background == "Acolyte":
            if Dice(2) == 1:
                cantrip +=  "\t light"
            if Dice(2) == 1:
                cantrip +=  "\t sacred flame"
            if Dice(2) == 1:
                cantrip +=  "\t thaumaturgy"
            slots1 += Dice(3)
            if Dice(2) == 1:
                first += "\t bless"
            if Dice(2) == 1:
                first += "\t cure wounds"            
            if Dice(2) == 1:
                first += "\t sanctuary"            
    
    
        if background == "Cultist":
            if Dice(2) == 1:
                cantrip +=  "\t Light"
            if Dice(2) == 1:
                cantrip += "\t Sacred flame"
            if Dice(2) == 1:
                cantrip += "\t Thaumaturgy" 
            slots1 += Dice(4)
            if Dice(2) == 1:
                first += "\t Command"
            if Dice(2) == 1:
                first += "\t inflict wounds"
            if Dice(2) == 1:
                first += "\t shield of faith"
            slots2 += Dice(3)
            if Dice(2) == 1:
                second += "\t hold person" 
            if Dice(2) == 1:
                second += "\t spiritual weapon"

        if background=="Healer":
            if Dice(2) == 1:
                cantrip +=  "\t guidance" 
            if Dice(2) == 1:
                cantrip +=  "\t sacred flame"
            slots1 += Dice(2)
            if Dice(2) == 1:
                first +=  "\t cure wounds"
            
        if background == "Mage":
            if Dice(2) == 1:
                cantrip +=  "\t firebolt" 
            if Dice(2) == 1:
                cantrip +=  "\t light" 
            slots1 += Dice(2)
            if Dice(2) == 1:
                first +=  "\t Sleep"
    
        if background == "Priest":
            if Dice(2) == 1:
                cantrip += "\t Guidance"
            if Dice(2) == 1:
                cantrip += "\t Light"
            if Dice(2) == 1:
                cantrip += "\t Sacred Flame"
            if Dice(2) == 1:
                cantrip += "\t Thaumaturgy"
                
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
            if Dice() == 1:
                cantrip +=  "\n- Summon Air Elemental. \n\t Five aarakocra within 30 feet of each other can magically summon an air elemental. Each of the five must use its action and movement on three consecutive turns to perform an aerial dance and must maintain concentration while doing so (as if concentrating on a spell). When all five have finished their third turn of the dance, the elemental appears in an unoccupied space within 60 feet of them. It is friendly toward them and obeys their spoken commands. It remains for 1 hour, until it or all its summoners die, or until any of its summoners dismisses it as a bonus action. A summoner can't perform the dance again until it finishes a short rest. When the elemental returns to the Elemental Plane of Air, any aarakocra within 5 feet of it can return with it."
                
        if race == "Celestial":
            if Dice(2) == 1:
                cantrip +=  "\t light" 
            if Dice(2) == 1:
                cantrip +=  "\t sacred flame" 
            if Dice(2) == 1:
                cantrip +=  "\t thaumaturgy" 
            slots1 += Dice(3)
            if Dice(2) == 1:
                first +=  "\t bless" 
            if Dice(2) == 1:
                first +=  "\t cure wounds" 
            if Dice(2) == 1:
                first +=  "\t sanctuary"
                
        if race == "Elf":
            if Dice() == 1:
                cantrip += "\t dancing lights"
            if Dice() == 1:
                one += "\t darkness"
            if Dice() == 1:
                one += "\t faerie fire"
                
        if race == "Fey":
            if Dice() == 1:
                cantrip += "\t Teleport (Recharge 4–6). \n\t The Fey magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the dog can make one bite attack."
            if Dice(3) == 1:
                cantrip += "\t druidcraft"
            if Dice() == 1:
                one += "\t confusion"
            if Dice() == 1:
                one += "\t dancing lights"
            if Dice() == 1:
                one += "\t detect evil and good"   
            if Dice() == 1:
                one += "\t detect thoughts"   
            if Dice() == 1:
                one += "\t dispel magic"   
            if Dice() == 1:
                one += "\t entangle"   
            if Dice() == 1:
                one += "\t fly"   
            if Dice() == 1:
                one += "\t phantasmal force"   
            if Dice() == 1:
                one += "\t polymorph"   
            if Dice() == 1:
                one += "\t sleep"   

                
        if Dice(10) == 1: 
            background = Background()
        if Dice(10) == 1: 
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
























def Actions():
    r = ""

    if Type == "Dragon":
        r = r+ "\n- Flight"

    if Type == "Dragon":
        r = r+ "\n- Language: Draconic"

    if Type == "Dragon":
        if Dice(2) == 1:
            r = r+ "\n- Darkvision \n\t 60 ft"

    if Type == "Dragon":
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
            
    if Type == "Dragon":
        if Dice(2) == 1:
            r = r + "\n - Amphibious"

    if Type == "Dragon":
        if Dice() == 1:
            r = r + "\n - Blindsight \n\t 10 ft"

    if Type == "Dragon": 
        if Dice(2) == 1:
            r = r+ "\n- Keen Senses \n\t The Dragon has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell."
            
    if Type == "Dragon": 
        if Dice(2) == 1:
            r = r+ "\n- Limited Telepathy \n\t The Dragon can magically communicate simple ideas, emotions, and images telepathically with any creature within 100 feet of it that can understand a language."
            
    if Type == "Dragon": 
        if Dice(2) == 1:
            r = r+ "\n- Magic Resistance \n\t The Dodragon has advantage on saving throws against spells and other magical effects."           
            
    if Type == "Fey": 
        if Dice(2) == 1:
            r = r+ "\n- Magic Resistance \n\t The Fae has advantage on saving throws against spells and other magical effects."

    if Type == "Fey": 
        if Dice(2) == 1:
            r = r+ "\n- Superior Invisibility \n\t  The Fae magically turns invisible until its concentration ends (as if concentrating on a spell). Any equipment the Fae wears or carries is invisible with it."


    if Type == "Nymph": 
        r = r+ "\n- Teleport"
        r = r+ "\n- Magic Resistance"
        r = r+ "\n- Speak with Beasts and Plants"
        r = r+ "\n- At will: druidcraft\n 3/day each: entangle, goodberry \n 1/day each: barkskin, pass without trace, shillelagh"
        r = r+ "\n- Fey Charm"
        
        
    if Type == "Beast" or Type == "Beastfolk": 
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
        if Dice(8) == 1:
            r = r+ "\n - Pounce \n\t If the beast moves at least 20 feet straight toward a creature and then hits it with an attack on the same turn, that target must succeed on a DC [10+%STR] Strength saving throw or be knocked prone. If the target is prone, the Beast can make one attack against it as a bonus action."
        if Dice(8) == 1:
            r = r+ "\n- Illumination.\n\tThe beast sheds bright light in a 10-foot radius and dim light for an additional 10 ft."
        if Dice(8) == 1:
            r = r+ "\n-Sure-Footed \n\t The beast has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
        if Dice() == 1:
            r = r + "\n- Hold Breath. \n\t The beast can hold its breath for 30 minutes."
        if Dice(8) == 1:
            r = r+ "\n- Mimicry \n\t The Raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."
        if Dice(8) == 1:
            r = r+ "\n- Beast of Burden \n\t The mule is considered to be a Large animal for the purpose of determining its carrying capacity."
        if Dice(8) == 1:
            r = r+ "\n- Swamp Camouflage \n\t The Beast has advantage on Dexterity (Stealth) checks made to hide in swampy terrain."
        if Dice(4) == 1:
            r = r+ "\n- Bite. \n\t  Melee Weapon Attack: reach 5 ft., one target. Hit: 4 (1d6 + %STR) piercing damage, and the target is grappled (escape DC 10 + %STR). Until this grapple ends, the target is restrained, and the beast can't bite another target."
            if Dice() == 1:
                r = r+ "\n- Swallow. \n\t  The beast makes one bite attack against a target creature smaller than themselves it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the beast, and it takes 6 (2d4+%CON) acid damage at the start of each of the beast's turns. The beast can have only one target swallowed at a time. If the beast dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 feet of movement, exiting prone."
            if Dice(12) == 1:
                r = r+ "\n-  Hold Breath. \n\t  The beast can hold its breath for 15 minutes.\n-  swimming \n\t  speed of 30 feet.)"
                r = r+ "\n-  Spider Climb. \n\t  The beast can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
            
    if Type == "Beastfolk":
        r = r + "\n- Speak with Animal \n\t The Beastfolk can communicate simple concepts to his affinity animal when it speaks in Beast language."

    if Type == "Elf" or Type == 6:
        r = r+ "\nFey Ancestry.\n\t The Elf has advantage on saving throws against being charmed, and magic can't put the Elf to sleep."
        
        if Dice(4) <= 3:
            r = r+ "\n Darkvision \n\t 60ft"
        else:
            r = r+ "\n Darkvision \n\t 120ft"
            r = r+ "\nSunlight Sensitivity. \n\t While in sunlight, the Elf has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."


    if Type == "Aven(Birdfolk)" or Type == 7:
        r = r+ "\n- Fly \n\t 50ft"
        
    if Type == "Construct" or Type == 8:
        r = r+ "\n- Damage Immunities: Poison"
    if Type == "Construct" or Type == 9:
        r = r+ "\n- Condition Immunities: Poisoned, Charmed"
    if Type == "Construct" or Type == 10:
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
            r = r+ "\n Condition Immunities: paralyzed \n"
        if Dice()==1:
            r = r+ "\n Condition Immunities: charmed \n"
        if Dice()==1:
            r = r+ "\n- Axiomatic Mind. \n\t The Construct can't be compelled to act in a manner contrary to its nature or its instructions."
        if Dice() == 1:
            r = r+"\n- Disintegration. \n\t If the Construct dies, its body disintegrates into dust, leaving behind its weapons and anything else it was carrying."
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

    if Type == "Goblin" or Type == 9:
        r = r+ "\n- Nimble Scape \n\t The goblin can take the Disengage or Hide action as a bonus action on each of its turns."
        
    if Type == "Aberration" or Type == 10:
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
        if Dice()==1: 
            r = r+ "\n- Telepathy: \n\t 60ft"
            if Dice(3)==1:
                r = r+ "\n-Advanced Telepathy: \n\t The Aberration can perceive the content of any telepathic communication used within 60 feet of it, and it can't be surprised by creatures with any form of telepathy."
            if Dice(3)==1:
                r = r+ "\n-Telepathic Shroud. \n\t The Aberration is immune to any effect that would sense its emotions or read its thoughts, as well as all divination spells."
        if Dice(2)==1: 
            r = r+ "\n- Detect Sentience: \n\t It can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by a mind blank spell."
            if Dice()==1: 
                r = r+ "\n- Devour Intellect: \n\t It targets one creature it can see within 10 feet of it that has a brain. The target must succeed on a DC [10+%DEX] Intelligence saving throw against this magic or take 11 (2d10) psychic damage. Also on a failure, roll 3d6: If the total equals or exceeds the target's Intelligence score, that score is reduced to 0. The target is stunned until it regains at least one point of Intelligence."
        if Dice(2)==1: 
            r = r+ "\n- Body Thief. \n\t The intellect devourer initiates an Intelligence contest with an incapacitated humanoid within 5 feet of it that isn't protected by protection from evil and good. If it wins the contest, the intellect devourer magically consumes the target's brain, teleports into the target's skull, and takes control of the target's body. While inside a creature, the intellect devourer has total cover against attacks and other effects originating outside its host. The intellect devourer retains its Intelligence, Wisdom, and Charisma scores, as well as its understanding of Deep Speech, its telepathy, and its traits. It otherwise adopts the target's statistics. It knows everything the creature knew, including spells and languages. \n\t If the host body dies, the intellect devourer must leave it. A protection from evil and good spell cast on the body drives the intellect devourer out. The intellect devourer is also forced out if the target regains its devoured brain by means of a wish. By spending 5 feet of its movement, the intellect devourer can voluntarily leave the body, teleporting to the nearest unoccupied space within 5 feet of it. The body then dies, unless its brain is restored within 1 round."
        if Dice() == 1:
            r = r+ "\n- Damage Vulnerabilities: \n\t psychic"

        if Dice() == 1:
            r = r+ "\n- Magic Resistance: \n\t The Aberration has advantage on saving throws against spells and other magical effects."
        
    elif Type == "Aven(Birdfolk)" or Type == 14:
        r = r+ "\n- Ambusher"
        r = r+ "\n- Mimicry \n\t The Raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."
        
        
    elif Type == "Elemental" or Type == 15:
        r = "\n- False Appereance \n- Death Burst \n- Damage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks"
        rdm = Dice(4)
        if rdm == 1:
            r = "\n- Heated Body \n- Damage Immunities: fire  \n- Damage Vulnerabilities: cold"
        
    elif Type == "Fey":
        if Dice() == 1:
            r = r + "\n - Invisibility"
            
    elif Type == "Fey":
        if Dice() == 1:
            r = r + "\n - Heart Sight"
            
    elif Type == "Fey":
        if Dice() == 1:
            r = r + "\n -  Teleport (Recharge 4–6). \n\t The Fey magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the Fey can make one attack."

    elif Type == "Assassin":
        r =+ "\n- Superior Invisibility"
        
    elif Type == "Undead":
        r = r + "\nDamage Immunities: poison"+"\n Condition Immunities: exhaustion, poisoned, charmed"
        
    elif Type == "Undead":
        if Dice(2) == 1:
            r = r + "\n - Undead Fortitude"
            
    elif Type == "Undead":
        if Dice(2) == 1:
            r = r + "\n -Stench"

    elif Type == "Undead":
        if Dice(2) == 1:
            r = r + "\n -Turn Defiance"

    elif Type == "Undead":
        if Dice() == 1:
            r = r + "\n - Turn Immunity \n\t The Undead is immune to effects that turn undead."


    elif Type == "Lizardfolk":
        r = r+"\n\n- Hold Breath"
        if Dice(2) == 1:
            r = r + "\n - Chameleon Skin \n\t The lizard can hold its breath for 15 minutes. (A lizard that has this trait also has a swimming speed of 30 feet.)"
        if Dice(2) == 1:
            r = r + "\n -  Spider Climb. \n\t The lizard can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
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

    elif Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- False Appearance"
    elif Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Engulf"
    elif Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Gelatinous Cube"
    elif Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Transparent"
    elif Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Spider Climb"
    elif Type == "Ooze":
        if Dice() == 1:
            r = r+ "\n- Split(Yellow): Lightning or Slashing"

    elif Type == "Hobgoblin" or Type == 24:
        r = r+"\n- Martial Advantage"
        
    elif Type == "Lycan" or Type ==25:
        r = r+ "\n- Shapechanger"
        r = r+"\n- Pack Tactics"
        
    elif Type == "Orc" or Type == 25:
        r = r+ "\n- Aggressive"
        
    elif Type == 26:
        r = r + "\n- Blood Frenzy"
    
    elif Type == "Scout" or Type == 27:
        r = r+ "\n- Keen Senses\n\t The beast has advantage on Wisdom (Perception) checks that rely on senses."   
        
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
            r = r+ "\n Condition Immunities: charmed"
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r+ "\n Condition Immunities:   poisoned"

        
    elif Type == "Spirit":
        if Dice(2) == 1:
            r = r+"\n- Damage Resistances: acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks"

    elif Type == "Spirit":
        if Dice(2) == 1:
            r = r+"\n- Damage Immunities: necrotic, poison "

    elif Type == "Spirit":
        if Dice(2) == 1:
            r = r+"\n- Condition Immunities: charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious"

    elif Type == "Spirit":
        rdm = Dice(2)
        if rdm == 1:
            r = r+"\n- Amorphous"
            r = r+"\n- Shadow Stealth"
            r = r+"\n- Sunlight Weakness"
        elif rdm == 2:
            r = r + "\n- Incorporeal Movement"
            r = r + "\n- Sunlight Sensitivity"
            r = r + "\n- Life Drain"

    elif Type == "Spirit":
        if Dice(2) == 1:
            r = r + "\n- Invisibility"

    elif Type == "Spirit":
        if Dice(2) == 1:
            r = r + "\n- Telekinetic Thrust"

    elif Type == "Vandit":
        r = r+ "\n- Pack Tactics"
        


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
        if Dice(2)==1:
            r = r+ "\n Dark Devotion.\n\t The cultist has advantage on saving throws against being charmed or frightened."
        
        
    elif Type == "Fiend" or Type == 34:
        if Dice(3)==1:
            r = r + "\nDamage Resistances cold"
        if Dice(3)==1:
            r = r + "\nDamage Resistances: fire"
        if Dice(3)==1:
            r = r + "\nDamage Resistances: lightning"
        if Dice(3)==1:
            r = r + "\nDamage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks" 
        if Dice(3)==1:
            r = r + "\nDamage Immunities: poison"
        if Dice(3)==1:
            r = r + "\nDamage Immunities: fire"
        if Dice(3)==1:
            r = r + "\nCondition Immunities: charmed"
        if Dice(3)==1:
            r = r + "\nCondition Immunities: frightened"
        if Dice(3)==1:
            r = r + "\nCondition Immunities: poisoned"
        if Dice(2)==1:
            r = r + "\n Darkvision \n\t 60 ft."
        else: 
            if Dice(2)==1:
                r = r + "\n Darkvision \n\t 120 ft."
        if Dice(2)==1:
            r = r + "\n Devil's Sight. \n\t Magical darkness doesn't impede the Fiend's darkvision."
        if Dice()==1:
            r = r +"\nMagic Resistance"
        if Dice(3) == 1:
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
        
    elif Type == 42:
        r = r + "\n-At will: mage hand (the hand is invisible) \n 3/day each: feather fall, jump, see invisibility, shield"

    elif Type == "Monstrosity" or Type == 43:
        r = r + "\n-Shapechanger"   
        if Dice(2) == 1:
            r = r + "\n-False Appearance"  
        if Dice(2) == 1:
            r = r + "\n-Stone Camouflage.\n\t The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.\n"  
        if Dice(2) == 1:
            r = r + "\n- Keen Sight.\n\t The griffon has advantage on Wisdom (Perception) checks that rely on sight.\n"  
        if Dice(2) == 1:
            r = r + "\n- Flight.\n\t 60 ft.\n"  

    elif Type == "Priest" or Type == 45:
        r = r + "\nDivine Eminence"
        r = r + "\nCantrips (at will): light, sacred flame, thaumaturgy\n 1st level (4 slots): cure wounds, guiding bolt, sanctuary \n 2nd level (3 slots): lesser restoration, spiritual weapon \n 3rd level (2 slots): dispel magic, spirit guardians"
        
    elif Type == "Gnoll" or Type == 46:
        r = r + "\n Rampage.\n\t When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."
 
    elif Type == "Shaman" or Type == 47:
        if Dice(2)==1:
            r = r + "\n Change Shape: \n\t The Shaman magically polymorphs into a Beast, remaining in that form for up to 1 hour. It can revert to its true form as a bonus action. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
            
    elif Type == "Ranger" or Type == 48:
        r = r + Attack(4)
        r = "\n - Multiattack."
        
    elif Type == "Bandit" or Type == 49:
        r = r + "\n- Parry \n\t The Bandit adds 2 to its AC against one melee attack that would hit it. To do so, the bandit must see the attacker and be wielding a melee weapon."
        
    elif Type =="Guard" or Type == 50:
        r = r + "\n- Parry \n\t The Guard adds 2 to its AC against one melee attack that would hit it. To do so, the Guard must see the attacker and be wielding a melee weapon."
        
    if Type == "Kobold" or Type == 51:    
        r = r + "\n- Darkvision \n\t 60ft."
        r = r + "\n- Pack Tactics \n\t The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated."
        r = r + "\n- Sunlight Sensitivity \n\t While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
    
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
            r = r + "\n-Animating Spores"  
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n-Hallucination Spores"  


    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n-Pacifying Spores"   
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n-Rapport Spores (3/Day).\n\t A 10-foot radius of spores extends from the plant. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour."   
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n-Caustic Spores"   
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n-Infestation Spores"   
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n-Euphoria Spores"   
            
    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n Condition Immunities\n\t blinded, deafened, frightened"

    if Type == "Plant": 
        if Dice() == 1:
            r = r + "\n Blindsight\n\t 30 ft"        
        

    if Type == "Warrior":
        r = r + "\n- Pack Tactics \n\t The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated."
        
    if Type == "Warrior":
        if Dice(2)==1:
            r= r + "\n- Multiattack \n\t The Warrior can attack an additional time on his turn."

    else :
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
    if rc == "Giant": STR += Dice(12)
    
    print(Title())
    print(bg)
    print(rc)
    print(Name(rc))
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
    print("COMBAT ACTIONS:")
    print("\tTo hit: +", Modifier(max(STR,DEX)+ Lvl/5))
    print("\n\t- Simple Attack:")
    print (Attack(Dice(4)))
    print("\n\t- Special Attack: {} Charges/Combat".format(Dice( 1 + int(Lvl/4))))
    print (SpecialAttack(Lvl, Modifier(random.choice([STR,DEX,CON,INT,WIS,CHA ]))))

    print("\n\n")
    print("SPELLCASTING:\n\t Spellsave DC:", 10+ Modifier(max(INT,WIS,CHA)))
    print("\t To hit: +", Modifier(max(INT,WIS,CHA)+ Lvl/5))
    print(Magic(Lvl,rc,bg))
    
    print("\n\n")
    print(Actions(bg))
    print(Actions(rc))
    print(Actions())
    print("\n")

    if Dice(Lvl) >= 15:
        print("LEGENDARY ACTIONS:")
        print(Legendary(bg))
        print(Legendary(rc))


NPC()
