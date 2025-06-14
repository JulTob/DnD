from Minion import Record, Initialized, Alert, Warning, News, Ends, Fail, Catched, FailureError
import random
import time
from contextlib import contextmanager
from collections import defaultdict, Counter

try: # Cartography:
	import AtlasAlusoris.Map_of_NPC as NPC
	from AtlasLudus.Map_of_Dice     import Dice
	from AtlasNomina.Map_of_Word_Entropy import entropify, reduce_entropy, increase_entropy, to_mean_entropy
	from AtlasLudus.Map_of_Useful_Functions import select1
except FailureError as failed:
	Fail(f"The Atlas to Names have not been found:\n {failed}", failed)
	raise FailureError

MAX_ATTEMPTS = 3
MAX_DEPTH = 1

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
						Record(f"Naming Strategy Syllabic Extraction: {name}")
						name_ent = entropify(name, names)
						if name_ent and is_valid_name(name, strategy):
							Record(f"Strategy Syllabic Extraction + Entropify: {name}")
							name = name_ent
						return name
			elif strategy == "Mix":
				name = Mixer(names, prefix, fix, suffix, depth + 1)
				name_b = name
				if name and is_valid_name(name, strategy):
					Record(f"Naming Strategy {strategy}: {name}")
					return name
				Record(f"Naming Strategy {strategy} FAILED: {name}")
			elif strategy == "EchoMorphology":
				name = random.choice(names) # NewWord(names, prefix, fix, suffix, depth + 1)
				for i in range(MAX_ATTEMPTS):
					name = EchoMorphology(name)
					if name and is_valid_name(name, strategy):
						Record(f"Naming Strategy Echomorphology: {name}")
					name = entropify(name, names)
					if name and is_valid_name(name, strategy):
						Record(f"Naming Strategy Echomorphology + Entropify: {name}")
						return name
				Record(f"Naming Strategy {strategy} FAILED: {name}")
				return random.choice(names) # NewWord(names, prefix, fix, suffix, depth + 1)
			elif strategy == "Syllabic":
				name = Syllabic(prefix, fix, suffix)
				if name:
					Record(f"Naming Strategy Syllabic Composition: {name}")
					return name
			elif strategy == "Choose":
				name = random.choice(names)
				Record(f"Naming Strategy Chosen: {name}")
				return name
			elif strategy == "Markov":
					markov = MarkovNameGenerator(names)
					for _ in range(MAX_ATTEMPTS):
						name = markov.generate_name()
						if name and is_valid_name(name, strategy):
							Record(f"Naming Strategy {strategy}: {name}")
							return name
			elif strategy == "PhonotacticWeighted":
					phonotactics = ExtractWeightedPhonotacticElements(names)
					for i in range(MAX_ATTEMPTS):
						name = GenerateFromWeightedPhonotactics(phonotactics)
						if name and is_valid_name(name, strategy):
							Record(f"Naming Strategy Phonotactic Extracted: {name}")
							return name
			else:
				Record(f"Naming Strategy Default Chosen: {name}")
				name = random.choice(names)
				return name

		except Exception as e:
			Alert(f"Error In Naming by {strategy}: \n\t {e} ")
			return random.choice(names)
	Alert(f"Fallback name: {name}")
	return random.choice(names)

def Surnamer(lusor,  i=0):
	"""Deterministic surname: we just offset the seed by +1."""
	with deterministic(lusor.seed + i):
		Record("Surname Builder Initiated")
		random.seed(lusor.seed + i)
		surnames = SurnamesList(lusor)
		o, n, c = Surphonotactic(lusor)
		surname = NewWord(surnames, o, n, c)
	return surname.capitalize()

def Namer(lusor, i=0):
	with deterministic(lusor.seed + i):
			Record("Name Builder Initiated")
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
			except Exception as e:
				Warning(f"Name strategy failed: {e}")
			return None

		with ThreadPoolExecutor() as ex:
			futures = [ex.submit(task, fn) for fn in strategy_fns]
			try:
				done, _ = wait(futures, timeout=timeout, return_when=FIRST_COMPLETED)
			except TimeoutError:
				Warning(f"Naming strategies timed out after {timeout}s.")
				continue

			for fut in done:
				result = fut.result()
				if result:
					return result

		Record(f"Attempt {attempt + 1}/{retries} found no valid name. Retrying...")

	# All attempts failed or timed out; fallback to predefined list
	fallback_name = random.choice(fallback_names)
	Warning(f"All strategies failed or timed out. Falling back to: {fallback_name}")
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
	try:
		module_path = race_module_map.get(trait)
		if module_path:
			race = importlib.import_module(module_path)
			return race
		Fail(f"No known race found for {trait}, using fallback.")
		return importlib.import_module("AtlasNomina.Races.plantilla")
	except ImportError as e:
		Fail(f"Import failed for {trait}:", e)
		return importlib.import_module("AtlasNomina.Races.plantilla")
	except ModuleNotFoundError as e:
		Fail(f"Import not found for {trait}:", e)
		return importlib.import_module("AtlasNomina.Races.plantilla")
	except SyntaxError as e:
		Fail(f"Syntax error in {trait} race module: {e}")
		return importlib.import_module("AtlasNomina.Races.plantilla")
	except:
		Fail(f"Unknown error for {trait} Name library:")
		return importlib.import_module("AtlasNomina.Races.plantilla")

def NewName(lusor):
	"""
	Generate a full name for the given lusor (character).
	"""
	from random import seed
	import AtlasNomina.Races.plantilla as fallback

	genus = lusor.genus
	seeding = lusor.seed
	seed(seeding)

	race = LoadRace(lusor.race)

	try:
		names = race.Names(genus)
	except AttributeError:
		names = fallback.Names(genus)

	try:
		surnames = race.Surnames(genus)
	except AttributeError:
		surnames = fallback.Surnames(genus)

	try:
		o, n, c = race.Phonotactic(genus)
	except AttributeError:
		o, n, c = fallback.Phonotactic(genus)

	try:
		os, ns, cs = race.Surphonotactic(genus)
		Record(f"Loaded race module: {race} at {dir(race)}")

	except AttributeError:
		os, ns, cs = fallback.Surphonotactic(genus)
		Fail(f"Loaded race module: {race} at {dir(race)}")
		Fail(f"Race module path: {race.__file__}")
		Fail(f"lusor.race: {lusor.race!r}")


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
			f"{name} {name2} <br> {surname} {surname2}",
			])
	elif "Gnome"         in genus:
		name = NewWord(names, o, n, c).capitalize()
		name2 = NewWord(names, o, n, c).capitalize()
		name3 = NewWord(names, o, n, c).capitalize()
		surname = NewWord(surnames, os, ns, cs).capitalize()
		FullName =  f"{name} {name2} {name3}<br> {surname}"
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

	News(f'Name Selected: {FullName}')
	return FullName.title()

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
	Record("General Phonotactic called")
	genus = lusor.genus
	race = LoadRace(lusor.race)  # Dynamically load the race module
	# Check if the race module has a `Phonotactic` method
	try:
		prefix, fix, suffix = race.Phonotactic(genus)
		return prefix, fix, suffix
	except AttributeError:
		# If no `Phonotactic` function is found in the race, fallback to a default
		Warning(f"No 'Phonotactic' function found in {race}. Using fallback.")
		import AtlasNomina.Races.plantilla as fallback
		return fallback.Phonotactic(genus)
	except Exception as e:
		Fail(f"Name generation failed. Falling back. Error: {e}")
		import AtlasNomina.Races.plantilla as fallback
		return fallback.Phonotactic(genus)

	return prefix, fix, suffix

def Surphonotactic(lusor):
	Record("General Surhonotactic called")
	genus = lusor.genus
	race = LoadRace(lusor.race)  # Dynamically load the race module
	try:
		prefix, fix, suffix = race.Surphonotactic(genus)
	except AttributeError:
		# If no `Phonotactic` function is found in the race, fallback to a default
		Warning(f"No 'Phonotactic' function found in {race}. Using fallback.")
		import AtlasNomina.Races.plantilla as fallback
		prefix, fix, suffix = fallback.Surphonotactic(genus)
	Record(prefix)
	Record(fix)
	Record(suffix)
	return prefix, fix, suffix

def NamesList(lusor):
	Names = []
	race = LoadRace(lusor.race)
	try:
		Names = race.Names(lusor.genus)
	except AttributeError:
		Warning(f"No 'Names' for {race}. Using fallback.")
		from AtlasNomina.Races import plantilla
		Names = plantilla.Names(lusor.genus)
	Record(Names)
	if not Names:
		Names = Races.plantilla.Names(genus)
	return Names

def SurnamesList(lusor):
	race = LoadRace(lusor.race)
	try:
		Surnames = race.Surnames(lusor.genus)
	except AttributeError:
		Warning(f"No 'Surnames' in {race}. Using fallback.")
		from AtlasNomina.Races import plantilla
		Surnames = plantilla.Surnames(lusor.genus)
	else:
		Warning(f"No specific race match for {lusor.race}. Using fallback.")
		from AtlasNomina.Races import plantilla
		Surnames = plantilla.Surnames(lusor.genus)
	return Surnames

def Syllabic(prefix,fix,suffix):
	'''
	-- Syllabic Union. --
	Creates a syllabic union from the prefix, fix, and suffix lists.
	'''
	pre = random.choice(prefix)
	fix = random.choice(fix)
	suf = random.choice(suffix)

	result = f"{pre}{fix}{suf}"
	Record(f"Syllabic union (pre-fix-suf) produced: {result}")
	return result

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
	Record(f"{strategy}: Checking '{name}' for validity.")

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

	Record(f"{strategy}: '{name}' is valid.")
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
	Record(f'Mixer function: {result}')
	result = entropify(result, names)
	Record(f'Mixer function result: {result}')
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
		Alert("EMPTY WEIGHT DICTIONARY")
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

class MarkovNameGenerator:
	def __init__(self, names, order=random.randint(1, 6)):
		self.names = [name.lower() for name in names if isinstance(name, str)]
		self.order = order
		self.chain = defaultdict(Counter)
		self.starting_states = []
		self.populate_markov_chain()

	def ends_well(self, name):
		return (
			len(name) > 2
			and name[-1] in 'aeioulnrst'
			and not name.endswith(('kk', 'rr', 'zz'))
			)

	def populate_markov_chain(self):
		for name in self.names:
			padded_name = ('^' * self.order) + name + '$'
			for i in range(len(padded_name) - self.order):
				state = padded_name[i:i + self.order]
				next_char = padded_name[i + self.order]
				self.chain[state][next_char] += 1
				if i == 0:
					self.starting_states.append(state)

	def _weighted_random_choice(self, counter):
		choices, weights = zip(*counter.items())
		return random.choices(choices, weights=weights)[0]

	def generate_name(self, min_length=4, max_length=10, max_attempts=20):
		vowels = 'aeiou'
		consonants = 'bcdfghjklmnpqrstvwxyz'

		for attempt in range(max_attempts):
			state = random.choice(self.starting_states)
			name = ''
			consecutive_vowels = consecutive_consonants = 0

			while True:
				next_char = self._weighted_random_choice(self.chain[state])

				if next_char == '$':
					if min_length <= len(name) <= max_length:
						break  # Valid end
					else:
						# Too short, retry from start
						state = random.choice(self.starting_states)
						name = ''
						consecutive_vowels = consecutive_consonants = 0
						continue

				# Avoid triple repeating letters
				if len(name) >= 2 and next_char == name[-1] == name[-2]:
					continue

				# Enforce vowel/consonant balance
				if next_char in vowels:
					consecutive_vowels += 1
					consecutive_consonants = 0
					if consecutive_vowels > 2:
						continue
				elif next_char in consonants:
					consecutive_consonants += 1
					consecutive_vowels = 0
					if consecutive_consonants > 3:
						continue
				else:
					consecutive_vowels = consecutive_consonants = 0

				name += next_char
				state = state[1:] + next_char

				if len(name) >= max_length:
					break  # Forcefully truncate long names

			name = name.capitalize()
			if is_valid_name(name, "Markov"):
				return name

		# After max attempts, fallback to random choice
		fallback = random.choice(self.names).capitalize()
		return fallback
