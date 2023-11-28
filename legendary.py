import dnd
import npc_class as NPC
import random
import attacks

def Dice(D=6,N=1):
    return dnd.Dice(D=6,N=1)

def PB(level):
    return dnd.PB(level)

def NumLegendaryAction(npc):
    n = max(3,min(npc.PB()//2,5))
    return Dice(n)

def Resistances(npc):
    if npc.level >= 20:
        res = 1 + (npc.level - 20) // 5
        return f"\nLegendary Resistance ({res}/Day): If {npc.name} fails a saving throw, {npc.gender} can choose to succeed instead. \n"
    else: return ""

def Legendary(npc):
    race = npc.race
    background = npc.background
    lvl = npc.level
    actions = []
    num = NumLegendaryAction(npc)
    pb = npc.PB()
    STR = npc.AS.str_mod
    
    
    r = "\n✯    LEGENDARY ACTIONS:    ✯\n"
    r += Resistances(npc)
    r += f"The {npc.background} {npc.race} can take {num} legendary actions, choosing from the options below. " +\
             f"\n\t Only one legendary action can be used at a time, and only at the end of another creature's turn. "+\
             f"\n\t The {npc.background} {npc.race} regains spent legendary actions at the start of its turn.\n"

    # General actions
    attack = f"\n- Attack \n\t The {npc.race} can do one simple attack to any creature"
    move = f"\n- Move \n\t The {race} can move half their movement"
    shimmering_shield = f"\n- Shimmering Shield (Costs 2 Actions). The {race} creates a shimmering, magical field around itself or another creature it can see within 60 feet of it. The target gains a +2 bonus to AC until the end of the {race}'s next turn."
    heal_self = f"\n- Heal Self (Costs 3 Actions). \n\t The {race} magically regains {2*4+npc.proficiency_bonus} (2d8 + {npc.proficiency_bonus}) hit points."
    wing_attack = f"\n- Wing Attack (Costs 2 Actions): The {race} beats its wings. Each creature within 10 feet of the {race} must succeed on a DC {10+PB(lvl)}DEX saving throw or take {Dice(6, 2) + PB(lvl)} bludgeoning damage and be knocked prone."
    command_ally = f"\n- Command Ally: The {background} issues a command to one of its allies, allowing the ally to immediately take an extra action on the {background}'s turn."

    racial_actions = {
        "Celestial": [
            f"\n- Shimmering Shield (Costs 2 Actions). The {race} creates a shimmering, magical field around itself or another creature it can see within 60 feet of it. The target gains a +2 bonus to AC until the end of the {race}'s next turn.",
            f"\n- Heal Self (Costs 3 Actions). \n\t The {race} magically regains {2*4+npc.proficiency_bonus} (2d8 + {npc.proficiency_bonus}) hit points.",
            f"\n- Radiant Blast. The Celestial releases a burst of radiant energy, targeting one creature it can see within 60 feet. The target must succeed on a Wisdom saving throw or take {Dice(pb//2)}d6 radiant damage and be blinded until the end of the Celestial's next turn.",
            f"\n- Healing Touch. The Celestial touches another creature, healing it for {Dice(pb//2)}d4 of hit points.",
            ],
        "Dragon": [
            f"\n- Wing Attack (Costs 2 Actions). \n\t Each creature within 10 feet must succeed on a DC {8+pb+STR} DEX save or take {pb}d6 + {STR} bludgeoning damage and be knocked prone.",
            f"\n- Tail Sweep. The Dragon makes a tail attack against all creatures within 10 feet. Each must succeed on a Dexterity saving throw or take {pb//2}d6 bludgeoning damage and be knocked prone.",
            f"\n- Frightful Presence. Each creature of the Dragon's choice within {5*Dice(4)} feet and aware of it must succeed on a Wisdom saving throw or become frightened for 1 minute."            
            ],
        "Aberration": [
            f"\n- Mind Warp. The Aberration targets one creature it can see within 60 feet, assaulting its mind. The target must make an Intelligence saving throw or take {pb//2}d6 psychic damage and be stunned until the end of the Aberration's next turn.",
            f"\n- Warp Reality. The Aberration alters reality in a small area, creating difficult terrain within {5*Dice()}."
            ],
        "Undead": [
            f"\n- Deathly Touch. The Undead touches one creature, forcing it to make a Constitution saving throw or take necrotic {pb-1}d4 damage.",
            f"\n- Terrifying Visage. The Undead reveals its horrifying true form, causing all nearby enemies to make a Wisdom saving throw or become frightened."
            ],
        "Elemental": [
            f"\n- Elemental Blast. The Elemental sends out a burst of its elemental energy in a line, requiring a Dexterity saving throw from affected creatures or take {pb//2}d6 {attacks.Damage()} damage.",
            f"\n- Elemental Blast. The Elemental sends out a burst of its elemental energy in a cone, requiring a Dexterity saving throw from affected creatures or take {pb-1}d4 {attacks.Damage()} damage.",
            f"\n- Elemental Shift. The Elemental alters its form, gaining resistance to a damage type of its choice until its next turn."
            ],
        "Fey": [
            f"\n- Beguiling Gaze. The Fey targets one creature it can see, charming it, unless the target succeeds on a Wisdom saving throw.",
            f"\n- Beguiling Gaze. The Fey targets one creature it can see, putting it to sleep, unless the target succeeds on a Wisdom saving throw.",
            f"\n- Nature's Wrath. The Fey summons vines or thorns in an area within {5*Dice(2)*Dice(4)*Dice(6)}, making it difficult terrain. Every creature that starts its turn within the area takes 1d4 damage."
            ],
        "Fiend": [
            f"\n- Hellfire Blast. The Fiend releases a burst of hellfire, causing {pb//2}d4 fire damage to all creatures within {10*Dice(6)} area.",
            f"\n- Infernal Command. The Fiend commands lesser fiends to attack a target creature, allowing them to attack immediately, using their reaction to do an attack to that target."
            ],
        "Giant": [
            f"\n- Mighty Throw. The Giant throws a large rock or similar object at a target, causing {pb-1}d6 damage on impact.",
            f"\n- Stomp. The Giant stomps the ground, creating a shockwave within {5*Dice()} feet that knocks nearby creatures prone unless they succeed on a Strength saving throw."
            ],
        "Gnome": [
            f"\n- Ingenious Trap. The Gnome quickly assembles and sets a trap, which can ensnare a creature within 5 feet of it, making it prone, unless the target succeeds on a Dexterity saving throw.",
            f"\n- Ingenious Trap. The Gnome quickly assembles and sets a trap, which can damage a creature within 5 feet of it, making 1d6 of {attacks.Damage()}, unless the target succeeds on a Dexterity saving throw.",
            f"\n- Gnome's Escape. The Gnome uses a gadget to teleport up to {Dice()*6} feet."
            f"\n- Gnome's Escape. The Gnome uses a gadget to become temporarily invisible until the start of their turn."
            ],
        "Goblin": [
            f"\n- Sneaky Stab. The Goblin makes a sudden simple melee attack with advantage on its attack roll.",
            f"\n- Disappear. The Goblin blends into its surroundings, becoming hidden to its enemies."
            ],
        "Halfling": [
            f"\n- Lucky Break. The Halfling provoques disadvantage to the next attack targeted at them.",
            f"\n- Nimble Dodge. The Halfling moves quickly, gaining a +2 AC until the start of their turn."
            ],
        "Kobold": [
            f"\n- Swarm Tactics. The Kobold directs its allies in a coordinated attack, all allies within {Dice(2)*Dice(6)*10} feet of the kobold can move up to half their speed.",
            f"\n- Quick Tinkerer. The Kobold quickly activates a tinkered device that blinds an enemy within 5ft of the Kobold."
            ],
        "Lizardfolk": [
            f"\n- Scaled Defense. The Lizardfolk hardens its scales, gaining +2 AC until the start of their turn.",
            f"\n- Swift Reptile. The Lizardfolk scapes swiftly, moving up to half their speed without provoking opportunity attacks."
            ],
        "Monstrosity": [
            f"\n- Terrifying Roar. The Monstrosity emits a fearsome roar, causing an enemie within 5 feet to become frightened on a failed Wisdom saving throw.",
            f"\n- Rend and Tear. The Monstrosity makes a special attack against a single target."
            ],
        "Ooze": [
            f"\n- Engulf. The Ooze attempts to engulf a nearby smaller creature, trapping it inside its body, unless the creature succeeds a Dexterity Saving Throw, being restrained on a fail.",
            f"\n- Corrosive Touch. The Ooze makes a pseudopod melee attack, dealing {pb//2}d6 acid damage on a hit."
            ],
        "Orc": [
            f"\n- War Cry. The Orc lets out a powerful cry, bolstering the morale of allies and intimidating enemies. Within {Dice(2)*Dice(6)*10} feet, all allies of the Orc become immune to the Frightened condition, and enemies within the range make a Wisdom saving throw or become Frightened",
            f"\n- Brutal Strike. The Orc makes a simple attack. On a hit, the target becomes Prone."
            ],
        "Plant": [
            f"\n- Entangling Roots. The Plant causes roots to burst from the ground, attempting to entangle nearby creatures. The terrain within {Dice(2)*Dice(6)*10} feet becomes difficult terrain.",
            f"\n- Healing Sap. The Plant exudes a restorative sap, healing itself or an ally within 5 feet. The target heals 1d4{npc.AS.wis_mod:+}"
            ],
        "Snakefolk": [
            f"\n- Venomous Bite. The Snakefolk delivers a poisonous bite to a creature it can reach within 5 feet. On a hit of a melee weapon attack de target receives {pb//2}d4 poison damage, and becomes poisoned",
            f"\n- Serpentine Grace. The Snakefolk slithers quickly, avoiding attacks and repositioning itself. The Snakefolk moves half his speed without provoking opportunity attacks"
            ],
        "Undead": [
            f"\n- Deathly Touch. The Undead delivers a chilling touch, causing {pb//2}d4 necrotic damage on a successful attack.",
            f"\n- Deadly Gaze. The target becomes frightened on a failed Wisdom saving throw."
            ]
        }

    
    background_actions = {
    "Artist": [
        f"\n- Inspiring Display. The Artist performs a stunning display of skill, inspiring an ally within sight to take an extra action."
        ],
    "Bandit": [
        f"\n- Tactical Ambush. The Bandit uses his cunning and gains a tactical advantage, gaining advantage on its first attack roll against a target."
        ],
    "Bard": [
        f"\n- Bardic Inspiration. The Bard inspires an ally within earshot, granting them a bonus to their next ability check, attack roll, or saving throw of 1d{2*(1+Dice())}."
        ],
    "Barbarian": [
        f"\n- Rage. The Barbarian enters a state of rage, gaining bonus of {1+ pb//2} to melee damage, and gains resistance to bludgeoning, piercing, and slashing damage."
        ],
    "Berserker": [
        f"\n- Frenzied Attack. The Berserker makes an attack with advantage against a single target. The next attack against the Berserker gains advantage."
        ],
    "Charlatan": [
        f"\n- Deceptive Maneuver. The Charlatan confuses an enemy, causing it to have disadvantage on its next attack."
        ],
    "Cleric": [
        f"\n- Divine Inspiration. The Cleric calls upon their deity for inspiration, healing an ally {pb//2}d4."
        ],
    "Crafter": [
        f"\n- Quick Fix. The Crafter can use a cantrip that takes 1 Action."
        ],
    "Criminal": [
        f"\n- Sneaky Strike. The Criminal makes a stealthy attack, gaining advantage if the target has an enemy within 5 feet of them."
        ],
    "Commoner": [
        f"\n- Unexpected Courage (Costs 2 actions). The Commoner rallies their inner strength, attacking with extraordinary bravery. It makes a simple attack. The attack is a Critical hit on a 19 or 20 on the atttack roll. "
        ],
    "Cultist": [
        f"\n- Dark Ritual (Costs 2 Actions). The Cultist quickly performs a sinister ritual, targeting one creature it can see within 30 feet. The target must succeed on a Wisdom saving throw or become cursed. While cursed, the target takes an additional {Dice(4)} necrotic damage whenever it takes damage from any source. The curse lasts for 1 minute or until the Cultist is incapacitated or dies."
        ],
    "Druid": [
        f"\n- Nature's Aid. The Druid calls upon nature to assist, by healing an ally {pb//2}d4."
        f"\n- Nature's Aid. The Druid calls upon nature to assist, entangling an enemy. On a failed Dexterity saving throw the enemy is restrained."
        ],
    "Expert": [
        f"\n- Masterful Insight. The Expert quickly assesses the situation, gaining insight into an enemy's weakness. The Expert's next attack has advantage."
        ],
    "Explorer": [
        f"\n- Pathfinder. The Explorer can move their full speed without provoking opportunity attacks."
        ],
    "Guard": [
        f"\n- Protective Stance. The Guard takes a defensive position, granting increased {1+pb//2:+} AC to themselves and one other creature."
        ],
    "Healer": [
        f"\n- Swift Aid. The Healer quickly tends to an ally's wounds, restoring {pb-1}d6 hit points."
        ],
    "Hero": [
        f"\n- Heroic Sacrifice (Costs 2 Actions). The Hero finds the strength to keep fighting, gaining {pb//2}d6 temporary hit points."
        ],
    "Hunter": [
        f"\n- Precise Shot. The Hunter makes a special attack."
        ],
    "Knight": [
        f"\n- Chivalrous Charge. The Knight charges an enemy, moving half their speed and doing a simple attack."
        ],
    "Mage": [
        f"\n- Arcane Burst. The Mage releases a burst of magical energy. All creatures within {Dice(6)*5} feet receive {pb//2}d6 {attacks.Damage()} damage"
        ],
    "Monk": [
        f"\n- Ki Strike. The Monk channels their ki energy to make rapid strikes, making two simple attacks."
        ],
    "Merchant": [
        f"\n- Shrewd Bargain. The Merchant distracts an enemy with an enticing offer or bribe. The target the Merchant can see gets disadvantage on his next attack."
        ],
    "Noble": [
        command_ally,
        f"\n- Commanding Presence. The Noble commands an ally, allowing them to move half their speed."
        ],
    "Priest": [
        f"\n- Blessing. The Priest blesses an ally, granting them a bonus 1d{2*(1+Dice())} to their next attack or saving throw."
        ],
    "Pirate": [
        f"\n- Boarding Action. The Pirate swiftly moves across the battlefield, engaging an enemy in close combat, moving their full speed and doing a simple attack."
        ],
    "Ranger": [
        f"\n- Hunter's Mark. The Ranger marks a target, granting a bonus {pb//2}d6 to damage on their next attack against that target."
        ],
    "Scholar": [
        f"\n- Moment of Clarity. The Scholar provides critical information or advice, granting advantage to an ally's next check."
        ],
    "Soldier": [
        f"\n- Tactical Maneuver. The Soldier directs their allies, granting advantage to their next attack."
        ],
    "Rogue": [
        f"\n- Cunning Action. The Rogue uses their quick wits to gain advantage on their next action."
        ],
    "Scholar": [
        f"\n- Insightful Discovery. The Scholar uses their knowledge to reveal an immunity, resistance, or vulnerability, or provide crucial information about an enemy."
        ],
    "Shaman": [
        f"\n- Spirit Call. The Shaman calls upon the spirits to aid in battle, healing all allies within {5*Dice()} feet {pb//2}d4 hit points."
        f"\n- Spirit Call. The Shaman calls upon the spirits to aid in battle, harming all enemies that start their turn within {5*Dice()} feet {pb//2}d4 hit points."
        ],
    "Soldier": [
        f"\n- Battle Cry. The Soldier rallies their allies, granting them courage. All allies that can hear, within {Dice()*10} feet, become immune to the Frightened condition for 1 minute."
        ],
    "Spy": [
        f"\n- Covert Operation. The Spy gathers crucial information or sabotages an enemy, causing their next attack to be at disadvantage."
        ],
    "Traveler": [
        f"\n- Swift Movement. The Traveler uses their knowledge of the terrain to move quickly or create an escape route. The Traveler moves up to their speed without procoking opportunity attacks."
        ],
    "Urchin": [
        f"\n- Street Smarts. The Urchin uses their survival skills to disengage, hide, or dash."
        ],
    "Warrior": [
        f"\n- Battle Frenzy. The Warrior enters a state of frenzy, increasing their attack capability for a short time. He makes a simple attack at disadvantage. On a hit, the target recives an extra {pb//2}d6 damage."
        ],
    "Warlock": [
        f"\n- Eldritch Invocation (Costs 2 actions). The Warlock invokes a fiend of CR {1 + pb//3} or less, granted by their otherworldly patron."
        ],
    "Witch": [
        f"\n- Hex. The Witch places a curse on an enemy, causing their saving throws to have disadvantage for 1 minute."
    ]
}

    # Adding race-specific actions
    if race in racial_actions:
        actions += racial_actions[race]
    if background in background_actions:
        actions += background_actions[background]
        
    # Add general actions
    actions += [attack, move]

    num_actions = min(pb // 2, len(actions))

    selected_actions = random.sample(actions, num_actions) if actions else ["No legendary actions available."]

    return  r + "\n".join(selected_actions)


def Lair(npc):
    Type=npc.race
    race=npc.race
    background=npc.background
    name = npc.title
    lvl = npc.level
    
    if Type == "":
        if Dice(0) == 1:    Type= Race()
        else:               Type= Background()

    r = "\n⛫   LAIR ACTIONS:   ⛫\n"
    r += "Unless otherwise noted, any lair action that demands a saving throw uses the spellsave DC above."
    r += "\n On initiative count 20 (losing initiative ties), the creature can take a lair action to cause one of the following effects, but can't use the same effect two rounds in a row:\n"


    attack = f"\n- Attack \n\t{name} can do one simple attack to any creature"
    move = f"\n- Move \n\t{name} can move half their movement"
    shimmering_shield = f"\n- Shimmering Shield (Costs 2 Actions).\n\t{name} creates a shimmering, magical field around itself or another creature it can see within 60 feet of it. The target gains a +2 bonus to AC until the end of the {race}'s next turn."
    heal_self = f"\n- Heal Self (Costs 3 Actions). \n\t{name} magically regains {2*4+npc.proficiency_bonus} (2d8 + {npc.proficiency_bonus}) hit points."
    wing_attack = f"\n- Wing Attack (Costs 2 Actions):{name} beats its wings. Each creature within 10 feet of {name} must succeed on a DC {10+PB(lvl)}DEX saving throw or take {Dice(6, 2) + PB(lvl)} bludgeoning damage and be knocked prone."
    command_ally = f"\n- Command Ally: {name} issues a command to one of its allies, allowing the ally to immediately take an extra action on {name}'s turn."

    if race == "Celestial": actions += [attack, shimmering_shield, heal_self]

    if background == "Noble": actions += command_ally

    actions += [attack, move]

    num_actions = min(PB(lvl) // 2, len(actions))  # Simple example: 1 action per 5 levels

    selected_actions = random.sample(actions, num_actions) if actions else ["No legendary actions available."]
    return  r + "\n".join(selected_actions)

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
    

    race = npc.race
    background = npc.background
    lvl = npc.level
    actions = []
    creature_type = npc.race + ' ' + npc.subrace + ' ' + npc.background

    r = "\n♕   REGIONAL EFFECTS:   ♛\n"
    r += f"The {npc.background} {npc.race} has an effect on its domains that may include any of the following magical effects:\n"
    s = f"\nIf the {npc.background} {npc.race} dies, these effects dissipate during the next {Dice(6,2)} days."


    attack = f"\n- Attack \n\t The {race} can do one simple attack to any creature"
    move = f"\n- Move \n\t The {race} can move half their movement"
    shimmering_shield = f"\n- Shimmering Shield (Costs 2 Actions). The {race} creates a shimmering, magical field around itself or another creature it can see within 60 feet of it. The target gains a +2 bonus to AC until the end of the {race}'s next turn."
    heal_self = f"\n- Heal Self (Costs 3 Actions). \n\t The {race} magically regains {2*4+npc.proficiency_bonus} (2d8 + {npc.proficiency_bonus}) hit points."
    wing_attack = f"\n- Wing Attack (Costs 2 Actions): The {race} beats its wings. Each creature within 10 feet of the {race} must succeed on a DC {10+PB(lvl)}DEX saving throw or take {Dice(6, 2) + PB(lvl)} bludgeoning damage and be knocked prone."
    command_ally = f"\n- Command Ally: The {background} issues a command to one of its allies, allowing the ally to immediately take an extra action on the {background}'s turn."

    effects = []
    
    if "Dragon" in creature_type:
        effects.append("The nearby land becomes scorched and inhospitable.")
        effects.append("Local wildlife becomes aggressive and mutated.")
        effects.append("Volcanic activity increases within a mile of the lair.")
        
    if "Undead" in creature_type:
        effects.append("The dead rise in nearby graveyards.")
        effects.append("Shadows seem to move on their own, even in broad daylight.")
        effects.append("Local plants wither and die.")

    num_of_effects = min(len(effects), 5)  # change 5 to the desired number of effects
    selected_effects = random.sample(effects, num_of_effects)
    
    r += "\n" + "\n".join(selected_effects)
    r += "\n" + s
    return 
        
    if race == "Celestial": actions += [attack, shimmering_shield, heal_self]

    if background == "Noble": actions += command_ally

    actions += [attack, move]

    num_actions = min(PB(lvl) // 2, len(actions))  # Simple example: 1 action per 5 levels

    selected_actions = random.sample(actions, num_actions) if actions else ["No legendary actions available."]
    return  r + "\n".join(selected_actions) + s



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
