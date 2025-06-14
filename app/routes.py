# /app/routes.py

''' Cartography '''
from flask import render_template, request, redirect, url_for, Response, jsonify, session
from urllib.parse import quote_plus, unquote_plus

from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError
from random import randint
import random


Initialized("Routes: Atlas ready.")

# Initialize routes
def init_routes(app):
	"""Initialize all routes for the D&D character generator application."""
	Initialized("<Init Routes()<")

	@app.route('/')
	def home():
		"""
		Serve the homepage and set up default options for
		races, species, classes, backgrounds, and archetypes.
		"""
		from AtlasAlusoris.Map_of_Races 	import race_weights
		from AtlasAlusoris.Map_of_Archetypes 	import Archetypes, Archetype
		from AtlasLusoris.Map_of_Backgrounds	import backgrounds
		from AtlasLusoris.Map_of_Species 	import species
		from AtlasLusoris.Map_of_Classes 	import classes
		Initialized("<Init Routes<home>")
		# Races
		races = [race for race in race_weights.keys() if race]
		races.sort()
		races.insert(0, "Random")
			# Add "Random" as the first option

		# Species
		try:
			species_list = list(species.keys())
			species_weights = list(species.values())
		except (ImportError, NameError) as e:
			species_list = ["Human", "Elf", "Dwarf"]
			species_weights = [1,1,1]
			Alert("No Species Were found in the Routes. Defaulted lists.", e)

		# Classes
		class_list = ["Random"] + classes

		# Backgrounds for PCs
		char_backgrounds = ["Random"] + backgrounds

		# Species for PCs
		char_species = ["Random"] + species_list

		# Archetypes for NPCs
		npc_archetypes = ["Random"] + Archetypes

		html = render_template('index.html',
								races=races,
								species_list=char_species,
								class_list=class_list,
								char_backgrounds = char_backgrounds,
								npc_archetypes=npc_archetypes,
								)
		return html # Response(html, mimetype='text/html')

	@app.route('/favicon.ico')
	def favicon():
		svg = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
<text x="50%" y="50%" dominant-baseline="central" text-anchor="middle" font-size="48">⚜️</text>
</svg>
'''
		return Response(svg, mimetype='image/svg+xml')

	@app.route('/character')
	def random_character():
		"""
		Redirect to a randomly generated character display page.
		"""
		Initialized("<Init Routes<character>")
		seed = random.randint(1, 2**8)
		level = random.randint(1, 20)
		character = summon_character(level=level, seed=seed)
		char_dict = character.to_dict()

		# URL-encode parameters for the redirect
		species = quote_plus(char_dict['Species'])
		char_class = quote_plus(char_dict['Class'])
		background = quote_plus(char_dict['Background'])
		gender = quote_plus(char_dict['Gender'])
		#name = quote_plus(char_dict['name'])
		return redirect(url_for('character_display',
								species=species,
								char_class=char_class,
								background=background,
								level=level,
								gender=gender,
								seed=seed))

	@app.route('/character/<species>/<char_class>/<background>/<int:level>/<gender>/<seed>', methods=['GET'])
	def character_display(species, char_class, background, level, gender, seed):
		"""	Display a generated character
			based on the specified parameters.	"""
		species = unquote_plus(species)
		char_class = unquote_plus(char_class)
		background = unquote_plus(background)
		gender = unquote_plus(gender)
		#name = unquote_plus(name)

		# Generate the character with provided parameters
		character = summon_character(
			species=species,
			char_class=char_class,
			background=background,
			level=level,
			gender=gender,
			seed=seed)
		char_dict = character.to_dict()

		return render_template('character.html', character=char_dict)

	@app.route('/generate_character', methods=['POST'])
	def generate_character_route():
		"""	Handle character generation requests
			with selected form data.
			"""
		Initialized("<Init Routes<character>")
		selected_species = request.form.get('species', 'Random')
		selected_class = request.form.get('class', 'Random')
		selected_background = request.form.get('background', 'Random')
		level = int(request.form.get('level', random.randint(1, 20)))
		seed = random.randint(0, 2**8)

		# Define default species, class, archetype if 'Random' is chosen
		species = 		selected_species 	if selected_species 	!= 'Random' else None
		char_class = 	selected_class 		if selected_class 		!= 'Random' else None
		background = 	selected_background 	if selected_background 	!= 'Random' else None

		character = summon_character(
			species = species,
			char_class = char_class,
			background = background,
			level = level,
			seed = seed
			)

		Inform(f"Character initialized with level: {character.level}, skills: {character.skills}")

		char_dict = character.to_dict()

		# URL-encode parameters for the redirect
		species_encoded = quote_plus(char_dict['Species'])
		char_class_encoded = quote_plus(char_dict['Class'])
		background_encoded = quote_plus(char_dict['Background'])

		gender = quote_plus(char_dict['Gender'])

		return redirect(url_for('character_display',
								species=species_encoded,
								char_class=char_class_encoded,
								background=background_encoded,
								level=level,
								seed=seed,
								gender=gender))

	@app.route('/character/random')
	def character_random():
		seed = random.randint(0, 2**8)
		level = random.randint(1, 20)
		character = summon_character(level=level, seed=seed)
		return render_template('character.html', character=character)

	@app.route('/npc')
	def random_npc():
		from AtlasLudus.Map_of_Dice 	import Dice
		from AtlasAlusoris.Map_of_Races 	import Race
		from AtlasAlusoris.Map_of_Archetypes 	import Archetypes, Archetype
		from urllib.parse import quote_plus
		"""Redirect to a randomly generated NPC display page."""
		Initialized("<Init Routes<Random npc>")
		seed = randint(1,2**8)
		race = Race()
		archetype = Archetype()
		level = Dice(6,3)
		return redirect(
			url_for(
				'npc_display',
				race=race,
				archetype=archetype,
				level=level,
				seed = seed
				)
			)

	@app.route('/npc/<race>/<archetype>/<level>/<seed>', methods=['GET'])
	def npc_display(race,archetype,level,seed):
		"""Display a generated NPC based on the specified parameters."""
		from AtlasAlusoris.Map_of_NPC 	import NPC
		from AtlasAlusoris.Map_of_Races import race_weights
		from AtlasAlusoris.Map_of_Archetypes import Archetypes
		Initialized("<Init Routes<NPC>")
		if seed is None:
			seed = randint(1,2**8)
		else:
			seed = int(seed)
		random.seed(seed)
		response = f"New NPC - Seed: {seed}, Archetype: {archetype}, Level: {level}, Race: {race}"
		Initialized(response)

		npc = NPC(
			race = unquote_plus(race),
			archetype = unquote_plus(archetype),
			lvl = int(level),
			seed = seed)
		session['npc'] = npc.to_dict()
		Ends("NPC Invoqued")
		return render_template(
			'npc.html',
			npc=npc,
			races=list(race_weights.keys()),
			npc_archetypes=Archetypes)

	@app.route('/generate_npc', methods=['POST'])
	def npc_generator():
		"""Handle NPC generation requests with selected form data."""
		from AtlasLudus.Map_of_Dice 	import Dice
		from AtlasAlusoris.Map_of_Races 	import Race
		from AtlasAlusoris.Map_of_Archetypes 	import Archetypes, Archetype
		Initialized("<Init Routes<New NPC>")
		seed = random.randint(1,2**8)


		# Get the selected race and archetype from the form data
		selected_race = request.form.get('race', 'Random')
		selected_archetype = request.form.get('archetype', 'Random')

		# If 'Random' is selected, pick a race or archetype at random
		if selected_race == 'Random':
				selected_race = Race()
		if selected_archetype == 'Random':
				selected_archetype = Archetype()
		level_input = request.form.get('level', '')
		try:
			level = int(level_input) if level_input.isdigit() else Dice(10, 2)
		except:
			level = Dice(10, 2)
		# Redirect to the detailed NPC page
		return redirect(url_for('npc_display', race=selected_race, archetype=selected_archetype, level=level, seed=seed))

	@app.context_processor
	def utility_processor():
		"""Utility processor for Jinja templates."""
		from AtlasLudus.Map_of_Dice 	import Dice
		from AtlasActorLudi.Map_of_Scores 	import Modifier
		from AtlasPugna.Map_of_Legendary_Actions import Legendary, Region, Lair
		return dict(Modifier=Modifier, Dice=Dice, Lair=Lair, Legendary=Legendary, Region=Region)

	def generate_html_for_npcs(npcs):
		html_content = ""
		for npc, seed in npcs:
					# Constructing the URL
			npc_link = url_for('npc_display', race=npc.race, archetype=npc.archetype, level=npc.level, seed=seed)
			# Embedding the URL in the HTML
			html_content += f'<a href="{npc_link}"> <h3>{npc.name}, <b>{npc.title}</b></h3></a><i> {npc.race}, {npc.archetype}</i><br>'
		return html_content


	@app.route('/list', defaults={'race': 'Random', 'archetype': 'Random'})
	@app.route('/list/<race>/<archetype>', methods=['GET'])
	def npc_list(race, archetype):
		from AtlasAlusoris.Map_of_NPC import NPC
		from AtlasAlusoris.Map_of_Races import race_weights
		from AtlasAlusoris.Map_of_Archetypes import Archetypes
		from random import randint, choice
		from urllib.parse import unquote_plus
		# Normalize input
		race = unquote_plus(race)
		archetype = unquote_plus(archetype)
			# Randomize if needed
		if race == "Random":
			NPCrace = choice(list(race_weights.keys()))
		if archetype == "Random":
			NPCarchetype = choice(Archetypes)

		npcs = []
		seed = randint(0, 16383)
		for i in range(5):
			level = randint(1, 20)
			if race == "Random":
				NPCrace = choice(list(race_weights.keys()))
			if archetype == "Random":
				NPCarchetype = choice(Archetypes)

			npc = NPC(
				race=NPCrace,
				archetype=NPCarchetype,
				lvl=level,
				seed=seed + i,
				light=True)
			npcs.append(npc)

		return render_template("npclist.html", npcs=npcs, race=race, archetype=archetype)


	def summon_character(species=None, char_class=None, background=None, level=1, gender=None, seed=None):
		from AtlasLusoris.Grimoire_of_Characters import Character
		return Character(
			species=species,
			char_class=char_class,
			background=background,
			level=level,
			gender=gender,
			seed=seed,
			)
