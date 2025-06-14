import random





def Imprisoned():
	intros = [
	"After centuries of imprisonment, <NAME> was the first <RACE> to find freedom once more, corrupting and transforming those foolish enough to try and wield the magical weapon that contained <PRONOUN> essence.",
	"After centuries locked away in the depths of <PRISON>, <NAME> emerged as the first <RACE> to reclaim freedom, unleashing a corrupting power that transformed any who dared to wield the cursed <MAGIC_WEAPON> that held the essence of a God.",
	"For ages, <NAME> languished within the shadowed confines of <PRISON>, until the bonds of captivity shattered—making <NAME> the first <RACE> to taste freedom and find retribution.",
	"Imprisoned for centuries in the dark vaults of <PRISON>, <NAME> finally broke free, marking a turning point for <NAME>.",
	"Locked away for centuries within the cursed halls of <PRISON>, <NAME> emerged as the first <RACE> to ever escape, forever altered and corrupted.",
	"After an eternity in the dungeons of <PRISON>, <NAME> shattered the chains of confinement and became the first of <RACE> to experience liberation.",
	"For centuries, <NAME> was confined within the grim recesses of <PRISON>, until at last freedom was won. As the first <RACE> to break free, <NAME> now seeks a new life. But some things are even harder to break out of."
	]
	return intros

def MagicTraits():
	intros = [
	"<TITLE> can manipulate <PRONOUN> prey's emotions and consume their essence. ",
	"<TITLE> receives flashes of memory and insight from each soul <PRONOUN> touches.",
	]
	return intros

def Feyworld(ludis):
	intros = [
		"Innately connected to the magic of the spirit realm, <NAME> is a <SUBRACE>, a kind of <RACE>. <MAGIC_TRAITS>"
		]
	return intros

def Intro(ludis):
	intros = [
		"<FALLEN>",
		"<IMPRISONED>",
		"<FALLEN>\n<IMPRISONED>",
		"In <CITY>, there lived <NAME>, a <RACE> who dreamed of <GOAL>.",
		"Long ago, <NAME> of <CITY> sought <GOAL> as a <RACE>.",
		"<FEYWORLD>",
		]
	return intros

def Corruption(ludis):
	motivations = [
		"Now, anger and dispair have corrupted <PRONOUN> heart. <TITLE> is now a heartless creature, no longer what <NAME> used to be."
		]
	if "Undead" in ludis.genus or "Undead" in ludis.genus:
		motivations += [
			"Now, with stolen flesh, he walks <KINGDOM> in a brutal approximation of his previous form.",
			]
	return motivations

def Search(ludis):
	motivations = [
	"<NAME> is now traveling the world in search of remnants of <PRONOUN> ancestors."
		]
	return motivations

def Motivation(ludis):
	motivations = [
		"<CORRUPTION>",
		"<SEARCH>",
		# Personal
		"<FAME>",
		"<FORTUNE>",
		"<FULFILLMENT>",
		"<HEALING>",
		# Duty
		"<FAMILY>",
		"<NATION>",
		"<FACTION>",
		"<DIVINE>",
		"<COSMIC>",
		"<RESPONSIBILITY>",
		# Vengeance & Redemption
		"<LOST_SOMETHING>",
		"<DISHONORED>",
		]

	return motivations

def Adventure(ludis):
	adventures = [
		"<NAME> encountered <INCITING_INCIDENT> which sparked a new path.",
		"Fate intervened when <INCITING_INCIDENT> forced <NAME> to act.",
		]
	return adventures

def Conflict(ludis):
	conflicts = [
		"Yet, <NAME> faced grave danger from <ENEMY>, needing allies to survive.",
		"However, the looming threat of <ENEMY> stood in the way of <NAME>'s goal.",
		# External Conflict
		f"<ENEMY>",
		f"<RIVALRY>",
		f"<SOCIETAL_STRUGGLE>",
		Vengance(ludis),
		# Internal Conflict
		f"<HAUNTED>",
		f"<PAST>",
		f"<WEAKNESS>",
		f"<FLAW>",
		]
	return conflicts

def City(ludis):
	return [
		"Stone Town", "Moonfall Village", "Ravenport"
		]

def Name(ludis):
	return [ludis.name]

def Title(ludis):
	return [ludis.title]

def Race(ludis):
	return [ludis.race]

def Goal(ludis):
	goals = [
		"eternal glory", "lost treasure", "family vengeance"
		]
	return goals

def Motive(ludis):
	motives = [
		"burning ambition", "a prophecy", "past humiliation"
		]
	return motives

def IncitingIncident(ludis):
	incidents = [
		"a band of outlaws attacked a traveling caravan",
		"a cursed relic chose <NAME> as its bearer",
		"the realm's Guardian offered <NAME> an impossible quest"
		]
	return incidents

def Pronoun(ludis):
	return [ludis.gender]

def Hometown(ludis):
	return [
		"a small town by the mountains",
		"a vibrant city full of lights",
		"a village in the stepes of the wilds",
		"the capital of the kingdom",
		]

def Kingdom(ludis):
	return [
		"Old Kingdom",
		"New Kingdom",
		"North",
		"South",
		"East",
		"West",
		]

def Prestige(ludis):
	return [
	"Monarch",
	"Leader",
	"Knight",
	"King",
	"Lord",
	"Queen",
	"Baron",
	"Baroness",
	"Chief",
	]

def Ideals(ludis):
	return [
		"wisdom and peace",
		"honor and justice",
		"safety and order",
		"harmony and balance",
		"courage and honor",
		"fame and fortune",
		]

def Parental(ludis):
	return [
		"father",
		"mother",
		"uncle",
		"aunt",
		"older brother",
		"older sister",
		"grandfather",
		"grandmother",
		]

def DrivenBy(ludis):
	return [
	"driven by ambition, pride, and dreams of fame.",
	"resolved never to return, until fame and fortune is earned",
	f"but one day <NAME> will return, after <GENDER> has become the <ARCHETYPE> <PRESTIGE>.",
	f"but one day <NAME> will return, after <GENDER> has become the <RACE> <PRESTIGE>.",
	]

def Hero(ludis):
	return [
	"noble warrior",
	"great hero",
	"wise wizard",
	"honored defender",
	]

def Dread(ludis):
	return [
	"Void",
	"Abernus",
	"Hell",
	"World Beyond",
	"Darkness",
	"Hades",
	]

def InocentGroup(ludis):
	return [
		"merchants",
		"monks",
		"villagers",
		"travelers",
		"townspeople",
		]

def Weapon(ludis):
	return [
		"crossbow",
		"sword",
		"axe",
		"scepter",
		"magic wand",
		"piromancy",
		]



def Hability(ludis):
	return [
		"theft",
		"secrets",
		"punching",
		"knive throwing",
		"illusions",
		"distraction",
		"oratory",
		]

def Familial(ludis):
	return [
		"father",
		"mother",
		"uncle",
		"brother",
		"sister",
		"wife",
		"husband",
		"son",
		]


def ApplyStoryConstraints(ludis, story_dict):
	"""
	Modifies story_dict based on properties from ludis (NPC).
	"""
	random.seed(ludis.seed) # for consistency

	# For example, if the race is Elf, add more 'Elf-specific' expansions:
	if "Elf" in ludis.genus or ludis.race == "Elf":
		# Force or strongly weight the RACE to "Elf"
		story_dict["RACE"] = ["Elf"]

		# Add or remove expansions in 'CITY' that are more 'Elven'
		story_dict["CITY"].extend([
			"Sylvarin Grove",
			"Celindor Haven",
			"Evergreen Glades"
		])

		# Possibly add special 'GOAL' or 'INCITING_INCIDENT' expansions:
		story_dict["GOAL"].append("defending the sacred forest")

		story_dict["INCITING_INCIDENT"].append(
			"a horde of trolls threatened the ancient glades, calling on <NAME> to defend the realm"
		)

	# If the NPC is an Orc:
	if "Orc" in ludis.genus or ludis.race == "Orc":
		# Similarly, override or add expansions for Orc
		story_dict["RACE"] = ["Orc"]
		story_dict["CITY"].extend(["Grom'gar Outpost", "Thunder Hold"])
		# etc.

	# If alignment is "Good", you might add expansions with heroic flavor:
	if "Good" in ludis.alignment:
		story_dict["MOTIVE"].append("a righteous cause to protect the innocent")

	# If the NPC is a Fiend, you might remove or alter 'GOAL' to be more sinister
	if "Fiend" in ludis.genus:
		story_dict["GOAL"].append("mastery over mortal souls")
		# Possibly remove 'eternal glory' if it doesn't fit a Fiend
		if "eternal glory" in story_dict["GOAL"]:
			story_dict["GOAL"].remove("eternal glory")

	# Return the modified dictionary
	return story_dict

def ExpandTemplate(text, dictionary):
	import re

	pattern = r"<(\w+)>"

	while re.search(pattern, text):
		match = re.search(pattern, text)
		if not match:
			break
		key = match.group(1)

		# pick random expansion
		expansion = random.choice(dictionary[key])

		# if expansion still has placeholders, expand them too
		expansion = ExpandTemplate(expansion, dictionary)

		# Replace the first occurrence
		text = text[:match.start()] + expansion + text[match.end():]

	return text


####



def Place(ludis):
	descriptors = [
		"sacred",
		"dark",
		"stone",
		]

	places = [
		"forest",
		"mountain",
		"swamp",
		"city",
		"town",
		]
	descriptor = random.choice(descriptors)
	place = random.choice(places)
	return f"{descriptor} {place}"

def Ally(ludis):
	allies = [
		f"wandering priest",
		f"wise druid",
		f"compasive nun",
		f"wandering warrior",
		f"lonely ronin",
		f"honorable knight",
		]
	ally = random.choice(allies)
	return ally


def Personality(ludis):
	gender=ludis.gender
	weapon = Weapon(ludis)
	archetype=ludis.archetype
	name=ludis.name

	personalities = [
		f"A cheerful soul, a charming fellow, and a romantic, {gender} always has a {weapon} with him.",
		f"{name} is the best {archetype} on the coast, no less.",
		f"A bit overconfident but still respected among others, {name} is always ready to lend a helping hand to a fellow {archetype}.",
		"Few people know that behind the mask of this jolly person are eyes filled with sorrow and grim determination",

		]
	if "Good" in ludis.genus:
		personalities += [
			f"Wandering around the world, {name} was always eager to do a good deed and help fellow travelers in their hour of need."
			]
	if "warrior" in ludis.genus:
		personalities += [
		f"A general who knows neither defeat nor fear. There is no problem which {gender} could not solve relying on wisdom and incredible strength."
		]
	personality = random.choice(personalities)
	return personality

def AllyTwist(ludis, ally):
	twists = [
		f"Oddly enough, the <ALLY> turned out to be a great <ARCHETYPE> retired , but still sharp and skillful as ever. the <ALLY> raised <NAME> to be a talented <ARCHETYPE>. After all this time, <NAME> has since become an accomplished <ARCHETYPE>.",
		]
	return twists


def Problem(ludis):
	archetype=ludis.archetype
	enemy = Enemy(ludis)
	problems = [
		f"That night a band of {enemy} attacked the village. They were plundering and killing locals.",
		]
	problem = random.choice(problems)
	return problem

def Treasure(ludis):
	treasures = [
		"pair of beautiful red enchanted boots",
		"gorgeous necklace",
		"precious ring",
		"jewelled dagger",
		"magic sword",
		]
	treasure = random.choice(treasures)
	return treasure

def Encounter(ludis):
	gender=ludis.gender
	race=ludis.race
	name=ludis.name
	ally = Ally(ludis)
	treasure = Treasure(ludis)

	encounters = [
		f"One morning, terrified and exhausted, {gender} met the {ally}. The {ally} took {name} with them, giving {name} a chance at a better future. <ALLY_TWIST>",
		f"One day the {race} spotted a {treasure} which belonged to a {ally}. Having decided that this was a trifling matter, {gender} immediately tried to steal the <TREASURE>, but was knocked down with a club. After that, the {ally} took pity on poor {name} and healed all wounds. This was the first time when someone was kind to {name} and actually cared for the {race}. Touched to the very heart, {name} vowed to protect the {ally} from any misfortune. Since then, {gender} has been following the {ally}, helping in any matter."
		]
	if "Human" not in ludis.genus:
		encounters += [
			f"Having encountered human beings for the first time, {gender} immediately showed her temper. When locals invited her to stop by, {gender} firmly refused, as a {race} will never share room and meal with humans.{Problem(ludis)} {name} thought that humans and their problems did not bother {title} at all and opted not to interfere, but Destiny itself proved that it knew better. That night not a single enemy escaped from {title}. "
			]
	encounter = random.choice(encounters)
	return encounter

def Mascot(ludis):
	mascots = [
		"panther",
		"bear",
		"tiger",
		"wolf",
		]
	mascot = random.choice(mascots)
	return mascot

def Ancients(ludis):
	random.seed(ludis.seed) # for consistency
	ancients = [
		"Ancients",
		"Gods",
		"Titans",
		"Elders",
		]
	ancient = random.choice(ancients)
	return ancient


def Conflicts(ludis):
	name=ludis.name
	race=ludis.race
	archetype=ludis.archetype
	gender=ludis.gender
	title=ludis.title
	inocents = InocentGroup(ludis)
	enemy = Enemy(ludis)
	pron = Pronoun(gender)

	conflicts = [
		f"{name} helped {inocents} defeat {enemy}, rescued {inocents} from threats, and earned admiration through {pron} courage.",
		f"Haunted by a shadowy past, {name} struggles with inner demons that threaten to overtake their destiny.",
		f"Driven by an unyielding quest for redemption, {name} confronts challenges that test their very soul.",
		]
	if  "Warrior" in ludis.genus:
		conflicts.append(f"Wielding unmatched strength and valor, {name} faced battles that echoed through the Kingdom.")
	if  "Knight" in ludis.genus:
		conflicts.append([
			f"Wielding unmatched strength and valor, {name} faced battles that echoed through the Kingdom.",
			f"Since childhood, {gender} was taught to become a knight, and the years of exhausting training were not in vain.",
			])
	if "Fiend" in ludis.genus:
		conflicts.append([
			f"Over the centuries, {gender} mastered the art of illusions and seduction charms, often using them for personal benefit. {name} has no equal in cunning and deceit. However, when the demons decided to seize the reins of power in the world of the living, {title} suddenly came forward to protect mortals. What reasons could {gender} possibly have? What plans is {gender} weaving? Nobody knows. And while mortals gratefully accept the help, still, they treat {name} with great caution. "
			])
	conflict = random.choice(conflicts)
	return conflict

def Resolution(ludis):
	random.seed(ludis.seed) # for consistency

	name=ludis.name
	race=ludis.race
	archetype=ludis.archetype
	gender=ludis.gender
	title=ludis.title
	resolutions = [
		f"In the end, the journey of {name} became a legendary tale of perseverance and hope.",
		f"Through trials and triumphs, {name} forged a path that shone as a beacon of resilience in dark times.",
		f"As time has flown by, {name} has become a great {archetype}. Word travels quickly, and stories about the {archetype} went forth to the four corners of the world."
		]
	if "Elf" in ludis.genus:
		resolutions += [
			f"As time has flown by, {name} has become a great {archetype}. Word travels quickly, and stories about the {archetype} went forth to the four corners of the world. They are still passed on from generation to generation, but very few know that {name} is still wandering through the {place}. "
			]
	if "Vampire" in ludis.genus:
		resolutions += [
			f"However, things changed. During a brutal encounter with a squad of high vampires, {gender} was captured and turned. {name} became one of the very monsters that {gender} always hated. The bloodsuckers hoped that {title} would become a valuable tool that could be easily manipulated, but turning into a vampire did not break the {archetype}. Having acquired new abilities, {name} escaped from captivity, killing all enemies. The thirst for retribution was stronger than the thirst for blood. The new abilities, coupled with the training and analytical mindset, made {title} a death machine for monsters. The bloody hunt for justice has begun. ",
			]
	if "Good" in ludis.genus:
		resolution += [
			f"{name} will not stop until {gender} has eliminated all those who hurt innocent people.",
			]

	resolution = random.choice(resolutions)

def FamilyWeapon(ludis):
	random.seed(ludis.seed) # for consistency
	family_weapons = [
		"pair of sacred axes",
		"book of secret spells",
		"golden sword",
		"silver scepter",
		]
	family_weapon = random.choice(family_weapons)
	return family_weapon


def Call(ludis): #Call to adventure
	random.seed(ludis.seed) # for consistency

	name=ludis.name
	archetype = ludis.archetype
	calls = [
		f"When the time was right, {name} finally departed from {Homeland(ludis)}, eager to experience adventures firsthand and embrace whatever Destiny might offer.",
		]
	call = random.choice(calls)
	return call



def Presentation(ludis):
	name=ludis.name
	race=ludis.race
	archetype=ludis.archetype
	gender=ludis.gender
	title=ludis.title
	subrace = ludis.subrace
	noble = Noble()
	ancient = Ancients(ludis)
	place = Place(ludis).capitalize()
	pron = Pronoun(gender)

	introductions = [
		f"In the dim light of a forgotten realm, {name}, a {race} {archetype}, emerged with an air of mystery. {Personality(ludis)}",
		f"Long ago, in the mystical lands, there was a {race} {archetype} known as {name} whose destiny was written in the stars.{Personality(ludis)} {Personality(ludis)}",
		f"{name} is the last heir of a once illustrious {knight} who lost his entire fortune in gambling. Now {gender} has got neither land to inherit, nor wealth. {gender.capitalize()} has no more ties at home, so {name} travels the world striving to become famous, get rich and reclaim the family's ancestral castle.",
		f"{gender} has embarked on the most dangerous adventures, but luck and innate talents often allowed {title} to get away with it. Mostly being penniless for some reason, though. {Personality(ludis)}",
		f"It’s been many years now. Night after night, {name} wakes up haunted by a nightmare, replaying the tragic events of that fatal night. {Incident(ludis)} ",
		f"{name} always resented being part of the {subrace} civilization. {name} felt a deep aversion to those in power - selfish, avaricious, and wicked. Always power-hungry and willing to do anything to seize power and gold. {Personality(ludis)} The older {gender} got, the move obvious it felt - {gender} did not belong there, in a sin-racked world.",
		f"Born in a deprived neighborhood, {name} always knew that life was rough; hunger and cold were frequent companions. {name} learned how to fight to survive and mastered the art of {Hability(ludis)}, which saved his life more than once. One more fight and {gender} decided to leave town forever.",
		f"{name} is a {archetype} and a closest confidant of the king. There have been legends about his shiny merits and glorious deeds for the kingdom, certainly, every young and little {race} knows the name of {title}. {gender.capitalize()} is the embodiment of a living legend. {Trait(ludis)}",
		f"{name} is the youngest offspring of the {subrace} {noble}. The {noble} was fervently trying to protect {name}, that is why {gender} was never sent on a challenging mission. There was a particular reason, though. Long before {name} was born, the High Priest delivered a prophecy to the {noble}. It stated that {name} is destined to play a special role in the course of history. The {noble} desperately tried to safeguard {name}, but even though {gender} grew up hardly suspecting that {gender} was chosen by Fate, one day everything changed. {Incident(ludis)} ",
		f"There is no creature in the world whose bad luck is worse than that of {name}. {gender.capitalize()} could only get up early in the morning, and it was enough for a young {race} to get into new troubles. Once {gender} learned to walk, the peaceful days in his village were over. There was not a single day when the villagers did not discuss the latest troubles of the unlucky {race}. Falling into a well, becoming a victim of a swarm of wild bees, eating a handful of unripe fruit and not being able to leave the privy during a week afterwards... And all of this was just the beginning. {name} was growing up, and so was the misfortune. {Incident(ludis)}",
		f"""Even being in a cradle, {name} was charmed by other people's things, consequently snatching everything {gender} could, whether being unnoticed or not. As {gender} grew older, kleptomania only intensified. But misadventures were getting worse every time {gender} exercised the thief's craft. The more expensive things {gender} tried to steal, the more often {gender} got severely punched. Tired of the escapades of {name}, the {race} village kicked him out. But this hardly taught a lesson to {name}. While traveling, {gender} often found new troubles. {Encounter(ludis)}""",
		f"{name} is the last descendant of the wealthiest {noble} of {place}. As a child, {gender} experienced real horror, witnessing how {enemy} brutally murdered the parents of {name}. {Vengance(ludis)}"
		]
	if "Elf" in ludis.genus:
		introductions.append([
			f"Graceful and wise, {name}'s elven heritage imbued them with an otherworldly charm."
			])
	if  "Knight" in ludis.genus:
		introductions.append([
			f"Having been granted an honorary title of knighthood upon reaching maturity, {name} managed to participate in various warfare campaigns and sieges, and proved to be a brave and skilled warrior",
			f"A beggar knight known to everyone.",
			])
	if "Good" in ludis.genus:
		introduction.append([
			f"Although allies and fellows have called {title} a daredevil - the one who undertakes a risky challenge thinking little in advance and is guided only by his urge to take action - they all also note that {name} is a good-natured comrade who will never leave a friend behind. ",
			])
	if ludis.subrace in  ["Aberration", "Fiend", "Monstrosity", "Ooze", "Undead"]:
		introduction.append([
			f"Something terrible happened several thousand years ago. A sudden split occurred among the {ancient}, which led to a centuries-long war. The history of those events is now hidden in the mists of time, but we all know exactly what caused it. Some of the {ancient} embraced the dark ways of magic, hoping to gain more power. They got what they desired, but the price was high. Their own souls turned dark, darker than the Night, and their selfs transformed, reborn into something new and horrifying. This is how {subrace} appeared, and {name} was one of the first among them.",
			])


	intro = random.choice(introductions)
	return intro

def ArchetypeBackground(ludis):
	background = [
		f"Years ago, in {Homeland(ludis)}, {name}, a young {race}, grew up listening to captivating stories of adventure told by {pron} {Parental(ludis)}. These tales planted the seeds of dreams within {pron} heart.",
		f"For centuries, {name}, {title}, has wandered the world, spreading {Ideals(ludis)}.",
		f"Since childhood, {name}, a young {race}, lived in the shadow of {pronoun} family’s fallen glory, trained rigorously to restore {pronoun} ancestral legacy as a {archetype}.",
		]
	if "Noble" in ludis.genus:
		background += [
			f"{name} is the descendant of a once illustrious {Prestige(Ludis)} who lost {pronoun} entire fortune gambling.",
			]
	if "Fiend" in ludis.genus:
		background = [
				f"{name}, once a {Hero(ludis)} revered across The {Kingdom(ludis)}, was among the legendary champions who defended it from the threat of The <DREAD>. {Fall(ludis)}",
				]

	background = random.choice(background)
	return background

def BioOrigin(ludis):
	race = ludis.race
	subrace = ludis.subrace
	origins = [
		f"Belonging to the ancient {race} race known as the {subrace}, remaining very few nowdays.",

		]
	origin = random.choice(origin)
	return origin



#########################


def Reputation(ludis):

	reputations = [
		f"Renowned for <PRONOUN> mastery of the <WEAPON>, <TITLE> bears a special insignia awarded by grateful townspeople.",
		f"Wherever <GENDER> goes, children run joyfully to greet, enchanted by <PRONOUN> kindness and the countless stories.",
			f"<PRONOUN> reputation as <TITLE> follows everywhere <GENDER> goes, marking <NAME> as a daring <ARCHETYPE> known to risk everything without careful consideration.",
			f"Highly sociable and good-hearted, <NAME> makes friends easily, forging bonds of loyalty across numerous campaigns, always willing to risk everything for a companion.",
			]
	if "Celestial" in genus:
		reputations += [
			f"Renowned globally, <NAME> is revered by many, even worshipped as a divine being."
			]
	if "Good" in genus:
		reputations += [
			f"Known throughout the realm as <TITLE>. Daring but good-natured, <NAME> never abandons those in need, earning admiration and friendships wherever <PRONOUN> path leads."
			]
	return reputations


def Rellationships(ludis):
	random.seed(ludis.seed) # for consistency

	name = ludis.name
	title = ludis.title
	archetype = ludis.archetype
	gender = ludis.gender
	pronoun = Pronoun(gender)
	genus = ludis.genus
	subrace= ludis.subrace
	race= ludis.race
	parent = Parental(ludis)
	ideals = Ideals(ludis)

	rellationships = [
			f"{name} secretly belongs to the ancient race of the {subrace}, an ancient lineage whose numbers have dwindled over the millennia. ",
			f"Guided and inspired by stories of {pronoun} ancestors, especially {pronoun} {parent}, an impoverished yet noble figure, who instilled in {name} the values of {ideals}.",
			]
	rellationship = random.choice(rellationships)
	return rellationship

def Incident(ludis):
	random.seed(ludis.seed) # for consistency

	name=ludis.name
	race=ludis.race
	archetype=ludis.archetype
	gender=ludis.gender
	title=ludis.title
	enemy = Enemy(ludis)
	mascot = Mascot(ludis)
	noble = Noble()
	place = Place(ludis)
	pronoun = Pronoun(gender)

	incidents = [
		f"Finally ready, {name} ventured into the unknown, awaiting whatever Destiny might offer. A chance appeared when {gender} saved locals from disaster.",
		f"One moonless night, home is attacked by {enemy}. {Parental(ludis).capitalize()} tries to protect {name}, hiding the young kid in the cellar. The creatures of the night are feasting, and the house shakes with baleful laughter and cries. Nobody survived that dreadful night, except for the little {name} in the cellar. When the bloodbath was over, {name} slipped out of the ruins and escaped into the {Place(ludis)}. {Encounter(ludis)}. Now {name} wants vengance on all {enemy}. {Vengance(ludis)}",
		f"{Personality(ludis)} In the course of some wanderings, {gender} met a faithful friend - a {mascot}, wounded and captured by poachers. They did not stand a chance against a {title}. The bond that linked the {subrace} and the rescued creature has strengthened ever since. Should {name} summon it, the {mascot} is always there to help.",
		f"Rumor has it that once {gender} single-handedly withstood an entire army. Truth be told, this was not a great exaggeration... Few decades ago, the {race} king was surrounded by a horde, and it seemed that his death was inevitable. But suddenly {name} burst into the enemy troops. As quick and deadly as a lightning strike, {title} cut down one enemy after another. The horde trembled after his ferocious onslaught and began to give up their positions. After the massacre, {name} recaptured the king alive, albeit injured. The king could no longer take part in battles and, as a token of gratitude for his salvation, honored {name} with his {Weapon(ludis)}. Since then, {name} has been the embodiment of the king’s will and a symbol of peace in the Kingdom. Since then, {gender} has been defending the borderlines, instilling confidence and fighting spirit into other guardians of the realm. ",
		f"{name} was trained in the secret guild of {Place(ludis)} Sentinels.",
		f"Darkness has closed in and dreadful omens proclaimed an inevitable disaster. That’s how it all started. {title} was finally assigned to set off on a mission - a clandestine one, so hard and so secret, that {subrace} superiors themselves knew nothing about it. {gender.capitalize()} was deeply discouraged and could only guess if the task was ever possible to accomplish, but never showed any doubt in front of the {noble}. ",
		f"Leaving home, {place}, {name} said farewell to her kith and kin. Everybody came to say goodbye, as now they could only hope that {gender} would come back. {name} started a journey to the big world with no clue where to go. {Encounter(Ludis)}",
		f"Forced to leave {pronoun} {Homeland(ludis)}, {name} set out into the unknown, {DrivenBy(ludis)}.",
		]
	incident = random.choice(incidents)
	return incident

def Twist(ludis):
	random.seed(ludis.seed) # for consistency

	name=ludis.name
	title=ludis.title
	archetype = ludis.archetype
	gender = ludis.gender
	genus = ludis.genus
	pronoun = Pronoun(gender)

	twists = [
			f"Yet, behind {pronoun} gentle appearance, lies a serious and judicious protector tasked with safeguarding the threads of Reality.",
			f"Gifted with exceptional bravery, unmatched luck, and an extraordinary ability to survive against all odds, {title} is famous for rushing headlong into danger and miraculously escaping unscathed.",
			]
	twist = random.choice(twists)
	return twist

def Struggle(ludis):
	def SocietalStruggle(ludis):
		name=ludis.name
		title=ludis.title
		gender = ludis.gender
		pronoun = Pronoun(gender)
		conflicts = [
				f"Long ago, {name} made a fateful decision against the sacred laws of {Pronoun(gender)} people: {gender} took an apprentice from beyond the Realm, breaking an ancient rule that forbade interference.",
				f"Despite embarking on countless perilous adventures, fortune has rarely favored {title} financially. {name} is frequently penniless despite {pronoun} many exploits.",
				f"Having neither land to inherit nor wealth to promise comfort, {name} has no more ties to {pronoun} home.",

				]
		conflict = random.choice(conflicts)
		return conflict

	random.seed(ludis.seed) # for consistency

	name=ludis.name
	archetype = ludis.archetype
	gender = ludis.gender
	genus = ludis.genus

	conflicts = [
			f"{SocietalStruggle(ludis)}",
			]
	conflict = random.choice(conflicts)
	return conflict

def Resolution(ludis):
	gender = ludis.gender
	title = ludis.title
	pronoun = Pronoun(gender)

	resolutions = [
			f"Despite {pronoun} unresolved inner struggles, {title}continues wandering the world, quietly defending the mortal realm from dark forces of the underworld.",
			f"Continuing on {pronoun} endless quest for {Ideals(ludis)}, {name} remains a wandering legend. Beloved by allies, respected for bravery, yet perpetually impoverished, determined to one day reclaim {pronoun} ancestral home."
			]
	resolution = random.choice(resolutions)
	return resolution

###
def Fulfillment(ludis): # For the functions
	random.seed(ludis.seed) # for consistency
	things = [
		f"",
		]
	thing = random.choice(things)
	return thing

def Fortune(ludis): # For the functions
	random.seed(ludis.seed) # for consistency
	things = [
		f"",
		]
	thing = random.choice(things)
	return thing

def Trait(ludis): # SOmething significant about them
	random.seed(ludis.seed) # for consistency
	things = [
		f"{Skill(ludis)}",
		f"{Mark(ludis)}",
		f"{Insignia(ludis)}",
		]
	thing = random.choice(things)
	return thing

def Reputation(ludis): # What people think of them
	random.seed(ludis.seed) # for consistency
	reputations = [
		f"{Legendary(ludis)}",
		f"{Heroic(ludis)}",
		f"{Disgraced(ludis)}",
		f"{Fallen(ludis)}",
		f"{Outsider(ludis)}",
		f"{Unknown(ludis)}",
		f"{Outsider(ludis)}",
		]
	reputation = random.choice(reputations)
	return reputation

def Origin(ludis):
	origins = [
		f"{Humble(ludis)}",
		f"{Noble(ludis)}",
		f"{Tragic(ludis)}",
		f" {Exceptional(ludis)}",
		]
	origin = random.choice(origins)
	return intro

def Introduction(ludis): # Origin & Normality
	random.seed(ludis.seed) # for consistency
	introductions = [
		f"<ORIGIN>",
		f"<REPUTATION>",
		f"<TRAIT>",
		f"<ORIGIN><REPUTATION>",
		f"<ORIGIN><TRAIT>",
		f"<REPUTATION><TRAIT>",
		#TooLong? f"<ORIGIN><REPUTATION><TRAIT>",
		]
	intro = random.choice(introductions)
	return intro


def Adventure(ludis): # Character ventures into unfamiliar world
	random.seed(ludis.seed) # for consistency
	adventures = [
		# Call to Adventure
		f"{Voluntary(ludis)}",
		f"{Forced(ludis)}",
		f"{Accidental(ludis)}",
		# Inciting Incident
		f"{Witness(ludis)}",
		f"{Injustice(ludis)}",
		f"{Encounter(ludis)}",
		f"{Tragedy(ludis)}",
		f"{Revelation(ludis)}",
		# Early Achievements
		f"{HeroicDeed(ludis)}",
		f"{Discovery(ludis)}",
		f"{Acquisition(ludis)}",
		f"{EarnedHonor(ludis)}",
		f"{Title(ludis)}",
		]
	adventure = random.choice(adventures)
	return adventure


def Quest(ludis):
	def Lost_Object():
		def Blueprint(ludis):
			random.seed(ludis.seed) # for consistency
			things = [
				f"",
				]
			thing = random.choice(things)
			return thing

		random.seed(ludis.seed) # for consistency
		things = [
			f"The heirloom sword of the House Valerian was lost centuries ago, rumored to rest deep within the Dark Forest.",
			]
		thing = random.choice(things)
		return thing
	def Sacred_Artifact():
		random.seed(ludis.seed) # for consistency
		things = [
			f"Recover the Crystal Orb hidden in the forgotten temple ruins to restore balance to the kingdom.",
			]
		thing = random.choice(things)
		return thing
	def Protect_Town(ludis):
		random.seed(ludis.seed) # for consistency
		things = [
			f"Defend Stone Town from impending attacks by ruthless outlaws who threaten local merchants.",
			]
		thing = random.choice(things)
		return thing
	def Prophecy(ludis):
		random.seed(ludis.seed) # for consistency
		things = [
			f"Hunt down the necromancer responsible for the massacre of your village.",
			]
		thing = random.choice(things)
		return thing
	def Vengeance(ludis):
		random.seed(ludis.seed) # for consistency
		things = [
			f"Hunt down the necromancer responsible for the massacre of your village.",
			]
		thing = random.choice(things)
		return thing
	def Restore_Honor(ludis):
		random.seed(ludis.seed) # for consistency
		things = [
			f"Recover the ancestral castle lost by your father due to gambling debts, restoring honor to your family’s lineage.",
			]
		thing = random.choice(things)
		return thing
	def Kidnapping(ludis):
		random.seed(ludis.seed) # for consistency
		things = [
			f"Rescue the mayor's daughter captured by a savage troll hiding deep in the dark mountains.",
			]
		thing = random.choice(things)
		return thing
	def Mysterious_Ruins(ludis):
		random.seed(ludis.seed) # for consistency
		things = [
			f"Explore ruins of an ancient civilization in search of long-forgotten knowledge about the Ancients.",
			]
		thing = random.choice(things)
		return thing
	def Protect_Person(ludis):
		random.seed(ludis.seed) # for consistency
		things = [
			f"I need to safely guide the Mayor’s son across the dark forest path known for monster ambushes.",
			]
		thing = random.choice(things)
		return thing
	random.seed(ludis.seed) # for consistency
	quests = [
		# Defense
		f"{Protect_Town()}",
		f"{Defend_Bastion()}",
		# Elimination
		f"{Defeat_Creature()}",
		f"{Assassinate_Target()}",
		f"{Clear_Enemy_Base()}",
		# Rescue
		f"{Kidnapping()}",
		f"{Missing_Adventurers()}",
		f"{Trapped_Innocents()}",
		# Exploration
		f"{Uncharted_Land()}",
		f"{Mysterious_Ruins()}",
		f"{Lost_City()}",
		f"{Forbidden_Area()}",
		# Personal_Quest
		f"{Redemption()}",
		f"{Restore_Honor()}",
		f"{Vengeance()}",
		f"{Prophecy()}",
		f"{Enlightenment()}",

		]
	quest = random.choice(quests)
	return quest

def Storyold(ludis):
	"""
	Generate a story for an ludis based on their characteristics.
	The ludis parameter is expected to be a ludis (PC/NPC) object
	"""

	# Combine the sections to form the final story.

	story_templates = [
		f"{Introduction(ludis)}{Motivation(ludis)}{Adventure(ludis)}{Conflict(ludis)}{Quest(ludis)}"
		]
	story = random.choice(story_templates)
	return story


def Story(ludis):
	try:

		# 1) Get the base dictionary
		base_dict = StoryTree(ludis)

		# 2) Apply constraints based on the NPC
		constrained_dict = ApplyStoryConstraints(ludis, base_dict)

		# 3) Expand placeholders from the "STORY" root
		template = random.choice(constrained_dict["STORY"])
		story_text = ExpandTemplate(template, constrained_dict)
	except ImportError as e:
		Alert(f"The Story couldn't be built:\n {e}", e)
		story_text = f"The story of {ludis.title}is hidden in mystery."

	return story_text

def Theme(ludis):
	themes = []
	return themes

def Gender(ludis):
	return ludis.gender

def StoryTree(ludis):
	story = {
	"NAME": Name(ludis),
	"TITLE":Title(ludis),
	"RACE": Race(ludis),
	"PRONOUN":Pronoun(ludis),
	"GENDER": Gender(ludis),
	"STORY": [
		"<INTRO> <MOTIVATION> <ADVENTURE> <CONFLICT> <QUEST>",
		"<INTRO> <MOTIVATION> <QUEST>"
		],
	"INTRO": Intro(ludis),
	"MOTIVATION": Motivation(ludis),
	"ADVENTURE": Adventure(ludis),
	"CONFLICT": Conflict(ludis),
	"QUEST": [
		"<RETRIEVAL>",
		"<ESCORT>",
		"<INVESTIGATION>",
		"<DEFENSE>",
		],
	"RETRIEVAL": [
			f"<LOST>",
			f"<STOLEN>",
			f"<SACRED_ARTIFACT>",
			f"<LEGENDARY_WEAPON>",
			],
	"ESCORT": [
		"<PROTECT_PERSON>",
		"<GUIDE_TRAVELERS>",
		"<SAFELY_TRANSPORT>",
		],
	"INVESTIGATION": [
		"<SOLVE_MYSTERY>",
		"<DISCOVER_TRUTH>",
		"<EXPOSE_TRAITOR>",
		"<UNCOVER_ANCIENT_SECRET>",
		],
	"CITY": City(ludis),
	"GOAL": Goal(ludis),
	"MOTIVE": Motive(ludis),
	"INCITING_INCIDENT": IncitingIncident(ludis),
	"HOMETOWN": Hometown(ludis),
	"KINGDOM":Kingdom(ludis),
	"PRESTIGE":Prestige(ludis),
	"IDEALS": Ideals(ludis),
	"PARENTAL": Parental(ludis),
	"DRIVEN_BY": DrivenBy(ludis),
	"HERO": Hero(ludis),
	"DREAD": Dread(ludis),
	"INOCENT_GROUP": InocentGroup(ludis),
	"WEAPON": Weapon(ludis),
	"REPUTATION": Reputation(ludis),
	"HABILITY": Hability(ludis),
	"FAMILIAL": Familial(ludis),
	"ENEMY": Enemy(ludis),
	"CORRUPTION": Corruption(ludis),
	"PRISON": Prison(ludis),

	}
	return story

def Vengance(ludis):
	statements = [
		"<TITLE> is seeking an apocalyptic and long overdue vengeance.",
		"<TITLE> now walks the world burdened by an insatiable desire for retribution.",
		f"<NAME> has slain hordes of <ENEMY> but failed to find the ones who killed the family <PRONOUN> forever lost.",
		f"Seeking revenge, <PRONOUN> will know no rest until justice is served.",
		"Haunted by loss, <NAME> has embraced a destiny of relentless vengeance.",
		]
	failures = [
		"<TITLE> has slain hordes of <ENEMY>, yet the elusive specter who wronged <NAME> remains unavenged.",
		f"After that, <PRONOUN> vowed to dedicate a lifetime to the fight against <ENEMY>. For many years, <NAME> trained, turning into an instrument of retribution. But never was <PRONOUN> just a mad butcher. <TITLE> was a talented strategist who always kept studying the peculiarities and habits of <ENEMY>. With each new hunt, the <ARCHETYPE> gained new skills and searched for the enemy's weak points. ",
		"In the blood of countless battles, <TITLE> failed to reclaim what was stolen, leaving a void that no victory could fill.",
		"Though <NAME> has toppled legions of <ENEMY>, the fateful act that shattered <PRONOUN> world remains unresolved.",
		]
	strategies = [
		"Driven by a burning desire for justice, <NAME> will not know rest until every wrong is righted.",
		"For <NAME>, vengeance is a sacred oath. One that demands relentless pursuit until the scales of fate are balanced.",
		"No shadow of doubt crosses the mind of <NAME>: justice must be exacted, no matter the cost.",
		"After that fateful day, <NAME> vowed to dedicate a lifetime to the eradication of <ENEMY>. Through rigorous training, <NAME> transformed into a master tactician, each battle honing <PRONOUN> resolve.",
		"Refusing to succumb to despair, <NAME> immersed in relentless discipline, studying every nuance of <ENEMY>'s methods until every weakness was laid bare.",
		"The scars of failure spurred <NAME> to seek perfection in the art of retribution; every duel, every strategy, became a stepping stone toward a meticulously calculated vengeance.",
		"With every confrontation, <NAME> refined <PRONOUN> technique, evolving from a mere avenger into a living embodiment of retribution. An instrument honed to dismantle the very essence of <ENEMY>.",
		]
	# Randomly select one element from each list
	part1 = random.choice(statements)
	part2 = random.choice(failures)
	part3 = random.choice(strategies)

	# Concatenate the parts with appropriate punctuation/spaces
	full_paragraph = f"{part1} {part2} {part3}"

	# Optionally, you can run this full paragraph through your ExpandTemplate function to replace placeholders
	full_paragraph = ExpandTemplate(full_paragraph, StoryTree(ludis))

	return full_paragraph

def Enemy(ludis):
	race = ludis.race
	genus = ludis.genus

	enemies = [
		"vampires",
		"necromancers",
		"demons",
		"ghouls",
		"zombies",
		"cursed wolves",
		"werewolves",
		"outlaws",
		"bandits",
		"zealots",
		]
	if "Fiend" in genus or race == "Fiend":
		enemies += [
			"celestials",
			"angels",
			"clerics",
			"paladins"
			]
	if "Undead" in genus or race == "Undead":
		enemies = [
			"elementals",
			"constructs",
			"lycans",
			"angels",
			"angels",
			"celestials",
			"oozes",
			"animated plants",
			"paladins",
			"clerics",
			"zealots",
			"inquisitors",
			]
	if "Elf" in genus or race == "Elf":
		enemies += [
			"dwarves",
			"automatons",
			"dragons",
			"giants",
			"humans",
			"lizardfolk",
			"snakefolk",
			"animated plants",
			]
	if "Orc" in genus or race == "Orc":
		enemies += [
			"dragons",
			"aberrations",
			"constructs",
			"elementals",
			"pixies",
			"hags",
			"gnomes",
			"goblins",
			"chimeras",
			"wendigos",
			"sphynxs",
			]
	if "Human" in genus or race == "Human":
		enemies += [
			"undeads",
			"aberrations",
			"beasts",
			"fiends",
			"dragons",
			"giants",
			"nagas",
			"oozes",
			"beholders",
			"illithid",
			"giths",
			]
	if "Aberration" in genus or race == "Aberration":
		enemies += [
			"beastfolk",
			"beastfolk warbands",
			"arachnidfolk",
			"druids",
			"monster-hunters",
			"titans",
			"paladins",
			"inquisitors",
			"centaurs",
			"gnolls",
			"lycans",
			"minotaurs",
			"ratfolk",
			"skinwalkers",
			"werebears",
			"catfolk",
			"celestials",
			"angels",
			"golems",
			]
	if "Beast" in genus or race == "Beast":
		enemies += [
			"aberrations",
			"constructs",
			"centaurs",
			"demons",
			"devils",
			"dragons",
			"drones",
			"dwarfs",
			"mutants",
			"ogres",
			"robots",
			"shadows",
			"specters",
			"warlocks",
			"wizards",
			"humans",
			"hunters",
			]
	if "Beastfolk" in genus or race == "Beastfolk":
		enemies += [
			"angels",
			"dwarves",
			"humans",
			"halflings",
			"kobolds",
			"gnomes",
			"lizardfolk",
			"monsters",
			"orcs",
			"nagas",
			"giths",
			"dragonborns",
			"cyclops",
			"pirates",
			"raiders",
			"soldiers",
			"sorcerers",
			"warlords",
			"slavers",
			]
	if "Catfolk" in genus or race == "Catfolk":
		enemies += [
			"constructs",
			"dragons",
			"giants",
			"kobolds",
			"lizardfolk",
			"monsters",
			"dinosaurs",
			"nagas",
			"gorgons",
			"snakefolk",
			"undeads",
			"vampires",
			]
	if "Aven" in genus or race == "Aven":
		enemies += [
		"dragons",
		"elementals",
		"giant eagle tyrants",
		"sky tyrants",
		"catfolk",
		"sky pirates",
		"snakefolk",
		"nagas",
		"beholders",
		"illithid",
		"eldritch horrors",
		"drones",
		"trolls",
		"vampires",
			]
	if "Celestial" in genus or race == "Celestial":
		enemies += [
			"fiends",
			"hellspawn",
			"demons",
			"abominations",
			"fallen angels",
			"cultists",
			"Chaos Fiends",
			"fallen angels",
			]
	if "Construct" in genus or race == "Construct":
		enemies += [
			"druids",
			"dwarves",
			"elementals",
			"fey",
			"gnomes",
			"goblins",
			"halflings",
			"oozes",
			"trolls",
			"treants",
			"awakened trees",
			"ents",
			"dryads",
			"Wood Elves",
			"Sylvan Elves",
			"Wild Elves",
			"eladrins",
			"nagas",
			"lamias",
			"barbarians",
			"shamans",
			]
	if "Dragon" in genus or race == "Construct":
			enemies += [
			"titans",
			"heroes",
			"knights",
			"mages",
			"paladins",
			"rangers",
			"rogues",
			"wizards",
			"dwarves",
			"elves",
			"giants",
			"halflings",
			"humans",
			"dragon-slayers",
			"orcs",
			"leonids",
			"sphynxes",
			"leprechauns",
			"ogres",
			"trolls",
			"Frost Giants",
			"Fire Giants",
			"onis",
			"Stone Giants",
			"Storm Giants",




				]
	if "Dwarf" in genus or race == "Dwarf":
			enemies += [
			"elven warbands",
			"criminals",
			"mages",
			"pirates",
			"soldiers",
			"sorcerers",
			"wizards",
			"wiches",
			"aven raiders",
			"robots",
			"dragons",
			"humans",
			"elves",
			"goblins",
			"kobolds",
			"monters",
			"undeads",
			"ogres",
			"trolls",
			"Frost Giants",
			"Fire Giants",
			"onis",
			"Stone Giants",
			"Storm Giants",
				]
	if "Elemental" in genus or race == "Elemental":
			enemies += [
			"elven warbands",
			"mage-thieves",
			"mages",
			"warlocks",
			"clerics",
			"sorcerers",
			"wizards",
			"wiches",
			"druids",
			"robots",
			"celestials",
			"humans",
			"nagas",
			"beholders",
			"elder gods",
			"merfolk",
			"dragons",
			"gnomes",
			"goblins",
			"gremlins",
			"krakens",
			"Shadows",
			]
	if "Elf" in genus or race == "Elf":
			enemies += [
			"dwarven industrialists",
			"demonic whisperers",
			"human lumber barons",
			"sorcerers",
			"angels",
			"constructs",
			"dragons",
			"fire elementals",
			"warlocks and demons",
			"kobolds",
			"lizardfolk",
			"monsters",
			"slime cubes",
			"Uruk warlords",
			"Gorgones",
			]
	if "Fey" in genus or race == "Fey":
			enemies += [
			"wizard hunters",
			"iron-knights",
			"beholders",
			"chaos demons",
			"eldritch horrors",
			"owlins",
			"harpies",
			"kongs",
			"kitsunes",
			"centaurs",
			"gnolls",
			"minotaurs",
			"werewolves",
			"werebears",
			"golems",
			"clockwork horrors",
			"modrons",
			"genies",
			"imps",
			"trolls",
			"chimeras",
			"warlocks",
			"shamans",
			"inquisitors",

			]
	if "Fiend" in genus or race == "Fiend":
			enemies = [
			"celestials",
			"crusaders",
			"paladins",
			"demon hunters",
			"inquisitors",
			"clerics",
			"heroes",
			"knights",
			"monks",
			"exorcists",
			"exorcist priests",
			"warlocks",
			"gods",
			"minor gods",
			"angels",
			]
	if "Giant" in genus or race == "Giant":
			enemies += [
			"dragons",
			"titans",
			"gods",
			"fae",
			"gnomes",
			"goblins",
			"halflings",
			"humans",
			"berserkers",
			"heroes",
			"giant hunters",
			"knights",
			"paladins",
			"rogues",
			"tricksters",
			"satyrs",
			"golems",
			"sphynxes",

			]
	if "Gnome" in genus or race == "Gnome":
		enemies += [
			"kobolds",
			"ogres",
			"basilisks",
			"chimeras",
			"clerics",
			"catfolk",
			"orcs",
			"kitsunes",
			"centaurs",
			"genies",
			"hags",
			"trolls",
			"onis",
			]
	if "Goblin" in genus or race == "Goblin":
		enemies += [
		"ogres",
		"trolls",
		"giants",
		"chimeras",
		"orcs",
		"goblin hunters",
		"goblin slayers",
		"halflings"
		"griffins",
		"manticores",
		"dragons",
		"dwarves",
		"dwarven conquistadors",
		"fiends",
		"giants",
		"halfling raiders",
		"vampire inquisitors",
		"monsters",
		]
	if "Halfling" in genus or race == "Halfling":
		enemies += [
		"giant rabbits",
		"giant rats",
		"salamanders",
		"satyrs",
		"living scarecrows",
		"giant spiders",
		"giant scorpions",
		"giant slugs",
		"giant snails",
		"giant snakes",
		"trolls",
		"dragons",
		"warlocks",
		"wolves",
		"werewolves",
		"barbarians",
		]
	if "Human" in genus or race == "Human":
		enemies += [
			"bandits",			"barbarians",			"berserkers",			"mercenaries",			"zealots",			"inquisitors",			"dark wizards",			"ninjas",			"pirates",			"sorcerers",			"hags",			"dinosaurs",			"dragons",			"lycans"
			]
	if "Kobold" in genus or race == "Kobold":
		enemies += [
			"minotaurs",		"ratfolk",		"catfolk",		"drones",		"golems",		"androids",		"knights",		"modrons",		"shadow demons",		"pixies",		"giants",		"cyclops",		"trolls",		"ogres",
			]
	if "Lizardfolk" in genus or race == "Lizardfolk":
		enemies += [
		"elven ragngers",		"pyromancers",		"snakefolk",		"nagas",		"gorgons",		"scorpionfolk",		"poachers",		"giant slimes",		"constructs",
		]
	if "Monstrosity" in genus or race == "Monstrosity":
		enemies += [
			"witchers",		"heroes",		"warriors",		"mages",		"sorcerers",		"drones",		"titans",		"giants",		"beholders",		"kongs",		"minotaurs",
			]
	if "Ooze" in genus or race == "Ooze":
		enemies += [
			"knights",			"pyromancers",			"alchemists",			"androids",			"dragons",			"fire elementals",			"ice elementals",			"storm elementals",			"elementals",			"demons",			"fire demons",			"fire giants",
			]
	if "Orc" in genus or race == "Orc":
		enemies += [
			"dragons",			"elven raiders",			"dwarven warmongers",			"human nobles",			"gorgons",			"wendigos",			"abominations",			"yetis",			"hunters",			"soldiers",
			]
	if "Plant" in genus or race == "Plant":
		enemies += [
			"pyromancers",			"slimes",			"fire elementals",			"magma elementals",			"dragons",			"dwarf industrialits","humans",			"fire giants",
			]
	if "Snakefolk" in genus or race == "Snakefolk":
		enemies += [
			"lizardfolk",			"assassins",			"paladins",			"goblins",			"catfolk",
			]
	return enemies

def Prison(ludis):
	intros = []
	race = ludis.race  # Expecting a string, e.g., "Elf", "Orc", etc.
	archetype = ludis.archetype.lower()  # To ease comparisons

	# Race-specific prison descriptions:
	if race == "Elf":
		intros.append("the ancient, ivy-draped prison of the Twilight Glade")
		intros.append("the enchanted dungeons of the Moonlit Citadel")
	elif race == "Orc":
		intros.append("the brutal underground pits of Grom'gar")
		intros.append("the iron-forged labyrinth of Warstone")
	elif race == "Fiend":
		intros.append("the infernal depths of the Abyss")
		intros.append("the cursed Dungeons of Eternal Torment")
	elif race == "Celestial":
		intros.append("the inside of a Holy Relic")
	elif race == "Undead":
		intros.append("the shadowed tomb of Endless Night")
	elif race == "Dragon":
		intros.append("the Forgotten Dungeon, enchanted in a deep sleep that lasted an Age")
	elif race == "Dwarf":
		intros.append("the stone-carved prison deep within Mountain Halls")
	elif race == "Human":
		intros.append("the Catacombs, the most secure prison of the Empire")
	elif race == "Construct":
		intros.append("the cold, clockwork chambers of a forsaken foundry, long after it's constructor's death")
	elif race == "Fey":
		intros.append("the twisting, ever-shifting Maze of the fae realm")
	elif race == "Goblin":
		intros.append("the grim underground Warrens of the Goblin Horde")
	# Add more race-specific cases as needed

	# Archetype-specific prison options:
	if "wizard" in archetype or "mage" in archetype:
		intros.append("the arcane cell beneath the Tower of Secrets")
		intros.append("the mystic prison of Enchanted Chains")
	elif "warrior" in archetype:
		intros.append("the Slave Pits")
	elif "rogue" in archetype:
		intros.append("the Shadowed Vault")

	# Generic options (always available):
	intros.append("the Labyrinthine Dungeons hidden beneath the Forgotten Fortress")
	intros.append("the Ancient Catacombs lost to time")

	return intros


def Fallen():
	intros = [
		"Once honored defenders of the <KINGDOM> against <DREAD>, <NAME> and <PRONOUN> brethren would eventually become an even greater threat to <KINGDOM>, and were defeated only by <DEFEATED_BY>.",
		"In a bygone era, <NAME> and <PRONOUN> loyal companions stood as stalwart protectors of <KINGDOM> against the terror of <DREAD>, until betrayal and defeat against <DEFEATED_BY> brought their fall from grace.",
		"Long revered as champions of <KINGDOM>, <NAME> and <PRONOUN> kin once vanquished the forces of <DREAD>, yet their honor was shattered by the cunning of <DEFEATED_BY>.",
		"Before their fall, <NAME> and <PRONOUN> comrades were the beacon of hope for <KINGDOM>, triumphing over the might of <DREAD>; however, the relentless schemes of <DEFEATED_BY> ultimately brought them to ruin.",
		"In ages past, <NAME> and <PRONOUN> esteemed order defended <KINGDOM> against the onslaught of <DREAD>, only to be overthrown by the treachery of <DEFEATED_BY>, leaving their legacy in tatters.",
		"Once the illustrious defenders of <KINGDOM> who repelled the dread forces of <DREAD>, <NAME> and <PRONOUN> band fell from favor when <DEFEATED_BY> exploited their greatest weakness."
		]
	return intros
