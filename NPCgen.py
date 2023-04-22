# NPC creator 
import random

def Title():
    descriptor = [
        "The Air",
        "The Alcoholic",
        "The Alpha", 
        "The Aberrant",
        "The Aprendice of"
        "The Baron of",
        "The Brass",
        "The Bursting",
        "The Blending",
        "The Black",
        "The Blue",
        "The Climate",
        "The Chain",
        "The Chief",
        "The Collector",
        "The Deadly",
        "The Death",
        "The Dawning",
        "The Dark",
        "The Doctor", 
        "The Equinox",
        "The Equivalence",
        "The Emphasising",
        "The Emmerald", 
        "The Engine",
        "The Energy",
        "The Errant",
        "The Earth",
        "The Fleshwork",
        "The Fire",
        "The Fool",
        "The Forest",
        "The Gas",
        "The Green",
        "The Great",
        "The High",
        "The Impulse",
        "The Inkwork",
        "The Ironbark",
        "The Ice",
        "The Icicle",
        "The Ink",
        "The Jewelcraft",
        "The Life",
        "The Lightning",
        "The Lord Of the",
        "The Lord Of",
        "The Master",
        "The Mad",
        "The Mind",
        "The Mirror",
        "The Mist",
        "The Moon",
        "The Mutant",
        "The Night",
        "The Nightmare",
        "The New",
        "The Orange",
        "The Old",
        "The Pain",
        "The Powder",
        "The Power",
        "The Purifying",
        "The Rat",
        "The Rainstorm",
        "The Red",
        "The Ruby",
        "The Rune",
        "The Storm",
        "The Stone",
        "The Start",
        "The Spark",
        "The Spell",
        "The Tender",
        "The True",
        "The Undead",
        "The Void",
        "The Warping",
        "The Water",
        "The White",
        "The Wind" ,
        "The Wolf"
        
        ]
    rank = [
        " Abomination",
        " Alchemist",
        "Aprentice",
        " Arrow",
        " Ash",
        " Assassin",
        " Bard", 
        " Baron",
        " Battle", 
        " Benefactor",
        " Berserker",
        " Blade",
        "Bow",
        " Chemist",
        " Collector",
        " Darkness",
        " Diamond",
        " Death",
        " Doctor",
        " Doom",
        " Dragon",
        " Druid",
        " Eater",
        " Enforcer",
        " Fire", 
        " Flutist",
        " Genius",
        " Geneticist", 
        " Grandmaster",
        " Hand",
        " Horror",
        " Hunter",
        " Inquisitor",
        " Knight",
        " Killer",
        " Knife",
        " Leader",
        " Licht",
        " Lotus",
        " Lord",
        " Machine",
        " Mage",
        " Master",
        " Martyr",
        " Mind",
        " Monk",
        " Monster",
        " Moon",
        " Nightmare",
        " Nomad",
        " Of Justice",
        " Of The East",
        " Of The Forest",
        " Of The Hills",
        " Of The North",
        " Of The Mountain",
        " Of The Sands",
        " Of The Sea",
        " Of The South",
        " Of The West",
        " Oni",
        " Outlaw",
        " Pathologist",
        " Paw",
        "Pirate",
        " Poet",
        " Prophet",
        " Ranger",
        " Reptile", 
        " Ruby",
        " Rune",
        " Scientist",
        " Shadow",
        " Sorcerer",
        " Skull",
        " Surgeon",
        " Spirit",
        " Terror",
        " Void",
        " Warlock",
        " Wizard",
        " Witch",
        " Witchhunter",
        " Wolf",
        " Writter" 
        ] 
    
    title = random.choice(descriptor) + " " + random.choice(rank)
    return title
   
def Background():
    Backgrounds = [
        "Acolyte",
        "Alchemist",
        "Archmage",
        "Assassin",
        "Bandit",
        "Berserker",
        "Commoner",
        "Cultist",
        "Druid",
        "Expert",
        "Gladiator",
        "Guard",
        "Knight", 
        "Mage",
        "Noble", 
        "Priest",
        "Pirate",
        "Scout",
        "Spy",
        "Spellcaster",
        "Thug", 
        "Tribal Warrior",
        "Veteran",
        "Warrior",
        ""
        ]
    return random.choice(Backgrounds)
   
def Race():
    Races = [
        "Human","Human","Human","Human","Human","Human","Human",
        "Aberration",
        "Aven(Birdfolk)"
        "Beast",
        "Catfolk",
        "Celestial", 
        "Construct",
        "Demon",
        "Dragon",
        "Elf","Elf","Elf","Elf","Elf","Elf","Elf",
        "Elemental",
        "Fey", "Fey",
        "Fiend",
        "Giant",
        "Gnoll",
        "Gnome",
        "Goblin",
        "Hobgoblin",
        "Kenku",
        "Kobold",
        "Lizardfolk",
        "Lycan",
        "Merfolk",
        "Monstrosity",
        "Nymph",
        "Ooze",
        "Orc",
        "Plant",
        "Spirit",
        "Undead",
        "Vampire",
        "Werewolf",
        "Wolf",
        ""
        ]
    return random.choice(Races)

 
def Dice(D=6):
    roll = random.randint(1,D)
    return roll
    
def AbilityScore():
    d1 = Dice()
    d2 = Dice() 
    d3 = Dice()
    d4 = Dice()
    return d1+d2+d3+d4 - min(d1,d2,d3,d4) + Dice(3) -1
    
def NPC():
    """NPC creator"""
    STR = AbilityScore()
    DEX = AbilityScore()
    CON = AbilityScore()
    WIS = AbilityScore()
    CHA = AbilityScore()
    
    
    
    
    
    
    print(Title())
    print(Background())
    print(Race())
    print("STR:", STR,
        "  DEX:", DEX,
        "  CON:", CON, 
        "  WIS:", WIS,
        "  CHA:", CHA)
 
    
NPC()
