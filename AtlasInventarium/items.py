import dnd
import random

def Item(npc):


     afterthought = """Afterthought.

Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 7 (1d4 + 5) piercing damage, plus 9 (2d8) necrotic damage. If the target is a creature, it is afflicted by entropic magic, taking 9 (2d8) necrotic damage at the start of each of its turns. Immediately after taking this damage on its turn, the target can make a DC 20 Constitution saving throw, ending the effect on itself on a success. Until it succeeds on this save, the afflicted target can't regain hit points."""



     item = [
         afterthought,
         ]

     return random.choice(item)
