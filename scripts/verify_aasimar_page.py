"""
Hold the Aasimar kit to its wiki page, which is the authority over it.

``Documenta/Canon/Mythos/Aasimar.md`` is locked: every statement in its chapter 0
carries a book, and the rule for a book is that **the code adapts to the page and
never the reverse**.  A discrepancy is therefore a defect in the code, not a
disagreement to be settled by whoever is reading.  This reads both and names
every one of them.

It checks the player-facing description byte for byte, that all eight flavour
lines reach the sheet, that every Ideal's form, metal, gem, tell and Muse match
the table row for row, that the perches and the plumages match, and the Size,
Size weighting and Speed.

Run it after touching either side.  If it fails, the page is right.
"""
import re
import sys
from pathlib import Path

# Runnable as `make verify-aasimar` from anywhere in the checkout.
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
	sys.path.insert(0, str(_ROOT))

page = (_ROOT / "Documenta/Canon/Mythos/Aasimar.md").read_text()
bad = []

def check(ok, what):
	print(("  ok   " if ok else "  DIFF ") + what)
	if not ok:
		bad.append(what)

# ---- the description ------------------------------------------------------
from AtlasActorLudi.SpeciesKit.Aasimar import Aasimar
block = page.split("```txt", 1)[1].split("```", 1)[0].strip()
code_desc = Aasimar.DESCRIPTION.strip()
print("description:")
check(block == code_desc, "the player-facing description is byte-identical")
if block != code_desc:
	for a, b in zip(block.split("\n"), code_desc.split("\n")):
		if a != b:
			print("     page:", a[:110]); print("     code:", b[:110])

# ---- the eight lines ------------------------------------------------------
print("\nthe eight flavour lines:")
lines = re.findall(r"^> > 📘 _(.+?)_\s*$", page, re.M)
check(len(lines) == 8, f"the page carries eight lines (found {len(lines)})")
res = (_ROOT / "AtlasActorLudi/SpeciesKit/Aasimar/resolution.py").read_text()
flat = re.sub(r'"\s*\n\s*(?:f?")', "", res)          # join adjacent string parts
for line in lines:
	check(line in flat, f"wired: {line}")

# ---- the Ideals table -----------------------------------------------------
print("\nthe Ideals:")
from AtlasActorLudi.SpeciesKit.Aasimar.Map_of_Ideals import IDEALS, PERCHES, PLUMAGES, SINGLE_PLUMAGES
rows = re.findall(
	r"^\| \*\*(\w+)\*\* \| (.+?) \| (.+?) \| (.+?) \| \*(.+?)\* \| (.+?) \|$",
	page, re.M)
check(len(rows) == len(IDEALS), f"{len(rows)} rows on the page, {len(IDEALS)} in the code")
for name, form, metal, gem, tell, muse in rows:
	i = IDEALS.get(name)
	if i is None:
		check(False, f"{name} is on the page but not in the code"); continue
	check(i.form == form.strip(), f"{name} form")
	check(i.metal == metal.strip(), f"{name} metal")
	check(i.gem == gem.strip(), f"{name} gem")
	check(i.tell == tell.strip(), f"{name} tell")
	check(i.muse == muse.split("(")[0].strip(), f"{name} muse")

# ---- perches and plumages -------------------------------------------------
print("\nthe body:")
perches = re.findall(r"^\| (your [\w ]+|the [\w ]+) \| (.+?) \|$", page, re.M)
check(len(perches) == len(PERCHES), f"{len(perches)} perches on the page, {len(PERCHES)} in the code")
for place, disguise in perches:
	check(any(p.place == place and p.disguise == disguise for p in PERCHES), f"perch: {place}")
plumes = re.findall(r"^- \*(\{a\}.*?)\*", page, re.M)
check(len(plumes) == len(PLUMAGES) + len(SINGLE_PLUMAGES),
	f"{len(plumes)} plumages on the page, {len(PLUMAGES) + len(SINGLE_PLUMAGES)} in the code")
for p in plumes:
	check(p in PLUMAGES or p in SINGLE_PLUMAGES, f"plumage: {p}")

# ---- the numbers ----------------------------------------------------------
print("\nthe numbers:")
check(Aasimar.SIZE_WEIGHTS == (90, 10), "size 90/10")
check(Aasimar.SIZE_OPTIONS == ("Medium", "Small"), "sizes Medium or Small")
check(Aasimar.SPEED == 30, "speed 30")

print(f"\n{'ALL CLEAR' if not bad else str(len(bad)) + ' DISAGREEMENTS'}")
sys.exit(1 if bad else 0)
