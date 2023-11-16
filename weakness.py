import dnd
import npc_class as NPC
import random


def Extra_Weaknesses(npc):
    race= npc.race
    background= npc.background
    lvl = npc.level
    # Definitions of extra weaknesses
    freeze = f"\n- Freeze: If the {race} takes cold damage, it partially freezes; All its speed is reduced by 20 feet until the end of its next turn."



    
    # Dictionary to store possible extra weaknesses for each race
    extra_weaknesses_race = {
        "Aberration": [],
        "Beast":[],
        "Beastfolk": [],
        "Celestial": [],
        "Construct": [],
        "Dragon":[],
        "Elf": [],
        "Elemental":[freeze],
        "Fey": [],
        "Fiend": [freeze],
        "Goblin": [],
        "Lizardfolk":[freeze],
        "Orc": [],
        "Snakefolk":[freeze],
    }

    # Dictionary to store possible extra weaknesses for each background
    extra_weaknesses_background = {
        "Noble": [],
        "Berserker": [],
        "Scholar":[],

        }

    # Fetch the extra weaknesses for the selected race and background
    possible_extra_weaknesses_race = extra_weaknesses_race.get(race, [])
    possible_extra_weaknesses_background = extra_weaknesses_background.get(background, [])

    # Combine race and background weaknesses
    possible_extra_weaknesses = possible_extra_weaknesses_race + possible_extra_weaknesses_background

    # Determine the number of weaknesses to select, this number can be changed as needed
    number_of_weaknesses_to_select = PB(lvl)  # for example

    # Randomly determine which extra weaknesses the character has
    if possible_extra_weaknesses and len(possible_extra_weaknesses) >= number_of_weaknesses_to_select:
        selected_weaknesses = random.sample(possible_extra_weaknesses, number_of_weaknesses_to_select)
        formatted_weaknesses = [weaknesses.format(race) for weaknesses in selected_weaknesses]
    else:
        formatted_weaknesses = [""]

    # Join the list of formatted weaknesses into a single string separated by newlines or any other separator
    formatted_weaknesses_string = '\n'.join(formatted_weaknesses)

    return formatted_weaknesses_string
