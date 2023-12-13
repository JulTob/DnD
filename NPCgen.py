# NPC creator
import random
import json
 
from names import Title, Racial_Names


from backgrounds import Background

from races import Race, Monster

from personality import PlotHook, Trait, Ideal

import npc_class as NPC

import dnd

def Dice(D=6,N=1):
    return dnd.Dice(D,N)

def Dizero(D=6,N=1):
    return dnd.Dizero(D,N)

def Modifier(AS):
    return dnd.Modifier(AS)

def Proficiency(AS):
    return dnd.Proficiency(AS)

def PB(lvl):
    return dnd.PB(lvl)

def proficiencyBonus(lvl):
    return PB(lvl)

def ask_chatgpt(question):
    try: 
        import openai

        # Open AI Key
        keyFile = open("key.txt", "r")
        key = keyFile.read()
        openai.api_key = key
        keyFile.close()

        # Use the Completion API to ask the question
        response = openai.Completion.create(
            model = "gpt-3.5-turbo-instruct", #"text-davinci-002", ## You can specify other models as well: "text-davinci-002", "curie", "ada
            prompt=question,
            max_tokens=500,  # Limit the response length, adjust as needed
            temperature=1
        )
        return response.choices[0].text.strip()
    except:
        return ""


def Style():
    import style
    return style.Style()

def Senses(npc):
    import senses
    return senses.Senses(npc)

def Movement(npc):
    return npc.Movement()


def Resistances(npc):
    import resistances
    return resistances.Resistances(npc)


def ConditionImmunities(npc):
    import resistances
    return resistances.ConditionImmunities(npc)


def Extra_Defenses(npc):
    import resistances
    return resistances.Extra_Defenses(npc)


def Extra_Weaknesses(npc):
    import weakness
    weakness.Extra_Weaknesses(npc)


def Martial_Skills(npc):
    import martial
    return martial.Skills(npc)


def Abilities(npc):
    import abilities
    return abilities.Abilities(npc)

def Legendary(npc):
    import legendary
    return legendary.Legendary(npc)



def Lair(npc):
    import legendary
    return legendary.Lair(npc)


def Region(npc):
    import legendary
    return legendary.Region(npc)


        
def NPC_gen():
    """NPC creator"""

    npc = NPC.NPC(
        race = Race(),
        background = Background(),
        lvl = Dice(50)
        )

    bg = npc.background
    Lvl = npc.level
    
    rc = npc.race
    mn = npc.subrace
    


    STR, DEX, CON, INT, WIS, CHA = npc.ability_scores.STR, npc.ability_scores.DEX, npc.ability_scores.CON, npc.ability_scores.INT, npc.ability_scores.WIS, npc.ability_scores.CHA


    print(f"{npc.name}, {npc.title}")


    AC = npc.AC
    HP = npc.HP


    r = ""
    r += "- {} - ".format(npc.alignment) + npc.gender
    r += "\n"
    r += npc.background
    r += "\n"
    r += f"{npc.race}: {npc.subrace}"
    r += "\n"
    r += "\n"



    r += f"Lvl: {npc.level}⚜︎\t    HP: {npc.HP}♡\t    AC: {npc.AC}⛨️"
    r += ("\n\t" +
          f"STR: {npc.ability_scores.STR}  \t |  {Modifier(npc.ability_scores.STR)} \n\t" +
          f"DEX: {npc.ability_scores.DEX}  \t |  {Modifier(npc.ability_scores.DEX)} \n\t" +
          f"CON: {npc.ability_scores.CON}  \t |  {Modifier(npc.ability_scores.CON)} \n\t" +
          f"INT: {npc.ability_scores.INT}  \t |  {Modifier(npc.ability_scores.INT)} \n\t" +
          f"WIS: {npc.ability_scores.WIS}  \t |  {Modifier(npc.ability_scores.WIS)} \n\t" +
          f"CHA: {npc.ability_scores.CHA}  \t |  {Modifier(npc.ability_scores.CHA)} \n\t")
    r += "\n"

    r += (npc.saving_throws.string) + "\n\n"
    r += (npc.skills.string) + "\n"




    r += "\n"
    r += "Passive Perception: {}".format( npc.passive_perception)
    r += "\n"
    r += "Proficiency Bonus: +{}".format( npc.proficiency_bonus)
    r += "\n"

    r += "\n"
    r += "Languages: \n\t{}".format(npc.languages)
    r += "\n"
    r += "\n"
    
    r += "⫷   COMBAT ACTIONS:   ⫸"
    r += "\n"
    r += f"\tTo hit: {npc.to_hit_bonus:+}"
    
    r += "\n" + npc.simple_attacks + "\n"
        
    r += f"\n {npc.special_attack}" 
    r += "\n\n"



    r += "༼ SPELLCASTING:\t{} ༽".format(npc.spellcasting_ability)
    r += "\n"
    r += "\t Spellsave DC {}".format(npc.spell_save_dc)
    r += "\n"
    r += "\t To hit: +{}".format(npc.spell_attack_bonus)
    r += "\n\n"
    r += npc.spells
        
        

    r += "\n"
    r += npc.abilities
    r += "\n"

    if Dice(Lvl) >= 15:
        r += Legendary(npc)
        r += "\n"

    if Dice(Lvl) >= 20:
        r += Lair(npc)
        r += "\n"

    if Dice(Lvl) >= 25:
        r += Region(npc)



    print(r)


    
    print("\n꧁  Their Story ꧂\n\n")
    s = ""
    s += "\n"
    s += " - Traits -"
    s += "\n"
    s += npc.trait
    s += " - Ideal -"
    s += "\n"
    s += npc.ideal
    s += "\n"
    s += " - Story Hook -"
    s += "\n"
    ph = npc.plothook
    s += ph


    try: 
        question = "Craft the presentation for a D&D NPC: "
        question += "\n Name: " + npc.name
        question += "\n Known as: " + npc.title
        question += "\n Race " + npc.race + "\n Subrace:" + npc.subrace
        question += "\n Alignment: " + npc.alignment
        question += "\n Background:" + npc.background
        question += "\n Traits:" + npc.trait
        question += "\n Ideals:" + npc.ideal
        question += "\n Problem or Plot Hook: " + ph 
        question += "\n Suggest a creative problem that leads to a conflict for the group. "
        question += "This conflict must be specific and well defined, having a certain success state and fail state."
        question += "The problem must be solvable in at least three different ways: One social, one using skills, and one martial. "
        question += "\n The group of players should be able to adopt a possition of antagonists or allies with the NPC."
        question += "\n Expand details as necessary. "
        question += "\n Write it in the style of " + Style()
        question += "\n Write it in first person, as if he was introducing himself, and use three paragraphs of about 150 words each, expanding where appropiate. "
        question += "\n The first paragraph must be a presentation containing information of their name and background. "
        question += "\n The second paragraph must expand on their ideals and goals."
        question += "\n The third paragraph must explain why the player's characters may help or confront the NPC, using the Ploot Hook as the source of the conflict."  
        answer = ask_chatgpt(question)
        print(answer)
        print(s)
    except Exception as e:
        print(s)
        print(f"Encountered an error: {e}")

    
NPC_gen()
