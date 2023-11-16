import dnd
import npc_class as NPC
import random
import dnd

def Dice(D=6,N=1):
    return dnd.Dice(D=6,N=1)

def PB(level):
    return dnd.PB(level)


def Legendary(npc):
    race = npc.race
    background = npc.background
    lvl = npc.level
    actions = []
    
    attack = f"\n- Attack \n\t The {race} can do one simple attack to any creature"
    move = f"\n- Move \n\t The {race} can move half their movement"
    shimmering_shield = f"\n- Shimmering Shield (Costs 2 Actions). The {race} creates a shimmering, magical field around itself or another creature it can see within 60 feet of it. The target gains a +2 bonus to AC until the end of the {race}'s next turn."
    heal_self = f"\n- Heal Self (Costs 3 Actions). \n\t The {race} magically regains {2*4+npc.proficiency_bonus} (2d8 + {npc.proficiency_bonus}) hit points."
    wing_attack = f"\n- Wing Attack (Costs 2 Actions): The {race} beats its wings. Each creature within 10 feet of the {race} must succeed on a DC {10+PB(lvl)}DEX saving throw or take {Dice(6, 2) + PB(lvl)} bludgeoning damage and be knocked prone."
    command_ally = f"\n- Command Ally: The {background} issues a command to one of its allies, allowing the ally to immediately take an extra action on the {background}'s turn."

    if race == "Celestial": actions += [attack, shimmering_shield, heal_self]

    if background == "Noble": actions += command_ally

    actions += [attack, move]

    num_actions = min(PB(lvl) // 2, len(actions))  # Simple example: 1 action per 5 levels

    selected_actions = random.sample(actions, num_actions) if actions else ["No legendary actions available."]
    return "\n".join(selected_actions)


def Lair(npc):
    Type=npc.race
    if Type == "":
        if Dice(0) == 1:    Type= Race()
        else:               Type= Background()

    r = ""

    if Type == "Dragon" and Dice() == 1:        r += "\n- Chaotic Aura \n\t The dragon creates misdirecting currents of air and magic around itself. Until initiative count 20 on the next round, whenever a ranged attack roll misses the dragon, reroll the attack against a random creature within 30 feet of the dragon that doesn't have total cover against the attack."
    if Type == "Dragon" and Dice() == 1:        r += "\n- Grasping Plants \n\t The dragon causes roots and vines to temporarily grow around it; until initiative count 20 on the next round, the ground within 20 feet of the dragon is difficult terrain."

    if Type == "Fey" and Dice() == 1:        r += "\n- Chaotic Aura \n\t The Fey creates misdirecting currents of air and magic around itself. Until initiative count 20 on the next round, whenever a ranged attack roll misses the Fey, reroll the attack against a random creature within 30 feet of the fey that doesn't have total cover against the attack."
    if Type == "Fey" and Dice() == 1:        r += "\n- Grasping Plants \n\t The fey causes roots and vines to temporarily grow around it; until initiative count 20 on the next round, the ground within 20 feet of the fey is difficult terrain."
    if Type == "Fey" and Dice() == 1:        r += "\n- Fey Walk \n\t Until initiative count 20 on the next round, the fey can pass through solid walls, doors, ceilings, and floors as if the surfaces weren't there."
    if Type == "Fey" and Dice() == 1:        r += "\n- The fey targets any number of doors and windows that they can see, causing each one to either open or close as they wish. Closed doors can be magically locked (requiring a successful DC 20 Strength check to force open) until they choose to make them unlocked, or until they use this lair action again to open them."
    if Type == "Fey" and Dice() == 1:        r += "\n- The fey fills up to four 10-foot cubes of water with ink. The inky areas are heavily obscured for 1 minute, although a steady, strong underwater current disperses the ink on initiative count 10. The fey ignores the obscuring effect of the ink."
    if Type == "Fey" and Dice() == 1:        r += "\n- The fey chooses one humanoid within the lair and instantly creates a simulacrum of that creature (as if created with the simulacrum spell). This hideous simulacrum is formed out of seaweed, slime, half-eaten fish, and other garbage, but still generally resembles the creature it is imitating. This simulacrum obeys the fey's commands and is destroyed on initiative count 20 on the next round."
    if Type == "Fey" and Dice() == 1:        r += "\n- The fey creates an illusory duplicate of themselves, which appears in its own space. As long as they can see their duplicate, the fey can move it a distance equal to their walking speed as well as make the illusion speak on their turn (no action required). The illusion has the same statistics as the fey but can't take actions or reactions. It can interact with its environment and even pick up and hold real objects. The illusion seems real in every way but disappears if it takes any amount of damage. Otherwise, it lasts until the fey dismisses it (no action required) or can no longer see it. If the fey uses this lair action to create a new duplicate, the previous one vanishes, dropping any real objects in its possession."

    if Type == "Fiend" and Dice() == 1:     r += "\n- One creature the fiend can see within 120 feet of them must succeed on a Charisma saving throw or be banished to a prison demiplane. To escape, the creature must use its action to make a Charisma check contested by the fiend's. If the creature wins, it escapes the demiplane. Otherwise, the effect ends on initiative count 20 on the next round. When the effect ends, the creature reappears in the space it left or in the nearest unoccupied space if that one is occupied."
    if Type == "Fiend" and Dice() == 1:     r += "\n- The fiend targets up to three creatures that they can see within 60 feet of them. Each target must succeed on a Constitution saving throw or be flung up to 30 feet through the air. A creature that strikes a solid object or is released in midair takes 1d6 bludgeoning damage for every 10 feet moved or fallen."


    if Type == "Plant" and Dice() == 1:        r += "\n- Grasping Plants \n\t The plant causes roots and vines to temporarily grow around it; until initiative count 20 on the next round, the ground within 20 feet of the plant is difficult terrain."

    return r



def Region(npc):
    Type = npc.background
    if Type == "":
        if Dice(0) == 1:    Type= Race()
        else:               Type= Background()

    r = ""
    

    if Type == "Beastfolk":
        if Dice() == 1:        r += "\n- Beasts that have an Intelligence score of 2 or lower are charmed by the beastfolk and directed to be aggressive toward intruders in the area."

    if Type == "Celestial":
        if Dice() == 1:        r += "\n- Open flames of a non magical nature are extinguished within the celestial's domain. Torches and campfires refuse to burn, but closed lanterns are unaffected."
        if Dice() == 1:        r += "\n- Creatures native to the celestial's domain have an easier time hiding; they have advantage on all Dexterity (Stealth) checks made to hide."
        if Dice() == 1:        r += "\n- When a good-aligned creature casts a spell or uses a magical effect that causes another good-aligned creature to regain hit points, the target regains the maximum number of hit points possible for the spell or effect."
        if Dice() == 1:        r += "\n- Curses affecting any good-aligned creature are suppressed."
        

    
    if Type == "Fey":
        if Dice() == 1:        r += "\n- Compulsory Offering \n\t The first time a creature comes within 1 mile of the faerie dragon's lair, the creature must succeed on a DC 15 Wisdom saving throw or feel an overwhelming compulsion to leave an offering worth at least 5 gp stashed in an out-of-the-way place. The dragon immediately senses the location of this gift. A creature can be affected only once by this compulsion."
        if Dice() == 1:        r += "\n- Malleable Time \n\t Time is fluid within 1 mile of the fey's lair, flowing somewhere between half and twice its normal speed."
        if Dice() == 1:        r += "\n- Birds, rodents, snakes, spiders, or toads (or some other creatures appropriate to the fey) are found in great profusion."
        if Dice() == 1:        r += "\n- Beasts that have an Intelligence score of 2 or lower are charmed by the fey and directed to be aggressive toward intruders in the area."
        if Dice() == 1:        r += "\n- Strange carved figurines, twig fetishes, or rag dolls magically appear in trees."
        if Dice(8) == 1:       r += "\n- Most surfaces are covered by a thin film of slime, which is slick and sticks to anything that touches it."
        if Dice(8) == 1:       r += "\n- Currents and tides are exceptionally strong and treacherous. Any ability check made to safely navigate or control a vessel moving through these waters has disadvantage."
        if Dice(8) == 1:       r += "\n- Shores are littered with dead, rotting fish. The fey can sense when one of the fish is handled and cause it to speak with their voice."

    if Type == "Fiend":
        if Dice() == 1:        r += "\n- Birds, rodents, snakes, spiders, or toads (or some other creatures appropriate to the fiend) are found in great profusion."
        if Dice() == 1:        r += "\n- Shadows seem abnormally gaunt and sometimes move on their own as though alive."
        if Dice() == 1:        r += "\n- Creatures are transported to a harmless but eerie demiplane filled with shadowy forms, waxy corpses, and cackling. The creatures are trapped there for a minute or two, and then returned to the place where they vanished from."
        if Dice() == 1:        r += "\n- Intelligent creatures see hallucinations of dead friends, family members, and even themselves littering the fiendish realm. Any attempt to interact with a hallucinatory image causes it to disappear."


    
    return r
