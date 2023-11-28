"""
Senses library
It includes all the racial senses abailable for creatures
It also calculates the radius of visibility of the creature in diferent sights
"""

import npc_class as NPC

import dnd

def Dice(D=6,N=1):
    return dnd.Dice(D=D,N=N)

def PB(level):
    return dnd.PB(level)

def Senses(npc):
    race = npc.race
    background = npc.background
    # Senses
    sense = ""
    normal = 0
    darkvision = 0
    blindsight = 0
    tremorsense = 0
    telepathy = 0
    truesight = 0

    extras = ""

    # Enhanced Senses
    enhanced_smell =    f"\n- Enhanced Smell: The {race} can detect specific odors or substances within 60 feet."
    enhanced_hearing =  f"\n- Enhanced Hearing: The {race} can hear frequencies outside the normal range and detect sounds from up to {Dice(12) * 100} feet away."
    enhanced_taste =    f"\n- Enhanced Taste: The {race} can taste and identify specific ingredients or substances, and has advantage on saving throws against ingested poisons."
    enhanced_touch =    f"\n- Enhanced Touch: The {race} can feel vibrations through surfaces and detect changes in air pressure."
    keen_smell =        f"\n- Keen Smell. \n\t The {race} has advantage on Wisdom (Perception) checks that rely on smell."
    keen_hearing =      f"\n- Keen Hearing. \n\t The {race} has advantage on Wisdom (Perception) checks that rely on hearing."


    # Specialized Senses
    echolocation = f"\n- Echolocation: The {race} can perceive its surroundings within 60 feet as if it had blindsight, but only if it isn't deafened."
    electroreception = f"\n- Electroreception: The {race} can detect electric fields within 30 feet, useful for tracking creatures and navigating underwater."
    heat_vision = f"\n- Heat Vision: The {race} can see infrared radiation, allowing it to see heat signatures within 60 feet."
    magnetoreception = f"\n- Magnetoreception: The {race} can sense magnetic fields, and therefor presence of metals, aiding in navigation."

    # Psychic Senses
    aura_sense = f"\n- Aura Sense: The {race} can see the auras of living beings within 30 feet, possibly determining their emotional state or alignment."
    empathy = f"\n- Empathy: The {race} can sense the emotions of others within 30 feet."
    precognition = f"\n- Precognition: The {race} has brief, unreliable glimpses of possible future events."
    psychometry = f"\n- Psychometry: The {race} can read the history of an object it touches."

    # Sensory Communication
    pheromones = f"\n- Pheromones: The {race} can communicate with others of its kind through the release of chemical signals."
    color_change = f"\n- Color Change: The {race} can change the color of its skin to communicate or as a response to its environment."

    # Sensory Deprivation & Resistance
    sensory_dampening = f"\n- Sensory Dampening: The {race} can voluntarily dampen its own senses to resist sensory overload or certain types of attacks. Until the end of turn, all their Perception (Wisdom) checks are made at disadvantage"
    blind_fighting = f"\n- Blind Fighting: The {race} doesn’t need to see a creature to target it with an attack, provided the creature isn't hidden from the {race}."

    # Hide and Mimic
    mimicry = (f"\n- Mimicry \n\t The {race} can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. " 
                "A creature that hears the sounds can tell they are imitations with a successful DC {8+npc.proficiency_bonus} Wisdom (Insight) check.")
    chameleon_skin = "\n - Chameleon Skin \n\t The {race} has advantage on Dexterity (Stealth) checks made to hide."

    # Enviromental adaptations
    water_breathing= f"\n- Water Breathing. The {race} can breathe underwater"
    underwater_camouflage = f"\n- Underwater Camouflage. \n\t The {race} has advantage on Dexterity (Stealth) checks made while underwater."
    hold_breath = f"\n- Hold Breath. \n\t The {race} can hold its breath for {5*Dice(3)*Dice(4)} minutes"

    # Sensibilities
    sunlight_sensitivity = f"\n - Sunlight Sensitivity:\t While in sunlight, the {race} has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."

    # Illumination
    illumination = f"\n- Illumination:\t The {race} sheds bright light in a {Dice(3)*10}-foot radius and dim light for an additional {Dice(3)*10} ft."



                
    if race in [ "Human", "Aberration", "Aven", "Beast", "Beastfolk", "Celestial", "Construct", "Dragon","Dwarf","Elf","Elemental","Fey","Fiend",
        "Giant","Gnome","Goblin","Halfling","Kobold","Lizardfolk","Monstrosity","Ooze","Orc","Plant","Snakefolk","Undead"]:
        normal = 60
        
    if race == "Aberration":
        normal      -= Dice(2) * Dice(6) * 30
        blindsight  += Dice(0) * Dice(4) * 30
        telepathy   += Dice(0) * Dice(4) * 30
        tremorsense += Dice(0) * Dice(3) * 10
        truesight   += Dice(0) * Dice(3) * 10
        extras      += f"\n- Sense Magic: \t The {race} senses magic within 120 feet of it at will. This trait otherwise works like the Detect Magic spell but isn't itself magical."

        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += echolocation
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += empathy
        if Dice()==1: extras += precognition
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += sensory_dampening
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += keen_hearing
        if Dice()==1: extras += chameleon_skin
        if Dice()==1: extras += sunlight_sensitivity
    if race == "Aven":
        normal      += Dice(3) * Dice(6) * 30
        darkvision  += Dice(0) * Dice(3) * Dice(3) * Dice(2) * 10
        blindsight  += Dice(0) * Dice(0) * Dice(3) * 10
        tremorsense -= Dice(0) * Dice(0) * 10
        telepathy   += Dice(0) * Dice(6) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f"\n- Keen Sight: \t Advantage on Wisdom (Perception) checks that rely on sight."
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += magnetoreception
        if Dice(12)==1: extras += aura_sense
        if Dice()==1: extras += sensory_dampening
        if Dice(12)==1: extras += blind_fighting
        if "Kenku" in npc.subrace: extras += mimicry
        if Dice()==1: extras += hold_breath

    if race == "Beast":
        normal      += Dice(2) * Dice(8) * 30
        darkvision  += Dice(0) * Dice(5) * 30
        blindsight  += Dice(0) * Dice(3) * Dice(4) * 10
        tremorsense += Dice(0) * Dice(6) * 10
        telepathy   += Dice(0) * Dice(3) * 10
        truesight   += Dice(0) * Dice(6) * 10

        extras += f"\n- Keen Senses: Advantage on Wisdom (Perception) checks that rely on one of their senses"
        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += echolocation
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += empathy
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice(12)==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += mimicry
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += keen_hearing
        if Dice()==1: extras += chameleon_skin
        if Dice()==1: extras += sunlight_sensitivity
        if Dice()==1: extras += illumination
        
    if race == "Beastfolk":
        normal      += Dice(2) * Dice(8) * 30
        darkvision  += Dice(0) * Dice(5) * 30
        blindsight  += Dice(0) * Dice(3) * Dice(4) * 10
        tremorsense += Dice(0) * Dice(6) * 5
        telepathy   += Dice(0) * Dice(6) * 10
        truesight   += Dice(0) * Dice(3) * 10

        extras += f"\n- Keen Senses: Advantage on Wisdom (Perception) checks that rely on one of their senses"
        extras += "\n- Speak with Animal:\t The Beastfolk can communicate simple concepts to his affinity animal when it speaks in Beast language."


        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += echolocation
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += precognition
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += chameleon_skin
        if Dice()==1: extras += sunlight_sensitivity
        if Dice()==1: extras += illumination
        
    if race == "Celestial":
        normal      += Dice(2) * Dice(10) * 20
        darkvision  += Dice(6) * Dice(6) * 10
        blindsight  += Dice(0) * Dice(6) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(10) * 20
        truesight   += Dice(3) * Dice(6) * 10

        extras += f"\n- Radiant Sight: Can see divine auras and celestial beings within a {normal} range."
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += empathy
        if Dice()==1: extras += precognition
        if Dice(12)==1: extras += psychometry
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_hearing
        if Dice()==1: extras += illumination


    if race == "Construct":
        normal      += Dice(6) * Dice(6) * 20 - Dice(12)*10
        darkvision  += Dice(0) * Dice(6) * Dice(6) * 10
        blindsight  += Dice(0) * Dice(4) * Dice(4) * 10
        tremorsense += Dice(0) * Dice(3) * 5
        telepathy   += Dice(0) * Dice(0) * 20
        truesight   += Dice(0) * Dice(4) * Dice(4) * 10

        extras += f""
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += precognition
        if Dice(12)==1: extras += psychometry
        if Dice()==1: extras += color_change
        if Dice()==1: extras += sensory_dampening
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += mimicry
        if Dice()==1: extras += illumination

    if race == "Dragon":
        normal      += Dice(2) * Dice(12) * 20
        darkvision  += Dice(0) * Dice(12) * 20
        blindsight  += Dice(0) * Dice(12) * 10
        tremorsense += Dice(0) * Dice(3) * 5
        telepathy   += Dice(0) * Dice(6) * 20
        truesight   += Dice(0) * Dice(6) * 10

        extras += f""

        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += heat_vision
        if Dice(12)==1: extras += magnetoreception
        if Dice(12)==1: extras += aura_sense
        if Dice(12)==1: extras += empathy
        if Dice(12)==1: extras += precognition
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice(12)==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += keen_hearing
        if Dice()==1: extras += chameleon_skin

    if race == "Dwarf":
        normal      += Dice(2) * Dice(4) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(1) * 10
        tremorsense += Dice(0) * Dice(1) * 5
        telepathy   += Dice(0) * Dice(3) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += sunlight_sensitivity
        
    if race == "Elf":
        normal      += Dice(2) * Dice(12) * 20
        darkvision  += Dice(0) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += 0 * 5
        telepathy   += Dice(0) * Dice(3) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f"\n- Keen Senses: Advantage on Wisdom (Perception) checks that rely on sight and hearing."
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += sunlight_sensitivity

    if race == "Elemental":
        normal      += Dice(2) * Dice(6) * 20
        darkvision  += Dice(0) * Dice(6) * Dice(3) * 10
        blindsight  += Dice(0) * Dice(3) * 10
        tremorsense += Dice(0) * Dice(4) * Dice(4) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(2) * 10

        extras += f""
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += chameleon_skin
        if Dice()==1: extras += illumination



    if race == "Fey":
        normal      += Dice(2) * Dice(6) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(3) * 10
        tremorsense += 0 * Dice(0) * 5
        telepathy   += Dice(2) * Dice(6) * 10
        truesight   += Dice(0) * Dice(6) * 10

        extras += f"\n- Fey Sight: Can see through magical darkness and illusions up to {normal} feet."
        
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += empathy
        if Dice()==1: extras += precognition
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += mimicry
        if Dice()==1: extras += chameleon_skin
        
    if race == "Fiend":
        normal      += Dice(4) * Dice(6) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(10) * 10
        tremorsense += Dice(0) * Dice(2) * 5
        telepathy   += Dice(0) * Dice(12) * 10
        truesight   += Dice(2) * Dice(6) * 10

        extras += f""

        if Dice(12)==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_taste
        if Dice(12)==1: extras += heat_vision
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += precognition
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += sensory_dampening
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += mimicry
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += sunlight_sensitivity

    if race == "Giant":
        normal      += Dice(3) * Dice(6) * 20
        darkvision  += Dice(0) * Dice(0) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += sunlight_sensitivity
        
    if race == "Gnome":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(5) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(3) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += empathy
        if Dice()==1: extras += precognition
        if Dice()==1: extras += psychometry
        if Dice()==1: extras += mimicry
        
    if race == "Goblin":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_hearing
        if Dice()==1: extras += keen_smell

    if race == "Halfling":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(0) * Dice(0) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += precognition

    if race == "Kobold":
        normal      += Dice(0) * Dice(0) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""

        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += sunlight_sensitivity

    if race == "Lizardfolk":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(4) * Dice(3) * 10
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice(2)==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += sensory_dampening
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += chameleon_skin
        if Dice(8)==1: extras += sunlight_sensitivity

    if race == "Monstrosity":
        normal      += Dice(-1) * Dice(100) * 20
        darkvision  += Dice(0) * Dice(12) * 20
        blindsight  += Dice(0) * Dice(12) * 10
        tremorsense += Dice(0) * Dice(12) * 5
        telepathy   += Dice(0) * Dice(12) * 10
        truesight   += Dice(0) * Dice(3) * Dice(2) * 10

        extras += f""
        if Dice(12)==1: extras += enhanced_smell 
        if Dice(12)==1: extras += enhanced_hearing
        if Dice(12)==1: extras += enhanced_taste
        if Dice(12)==1: extras += enhanced_touch
        if Dice(12)==1: extras += echolocation
        if Dice(12)==1: extras += electroreception
        if Dice(12)==1: extras += heat_vision
        if Dice(12)==1: extras += magnetoreception
        if Dice(12)==1: extras += pheromones
        if Dice(12)==1: extras += color_change
        if Dice(12)==1: extras += sensory_dampening
        if Dice(12)==1: extras += blind_fighting
        if Dice(12)==1: extras += keen_smell
        if Dice(12)==1: extras += mimicry
        if Dice(12)==1: extras += water_breathing
        if Dice(12)==1: extras += underwater_camouflage
        if Dice(12)==1: extras += hold_breath
        if Dice(12)==1: extras += chameleon_skin
        if Dice(12)==1: extras += sunlight_sensitivity
        if Dice(12)==1: extras += illumination

    if race == "Ooze":
        normal      += Dice(-1) * Dice(0) * 60
        darkvision  += Dice(-1) * Dice(0) * 20
        blindsight  += Dice(0) * Dice(3) * 10
        tremorsense += Dice(0) * Dice(6) * 5
        telepathy   += Dice(0) * Dice(12) * 10
        truesight   += Dice(-1) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice(2)==1: extras += blind_fighting
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage

    if race == "Orc":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += enhanced_touch

    if race == "Plant":
        normal      += Dice(-10) * Dice(10) * 20
        darkvision  += Dice(-1) * Dice(0) * 20
        blindsight  += Dice(4) * Dice(3) * 10
        tremorsense += Dice(2) * Dice(3) * 5
        telepathy   += Dice(0) * Dice(6) * 10
        truesight   += Dice(0) * Dice(3) * 10

        extras += f""
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += empathy
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += water_breathing
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += chameleon_skin
        if Dice(20)==1: extras += sunlight_sensitivity
        if Dice(20)==1: extras += illumination

    if race == "Snakefolk":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(2) * Dice(6) * 20
        blindsight  += Dice(2) * Dice(4) * 10
        tremorsense += Dice(0) * Dice(3) * 5
        telepathy   += Dice(0) * Dice(2) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        if Dice()==1: extras += enhanced_smell
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += enhanced_touch
        if Dice()==1: extras += electroreception
        if Dice()==1: extras += heat_vision
        if Dice()==1: extras += magnetoreception
        if Dice()==1: extras += pheromones
        if Dice()==1: extras += color_change
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += keen_smell
        if Dice()==1: extras += underwater_camouflage
        if Dice()==1: extras += hold_breath
        if Dice()==1: extras += chameleon_skin
        

    if race == "Undead":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(0) * Dice(12) * 20
        blindsight  += Dice(0) * Dice(12) * 10
        tremorsense += Dice(0) * Dice(5) * 5
        telepathy   += Dice(0) * Dice(12) * 10
        truesight   += Dice(0) * Dice(12) * 10
        extras += f""
        
        if Dice()==1: extras += enhanced_taste
        if Dice()==1: extras += aura_sense
        if Dice()==1: extras += precognition
        if Dice()==1: extras += sensory_dampening
        if Dice()==1: extras += blind_fighting
        if Dice()==1: extras += sunlight_sensitivity
        if Dice(100)==1: extras += illumination

    if race == "":
        normal      += Dice(10) * Dice(10) * 20
        darkvision  += Dice(0) * Dice(0) * 20
        blindsight  += Dice(0) * Dice(0) * 10
        tremorsense += Dice(0) * Dice(0) * 5
        telepathy   += Dice(0) * Dice(0) * 10
        truesight   += Dice(0) * Dice(0) * 10

        extras += f""
        
        
    # Additional sense-related abilities
    if telepathy>0:
        if Dice() == 1:
            extras += f"\n- Advanced Telepathy: \n\t The {race} can perceive the content of any telepathic communication used within {telepathy//2} feet of it, and it can't be surprised by creatures with any form of telepathy."
        if Dice() == 1:
            extras += f"\n- Telepathic Shroud. \n\t The {race} is immune to any effect that would sense its emotions or read its thoughts, as well as all divination spells."
        if Dice() == 1:
            extras += f"\n- Limited Telepathy. \n\t The {race} can magically transmit simple messages and images to any creature within {telepathy} feet of it that can understand a language. This form of telepathy doesn't allow the receiving creature to telepathically respond."
        if Dice() == 1:
            extras += f"\n- Detect Sentience: \n\t The {race} can sense the presence and location of any creature within {2*telepathy} feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by a mind blank spell."

    if normal<=0: sense += f"Blind\t"
    if darkvision>0: sense += f"Darkvision: {darkvision}ft. \t"
    if blindsight>0: sense += f"Blindsight: {blindsight}ft. \t"
    if tremorsense>0: sense += f"Tremorsense: {tremorsense}ft. \t"
    if truesight>0: sense += f"Truesight: {truesight}ft. \t"
    sense += extras

    return sense

