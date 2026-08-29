import sys, hashlib
sys.path.insert(0, "/Users/tbs/Desktop/DnD")
from AtlasActorLudi.Map_of_Character_Generation import summon_player
rows = []
for seed in range(1, 61):
    c = summon_player(seed=seed, level=5)
    rows.append(f"{seed}:{','.join(c.languages.names())}")
blob = "\n".join(rows)
open(sys.argv[1], "w").write(hashlib.md5(blob.encode()).hexdigest() + "\n" + blob)
