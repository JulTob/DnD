import dnd
import npc_class as NPC
import random

def PB(level):
    return dnd.PB(level)

def Dice(D=6,N=1):
    return dnd.Dice(D=D,N=N)

def Skills(npc):
    race = npc.race
    background = npc.background
    lvl = npc.level
    
    # Definitions of extra martial skills
    blinding_spittle = f"\n- Blinding Spittle (Recharge 5–6). \n\t The {race} spits a chemical glob at a point it can see within 15 feet of it. The glob explodes in a blinding flash of light on impact. Each creature within 5 feet of the flash must succeed on a DC {10+PB(lvl)} Dexterity saving throw or be blinded until the end of the {race}'s next turn."
    body_thief = f"\n- Body Thief." + \
        f"\n\t The {race} initiates an Intelligence contest with an incapacitated humanoid within 5 feet of it that isn't protected by protection from evil and good." + \
        f"If it wins the contest, the {race}'s magically takes control of the target's body. " +\
        f"The {race} retains its Intelligence, Wisdom, and Charisma scores, as well as its understanding of any language, its senses, and its traits." +\
        f"It otherwise adopts the target's statistics. It knows everything the creature knew, including spells and languages." +\
        f"\n\t If the host body dies, the {race} must leave it. A protection from evil and good spell cast on the body drives the {race} out. " +\
        f"The {race} is also forced out if the target regains control by means of a wish. " +\
        f"By spending 5 feet of its movement, the {race} can voluntarily leave the body within 5 feet of it."
    devour_intellect = ( f"\n- Devour Intellect: \t The {race} targets one creature it can see within 10 feet of it that has a brain. "
                         f"The target must succeed on a DC {10+PB(lvl)} Intelligence saving throw against this magic or take 11 (2d10) psychic damage. "
                         "Also on a failure, roll 3d6: If the total equals or exceeds the target's Intelligence score, that score is reduced to 0. "
                         "The target is stunned until it regains at least one point of Intelligence.")

    amphibious = f"\n- Amphibious. \n\t The {race} can breathe air and water."
    invisible_passage = f"\n- Invisible Passage \n\t  The {race} magically turns invisible until they attack or cast a spell, or until their concentration ends (as if concentrating on a spell)." +\
                        "While invisible, they leave no physical evidence of their passage, so they can be tracked only by magic. Any equipment they wear or carry is invisible with them."
    gibbering = f"\n- Gibbering. \n\t The {race} babbles incoherently while it can see any creature and isn't incapacitated. " +\
                f"Each creature that starts its turn within 20 feet of the Aberration and can hear the gibbering must succeed on a DC {10+PB(lvl)} Wisdom saving throw. " +\
                "On a failure, the creature can't take reactions until the start of its next turn and rolls a d8 to determine what it does during its turn. " +\
                "On a 1 to 4, the creature does nothing. " +\
                "On a 5 or 6, the creature takes no action or bonus action and uses all its movement to move in a randomly determined direction. " +\
                "On a 7 or 8, the creature makes a melee attack against a randomly determined creature within its reach or does nothing if it can't make such an attack."
    tentacles= "\n- Tentacles. \n\t Reach 10 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must succeed on a " +\
               f"DC {10+PB(lvl)} Constitution saving throw or be poisoned for 1 minute. The poisoned target is paralyzed, and it can repeat the saving throw at the" +\
               f" start of each of its turns, ending the effect on a success. \n\t The target is also grappled (escape DC {10+PB(lvl)}). If the target is Medium or " +\
               f"smaller, it is also restrained until this grapple ends. While grappling the target, the {race} has advantage on attack rolls against it and can 't "+\
               f"use this attack against other targets. When the {race} moves, any Medium or smaller target it is grappling moves with it."
    multiattack = random.choice([
        f"\n-Multiattack: The {race} makes two simple attacks.",
        f"\n-Multiattack: The {race} makes two simple melee attacks.",
        f"\n-Multiattack: The {race} makes three simple attacks.",
        f"\n-Multiattack (Two-Weapon Combat Style): The {race} makes two attacks with its main hand weapon and one with its offhand weapon.",
        f"\n-Multiattack (Rapid Shot): The {race} makes three ranged attacks, each with a -2 penalty to the attack roll.",
        f"\n-Multiattack (Sweeping Attack): The {race} makes a single attack against all enemies within reach."
        ])
    skewer = f"\n- Skewer:\t Once per turn, when the {race} makes a Melee attack and hits, the target takes an extra 10 (3d6) damage, and the {race} gains temporary hit points equal to the extra damage dealt."
    stench = f"\n- Stench:\t Any creature other than a {race} that starts its turn within 5 feet of the {race} must succeed on a DC {8+npc.proficiency_bonus + npc.ability_scores.con_mod} Constitution saving throw or be poisoned until the start of the creature's next turn. On a successful saving throw, the creature is immune to the stench of all Lizardfolk for 1 hour."
    blood_frenzy = f"\n- Blood Frenzy:\t The {race} has advantage on melee attack rolls against any creature that doesn't have all its hit points."
    reckless = f"\n-Reckless:\t At the start of its turn, the {background} can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn."
    martial_advantage = f"\n- Martial Advantage \n\t Once per turn, the {race} can deal an extra {npc.proficiency_bonus*3} ({npc.proficiency_bonus}d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the {race} that isn't incapacitated."



    # Dictionary to store possible extra martial skills for each race
    extra_skills_race = {
        "Aberration": [reckless, blinding_spittle, body_thief, amphibious, gibbering, tentacles, multiattack, devour_intellect, stench],
        "Beast":[reckless, blood_frenzy, amphibious, multiattack,skewer, stench],
        "Beastfolk":[reckless, blood_frenzy, amphibious, multiattack],
        "Fey": [amphibious, invisible_passage, gibbering, multiattack],
        "Fiend":[skewer, stench, multiattack, blood_frenzy, reckless],
        "Lizardfolk": [skewer, stench, blood_frenzy, reckless],
        "Monstrosity":[blood_frenzy, reckless],
        "Plant": [body_thief, amphibious, tentacles, multiattack, devour_intellect, skewer],
        "Undead": [body_thief, invisible_passage, multiattack, devour_intellect,skewer, stench, blood_frenzy, reckless],
    }

    # Dictionary to store possible extra skills for each background
    extra_skills_background = {
        "Commoner": [reckless],
        "Berserker": [multiattack, blood_frenzy, reckless],
        "Noble": [multiattack],
        
    }

    # Fetch the extra skills for the selected race and background
    possible_extra_skills_race = extra_skills_race.get(race, [])
    possible_extra_skills_background = extra_skills_background.get(background, [])

    # Combine race and background defenses
    possible_extra_skills = list(set(possible_extra_skills_race + possible_extra_skills_background))

    # Determine the number of skills to select, this number can be changed as needed
    number_of_skills_to_select = Dice(npc.proficiency_bonus+1)  # for example, you can change this to what makes sense in your context

    # Randomly determine which extra skills the character has
    if possible_extra_skills and len(possible_extra_skills) >= number_of_skills_to_select:
        selected_skills = random.sample(possible_extra_skills, number_of_skills_to_select)
        formatted_skills = [skill.format(race=race, background=background) for skill in selected_skills]
    else:
        formatted_skills = []

    # Join the list of formatted skills into a single string separated by newlines or any other separator
    formatted_skills_string = '\n'.join(formatted_skills)

    return formatted_skills_string
