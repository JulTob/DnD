import npc_class as NPC
import random

def Dice(D=6,N=1):
    """Rolls N dices with D sides each. If D is 0, simulates a coin flip."""
    roll = 0
    for m in range(N):
        if D >= 1: roll += random.randint(1, D)
        else: roll += random.randint(D, 1)
    return roll

def add_language(languages, language, chance=6):
    """Try to add a language based on a dice roll and chance."""
    if Dice(chance) == 1 and language not in languages:
        languages.append(language)


def Language(npc):
    race = npc.race
    background = npc.background
    if race == "":
        race = Race()
    if background == "":
        background = Background()

    languages = [""]

    if race == "base":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
    if race == "Human":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 6,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Aberration":
        langs = {
            "Dwarvish": 15,
            "Elvish": 15,
            "Giant": 9,
            "Gnomish": 20,
            "Goblin": 9,
            "Halfling": 20,
            "Orc": 9,
            "Abyssal": 7,
            "Celestial": 20,
            "Draconic": 9,
            "Deep Speech": 1,
            "Infernal": 9,
            "Primordial": 19,
            "Sylvan": 20,
            "Undercommon": 5,
            "Telepathy (60 ft.) ": 5
            }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)      

    if race == "Aven":
        langs = {
            "Dwarvish": 14,
            "Elvish": 9,
            "Giant": 15,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 14,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 9,
            "Draconic": 9,
            "Deep Speech": 100,
            "Infernal": 100,
            "Primordial": 3,
            "Sylvan": 5,
            "Undercommon": 100
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Beast":
        langs = {
            "Beastly Speech":1,
            "Dwarvish": 20,
            "Elvish": 10,
            "Giant": 20,
            "Gnomish": 10,
            "Goblin": 10,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 10,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 10,
            "Sylvan": 2,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Beastfolk":
        langs = {
            "Beastly Speech":1,
            "Dwarvish": 20,
            "Elvish": 8,
            "Giant": 15,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 10,
            "Celestial": 10,
            "Draconic": 10,
            "Deep Speech": 20,
            "Infernal": 10,
            "Primordial": 10,
            "Sylvan": 4,
            "Undercommon": 10,
            f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if race == "Celestial":
        langs = {
            "Dwarvish": 10,
            "Elvish": 8,
            "Giant": 10,
            "Gnomish": 10,
            "Goblin": 10,
            "Halfling": 10,
            "Orc": 10,
            "Abyssal": 8,
            "Celestial": 1,
            "Draconic": 10,
            "Deep Speech": 20,
            "Infernal": 8,
            "Primordial": 20,
            "Sylvan": 6,
            "Undercommon": 20,
            "All languages":8,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
   
        if Dice(2): add_language(languages, "Telepathy. (60 feet).", 8) 
        else: add_language(languages, "Telepathy. (120 feet).", 10) 

    if race == "Construct":
        add_language(languages, "Understands the languages of its creator.", 1) 
        add_language(languages, "All languages.", 5) 

    if race == "Dragon":
        langs = {
            "Dwarvish": 8,
            "Elvish": 8,
            "Giant": 8,
            "Gnomish": 8,
            "Goblin": 8,
            "Halfling": 8,
            "Orc": 8,
            "Abyssal": 8,
            "Celestial": 8,
            "Draconic": 1,
            "Deep Speech": 10,
            "Infernal": 8,
            "Primordial": 10,
            "Sylvan": 4,
            "Undercommon": 10
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Dwarf":
        langs = {
            "Dwarvish": 1,
            "Elvish": 5,
            "Giant": 5,
            "Gnomish": 16,
            "Goblin": 16,
            "Halfling": 8,
            "Orc": 20,
            "Abyssal": 18,
            "Celestial": 16,
            "Draconic": 12,
            "Deep Speech": 3,
            "Infernal": 12,
            "Primordial": 12,
            "Sylvan": 20,
            "Undercommon": 4
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Elf":
        langs = {
            "Dwarvish": 6,
            "Elvish": 1,
            "Giant": 12,
            "Gnomish": 6,
            "Goblin": 18,
            "Halfling": 12,
            "Orc": 20,
            "Abyssal": 8,
            "Celestial": 8,
            "Draconic": 8,
            "Deep Speech": 16,
            "Infernal": 8,
            "Primordial": 6,
            "Sylvan": 4,
            "Undercommon": 6
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
    if race == "Elemental":
        langs = {
            "Dwarvish": 8,
            "Elvish": 8,
            "Giant": 8,
            "Gnomish": 8,
            "Goblin": 18,
            "Halfling": 18,
            "Orc": 12,
            "Abyssal": 12,
            "Celestial": 12,
            "Draconic": 12,
            "Deep Speech": 20,
            "Infernal": 12,
            "Primordial": 1,
            "Sylvan": 4,
            "Undercommon": 10,
            "Ignan": 4,
            "Terran":4,
            "Aquan":4,
            "Auran":4
            
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if race == "Fey":
        langs = {
            "Dwarvish": 14,
            "Elvish": 3,
            "Giant": 10,
            "Gnomish": 8,
            "Goblin": 4,
            "Halfling": 16,
            "Orc": 16,
            "Abyssal": 16,
            "Celestial": 16,
            "Draconic": 8,
            "Deep Speech": 20,
            "Infernal": 16,
            "Primordial": 8,
            "Sylvan": 1,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Fiend":
        langs = {
            "Dwarvish": 4,
            "Elvish": 4,
            "Giant": 8,
            "Gnomish": 4,
            "Goblin": 2,
            "Halfling": 12,
            "Orc": 4,
            "Abyssal": 2,
            "Celestial": 25,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 2,
            "Primordial": 22,
            "Sylvan": 20,
            "Undercommon": 8,
            "Telepathy (60 ft.)": 10,
            "Telepathy (120 ft.)": 12            
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Giant":
        langs = {
            "Dwarvish": 4,
            "Elvish": 20,
            "Giant": 1,
            "Gnomish": 8,
            "Goblin": 8,
            "Halfling": 20,
            "Orc": 8,
            "Abyssal": 12,
            "Celestial": 12,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 12,
            "Primordial": 16,
            "Sylvan": 8,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Gnome":
        langs = {
            "Dwarvish": 3,
            "Elvish": 3,
            "Giant": 3,
            "Gnomish": 1,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 10,
            "Abyssal": 12,
            "Celestial": 12,
            "Draconic": 12,
            "Deep Speech": 12,
            "Infernal": 12,
            "Primordial": 12,
            "Sylvan": 4,
            "Undercommon": 12
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Goblin":
        langs = {
            "Dwarvish": 18,
            "Elvish": 16,
            "Giant": 10,
            "Gnomish": 18,
            "Goblin": 1,
            "Halfling": 18,
            "Orc": 4,
            "Abyssal": 10,
            "Celestial": 19,
            "Draconic": 6,
            "Deep Speech": 10,
            "Infernal": 10,
            "Primordial": 20,
            "Sylvan": 2,
            "Undercommon": 2
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Halfling":
        langs = {
            "Dwarvish": 4,
            "Elvish": 4,
            "Giant": 20,
            "Gnomish": 4,
            "Goblin": 20,
            "Halfling": 1,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 4,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 18,
            "Sylvan": 18,
            "Undercommon": 20
            }
        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if race == "Kobold":
        langs = {
            "Dwarvish": 6,
            "Elvish": 18,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 8,
            "Halfling": 20,
            "Orc": 12,
            "Abyssal": 8,
            "Celestial": 10,
            "Draconic": 1,
            "Deep Speech": 8,
            "Infernal": 8,
            "Primordial": 20,
            "Sylvan": 16,
            "Undercommon": 6
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
        
    if race == "Lizardfolk":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 10,
            "Gnomish": 20,
            "Goblin": 10,
            "Halfling": 20,
            "Orc": 4,
            "Abyssal": 4,
            "Celestial": 20,
            "Draconic": 1,
            "Deep Speech": 4,
            "Infernal": 4,
            "Primordial": 4,
            "Sylvan": 4,
            "Undercommon": 20,
            f"Beast Telepathy (Only Reptiles): The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3,

        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Monstrosity":
        langs = {
            "Dwarvish": 10,
            "Elvish": 22,
            "Giant": 9,
            "Gnomish": 25,
            "Goblin": 11,
            "Halfling": 22,
            "Orc": 7,
            "Abyssal": 4,
            "Celestial": 22,
            "Draconic": 6,
            "Deep Speech": 1,
            "Infernal": 5,
            "Primordial": 12,
            "Sylvan": 9,
            "Undercommon": 1
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    
    if race == "Ooze":
        add_language(languages, "Telepathy. ", 1)

    if race == "Orc":
        langs = {
            "Dwarvish": 12,
            "Elvish": 12,
            "Giant": 4,
            "Gnomish": 22,
            "Goblin": 2,
            "Halfling": 22,
            "Orc": 1,
            "Abyssal": 8,
            "Celestial": 8,
            "Draconic": 8,
            "Deep Speech": 22,
            "Infernal": 8,
            "Primordial": 8,
            "Sylvan": 8,
            "Undercommon": 8
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Plant":
        langs = {
            "Dwarvish": 20,
            "Elvish": 5,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 10,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 2,
            "Sylvan": 1,
            "Undercommon": 8,
            "Telepathy":4
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Snakefolk":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 2,
            "Celestial": 20,
            "Draconic": 1,
            "Deep Speech": 2,
            "Infernal": 10,
            "Primordial": 4,
            "Sylvan": 8,
            "Undercommon": 20,
            f"Beast Telepathy (Only Snakes): The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3,

        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
        
    if race == "Undead":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 6,
            "Abyssal": 2,
            "Celestial": 2,
            "Draconic": 6,
            "Deep Speech": 2,
            "Infernal": 2,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 4
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    # BACKGROUNDS
    if background == "base":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if background == "Druid":
        langs = {
            "Druidic":1,
            "Dwarvish": 20,
            "Elvish": 4,
            "Giant": 20,
            "Gnomish": 10,
            "Goblin": 10,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 16,
            "Draconic": 4,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 4,
            "Sylvan": 4,
            "Undercommon": 20,
            f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3,

        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    
    if background == "Bandit":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if background == "Bard":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 20,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 6,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Berserker":
        langs = {
            "Dwarvish": 6,
            "Elvish": 20,
            "Giant": 6,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 6,
            "Abyssal": 12,
            "Celestial": 20,
            "Draconic": 16,
            "Deep Speech": 16,
            "Infernal": 12,
            "Primordial": 16,
            "Sylvan": 20,
            "Undercommon": 6
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            


    if background == "Charlatan":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 20,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Cultist":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 8,
            "Celestial": 8,
            "Draconic": 8,
            "Deep Speech": 8,
            "Infernal": 8,
            "Primordial": 8,
            "Sylvan": 20,
            "Undercommon": 8
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Criminal":
        langs = {
            "Thieve's Cant":1,
            "Dwarvish": 12,
            "Elvish": 12,
            "Giant": 20,
            "Gnomish": 12,
            "Goblin": 12,
            "Halfling": 12,
            "Orc": 12,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 4
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Expert":
        langs = {
            "Dwarvish": 5,
            "Elvish": 5,
            "Giant": 5,
            "Gnomish": 5,
            "Goblin": 19,
            "Halfling": 19,
            "Orc": 19,
            "Abyssal": 19,
            "Celestial": 5,
            "Draconic": 19,
            "Deep Speech": 19,
            "Infernal": 19,
            "Primordial": 19,
            "Sylvan": 19,
            "Undercommon": 19
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if background == "Explorer":
        langs = {
            "Dwarvish": 4,
            "Elvish": 4,
            "Giant": 4,
            "Gnomish": 4,
            "Goblin": 4,
            "Halfling": 4,
            "Orc": 4,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 4,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Healer":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 10,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 4,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 4,
            "Sylvan": 4,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Hero":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Hunter":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 6,
            "Sylvan": 1,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Knight":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Mage":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 6,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 6,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 6,
            "Infernal": 6,
            "Primordial": 6,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Monk":
        langs = {
            "Dwarvish": 10,
            "Elvish": 10,
            "Giant": 10,
            "Gnomish": 10,
            "Goblin": 10,
            "Halfling": 10,
            "Orc": 10,
            "Abyssal": 10,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 10,
            "Infernal": 10,
            "Primordial": 6,
            "Sylvan": 10,
            "Undercommon": 10,
            f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":10,

        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)




    if background == "Noble":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 12,
            "Draconic": 12,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Priest":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 6,
            "Celestial": 6,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 6,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Pirate":
        langs = {
            "Thieve's Cant":1,
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 12,
            "Infernal": 20,
            "Primordial": 12,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Ranger":
        langs = {
            "Dwarvish": 20,
            "Elvish": 4,
            "Giant": 4,
            "Gnomish": 20,
            "Goblin": 4,
            "Halfling": 20,
            "Orc": 4,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 6,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 6,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Scholar":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 6,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 6,
            "Infernal": 6,
            "Primordial": 6,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Shaman":
        langs = {
            "Druidic":1,
            "Dwarvish": 20,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 20,
            "Goblin": 6,
            "Halfling": 20,
            "Orc": 6,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 8,
            "Sylvan": 1,
            "Undercommon": 20,
            f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":10,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Spy":
        langs = {
            "Thieve's Cant":1,
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if background == "Traveler":
        langs = {
            "Dwarvish": 5,
            "Elvish": 5,
            "Giant": 5,
            "Gnomish": 5,
            "Goblin": 5,
            "Halfling": 5,
            "Orc": 5,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 12,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Urchin":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if background == "Warrior":
        langs = {
            "Dwarvish": 6,
            "Elvish": 6,
            "Giant": 6,
            "Gnomish": 6,
            "Goblin": 6,
            "Halfling": 6,
            "Orc": 6,
            "Abyssal": 20,
            "Celestial": 20,
            "Draconic": 20,
            "Deep Speech": 20,
            "Infernal": 20,
            "Primordial": 20,
            "Sylvan": 20,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            



    if background == "Warlock":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 20,
            "Gnomish": 20,
            "Goblin": 20,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 6,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 6,
            "Infernal": 6,
            "Primordial": 6,
            "Sylvan": 6,
            "Undercommon": 20
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            


    if background == "Witch":
        langs = {
            "Dwarvish": 20,
            "Elvish": 20,
            "Giant": 12,
            "Gnomish": 20,
            "Goblin": 6,
            "Halfling": 20,
            "Orc": 20,
            "Abyssal": 6,
            "Celestial": 6,
            "Draconic": 6,
            "Deep Speech": 6,
            "Infernal": 6,
            "Primordial": 6,
            "Sylvan": 12,
            "Undercommon": 20,
            f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":10,

        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
    return "Common" + ", ".join(languages)

