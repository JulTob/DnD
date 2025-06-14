import random
from AtlasLudus.Map_of_Dice import Dice
from AtlasActorLudi.Map_of_Scores import PB, Modifier


def setObjects(char):
	""" Equip character with items based on skills and proficiencies. """
	from AtlasInventarium.Grimoire_of_Objects import Object
	import AtlasInventarium.Grimoire_of_Objects as objects

	char.equipment.calculate_budget(
		char.char_class, char.background, char.level )

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
		char.equipment.buy_item(tinker_Tools)

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

	if char.skills.Heavy.is_proficient():
		armor = char.equipment.HeavyArmor()
		AC_candidate = armor.armor_class
		if AC_candidate > char.AC:
			char.AC = AC_candidate
			char.equipment.equip_defense(armor)

	if char.skills.Medium.is_proficient():
		armor = char.equipment.MediumArmor(Modifier(char.abilities.DEX))
		AC_candidate = armor.armor_class
		if AC_candidate > char.AC:
			char.AC = AC_candidate
			char.equipment.equip_defense(armor)

	if char.skills.Light.is_proficient():
		armor = char.equipment.LightArmor(Modifier(char.abilities.DEX))
		AC_candidate = armor.armor_class
		if AC_candidate > char.AC:
			char.AC = AC_candidate
			char.equipment.equip_defense(armor)

	set_Armor(char)

def GenerateEquipment(char):
	"""
	Equips a character with armor, weapons, and gear based on class, background, and proficiencies.
	Spends available budget wisely.
	"""
	equip = char.equipment
	skills = char.skills
	abilities = char.abilities

	# Step 1: Calculate budget based on class, background, and level
	equip.calculate_budget(char.char_class, char.background, char.level)

	# Step 2: Equip armor intelligently
	set_Armor(char)  # Already prefers Unarmored Defense if Monk/Barb

	# Step 3: Primary weapon based on STR or DEX
	if skills.Martial_Weapons.is_proficient():
		weapons = [
			Weapon(
				name="Longsword",
				value=15,
				weight=3,
				N=1, D=8,
				Mod=Modifier(abilities.STR),
				dmg="slashing",
				description="Standard martial blade",
				weapon_type="Martial",
				mastery="Swords"
				),
			]
		weapon = random.choice(weapons)
		equip.buy_item(weapon)
		equip.equip_right(weapon)

	# Distance weapon
	if skills.Simple_Weapons.is_proficient():
		weapons = [
			Weapon(
				name="Shortbow",
				value=25,
				weight=2,
				N=1, D=6,
				Mod=Modifier(abilities.DEX),
				dmg="piercing",
				description="Light ranged weapon",
				weapon_type="Ranged",
				mastery="Bows"
				),
			]
		weapon = random.choice(weapons)
		equip.buy_item(weapon)
		equip.equip_ranged(weapon)

	else:
		# Fallback: give basic club if no proficiencies
		weapons = [
			Weapon(
				name="Club",
				value=1,
				weight=2,
				N=1, D=4,
				Mod=Modifier(abilities.STR),
				dmg="bludgeoning",
				description="Simple melee weapon"
				) ,
			]
		equip.buy_item(weapon)
		equip.equip_right(weapon)

	# Step 4: Shield if proficient
	if skills.Shields.is_proficient():
		shield = Object(
			name="Shield",
			value=10,
			weight=6,
			description="+2 AC shield"
		)
		equip.buy_item(shield)
		equip.equip_left(shield)

	# Step 5: Starter tools and survival items
	tools = [
		Object("Backpack", 2, 5, description="Standard adventurer's pack"),
		Object("Rations", 1, 2, quantity=5, description="Dry food"),
		Object("Rope", 1, 1, description="50ft hempen rope"),
		Object("Torch", 0.1, 1, quantity=3, description="Standard torch"),
		Object("Waterskin", 2, 2, description="Filled with water"),
	]

	random.shuffle(tools)
	for item in tools:
		if equip.purse >= item.value:
			equip.buy_item(item)

	# Calculate money
	char.equipment.calculate_budget(char.char_class, char.background, char.level)

	# Add armor based on proficiencies
	set_Armor(char)

	# Add one weapon based on proficiencies
	if char.skills.Swords.is_proficient():
		sword = Weapon(name="Longsword", value=15, weight=3, N=1, D=8, Mod=Modifier(char.abilities.STR), dmg="slashing")
		char.equipment.buy_item(sword)
		char.equipment.equip_right(sword)
	elif char.skills.Bows.is_proficient():
		bow = Weapon(name="Shortbow", value=25, weight=2, N=1, D=6, Mod=Modifier(char.abilities.DEX), dmg="piercing")
		char.equipment.buy_item(bow)
		char.equipment.equip_ranged(bow)

	# Add basic tools or items if money left
	if char.equipment.purse > 10:
		rope = Object(name="Rope", value=1, weight=10, description="50 feet hempen rope")
		char.equipment.buy_item(rope)

	if char.equipment.purse > 20:
		torch = Object(name="Torch", value=1, weight=1, quantity=5, description="Standard torches")
		char.equipment.buy_item(torch)


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

	if not char.equipment.defense:
		armor = char.equipment.Clothes(Modifier(char.abilities.DEX))
		char.equipment.equip_defense(armor)

	if char.skills.Shields.is_proficient():
		AC_candidate = char.AC + 2
		if AC_candidate > char.AC:
			char.AC = AC_candidate
			char.equipment.equip_left(Object(
				name = "Shield",
				value = 10,
				weight = 6,
				description = "+2 AC"))



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
		super().__init__(name, weight, value, quantity, rarity, description)
		if armor_type == "Light":
			armor.armor_class = armor_class + dex_bonus
		elif armor_type == "Medium":
			armor.armor_class = armor_class + min(dex_bonus,2)
		else:
			armor.armor_class = armor_class
		armor.armor_type = armor_type

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
			N = 1, D=6,
			Mod=0,
			dmg = "bludgeoning",
			description="",
			weapon_type = "Light",
			mastery = ""):
			"""
			Initialize an weapon object

			Parameters:
			- damage: The nDd Damage of the weapon.
			"""
			super().__init__(name, weight, value, quantity, rarity, description)
			weapon.damage = f"{N}D{D} + {Mod}  ({dmg})"
			weapon.attack = f"1D20 + {Mod}"
			weapon.mastery = mastery
			weapon.weapon_type = weapon.weapon_type

		def __repr__(weapon):
			"""String representation of Equipment."""
			base = super().__repr__()
			extra = ""
			if weapon.damage:
				extra += f"To Hit: {weapon.attack} , Damage: {weapon.damage}"
			return base + extra

class Inventory:
	def __init__(inventory):
		"""Inventory to manage equipped items, bag, and coins."""
		inventory.equipped =	[]  # List of equipped items (weapons, armor, etc.)
		inventory.bag = 	[]	# List of unequipped items
		inventory.purse = 	0 	# Purse with gold coins

		# Equipped item slots
		inventory.defense = 	None
		inventory.melee = 	None
		inventory.ranged = 	None
		inventory.right = 	None
		inventory.left = 	None

	def add_item_to_bag(self, item):
		"""Adds an item to the bag."""
		self.bag.append(item)

	def buy_item(self, item):
		"""Adds an item to the bag."""
		if self.purse > item.value:
			self.add_item_to_bag(item)
			self.purse -= item.value

	def equip_item(self, item):
		"""Equips an item and moves it from the bag to equipped items."""
		if item in self.bag:
			self.bag.remove(item)
		self.add_item_to_bag(item)

	def equip_left(self, item):
		"""Equips an item and moves it from the bag to left hand."""
		if item in self.bag:
			self.bag.remove(item)
			self.left = item
		else:
			if item.value < self.purse:
				if self.right:
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
		"""Equips an item and moves it from the bag to equipped items."""
		if item in self.bag:
			self.bag.remove(item)
			self.defense = item
		else:
			if item.value < self.purse:
				if self.defense:
					self.purse += self.defense.value
				self.defense = item
				self.purse -= item.value


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
				f"Bag: {[str(item) for item in self.bag]}\n"
				f"Purse: {self.purse} gp\n"
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
		print(f"Base budget from class: {base} gold")
		base += Dice(N = lvl - 1, D=40)
		print(f"Base budget from class and level: {base} gold")
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
			armor_class=10 + dex_mod,
			armor_type="Light",
			weight=0,
			value=0,
			description="Simple garments")

	def LightArmor(self, dex_mod=0):
		from AtlasInventarium.Grimoire_of_Objects import Armor
		return Armor(
			name="Leather Armor",
			armor_class=11 + dex_mod,
			armor_type="Light",
			weight=10,
			value=10,
			description="Leather armor")

	def MediumArmor(self, dex_mod=0):
		from AtlasInventarium.Grimoire_of_Objects import Armor
		return Armor(
			name="Scale Mail",
			armor_class=14 + min(dex_mod, 2),
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
	# ───────────────────────────────────────────

	def Left_Hand_Equipment(self, is_shields = False, is_light = False):
		return
