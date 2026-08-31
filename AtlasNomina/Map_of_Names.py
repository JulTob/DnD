import random
import time
from contextlib import contextmanager
from collections import defaultdict, Counter
from Minion import guardian, watcher, warden, spy, minion, changeling, print_record, report_bug, CHANGELING_MINION, CHANGELING_COLOR

try:
	import AtlasAlusoris.Map_of_NPC as NPC
	from AtlasLudus.Map_of_Dice import Dice
	from AtlasNomina.Map_of_Word_Entropy import entropify, reduce_entropy, increase_entropy, to_mean_entropy
	from AtlasNomina.Map_of_Markov import MarkovNameGenerator
	from AtlasLudus.Map_of_Useful_Functions import select1
except ImportError:
	raise

MAX_ATTEMPTS = 3
MAX_DEPTH = 1

# How many goes each naming method gets before NewWord moves to the next one.
# Its own constant on purpose: how many times to *repeat a method* is a
# different decision from how many attempts a method makes internally, and they
# should be tunable apart. Setting this to 1 restores the pre-ladder behaviour
# exactly, dice for dice, for anyone who needs old seeds to name old characters.
METHOD_ATTEMPTS = 3

# ─────────────────────────────────────────────────────────────────────────────
#  The naming ladder
# ─────────────────────────────────────────────────────────────────────────────
# Three rungs, each a working generator, each simpler than the one above it:
#
#   1. the character's own race module   Elf.Names, Dwarf.Phonotactic, ...
#   2. plantilla, the generic template   written to answer for any genus
#   3. the LAST_RESORT rosters           plain tuples, so they cannot fail
#
# Every step down is reported by the Minion system, naming what broke, where,
# and who took over. A silent demotion is the thing to avoid: a generic name is
# a fine sheet and a bad diagnosis, and nobody goes looking for a bug they were
# never told about.
#
# Note what the ladder replaces. A Dice Bag is opened fresh from
# ``seed|purpose|version`` on every call, so a second attempt at the same name
# replays the identical dice and arrives at the identical failure: against a
# seeded generator, retrying is futile by construction, however many times it is
# done. The only recovery available is to ask somebody else. That is the whole
# design, and it is why these functions carry @changeling rather than @guardian.

# Rung three. Deliberately plain: a name off this list should read as somebody's
# character, not as an error message, because that is exactly when it is used.
LAST_RESORT_NAMES = (
	"Ada", "Bran", "Cora", "Dain", "Edda", "Fenn", "Gale", "Hale",
	"Ida", "Jarl", "Kesh", "Lorn", "Mira", "Nell", "Orin", "Pell",
	"Quill", "Rook", "Sela", "Tarn", "Vale", "Wren", "Yara", "Zeph",
	)

LAST_RESORT_SURNAMES = (
	"Ashdown", "Blackwater", "Coldiron", "Dunmore", "Eastmarch",
	"Fairholm", "Greystone", "Hallow", "Ironvale", "Keelson",
	"Longbarrow", "Marchwood", "Northgate", "Oakhand", "Pinefall",
	"Redhill", "Stormcrow", "Thornbury", "Underhill", "Westwind",
	)

# Onset, nucleus and coda: enough to build a syllable out of nothing.
LAST_RESORT_PHONOTACTIC = (
	("b", "br", "d", "dr", "f", "g", "gr", "h", "k", "kr",
		"l", "m", "n", "p", "r", "s", "st", "t", "th", "v"),
	("a", "e", "i", "o", "u", "ae", "ea", "io", "ua", "ar",
		"or", "en", "in"),
	("n", "r", "l", "s", "th", "nd", "rn", "ll", "ss", "k", "m", "d"),
	)

# The four functions every race module is expected to offer, and what answers
# for each one when no module can. Adding a fifth ingredient means adding it
# here: that is the whole registration, and the ladder covers it from then on.
LAST_RESORT_INGREDIENT = {
	"Names":          LAST_RESORT_NAMES,
	"Surnames":       LAST_RESORT_SURNAMES,
	"Phonotactic":    LAST_RESORT_PHONOTACTIC,
	"Surphonotactic": LAST_RESORT_PHONOTACTIC,
	}

NAMING_INGREDIENTS = tuple(LAST_RESORT_INGREDIENT)


def _rung_name(
		source,
		):
	"""How a rung of the ladder is called in the log."""
	return getattr(
		source,
		"__name__",
		str(source),
		).split(".")[-1]


def _report_demotion(
		source,
		ingredient,
		reason,
		heir,
		):
	"""One line saying who could not answer, why, and who is being asked next."""
	print_record(
		f"{CHANGELING_MINION}: {time.strftime('%Y-%m-%d %H:%M:%S')} [naming] "
		f"{_rung_name(source)}.{ingredient} {reason}; "
		f"{heir} takes over.",
		CHANGELING_COLOR,
		)


def _plantilla():
	"""Rung two, imported late so a broken race module cannot take it down too."""
	try:
		from AtlasNomina.Races import plantilla
		return plantilla
	except Exception as exc:
		report_bug(
			exc
			)
		return None


def _groomed(
		answer,
		):
	"""
	Strip stray whitespace from a roster of name parts, QST-0052.

	Length and order are preserved on purpose: seeded draws pick by index, so
	grooming an entry may never move its neighbours. Anything that is not a
	flat collection of strings (the phonotactic triples) passes untouched.
	"""
	if isinstance(answer, (list, tuple)) and all(
			isinstance(entry, str) for entry in answer
			):
		return type(answer)(
			entry.strip() for entry in answer
			)
	return answer


def Race_Ingredient(
		race,
		ingredient,
		genus,
		):
	"""
	Ask a race module for one of its four naming ingredients, and keep asking
	downwards until something answers.

	A missing function and a bug inside a present one are the same event here:
	both mean this module cannot supply this ingredient for this genus, and both
	are reported before the demotion. The bottom rung is a constant, so this
	function has no failing path and its callers need no fallback of their own.
	"""
	ladder = [race, _plantilla()]
	for rung, source in enumerate(ladder):
		if source is None:
			continue
		heir = (
			_rung_name(ladder[rung + 1])
			if rung + 1 < len(ladder) and ladder[rung + 1] is not None
			else "the last-resort roster"
			)
		provider = getattr(
			source,
			ingredient,
			None,
			)
		if provider is None:
			_report_demotion(source, ingredient, "is not defined", heir)
			continue
		try:
			answer = provider(genus)
		except Exception as exc:
			report_bug(
				exc
				)
			_report_demotion(
				source,
				ingredient,
				f"raised {type(exc).__name__}",
				heir,
				)
			continue
		if answer:
			return _groomed(
				answer
				)
		_report_demotion(source, ingredient, "came back empty", heir)
	return LAST_RESORT_INGREDIENT[ingredient]


def _steady_pick(
		lusor,
		roster,
		offset=0,
		):
	"""Pick from a roster without needing the Character's full naming path."""
	try:
		return lusor.Pick(
			roster,
			dice=lusor.Dice_Bag(
				"Nomina.LastResort",
				version="1",
				),
			)
	except Exception as exc:
		report_bug(
			exc
			)
		from zlib import crc32

		identity = str(
			getattr(
				lusor,
				"seed",
				"",
				)
			or getattr(
				lusor,
				"race",
				"",
				)
			or id(
				lusor
				)
			).encode(
				"utf-8"
				)
		return roster[
			(crc32(
				identity
				) + offset) % len(
					roster
					)
			]


def LastResortGivenName(
		lusor,
		i=0,
		):
	"""Rung three for a given name: roster only."""
	return _steady_pick(
		lusor,
		LAST_RESORT_NAMES,
		)


def LastResortFamilyName(
		lusor,
		i=0,
		):
	"""Rung three for a family name."""
	return _steady_pick(
		lusor,
		LAST_RESORT_SURNAMES,
		offset=7,
		)


def LastResortName(
		lusor,
		):
	"""Rung three for a whole name. Nothing here can raise."""
	return (
		f"{LastResortGivenName(lusor)} {LastResortFamilyName(lusor)}"
		)


def LastResortWord(
		character,
		names=None,
		prefix=None,
		fix=None,
		suffix=None,
		depth=0,
		*,
		dice=None,
		):
	"""NewWord's stand-in, carrying NewWord's signature."""
	return _steady_pick(
		character,
		LAST_RESORT_NAMES,
		)


@changeling(LastResortWord)
def NewWord(    names ,    prefix,    fix,    suffix,    depth = 0):
	'''
	Generates a new word based on the lists in a Lexicon object
	It uses different methods selected at random:
	- From the premade lists, concatenate a random selection of prefix-fix-suffix
	- Extraction of syllables from the Names list and generating by syllables
		- Weighted syllables
	- Markov Generator: Weighted Random Probability for the next letter
	- Remixing leters of a name to generate a new name.
	- Choosing a name directly from the lexicon.
	'''

	strategies = [
		#"EntropyUp",
		"Entropify",
		"EntropyDown",
		"Mutate",
		#"Extraction",
		#"Mix",
		"Markov",
		# "PhonotacticWeighted", ### Commented out: Errors
		"Syllabic",
		"Choose",
		# "EchoMorphology", ### Commented out: Feels weird
		]
	if depth > MAX_DEPTH:
		return random.choice(names)

	choices = strategies[:]
	random.shuffle(choices)
	HEAVY = {"Markov", "PhonotacticWeighted", "WeightExtraction"}
	for strategy in choices:
		try:
			if strategy == "EntropyUp":
				name = random.choice(names)
				newName = mutate_entropy(name, increase_entropy, names)
				if is_valid_name(newName, strategy): return newName
				else: return name
			elif strategy == "EntropyDown":
				name = random.choice(names) # NewWord(names, prefix, fix, suffix, depth)
				newName = mutate_entropy(name, reduce_entropy, names)
				if is_valid_name(newName, strategy): return newName
				else: return name
			elif strategy == "Entropify":
				name = random.choice(names)# NewWord(names, prefix, fix, suffix, depth)
				newName = mutate_entropy(name, to_mean_entropy, names)
				if is_valid_name(newName, strategy): return newName
				else: return name
			elif strategy == "Mutate":
				name = random.choice(names)
				newName1 = mutate_entropy(name, increase_entropy, names)
				newName2 = mutate_entropy(newName1, reduce_entropy, names)
				newName3 = mutate_entropy(newName2, to_mean_entropy, names)
				if is_valid_name(newName3, strategy): return newName3
				elif is_valid_name(newName2, strategy): return newName2
				elif is_valid_name(newName1, strategy): return newName1
				else: return name
			elif strategy == "Extraction":
				for _ in range(MAX_ATTEMPTS):
					name = SyllabicComposition(names, min_syllables=2, max_syllables=6)
					if name and is_valid_name(name, strategy):
						name_ent = entropify(name, names)
						if name_ent and is_valid_name(name, strategy):
							name = name_ent
						return name
			elif strategy == "Mix":
				name = Mixer(names, prefix, fix, suffix, depth + 1)
				name_b = name
				if name and is_valid_name(name, strategy):
					return name
			elif strategy == "EchoMorphology":
				name = random.choice(names) # NewWord(names, prefix, fix, suffix, depth + 1)
				for i in range(MAX_ATTEMPTS):
					name = EchoMorphology(name)
					if name and is_valid_name(name, strategy):
						pass
					name = entropify(name, names)
					if name and is_valid_name(name, strategy):
						return name
				return random.choice(names) # NewWord(names, prefix, fix, suffix, depth + 1)
			elif strategy == "Syllabic":
				name = Syllabic(prefix, fix, suffix)
				if name:
					return name
			elif strategy == "Choose":
				name = random.choice(names)
				return name
			elif strategy == "Markov":
					markov = MarkovNameGenerator(names)
					for _ in range(MAX_ATTEMPTS):
						name = markov.generate_name()
						if name and is_valid_name(name, strategy):
							return name
			elif strategy == "PhonotacticWeighted":
					phonotactics = ExtractWeightedPhonotacticElements(names)
					for i in range(MAX_ATTEMPTS):
						name = GenerateFromWeightedPhonotactics(phonotactics)
						if name and is_valid_name(name, strategy):
							return name
			else:
				name = random.choice(names)
				return name

		except Exception:
			return random.choice(names)
	return random.choice(names)

def Surnamer(lusor,  i=0):
	"""Deterministic surname: we just offset the seed by +1."""
	with deterministic(lusor.seed + i):
		random.seed(lusor.seed + i)
		surnames = SurnamesList(lusor)
		o, n, c = Surphonotactic(lusor)
		surname = NewWord(surnames, o, n, c)
	return surname.capitalize()

def Namer(lusor, i=0):
	with deterministic(lusor.seed + i):
			random.seed(lusor.seed + i)
			names = NamesList(lusor)
			o, n, c = Phonotactic(lusor)
			name = NewWord(names, o, n, c)
	return name.capitalize()

def EchoMorphology(base_name):
	pattern = []
	for c in base_name.lower():
		if c in 'aei':
			pattern.append('A')
		if c in 'ou':
			pattern.append('O')
		if c in 'bdptfvwr':
			pattern.append('B')
		if c in 'ckqsxz':
			pattern.append('C')
		if c in 'ghjy':
			pattern.append('G')
		if c in 'lmn':
			pattern.append('M')
		else:
			pattern.append('X')
	name = ''
	for p in pattern:
		if p == 'A':
			name += random.choice('aei')
		if p == 'O':
			name += random.choice('ou')
		if p == 'B':
			name += random.choice('bdptv')
		if p == 'C':
			name += random.choice('csx')
		if p == 'G':
			name += random.choice('gjy')
		if p == 'M':
			name += random.choice('lmn')
	return name.capitalize()

def ExtractWeightedPhonotacticElements(name_list):
	from collections import Counter

	prefix_counts = Counter()
	fix_counts = Counter()
	suffix_counts = Counter()

	for name in name_list:
		name = name.lower()
		if len(name) < 3: continue

		prefix = name[:2]
		fix = name[1:3]
		suffix = name[-2:]

		prefix_counts[prefix] += 1
		fix_counts[fix] += 1
		suffix_counts[suffix] += 1

	return {
		'prefix': list(prefix_counts.keys()),
		'prefix_weights': list(prefix_counts.values()),
		'fix': list(fix_counts.keys()),
		'fix_weights': list(fix_counts.values()),
		'suffix': list(suffix_counts.keys()),
		'suffix_weights': list(suffix_counts.values()),
	}

def GenerateFromWeightedPhonotactics(phonotactics, syllable_count=2):
	import random

	name = ''
	for _ in range(syllable_count):
		o = random.choices(phonotactics['prefix'], weights=phonotactics['prefix_weights'])[0]
		n = random.choices(phonotactics['fix'], weights=phonotactics['fix_weights'])[0]
		c = random.choices(phonotactics['suffix'], weights=phonotactics['suffix_weights'])[0]
		name += o + n[-1] + c[-1]  # basic syllable smoothing
	return name.capitalize()

@contextmanager
def deterministic(seed: int):
	"""
	Temporarily seed the global random module so that every random.*
	call inside the with‑block is repeatable, then restore the old state.
	"""
	state = random.getstate()
	random.seed(seed)
	try:
		yield
	finally:
		random.setstate(state)

def first_valid(strategy_fns, validator, fallback_names, retries=2, timeout=2.0):
	"""
	Run strategy_fns (list of callables) in parallel with timeout.
	Return the first valid result or fallback to a name from fallback_names.
	"""
	for attempt in range(retries):
		stop = Event()

		def task(fn):
			try:
				if stop.is_set():
					return None
				result = fn()
				if result and validator(result):
					stop.set()
					return result
			except Exception as exc:
				# Was ``raise e``, which crossed the thread boundary and came
				# back out of fut.result(), so one broken strategy failed the
				# whole heat instead of losing it.
				report_bug(exc)
			return None

		with ThreadPoolExecutor() as ex:
			futures = [ex.submit(task, fn) for fn in strategy_fns]
			try:
				done, _ = wait(futures, timeout=timeout, return_when=FIRST_COMPLETED)
			except TimeoutError:
				continue

			for fut in done:
				result = fut.result()
				if result:
					return result


	# All attempts failed or timed out; fallback to predefined list
	fallback_name = random.choice(fallback_names)
	return fallback_name

def LoadRace(trait):
	"""
	Dynamically imports the appropriate race module based on the genus.
	The imported module for the race, or a fallback module if not found.
	"""
	race_module_map = {
		"Aberration": 	"AtlasNomina.Races.Aberration",
		"Aven" : 		"AtlasNomina.Races.Aven",
		"Beast": 		"AtlasNomina.Races.Beast",
		"Beastfolk": 	"AtlasNomina.Races.Beastfolk",
		"Catfolk": 		"AtlasNomina.Races.Catfolk",
		"Celestial" : 	"AtlasNomina.Races.Celestial",
		"Construct" : 	"AtlasNomina.Races.Construct",
		"Dragon"    : 	"AtlasNomina.Races.Dragon",
		"Dwarf"		: 	"AtlasNomina.Races.Dwarf",
		"Elemental" : 	"AtlasNomina.Races.Elemental",
		"Elf"    : 		"AtlasNomina.Races.Elf",
		"Fey"    : 		"AtlasNomina.Races.Fey",
		"Fiend"    : 	"AtlasNomina.Races.Fiend",
		"Giant"    : 	"AtlasNomina.Races.Giant",
		"Gnome"    : 	"AtlasNomina.Races.Gnome",
		"Goblin" : 		"AtlasNomina.Races.Goblin",
		"Halfling"    : "AtlasNomina.Races.Halfling",
		"Human"    : 	"AtlasNomina.Races.Human",
		"Kobold"    : 	"AtlasNomina.Races.Kobold",
		"Lizardfolk" : 	"AtlasNomina.Races.Lizardfolk",
		"Monstrosity" : "AtlasNomina.Races.Monstrosity",
		"Ooze" : 		"AtlasNomina.Races.Ooze",
		"Orc" : 		"AtlasNomina.Races.Orc",
		"Plant" : 		"AtlasNomina.Races.Plant",
		"Snakefolk" : 	"AtlasNomina.Races.Snakefolk",
		"Undead": 		"AtlasNomina.Races.Undead",
		"Vampire": 		"AtlasNomina.Races.Vampire",
		}
	import importlib
	module_path = race_module_map.get(trait)
	if module_path is None:
		# Not an error: plenty of genera have no module of their own and the
		# template is the right answer for them. Nothing to report.
		return _plantilla()
	try:
		return importlib.import_module(module_path)
	except Exception as exc:
		# A race module that will not even import is a real defect, and used to
		# be indistinguishable from the line above: the sheet quietly filled
		# with template names and nobody was told which module was down.
		report_bug(exc)
		_report_demotion(
			module_path,
			"the module",
			f"would not import ({type(exc).__name__})",
			"plantilla",
			)
		return _plantilla()

@changeling(LastResortName)
def NewName(lusor):
	"""
	Generate a full name for the given lusor (character).

	Was @guardian. The dice here come from a Bag opened on the seed, so every
	retry drew the same numbers and met the same wall: a hundred attempts at a
	failure that never had a second outcome. A Changeling steps aside to
	LastResortName instead, and the sheet gets a name either way.
	"""
	from random import seed
	import AtlasNomina.Races.plantilla as fallback

	genus = lusor.genus
	seeding = lusor.seed
	seed(seeding)

	race = LoadRace(lusor.race)

	# Four ingredients, one ladder each. These used to catch AttributeError
	# only, which covered a race module that never defined the function and let
	# every bug *inside* a defined one straight through: that is how a stray
	# ``Names +=`` in Elf.Phonotactic became a hundred retries and a ceiling
	# message instead of one reported UnboundLocalError and a generic elf.
	names = Race_Ingredient(race, "Names", genus)
	surnames = Race_Ingredient(race, "Surnames", genus)
	o, n, c = Race_Ingredient(race, "Phonotactic", genus)
	os, ns, cs = Race_Ingredient(race, "Surphonotactic", genus)


	# Define genus-based flags
	MONSTER =         "Monstrosity"    in genus
	CELESTIAL =     "Celestial"        in genus
	BEAST =         ("Beast" in genus) and not("folk" in genus)
	if  "Giant"        in genus:
		name = NewWord(names, o, n, c).capitalize()
		surname = NewWord(surnames, os, ns, cs).capitalize()
		FullName =  f"{name} {surname}son"
	elif "Elemental"    in genus:
		random.seed(seeding)
		name = NewWord(names, o, n, c).capitalize()
		surname = NewWord(surnames, os, ns, cs).capitalize()
		FullName = f"{name} {surname}"
	elif BEAST or MONSTER:
		name = NewWord(names, o, n, c).capitalize()
		FullName = name
	elif "Construct"     in genus:
		name = NewWord(names, o, n, c).capitalize()
		surname = NewWord(surnames, os, ns, cs).capitalize()
		FullName = select1([
			f"{name}-{surname}",
			f"{name} {surname}",
			f"{name}:{surname}",
			f"{name}_{surname}",
			])
	elif "Dwarf"         in genus:
		name = NewWord(names, o, n, c).capitalize()
		name2 = NewWord(names, o, n, c).capitalize()
		surname = NewWord(surnames, os, ns, cs).capitalize()
		surname2 = NewWord(surnames, os, ns, cs).capitalize()
		FullName = select1([
			f"{name} {name2} {surname} {surname2}",
			])
	elif "Gnome"         in genus:
		name = NewWord(names, o, n, c).capitalize()
		name2 = NewWord(names, o, n, c).capitalize()
		name3 = NewWord(names, o, n, c).capitalize()
		surname = NewWord(surnames, os, ns, cs).capitalize()
		FullName =  f"{name} {name2} {name3} {surname}"
	elif "Vampire"         in genus:
		name = NewWord(names, o, n, c).capitalize()
		surname = NewWord(surnames, os, ns, cs).capitalize()
		FullName = f"{name} {surname}"
	else:
		name = NewWord(names, o, n, c).capitalize()
		surname = NewWord(surnames, os, ns, cs).capitalize()
		FullName = f"{name} {surname}"

	if "Noble"         in genus:
		if lusor.gender.title() == "He":
			FullName = f"Lord {FullName}"
		if lusor.gender.title() == "She":
			FullName = f"Lady {FullName}"
		if lusor.gender.title() == "They":
			FullName = f"Noble {FullName}"

	# One exit, one guarantee (QST-0052): no name reaches a sheet or a
	# sentence with leading, trailing, or doubled spaces, whichever branch
	# above assembled it and whichever part came back empty.
	lusor._name = " ".join(
		name.split()
		)
	return " ".join(
		FullName.split()
		).title()

# The four ingredient readers below are @guardian no longer. Every one of them
# reads a seeded generator, so a retry replays the same dice into the same wall;
# and every one of them now goes through Race_Ingredient, which has no failing
# path of its own. The safeguard moved from repeating the work to replacing it.

def Phonotactic(lusor, sur = False):
	"""
	Retrieve phonotactic elements (prefix, fix, suffix) for a lusor's genus.

	Args:
		lusor (object): The lusor object containing genus and other attributes.
		sur (bool): Whether to retrieve surname phonotactics.

	Returns:
		tuple: prefix, fix, and suffix as lists.
	"""
	if sur:
		return Surphonotactic(lusor)
	return Race_Ingredient(
		LoadRace(lusor.race),
		"Phonotactic",
		lusor.genus,
		)

def Surphonotactic(lusor):
	"""Retrieve the surname's phonotactic elements for a lusor's genus."""
	return Race_Ingredient(
		LoadRace(lusor.race),
		"Surphonotactic",
		lusor.genus,
		)

def NamesList(lusor):
	"""The lexicon of given names this lusor's kind draws on."""
	# Was: a plain `if not Names` guard falling through to
	# ``Races.plantilla.Names(genus)`` — a module never imported under that name
	# and a variable never defined in this scope. It could only ever raise
	# NameError, so an empty lexicon was the one case it did not handle.
	# Race_Ingredient treats empty as a refusal and demotes on it.
	return Race_Ingredient(
		LoadRace(lusor.race),
		"Names",
		lusor.genus,
		)

def SurnamesList(lusor):
	"""The lexicon of family names this lusor's kind draws on."""
	return Race_Ingredient(
		LoadRace(lusor.race),
		"Surnames",
		lusor.genus,
		)

# No @guardian. NewWord's ladder already gives every method METHOD_ATTEMPTS
# goes with fresh dice, and nesting a second retry inside the first turns three
# tries into thirty, each one reported. One mechanism, owned by the caller.
def Syllabic(prefix,fix,suffix):
	'''
	-- Syllabic Union. --
	Creates a syllabic union from the prefix, fix, and suffix lists.
	'''
	pre = random.choice(prefix)
	fix = random.choice(fix)
	suf = random.choice(suffix)

	result = f"{pre}{fix}{suf}"
	return result

# No @spy. It was a development probe, and it had outlived that: this is a pure
# predicate called several times per strategy per name, and the Spy prints a
# full call tree on every one of those calls, success or failure. Nothing was
# learnt from the thousandth identical tree that the first had not already said.
def is_valid_name(name, strategy=""):
	"""
	Checks if a name is valid based on various specific criteria.

	Parameters:
		name (str): The name to check.

	Returns:
		bool: True if the name is valid, False otherwise.
	"""
	#Record(f"Checking name: {name}")
	#Record(type(name))

	if not name.isalpha(): return False

	# Check if name has the right range of length in letters
	if len(name) < 4:
		#Record("Name Too Short")
		return False
	if len(name) > 10:
		#Record("Name Too Long")
		return False

	vowels = "aeiou"

	# Check if at least one of the first two letters is a vowel or an exception
	exceptions = ["br",    "tr", "pr", "gr", "fr","vl", "dr", "bl", "ch","kr", "sh", "th", 'kl', 'st']
	if not any(char in vowels for char in name[:2].lower()):
		if not name[:2].lower() in exceptions:
			return False

	# Check each substring of 3 letters for at least one vowel
	for i in range(len(name) - 2):
		chunk = name[i:i+3].lower()
		if not any(vowel in chunk for vowel in vowels):
			return False

	# Check for no more than two consecutive vowels
	consecutive_vowels = 0
	for char in name.lower():
		if char in vowels:
			consecutive_vowels += 1
			if consecutive_vowels > 2:
				return False
		else:
			consecutive_vowels = 0

	Valid = 'aeiou'
	if not any(char in Valid for char in name[-2:].lower()):
		# Last two letters should not be consonants
		return False

	# QUE or QUI use of Q
	for i in range(len(name) - 1):
		if name[i].lower() == 'q' and not (name[i+1:i+3].lower() in ["ue", "ui"]):
			return False

	if "aa" in name.lower(): return False
	if "ee" in name.lower(): return False
	if "ii" in name.lower(): return False
	if "uu" in name.lower(): return False
	if "pp" in name.lower(): return False
	if "jr" in name.lower(): return False

	return True

DEPTH = 3

def Mixer(names,prefix,fix,suffix, depth = 15):
	"""
	Mixes names by transforming the sound-alike letters in a name.
	"""

	import AtlasNomina.Linguistics as Linguistics

	sound_mappings = Linguistics.sound_mapping()

	# Generate a base name using NewWord and pass the seed for consistency
	Name =  NewWord(names,prefix,fix,suffix, depth-1)

	name_list = list(Name)
		# Transforms the name string into a list of letters

	# Iterate over each letter in the name
	for i in range(len(name_list)):
		original_letter = name_list[i].lower()
		# Decide whether to switch the letter (Weights=[switch,stay])
		if random.choices([True, False], weights=[7, 15])[0]:
			# Get the sound-alike options for the selected letter
			sound_alike_options = sound_mappings.get(original_letter, [])
			# If there are options, replace the letter
			if sound_alike_options:
				name_list[i] = random.choice(sound_alike_options)
	# Join the list back into a string
	result = ''.join(name_list).capitalize()
	result = entropify(result, names)
	return result

def mutate_entropy(base, fn, names):
	for _ in range(MAX_ATTEMPTS**2):
		new = fn(base, names)
		if new and is_valid_name(new, fn.__name__):
			return new
	return base
		# give up, keep original


def SyllabicExtraction(names):
	'''
	This function produces a set of syllables present in the words
	that make up the list of 'names'. It includes substrings of all lengths
	by sliding through each word.

	For 'Joan', it would produce:
	{'j', 'o', 'a', 'n', 'jo', 'oa', 'an', 'joa', 'oan', 'joan'}.

	Then it adds this set to the overall set, avoiding duplicates.
	'''
	import re
	syllables = set()
	pattern = re.compile(r'[bcdfghjklmnpqrstvwxyz]?[aeiou]{1,2}[bcdfghjklmnpqrstvwxyz]?')
	for name in names:
		chunks = pattern.findall(name.lower())
		for chunk in chunks:
			if 2 <= len(chunk) <= 4:
				syllables.add(chunk)

	return list(syllables)

def SyllabicComposition(names, min_syllables=2, max_syllables=6):
	syllables = SyllabicExtraction(names)
	if not syllables:
		return random.choice(names)
	selected = random.choices(syllables, k=random.randint(min_syllables, max_syllables))
	return ''.join(selected).capitalize()

def SyllabicWeightedExtraction(names):
	syllable_weights = defaultdict(int)
	for name in names:
		length = len(name)
		for i in range(length):
			for j in range(i+1, length+1):
				syllable = name[i:j].lower()
				syllable_weights[syllable] += 1
	return syllable_weights

def SyllabicWeightedName(names, min_syllables=2, max_syllables=6):
	# Extracting syllables and their weights
	syllables_with_weights = SyllabicWeightedExtraction(names)

	if not syllables_with_weights:
		return random.choice(names)

	syllables = list(syllables_with_weights.keys())
	weights   = list(syllables_with_weights.values())

	attempts = 0
	while attempts < 10:
		# pick between min_syllables and max_syllables chunks
		k = random.randint(min_syllables, max_syllables)
		selected_syllables = random.choices(population = syllables, weights=weights, k=k)
		name = ''.join(selected_syllables).capitalize()
		if is_valid_name(name, "SyllabicWeighted"):
			return name
		attempts += 1

	# if none passed validity in 10 tries, return whatever we last built
	return ''.join(selected_syllables).capitalize()


def SyllabicExtraction__Legacy(names):
	syllables = set()
	for name in names:
		length = len(name)
		for i in range(1, length):
			syllables.add(name[:i].lower())
			syllables.add(name[i:].lower())
	return list(syllables)

def SyllabicName__Legacy(syllables, min_syllables=2, max_syllables=8):
	name = ''.join(random.choice(syllables) for _ in range(random.randint(min_syllables, max_syllables)))
	return name.capitalize()
