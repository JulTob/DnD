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
        "The Battle",
        "The Baron of",
        "The Bearded", 
        "The Beholder",
        "The Blending",
        "The Black",
        "The Blue",
        "The Bone",
        "The Bursting",
        "The Brass",
        "The Bronce",
        "The Brain",
        "The Climate",
        "The Chain",
        "The Champion",
        "The Chief",
        "The Chimera",
        "The Collector",
        "The Conjurer",
        "The Coral",
        "The Clokwork",
        "The Deadly",
        "The Death",
        "The Dawning",
        "The Dark",
        "The Doctor", 
        "The Deep",
        "The Divine",
        "The Diviner",
        "The Dream",
        "The Equinox",
        "The Equivalence",
        "The Emphasising",
        "The Emmerald", 
        "The Enchanter",
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
        "The Gas",
        "The Green",
        "The Golden",
        "The Great",
        "The Gladiator",
        "The Hell",
        "The High",
        "The Hive",
        "The Hungry",
        "The Impulse",
        "The Inkwork",
        "The Iron",
        "The Ironbark",
        "The Ice",
        "The Icicle",
        "The Ink",
        "The Illusionist",
        "The Jewelcraft",
        "The Kraken",
        "The Life",
        "The Lightning",
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
        "The Ocean",
        "The Orange",
        "The Old",
        "The Owl",
        "The Pain",
        "The Plague",
        "The Powder",
        "The Power",
        "The Purifying",
        "The Protector",
        "The Rat",
        "The Rainstorm",
        "The Red",
        "The Ruby",
        "The Rune",
        "The Sad",
        "The Shadow",
        "The Silver",
        "The Skelleton",
        "The Smiling",
        "The Spring",
        "The Storm",
        "The Stone",
        "The Start",
        "The Stars",
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
        "Archfey",
        "Archdruid",
        "Archmage",
        " Ash",
        " Assassin",
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
        " Chemist",
        "Champion",
        " Collector",
        "Collosus",
        "Commander",
        " Darkness",
        " Diamond",
        "Dino",
        " Death",
        " Devil",
        " Doctor",
        " Doom",
        " Dragon",
        " Drake",
        " Druid",
        "Dream",
        " Eater",
        "Eclipse",
        "Enforcer",
        "Elite",
        "Elemental",
        " Fire", 
        "Fury",
        " Flutist",
        "Flame",
        "Freedomfighter",
        " Genius",
        " Geneticist", 
        "Giant",
        " Grandmaster",
        "Ghost",
        "Golem",
        " Hand",
        "Hag",
        "Hive",
        " Horror",
        "Hound",
        " Hunter",
        "Hunger",
        " Inquisitor",
        "Incubus",
        " Knight",
        " Killer",
        " Knife",
        "King",
        "Kiss",
        " Leader",
        " Licht",
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
        "Necromancer",
        " Nightmare",
        " Nomad",
        " Of Justice",
        "Of The Abyss",
        "Of the Autumn",
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
        " Ranger",
        "Rat",
        "Raven",
        "Revenant",
        " Reptile", 
        " Ruby",
        " Rune",
        "Saurius",
        "Salamander",
        " Scientist",
        " Shadow",
        "Shark",
        "Sorcerer",
        "Snake",
        "Skeleton",
        " Skull",
        " Surgeon",
        "Sucubus",
        " Spirit",
        "Spider",
        "Swashbuckler",
        " Terror",
        "Trapper",
        "Troll",
        "Thief",
        " Void",
        "Vampire",
        "Walker",
        " Warlock",
        "Werewolf",
        " Wizard",
        " Witch",
        " Witchhunter",
        " Wolf",
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
        "Assassin",
        "Bandit",
        "Bard",
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
        "Student",
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
        "Aven(Birdfolk)",
        "Beast", 
        "Beast",
        "Catfolk",
        "Celestial", 
        "Centaur",
        "Construct",
        "Demon",
        "Dragon",
        "Dwarf","Dwarf","Dwarf",
        "Elf","Elf","Elf","Elf","Elf","Elf",
        "Elemental",
        "Fey", "Fey",
        "Fiend",
        "Giant",
        "Gnoll",
        "Gnome",
        "Goblin",
        "Hag",
        "Hobgoblin",
        "Illithid",
        "Kenku",
        "Kobold",
        "Lizardfolk",
        "Lycan",
        "Merfolk",
        "Monstrosity",
        "Nymph",
        "Ogre",
        "Ooze",
        "Orc",
        "Plant",
        "Snakefolk",
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
def Modifier(AS):
    return int((AS-10)/2)

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


def Spellcasting(Type=Dice(50)):
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
        r = r + "\n- Pack Tactics"
        
    elif Type == "Plant" or Type == 6: 
        r = r+ "\n- False Appereance"
        r = r+ "\n- Entangling Plants"
        
    elif Type == "Nymph" or Type == 7: 
        r = r+ "\n- Teleport"
        r = r+ "\n- Magic Resistance"
        r = r+ "\n- Speak with Beasts and Plants"
        r = r+ "\n- At will: druidcraft\n 3/day each: entangle, goodberry \n 1/day each: barkskin, pass without trace, shillelagh"
        r = r+ "\n- Fey Charm"
    elif Type == "Beast" or Type == 8: 
        rdm = Dice(6)
        if rdm == 1:
            r = r+ "\n -Grappler (DC 10+%STR)"
        if rdm == 2: 
            r = r+ "\n -Charger (2d6, DC 10+%STR)"
        if rdm == 3: 
            r = r+ "\n -Keen Senses"
        if rdm == 4: 
            r = r+ "\n -Amphibious"
        if rdm == 5: 
            r = r+ "\n -SpiderClimb"  
        if rdm == 6: 
            r = r+ "\n -Pack Tactics"  
            
    elif Type == "Elf" or Type == 9:
        rdm = Dice(1)
        if rdm == 1:
            r = r+ "\n At will: dancing lights\n    1/day each: darkness, faerie fire"

    elif Type == "Aven(Birdfolk)" or Type == 10:
        r = r+ "\n- Flight"
    elif Type == "Construct" or Type == 11:
        r = r+ "\n- Axiomatic Mind \n- False Apperance"
        r = r+ "\n- Damage Immunities: poison, psychic \n\n Condition Immunities: blinded, charmed, deafened, exhaustion, frightened, paralyzed, petrified, poisoned \n"
    elif Type == "Goblin" or Type == 12:
        r = r+ "Nimble Scape"
    elif Type == "Aberration" or Type == 13:
        r = r+ "Blindsight"
    elif Type == "Kenku"  or Type == 14:
        r = r+ "\n- Ambusher \n- Mimicry"
    elif Type == "Elemental" or Type == 15:
        r = "False Appereance \n Death Burst"
        
    elif Type == "Fey" or Type == 16:
        r = "\n- Invisibility \n\n At will: druidcraft \n    1/day each: confusion, dancing lights, detect evil and good, detect thoughts, dispel magic, entangle, fly, phantasmal force, polymorph, sleep"
        rdm = Dice(2)
        if rdm == 1:
            r = r + "\n - Invisibility"
        if rdm == 2:
            r = r + "\n - Heart Sight"
        return r
        
    elif Type == "Assassin" or Type == 17:
        return "\n- Superior Invisibility"
        
    elif Type == "Undead" or Type == 18:
        r = r + "\nDamage Immunities: poison"+"\n Condition Immunities: exhaustion, poisoned"
        rdm = Dice(2)
        if rdm == 1:
            r = r + "\n -Undead Fortitude"

    elif Type == "Lizardfolk" or Type == 19:
        r = r+"\n- Hold Breath"
        rdm = Dice(2)
        if rdm == 1:
            r = r + "\n - Chameleon Skin"
        return r
        
    elif Type == "Vampire" or Type == 20:
        r = r + "\n - Sunlight Sensitivity"
        return r
        
    elif Type == "Wolf" or Type == 21:
        r = r + "\n - Pack Tactics"
        r = r + "\n - Keen Hearing and Smell."
        
    elif Type == "Gnome" or Type == 22:
        r = r + "\n - Gnome Cunning"
        r = r + "\n\n At will: nondetection (self only) \n   1/day each: blindness/deafness, blur, disguise self"
        
    elif Type == "Ooze" or Type == 23:
        r = r+ "\n- Amorphous"
        r = r+ "\n- Corrode Material"
        r = r+ "\n- False Appearance"
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
        r = r+ "\n- Keen Hearing and Sight"
        
    elif Type == "Spirit" or Type == 28:
        r = r+"\n- Amorphous"
        r = r+"\n- Shadow Stealth"
        r = r+"\n- Sunlight Weakness"
        
    elif Type == "Thug" or Type == 29:
        r = r+ "\n- Pack Tactics"
    elif Type == "Dragon" or Type == 30:
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
            
    
    elif Type == "Dwarf" or Type == 31:
        r = r + "\n -Resilience"
        rdm = Dice(5)
        if rdm == 1:
            r = r + "\n - Sunlight Sensitivity"
        elif rdm == 2:
            r = r + "\n -Enlarge"
            r = r + "\n Invisibility"
    
    else:    
        r = r + "\n- Multiattack\n" + Spellcasting(Dice(31))
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
    
    Lvl = Dice(20)
    rc = Race()
    
    
    print(Title())
    print(bg)
    print(rc)
    print("Lvl:", Lvl, "   HP:", Lvl*(Dice(12) + Modifier(CON)))
    print("\nSTR:", STR,
        "  DEX:", DEX,
        "  CON:", CON, 
        "  INT:", INT, 
        "  WIS:", WIS,
        "  CHA:", CHA, "\n")
 
    print (Attack("Melee"))
    print (Attack(Dice(4)), "+1d4 " + Damage() +" dmg")

    print("\n")
    print(Spellcasting(bg))
    print(Spellcasting(rc))
    print(Spellcasting())
    
NPC()
