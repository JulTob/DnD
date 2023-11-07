import random

def Race():
    race_weights = {
        "Human": 26,
        "Aberration": 16,
        "Aven": 16,
        "Beast": 18,
        "Beastfolk": 17,
        "Celestial": 16,
        "Construct": 16,
        "Dragon": 17,
        "Dwarf": 20,
        "Elf": 20,
        "Elemental": 17,
        "Fey": 16,
        "Fiend": 16,
        "Giant": 16,
        "Gnome": 17,
        "Goblin": 20,
        "Halfling": 19,
        "Kobold": 20,
        "Lizardfolk": 16,
        "Monstrosity": 17,
        "Ooze": 16,
        "Orc": 21,
        "Plant": 17,
        "Snakefolk": 16,
        "Undead": 19,
        "Beholder": 0,
        "Vampire":0,
        "": 0
    }
    
    return random.choices(list(race_weights.keys()), weights=race_weights.values(), k=1)[0]
