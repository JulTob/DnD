import dnd
import npc_class as NPC
import random

"""
spell.py
    For spell class and specific spell constants.
"""

class Spell:
    def __init__(self, name, definition = ""):
        self.name = name
        self.definition = definition

    def __str__(self):
        conector = ""
        if self.definition: conector= ": "
        return f"{self.name}{conector}{self.definition}"

"""
class Spell:
    def __init__(self, name, level, school, casting_time, action_range, components, duration, description):
        self.name = name
        self.level = level
        self.school = school
        self.casting_time = casting_time
        self.action_range = action_range
        self.components = components
        self.duration = duration
        self.description = description

    def __str__(self):
        return f"{self.name} (Level {self.level}, {self.school}): {self.description}"
"""


dissonant_whispers = Spell("Dissonant Whispers", "A discordant melody that only one creature of your choice within range can hear, wracking it with terrible pain.")
shield = Spell("Shield", "An invisible barrier of magical force appears and protects you.")
ray_of_sickness = Spell("Ray of Sickness", "A ray of sickening greenish energy lashes out toward a creature within range.")
mage_armor = Spell("Mage Armor", "Protective magical force surrounds you, manifesting as a spectral frost that covers you and your gear.")
cure_wounds = Spell("Cure Wounds", "A creature you touch regains a number of hit points.")
suggestion = Spell("Suggestion", "You suggest a course of activity and magically influence a creature you can see within range that can hear and understand you.")
phantasmal_force = Spell("Phantasmal Force", "You craft an illusion that takes root in the mind of a creature that you can see within range.")
animal_messenger = Spell("Animal Messenger", "You use an animal to deliver a message.")
barkskin = Spell("Barkskin", "The skin of a willing creature you touch becomes as tough as bark.")
major_image = Spell("Major Image", "You create the image of an object, a creature, or some other visible phenomenon.")
lightning_bolt = Spell("Lightning Bolt", "A stroke of lightning forming a line 100 feet long and 5 feet wide blasts out from you in a direction you choose.")
call_lightning = Spell("Call Lightning", "A storm cloud appears in the shape of a cylinder that is 10 feet tall with a 60-foot radius.")
phantasmal_killer = Spell("Phantasmal Killer", "You tap into the nightmares of a creature you can see within range and create an illusory manifestation of its deepest fears.")
dimension_door = Spell("Dimension Door", "You teleport yourself from your current location to any other spot within range.")
telekinesis = Spell("Telekinesis", "You can try to move an object that weighs up to 1,000 pounds.")
reincarnate = Spell("Reincarnate", "You touch a dead humanoid or a piece of a dead humanoid.")

# spell.py

# ... Spell class definition ...

# Spell Constants
alter_self = Spell("Alter Self", "[Spell description here]")
antimagic_field = Spell("Antimagic Field", "[Spell description here]")
arcane_eye = Spell("Arcane Eye", "[Spell description here]")
blink = Spell("Blink", "[Spell description here]")
charm_person = Spell("Charm Person", "[Spell description here]")
contingency = Spell("Contingency", "[Spell description here]")
darkness = Spell("Darkness", "[Spell description here]")
demiplane = Spell("Demiplane", "[Spell description here]")
dimension_door = Spell("Dimension Door", "[Spell description here]")
disguise_self = Spell("Disguise Self", "[Spell description here]")
dispel_magic = Spell("Dispel Magic", "[Spell description here]")
expeditious_retreat = Spell("Expeditious Retreat", "[Spell description here]")
feather_fall = Spell("Feather Fall", "[Spell description here]")
fog_cloud = Spell("Fog Cloud", "[Spell description here]")
foresight = Spell("Foresight", "[Spell description here]")
greater_invisibility = Spell("Greater Invisibility", "[Spell description here]")
hypnotic_pattern = Spell("Hypnotic Pattern", "[Spell description here]")
imprisonment = Spell("Imprisonment", "[Spell description here]")
invisibility = Spell("Invisibility", "[Spell description here]")
leomunds_tiny_hut = Spell("Leomund’s Tiny Hut", "[Spell description here]")
locate_creature = Spell("Locate Creature", "[Spell description here]")
mage_hand = Spell("Mage Hand", "[Spell description here]")
mass_suggestion = Spell("Mass Suggestion", "[Spell description here]")
message = Spell("Message", "[Spell description here]")
mind_blank = Spell("Mind Blank", "[Spell description here]")
minor_illusion = Spell("Minor Illusion", "[Spell description here]")
mislead = Spell("Mislead", "[Spell description here]")
misty_step = Spell("Misty Step", "[Spell description here]")
modify_memory = Spell("Modify Memory", "[Spell description here]")
nondetection = Spell("Nondetection", "[Spell description here]")
passwall = Spell("Passwall", "[Spell description here]")
pass_without_trace = Spell("Pass Without Trace", "[Spell description here]")
phantasmal_force = Spell("Phantasmal Force", "[Spell description here]")
prestidigitation = Spell("Prestidigitation", "[Spell description here]")
project_image = Spell("Project Image", "[Spell description here]")
seeming = Spell("Seeming", "[Spell description here]")
silence = Spell("Silence", "[Spell description here]")
sleep = Spell("Sleep", "[Spell description here]")
teleport = Spell("Teleport", "[Spell description here]")
teleportation_circle = Spell("Teleportation Circle", "[Spell description here]")
thaumaturgy = Spell("Thaumaturgy", "[Spell description here]")
time_stop = Spell("Time Stop", "[Spell description here]")
true_seeing = Spell("True Seeing", "[Spell description here]")



