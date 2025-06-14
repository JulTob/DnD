from collections import Counter
import math
import random

sample = [
	"Caderan",		"Zore",			"Ariel",		"Mernaz", 		"Zurvan", 		"Zania",		"Artemisia", 	"Aidenia", "Artemia", "Ardenia", "Alia",	"Artenia", "Alstroemeria", "Celestia", "Calliopia", "Dalia",	"Elisia", "Elyria", "Ejamia", "Gazania", "Jusia",	"Nala", "Nusia", "Nalia", "Nusia", "Naussia",		"Nubia", "Numia", 'Aveley','Asaelfr','Aredhel',	'Alveradis','Alva','Alfros','Alfridh','Alfin','Alflaug','Alfífa',	'Alfeizer',	'Alfagert',	'Alfadis',	'Albrun',	'Albegundi',	'Albelinda',	'Eldalote',		'Elfaru',		'Elferun',		'Alfil',		'Alfiz',		'Afelina',		'Elfreda',		'Alfilde',		'Aelfwynn','Aelfswif','Lili','Alba','Aelflaed',	'Aelfif','Aafje','Siofra','Arezu','Aria','Asal',	'Ava',	"Fariba",	"Faride",	"Gol",	"Golbahar","Golnar",	"Mitra","Mozgan","Nahid","Narges","Nasrin","Nazanin",		"Nazli","Neda","Negar","Negin","Nima","Niuxa","Nouxa",	"Paniz",	"Pari",	"Parisa",	"Parvane",	"Rana",	"Reza",			"Roxan",		"Roxas",		"Saba",			"Sajar",	"Sajar",		"Sanaz",		"Setar",		"Xiva",			"Sima",			"Simin",		"Sina",		"Soraya",		"Turaya",		"Vida",			"Yasaman",		"Jasaman",	"Yasamin",	"Jasmin",	"Balian",		"Caladwen", "Caspian", "Cian", "Deirdre",	"Einar",	 "Emrys",	"Eolande",	 "Faelan",	"Gael",  "Haldir", "Isolde",	"Kaelan", "Kaia", "Kian",	"Lorcan", "Lorien", "Luzien", "Maelis", "Maeve",		"Mitran", 		"Naida", 		"Niam", 		"Nuala", "Oisin",		"Orin", "Rianon", 		"Rordan", 		"Rogan", 		"Sable",	"Sirse", "Sariel", 		"Serafina", 	"Sorca", 		"Taran",		"Tariel", 	"Tarin", 		"Talia", 		"Tandor", 		"Tiranduil",	"Tirian", 		"Vanora", "Varian",	"Zarek", 	"Zarina", 	"Zelen", "Zorion", 		"Zephyr",	"Ardashir", "Azar", "Behzad", "Cyra", "Darius",		"Elara", "Farzin", "Golnar", "Jahan", "Jaleh",		"Kaven", 		"Kian", 		"Lalek", 		"Maxin", 		"Mitra",		"Neda", "Pari", "Ramin", "Roxana", "Shirin",	"Soraya", 		"Tamine", 		"Vayid", 		"Yasmine", 		"Zarir",		"Elfiridia", "Elefric", 		"Oforil", 		"Edric", 	"Etheltan",	"Horothigar", 	"Beowulf", 	"Hilda", 		"Alfred", 		"Friga",		"Areliana", 	"Ajeron", 		"Alila", 		"Aislin", 	"Aithne",	"Anwen", "Arlen", 	"Aurnia", 	"Bard", 	"Bevin",		"Blade", 		"Bran", 		"Briana", 		"Brin", 		"Celan", 		"Citriona", 	"Cime", 		"Catal", "Cianan",	"Ciara", "Conall", "Conloc", 		"Dagda", 		"Daraja",		"Dervila", 		"Devin", 	"Darmud", 		"Dillon", 	"Donovan",	"Druantia", "Amon", 		"Iblin", "Ezne", 		"Enda",		"Etain", 		"Fergus", "Finian", 		"Fion", 	"Graine",		"Keira", 		"Laise", 		"Lir", 			"Maebel", 		"Maire",		"Merin", 		"Neala", 		"Nial", 		"Nola", 		"Odran",		"Orlet", 		"Padrig", 		"Rona", 		"Rosin", 	"Ronan",	"Ruaidhri", "Saoirse", "Soban", 		"Sorca", 		"Talesin",		"Tiernan", 		"Turluj", 		"Una", 		"Seultan", 	"Zaira",		"Azade", 		"Baram", "Bardia", "Cyrus", "Daria",		"Darius", 	"Daric", 		"Elam", 		"Fara", 	"Feretan",	"Golshan", 		"Haleh", "Hamid", 		"Hoda", 	"Javane",		"Kamran", 		"Kian", 		"Ladan", 		"Leila", 		"Manaz",		"Merdad", 		"Narin", 		"Navid", 		"Parisa",		"Roxan", 		"Sajar", 		"Xaram", 		"Sapour", 		"Simin",		"Sorux", 		"Tamuras", 		"Yasmin", 		"Zara", 		"Zartos",		"Zefir", 	"Zalex",
	]

syze_SYMBOL = 3
STEPS = 1

def reduce_entropy(name, names = sample):
	return down_entropy(name, names, syze = syze_SYMBOL)
def increase_entropy(name, names = sample):
	return up_entropy(name, names, syze = syze_SYMBOL)
def to_mean_entropy(name, names = sample):
	return entropify(name, names, syze = syze_SYMBOL)

def down_entropy(name, names=sample, steps=STEPS, syze=3):
	symbol_entropies = calculate_symbol_entropies(names, syze=syze)
	name = replace_symbol(name, symbol_entropies, target='lower', syze=syze)
	return name.capitalize()

def up_entropy(name, names = sample, steps=STEPS, syze=3):
	symbol_entropies = calculate_symbol_entropies(names, syze=syze)
	name = replace_symbol(name, symbol_entropies, target='higher', syze=syze)
	return name.capitalize()

def entropify(name, names = sample, steps=STEPS, syze = 3):
	"""
	Adjusts the entropy of a name to be closer to the average entropy of the list of names.
	"""
	symbol_entropies = calculate_symbol_entropies(names, syze=syze)
	average_entropy = calculate_average_entropy(names, symbol_entropies, syze=syze)
	name = error_correct(name, symbol_entropies, syze=syze)
	current_entropy = calculate_name_entropy(name, symbol_entropies, syze=syze)
	while True:
		if current_entropy <= average_entropy*0.75:
			name = up_entropy(name, names, 1, syze=syze)
			current_entropy = calculate_name_entropy(name, symbol_entropies, syze=syze)
		elif current_entropy >= average_entropy*1.25:
			name = down_entropy(name, names, 1, syze=syze)
			current_entropy = calculate_name_entropy(name, symbol_entropies, syze=syze)
		else: break
	return name.capitalize()


def main():
	# Sample list of names
	names = sample

	symbol_entropies = calculate_symbol_entropies(names, syze=syze_SYMBOL)
	sorted_items = sorted(symbol_entropies.items(), key=lambda item: item[1], reverse=True)


	# Print the symbol entropies in a readable format
	print(f"{'Symbol':<10} {'Entropy':>10}")
	print("-" * 22)
	for symbol, entropy in sorted_items:
		print(f"{symbol:<10} {entropy:>10.4f}")

	original_name = "Legolas"
	print(f"Original Name: {original_name} {calculate_name_entropy(original_name,symbol_entropies)}")


	# Decrease entropy
	decreased_name = down_entropy(original_name, names, steps=STEPS)
	print(f"Name after decreasing entropy: {decreased_name} {calculate_name_entropy(decreased_name,symbol_entropies)}")
	# Increase entropy
	increased_name = up_entropy(original_name, names, steps=STEPS)
	print(f"Name after increasing entropy: {increased_name} {calculate_name_entropy(increased_name,symbol_entropies)}")

	# Entropify
	entropified_name = entropify(original_name, names, steps=STEPS)
	print(f"Name after entropify: {entropified_name} {calculate_name_entropy(entropified_name,symbol_entropies)}")


	print("Legolas: V")
	print(down_entropy("Legolas", steps=1, syze=3))
	print("Alia: ^")
	print(up_entropy("Alia",     steps=1, syze=3))
	print("Xzyq: ~")
	print(entropify("Xzyq",      steps=1, syze=3))

def replace_symbol(name, symbol_entropies, target='lower', syze=3):
	"""
	Attempts to improve entropy by randomly selecting a substring in the name
	and trying replacements. Stops as soon as a valid entropy improvement
	is found. Makes at most one substitution per call.
	"""
	# Asegúrate de que el nombre sólo contiene substrings válidas
	name = error_correct(name, symbol_entropies, syze=syze)
	original_entropy = calculate_name_entropy(name, symbol_entropies, syze=syze)

	substrings = find_substrings(name.lower(), syze)
	candidates = list(symbol_entropies.keys())

	# Get max/min entropies for synthetic assignment
	max_entropy = 1
	min_entropy = 0

	# If any substr in the name is missing in entropies, fix it first (recursively, for correction only)
	for substr in substrings:
		if substr not in symbol_entropies:
			# Assign an extreme entropy so the correction process knows what to do
			symbol_entropies[substr] = max_entropy if target == 'lower' else min_entropy
			# After correction, remove the artificial entry so it doesn't stay in the dict
			corrected = replace_symbol(name, symbol_entropies, target=target, syze=syze)
			del symbol_entropies[substr]
			return corrected

	# Now, all substrings are valid. Proceed with at most ONE entropy-improving substitution.
	best_name = name
	best_entropy = original_entropy
	improved = False

	# Candidates for replacement are those with valid entropy, and not the same as the current substr
	random.shuffle(substrings)
	for substr in substrings:
		idx = name.lower().find(substr)
		if idx == -1:
			continue

		random.shuffle(candidates)
		for candidate in candidates:
			if candidate == substr:
				continue
			# Do one substitution
			new_name = (name[:idx] + candidate + name[idx + syze:]).capitalize()
			# **Check ALL substrings in new_name are valid**
			new_substrings = find_substrings(new_name.lower(), syze)
			if any(s not in symbol_entropies for s in new_substrings):
				continue  # Skip candidates that would introduce invalid substrings

			new_entropy = calculate_name_entropy(new_name, symbol_entropies, syze=syze)
			# Check for improvement
			if (target == 'lower' and new_entropy < best_entropy) or (target == 'higher' and new_entropy > best_entropy):
				print(f"{name} → {candidate}  ({best_entropy:.4f} → {new_entropy:.4f}) : {new_name}")
				return new_name  # <--- Immediately return after one successful substitution

	# If no improvement found, return original name
	return name

def replace_low_entropy_symbol(name, symbol_entropies, syze=syze_SYMBOL):
	return replace_symbol(name, symbol_entropies, target='lower', syze=syze)

def replace_high_entropy_symbol(name, symbol_entropies, syze=syze_SYMBOL):
	return replace_symbol(name, symbol_entropies, target='higher', syze=syze)

def get_symbols_in_name(name, symbol_entropies, syze):
	"""
	Finds substrings in a name and retrieves their entropies.
	Assigns a default entropy valuem of 1 to substrings not found in symbol_entropies.

	Parameters:
		name (str): The name to analyze.
		symbol_entropies (dict): A dictionary mapping symbols to their entropies.
		syze (int): Minimum length of substrings to consider.

	Returns:
		dict: A dictionary mapping substrings in the name to their entropies.
	"""
	substrings = find_substrings(name, syze)
	symbols_in_name = {}
	max_entropy = max(symbol_entropies.values(), default=1.0)
	for substring in substrings:
		entropy = symbol_entropies.get(substring, max_entropy)
		symbols_in_name[substring] = entropy
	return symbols_in_name

def find_substrings(name, syze):
	"""
	Generates all possible substrings of a given name with a minimum length.

	Parameters:
		name (str): The name from which to extract substrings.
		syze (int): Minimum length of substrings to consider.

	Returns:
		list of str: A list of substrings.
	"""
	assert isinstance(name, str), "The 'name' parameter must be a string."
	assert isinstance(syze, int) and syze >= 1, "The 'syze' must be an integer greater than or equal to 1."

	substrings = []
	length = len(name)
	for i in range(length - syze + 1):
		substrings.append(name[i:i + syze])
	return substrings

def error_correct(name, symbol_entropies, syze=syze_SYMBOL):
	return name.capitalize()

def calculate_average_entropy(names, symbol_entropies, syze=syze_SYMBOL):
	"""
	Calculates the average entropy across a list of names.
	"""
	total_entropy = 0.0
	for name in names:
		name_entropy = calculate_name_entropy(name, symbol_entropies, syze)
		total_entropy += name_entropy
	average_entropy = total_entropy / len(names)
	return average_entropy

def calculate_name_entropy(name, symbol_entropies, syze=syze_SYMBOL):
	"""
	Calculates the average entropy of the substrings in a name.

	>>Parameters:
		name (str): The name to analyze.
		symbol_entropies (dict): A dictionary mapping symbols to their entropies.
		syze (int): Minimum length of substrings to consider.
	<<Returns:
		float: The entropy of the name.
	"""
	name = error_correct(name, symbol_entropies, syze=syze)
	symbols_in_name = get_symbols_in_name(name.lower(), symbol_entropies, syze)
	if not symbols_in_name:
		return 0
	total_entropy = sum(symbols_in_name.values())
	return total_entropy

def calculate_symbol_probabilities(names, syzes):
	"""
	Calculates the probability of each symbol (substring) in the names list.
	"""
	substring_counter = Counter()
	total_substrings = 0

	for syze in syzes:
		for name in names:
			substrings = find_substrings(name.lower(), syze)
			substring_counter.update(substrings)
			total_substrings += len(substrings)
		symbol_probabilities = {}
		for substring, count in substring_counter.items():
			probability = count / total_substrings
			symbol_probabilities[substring] = probability

	return symbol_probabilities

def calculate_symbol_entropies(names, syze=syze_SYMBOL):
	"""
	Calculates the entropy of each symbol (substring) in the names list.

	Parameters:
		names (list of str): A list of reference names.
		syze (int): Minimum length of substrings to consider.

	Returns:
		dict: A dictionary mapping symbols to their entropies.
	"""
	assert names, "The 'names' list cannot be empty."
	assert isinstance(syze, int) and syze >= 1, "The 'syze' must be an integer greater than or equal to 1."

	symbol_probabilities = calculate_symbol_probabilities(names, [syze-1, syze, syze+1])
	symbol_entropies = {}
	#symbol_entropies[""] = 0.0
	for symbol, probability in symbol_probabilities.items():
		assert 0 < probability <= 1, "Probability must be between 0 and 1."
		entropy = -probability * math.log2(probability)
		symbol_entropies[symbol] = entropy
	return symbol_entropies

if __name__ == "__main__":
	main()
