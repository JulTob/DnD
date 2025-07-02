import random

schools = ["Abjuration",    "Conjuration",      "Divination",
           "Enchantment",   "Evocation",        "Illusion",
           "Necromancy",    "Transmutation"]

ranges = ["Touch",
          "Short (30 feet)",
          "Medium (60 feet)",
          "Long (120 feet)",
          "Unlimited"]

damage_types = [
        "Slashing",     "Piercing",     "Bludgeoning",
        "Poison",       "Acid",         "Fire",
        "Cold",         "Radiant",      "Necrotic",
        "Lightning",    "Force",        "Psychic",
        "Thunder",      "Healing",      "Temporary Hit Points",]

ConditionsTypes = [
        "Blinded",          "Charmed",      "Deafened",
        "Exhaustion",       "Frightened",   "Grappled",
        "Incapacitated",    "Invisible",    "Paralyzed",
        "Petrified",        "Poisoned",     "Prone",
        "Restrained",       "Stunned",      "Unconscious",
        ""
    ]

base_dice = ["d4", "d6", "d8", "d10", "d12"]


class SpellGenerator:
    def __init__(self):
        self.level = random.choice(range(0, 10))
            # Spell levels from 0 (cantrip) to 9
        self.school = random.choice(schools)
        self.range = random.choice(ranges)
        self.components = self.generate_components()
        self.effect = self.generate_effect()

    def generate_components(self):
        components = ["V", "S", "M"]
        return random.sample(components, random.randint(1, len(components)))

    def generate_effect(self):
        dice_number = max(1, self.level)  # Ensure at least 1 die
        dice_type = random.choice(base_dice)
        damage_dice = f"{dice_number}{dice_type}"

        return {
            "damage_type": random.choice(damage_types),
            "damage_dice": damage_dice
        }

    def __str__(self):
        components_str = ', '.join(self.components)
        return (f"Level: {self.level}\n"
                f"School: {self.school}\n"
                f"Range: {self.range}\n"
                f"Components: {components_str}\n"
                f"Effect: {self.effect['damage_type']} ({self.effect['damage_dice']})")



# Example usage:
random_spell = SpellGenerator()
print(random_spell)




def Damage():

    return random.choice(DamageTypes)





def Condition(dmg):

    if dmg == "Slashing":       return random.choice(["Exhaustion", "Incapacitated", "Poisoned", "Prone"])
    elif dmg == "Piercing":     return random.choice(["Blinded", "Exhaustion", "Incapacitated", "Poisoned", "Grappled"])
    elif dmg == "Bludgeoning":  return random.choice(["Blinded", "Deafened", "Exhaustion", "Incapacitated", "Prone", "Stunned", "Uncoscious", "Grappled", "Restrained"])
    elif dmg == "Poison":       return random.choice(["Blinded", "Charmed", "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Restrained", "Unconscious"])
    elif dmg == "Acid":         return random.choice(["Blinded", "Exhaustion", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Restrained", "Unconscious"])
    elif dmg == "Fire":         return random.choice(["Blinded", "Charmed", "Incapacitated", "Paralyzed", "Stunned", "Unconscious"])
    elif dmg == "Cold":         return random.choice(["Exhaustion", "Incapacitated", "Paralyzed", "Petrified", "Restrained", "Grappled"])
    elif dmg == "Radiant":      return random.choice(["Blinded", "Charmed", "Deafened", "Frightened", "Incapacitated", "Paralyzed", "Prone", "Stunned", "Unconscious"])
    elif dmg == "Necrotic":     return random.choice(["Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Lightning":    return random.choice(["Blinded", "Charmed", "Deafened", "Exhaustion", "Frightened", "Grappled", "Incapacitated", "Paralyzed", "Petrified", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Force":        return random.choice(["Blinded", "Deafened", "Exhaustion", "Incapacitated", "Prone", "Stunned", "Unconscious", "Grappled"])
    elif dmg == "Psychic":      return random.choice(["Blinded", "Charmed", "Deafened", "Exhaustion", "Frightened", "Incapacitated", "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious"])
    elif dmg == "Thunder":      return random.choice(["Blinded", "Deafened", "Exhaustion", "Incapacitated", "Paralyzed", "Prone", "Stunned"])
    else:                       return random.choice(ConditionsTypes)





def SavingThrow(dmg):
    if dmg == "Slashing":       st = random.choice(["STR", "DEX"])
    elif dmg == "Piercing":     st = random.choice(["STR", "DEX", "CON"])
    elif dmg == "Bludgeoning":  st = random.choice(["STR", "DEX", "CON"])
    elif dmg == "Poison":       st = "CON"
    elif dmg == "Acid":         st = random.choice(["STR", "DEX", "CON"])
    elif dmg == "Fire":         st = random.choice(["STR", "DEX", "CON", "CHA"])
    elif dmg == "Cold":         st = random.choice(["STR", "DEX", "CON"])
    elif dmg == "Radiant":      st = random.choice(["DEX", "CON", "WIS", "CHA"])
    elif dmg == "Necrotic":     st = random.choice(["STR", "CON", "WIS", "CHA"])
    elif dmg == "Lightning":    st = random.choice(["DEX", "CON", "WIS", "INT"])
    elif dmg == "Force":        st = random.choice(["STR", "CON", "CHA"])
    elif dmg == "Psychic":      st = random.choice(["INT", "WIS", "CHA"])
    elif dmg == "Thunder":      st = random.choice(["STR", "DEX", "CON"])
    else:                       st = "DEX"
    return st





def Recovery(con):
    if con == "Unconscious":    st = random.choice(["CON", "INT", "WIS", "CHA"])
    elif con == "Stunned":      st = random.choice(["CON", "INT", "WIS", "CHA"])
    elif con == "Restrained":   st = random.choice(["STR", "DEX", "CON"])
    elif con == "Poisoned":     st = random.choice(["CON", "WIS"])
    elif con == "Prone":        st = random.choice(["STR", "DEX", "CON"])
    elif con == "Petrified":    st = random.choice(["STR", "CON", "INT", "WIS", "CHA"])
    elif con == "Paralyzed":    st = random.choice(["STR", "CON", "WIS", "CHA"])
    elif con == "Invisible":    st = random.choice(["CON", "INT", "WIS", "CHA"])
    elif con == "Incapacitated":st = random.choice(["STR", "CON", "WIS", "CHA"])
    elif con == "Grappled":     st = random.choice(["STR", "DEX"])
    elif con == "Blinded":      st = random.choice(["CON", "INT", "WIS", "CHA"])
    elif con == "Frightened":   st = random.choice(["CON", "INT", "WIS", "CHA"])
    elif con == "Exhaustion":   st = random.choice(["STR", "CON", "CHA"])
    elif con == "Deafened":     st = random.choice(["STR", "CON", "WIS"])
    elif con == "Charmed":      st = random.choice(["CHA", "WIS"])
    else:                       st = "CON"
    return st








def SpellName():

    author = [
    "", "Chainer",
    "", "Brain",
    "", "Flamer",
    "",	"of Angels",
        ]

    verb =[
    "",	"Ostracize",
    "",	"Fade",
    "",	"Riot",
    "",	"Bond",
    "",	"Storm",
    "",	"Duress",
    "",	"Nourishing",
    "",	"Break",
    "",	"Mercy",
        ]

    subject =[
    "",	"Fiend",
    "",	"Beast",
    "",	"Flame",
        ]

    name = f"{random.choice(author)} {random.choice(verb)} {random.choice(subject)}"
    return name
