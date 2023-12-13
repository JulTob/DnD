import npc_class as NPC
import random
import dnd

def Dice(D=6,N=1):
    return dnd.Dice(D,N)

def add_language(languages, language, chance=6):
    """Try to add a language based on a dice roll and chance."""
    if chance<1 and language not in languages:
        languages.append(language)
    elif Dice(chance) == 1 and language not in languages:
        languages.append(language)


def Language(npc):
    race = npc.race
    background = npc.background
    INT = npc.ability_scores.int_mod
    if race == "":
        race = Race()
    if background == "":
        background = Background()

    languages = [""]

    if race == "base":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
    if race == "Human":
        langs = {
            "Dwarvish": 6-INT,
            "Elvish": 6-INT,
            "Giant": 6-INT,
            "Gnomish": 6-INT,
            "Goblin": 6-INT,
            "Halfling": 6-INT,
            "Orc": 6-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Aberration":
        langs = {
            "Dwarvish": 15-INT,
            "Elvish": 15-INT,
            "Giant": 9-INT,
            "Gnomish": 20-INT,
            "Goblin": 9-INT,
            "Halfling": 20-INT,
            "Orc": 9-INT,
            "Abyssal": 7-INT,
            "Celestial": 20-INT,
            "Draconic": 9-INT,
            "Deep Speech": 1-INT,
            "Infernal": 9-INT,
            "Primordial": 19-INT,
            "Sylvan": 20-INT,
            "Undercommon": 5-INT,
            "Telepathy (60 ft.) ": 5-INT,
            }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)      

    if race == "Aven":
        langs = {
            "Dwarvish": 14-INT,
            "Elvish": 9-INT,
            "Giant": 15-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 14-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 9-INT,
            "Draconic": 9-INT,
            "Deep Speech": 100-INT,
            "Infernal": 100-INT,
            "Primordial": 3-INT,
            "Sylvan": 5-INT,
            "Undercommon": 100-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Beast":
        langs = {
            "Beastly Speech":1-INT,
            "Dwarvish": 20-INT,
            "Elvish": 10-INT,
            "Giant": 20-INT,
            "Gnomish": 10-INT,
            "Goblin": 10-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 10-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 10-INT,
            "Sylvan": 2-INT,
            "Undercommon": 20-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Beastfolk":
        langs = {
            "Beastly Speech":1-INT,
            "Dwarvish": 20-INT,
            "Elvish": 8-INT,
            "Giant": 15-INT,
            "Gnomish": 6-INT,
            "Goblin": 6-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 10-INT,
            "Celestial": 10-INT,
            "Draconic": 10-INT,
            "Deep Speech": 20-INT,
            "Infernal": 10-INT,
            "Primordial": 10-INT,
            "Sylvan": 4-INT,
            "Undercommon": 10-INT,
            f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if race == "Celestial":
        langs = {
            "Dwarvish": 10-INT,
            "Elvish": 8-INT,
            "Giant": 10-INT,
            "Gnomish": 10-INT,
            "Goblin": 10-INT,
            "Halfling": 10-INT,
            "Orc": 10-INT,
            "Abyssal": 8-INT,
            "Celestial": 1,
            "Draconic": 10-INT,
            "Deep Speech": 20-INT,
            "Infernal": 8-INT,
            "Primordial": 20-INT,
            "Sylvan": 6-INT,
            "Undercommon": 20-INT,
            "All languages":8-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
   
        if Dice(2): add_language(languages, "Telepathy. (60 feet).", 8-INT) 
        else: add_language(languages, "Telepathy. (120 feet).", 10-INT) 

    if race == "Construct":
        add_language(languages, "Understands the languages of its creator.", 1-INT) 
        add_language(languages, "All languages.", 5-INT) 

    if race == "Dragon":
        langs = {
            "Dwarvish": 8-INT,
            "Elvish": 8-INT,
            "Giant": 8-INT,
            "Gnomish": 8-INT,
            "Goblin": 8-INT,
            "Halfling": 8-INT,
            "Orc": 8-INT,
            "Abyssal": 8-INT,
            "Celestial": 8-INT,
            "Draconic": 1-INT,
            "Deep Speech": 10-INT,
            "Infernal": 8-INT,
            "Primordial": 10-INT,
            "Sylvan": 4-INT,
            "Undercommon": 10-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Dwarf":
        langs = {
            "Dwarvish": 1,
            "Elvish": 8-INT,
            "Giant": 6-INT,
            "Gnomish": 16-INT,
            "Goblin": 16-INT,
            "Halfling": 8-INT,
            "Orc": 20-INT,
            "Abyssal": 18-INT,
            "Celestial": 16-INT,
            "Draconic": 12-INT,
            "Deep Speech": 4-INT,
            "Infernal": 12-INT,
            "Primordial": 12-INT,
            "Sylvan": 21-INT,
            "Undercommon": 4-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Elf":
        langs = {
            "Dwarvish": 6-INT,
            "Elvish": 1-INT,
            "Giant": 12-INT,
            "Gnomish": 6-INT,
            "Goblin": 18-INT,
            "Halfling": 12-INT,
            "Orc": 20-INT,
            "Abyssal": 8-INT,
            "Celestial": 8-INT,
            "Draconic": 8-INT,
            "Deep Speech": 16-INT,
            "Infernal": 8-INT,
            "Primordial": 6-INT,
            "Sylvan": 4-INT,
            "Undercommon": 6-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
    if race == "Elemental":
        langs = {
            "Dwarvish": 8-INT,
            "Elvish": 8-INT,
            "Giant": 8-INT,
            "Gnomish": 8-INT,
            "Goblin": 18-INT,
            "Halfling": 18-INT,
            "Orc": 12-INT,
            "Abyssal": 12-INT,
            "Celestial": 12-INT,
            "Draconic": 12-INT,
            "Deep Speech": 20-INT,
            "Infernal": 12-INT,
            "Primordial": 1-INT,
            "Sylvan": 4-INT,
            "Undercommon": 10-INT,
            "Ignan": 4-INT,
            "Terran":4-INT,
            "Aquan":4-INT,
            "Auran":4-INT,
            
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if race == "Fey":
        langs = {
            "Dwarvish": 14-INT,
            "Elvish": 3-INT,
            "Giant": 10-INT,
            "Gnomish": 8-INT,
            "Goblin": 4-INT,
            "Halfling": 16-INT,
            "Orc": 16-INT,
            "Abyssal": 16-INT,
            "Celestial": 16-INT,
            "Draconic": 8-INT,
            "Deep Speech": 20-INT,
            "Infernal": 16-INT,
            "Primordial": 8-INT,
            "Sylvan": 1-INT,
            "Undercommon": 20-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Fiend":
        langs = {
            "Dwarvish": 4-INT,
            "Elvish": 4-INT,
            "Giant": 8-INT,
            "Gnomish": 4-INT,
            "Goblin": 2-INT,
            "Halfling": 12-INT,
            "Orc": 4-INT,
            "Abyssal": 2-INT,
            "Celestial": 25-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 2-INT,
            "Primordial": 22-INT,
            "Sylvan": 20-INT,
            "Undercommon": 8-INT,
            "Telepathy (60 ft.)": 10-INT,
            "Telepathy (120 ft.)": 12-INT,            
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Giant":
        langs = {
            "Dwarvish": 4-INT,
            "Elvish": 20-INT,
            "Giant": 1-INT,
            "Gnomish": 8-INT,
            "Goblin": 8-INT,
            "Halfling": 20-INT,
            "Orc": 8-INT,
            "Abyssal": 12-INT,
            "Celestial": 12-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 12-INT,
            "Primordial": 16-INT,
            "Sylvan": 8-INT,
            "Undercommon": 20-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Gnome":
        langs = {
            "Dwarvish": 3-INT,
            "Elvish": 3-INT,
            "Giant": 3-INT,
            "Gnomish": 1-INT,
            "Goblin": 6-INT,
            "Halfling": 6-INT,
            "Orc": 10-INT,
            "Abyssal": 12-INT,
            "Celestial": 12-INT,
            "Draconic": 12-INT,
            "Deep Speech": 12-INT,
            "Infernal": 12-INT,
            "Primordial": 12-INT,
            "Sylvan": 4-INT,
            "Undercommon": 12-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Goblin":
        langs = {
            "Dwarvish": 18-INT,
            "Elvish": 16-INT,
            "Giant": 10-INT,
            "Gnomish": 18-INT,
            "Goblin": 1-INT,
            "Halfling": 18-INT,
            "Orc": 4-INT,
            "Abyssal": 10-INT,
            "Celestial": 19-INT,
            "Draconic": 6-INT,
            "Deep Speech": 10-INT,
            "Infernal": 10-INT,
            "Primordial": 20-INT,
            "Sylvan": 2-INT,
            "Undercommon": 2-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Halfling":
        langs = {
            "Dwarvish": 4-INT,
            "Elvish": 4-INT,
            "Giant": 20-INT,
            "Gnomish": 4-INT,
            "Goblin": 20-INT,
            "Halfling": 1-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 4-INT,
            "Draconic": 6-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 18-INT,
            "Sylvan": 18-INT,
            "Undercommon": 20-INT
            }
        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if race == "Kobold":
        langs = {
            "Dwarvish": 6-INT,
            "Elvish": 18-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 8-INT,
            "Halfling": 20-INT,
            "Orc": 12-INT,
            "Abyssal": 8-INT,
            "Celestial": 10-INT,
            "Draconic": 1,
            "Deep Speech": 8-INT,
            "Infernal": 8-INT,
            "Primordial": 20-INT,
            "Sylvan": 16-INT,
            "Undercommon": 6-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
        
    if race == "Lizardfolk":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 10-INT,
            "Gnomish": 20-INT,
            "Goblin": 10-INT,
            "Halfling": 20-INT,
            "Orc": 4-INT,
            "Abyssal": 4-INT,
            "Celestial": 20-INT,
            "Draconic": 1,
            "Deep Speech": 4-INT,
            "Infernal": 4-INT,
            "Primordial": 4-INT,
            "Sylvan": 4-INT,
            "Undercommon": 20-INT,
            f"Beast Telepathy (Only Reptiles): The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3-INT,

        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Monstrosity":
        langs = {
            "Dwarvish": 10-INT,
            "Elvish": 22-INT,
            "Giant": 9-INT,
            "Gnomish": 25-INT,
            "Goblin": 11-INT,
            "Halfling": 22-INT,
            "Orc": 7-INT,
            "Abyssal": 4-INT,
            "Celestial": 22-INT,
            "Draconic": 6-INT,
            "Deep Speech": 1-INT,
            "Infernal": 5-INT,
            "Primordial": 12-INT,
            "Sylvan": 9-INT,
            "Undercommon": 1
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    
    if race == "Ooze":
        add_language(languages, "Telepathy. ", 1)

    if race == "Orc":
        langs = {
            "Dwarvish": 12-INT,
            "Elvish": 12-INT,
            "Giant": 4-INT,
            "Gnomish": 22-INT,
            "Goblin": 2-INT,
            "Halfling": 22-INT,
            "Orc": 1-INT,
            "Abyssal": 8-INT,
            "Celestial": 8-INT,
            "Draconic": 8-INT,
            "Deep Speech": 22-INT,
            "Infernal": 8-INT,
            "Primordial": 8-INT,
            "Sylvan": 8-INT,
            "Undercommon": 8-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Plant":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 5-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 10-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 2-INT,
            "Sylvan": 1-INT,
            "Undercommon": 8-INT,
            "Telepathy":4-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if race == "Snakefolk":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 2-INT,
            "Celestial": 20-INT,
            "Draconic": 1-INT,
            "Deep Speech": 2-INT,
            "Infernal": 10-INT,
            "Primordial": 4-INT,
            "Sylvan": 8-INT,
            "Undercommon": 20-INT,
            f"Beast Telepathy (Only Snakes): The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3-INT,

        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
        
    if race == "Undead":
        langs = {
            "Dwarvish": 6-INT,
            "Elvish": 6-INT,
            "Giant": 6-INT,
            "Gnomish": 6-INT,
            "Goblin": 6-INT,
            "Halfling": 6-INT,
            "Orc": 6-INT,
            "Abyssal": 2-INT,
            "Celestial": 2-INT,
            "Draconic": 6-INT,
            "Deep Speech": 2-INT,
            "Infernal": 2-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 4-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    # BACKGROUNDS
    if background == "base":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if background == "Druid":
        langs = {
            "Druidic":1,
            "Dwarvish": 20-INT,
            "Elvish": 5-INT,
            "Giant": 20-INT,
            "Gnomish": 10-INT,
            "Goblin": 10-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 16-INT,
            "Draconic": 4-INT,
            "Deep Speech": 21-INT,
            "Infernal": 20-INT,
            "Primordial": 4-INT,
            "Sylvan": 3-INT,
            "Undercommon": 20-INT,
            f"Beast Telepathy: {npc.title} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":3-INT,

        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    
    if background == "Bandit":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if background == "Bard":
        langs = {
            "Dwarvish": 6-INT,
            "Elvish": 6-INT,
            "Giant": 20-INT,
            "Gnomish": 6-INT,
            "Goblin": 6-INT,
            "Halfling": 6-INT,
            "Orc": 6-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 6-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Berserker":
        langs = {
            "Dwarvish": 6-INT,
            "Elvish": 20-INT,
            "Giant": 6-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 6-INT,
            "Abyssal": 12-INT,
            "Celestial": 20-INT,
            "Draconic": 16-INT,
            "Deep Speech": 16-INT,
            "Infernal": 12-INT,
            "Primordial": 16-INT,
            "Sylvan": 20-INT,
            "Undercommon": 6-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            


    if background == "Charlatan":
        langs = {
            "Dwarvish": 6-INT,
            "Elvish": 6-INT,
            "Giant": 20-INT,
            "Gnomish": 6-INT,
            "Goblin": 6-INT,
            "Halfling": 6-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Cultist":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 8-INT,
            "Celestial": 8-INT,
            "Draconic": 8-INT,
            "Deep Speech": 8-INT,
            "Infernal": 8-INT,
            "Primordial": 8-INT,
            "Sylvan": 20-INT,
            "Undercommon": 8-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Criminal":
        langs = {
            "Thieve's Cant":1-INT,
            "Dwarvish": 12-INT,
            "Elvish": 12-INT,
            "Giant": 20-INT,
            "Gnomish": 12-INT,
            "Goblin": 12-INT,
            "Halfling": 12-INT,
            "Orc": 12-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 4-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Expert":
        langs = {
            "Dwarvish": 5-INT,
            "Elvish": 5-INT,
            "Giant": 5-INT,
            "Gnomish": 5-INT,
            "Goblin": 19-INT,
            "Halfling": 19-INT,
            "Orc": 19-INT,
            "Abyssal": 19-INT,
            "Celestial": 5-INT,
            "Draconic": 19-INT,
            "Deep Speech": 19-INT,
            "Infernal": 19-INT,
            "Primordial": 19-INT,
            "Sylvan": 19-INT,
            "Undercommon": 19-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)

    if background == "Explorer":
        langs = {
            "Dwarvish": 4-INT,
            "Elvish": 4-INT,
            "Giant": 4-INT,
            "Gnomish": 4-INT,
            "Goblin": 4-INT,
            "Halfling": 4-INT,
            "Orc": 4-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 4-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Healer":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 10-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 4-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 4-INT,
            "Sylvan": 4-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Hero":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 6-INT,
            "Draconic": 6-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 6-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Hunter":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 6-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 6-INT,
            "Sylvan": 1-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Knight":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 6-INT,
            "Draconic": 6-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 6-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Mage":
        langs = {
            "Dwarvish": 6-INT,
            "Elvish": 6-INT,
            "Giant": 6-INT,
            "Gnomish": 6-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 6-INT,
            "Celestial": 6-INT,
            "Draconic": 6-INT,
            "Deep Speech": 6-INT,
            "Infernal": 6-INT,
            "Primordial": 6-INT,
            "Sylvan": 6-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Monk":
        langs = {
            "Dwarvish": 10-INT,
            "Elvish": 10-INT,
            "Giant": 10-INT,
            "Gnomish": 10-INT,
            "Goblin": 10-INT,
            "Halfling": 10-INT,
            "Orc": 10-INT,
            "Abyssal": 10-INT,
            "Celestial": 6-INT,
            "Draconic": 6-INT,
            "Deep Speech": 10-INT,
            "Infernal": 10-INT,
            "Primordial": 6-INT,
            "Sylvan": 10-INT,
            "Undercommon": 10-INT,
            f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":10-INT,

        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)




    if background == "Noble":
        langs = {
            "Dwarvish": 6-INT,
            "Elvish": 6-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 12-INT,
            "Draconic": 12-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Priest":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 6-INT,
            "Celestial": 6-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 6-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)



    if background == "Pirate":
        langs = {
            "Thieve's Cant":1-INT,
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 12-INT,
            "Infernal": 20-INT,
            "Primordial": 12-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Ranger":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 4-INT,
            "Giant": 4-INT,
            "Gnomish": 20-INT,
            "Goblin": 4-INT,
            "Halfling": 20-INT,
            "Orc": 4-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 6-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 6-INT,
            "Sylvan": 6-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Scholar":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 6-INT,
            "Celestial": 6-INT,
            "Draconic": 6-INT,
            "Deep Speech": 6-INT,
            "Infernal": 6-INT,
            "Primordial": 6-INT,
            "Sylvan": 6-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Shaman":
        langs = {
            "Druidic":1,
            "Dwarvish": 20-INT,
            "Elvish": 6-INT,
            "Giant": 6-INT,
            "Gnomish": 20-INT,
            "Goblin": 6-INT,
            "Halfling": 20-INT,
            "Orc": 6-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 8-INT,
            "Sylvan": 1-INT,
            "Undercommon": 20-INT,
            f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":10-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Spy":
        langs = {
            "Thieve's Cant":1,
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if background == "Traveler":
        langs = {
            "Dwarvish": 5-INT,
            "Elvish": 5-INT,
            "Giant": 5-INT,
            "Gnomish": 5-INT,
            "Goblin": 5-INT,
            "Halfling": 5-INT,
            "Orc": 5-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 12-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT,
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)


    if background == "Urchin":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            

    if background == "Warrior":
        langs = {
            "Dwarvish": 6-INT,
            "Elvish": 6-INT,
            "Giant": 6-INT,
            "Gnomish": 6-INT,
            "Goblin": 6-INT,
            "Halfling": 6-INT,
            "Orc": 6-INT,
            "Abyssal": 20-INT,
            "Celestial": 20-INT,
            "Draconic": 20-INT,
            "Deep Speech": 20-INT,
            "Infernal": 20-INT,
            "Primordial": 20-INT,
            "Sylvan": 20-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            



    if background == "Warlock":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 20-INT,
            "Gnomish": 20-INT,
            "Goblin": 20-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 6-INT,
            "Celestial": 6-INT,
            "Draconic": 6-INT,
            "Deep Speech": 6-INT,
            "Infernal": 6-INT,
            "Primordial": 6-INT,
            "Sylvan": 6-INT,
            "Undercommon": 20-INT
        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            


    if background == "Witch":
        langs = {
            "Dwarvish": 20-INT,
            "Elvish": 20-INT,
            "Giant": 12-INT,
            "Gnomish": 20-INT,
            "Goblin": 6-INT,
            "Halfling": 20-INT,
            "Orc": 20-INT,
            "Abyssal": 6-INT,
            "Celestial": 6-INT,
            "Draconic": 6-INT,
            "Deep Speech": 6-INT,
            "Infernal": 6-INT,
            "Primordial": 6-INT,
            "Sylvan": 12-INT,
            "Undercommon": 20-INT,
            f"Beast Telepathy: The {npc.race} can magically command any animal it shares an affinity to within 120 feet of it, using a limited telepathy.":10-INT,

        }

        for lang, chance in langs.items():
            add_language(languages, lang, chance)
            
    return "Common" + ", ".join(languages)

