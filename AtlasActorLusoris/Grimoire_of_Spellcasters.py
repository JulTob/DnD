# AtlasLusoris/Grimoire_of_Spellcasters.py

import random
from AtlasMagia.Lodge_of_Spells import *



class Spellcaster:
	def __init__(caster, character, known=None):
		if known is None:	  known = []
		caster.character 	= character
		caster.level 		= character.level
		caster.casting_stat = caster.get_casting_stat()
		caster.spell_slots 	=  caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.prepare_spells()

	def get_casting_stat(caster):
		return "INT"  # default, override in subclasses

	def get_spell_slots(caster):
		slots_table = {}
		return slots_table

	def available_spells(caster):
		"""Return all spells this character can *learn* at their current level."""
		table = SPELL_LISTS.get(caster.character.char_class, {})
		# Collapse all spell levels the character has unlocked
		unlocked = [lvl for lvl in table if lvl <= caster.level]
		spells = [s for lvl in unlocked for s in table[lvl]]
		return spells

	def prepare_spells(caster):
		random.seed(self.character.seed)


	def __str__(caster):
		spells_names = "".join(f"<li>〖{spell.level}〗{spell.name}</li>" for spell in caster.spells_known)
		slots_html = ", ".join(f"Level {lvl}: {num}" for lvl, num in caster.spell_slots.items())
		spells_html = "".join(f"""<div class="npc-textbox">{spell}</div>""" for spell in caster.spells_known)

		return f"""
			<h1 style="font-family: 'Iglesia'; font-size:	3.1em; ">{caster.character.char_class} Spellcasting</h1>
			<p><b>Spell Slots:</b> {slots_html}</p>
			<ul style="list-style-type: '🪄'; text-align: left; font-family: 'Iglesia'">{spells_names}</ul>
			</div>
			{spells_html}
		"""

	def html(caster):
		if not caster.spells_known:
			return "<i>No spells known</i>"
		list_items = "".join(f"<li>{s.name}</li>" for s in caster.spells_known)
		return f"<b>Spellcasting</b><ul>{list_items}</ul>"

class Wizard(Spellcaster):
	def __init__(caster, character, known=None):
		if known is None:	  known = []
		caster.class_name 	= "Wizard"
		caster.character 	= character
		caster.level 		= character.level
		caster.spell_slots 	=  caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.casting_stat = caster.get_casting_stat()
		caster.prepare_spells()

	def get_casting_stat(caster):
		return "INT"

	def get_stats(caster, key):
		table = {
			1:  {"cantrips": 3, "spells": 4, 	"slots": (2,0,0,0,0,0,0,0,0)},
			2:  {"cantrips": 3, "spells": 5,  	"slots": (3,0,0,0,0,0,0,0,0)},
			3:  {"cantrips": 3, "spells": 6,  	"slots": (4,2,0,0,0,0,0,0,0)},
			4:  {"cantrips": 4, "spells": 7,  	"slots": (4,3,0,0,0,0,0,0,0)},
			5:  {"cantrips": 4, "spells": 9,  	"slots": (4,3,2,0,0,0,0,0,0)},
			6:  {"cantrips": 4, "spells": 10,  	"slots": (4,3,3,0,0,0,0,0,0)},
			7:  {"cantrips": 4, "spells": 11,  	"slots": (4,3,3,1,0,0,0,0,0)},
			8:  {"cantrips": 4, "spells": 12,  	"slots": (4,3,3,2,0,0,0,0,0)},
			9:  {"cantrips": 4, "spells": 14,  	"slots": (4,3,3,3,1,0,0,0,0)},
			10: {"cantrips": 5, "spells": 15,  	"slots": (4,3,3,3,2,0,0,0,0)},
			11: {"cantrips": 5, "spells": 16,  	"slots": (4,3,3,3,2,1,0,0,0)},
			12: {"cantrips": 5, "spells": 16,  	"slots": (4,3,3,3,2,1,0,0,0)},
			13: {"cantrips": 5, "spells": 17,  	"slots": (4,3,3,3,2,1,1,0,0)},
			14: {"cantrips": 5, "spells": 18,  	"slots": (4,3,3,3,2,1,1,0,0)},
			15: {"cantrips": 5, "spells": 19,  	"slots": (4,3,3,3,2,1,1,1,0)},
			16: {"cantrips": 5, "spells": 21,  	"slots": (4,3,3,3,2,1,1,1,0)},
			17: {"cantrips": 5, "spells": 22,  	"slots": (4,3,3,3,2,1,1,1,1)},
			18: {"cantrips": 5, "spells": 23,  	"slots": (4,3,3,3,3,1,1,1,1)},
			19: {"cantrips": 5, "spells": 24,  	"slots": (4,3,3,3,3,2,1,1,1)},
			20: {"cantrips": 5, "spells": 25,  	"slots": (4,3,3,3,3,2,2,1,1)},
			}
		lvl = caster.level
		if lvl > 20: lvl = 20
		value = table.get(lvl, {"cantrips": 0, "spells": 0, "slots": (0,0,0,0)})
		if key == "cantrips":
			return value["cantrips"]
		if key == "spells":
			return value["spells"]
		if key == "slots":
			return {i + 1: val for i, val in enumerate(value["slots"])}

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def prepare_spells(caster):
		random.seed(self.character.seed)
		num_spells = caster.level*2 + 4
		available = caster.available_spells()
		caster.spells_known = random.sample(available, min(len(available), num_spells))

	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return str(caster)

	def __str__(caster):
		n = caster.get_stats("spells")
		cantrips = [s for s in caster.spells_known if s.level == 0]
		other_spells = [s for s in caster.spells_known if s.level > 0]

		random.shuffle(other_spells)
		prepared = other_spells[:n]
		unprepared = other_spells[n:]
		all_spells = sorted(prepared + unprepared, key=lambda s: (s.level, s.name))
		spells = ""
		for spell in cantrips:
			spells += f"<li>【{spell.level}】{spell.name}</li>"
		for spell in all_spells:
			if spell in prepared or spell.level==0:
				spells += f"<li>【{spell.level}】{spell.name}</li>"
			else:
				spells += f"<li>〖{spell.level}〗{spell.name}</li>"
		slots_html = "<br>".join(
			f"<b>Level {lvl}</b>: <i>{num}</i>" for lvl, num in caster.spell_slots.items()
			)
		spells_html = "".join(
			f"""<div class="npc-textbox">{spell}</div>"""
			for spell in cantrips
			)
		spells_html += "".join(
			f"""<div class="npc-textbox">{spell}</div>"""
			for spell in all_spells
			)
		return f"""
			<div class="npc-textbox" style="grid-column: span 3;">
				<h1 style="font-family: 'Iglesia'; font-size:	3.1em; ">
					Wizard Spellcasting</h1>
				<p> As a student of arcane magic, you have learned to cast spells. </p>
				</div>
			<div class="npc-textbox" style="grid-column: span 1;">
				<h2>Spell Slots:</h2>
				{slots_html} <br>
				You regain all expended slots when you finish a Long Rest.</p>
				<br><br>
				</div>
			<div class="npc-textbox" style="grid-column: span 1;">
			<h3 style="font-family: 'Iglesia'; font-size:	3.1em; "> SpellBook </h3>
			You may prepare {n} spells whenever you finish a Long Rest, that you can use at any moment, from your book of spells:
			<ul style="list-style-type: '🪄'; text-align: left; font-family: 'Iglesia' ">
				{spells}</ul>
			<h2>Arcane Focus</h2>
			You can use an Arcane Focus (such as a wand or scepter),  as a Spellcasting Focus for your Wizard spells.
			</div>
			{spells_html}
			"""

class Sorcerer(Spellcaster):
	def __init__(caster, character):
		super().__init__(character)
		caster.metamagic_points = caster.level  # Basic rule, extend as needed

	def get_casting_stat(caster):
		return "CHA"

	def get_spell_slots(caster):
		slots_table = {
			1: {1: 2}, 2: {1: 3}, 3: {1: 4, 2: 2},
			4: {1: 4, 2: 3}, # Extend as needed
		}
		return slots_table.get(caster.level, {})

	def prepare_spells(caster):
		random.seed(self.character.seed)
		num_spells = caster.level + 1
		available = caster.available_spells()
		caster.spells_known = random.sample(available, min(len(available), num_spells))

	def __str__(caster):
		base_str = super().__str__()
		return base_str + f"<p><strong>Metamagic Points:</strong> {caster.metamagic_points}</p>"

class Monk(Spellcaster):
	def __init__(caster, character):
		super().__init__(character)
		caster.ki_points = caster.level

	def get_casting_stat(caster):
		return "WIS"

	def get_spell_slots(caster):
		return {}  # Monks typically don't use spell slots unless subclass-specific

	def prepare_spells(caster):
		random.seed(self.character.seed)
		caster.spells_known = []  # Typically none, unless subclass-specific

	def __str__(caster):
		return f"""
		<div class="spellcasting">
			<h3>Monk Ki Points</h3>
			<p><strong>Ki Points:</strong> {caster.ki_points}</p>
		</div>
		"""

class EldritchKnight(Spellcaster):
	def get_casting_stat(caster):
		return "INT"

	def get_stats(caster, key):
		table = {
			1:  {"cantrips": 0, "spells": 0,  "slots": (0,0,0,0)},
			2:  {"cantrips": 0, "spells": 0,  "slots": (0,0,0,0)},
			3:  {"cantrips": 2, "spells": 3,  "slots": (2,0,0,0)},
			4:  {"cantrips": 2, "spells": 4,  "slots": (3,0,0,0)},
			5:  {"cantrips": 2, "spells": 4,  "slots": (3,0,0,0)},
			6:  {"cantrips": 2, "spells": 4,  "slots": (3,0,0,0)},
			7:  {"cantrips": 2, "spells": 5,  "slots": (4,2,0,0)},
			8:  {"cantrips": 2, "spells": 6,  "slots": (4,2,0,0)},
			9:  {"cantrips": 2, "spells": 6,  "slots": (4,2,0,0)},
			10: {"cantrips": 3, "spells": 7,  "slots": (4,3,0,0)},
			11: {"cantrips": 3, "spells": 8,  "slots": (4,3,0,0)},
			12: {"cantrips": 3, "spells": 8,  "slots": (4,3,0,0)},
			13: {"cantrips": 3, "spells": 9,  "slots": (4,3,2,0)},
			14: {"cantrips": 3, "spells":10,  "slots": (4,3,2,0)},
			15: {"cantrips": 3, "spells":10,  "slots": (4,3,2,0)},
			16: {"cantrips": 3, "spells":11,  "slots": (4,3,3,0)},
			17: {"cantrips": 3, "spells":11,  "slots": (4,3,3,0)},
			18: {"cantrips": 3, "spells":11,  "slots": (4,3,3,0)},
			19: {"cantrips": 3, "spells":12,  "slots": (4,3,3,1)},
			20: {"cantrips": 3, "spells":13,  "slots": (4,3,3,1)}
			}
		lvl = caster.level
		if lvl > 20: lvl = 20
		value = table.get(lvl, {"cantrips": 0, "spells": 0, "slots": (0,0,0,0)})
		if key == "cantrips":
			return value["cantrips"]
		if key == "spells":
			return value["spells"]
		if key == "slots":
			return {i + 1: val for i, val in enumerate(value["slots"])}

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def available_spells(caster):
		"""Return all spells this character can *learn* at their current level."""
		table = (SPELL_LISTS.get(caster.character.subclass)
				or SPELL_LISTS.get(caster.character.char_class, {}))
		# Collapse all spell levels the character has unlocked
		unlocked = [lvl for lvl in table if lvl <= caster.level]
		spells = [s for lvl in unlocked for s in table[lvl]]
		for lvl in unlocked:
			spells.extend(table[lvl])
		return spells

	def prepare_spells(caster):
		random.seed(self.character.seed)
		cantrip_pool = [s for s in caster.spells_available if int(s.level) == 0]
		leveled_pool = [s for s in caster.spells_available if int(s.level) > 0]

		caster.spells_known = random.sample(cantrip_pool, min(len(cantrip_pool), caster.get_stats("cantrips")))

		slots = caster.get_stats("slots")
		weights = {lvl: slots.get(lvl, 0) for lvl in range(1, 10)}
		leveled_pool = list({s.name: s for s in leveled_pool}.values())
		leveled_weighted = [(s, weights.get(int(s.level), 0)) for s in leveled_pool if weights.get(int(s.level), 0) > 0]

		spells, spell_weights = zip(*leveled_weighted) if leveled_weighted else ([], [])

		chosen = random.choices(spells, weights=spell_weights, k=min(len(spells), caster.get_stats("spells")))
		unique_chosen = []
		seen = set()
		for s in chosen:
			if s.name not in seen:
				unique_chosen.append(s)
				seen.add(s.name)
		caster.spells_known += unique_chosen[:caster.get_stats("spells")]


	def modifier(caster):
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def html(caster):
		return str(caster)

	def __str__(caster):
		ordered_spells = sorted(caster.spells_known, key=lambda s: int(s.level))
		spells_names = "".join(f"<li>〖{spell.level}〗{spell.name}</li>" for spell in ordered_spells)
		spells_html = "".join(f"""<div class="npc-textbox">{spell}</div>""" for spell in ordered_spells)
		slots_html = "<br>".join(f"<b>Level {lvl}</b>: <i>{num}</i> " for lvl, num in caster.spell_slots.items())
		return f"""
			<div class="npc-textbox" style="grid-column: span 1;">
			<h1 style="font-family: 'Iglesia'; font-size:	3.1em; ">{caster.character.subclass} Spellcasting</h1>
			<p> Eldritch Knights combine the martial mastery common to all Fighters with a careful study of magic. Their spells both complement and extend their combat skills.<br> You have learned to cast spells. </p>
			<h2>Spell Slots:</h2> {slots_html} <br>  You regain all expended slots when you finish a Long Rest.</p>
			<ul style="list-style-type: '♟️'; text-align: left; font-family: 'Iglesia' ">{spells_names}</ul>
			<h2>Arcane Focus</h2>
			You can use an Arcane Focus (such as a wand or scepter),  as a Spellcasting Focus for your Wizard spells.
			</div>
			{spells_html}
			"""


# Warlock spellcasting progression for 2024 PHB
WARLOCK_SPELLCASTING_TABLE = {
		1:  {"cantrips": 2, "prepared": 2,  "slots": (2,),   "slot_level": 1},
		2:  {"cantrips": 2, "prepared": 3,  "slots": (2,),   "slot_level": 1},
		3:  {"cantrips": 2, "prepared": 4,  "slots": (2,),   "slot_level": 2},
		4:  {"cantrips": 3, "prepared": 5,  "slots": (2,),   "slot_level": 2},
		5:  {"cantrips": 3, "prepared": 6,  "slots": (2,),   "slot_level": 3},
		6:  {"cantrips": 3, "prepared": 7,  "slots": (2,),   "slot_level": 3},
		7:  {"cantrips": 3, "prepared": 8,  "slots": (2,),   "slot_level": 4},
		8:  {"cantrips": 3, "prepared": 9,  "slots": (2,),   "slot_level": 4},
		9:  {"cantrips": 3, "prepared": 10, "slots": (2,),   "slot_level": 5},
		10: {"cantrips": 4, "prepared": 10, "slots": (2,),   "slot_level": 5},
		11: {"cantrips": 4, "prepared": 11, "slots": (3,),   "slot_level": 5},
		12: {"cantrips": 4, "prepared": 11, "slots": (3,),   "slot_level": 5},
		13: {"cantrips": 4, "prepared": 12, "slots": (3,),   "slot_level": 5},
		14: {"cantrips": 4, "prepared": 12, "slots": (3,),   "slot_level": 5},
		15: {"cantrips": 4, "prepared": 13, "slots": (3,),   "slot_level": 5},
		16: {"cantrips": 4, "prepared": 13, "slots": (3,),   "slot_level": 5},
		17: {"cantrips": 4, "prepared": 14, "slots": (4,),   "slot_level": 5},
		18: {"cantrips": 4, "prepared": 14, "slots": (4,),   "slot_level": 5},
		19: {"cantrips": 4, "prepared": 15, "slots": (4,),   "slot_level": 5},
		20: {"cantrips": 4, "prepared": 15, "slots": (4,),   "slot_level": 5},
		}

class Warlock(Spellcaster):
	def __init__(caster, character,known=None):
		if known is None: 	known = []
		caster.class_name 	= "Warlock"
		caster.character 	= character
		caster.level 		= character.level
		caster.spell_slots 	= caster.get_spell_slots()
		caster.spells_available = caster.available_spells()
		caster.spells_known = known
		caster.casting_stat = caster.get_casting_stat()
		caster.prepare_spells()
		# Optionally track invocations, pact, arcanum

	def get_casting_stat(caster):
		return "CHA"

	def get_stats(caster, key):
		lvl = min(caster.level, 20)
		value = WARLOCK_SPELLCASTING_TABLE.get(lvl, WARLOCK_SPELLCASTING_TABLE[20])
		if key == "cantrips":
			return value["cantrips"]
		if key == "prepared":
			return value["prepared"]
		if key == "slots":
			# Unlike wizards, Warlocks only ever have one slot level at a time
			return {value["slot_level"]: value["slots"][0]}
		if key == "slot_level":
			return value["slot_level"]

	def get_spell_slots(caster):
		return caster.get_stats("slots")

	def available_spells(caster):
		"""Returns all spells this character can *prepare* at their current level."""
		table = SPELL_LISTS.get(caster.character.char_class, {})
		max_slot = caster.get_stats("slot_level")
		# Only show spells up to max_slot (warlock can never prepare 6+)
		unlocked = [lvl for lvl in table if lvl <= max_slot]
		spells = [s for lvl in unlocked for s in table[lvl]]
		return spells

	def prepare_spells(caster):
		random.seed(self.character.seed)
		n = caster.get_stats("prepared")
		# Warlocks can change prepared spells on level-up/long rest
		available = caster.available_spells()
		# Random for demo; in-app, let user select!
		caster.spells_known = random.sample(available, min(n, len(available)))

		# Always include cantrips
		cantrip_pool = [s for s in available if int(s.level) == 0]
		cantrips = random.sample(cantrip_pool, min(len(cantrip_pool), caster.get_stats("cantrips")))
		caster.spells_known = cantrips + [s for s in caster.spells_known if int(s.level) > 0]

		# If you want to display Mystic Arcanum, add a step here!

	def modifier(caster):
		# CHA-based, so use character abilities
		return (getattr(caster.character.AS, caster.casting_stat) - 10) // 2

	def __str__(caster):
		# Sort cantrips and leveled spells
		cantrips = [s for s in caster.spells_known if int(s.level) == 0]
		leveled = [s for s in caster.spells_known if int(s.level) > 0]
		n_prep = caster.get_stats("prepared")
		# For clarity, highlight which are "prepared" (all, for warlock; cantrips always ready)
		spell_list = ""
		for spell in cantrips:
			spell_list += f"<li>【{spell.level}】{spell.name}</li>"
		for spell in leveled:
			spell_list += f"<li>【{spell.level}】{spell.name}</li>"
		# Pact magic slot display: only one slot level at a time, but up to 2–4 slots!
		slots = caster.get_stats("slots")
		slot_level = caster.get_stats("slot_level")
		slot_str = f"<b>{len(slots)} × Level {slot_level} Spell Slot(s)</b>"
		# Mystic Arcanum: optionally list
		arcanum = ""
		if caster.level >= 11:
			arcanum += f"<p><b>Mystic Arcanum:</b> Choose {', '.join(str(x) for x in (6,7,8,9) if caster.level >= {11:6,13:7,15:8,17:9}[x])}th-level Warlock spells (cast 1/LR, not with slots).</p>"
		return f"""
		<div class="npc-textbox" style="grid-column: span 3;">
			<h1 style="font-family: 'Iglesia'; font-size: 3.1em;">Warlock Pact Magic</h1>
			<p>As a warlock, your pact grants you spellcasting drawn from a supernatural patron. Pact Magic uses <b>Charisma</b> and works differently from other spellcasters.</p>
		</div>
		<div class="npc-textbox" style="grid-column: span 1;">
			<h2>Pact Magic Slots:</h2>
			{slot_str}
			<br><i>All slots are cast at highest slot level.<br>
			You regain all slots on a Short or Long Rest.</i>
		</div>
		<div class="npc-textbox" style="grid-column: span 1;">
			<h3>Prepared Spells</h3>
			You prepare {n_prep} warlock spells at the end of each long rest. Each must be of a level you can cast.<br>
			<ul style="list-style-type: '🔮'; text-align: left; font-family: 'Iglesia'">
				{spell_list}
			</ul>
			<h3>Cantrips</h3>
			You always know {caster.get_stats("cantrips")} cantrips from the warlock list.<br>
		</div>
		{arcanum}
		"""


# Factory to get the appropriate class
def spellcaster(character):
	if "Wizard" in character:
		return Wizard(character)
	if "Sorcerer" in character:
		return Sorcerer(character)
	if "Monk" in character:
		return Monk(character)
	if "Warlock" in character:
		return Warlock(character)
	if "Eldritch Knight" in character:
		return EldritchKnight(character)
	# Add further subclasses or specific cases as needed
	return None
