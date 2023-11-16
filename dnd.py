"""
DnD Basics
dnd.py
"""

import random
import re






def Dice(D=6,N=1, modifier = 0):
    """ Rolls N dices with D sides each.
        If D is 0, simulates a coin flip. """
    roll = 0
    if N<1: return 0
    for _ in range(N):
        if D >= 1: roll += random.randint(1, D)
        else: roll += random.randint(D, 1)
    return roll + modifier

def Roll(text = "1d20"):
    match = re.match(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?', text)
    if not match:
        return "Invalid input format"

    # Extracting the values
    num_dice = int(match.group(1))
    num_sides = int(match.group(2))
    modifier = int(match.group(3)) if match.group(3) else 0

    return Dice(D = num_sides, N = num_dice, modifier = modifier)

def PB(level):
    """Calculate the proficiency bonus based on level."""
    if level < 5: return 2
    else:
        return 2 + (level - 1) // 4

def Dizero(D=6,N=1):
    """Rolls a dice with D sides and a 0 value."""
    roll = 0
    for m in range(N):
        if D < 0: roll += random.randint(D, 0) 
        else: roll += random.randint(0, D)
    return roll


def Modifier(score):
    """Calculate the modifier for a given ability score."""
    return (score - 10) // 2

def Proficiency(AS):
    return Dice(Modifier(AS)*2)

def Alignment(alignment = ""):
    if alignment == 'LG':
        return "Lawful Good"
    elif alignment == 'NG':
        return "Neutral Good"
    elif alignment == 'CG':
        return "Chaotic Good"
    if alignment == 'LN':
        return "Lawful Neutral"
    elif alignment == 'NN' or alignment == 'N':
        return "True Neutral"
    elif alignment == 'CN':
        return "Chaotic Neutral"
    if alignment == 'LE':
        return "Lawful Evil"
    elif alignment == 'NE':
        return "Neutral Evil"
    elif alignment == 'CE':
        return "Chaotic Evil"
    else:
        Alignments = [
            "Lawful Good",          "Neutral Good",        "Chaotic Good",
            "Lawful Neutral",       "True Neutral",        "Chaotic Neutral",
            "Lawful Evil",          "Neutral Evil",        "Chaotic Evil",
            "Unaligned",            ""
            ]
        return random.choice(Alignments)

def NewAbilityScore():
    d1 = Dice()
    d2 = Dice()
    d3 = Dice()
    d4 = Dice()
    score = d1+d2+d3+d4 - min(d1, d2, d3, d4) 
    return score
