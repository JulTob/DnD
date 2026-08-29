import sys, hashlib
sys.path.insert(0, "/Users/tbs/Desktop/DnD")
from AtlasActorLudi.AtlasAlusoris.Grimoire_of_NPC import NPC
rows = []
for seed in range(1, 26):
    n = NPC(seed=seed, lvl=6)
    rows.append("|".join(str(getattr(n, a, "-")) for a in
        ("name", "race", "subrace", "resistances", "senses")))
blob = "\n".join(rows)
open(sys.argv[1], "w").write(hashlib.md5(blob.encode()).hexdigest() + "\n" + blob)
