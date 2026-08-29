import sys
sys.path.insert(0, "/Users/tbs/Desktop/DnD")
from AtlasActorLudi.Map_of_Character_Generation import summon_player

def facet(c, key):
    try:
        if key == "name":       return str(c.name)
        if key == "languages":  return ",".join(c.languages.names())
        if key == "features":   return ",".join(sorted(f.name for f in c.features))
        if key == "spells":
            sc = c.get_spellcaster()
            return ",".join(sorted(str(s.name) for s in sc.spells_known)) if sc else "-"
        if key == "resistances": return str(getattr(c, "resistances", "-"))
        if key == "senses":      return str(getattr(c, "senses", "-"))
        if key == "race":        return f"{getattr(c,'race','?')}/{getattr(c,'subrace','?')}"
    except Exception as e:
        return f"ERR:{type(e).__name__}"
    return "-"

KEYS = ("name", "race", "languages", "features", "spells", "resistances", "senses")
out = {k: [] for k in KEYS}
for seed in range(1, 41):
    c = summon_player(seed=seed, level=6)
    for k in KEYS:
        out[k].append(f"{seed}:{facet(c, k)}")
import json
open(sys.argv[1], "w").write(json.dumps({k: "\n".join(v) for k, v in out.items()}))
