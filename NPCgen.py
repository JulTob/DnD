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
        "The Science",
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
        "Elk",
        "Elemental",
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
        "Lion",
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
        "Ranger",
        "Rat",
        "Raven",
        "Revenant",
        " Reptile", 
        " Ruby",
        " Rune",
        "Saurius",
        "Salamander",
        " Scientist",
        "Scarecrow",
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
        r = r+ "\nDamage Immunities poison \n Condition Immunities blinded, charmed, frightened, paralyzed, poisoned"
        if Dice(2) == 1:
            r = r + "\n-Animating Spores"  
        if Dice(2) == 1:
            r = r + "\n-Hallucination Spores"  
        if Dice(2) == 1:
            r = r + "\n-Pacifying Spores"   
        if Dice(2) == 1:
            r = r + "\n-Rapport Spores"   
        if Dice(2) == 1:
            r = r + "\n-Caustic Spores"   
        if Dice(2) == 1:
            r = r + "\n-Infestation Spores"   
        if Dice(2) == 1:
            r = r + "\n-Euphoria Spores"   


        
    elif Type == "Nymph" or Type == 7: 
        r = r+ "\n- Teleport"
        r = r+ "\n- Magic Resistance"
        r = r+ "\n- Speak with Beasts and Plants"
        r = r+ "\n- At will: druidcraft\n 3/day each: entangle, goodberry \n 1/day each: barkskin, pass without trace, shillelagh"
        r = r+ "\n- Fey Charm"
        
    elif Type == "Beast" or Type == 8: 
        r = r+ "\n- Keen Senses"
        rdm = Dice(8)
        if rdm == 1:
            r = r+ "\n -Grappler (DC 10+%STR)"
        if rdm == 2: 
            r = r+ "\n -Charger (2d6, DC 10+%STR)"
            r = r+ "\n -Relentless"
        if rdm == 3: 
            r = r+ "\n- Water Breathing"
            r = r+ "\n- Blood Frenzy"
        if rdm == 4: 
            r = r+ "\n- Amphibious"
            r = r+ "\n- Standing Leap"
        if rdm == 5: 
            r = r + "\n- SpiderClimb"  
            r = r + "\n- Web"
        if rdm == 6: 
            r = r+ "\n - Running Leap"
            r = r+ "\n - Pack Tactics"  
        if rdm == 7:
            r = r+ "\n - Pounce"
        if rdm == 8:
            r = r+ "\n - Constrict (restrained, 2d8 + %STR, escape DC 10+%STR)"
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
        r = r+ "\n- Nimble Scape"
    elif Type == "Aberration" or Type == 13:
        r = r+ "Blindsight"
    elif Type == "Kenku"  or Type == 14:
        r = r+ "\n- Ambusher \n- Mimicry"
        
        
    elif Type == "Elemental" or Type == 15:
        r = "\n- False Appereance \n- Death Burst \n- Damage Resistances: bludgeoning, piercing, and slashing from nonmagical attacks"
        rdm = Dice(4)
        if rdm == 1:
            r = "\n- Heated Body \n- Damage Immunities: fire  \n- Damage Vulnerabilities: cold"
        
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
        r = r + "\nDamage Immunities: poison"+"\n Condition Immunities: exhaustion, poisoned, charmed"
        if Dice(2) == 1:
            r = r + "\n -Undead Fortitude"
        if Dice(2) == 1:
            r = r + "\n -Stench"
        if Dice(2) == 1:
            r = r + "\n -Turn Defiance"
            

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
        if Dice(2) == 1:
            r = r+ "\n- Engulf"
        if Dice(2) == 1:
            r = r+ "\n- Gelatinous Cube"
        if Dice(2) == 1:
            r = r+ "\n- Transparent"
        if Dice(2) == 1:
            r = r+ "\n- Spider Climb"
        if Dice(2) == 1:
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
        r = r+ "\n- Keen Hearing and Sight"
        
    elif Type == "Spirit" or Type == 28:
        r = r+"\nDamage Resistances: acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks \nDamage Immunities: necrotic, poison \nCondition Immunities: charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious"
        rdm = Dice(2)
        if rdm == 1:
            r = r+"\n- Amorphous"
            r = r+"\n- Shadow Stealth"
            r = r+"\n- Sunlight Weakness"
        elif rdm == 1:
            r = r + "\n- Incorporeal Movement"
            r = r + "\n- Sunlight Sensitivity"
            r = r + "\n- Life Drain"

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
        elif rdm == 6:
            r = r + "\n - Repulsion Breath"
        elif rdm == 7:
            r = r + "\n - Poison Breath"
        if Dice(2) == 1:
            r = r + "\n - Amphibious"


    elif Type == "Dwarf" or Type == 31:
        r = r + "\n- Resilience"
        rdm = Dice(2)
        if rdm == 1:
            r = r + "\n- Sunlight Sensitivity"
        rdm = Dice(2)
        if rdm == 1:
            r = r + "\n- Enlarge"
        rdm = Dice(2)
        if rdm == 1:
            r = r + "\n- Invisibility"
    elif Type == 32:
        r = r+ "\n- Luring Song"
    
    elif Type == "Cultist" or Type == 33:
        r = r+ "\n- Skills Deception +4, Persuasion +4, Religion +2\n"
        r = r+ "\n    Cantrips (at will): light, sacred flame, thaumaturgy \n 1st level (4 slots): command, inflict wounds, shield of faith. \n 2nd level (3 slots): hold person, spiritual weapon"
        
        
    elif Type == "Fiend" or Type == 34:
        r = r + "\nDamage Resistances cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks \nDamage Immunities poison"
        r = r +"\nMagic Resistance"
        rdm = Dice(2)
        if rdm == 1:
            r = r + "\n- Shapechanger"
        rdm = Dice(2)
        if rdm == 1:
            r = r + "\n- Scare (1/Day)."
        rdm = Dice(2)
        if rdm == 1:
            r = r + "\n- Invisibility."
    elif Type == 35:
        r = r + "\n- Terrifying Glare"
    elif Type == "Spy" or Type == 36:
        r = r + "\n- Skills: Deception +5, Insight +4, Investigation +5, Perception +6, Persuasion +5, Sleight of Hand +4, Stealth +4"
        r = r + "\n- Cunning Action \n- Sneak Attack (1/Turn)."
    elif Type == "Berserker" or Type == 35:
        r = r + "\n- Multiattack"
        r = r + "\n- Reckless"
    elif Type == 36:
        r = r+"\n    At will: animal friendship (snakes) \n 3/day each: poison spray, suggestion"
    elif Type == "Bandit" or Type == 36:
        r = r + "\n- Parry\n"

    elif Type == "Centaur" or Type == 37:
        r = r + "\nSkills Athletics +6, Perception +3, Survival +3\n- Charge\n- Multiattack"
    elif Type == 38:
        r = r+ "\n    Cantrips (at will): sacred flame, thaumaturgy \n 1st level (3 slots): bane, shield of faith"
    elif Type == "Druid" or Type == 39:
        r = r + "\n- Cantrips (at will): druidcraft, produce flame, shillelagh \n 1st level (4 slots): entangle, longstrider, speak with animals, thunderwave \n2nd level (3 slots): animal messenger, barkskin\n"
    elif Type == "Druid" or Type == 39:
        r = r + "\n-Cantrips (at will): druidcraft, produce flame, thorn whip\n1st level (4 slots): entangle, fog cloud\n2nd level (3 slots): heat metal, spike growth\n3rd level (2 slots): conjure animals, plant growth"
    elif Type == 40:
        r = r + "\n-At will: mage hand (the hand is invisible) \n 3/day each: feather fall, jump, see invisibility, shield"
    elif Type == "Monstrosity" or Type == 41:
        r = r + "\n-Shapechanger"   
        if Dice(2) == 1:
            r = r + "\n-False Appearance"  

    elif Type == "Giant" or Type == 42:
        r = r + "\n-STR +" + Dice(12)  

    elif Type == 43:
        r = r + "\n-Cantrips (at will): guidance, resistance, thaumaturgy\n 1st level (4 slots): bless, command\n 2nd level (2 slots): augury, spiritual weapon (spear) "
 

    else:    
        r = r + "\n- Multiattack\n"
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
    print("Lvl:", Lvl, "   HP:", Lvl*(Dice(10) + Modifier(CON)))
    print("\nSTR:", STR,
        "  DEX:", DEX,
        "  CON:", CON, 
        "  INT:", INT, 
        "  WIS:", WIS,
        "  CHA:", CHA, "\n")
 
    print (Attack("Melee"))
    print (Attack(Dice(4)), "+", int(1 + Lvl/3) ,"d4 " + Damage() +" dmg")

    print("\n")
    print(Spellcasting(bg))
    print(Spellcasting(rc))
    print(Spellcasting())
    print("\n")


NPC()
