import dnd
import npc_class as NPC
import random


def PB(level):
    return dnd.PB(level)

def Dice(D=6,N=1):
    return dnd.Dice(D,N)



def Resistances(npc):

    race = npc.race
    background = npc.background
    pb = npc.pb

    damage_types = [
        "acid", "bludgeoning", "cold", "fire", "force", 
        "lightning", "necrotic", "piercing", "poison", 
        "psychic", "radiant", "slashing", "thunder",
        "bludgeoning, piercing, and slashing from nonmagical attacks"

    ]
    race_damage_tendencies = {
        "Dragon": {
            "acid": {
                "Immune": pb//2, "Resistant": pb//2, "None": pb, "Vulnerable": pb//3},
            "bludgeoning": {
                "Immune": pb//6, "Resistant": pb//2, "None": pb, "Vulnerable": pb//6},
            "cold": {
                "Immune": pb//3, "Resistant": pb//2, "None": pb, "Vulnerable": pb//6},
            "fire": {
                "Immune": pb//3, "Resistant": pb//2, "None": pb, "Vulnerable": pb//6},
            "force": {
                "Immune": pb//12, "Resistant": pb//6, "None": pb*2, "Vulnerable": pb//2},
            "lightning": {
                "Immune": pb//3, "Resistant": pb//2, "None": pb, "Vulnerable": pb//6},
            "necrotic": {
                "Immune": pb//6, "Resistant": pb//2, "None": pb, "Vulnerable": pb//6},
            "piercing": {
                "Immune": pb//6, "Resistant": pb, "None": 2*pb, "Vulnerable": pb//6},
            "poison": {
                "Immune": pb//6, "Resistant": (pb+1)//2, "None": pb, "Vulnerable": pb//6},
            "psychic": {
                "Immune": pb//6, "Resistant": pb//3, "None": pb, "Vulnerable": pb//6},
            "radiant": {
                "Immune": pb//7, "Resistant": pb//4, "None": pb, "Vulnerable": pb//6},
            "slashing": {
                "Immune": pb//6, "Resistant": pb//3, "None": pb, "Vulnerable": pb//6},
            "thunder": {
                "Immune": pb//6, "Resistant": pb//2, "None": pb, "Vulnerable": pb//6},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": pb//6, "Resistant": pb//3, "None": pb, "Vulnerable": 0},
            },

        "Human": {
                "acid":{
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "bludgeoning": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "cold": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "fire": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "force": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "lightning": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "necrotic": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "piercing": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "poison": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "psychic": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "radiant": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "slashing": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "thunder": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb//3},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": pb//8, "Resistant": pb//3, "None": pb*2, "Vulnerable": 0},
                },
        "Aberration": {
                "acid": {"Immune": 2, "Resistant": 5, "None": 3, "Vulnerable": 0},
                "bludgeoning": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
                "cold": {"Immune": 2, "Resistant": 4, "None": 3, "Vulnerable": 1},
                "fire": {"Immune": 2, "Resistant": 3, "None": 4, "Vulnerable": 1},
                "force": {"Immune": 2, "Resistant": 5, "None": 3, "Vulnerable": 10},
                "lightning": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
                "necrotic": {"Immune": 5, "Resistant": 3, "None": 2, "Vulnerable": 0},
                "piercing": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
                "poison": {"Immune": 5, "Resistant": 3, "None": 2, "Vulnerable": 0},
                "psychic": {"Immune": 3, "Resistant": 5, "None": 2, "Vulnerable": 0},
                "radiant": {"Immune": 1, "Resistant": 2, "None": 4, "Vulnerable": 3},
                "slashing": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
                "thunder": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": 2, "Resistant": 6, "None": 2, "Vulnerable": 0},
                },
        "Aven": {
                "acid": {
                    "Immune": 0, "Resistant": 2, "None": 10, "Vulnerable": 1},
                "bludgeoning": {
                    "Immune": 0, "Resistant": 4, "None": 10, "Vulnerable": 2},
                "cold": {
                    "Immune": 1, "Resistant": 3, "None": 10, "Vulnerable": 3},
                "fire": {
                    "Immune": 0, "Resistant": 2, "None": 10, "Vulnerable": 3},
                "force": {
                    "Immune": 0, "Resistant": 0, "None": 10, "Vulnerable": 2},
                "lightning": {
                    "Immune": 1, "Resistant": 4, "None": 10, "Vulnerable": 1},
                "necrotic": {
                    "Immune": 0, "Resistant": 2, "None": 10, "Vulnerable": 2},
                "piercing": {
                    "Immune": 0, "Resistant": 3, "None": 10, "Vulnerable": 3},
                "poison": {
                    "Immune": 0, "Resistant": 2, "None": 10, "Vulnerable": 2},
                "psychic": {
                    "Immune": 0, "Resistant": 2, "None": 10, "Vulnerable": 1},
                "radiant": {
                    "Immune": 0, "Resistant": 2, "None": 10, "Vulnerable": 1},
                "slashing": {
                    "Immune": 0, "Resistant": 3, "None": 10, "Vulnerable": 3},
                "thunder": {
                    "Immune": 0, "Resistant": 3, "None": 10, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": 0, "Resistant": pb//2, "None": pb, "Vulnerable": 0},
                },
        "Beast": {
                "acid": {"Immune": 1, "Resistant": 3, "None": 6, "Vulnerable": 2},
                "bludgeoning": {"Immune": 2, "Resistant": 4, "None": 3, "Vulnerable": 3},
                "cold": {"Immune": 2, "Resistant": 4, "None": 4, "Vulnerable": 2},
                "fire": {"Immune": 1, "Resistant": 3, "None": 5, "Vulnerable": 3},
                "force": {"Immune": 1, "Resistant": 1, "None": 8, "Vulnerable": 2},
                "lightning": {"Immune": 2, "Resistant": 3, "None": 5, "Vulnerable": 2},
                "necrotic": {"Immune": 1, "Resistant": 2, "None": 6, "Vulnerable": 3},
                "piercing": {"Immune": 2, "Resistant": 4, "None": 3, "Vulnerable": 3},
                "poison": {"Immune": 3, "Resistant": 4, "None": 2, "Vulnerable": 3},
                "psychic": {"Immune": 1, "Resistant": 2, "None": 7, "Vulnerable": 2},
                "radiant": {"Immune": 1, "Resistant": 2, "None": 6, "Vulnerable": 3},
                "slashing": {"Immune": 2, "Resistant": 4, "None": 3, "Vulnerable": 3},
                "thunder": {"Immune": 2, "Resistant": 3, "None": 5, "Vulnerable": 2},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": 4, "Resistant": 3, "None": 2, "Vulnerable": 3},
                },
        "Beastfolk": {
                "acid": {"Immune": 1, "Resistant": 4, "None": 6, "Vulnerable": 1},
                "bludgeoning": {"Immune": 2, "Resistant": 5, "None": 4, "Vulnerable": 1},
                "cold": {"Immune": 3, "Resistant": 5, "None": 3, "Vulnerable": 1},
                "fire": {"Immune": 2, "Resistant": 4, "None": 4, "Vulnerable": 2},
                "force": {"Immune": 1, "Resistant": 2, "None": 8, "Vulnerable": 1},
                "lightning": {"Immune": 2, "Resistant": 3, "None": 6, "Vulnerable": 1},
                "necrotic": {"Immune": 1, "Resistant": 2, "None": 7, "Vulnerable": 2},
                "piercing": {"Immune": 2, "Resistant": 5, "None": 4, "Vulnerable": 1},
                "poison": {"Immune": 4, "Resistant": 5, "None": 2, "Vulnerable": 1},
                "psychic": {"Immune": 1, "Resistant": 3, "None": 7, "Vulnerable": 1},
                "radiant": {"Immune": 1, "Resistant": 3, "None": 6, "Vulnerable": 2},
                "slashing": {"Immune": 2, "Resistant": 5, "None": 4, "Vulnerable": 1},
                "thunder": {"Immune": 3, "Resistant": 5, "None": 3, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered": {
                    "Immune": 10, "Resistant": 6, "None": 4, "Vulnerable": 0},
                },

        "Celestial": {
                "acid": {
                    "Immune": 5, "Resistant": 7, "None": 3, "Vulnerable": 1},
                "bludgeoning": {
                    "Immune": 3, "Resistant": 8, "None": 4, "Vulnerable": 1},
                "cold": {
                    "Immune": 6, "Resistant": 7, "None": 3, "Vulnerable": 1},
                "fire": {
                    "Immune": 6, "Resistant": 6, "None": 3, "Vulnerable": 1},
                "force": {
                    "Immune": 6, "Resistant": 8, "None": 4, "Vulnerable": 1},
                "lightning": {
                    "Immune": 5, "Resistant": 8, "None": 4, "Vulnerable": 1},
                "necrotic": {
                    "Immune": 9, "Resistant": 5, "None": 3, "Vulnerable": 1},
                "piercing": {
                    "Immune": 3, "Resistant": 8, "None": 4, "Vulnerable": 1},
                "poison": {
                    "Immune": 9, "Resistant": 4, "None": 3, "Vulnerable": 1},
                "psychic": {
                    "Immune": 6, "Resistant": 6, "None": 3, "Vulnerable": 1},
                "radiant": {
                    "Immune": 11, "Resistant": 3, "None": 1, "Vulnerable": 1},
                "slashing": {
                    "Immune": 3, "Resistant": 8, "None": 4, "Vulnerable": 1},
                "thunder": {
                    "Immune": 5, "Resistant": 7, "None": 3, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": 6, "Resistant": 6, "None": 3, "Vulnerable": 1},
                "bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered": {
                    "Immune": 9, "Resistant": 5, "None": 5, "Vulnerable": 1},
                },
        "Construct": {
                "acid": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "bludgeoning": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "cold": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "fire": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "force": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "lightning": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "necrotic": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "piercing": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "poison": {
                    "Immune": pb, "Resistant": pb//2, "None": 0, "Vulnerable": 0},
                "psychic": {
                    "Immune": pb//2, "Resistant": pb//3, "None": pb, "Vulnerable": pb//2},
                "radiant": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "slashing": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "thunder": {
                    "Immune": pb//5, "Resistant": pb//3, "None": pb+2, "Vulnerable": pb//2},
                "bludgeoning, piercing, and slashing from nonmagical attacks": {
                    "Immune": pb//2, "Resistant": pb+1, "None": pb//2, "Vulnerable": 0},
                },
        "Dwarf": {
            "acid": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "bludgeoning": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "cold": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "fire": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "lightning": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 1, "None": 8, "Vulnerable": 1},
            "piercing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "poison": {
                "Immune": 3, "Resistant": 7, "None": 0, "Vulnerable": 0},
            "psychic": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "slashing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "thunder": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            },
        "Elf": {
            "acid": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
            "bludgeoning": {"Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 1},
            "cold": {"Immune": 1, "Resistant": 5, "None": 4, "Vulnerable": 0},
            "fire": {"Immune": 1, "Resistant": 5, "None": 4, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 4, "None": 6, "Vulnerable": 0},
            "lightning": {"Immune": 1, "Resistant": 4, "None": 4, "Vulnerable": 1},
            "necrotic": {"Immune": 1, "Resistant": 2, "None": 5, "Vulnerable": 2},
            "piercing": {"Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 1},
            "poison": {"Immune": 3, "Resistant": 5, "None": 2, "Vulnerable": 0},
            "psychic": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "radiant": {"Immune": 1, "Resistant": 3, "None": 5, "Vulnerable": 1},
            "slashing": {"Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 1},
            "thunder": {"Immune": 0, "Resistant": 3, "None": 6, "Vulnerable": 1},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            },
        "Elemental": {
            "acid": {
                "Immune": 5, "Resistant": 6, "None": 5, "Vulnerable": 5},
            "bludgeoning": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 6},
            "cold": {
                "Immune": 6, "Resistant": 6, "None": 8, "Vulnerable": 7},
            "fire":{
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 6},
            "force": {
                "Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 15},
            "lightning": {
                "Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "necrotic": {
                "Immune": 5, "Resistant": 5, "None": 10, "Vulnerable": 5},
            "piercing": {
                "Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "poison": {
                "Immune": 10, "Resistant": 5, "None": 0, "Vulnerable": 0},
            "psychic": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 5},
            "radiant": {
                "Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "slashing": {
                "Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "thunder": {
                "Immune": 6, "Resistant": 6, "None": 7, "Vulnerable": 6},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 6, "Resistant": 7, "None": 10, "Vulnerable": 0},
            },
        "Fey": {
            "acid": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "bludgeoning": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "cold": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "fire": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "lightning": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 2, "None": 2, "Vulnerable": 10},
            "piercing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "poison": {"Immune": 10, "Resistant": 0, "None": 0, "Vulnerable": 0},
            "psychic": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 2, "None": 2, "Vulnerable": 10},
            "slashing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "thunder": {"Immune": 2, "Resistant": 8, "None": 5, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 10, "None": 0, "Vulnerable": 0},
            },
        "Fiend": {
            "acid": {
                "Immune": pb//2, "Resistant": pb, "None": pb//2, "Vulnerable": pb//5},
            "bludgeoning": {
                "Immune": 0, "Resistant": 0, "None": pb, "Vulnerable": 0},
            "cold": {
                "Immune": pb//2, "Resistant": pb, "None": pb//3, "Vulnerable": pb//4},
            "fire": {
                "Immune": pb, "Resistant": pb//2, "None": pb//3, "Vulnerable": pb//4},
            "force": {
                "Immune": 0, "Resistant": pb//4, "None": pb, "Vulnerable": pb//4},
            "lightning": {
                "Immune": pb//2, "Resistant": pb, "None": pb//2, "Vulnerable": pb//3},
            "necrotic": {
                "Immune": pb, "Resistant": pb//2, "None": pb//3, "Vulnerable": pb//4},
            "piercing": {
                "Immune": 0, "Resistant": pb//2, "None": pb, "Vulnerable": 0},
            "poison": {
                "Immune": 2*pb, "Resistant": pb, "None": pb//2, "Vulnerable": pb//3},
            "psychic": {
                "Immune": pb//3, "Resistant": pb, "None": pb, "Vulnerable": pb//3},
            "radiant": {
                "Immune": pb//5, "Resistant": pb//4, "None": pb//2, "Vulnerable": pb*2},
            "slashing": {
                "Immune": 0, "Resistant": 0, "None": pb, "Vulnerable": 0},
            "thunder": {
                "Immune": pb//2, "Resistant": pb, "None": pb//2, "Vulnerable": pb//3},
            "bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered": {
                "Immune": pb*2, "Resistant": pb, "None": pb//2, "Vulnerable": pb//3},
            },
        "Giant": {
            "acid": {
                "Immune": 0, "Resistant": pb//3, "None": pb*2, "Vulnerable": pb+1},
            "bludgeoning": {
                "Immune": 0, "Resistant": pb, "None": pb//2, "Vulnerable": 0},
            "cold": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//4},
            "fire": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//4},
            "force": {
                "Immune": 0, "Resistant": 0, "None": pb*2, "Vulnerable": pb//4},
            "lightning": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//4},
            "necrotic": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//4},
            "piercing": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//4},
            "poison": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//4},
            "psychic": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//3},
            "radiant": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//4},
            "slashing": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//4},
            "thunder": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//4},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": pb//3, "Resistant": pb, "None": pb*2, "Vulnerable": pb//4},
            },
        "Gnome": {
            "acid": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "bludgeoning": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "cold": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "fire": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "lightning": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "piercing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "poison": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "psychic": {"Immune": 0, "Resistant": 6, "None": 10, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "slashing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "thunder": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            },
        "Goblin": {
            "acid": {
                "Immune": 0, "Resistant": 4, "None": 10, "Vulnerable": 5},
            "bludgeoning": {
                "Immune": 1, "Resistant": 4, "None": 18, "Vulnerable": 10},
            "cold": {
                "Immune": 2, "Resistant": 8, "None": 16, "Vulnerable": 4},
            "fire": {
                "Immune": 0, "Resistant": 4, "None": 8, "Vulnerable": 6},
            "force": {
                "Immune": 0, "Resistant": 1, "None": 10, "Vulnerable": 8},
            "lightning": {
                "Immune": 1, "Resistant": 7, "None": 12, "Vulnerable": 4},
            "necrotic": {
                "Immune": 1, "Resistant": 4, "None": 16, "Vulnerable": 8},
            "piercing": {
                "Immune": 1, "Resistant": 4, "None": 16, "Vulnerable": 8},
            "poison": {
                "Immune": 4, "Resistant": 8, "None": 6, "Vulnerable": 1},
            "psychic": {
                "Immune": 2, "Resistant": 4, "None": 16, "Vulnerable": 10},
            "radiant": {
                "Immune": 1, "Resistant": 2, "None": 20, "Vulnerable": 10},
            "slashing": {
                "Immune": 1, "Resistant": 4, "None": 12, "Vulnerable": 12},
            "thunder": {
                "Immune": 1, "Resistant": 10, "None": 16, "Vulnerable": 4},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 1, "Resistant": 1, "None": 20, "Vulnerable": 0},
            },
        "Halfling": {
            "acid": {"Immune": 1, "Resistant": 4, "None": 10, "Vulnerable": 0},
            "bludgeoning": {"Immune": 1, "Resistant": 6, "None": 8, "Vulnerable": 0},
            "cold": {"Immune": 1, "Resistant": 5, "None": 9, "Vulnerable": 0},
            "fire": {"Immune": 1, "Resistant": 5, "None": 9, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 2, "None": 13, "Vulnerable": 0},
            "lightning": {"Immune": 1, "Resistant": 5, "None": 9, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 3, "None": 12, "Vulnerable": 0},
            "piercing": {"Immune": 1, "Resistant": 7, "None": 7, "Vulnerable": 0},
            "poison": {"Immune": 3, "Resistant": 10, "None": 2, "Vulnerable": 0},
            "psychic": {"Immune": 1, "Resistant": 5, "None": 9, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 3, "None": 12, "Vulnerable": 0},
            "slashing": {"Immune": 1, "Resistant": 7, "None": 7, "Vulnerable": 0},
            "thunder": {"Immune": 1, "Resistant": 5, "None": 9, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 5, "None": 10, "Vulnerable": 0},
            },
        "Kobold": {
            "acid": {
                "Immune": 1, "Resistant": 2, "None": 12, "Vulnerable": 4},
            "bludgeoning": {
                "Immune": 0, "Resistant": 1, "None": 12, "Vulnerable": 8},
            "cold": {
                "Immune": 1, "Resistant": 2, "None": 12, "Vulnerable": 5},
            "fire": {
                "Immune": 2, "Resistant": 4, "None": 12, "Vulnerable": 3},
            "force": {
                "Immune": 0, "Resistant": 1, "None": 10, "Vulnerable": 4},
            "lightning": {
                "Immune": 1, "Resistant": 2, "None": 12, "Vulnerable": 4},
            "necrotic": {
                "Immune": 0, "Resistant": 2, "None": 12, "Vulnerable": 6},
            "piercing": {
                "Immune": 1, "Resistant": 2, "None": 13, "Vulnerable": 0},
            "poison": {
                "Immune": 2, "Resistant": 3, "None": 12, "Vulnerable": 3},
            "psychic": {
                "Immune": 0, "Resistant": 1, "None": 12, "Vulnerable": 5},
            "radiant": {
                "Immune": 0, "Resistant": 1, "None": 12, "Vulnerable": 5},
            "slashing": {
                "Immune": 0, "Resistant": 1, "None": 12, "Vulnerable": 7},
            "thunder": {
                "Immune": 1, "Resistant": 2, "None": 12, "Vulnerable": 5},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 2, "None": 12, "Vulnerable": 0},
            },
        "Lizardfolk": {
            "acid": {
                "Immune": 3, "Resistant": 6, "None": 9, "Vulnerable": 1},
            "bludgeoning": {
                "Immune": 2, "Resistant": 7, "None": 9, "Vulnerable": 1},
            "cold": {
                "Immune": 3, "Resistant": 6, "None": 10, "Vulnerable": 1},
            "fire": {
                "Immune": 2, "Resistant": 5, "None": 10, "Vulnerable": 3},
            "force": {
                "Immune": 0, "Resistant": 4, "None": 11, "Vulnerable": 4},
            "lightning": {
                "Immune": 2, "Resistant": 6, "None": 8, "Vulnerable": 3},
            "necrotic": {
                "Immune": 1, "Resistant": 4, "None": 10, "Vulnerable": 5},
            "piercing": {
                "Immune": 2, "Resistant": 10, "None": 7, "Vulnerable": 2},
            "poison": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "psychic": {
                "Immune": 2, "Resistant": 3, "None": 10, "Vulnerable": 6},
            "radiant": {
                "Immune": 1, "Resistant": 3, "None": 10, "Vulnerable": 6},
            "slashing": {
                "Immune": 2, "Resistant": 8, "None": 8, "Vulnerable": 3},
            "thunder": {
                "Immune": 2, "Resistant": 5, "None": 10, "Vulnerable": 3},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 4, "Resistant": 7, "None": 10, "Vulnerable": 1},
            },

        "Monstrosity": {
            "acid": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "bludgeoning": {
                "Immune": 3, "Resistant": 6, "None": 6, "Vulnerable": 4},
            "cold": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "fire": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "force": {
                "Immune": 3, "Resistant": 3, "None": 6, "Vulnerable": 6},
            "lightning": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "necrotic": {
                "Immune": 4, "Resistant": 4, "None": 6, "Vulnerable": 5},
            "piercing": {
                "Immune": 3, "Resistant": 6, "None": 6, "Vulnerable": 4},
            "poison": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "psychic": {
                "Immune": 4, "Resistant": 4, "None": 6, "Vulnerable": 5},
            "radiant": {
                "Immune": 3, "Resistant": 4, "None": 6, "Vulnerable": 6},
            "slashing": {
                "Immune": 3, "Resistant": 6, "None": 6, "Vulnerable": 4},
            "thunder": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 6, "Resistant": 6, "None": 6, "Vulnerable": 1},
            },
        "Ooze": {
            "acid": {
                "Immune": 11, "Resistant": 1, "None": 6, "Vulnerable": 1},
            "bludgeoning": {
                "Immune": 11, "Resistant": 6, "None": 1, "Vulnerable": 1},
            "cold": {
                "Immune": 1, "Resistant": 6, "None": 6, "Vulnerable": 6},
            "fire": {
                "Immune": 1, "Resistant": 6, "None": 6, "Vulnerable": 6},
            "force": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "lightning": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "necrotic": {"Immune": 5, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "piercing": {"Immune": 10, "Resistant": 5, "None": 0, "Vulnerable": 0},
            "poison": {"Immune": 10, "Resistant": 0, "None": 5, "Vulnerable": 0},
            "psychic": {"Immune": 10, "Resistant": 0, "None": 5, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "slashing": {"Immune": 10, "Resistant": 5, "None": 0, "Vulnerable": 0},
            "thunder": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 5},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 10, "Resistant": 0, "None": 0, "Vulnerable": 0},
            },
        "Orc": {
            "acid": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "bludgeoning": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "cold": {
                "Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "fire": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "force": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "lightning": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "necrotic": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "piercing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "poison": {"Immune": 1, "Resistant": 4, "None": 5, "Vulnerable": 0},
            "psychic": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "radiant": {"Immune": 0, "Resistant": 2, "None": 8, "Vulnerable": 0},
            "slashing": {"Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            "thunder": {"Immune": 0, "Resistant": 3, "None": 7, "Vulnerable": 0},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 0, "Resistant": 5, "None": 5, "Vulnerable": 0},
            },
        
        "Plant": {
            "acid": {
                "Immune": pb//2, "Resistant": pb-1, "None": 2*pb, "Vulnerable": pb},
            "bludgeoning": {
                "Immune": pb//2, "Resistant": pb-1, "None": 2*pb, "Vulnerable": pb},
            "cold": {
                "Immune": pb//2, "Resistant": pb-1, "None": 2*pb, "Vulnerable": pb},
            "fire": {
                "Immune": pb//8, "Resistant": pb//4, "None": pb, "Vulnerable": 2*pb},
            "force": {
                "Immune": 0, "Resistant": pb//2, "None": pb, "Vulnerable": pb+1},
            "lightning": {
                "Immune": (pb-1)//2, "Resistant": pb//2, "None": pb*2, "Vulnerable": pb},
            "necrotic": {
                "Immune": (pb-1)//4, "Resistant": pb//3, "None": pb, "Vulnerable": pb*2},
            "piercing": {
                "Immune": (pb-1)//3, "Resistant": pb//2, "None": pb+3, "Vulnerable": pb+1},
            "poison": {
                "Immune": pb*2, "Resistant": pb, "None": 0, "Vulnerable": 0},
            "psychic": {
                "Immune": pb, "Resistant": pb, "None": pb, "Vulnerable": 0},
            "radiant": {
                "Immune": pb//2, "Resistant": pb, "None": pb, "Vulnerable": pb//2},
            "slashing": {
                "Immune": 0, "Resistant": pb//3, "None": pb//2, "Vulnerable": pb},
            "thunder": {
                "Immune": 0, "Resistant": pb//2, "None": 2*pb, "Vulnerable": pb},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": pb//4, "Resistant": pb, "None": pb, "Vulnerable": 0},
            },
        

        "Snakefolk": {
            "acid": {"Immune": 2, "Resistant": 5, "None": 7, "Vulnerable": 1},
            "bludgeoning": {"Immune": 1, "Resistant": 3, "None": 8, "Vulnerable": 3},
            "cold": {"Immune": 1, "Resistant": 3, "None": 7, "Vulnerable": 4},
            "fire": {"Immune": 2, "Resistant": 5, "None": 6, "Vulnerable": 2},
            "force": {"Immune": 1, "Resistant": 2, "None": 10, "Vulnerable": 2},
            "lightning": {"Immune": 1, "Resistant": 4, "None": 8, "Vulnerable": 2},
            "necrotic": {"Immune": 1, "Resistant": 3, "None": 8, "Vulnerable": 3},
            "piercing": {"Immune": 1, "Resistant": 8, "None": 6, "Vulnerable": 0},
            "poison": {
                "Immune": 2*pb, "Resistant": pb, "None": pb//4, "Vulnerable": pb//8},
            "psychic": {"Immune": 1, "Resistant": 4, "None": 8, "Vulnerable": 2},
            "radiant": {"Immune": 0, "Resistant": 3, "None": 9, "Vulnerable": 3},
            "slashing": {"Immune": 1, "Resistant": 6, "None": 6, "Vulnerable": 2},
            "thunder": {"Immune": 1, "Resistant": 3, "None": 9, "Vulnerable": 2},
            "bludgeoning, piercing, and slashing from nonmagical attacks": {
                "Immune": 1, "Resistant": 7, "None": 5, "Vulnerable": 2},
            },
        "Undead": {
            "acid": {
                "Immune": pb//3, "Resistant": pb, "None": pb+2, "Vulnerable": pb//2},
            "bludgeoning": {
                "Immune": pb//3, "Resistant": pb, "None": pb+2, "Vulnerable": pb},
            "cold": {
                "Immune": pb-1, "Resistant": pb, "None": pb//3, "Vulnerable": pb//2},
            "fire": {
                "Immune": pb//3, "Resistant": pb-1, "None": pb+1, "Vulnerable": pb-1},
            "force": {
                "Immune": 0, "Resistant": pb//10, "None": 2*pb, "Vulnerable": pb//3},
            "lightning": {
                "Immune": pb//3, "Resistant": pb-1, "None": pb+1, "Vulnerable": pb//3},
            "necrotic": {
                "Immune": 2*pb, "Resistant": pb, "None": pb//6, "Vulnerable": pb//10},
            "piercing": {
                "Immune": pb//3, "Resistant": pb, "None": pb, "Vulnerable": pb//3},
            "poison": {
                "Immune": 2*pb, "Resistant": pb, "None": 0, "Vulnerable": 0},
            "psychic": {
                "Immune": pb//3, "Resistant": pb//2, "None": pb, "Vulnerable": pb-1},
            "radiant": {
                "Immune": pb//6, "Resistant": pb//3, "None": pb-2, "Vulnerable": 2*pb},
            "slashing": {
                "Immune": pb//3, "Resistant": pb, "None": pb, "Vulnerable": pb//3},
            "thunder": {
                "Immune": pb//3, "Resistant": pb-1, "None": pb+2, "Vulnerable": pb//2},
            "bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered": {
                "Immune": pb+3, "Resistant": pb, "None": pb, "Vulnerable": 0},
            },


        }
            
    # Fetch the damage tendencies for the selected race, or use an empty dictionary if the race is not defined
    damage_tendencies = race_damage_tendencies.get(race, {})

    # Randomly determine resistances, immunities, and vulnerabilities based on the damage tendencies
    resistances = []
    immunities = []
    vulnerabilities = []
    for damage_type, tendencies in damage_tendencies.items():
        category = random.choices(list(tendencies.keys()), list(tendencies.values()))[0]
        if category == "Resistant":
            resistances.append(damage_type)
        elif category == "Immune":
            immunities.append(damage_type)
        elif category == "Vulnerable":
            vulnerabilities.append(damage_type)

            
    # Convert lists to strings
    resistances_str = "; ".join(resistances) if resistances else "None"
    immunities_str = "; ".join(immunities) if immunities else "None"
    vulnerabilities_str = "; ".join(vulnerabilities) if vulnerabilities else "None"

    # Compile the final string
    result = f" \nImmunities: {immunities_str}. \nResistances: {resistances_str}. \nVulnerabilities: {vulnerabilities_str}."
    return result


def ConditionImmunities(npc):
    race=npc.race
    background=npc.background
    
    # Condition Immunities
    condition_immunities = []

    conditions = [
        "Blinded", "Charmed", "Deafened", "Frightened", "Grappled",
        "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Prone",
        "Restrained", "Stunned", "Unconscious"
    ]

    race_condition_immunities = {
"Human": {      "Blinded": 10,  "Charmed": 5,   "Deafened": 10,     "Frightened": 10/2,     "Grappled": 100,    "Incapacitated": 100,   "Paralyzed": 10/1,  "Petrified": 100,   "Poisoned": 10/3,   "Prone": 100,   "Restrained": 100,  "Stunned": 10,      "Unconscious": 100,},   
"Aberration": { "Blinded": 2,   "Charmed": 1,   "Deafened": 2,      "Frightened": 10/10,    "Grappled": 10/3,   "Incapacitated": 10/2,  "Paralyzed": 10/2,  "Petrified": 10/1,  "Poisoned": 10/4,   "Prone": 10/2,  "Restrained": 10/3, "Stunned": 10/3,    "Unconscious": 100,},

"Aven": {
    "Blinded": 5,
    "Charmed": 3,
    "Deafened": 5,
    "Frightened": 5,
    "Grappled": 10,
    "Incapacitated": 10,
    "Paralyzed": 5,
    "Petrified": 10,
    "Poisoned": 5,
    "Prone": 0,
    "Restrained": 10,
    "Stunned": 5,
    "Unconscious": 0,},

"Beast": {      "Blinded": 3,   "Charmed": 10,  "Deafened": 3,      "Frightened": 10,       "Grappled": 2,      "Incapacitated": 10/1,  "Paralyzed": 10/2,  "Petrified": 10/2,  "Poisoned": 10/4,   "Prone": 10/3,  "Restrained": 10/4, "Stunned": 10/2,    "Unconscious": 100,},
"Beastfolk": {  "Blinded": 3,   "Charmed": 5,   "Deafened": 3,      "Frightened": 10/2,     "Grappled": 10/3,   "Incapacitated": 10/2,  "Paralyzed": 10/2,  "Petrified": 10/1,  "Poisoned": 10/3,   "Prone": 10/2,  "Restrained": 10/3, "Stunned": 10/2,    "Unconscious": 100,},
"Celestial": {  "Blinded": 5,   "Charmed": 1,   "Deafened": 5,      "Frightened": 1,        "Grappled": 10/3,   "Incapacitated": 10/3,  "Paralyzed": 3,     "Petrified": 10/2,  "Poisoned": 2,      "Prone": 5,     "Restrained": 3,    "Stunned": 5,       "Unconscious": 100,},
"Construct": {
    "Blinded": 50,
    "Charmed": 100,
    "Deafened": 50,
    "Frightened":100,
    "Grappled": 10,
    "Incapacitated": 50,
    "Paralyzed": 10,
    "Petrified": 70,
    "Poisoned": 100,
    "Prone": 10,
    "Restrained": 10,
    "Stunned": 80,
    "Unconscious": 100,},
"Dragon": {
    "Blinded": 3,   "Charmed": 2,   "Deafened": 2,      "Frightened": 10/7,     "Grappled": 10/5,   "Incapacitated": 10/2,  "Paralyzed": 10/2,  "Petrified": 10/2,  "Poisoned": 10/6,   "Prone": 10/3,  "Restrained": 10/4, "Stunned": 10/3,    "Unconscious": 100,},
"Dwarf": {      "Blinded": 5,   "Charmed": 3,   "Deafened": 5,      "Frightened": 10/2,     "Grappled": 10/3,   "Incapacitated": 10/2,  "Paralyzed": 10/2,  "Petrified": 10/2,  "Poisoned": 10/8,   "Prone": 10/2,  "Restrained": 10/3, "Stunned": 10/2,    "Unconscious": 100,},
"Elf":{         "Blinded": 3,   "Charmed": 2,   "Deafened": 3,      "Frightened": 10/3,     "Grappled": 10/3,   "Incapacitated": 10/3,  "Paralyzed": 10/3,  "Petrified": 5,     "Poisoned": 5/2,    "Prone": 10/3,  "Restrained": 10/3, "Stunned": 3/10,    "Unconscious": 100,},
"Elemental": {  "Blinded": 5,   "Charmed": 50,  "Deafened": 50,     "Frightened": 5,        "Grappled": 3,      "Incapacitated": 10,    "Paralyzed": 9,     "Petrified": 3,     "Poisoned": 3,      "Prone": 3,     "Restrained": 3,    "Stunned": 10,      "Unconscious": 9,},
"Fey":{         "Blinded": 5,   "Charmed": 2,   "Deafened": 5,      "Frightened": 10/5,     "Grappled": 10/3,   "Incapacitated": 10/4,  "Paralyzed": 10/3,  "Petrified": 10/1,  "Poisoned": 10/4,   "Prone": 10/2,  "Restrained": 10/3, "Stunned": 10/3,    "Unconscious": 100,},
"Fiend": {      "Blinded": 3,   "Charmed": 2,   "Deafened": 3,      "Frightened": 10/7,     "Grappled": 10/4,   "Incapacitated": 10/2,  "Paralyzed": 10/3,  "Petrified": 10/1,  "Poisoned": 10/6,   "Prone": 10/3,  "Restrained": 10/4, "Stunned": 10/3,    "Unconscious": 5,},
"Giant": {      "Blinded": 3,   "Charmed": 5,   "Deafened": 3,      "Frightened": 10/3,     "Grappled": 10/7,   "Incapacitated": 5,     "Paralyzed": 5,     "Petrified": 5,     "Poisoned": 3,      "Prone": 2,     "Restrained": 2,    "Stunned": 3,       "Unconscious": 100,},
"Gnome": {      "Blinded": 4,   "Charmed": 3,   "Deafened": 4,      "Frightened": 4,        "Grappled": 6,      "Incapacitated": 4,     "Paralyzed": 6,     "Petrified": 6,     "Poisoned": 4,      "Prone": 6,     "Restrained": 6,    "Stunned": 4,       "Unconscious": 100,},
"Goblin": {     "Blinded": 6,   "Charmed": 5,   "Deafened": 6,      "Frightened": 3,        "Grappled": 12,     "Incapacitated": 6,     "Paralyzed": 12,    "Petrified": 15,    "Poisoned": 6,      "Prone": 12,    "Restrained": 10,   "Stunned": 6,       "Unconscious": 101,},
"Halfling": {   "Blinded": 5,   "Charmed": 3,   "Deafened": 5,      "Frightened": 2,        "Grappled": 10,     "Incapacitated": 5,     "Paralyzed": 5,     "Petrified": 10,    "Poisoned": 3,      "Prone": 5,     "Restrained": 10,   "Stunned": 5,       "Unconscious": 100,},
"Kobold": {     "Blinded": 5,   "Charmed": 5,   "Deafened": 5,      "Frightened": 3,        "Grappled": 10,     "Incapacitated": 5,     "Paralyzed": 10,    "Petrified": 10,    "Poisoned": 5,      "Prone": 5,     "Restrained": 10,   "Stunned": 5,       "Unconscious": 100,},
"Lizardfolk": {
    "Blinded": 5,
    "Charmed": 5,
    "Deafened": 5,
    "Frightened": 75,
    "Grappled": 60,
    "Incapacitated": 25,
    "Paralyzed": 10,
    "Petrified": 10,
    "Poisoned": 80,
    "Prone": 30,
    "Restrained": 30,
    "Stunned": 20,
    "Unconscious": 1,},
"Monstrosity": {"Blinded": 3,   "Charmed": 5,   "Deafened": 3,      "Frightened": 5,        "Grappled": 2,      "Incapacitated": 3,     "Paralyzed": 3,     "Petrified": 3,     "Poisoned": 2,      "Prone": 2,     "Restrained": 2,    "Stunned": 3,       "Unconscious": 100,},
"Ooze": {       "Blinded": 1,   "Charmed": 1,   "Deafened": 100,    "Frightened": 1,        "Grappled": 100,    "Incapacitated": 2,     "Paralyzed": 2,     "Petrified": 2,     "Poisoned": 100,    "Prone": 100,   "Restrained": 100,  "Stunned": 2,       "Unconscious": 100,},
"Orc": {        "Blinded": 10,  "Charmed": 5,   "Deafened": 10,     "Frightened": 1.5,      "Grappled": 2,      "Incapacitated": 10,    "Paralyzed": 5,     "Petrified": 10,    "Poisoned": 3,      "Prone": 2,     "Restrained": 3,    "Stunned": 5,       "Unconscious": 100,},
"Plant": {
    "Blinded": 70,
    "Charmed": 70,
    "Deafened": 70,
    "Frightened": 70,
    "Grappled": 20,
    "Incapacitated": 10,
    "Paralyzed": 70,
    "Petrified": 10,
    "Poisoned": 100,
    "Prone": 80,
    "Restrained": 10,
    "Stunned": 10,
    "Unconscious": 50,},
"Snakefolk": {  "Blinded": 5,   "Charmed": 2,   "Deafened": 5,      "Frightened": 3,        "Grappled": 3,      "Incapacitated": 5,     "Paralyzed": 10,    "Petrified": 10,
                "Poisoned": 100,
                "Prone": 5,     "Restrained": 5,    "Stunned": 10,      "Unconscious": 100,},

    "Undead": {
        "Blinded": 1,
        "Charmed": 50,
        "Deafened": 1,
        "Exhaustion": 100,
        "Frightened": 50,
        "Grappled": 50,
        "Incapacitated": 10,
        "Paralyzed": 50,
        "Petrified": 50,
        "Poisoned": 100,
        "Prone": 50,
        "Restrained": 50,
        "Stunned": 50,
        "Unconscious": 90
        },

    }



    if race in ["Elemental", "Undead"] and Dice() == 1:
        exhaustion = "Exhaustion, "
    else: exhaustion = ""

    # Fetch the condition immunities for the selected race, or use an empty dictionary if the race is not defined
    condition_immunity_weights = race_condition_immunities.get(race, {})

    # Randomly determine condition immunities based on the weights
    for condition, weight in condition_immunity_weights.items():
        if random.choices([True, False], [weight, 100 - weight, ])[0]:
            condition_immunities.append(condition)

    # Format the output
    if condition_immunities:
        return "Condition Immunities: " + exhaustion + ", ".join(condition_immunities)
    else:
        return "No condition immunities"


def Extra_Defenses(npc):
    race= npc.race
    background= npc.background
    lvl = npc.level
    # Definitions of extra defenses
    acidic_blood = f"\n- Acidic Blood: \n\t Any creature that hits the {npc.race} with a melee attack while within 5 feet of it takes 2d6 acid damage."
    alien_mind = f"\n- Alien Mind: \n\t The {npc.race} has advantage on saving throws against being charmed or dominated."
    aberrant_ground = f"\n- Aberrant Ground. \n\t  The ground in a 10-foot radius around the {npc.race} is doughlike difficult terrain. Each creature that starts its turn in that area must succeed on a DC 10 Strength saving throw or have its speed reduced to 0 until the start of its next turn.  "
    arcane_awareness = f"\n- Arcane Awareness: \n\t The {npc.race} has advantage on Intelligence (Arcana) checks to recognize or recall information about spells or magical effects."
    berserker_resistance = f"\n- Berserker Resistance: \n\t The {npc.race} has resistance to bludgeoning, piercing, and slashing damage."
    diabolic_resilience = f"\n- Diabolic Resilience: \n\t The {npc.race} has resistance to bludgeoning, piercing, and slashing damage from non-magical attacks not made with silvered weapons."
    etherealness = f"\n- Etherealness: \n\t The {npc.race} can shift partially into the Ethereal Plane, granting it resistance to non-magical attacks and the ability to move through solid objects until the end of their next turn."
    fey_ancestry = f"\n - Fey Ancestry \n\t The {npc.race} has advantage on saving throws against being charmed, and magic can't put the {npc.race} to sleep."
    hellish_rebuke = f"\n- Hellish Rebuke: \n\t Once per turn, when the {npc.race} takes damage from a melee attack, it can cause flames to engulf its attacker, dealing fire 1d6 damage in return."
    infernal_wisdom = f"\n- Infernal Wisdom: \n\t The {npc.race} has advantage on saving throws against being charmed or frightened."
    lore_preservation = f"\n- Lore Preservation: \n\t Once per day, the {npc.race} can reroll a failed Intelligence check, taking the new roll."
    magic_resistance = f"\n- Magic Resistance: \n\t The {npc.race} has advantage on saving throws against spells and other magical effects."
    mental_fortitude = f"\n- Mental Fortitude: \n\t The {npc.race} has advantage on saving throws against being charmed or frightened."
    meticulous = f"\n- Meticulous: \n\t The {npc.race} has advantage on Investigation checks when analyzing texts or searching for information."
    otherwordly_perception = f"\n- Otherworldly Perception: \n\t The {npc.race} can sense the presence of invisible or hidden creatures within 60 feet of it."
    parry = f"\n- Parry: \n\t The {npc.background} can add 2 to its AC against one melee attack that would hit it."
    psychic_feedback = f"\n- Psychic Feedback: \n\t Any creature that attempts to read the {npc.race}'s thoughts or communicate telepathically with it takes 2d8 psychic damage."
    regeneration = f"\n- Regeneration: \n\t The {npc.race} regains 10 hit points at the start of its turn if it has at least 1 hit point."
    relentless = f"\n - Relentless \n\t (Recharges after a Short or Long Rest). \n\t If the {npc.race} takes {npc.level} damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."
    telepathic_shield = f"\n- Telepathic Shield: \n\t The {npc.race} has advantage on intelligence, wisdom, and charisma saving throws against spells and other magical effects that target its mind."
    spell_reflection = f"\n- Spell Reflection. \n\t  If the {npc.race} makes a successful saving throw against a spell, or a spell attack misses it, the {npc.race} can choose another creature (including the spellcaster) it can see within 30 feet of it. The spell targets the chosen creature instead of the {npc.race}. If the spell forced a saving throw, the chosen creature makes its own save. If the spell was an attack, the attack roll is rerolled against the chosen creature"
    snow_camouflage = f"\n- Snow Camouflage. \t The {npc.race} has advantage on Dexterity (Stealth) checks made to hide in snowy terrain."
    sure_footed = f"\n- Sure-Footed:\t The {npc.race} has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
    shielded_mind = f"\n- Shielded Mind \t The {race} is immune to any effect that would sense its emotions, read its thoughts, or detect its location."
    nimble_scape = f"\n- Nimble Scape:\t The {npc.race} can take the Disengage or Hide action as a bonus action on each of its turns."
    freeze = f"\n- Freeze: If the {npc.race} takes cold damage, it partially freezes; All its speed is reduced by 20 feet until the end of its next turn."
    slippery = f"\n- Slippery. \n\t The {npc.race} has advantage on ability checks and saving throws made to escape a grapple."
    SwampCamouflage =  f"\n- Swamp Camouflage \n\t The {race} has advantage on Dexterity (Stealth) checks made to hide in swampy terrain."
    LabyrinthineRecall = f"\n- Labyrinthine Recall \n\t The {race} can perfectly recall any path it has traveled."
    Burden = f"\n- {race} of Burden \n\t The {race} is considered to be a Large creature for the purpose of determining its carrying capacity."

    UnusualNature = "Unusual Nature. \n\t {npc.name} doesn't require air, food, drink, or sleep."


    
    # Dictionary to store possible extra defenses for each race
    extra_defenses_race = {
        "Aberration": [slippery, shielded_mind, relentless,spell_reflection, aberrant_ground, magic_resistance, regeneration, telepathic_shield, otherwordly_perception, etherealness, acidic_blood, psychic_feedback, alien_mind],
        "Beast":[
            SwampCamouflage,
            Burden,
            slippery, sure_footed],
        "Beastfolk": [
            SwampCamouflage,
            Burden,
            slippery, fey_ancestry,sure_footed, LabyrinthineRecall],
        "Celestial": [shielded_mind],
        "Construct": [magic_resistance],
        "Dragon":[magic_resistance],
        "Elf": [fey_ancestry],
        "Elemental":[freeze],
        "Fey": [nimble_scape],
        "Fiend": [
            LabyrinthineRecall,
            slippery,
            Burden,
            relentless,magic_resistance, regeneration, otherwordly_perception, etherealness, infernal_wisdom],
        "Goblin": [slippery, nimble_scape],
        "Lizardfolk":[
            SwampCamouflage, slippery, freeze,relentless,regeneration],
        "Orc": [
            Burden,
            relentless],
        "Snakefolk":[
            SwampCamouflage, slippery],
        "Undead": [
            UnusualNature],
    }

    # Dictionary to store possible extra defenses for each background
    extra_defenses_background = {
        "Noble": [parry],
        "Berserker": [relentless,berserker_resistance],
        "Scholar":[LabyrinthineRecall,
                   spell_reflection, arcane_awareness, mental_fortitude, lore_preservation, meticulous, shielded_mind],

        }

    # Fetch the extra defenses for the selected race and background
    possible_extra_defenses_race = extra_defenses_race.get(race, [])
    possible_extra_defenses_background = extra_defenses_background.get(background, [])

    # Combine race and background defenses
    possible_extra_defenses = possible_extra_defenses_race + possible_extra_defenses_background

    # Determine the number of defenses to select, this number can be changed as needed
    number_of_defenses_to_select = npc.proficiency_bonus  # for example

    # Randomly determine which extra defenses the character has
    if possible_extra_defenses and len(possible_extra_defenses) >= number_of_defenses_to_select:
        selected_defenses = random.sample(possible_extra_defenses, number_of_defenses_to_select)
    else:
        selected_defenses = [""]

    # Join the list of formatted defenses into a single string separated by newlines or any other separator
    defenses_string = '\n'.join(selected_defenses)

    return defenses_string


