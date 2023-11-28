import npc_class as NPC
import random
import dnd

def PB(lvl):
    return dnd.PB(lvl)

def Dicero(D=6,N=1):
    return dnd.Dizero(D,N)

def Dizero(D=6,N=1):
    return dnd.Dizero(D,N)


def Dice(D=6,N=1):
    return dnd.Dice(D,N)

def Movement(npc):

    race = npc.race
    background = npc.background

    # movement
    movement = "Speed: "
    normal = 0
    fly = 0
    swim = 0
    burrow = 0
    climb = 0

    extras = ""

    spider_climb = f"\n -Spider Climb: \t The {race} can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
    flyby = f"\n- Flyby \n\t The {race} is an agile flier, quick to fly out of enemies' reach. The {race} doesn't provoke an opportunity attack when it flies out of an enemy's reach."
    earth_glide = f"\n- Earth Glide:\t The {race} can burrow through nonmagical, unworked earth and stone. While doing so, the {race} doesn't disturb the material it moves through."

    if race in [ "Human", "Aberration", "Aven", "Beast", "Beastfolk", "Celestial", "Construct", "Dragon","Dwarf","Elf","Elemental","Fey","Fiend", "Giant","Gnome","Goblin","Halfling","Kobold","Lizardfolk","Monstrosity","Ooze","Orc","Plant","Snakefolk","Undead"]:
        normal = 30
        
    base_speeds = {
        "Human": {      "Walk": 30},
        "Dwarf": {      "Walk": 25,                                                                                                 "Climb": Dizero(2) * 5},
        "Elf": {        "Walk": 30},
        "Halfling": {   "Walk": 25},
        "Aberration": { "Walk": Dizero(6) * 10, "Fly": Dizero(6) * 10,                                                              "Climb": Dizero(3) * 10},
        "Aven": {       "Walk": 30,             "Fly": Dizero(6) * 10},
        "Beast": {      "Walk": Dice(12)*10,    "Fly": Dizero(6) * 10,          "Swim": Dizero(4) * 10, "Burrow": Dizero(4) * 5,    "Climb": Dizero(3) * 10},  
        "Beastfolk": {  "Walk": Dice(8)*10,     "Fly": Dizero(3) * 10,          "Swim": Dizero(3) * 10, "Burrow": Dizero(2) * 5,    "Climb": Dizero(3) * 10},  
        "Celestial": {  "Walk": Dice(6) * 10,   "Fly": Dice(4) * Dice(2) * 10},  
        "Construct": {  "Walk": Dice(6) * 10,   "Fly": Dizero(2) * 10,          "Swim": Dizero(2) * 10, "Burrow": Dizero(2) * 5},
        "Dragon": {     "Walk": Dice(12) * 10,  "Fly": Dice(12) * 10,           "Swim": Dice(12) * 10,  "Burrow": Dizero(5) * 5,    "Climb": Dizero() * 5},  
        "Dwarf": {      "Walk": 25},
        "Elf": {        "Walk": 30,                                             "Swim": Dizero(3) * Dizero(3) * 5},
        "Elemental": {  "Walk": Dizero(6) * 10, "Fly": Dizero(6) * 10,          "Swim": Dizero(6) * 10, "Burrow": Dizero(6) * 5}, 
        "Fey": {        "Walk": Dice(6) * 10,   "Fly": Dizero(6) * 5},
        "Fiend": {      "Walk": Dice(6) * 10,   "Fly": Dizero(8) * 10,                                                              "Climb": Dizero(3) * 10},  
        "Giant": {      "Walk": Dice(6) * 20},
        "Gnome": {      "Walk": 25},
        "Goblin": {     "Walk": 30},
        "Halfling": {   "Walk": 25},
        "Kobold": {     "Walk": 30,             "Fly": Dizero(3) * Dizero(2) * 5},
        "Lizardfolk": { "Walk": Dice(3) * Dice(3) * 10,                         "Swim": Dice(6) * 10,                               "Climb": Dizero(3) * 10},
        "Monstrosity": {"Walk": Dice(6) * 10,   "Fly": Dizero(6) * 5,           "Swim": Dice(6) * 10,                               "Climb": Dizero(3) * 10},
        "Ooze": {       "Walk": Dice(6) * 10,                                                                                       "Climb": Dice(6) * 10},  
        "Orc": {        "Walk": 30},
        "Plant":  {     "Walk": Dice(3) * 10,                                   "Swim": Dice(3) * 10,   "Burrow": Dice(3) * 5,      "Climb":  Dice(3) * 10},  
        "Snakefolk": {  "Walk": 30,                                             "Swim": Dizero(6) * 10,                             "Climb":  Dizero(3) * 5},  
        "Undead": {     "Walk": Dizero(12) * 5, "Fly": Dizero(6) * 5,           "Swim": Dizero(3) * 5,  "Burrow": Dizero(2) * 5},  
    }


    # Set default speeds to 0
    normal = base_speeds.get(race, {}).get("Walk", 0)
    fly = base_speeds.get(race, {}).get("Fly", 0)
    swim = base_speeds.get(race, {}).get("Swim", 0)
    burrow = base_speeds.get(race, {}).get("Burrow", 0)
    climb = base_speeds.get(race, {}).get("Climb", 0)
    

    if normal>=0:   movement += f"Walk: {normal}ft. \t"
    if fly>0:       movement += f"Fly: {fly}ft. \t"
    if swim>0:      movement += f"Swim: {swim}ft. \t"
    if burrow>0:    movement += f"Burrow: {burrow}ft. \t"
    if climb>0:     movement += f"Climb: {climb}ft. \t"

    # Additional Movement-related abilities
    if race in [ "Aberration", "Beast", "Beastfolk", "Construct", "Dragon","Fey","Fiend", "Lizardfolk","Monstrosity","Ooze","Plant","Snakefolk","Undead"]:
        if Dice()==1: extras += spider_climb

    if race in [ "Beast", "Beastfolk", "Dragon","Fey"]:
        if fly>0 and Dice() == 1: extras += flyby

    if race in [ "Aberration", "Beast", "Beastfolk","Gnome","Lizardfolk","Monstrosity"]:
        if Dice() == 1: extras += f"\n- Standing Leap. \n\t The {race}'s long jump is up to half his speed in feet and its high jump is up to third his speed, with or without a running start."

    if race in [ "Aberration", "Beast", "Beastfolk","Monstrosity","Fiend", "Lizardfolk","Ooze","Snakefolk","Undead"]:
        if Dice()==1:
            extras += f"\n- Spider Climb \n\t The {race} can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
            if Dice() == 1:
                extras += f"\n- Web Sense \n\t While in contact with a web, the {race} knows the exact location of any other creature in contact with the same web."
            if Dice() == 1:
                extras += f"\n- Web Walker \n\t The {race} ignores movement restrictions caused by webbing."

    if race in [ "Beast", "Beastfolk", "Dragon","Fey"]:
        if Dice()==1: extras += f"\n- Hold Breath:\t The {race} can hold its breath for {Dice(3) * Dice(4) * 5} minutes."

    if race in [ "Aberration", "Beast", "Beastfolk", "Construct", "Dragon","Fiend", "Lizardfolk","Monstrosity","Plant","Snakefolk","Undead"]:
        if burrow > 0 and Dice()==1: extras += "\n - Tunneler: \t The {race} can burrow through solid rock at half its burrowing speed and leaves a 5 foot-wide, 8-foot-high tunnel in its wake."

    if race in ["Elemental"]:
        if burrow > 0 and Dice()==1: earth_glide


    movement += extras

    return movement
