import app.random as random
from AtlasLudus.Map_of_Dice import Dice
from AtlasActorLudi.Map_of_Scores import PB, Modifier
#from AtlasInventarium.Map_of_Weapons import Weapons

def setObjects(char):
	""" Equip character with items based on skills and proficiencies. """
	from AtlasInventarium.Grimoire_of_Objects import Object
	import AtlasInventarium.Grimoire_of_Objects as objects

	# Budget is rolled ONCE, by GenerateEquipment. This pass spends what is left.

	tool_proficiencies = {
		'Musical Instrument': 'Charisma',
		"Alchemist's Supplies": 'Intelligence',
		"Brewer's Supplies": 'Intelligence',
		"Calligrapher's Supplies": 'Dexterity',
		"Carpenter's Tools": 'Strength',
		"Cartographer's Tools": 'Wisdom',
		"Cobbler's Tools": 'Dexterity',
		"Cook's Utensils": 'Wisdom',
		"Glassblower's Tools": 'Intelligence',
		"Jeweler's Tools": 'Intelligence',
		"Leatherworker's Tools": 'Dexterity',
		"Mason's Tools": 'Strength',
		"Painter's Supplies": 'Wisdom',
		"Potter's Tools": 'Intelligence',
		"Smith's Tools": 'Strength',
		"Tinker's Tools": 'Dexterity',
		"Weaver's Tools": 'Dexterity',
		"Woodcarver's Tools": 'Dexterity',
		"Navigator's Tools": 'Wisdom',
		"Herbalism Kit": 'Intelligence',
		"Gaming Set": 'Wisdom',
		"Forgery Kit": 'Dexterity',
		"Disguise Kit": 'Charisma',
		"Thieves' Tools": 'Dexterity',
		}

	if char.skills.Musical_Instrument.is_proficient():
		musical_Instrument = objects.Object(
			name = "Musical Instrument",
			value=20, weight=3,
			description = "Ability: Charisma")
		char.equipment.buy_item(musical_Instrument)

	if char.skills.Alchemist_Supplies.is_proficient():
		alchemist_supplies = objects.Object(
			name = "Alchemist's Supplies",
			value=50, weight=8,
			description = "Ability: Intelligence")
		char.equipment.buy_item(alchemist_supplies)

	if char.skills.Brewer_Supplies.is_proficient():
		brewer_supplies = objects.Object(
			name = "Brewer's Supplies",
			value=20, weight=9,
			description = "Ability: Intelligence")
		char.equipment.buy_item(brewer_supplies)

	if char.skills.Calligrapher_Supplies.is_proficient():
		calligrapher_supplies = objects.Object(
			name = "Calligrapher's Supplies",
			value=10, weight=5,
			description = "Ability: Dexterity")
		char.equipment.buy_item(calligrapher_supplies)

	if char.skills.Carpenter_Tools.is_proficient():
		carpenter_Tools = objects.Object(
			name = "Carpenter's Tools",
			value=20, weight=9,
			description = "Ability: Strength")
		char.equipment.buy_item(carpenter_Tools)

	if char.skills.Cartographer_Tools.is_proficient():
		cartographer_Tools = objects.Object(
			name = "Cartographer's Tools",
			value=15, weight=6,
			description = "Ability: Wisdom")
		char.equipment.buy_item(cartographer_Tools)

	if char.skills.Cobbler_Tools.is_proficient():
		cobbler_Tools = objects.Object(
			name = "Cobbler's Tools",
			value=5, weight=5,
			description = "Ability: Dexterity")
		char.equipment.buy_item(cobbler_Tools)

	if char.skills.Cook_Utensils.is_proficient():
		cook_Utensils = objects.Object(
			name = "Cook's Utensils",
			value=1, weight=8,
			description = "Ability: Wisdom")
		char.equipment.buy_item(cook_Utensils)

	if char.skills.Glassblower_Tools.is_proficient():
		glassblower_Tools = objects.Object(
			name = "Glassblower's Tools",
			value=30, weight=5,
			description = "Ability: Intelligence")
		char.equipment.buy_item(glassblower_Tools)

	if char.skills.Jeweler_Tools.is_proficient():
		jeweler_Tools = objects.Object(
			name = "Jeweler's Tools",
			value=25, weight=2,
			description = "Ability: Intelligence")
		char.equipment.buy_item(jeweler_Tools)

	if char.skills.Leatherworker_Tools.is_proficient():
		leatherworker_Tools = objects.Object(
			name = "Leatherworker's Tools",
			value=5, weight=5,
			description = "Ability: Dexterity")
		char.equipment.buy_item(leatherworker_Tools)

	if char.skills.Mason_Tools.is_proficient():
		mason_Tools = objects.Object(
			name = "Mason's Tools",
			value=10, weight=8,
			description = "Ability: Strength")
		char.equipment.buy_item(mason_Tools)

	if char.skills.Painter_Supplies.is_proficient():
		painter_Supplies = objects.Object(
			name = "Painter's Supplies",
			value=10, weight=5,
			description = "Ability: Wisdom")
		char.equipment.buy_item(painter_Supplies)

	if char.skills.Potter_Tools.is_proficient():
		potter_Tools = objects.Object(
			name = "Potter's Tools",
			value=10, weight=3,
			description = "Ability: Intelligence")
		char.equipment.buy_item(potter_Tools)

	if char.skills.Smith_Tools.is_proficient():
		smith_Tools = objects.Object(
			name = "Smith's Tools",
			value=20, weight=8,
			description = "Ability: Strength")
		char.equipment.buy_item(smith_Tools)

	if char.skills.Tinker_Tools.is_proficient():
		tinker_Tools = objects.Object(
			name = "Tinker's Tools",
			value=50, weight=10,
			description = "Ability: Dexterity")
		char.equipment.buy_item(tinker_Tools)

	if char.skills.Weaver_Tools.is_proficient():
		weaver_Tools = objects.Object(
			name = "Weaver's Tools",
			value=1, weight=5,
			description = "Ability: Dexterity")
		char.equipment.buy_item(weaver_Tools)

	if char.skills.Woodcarver_Tools.is_proficient():
		woodcarver_Tools = objects.Object(
			name = "Woodcarver's Tools",
			value=1, weight=5,
			description = "Ability: Dexterity")
		char.equipment.buy_item(woodcarver_Tools)

	if char.skills.Navigator_Tools.is_proficient():
		navigator_Tools = objects.Object(
			name = "Navigator's Tools",
			value=25, weight=2,
			description = "Ability: Wisdom")
		char.equipment.buy_item(navigator_Tools)

	if char.skills.Herbalism_Kit.is_proficient():
		herbalism_Kit = objects.Object(
			name = "Herbalism Kit",
				value=5, weight=3,
				description = "Ability: Intelligence")
		char.equipment.buy_item(herbalism_Kit)

	if char.skills.Gaming_Set.is_proficient():
		gaming_Set = objects.Object(
			name = "Gaming Set",
				value=1, weight=0,
				description = "Ability: Wisdom")
		char.equipment.buy_item(gaming_Set)

	if char.skills.Forgery_Kit.is_proficient():
		forgery_Kit = objects.Object(
			name = "Forgery Kit",
				value=15, weight=5,
				description = "Ability: Dexterity")
		char.equipment.buy_item(forgery_Kit)

	if char.skills.Disguise_Kit.is_proficient():
		disguise_Kit = objects.Object(
			name = "Disguise Kit",
				value=25, weight=3,
				description = "Ability: Charisma")
		char.equipment.buy_item(disguise_Kit)

	if char.skills.Thieves_Tools.is_proficient():
		thieves_Tools = objects.Object(
			name = "Thieves' Tools",
				value=25, weight=1,
				description = "Ability: Dexterity")
		char.equipment.buy_item(thieves_Tools)

	# A worn shield keeps contributing when body armor is upgraded — comparing
	# bare armor against a shield-inclusive AC used to silently drop the +2.
	shield_bonus = 2 if char.equipment.is_wearing_shield() else 0

	if char.skills.Heavy.is_proficient():
		armor = char.equipment.HeavyArmor()
		AC_candidate = armor.armor_class + shield_bonus
		if AC_candidate > char.AC and char.equipment.equip_defense(armor):
			char.AC = AC_candidate

	if char.skills.Medium.is_proficient():
		armor = char.equipment.MediumArmor(Modifier(char.abilities.DEX))
		AC_candidate = armor.armor_class + shield_bonus
		if AC_candidate > char.AC and char.equipment.equip_defense(armor):
			char.AC = AC_candidate

	if char.skills.Light.is_proficient():
		armor = char.equipment.LightArmor(Modifier(char.abilities.DEX))
		AC_candidate = armor.armor_class + shield_bonus
		if AC_candidate > char.AC and char.equipment.equip_defense(armor):
			char.AC = AC_candidate

	set_Armor(char)

def GenerateEquipment(char):
	"""
	Equips a character with armor, weapons, and gear based on class, background, and proficiencies.
	Spends available budget wisely.
	"""
	#equip = char.equipment
	#skills = char.skills
	abilities = char.abilities

	# Step 1: Calculate budget based on class, background, and level
	char.equipment.calculate_budget(char.char_class, char.background, char.level)

	# Step 2: Equip armor intelligently
	set_Armor(char)


	if char.skills.Martial_Weapons.is_proficient():
		weapon =  char.equipment.Melee_Martial(Modifier(abilities.DEX), Modifier(abilities.STR))
	else:
		weapon =  char.equipment.Melee(Modifier(abilities.DEX), Modifier(abilities.STR))

	# The weapon factories already charged the purse; equip straight into the
	# slots the sheet renders (right hand doubles as the melee slot).
	char.equipment.equip_item(weapon, slot="right")
	char.equipment.melee = weapon

	# Step 3: Distance weapon — its own slot, so it never displaces a shield.
	if char.skills.Martial_Weapons.is_proficient():
		ranged_weapon = char.equipment.Ranged_Martial(
			Modifier(abilities.DEX), Modifier(abilities.STR))
	else:
		ranged_weapon = char.equipment.Ranged(
			Modifier(abilities.DEX), Modifier(abilities.STR))

	char.equipment.equip_item(ranged_weapon, slot="ranged")

	# Step 4: Shield (if proficient and a hand is free) — set_Armor owns the AC.
	if (
			char.skills.Shields.is_proficient()
			and not char.equipment.is_wearing_shield()
			and char.equipment.left is None
			):
		shield = Object(name="Shield", value=10, weight=6, description="+2 AC shield")
		if char.equipment.buy_item(shield):
			char.equipment.equip_item(shield, slot="left")
			char.AC += 2

	# Step 7: Optional - Add a few magic items if high-level character (level >=5)
	if char.level >= 5 and char.equipment.purse >= 100:
		magic_items = [
			Object("Potion of Healing", 50, 0.5, description="Restores 2d4+2 HP"),
			Object("Scroll of Fireball", 100, 0.2, description="Cast Fireball once"),
			Object("Cloak of Protection", 200, 1, description="+1 AC and saving throws"),
			]
		for item in magic_items:
			if char.equipment.purse >= item.value:
				char.equipment.buy_item(item)

	# Step 5: Starter tools and survival items
	tools = [
		Object("Backpack", 2, 5, description="Standard adventurer's pack"),
		Object("Rations", 1, 2, quantity=5, description="Dry food"),
		Object("Rope", 1, 1, description="50ft hempen rope"),
		Object("Torch", 0.1, 1, quantity=3, description="Standard torch"),
		Object("Waterskin", 2, 2, description="Filled with water"),
		]
	# Buy each survival item at most once (Rope and Torch used to be bought
	# twice, from two independent blocks, with different weights).
	random.shuffle(tools)
	for item in tools:
		if not char.equipment.has_item(item.name):
			char.equipment.buy_item(item)
	return

def set_Armor(char):
	""" Equip the best available armor based on AC and proficiencies. """
	best_armor_class = char.AC

	if char.skills.Unarmed_Monk.is_proficient():
		AC_candidate = 10 + Modifier(char.abilities.DEX) + Modifier(char.abilities.WIS)
		if AC_candidate > char.AC:
			armor = char.equipment.Clothes(Modifier(char.abilities.DEX))
			char.equipment.equip_defense(armor)
			char.AC = AC_candidate

	if char.skills.Unarmed_Barb.is_proficient():
		AC_candidate = 10 + Modifier(char.abilities.DEX) + Modifier(char.abilities.CON)
		if AC_candidate > char.AC:
			armor = char.equipment.Clothes(Modifier(char.abilities.DEX))
			char.equipment.equip_defense(armor)
			char.AC = AC_candidate

	dance = getattr(
			char.skills,
			"Unarmed_Dance",
			None,
			)
	if dance is not None and dance.is_proficient():
		AC_candidate = 10 + Modifier(char.abilities.DEX) + Modifier(char.abilities.CHA)
		if AC_candidate > char.AC:
			armor = char.equipment.Clothes(Modifier(char.abilities.DEX))
			char.equipment.equip_defense(armor)
			char.AC = AC_candidate

	if not char.equipment.defense:
		armor = char.equipment.Clothes(Modifier(char.abilities.DEX))
		char.equipment.equip_defense(armor)
		# The sheet must agree with the item actually worn.
		if armor.armor_class > char.AC:
			char.AC = armor.armor_class

	# A shield is worn once: +2 only when one is newly strapped on, and only
	# when a hand is free (set_Armor runs in both equipping passes).
	if (
			char.skills.Shields.is_proficient()
			and not char.equipment.is_wearing_shield()
			and char.equipment.left is None
			):
		char.equipment.equip_left(Object(
			name = "Shield",
			value = 10,
			weight = 6,
			description = "+2 AC"))
		char.AC += 2

class Object:
	def __init__(object, name="", value=0, weight=0,  quantity=1, rarity="Common", description=""):
		"""
		Initialize an Object with basic attributes.

		Parameters:
		- name: The name of the object.
		- weight: The weight of the object in pounds.
		- value: The value of the object in gold pieces.
		- quantity: How many of this object the character owns.
		- rarity: How rare the object is (Common, Uncommon, Rare, etc.).
		"""
		object.name = name
		object.weight = weight
		object.value = value
		object.quantity = quantity
		object.rarity = rarity
		object.description = description

	@property
	def total_value(object):
		"""Calculate the total value based on quantity."""
		return object.value

	@property
	def unitary_value(object):
		"""Calculate the unitary value based on quantity."""
		return object.value if object.quantity == 0 else object.value / object.quantity

	def __str__(object):
		"""Sheet entry. Without this a Shield rendered as its debug repr."""
		from AtlasScriptum.Map_of_Formats import Entry
		return Entry(
				object.name,
				object.description or "",
				)

	def __repr__(object):
		"""String representation of the Object."""
		return (f"{object.name} (Weight: {object.weight} lbs, "
				f"Value: {object.value} gp, Quantity: {object.quantity}, Rarity: {object.rarity})")

class Armor(Object):
	def __init__(armor,
		name,
		weight=0,
		value=0,
		quantity=1,
		rarity="Common",
		armor_class=0,
		dex_bonus=0,
		description="",
		armor_type = "Light"):
		"""
		Initialize an armor object

		Parameters:
		- armor_class: The armor class (AC) for armor.
		"""
		super().__init__(name, value, weight, quantity, rarity, description)
		# Keep the parts, not just the sum. "Clothes, AC 15" reads as though
		# the garment were armour; "10 + 5 Dex" says where the number came
		# from — the same courtesy a weapon does with "1d8 + 3".
		armor.base_class = armor_class
		if armor_type == "Light":
			armor.dex_applied = dex_bonus
		elif armor_type == "Medium":
			armor.dex_applied = min(dex_bonus, 2)
		else:
			armor.dex_applied = 0
		armor.armor_class = armor.base_class + armor.dex_applied
		armor.armor_type = armor_type

	def __str__(armor):
		"""Sheet entry — armour speaks its class and kind, not its debug repr."""
		from AtlasScriptum.Map_of_Formats import Entry
		if armor.dex_applied:
			result = (
				f"AC {armor.armor_class} "
				f"({armor.base_class} + {armor.dex_applied} Dex)"
				)
		else:
			result = f"AC {armor.armor_class}"
		if armor.armor_type:
			result += f", {armor.armor_type} armor"
		if armor.description and armor.description != armor.name:
			result += f". {armor.description}"
		return Entry(armor.name, result + ".")

	def __repr__(armor):
		"""String representation of Equipment."""
		base = super().__repr__()
		extra = ""
		if armor.armor_class:
			extra += f", AC: {armor.armor_class}"
		extra += f", Armor Type: {armor.armor_type}"
		return base + extra

class Weapon(Object):
	def __init__(weapon,
			name,
			weight=0,
			value=0,
			quantity=1,
			rarity="Common",
			armor_class=None,
			range_distance="",
			N = 1, D=6,
			Mod=0,
			dmg = "Bludgeoning",
			weapon_type = "Light",
			mastery = "",
			properties="",
			description=""):
			"""
			Initialize an weapon object

			Parameters:
			- damage: The nDd Damage of the weapon.
			"""
			super().__init__(name, value, weight, quantity, rarity, description)
			weapon.damage_intensity = N
			weapon.damage_dice =  D
			weapon.attack = f"1D20 + {Mod}"
			weapon.mastery = mastery
			weapon.attack_modifier = 	Mod
			weapon.range_distance = 	range_distance

			# The catalogue carries the real damage type as the first
			# sentence of `weapon_type` and never passes `dmg`, so the
			# default silently made every weapon Bludgeoning — a Spear read
			# "1D6+4 Bludgeoning, Piercing.". Take the type from there when
			# it is one, and drop it from the properties so it prints once.
			DAMAGE_WORDS = (
					"Bludgeoning",
					"Piercing",
					"Slashing",
					)
			parts = [
					piece.strip().rstrip(".")
					for piece in str(weapon_type).split(".")
					if piece and piece.strip()
					]
			if parts and parts[0] in DAMAGE_WORDS:
				weapon.damage_type = parts[0]
				parts = parts[1:]
			else:
				weapon.damage_type = dmg

			weapon.damage = f"{N}D{D} + {Mod}  ({weapon.damage_type})"
			# Join with sentence breaks. Raw concatenation ran the parts
			# together on the sheet ("Bludgeoning.ToppleVersatile (1d8)").
			weapon.properties = ". ".join(
					str(part).strip().rstrip(".")
					for part in (*parts, mastery, properties, description)
					if part and str(part).strip()
					)

	def __str__(wpn):
			from AtlasScriptum.Map_of_Formats import Entry
			result = f"{wpn.damage_intensity}D{wpn.damage_dice}"
			if wpn.attack_modifier:
				result += f"{wpn.attack_modifier:+}"
			result += f" {wpn.damage_type}"
			if wpn.range_distance:
					result += f", {wpn.range_distance}"
			if wpn.properties:
					result += f", {wpn.properties}."
			else:
					result += "."
			return Entry(wpn.name, result)

	def __repr__(weapon):
			"""String representation of Equipment."""
			base = super().__repr__()
			extra = ""
			if weapon.damage:
				extra += f"To Hit: {weapon.attack} , Damage: {weapon.damage}"
			return base + extra

	@property
	def weapon_type(wpn):
			return str(wpn)

class Inventory:
	def __init__(inventory):
		"""Inventory to manage equipped items, bag, and coins."""
		inventory.equipped = []	# List of equipped items (weapons, armor, etc.)
		inventory.bag = 	[]	# List of unequipped items
		inventory.purse = 	0	 # Purse with gold coins (floored to copper)

		# Equipped item slots
		inventory.defense = None
		inventory.melee = 	None
		inventory.ranged = 	None
		inventory.right = 	None
		inventory.left = 	None

	@property
	def purse(self):
		"""Coins on hand, always a clean copper-piece figure."""
		return self._purse

	@purse.setter
	def purse(self, value):
		# Floor to the copper piece (1/100 gold) at every mutation site, so
		# float crumbs can never surface as "38.70000000000002 gp". Always
		# down: a merchant does not round in the customer's favour. The
		# epsilon stops a bare floor() destroying a copper on values like
		# 0.29, whose binary form is 28.999999999999996 hundredths.
		import math
		self._purse = math.floor(float(value) * 100 + 1e-6) / 100

	def add_item_to_bag(self, item):
		"""Adds an item to the bag."""
		self.bag.append(item)

	def add(self, item):
		"""Adds an item to the bag."""
		self.bag.append(item)

	def buy_item(self, item):
		"""Adds an item to the bag. Returns True when the purchase happened."""
		if self.purse >= item.value:
			self.add_item_to_bag(item)
			self.purse -= item.value
			return True
		return False

	def get_worn_armor(self):
		"""The Armor currently in the defense slot, if any."""
		return self.defense

	def is_wearing_shield(self):
		"""True when a Shield occupies a hand slot."""
		for slot in (self.left, self.right):
			if slot is not None and getattr(slot, "name", "") == "Shield":
				return True
		return False

	def has_item(self, name):
		"""True when an item of this name is already carried or equipped."""
		for item in self.bag:
			if getattr(item, "name", "") == name:
				return True
		for slot in (self.defense, self.melee, self.ranged, self.right, self.left):
			if slot is not None and getattr(slot, "name", "") == name:
				return True
		return False


	def equip_item(self, item, slot=None):
		"""Equips an item and moves it from the bag to an equipped slot."""
		if item in self.bag:
			self.bag.remove(item)
		try:
			if slot == "right":
				self.right = item
			elif slot == "left":
				self.left = item
			elif slot == "defense":
				self.defense = item
			elif slot == "melee":
				self.melee = item
			elif slot == "ranged":
				self.ranged = item
		except:
			if item in self.bag:
				self.bag.remove(item)
		self.equipped.append(item)

	def equip_ranged(self, item):
		if item in self.bag:
			self.bag.remove(item)
		self.ranged = item
		self.equipped.append(item)  # Optional, if you want it tracked in equipped as well.

	def equip_left(self, item):
		"""Equips an item and moves it from the bag to left hand."""
		if item in self.bag:
			self.bag.remove(item)
			self.left = item
		else:
			if item.value < self.purse:
				if self.left:
					self.purse += self.left.value
				self.left = item
				self.purse -= item.value


	def equip_right(self, item):
		"""Equips an item and moves it from the bag to equipped items."""
		if item in self.bag:
			self.bag.remove(item)
			self.right = item
		else:
			if item.value < self.purse:
				if self.right:
					self.purse += self.right.value
				self.right = item
				self.purse -= item.value

	def equip_defense(self, item):
		"""Equip armor, buying it when it is not already carried.

		Returns True when the armor ends up worn — callers must not raise AC
		for armor the character could not afford.
		"""
		if item in self.bag:
			self.bag.remove(item)
			self.defense = item
			return True

		if item.value <= self.purse:
			if self.defense:
				self.purse += self.defense.value
			self.defense = item
			self.purse -= item.value
			return True

		return False

	def unequip_item(self, item):
		"""Unequips an item and moves it to the bag."""
		if item in self.equipped:
			self.equipped.remove(item)
			self.bag.append(item)
		else:
			print(f"{item} is not equipped.")

	def __repr__(self):
		"""Display the equipped items, bag contents, and purse."""
		return (f"Equipped Items: {[str(item) for item in self.equipped]}\n"
				f"Total Weight: {self.calculate_total_weight()} lbs")

	def calculate_budget(self, char_class, backg, lvl):
		"""Calculates the total budget based on gold coins in the purse."""
		base = 0
		if char_class == 'Fighter':
			base += Dice(N = 50, D=4)
		elif char_class =='Wizard':
			base += Dice(N = 40, D=4)
		elif char_class == 'Rogue':
			base += Dice(N = 40, D=4)
		elif char_class =='Cleric':
			base += Dice(N = 50, D=4)
		elif char_class =='Ranger':
			base += Dice(N = 50, D=4)
		elif char_class =='Paladin':
			base += Dice(N = 50, D=4)
		elif char_class =='Bard':
			base += Dice(N = 50, D=4)
		elif char_class =='Monk':
			base += Dice(N = 20, D=4)
		elif char_class =='Druid':
			base += Dice(N = 20, D=4)
		elif char_class =='Warlock':
			base += Dice(N = 40, D=4)
		elif char_class =='Sorcerer':
			base += Dice(N = 30, D=4)
		elif char_class =='Barbarian':
			base += Dice(N = 20, D=4)
		if lvl > 1:
			base += Dice(N = lvl - 1, D=40)
		if backg == 'Acolyte':
			base += Dice(10,5)
		elif backg =='Artisan':
			base += Dice(10,10)
		elif backg =='Charlatan':
			base += Dice(10,7)
		elif backg =='Criminal':
			base += Dice(10,7)
		elif backg =='Entertainer':
			base += Dice(10,10)
		elif backg =='Farmer':
			base += Dice(10,5)
		elif backg =='Guard':
			base += Dice(10,7)
		elif backg =='Guide':
			base += Dice(10,7)
		elif backg =='Hermit':
			base += Dice(10,3)
		elif backg =='Merchant':
			base += Dice(10,15)
		elif backg =='Noble':
			base += Dice(10,20)
		elif backg =='Sage':
			base += Dice(10,6)
		elif backg =='Sailor':
			base += Dice(10,8)
		elif backg =='Scribe':
			base += Dice(10,7)
		elif backg =='Soldier':
			base += Dice(10,10)
		elif backg =='Wayfarer':
			base += Dice(10,7)
		else:
			base += Dice(10,5)

		self.purse = base

	def Clothes(self, dex_mod=0):
		"""No-armor garments (base AC 10 + DEX)."""
		from AtlasInventarium.Grimoire_of_Objects import Armor
		return Armor(
			name="Clothes",
			armor_class=10,
			dex_bonus=dex_mod,
			armor_type="Light",
			weight=0,
			value=0,
			description="Simple garments")

	def LightArmor(self, dex_mod=0):
		from AtlasInventarium.Grimoire_of_Objects import Armor
		return Armor(
			name="Leather Armor",
			armor_class=11,
			dex_bonus=dex_mod,
			armor_type="Light",
			weight=10,
			value=10,
			description="Leather armor")

	def MediumArmor(self, dex_mod=0):
		from AtlasInventarium.Grimoire_of_Objects import Armor
		return Armor(
			name="Scale Mail",
			armor_class=14,
			dex_bonus=dex_mod,
			armor_type="Medium",
			weight=45,
			value=50,
			description="Scale mail")

	def HeavyArmor(self):
		from AtlasInventarium.Grimoire_of_Objects import Armor
		return Armor(
			name="Chain Mail",
			armor_class=16,
			armor_type="Heavy",
			weight=55,
			value=75,
			description="Chain mail")

	def Ranged(self, DEX_mod, STR_mod):
		Dart = Weapon(
			name = "Darts", weight=5, value=1, quantity=20,
			rarity="Common",
			Mod= max(DEX_mod,STR_mod),
			N = 1, D=4,
			description="",
			mastery = "Vex",
			weapon_type = "Piercing. 20/60 thrown range. Light. Finesse.")

		Dagger = Weapon(
			name = "Daggers",
			weight=5, value=10, quantity=5,
			rarity="Common",
			Mod= max(DEX_mod,STR_mod),
			N = 1, D=4,
			description="",
			mastery = "Nick",
			weapon_type = "Piercing. 20/60 thrown range. Light. Finesse.")

		Javelin = Weapon(
			name = "Javelins", weight=8, value=2, quantity=4,
			rarity="Common",
			Mod= STR_mod,
			N = 1, D=6,
			description="",
			mastery = "Slow",
			weapon_type = "Piercing. 30/120 thrown range.")

		Light_hammer = Weapon(
			name = "Light Hammers",
			weight = 8,
			value = 8,
			quantity = 4,
			rarity = "Common",
			Mod= STR_mod,
			N = 1, D=4,
			description="",
			mastery = "Nick",
			weapon_type = "Bludgeoning. 20/60 thrown range. Light.")
		Handaxe = Weapon(
			name = "Handaxes",
			weight = 8,
			value = 20,
			quantity = 4,
			rarity="Common",
			Mod= STR_mod,
			N = 1, D=6,
			description="",
			mastery = "Vex",
			weapon_type = "Slashing. 20/60 thrown range. Light.")
		Spear = Weapon(
			name = "Spear",
			value = 1,
			weight = 3,
			quantity = 1,
			rarity="Common",
			Mod= STR_mod,
			N = 1, D=6,
			description="",
			mastery = "Sap",
			weapon_type = "Piercing. 20/60 thrown range. Versatile(1d8).")

		Crossbow_light = Weapon(
			name = "Light Crossbow",
			N = 1, D=8,
			weight = 5,
			quantity = 1,
			value = 25,
			rarity="Common",
			Mod= STR_mod,
			description="",
			mastery = "Slow",
			weapon_type = "Piercing. 80/320 range. Ammunition. Loading. Two-Handed. ")

		Shortbow = Weapon(
			name = "Shortbow",
			N = 1, D=6,
			weight = 2,
			quantity = 1,
			value = 25,
			rarity="Common",
			Mod= STR_mod,
			description="",
			mastery = "Vex",
			weapon_type = "Piercing. 80/320 range. Ammunition. Two-Handed. ")

		Sling = Weapon(
			name = "Sling",
			N = 1, D = 4,
			weight = 0,
			quantity = 1,
			value = 0.1,
			rarity="Common",
			Mod= STR_mod,
			description="",
			mastery = "Slow",
			weapon_type = "Bludgeoning. 30/120 range. Bullet. Two-Handed. ")

		rangeds = []
		for item in [Dart, Dagger, Javelin, Light_hammer, Handaxe, Spear, Crossbow_light, Shortbow, Sling]:
			if item.value < self.purse:
				rangeds.append(item)
		ranged = random.choice(rangeds)
		self.purse -= ranged.value
		return ranged

	def Melee(self, DEX_mod, STR_mod):
		Dagger = Weapon(
			name = "Dagger",
			weight=1, value=2, quantity=1,
			rarity="Common",
			Mod= max(DEX_mod,STR_mod),
			N = 1, D=4,
			description="",
			mastery = "Nick",
			weapon_type = "Piercing. 20/60 thrown range. Light. Finesse.")
		Greatclub = Weapon(
			name = "Greatclub",
			weight=10, value=0.2, quantity=1,
			rarity="Common",
			Mod= STR_mod,
			N= 1, D= 8,
			description="",
			mastery = "Push",
			weapon_type = "Bludgeoning. Two-Handed.")
		Handaxe = Weapon(
			name = "Handaxe",
			weight = 2,
			value = 5,
			quantity = 1,
			rarity= "Common",
			Mod= STR_mod,
			N= 1, D= 6,
			description="",
			mastery = "Vex",
			weapon_type = "Slashing. 20/60 thrown range. Light.")
		Javelin = Weapon(
			name = "Javelins", weight=8, value=2, quantity=4,
			rarity="Common",
			Mod= STR_mod,
			N= 1, D= 6,
			description="",
			mastery = "Slow",
			weapon_type = "Piercing. 30/120 thrown range.")
		Light_hammer = Weapon(
			name = "Light Hammers",
			weight = 2,
			value = 2,
			quantity = 1,
			rarity = "Common",
			Mod= STR_mod,
			N = 1, D=4,
			description="",
			mastery = "Nick",
			weapon_type = "Bludgeoning. 20/60 thrown range. Light.")
		Mace = Weapon(
			name= "Light Hammers",
			weight= 4,
			value= 0.2,
			quantity= 1,
			rarity= "Common",
			Mod= STR_mod,
			N= 1, D= 6,
			description= "",
			mastery= "Sap",
			weapon_type= "Bludgeoning.")

		Quarterstaff = Weapon(
			name= "Quarterstaff",
			weight= 4,
			value= 0.2,
			quantity= 1,
			rarity= "Common",
			Mod= STR_mod,
			N= 1, D= 6,
			description= "Versatile (1d8)",
			mastery= "Topple",
			weapon_type= "Bludgeoning.")

		Sickle = Weapon(
			name= "Sickle",
			N= 1, D= 4,
			weight= 2,
			value= 1,
			quantity= 1,
			rarity= "Common",
			Mod= STR_mod,
			description= "Versatile (1d8)",
			mastery= "Nick",
			weapon_type= "Slashing. Light")

		Spear = Weapon(
			name = "Spear",
			value = 1,
			weight = 3,
			quantity = 1,
			rarity="Common",
			Mod= STR_mod,
			N = 1, D=6,
			description="",
			mastery = "Sap",
			weapon_type = "Piercing. 20/60 thrown range. Versatile(1d8).")

		melees = []
		for item in [Dagger, Greatclub, Handaxe, Javelin, Light_hammer, Mace, Quarterstaff,
			Sickle, Spear]:
			if item.value < self.purse:
				melees.append(item)
		melee = random.choice(melees)
		self.purse -= melee.value
		return melee

	def Melee_Martial(self, DEX_mod, STR_mod):

		Dagger = Weapon(
			name = "Dagger",
			weight=1, value=2, quantity=1,
			rarity="Common",
			Mod= max(DEX_mod,STR_mod),
			N = 1, D=4,
			description="",
			mastery = "Nick",
			weapon_type = "Piercing. 20/60 thrown range. Light. Finesse.")

		Greatclub = Weapon(
			name = "Greatclub",
			weight=10, value=0.2, quantity=1,
			rarity="Common",
			Mod= STR_mod,
			N= 1, D= 8,
			description="",
			mastery = "Push",
			weapon_type = "Bludgeoning. Two-Handed.")

		Handaxe = Weapon(
			name = "Handaxe",
			weight = 2,
			value = 5,
			quantity = 1,
			rarity= "Common",
			Mod= STR_mod,
			N= 1, D= 6,
			description="",
			mastery = "Vex",
			weapon_type = "Slashing. 20/60 thrown range. Light.")

		Javelin = Weapon(
			name = "Javelins", weight=8, value=2, quantity=4,
			rarity="Common",
			Mod= STR_mod,
			N= 1, D= 6,
			description="",
			mastery = "Slow",
			weapon_type = "Piercing. 30/120 thrown range.")

		Light_hammer = Weapon(
			name = "Light Hammers",
			weight = 2,
			value = 2,
			quantity = 1,
			rarity = "Common",
			Mod= STR_mod,
			N = 1, D=4,
			description="",
			mastery = "Nick",
			weapon_type = "Bludgeoning. 20/60 thrown range. Light.")

		Mace = Weapon(
			name= "Light Hammers",
			weight= 4,
			value= 0.2,
			quantity= 1,
			rarity= "Common",
			Mod= STR_mod,
			N= 1, D= 6,
			description= "",
			mastery= "Sap",
			weapon_type= "Bludgeoning.")

		Quarterstaff = Weapon(
			name= "Quarterstaff",
			weight= 4,
			value= 0.2,
			quantity= 1,
			rarity= "Common",
			Mod= STR_mod,
			N= 1, D= 6,
			description= "Versatile (1d8)",
			mastery= "Topple",
			weapon_type= "Bludgeoning.")

		Sickle = Weapon(
			name= "Sickle",
			N= 1, D= 4,
			weight= 2,
			value= 1,
			quantity= 1,
			rarity= "Common",
			Mod= STR_mod,
			description= "Versatile (1d8)",
			mastery= "Nick",
			weapon_type= "Slashing. Light")

		Spear = Weapon(
			name = "Spear",
			value = 1,
			weight = 3,
			quantity = 1,
			rarity="Common",
			Mod= STR_mod,
			N = 1, D=6,
			description="",
			mastery = "Sap",
			weapon_type = "Piercing. 20/60 thrown range. Versatile(1d8).")

		melees = []
		for item in [Dagger, Greatclub, Handaxe, Javelin, Light_hammer, Mace, Quarterstaff,
			Sickle, Spear]:
			if item.value < self.purse:
				melees.append(item)
		melee = random.choice(melees)
		self.purse -= melee.value
		return melee

	def Ranged_Martial(self, DEX_mod, STR_mod):
		Dart = Weapon(
			name = "Darts", weight=5, value=1, quantity=20,
			rarity="Common",
			Mod= max(DEX_mod,STR_mod),
			N = 1, D=4,
			description="",
			mastery = "Vex",
			weapon_type = "Piercing. 20/60 thrown range. Light. Finesse.")

		Dagger = Weapon(
			name = "Daggers",
			weight=5, value=10, quantity=5,
			rarity="Common",
			Mod= max(DEX_mod,STR_mod),
			N = 1, D=4,
			description="",
			mastery = "Nick",
			weapon_type = "Piercing. 20/60 thrown range. Light. Finesse.")

		Javelin = Weapon(
			name = "Javelins", weight=8, value=2, quantity=4,
			rarity="Common",
			Mod= STR_mod,
			N = 1, D=6,
			description="",
			mastery = "Slow",
			weapon_type = "Piercing. 30/120 thrown range.")

		Light_hammer = Weapon(
			name = "Light Hammers",
			weight = 8,
			value = 8,
			quantity = 4,
			rarity = "Common",
			Mod= STR_mod,
			N = 1, D=4,
			description="",
			mastery = "Nick",
			weapon_type = "Bludgeoning. 20/60 thrown range. Light.")
		Handaxe = Weapon(
			name = "Handaxes",
			weight = 8,
			value = 20,
			quantity = 4,
			rarity="Common",
			Mod= STR_mod,
			N = 1, D=6,
			description="",
			mastery = "Vex",
			weapon_type = "Slashing. 20/60 thrown range. Light.")
		Spear = Weapon(
			name = "Spear",
			value = 1,
			weight = 3,
			quantity = 1,
			rarity="Common",
			Mod= STR_mod,
			N = 1, D=6,
			description="",
			mastery = "Sap",
			weapon_type = "Piercing. 20/60 thrown range. Versatile(1d8).")

		Crossbow_light = Weapon(
			name = "Light Crossbow",
			N = 1, D=8,
			weight = 5,
			quantity = 1,
			value = 25,
			rarity="Common",
			Mod= STR_mod,
			description="",
			mastery = "Slow",
			weapon_type = "Piercing. 80/320 range. Ammunition. Loading. Two-Handed. ")

		Shortbow = Weapon(
			name = "Shortbow",
			N = 1, D=6,
			weight = 2,
			quantity = 1,
			value = 25,
			rarity="Common",
			Mod= STR_mod,
			description="",
			mastery = "Vex",
			weapon_type = "Piercing. 80/320 range. Ammunition. Two-Handed. ")

		Sling = Weapon(
			name = "Sling",
			N = 1, D = 4,
			weight = 0,
			quantity = 1,
			value = 0.1,
			rarity="Common",
			Mod= STR_mod,
			description="",
			mastery = "Slow",
			weapon_type = "Bludgeoning. 30/120 range. Bullet. Two-Handed. ")

		rangeds = []
		for item in [Dart, Dagger, Javelin, Light_hammer, Handaxe, Spear, Crossbow_light, Shortbow, Sling]:
			if item.value < self.purse:
				rangeds.append(item)
		ranged = random.choice(rangeds)
		self.purse -= ranged.value
		return ranged

	def Left_Hand_Equipment(self, is_shields = False, is_light = False):
		return

	def calculate_total_weight(self):
		"""Calculate the total weight of all equipped and bagged items."""
		total_weight = 0

		# Sum weight from equipped items
		for item in [self.defense, self.melee, self.ranged, self.right, self.left]:
			if item:
				total_weight += item.weight * item.quantity

		# Sum weight from items in bag
		for item in self.bag:
			total_weight += item.weight * item.quantity

		return total_weight


def choose_melee_weapon(skills, abilities):
	"""Return a random melee weapon based on proficiencies."""

	options = []
	simple = [
		Weapon(
				name="Club",
				value=1,
				weight=2,
				N=1,
				D=4,
				Mod=Modifier(abilities.STR),
				dmg="bludgeoning",
				weapon_type="Simple",
			),
		Weapon(
			name="Mace",
			value=5,
			weight=4,
			N=1,
			D=6,
			Mod=Modifier(abilities.STR),
			dmg="bludgeoning",
			weapon_type="Simple",
		),
		Weapon(
			name="Quarterstaff",
			value=0,
			weight=4,
			N=1,
			D=6,
			Mod=Modifier(abilities.STR),
			dmg="bludgeoning",
			weapon_type="Simple",
		),
		Weapon(
			name="Dagger",
			value=2,
			weight=1,
			N=1,
			D=4,
			Mod=Modifier(abilities.DEX),
			dmg="piercing",
			weapon_type="Light",
			),
		Weapon(
			name="Club",
			value=1,
			weight=2,
			N=1,
			D=4,
			Mod=Modifier(abilities.STR),
			dmg="bludgeoning",
			weapon_type="Simple",
			),
		Weapon(
			name="Dagger",
			value=2,
			weight=1,
			N=1,
			D=4,
			Mod=Modifier(abilities.DEX),
			dmg="piercing",
			weapon_type="Light",
			),
		Weapon(
			name="Spear",
			value=1,
			weight=3,
			N=1,
			D=6,
			Mod=Modifier(abilities.STR),
			dmg="piercing",
			weapon_type="Simple",
			),
		Weapon(
			name="Mace",
			value=5,
			weight=4,
			N=1,
			D=6,
			Mod=Modifier(abilities.STR),
			dmg="bludgeoning",
			weapon_type="Simple",
			),
		]

	martial = [
		Weapon(
			name="Longsword",
			value=15,
			weight=3,
			N=1,
			D=8,
			Mod=Modifier(abilities.STR),
			dmg="slashing",
			weapon_type="Martial",
			),
		Weapon(
			name="Longsword",
			value=15,
			weight=3,
			N=2,
			D=6,
			Mod=Modifier(abilities.STR),
			dmg="slashing",
			weapon_type="Martial",
			mastery="Swords",
			),
		Weapon(
			name="Warhammer",
			value=15,
			weight=2,
			N=1,
			D=8,
			Mod=Modifier(abilities.STR),
			dmg="bludgeoning",
			weapon_type="Martial",
			),
		Weapon(
			name="Rapier",
			value=25,
			weight=2,
			N=1,
			D=8,
			Mod=Modifier(abilities.DEX),
			dmg="piercing",
			weapon_type="Martial",
			),
		Weapon(
				name="Battleaxe",
				value=10,
				weight=4,
				N=1,
				D=8,
				Mod=Modifier(abilities.STR),
				dmg="slashing",
				weapon_type="Martial",
				mastery="Axes",
				),
	]

	if skills.Martial_Weapons.is_proficient():
		options += martial
	options += simple
	return random.choice(options)
