"""Official 2024-format Background records from Forgotten Realms."""

from AtlasLusoris.AtlasOfBackgrounds.OfficialBackgroundsKit import (
	Register_Backgrounds,
	)
from AtlasLusoris.Grimoire_of_Backgrounds import (
	Background,
	)
from AtlasVenustas import (
	Entry,
	)


SOURCE_TITLE = "Forgotten Realms: Heroes of Faerûn"
SOURCE_URL = "https://www.dndbeyond.com/sources/dnd/frhof"
SOURCE_LOCATOR = "Character Options — Backgrounds"

RECORDS = (


  
	# Based on the Background Chondathan Freebooter
	# source: Forgotten Realms: Heroes of Faerûn
	Background(
		name="Vagabond",
		abilities=(
			"STR",
			"DEX",
			"WIS",
			),
		skills=(
			"Athletics",
			"Sleight_of_Hand",
			),
		tool="Weaver_Tools",
		origin_feat="Skilled",
		description=(	
          """The road raised you, and you never learned to stay put. You drift into a new town like you own it: easy, curious, quick to make a friend and quicker to make an exit. The day a place starts to feel like a cage, you're already gone, chasing one more horizon.

 """
			),
		hook=Entry(
			title="Bearer of News",
			definition="Everyone wants to know what's happening beyond their own walls. Wherever you go, folk seek you out to hear gossips, rumors, and to press a letter or message into your hands. People see you as trustworthy, and you can almost always trade the news you carry for local gossips, information about the place, or even a secret, and a message you agree to deliver gets you a warm welcome at journey's end.",
			),
		),



  
	# Based on the Background Dead Magic Dweller
	# source: Forgotten Realms: Heroes of Faerûn
	Background(
		name="Survivalist",
		abilities=(
			"STR",
			"CON",
			"WIS",
			),
		skills=(
			"Medicine",
			"Survival",
			),
		tool="Leatherworker_Tools",
		origin_feat="Healer",
		description=(
			"Rescue never came, so you learned to be your own. You read the "
			"land for water and game, patch your gear from hide and sinew, and "
			"set a broken bone by feel when there's no one else to do it. "
			"Comfort is a stranger — but getting by on nothing is a craft "
			"you've long since mastered."
			),
		hook=Entry(
			title="Field Triage",
			definition="During a rest, an ally you tend can spend one of your Hit Dice to heal, as if it were their own. Once you do this, you can't again until you finish a Long Rest.",
			),
		),
	# Based on the Background Dragon Cultist
	# source: Forgotten Realms: Heroes of Faerûn
	Background(
		name="Dragon Cultist",
		abilities=(
			"DEX",
			"CON",
			"INT",
			),
		skills=(
			"Deception",
			"Stealth",
			),
		tool="Calligrapher_Supplies",
		origin_feat="Dragon Cult Initiate",
		description=(
			"You were raised in the hush of a hidden shrine, taught that "
			"dragons are the world's true and rightful powers — and that you "
			"serve one. Whether your wyrm is a tyrant to be feared or a "
			"guardian to be revered, you learned its secret signs, kept its "
			"ciphered scriptures, and moved unseen among those who would "
			"never understand the fire you carry."
			),
		hook=Entry(
			title="Secrets of the Dragon Master",
			definition="You are initiated into a secret organization that follows a powerful Dragon. But where most people picture a gigantic lizard, you know better: Dragons walk among mortals, wearing humanoid bodies and beautiful visages, playing a never-ending game of chess with the peoples of the realm. You are just a pawn, but you can access the vast knowledge of your Draconic Master. Through a cryptic ritual meditation, you may contact your Master (or other initiated cultists you have met in person) and consult their knowledge. Information is precious and hazardous, so you may not yet be ready to learn every secret — but you know the Cult is focused, above all, on other Dragons: their whereabouts, their hoards, their lairs, their humanoid identities... Your responsibilities to your Draconic Master may be burdensome, but the power you may gain is limitless, hidden behind their secrets.",
			),
		),
	# Based on the Background Emerald Enclave Caretaker
	# source: Forgotten Realms: Heroes of Faerûn
	Background(
		name="Wildkeeper",
		abilities=(
			"CON",
			"INT",
			"WIS",
			),
		skills=(
			"Nature",
			"Survival",
			),
		tool="Herbalism_Kit",
		origin_feat="Wildwarden",
		description=(
			"""You did not tame anything. You stayed. Season after season in one wild place: a wood, a marsh, a valley, a stretch of coast where the fog comes in by noon... Until it stopped treating you like weather and started treating you like a neighbour. You know which water is safe in a dry year, which root brings a fever down and which one you never touch, where the deer go when the snow comes and why they stopped going there. And somewhere in all that quiet you learned to truly listen, until the crows and the foxes and the old boar under the hill began to answer, and it turned out they had been complaining about you for years. You have buried animals you loved. You have sheltered both fox and rabbit in your hut through an especially hard winter, and all of you parted as friends. You do not think of the place as yours. If anything, it is the other way around."""
			),
		hook=Entry(
			title="Speaker for the Wild Things",
			definition="The wild has no voice in civilization, so it asks for yours. Wherever there is green country, the inhabitants of it will find you: a magpie with a complaint, a village dog that has decided to retire from hunting and wants to shepherd, an old badger who wants something done about the diggers on the ridge, a rookery of penguins presenting a formal grievance, a whale that has stopped singing and will not start again until somebody listens. What they bring is never tidy and never official (a spring gone sour, a track of dead things leading somewhere nobody goes, animals leaving a valley all at once, a stranger in the woods who smells like death), and it always reaches you first, because you are the one they trust. Country folk who work the land know your kind on sight, and they come to you when something is wrong: a herd that will not settle, a blight in the barley, whatever has been coming down out of the trees at night. Nobody appointed you. You are simply the one who is listening.",
			),
		),
	# Based on the Background Flaming Fist Mercenary
	# source: Forgotten Realms: Heroes of Faerûn
	Background(
		name="Sellsword",
		abilities=(
			"STR",
			"CON",
			"CHA",
			),
		skills=(
			"Intimidation",
			"Perception",
			),
		tool="Smith_Tools",
		origin_feat="Tough",
		description=(
			"You never fought for a flag, only for a fair price and the "
			"good name that brings the next contract. Guard work, siege "
			"lines, ugly little wars: danger became just another day's "
			"labor. You keep your blade honed and your armor sound, read a "
			"room for the first flicker of trouble, and let a hard look do "
			"the talking long before steel has to."
			),
		hook=Entry(
			title="The Next Contract",
			definition="Wherever blades are for hire, your reputation travels ahead of you. In any town of decent size you can find where sellswords drink and fixers broker deals, and turn up honest paid work: a caravan that needs guarding, a patron hiring muscle for a quiet job, or an old comrade willing to stand at your back for a share. The coin is real and so is the danger, and a name earned at swordpoint calls in old debts as often as new offers.",
			),
		),
	# Based on the Background Genie Touched
	# source: Forgotten Realms: Heroes of Faerûn
	Background(
		name="Fortune Teller",
		abilities=(
			"DEX",
			"WIS",
			"CHA",
			),
		skills=(
			"Perception",
			"Persuasion",
			),
		tool="Glassblower_Tools",
		origin_feat="Magic Initiate (Wizard)",
		description=(
			"You tell fortunes for a living — palms, cards, the drift of "
			"smoke inside a glass orb you blew yourself. Most of it is craft: "
			"a sharp eye for the hope or fear a stranger walks in carrying, a "
			"patter that hands them back their own secrets dressed as "
			"prophecy, fingers quick enough to keep the trick invisible. But "
			"not all of it. Every so often a vision arrives unbidden and "
			"turns out true, and even you cannot say how you knew. You have "
			"learned not to argue with an omen when it points — and the last "
			"one pointed you out the door, onto the road, toward whatever you "
			"are walking into now."
			),
		hook=Entry(
			title="Reading of the Signs",
			definition="You can read the fortune of a willing creature other than yourself. Over ten minutes — laying the cards, gazing into your glass, letting the pendulum swing — you draw a single sign and nothing more: a symbol (the Tower, the Lovers, the Death card), a sound (a raven's caw, a bell no hand has rung), a sensation (a sudden grave-cold in the air), or a truth of the heart before you (they are afraid; they grieve; they hope against all reason). The DM gives you the sign, never its meaning — the meaning is yours to divine. It is never plainly spoken and never false; yet whether the sight is true foresight or only a sharp read of the soul before you, not even you can say. You can read a given creature only once until it finishes a Long Rest. The one fortune you can never lay out is your own.",
			),
		),
	# Based on the Background Harper
	# source: Forgotten Realms: Heroes of Faerûn
	Background(
		name="Revolutionary",
		abilities=(
			"DEX",
			"INT",
			"CHA",
			),
		skills=(
			"Performance",
			"Sleight_of_Hand",
			),
		tool="Disguise_Kit",
		origin_feat="Agitator",
		description=(
			"You learned young that a song can do what a sword can't: fill "
			"a room with courage, then empty it into the streets. You speak "
			"for the people who have none — in taverns, in back rooms, on a "
			"crate in the market square — and a folded pamphlet finds a "
			"stranger's palm without your hands ever seeming to move. When "
			"the watch comes, you are already someone else, three alleys "
			"away. The cause has cost you a home, a name, a friend or two; "
			"it has never once cost you the belief that the world can be "
			"remade."
			),
		hook=Entry(
			title="The Cause",
			definition="Wherever people suffer under a boot, some of them are ready to push back, and they know your kind on sight. In any town you can find the cause's sympathizers: they will hide you, feed you, and carry your words where you cannot go. From them you learn who truly holds the town and who chafes under them, and there is always a local wrong they will beg you to help set right. Their aid is real but costly to give — every hand that shelters you risks the gallows for it.",
			),
		),
	# Based on the Background Ice Fisher
	# source: Forgotten Realms: Heroes of Faerûn
	Background(
		name="Ice Nomad",
		abilities=(
			"STR",
			"DEX",
			"CON",
			),
		skills=(
			"Animal_Handling",
			"Athletics",
			),
		tool="Woodcarver_Tools",
		origin_feat="Alert",
		description=(
			"""Your people do not stay; they follow: the herds, the thaw, the old roads worn into the ice by generations of runners and sleds. You were born to the long cold and the long march: keep the animals alive, keep moving, keep watch, and carry nothing you can't carry yourself. You shape your own sled and tools by feel, and warmth and walls mean little to you. When your band scattered (or you chose a road of your own), the ice let you go, and every land since has felt thin and overwarm."""
			),
		hook=Entry(
			title="Nothing Wasted",
			definition="Your people turned scraps into survival, and so can you. Given enough time and rough raw materials (bone, driftwood, hide, sinew, or packed snow), you can make the gear the cold demands: shelter from the storm, a sled runner, a patched harpoon. It is never pretty, but it keeps you and your companions alive where the unprepared simply die.",
			),
		),
	# Based on the Background Knight of the Gauntlet
	# source: Forgotten Realms: Heroes of Faerûn
	Background(
		name="Guardian",
		abilities=(
			"STR",
			"INT",
			"WIS",
			),
		skills=(
			"Athletics",
			"Medicine",
			),
		tool="Smith_Tools",
		origin_feat="Bastion",
		description=(
			"""You learned to be the thing that does not break. Whether you served a sworn order, a city watch, or a village that had no one else, the lesson never changed: put yourself between the weak and the blow, hold when others run, and mend what the fighting breaks. You drill until standing firm is instinct, keep your own gear sound, and have set more bones than you can count. Let the reckless chase glory. You would rather be the reason someone lived to see the morning."""
			),
		hook=Entry(
			title="The Last Line",
			definition="Trouble finds you. Or rather, the people fleeing it do. Wherever you go, the frightened and the cornered seem to know at a glance that you will stand for them: a hunted stranger begging sanctuary, a hamlet with no one left to defend it, a child who takes your hand because you look like safety. You can always turn them away, but you were made to be the wall between the weak and the wolves, and word of a protector spreads as fast as word of a threat.",
			),
		),
	Background(
		name="Herald",
		abilities=(
			"STR",
			"INT",
			"CHA",
			),
		skills=(
			"Insight",
			"Persuasion",
			),
		tool="Calligrapher_Supplies",
		origin_feat="Banner Bearer",
		description=(
			"""You are the mouth and the hand. A herald carries power that is not their own: a council, a temple, a patron, a forest... They chose you. Out of everyone they could have sent. And you may still wonder why. They send you where an army cannot go: your word opens gates that stay barred to soldiers, and you walk in alone, past the guards, into the room where the thing is decided. A herald who can be dismissed is worse than no herald at all, so you made yourself impossible to overlook. In any room you can tell who is listening, who is stalling, and who decided the answer before you walked in. If the talking works, you carry the treaty out, and everyone who wanted the war knows what is in your satchel. If the talking fails, you are already inside their lines, and you are the first blade they meet. Either way, it comes home with you or it does not come home at all. Any means necessary."""
			),
		hook=Entry(
			title="Words and Actions",
			definition="Speak the name of your power and you can demand parley: an audience with a ruler, a commander, a high priest, or whoever speaks for them. They will hear you out, because harming a herald is how small quarrels become wars. In exchange, when your power sends for you, you go. You are asked more than anyone should be: taking out threats, communicating with a secret source, or even retrieving a precious artifact for the cause. You have to do anything your power requires of you. Some errands are honorable. Some are not. If you are caught, you may not enjoy your immunity any longer.",
			),
		),
	Background(
		name="Naturalist",
		abilities=(
			"CON",
			"WIS",
			"CHA",
			),
		skills=(
			"Nature",
			"Performance",
			),
		tool="Painter_Supplies",
		origin_feat="Magic Initiate (Druid)",
		description=(
			"""You did not want to read about it. You wanted to see it. So you went: up the scree in bad weather, into the fen at the hour the things you were after come out, down to a shoreline nobody had bothered to name, with a board across your knees and the light already going. Half of what you have catalogued has bitten you at least once. You paint fast, because nothing holds still and the weather never cooperates, and you have learned to draw a thing accurately enough that someone who has never seen it would know it anywhere. And you can make people care: give you a crowd and a specimen and you can hold them for an hour explaining why a beetle matters, why the river changed, what the shape of a wing is for. Somewhere along the way, from watching too closely for too long, you picked up a little of what you were studying. You still cannot say how. That is the trouble with the natural world: it does not stop at the edge of the page."""
			),
		hook=Entry(
			title="Field Notes",
			definition="There is a scattered guild of people who care what you have seen: apothecaries, alchemists, private collectors, colleges with empty display cases, and wealthy eccentrics who will pay absurdly for a thing nobody else owns. Your plates and your notes are currency among them, and so is whatever you carry out of the field. A dragon's fang, a moulted celestial feather, spores from a fungus that grows in one cave in the world: what is left on the ground after a hard night is, to the right buyer, a spell component, a medicine, or the centerpiece of a collection. They pay, and they commission: a specimen of this, a drawing of that, proof that the thing the villagers keep describing is real. And somewhere out there is a creature nobody has ever drawn, which is precisely the kind of rumor that gets people killed.",
			),
		),
	Background(
		name="Tomb Raider",
		abilities=(
			"DEX",
			"CON",
			"INT",
			),
		skills=(
			"Investigation",
			"Religion",
			),
		tool="Mason_Tools",
		origin_feat="Lucky",
		description=(
			"""The tomb was sealed for a reason. You went in anyway. You read dead languages by torchlight while something shifts in the chamber ahead, and you know the gods of the underworld by name, which is useful, because in your line of work they come up. You have seen what happens to a man who reads the wrong passage aloud, and you have read it aloud anyway, because the alternative was the ceiling coming down. You know stone: which slab is a counterweight, which floor is a lie, which wall was built to keep something in rather than someone out. You have outrun a collapse, outlasted a curse (mostly), and been certain, twice, that you would not see daylight again. You did. Something in you insists on it. Everyone says the dead should be left in peace. Everyone is probably right. You are going back down tomorrow."""
			),
		hook=Entry(
			title="The Next Expedition",
			definition="Somebody is always funding a dig. A college with a theory, a temple that wants a relic home, a collector with more money than sense, a widow with her grandfather's map: they need someone who will actually go in, and there are not many of you. So the offers come, and the rivals with them, because the same rumor reaches three expeditions at once and only one of you gets there first. The rest arrives unasked. People bring you things they should never have picked up: an amulet that will not come off, a book that is warm to the touch, a jar whose seal somebody broke. You know the signs, the old prohibitions, and roughly what is likely to come through the door tonight, which makes you the one they send for when a crypt starts making noise. Whether you can stop it is a separate question. You have always found out the hard way.",
			),
		),
	Background(
		name="Hermeticist",
		abilities=(
			"INT",
			"WIS",
			"CHA",
			),
		skills=(
			"Arcana",
			"History",
			),
		tool="Jeweler_Tools",
		origin_feat="Crafter",
		description=(
			"""As above, so below: everything in this world answers to a greater law, and the Art of the Hermeticist and the Alchemist is knowing these laws of the arcane and the natural: the laws of correspondence. Gold to the sun, silver to the moon, iron to the red star. A stone cut on the right day and set in the right metal at the right hour does not merely decorate. It transmits something. Neither Druid nor Wizard knows of these secret arts, of metal and crystal and stone, of harvesting the power of the amethyst and the agate: the power of correspondence, not found in casting spells. Somebody initiated you into the Hermetic Art: a master with a locked cabinet, a traveling jeweler you hosted for a winter, a silent old woman working in silver to protect your village from the full moon. You have kept the tradition since, copying diagrams, runes, and circles you did not understand until the day you did. You know the great works by name and by history, every one of them, and how each was made. You understand the ciphers of nature and of the old manuals. And you know what the great secret would cost. Quinta Essentia. The Fifth Essence. The Philosopher's Stone. The one thing you still cannot produce. You will find it."""
			),
		hook=Entry(
			title="The Great Work",
			definition="Anyone can make magic items with the proper training. You have mastered it. You understand amulets, rings, and anything of metal, gem, crystal, or stone. Given the materials, the hours, and a quiet bench, you can produce trinkets of great power (you must follow the rules for Crafting Magic Items). The difficulty is never skill. It is always materials. What a true piece needs cannot be bought in a market: a scale from a silvery dragon, iron that fell out of the sky and is not cold yet, quicksilver from a spring that exists in one story and no map. So you go and get them, and others come with you, and that is how half your journeys have started. Between those, the commissions find you, because somebody always wants a thing ordinary money cannot buy: a ward for a child, a signet that cannot be forged, something to stop whatever has been visiting the house at night. And somewhere ahead is the piece you have been building toward your whole life, still missing the one component you have not yet discovered.",
			),
		),
	Background(
		name="Squire",
		abilities=(
			"STR",
			"WIS",
			"CHA",
			),
		skills=(
			"Animal_Handling",
			"Insight",
			),
		tool="Navigator_Tools",
		origin_feat="Field Lieutenant",
		description=(
			"""You served someone the songs are about. Maybe a knight, maybe an archmage, maybe the old druid the valley sent for when the river turned. Whoever they were, greatness has logistics: someone has to feed the horses, mend the tack, find the ford when the bridge is out, keep the packs dry, and know exactly how many days of food are left. That was you. You learned to read your master's silences before they spoke, and to read everyone who came to them: the petitioner who was lying, the rival smiling too hard, the boy who needed sending home before the fighting started. You saw them up close, on their worst days as well as their best, and you know the part the legends leave out. You are not them. Not yet. But you carried the gear, you kept the road, and when it came to it you stood where you were told and did not run."""
			),
		hook=Entry(
			title="In Their Name",
			definition="You carry someone else's name, and it still opens doors. Say who you served and old comrades will hear you out, quartermasters will find what you need, and people who owed your master will pay part of that debt to you, because that is how debts to the great are settled. Their enemies count the same way. And there are always obligations left unfinished: a promise your master made and cannot keep, a rival who has been waiting for them to be gone, someone who has been writing letters for two years and getting no answer. Those letters come to you now. Wherever people knew them, they will look at you and measure whether you are the real thing, or only the one who carried the bags.",
			),
		),
	Background(
		name="Stranger",
		abilities=(
			"STR",
			"CON",
			"CHA",
			),
		skills=(
			"Intimidation",
			"Perception",
			),
		tool="Cartographer_Tools",
		origin_feat="Tough",
		description=(
			"""You are from somewhere else. You will be from somewhere else for the rest of your life, and so, most likely, will your children. Something happened to the place you came from: a war, a flood, a decree, a gate that closed behind you, a thing that came up out of the sea. What survives of it survives in you: a language fewer people speak each year, a handful of songs, the way it was cooked at home, the names of people nobody here has ever heard of. You learned the roads out and the roads back, which crossings ask for papers and which guards can be talked past, because a map is not a curiosity when it is the difference between arriving and not. You learned to be spoken to badly and not answer. You also learned when not to swallow it: there is a way of standing that ends a conversation before it begins, and you can do it without raising your voice. Somewhere ahead is a place where you could finally put all of it down. You have not found it yet."""
			),
		hook=Entry(
			title="The Long Memory",
			definition="Wherever your people were scattered, some of them landed, and they will know you before you speak. A back room, a barbershop, a kitchen with the tea already poured: sit down and they will ask what you need before they ask who you are. Everyone at that table has needed it. Someday you will be asked in turn, and there is no polite way to refuse. Go and sit with the old ones. Here they are invisible: no records, no standing, waiting on grandchildren to translate them at counters. They are also the last library of a world that is being forgotten. They know the true names, the rites that were made illegal, what the pattern on your grandmother's coat actually meant, where a thing was buried the week before the soldiers came. None of it was ever written down. They will tell you, if you carry their stories. Your History. And when it turns, word crosses the network in a day: a shop burned, a permit revoked, a girl taken by men who will not show the warrant, a temple reassigned to a god this country prefers. Everyone gives what they can. What you can give is worth more than the coin they could quietly take away. You are the one who can go. You could stop, of course. Speak only their language, wear only what they wear, let the stories and the gods go quiet, and in a generation nobody would know. Some of yours have. Memories carry a weight and a pain that some cannot bear. Everyone understands. Nobody says anything to them. That is its own kind of sentence.",
			),
		),
	Background(
		name="Renegade",
		abilities=(
			"DEX",
			"INT",
			"CHA",
			),
		skills=(
			"Acrobatics",
			"Stealth",
			),
		tool="Thieves_Tools",
		origin_feat="Savage Attacker",
		description=(
			"""Nobody gave you anything. You took a corner of the world and dared them to come get it. A crew. A gang. A chapter. A family that picked itself. A few streets, a tunnel, the roofs over the market, a stretch of sewer that something older also uses and you have an understanding with. Yours now. There are rules. Yours. Nobody in the crew goes hungry. Nobody touches the people under your protection. Nobody sells out their own. Ever. Everyone knows what happens if they do. You cross a district by rooftop faster than a runner takes the street. You are through a lock before they finish arguing about the noise. You walk into a neighborhood that will lie to a magistrate for you, and nobody had to ask. And when it comes to blows you do not fight like someone who trained. You fight like someone who cannot afford to lose. Where the coin goes after, the crew's pot, a widow's hand, your own, is an argument you have had a hundred times and will have again. We might need it tonight. You might keep it tomorrow. Somebody's kid eats either way."""
			),
		hook=Entry(
			title="Free Country",
			definition="Every city has one. A squat. A rooftop. A bar that does not serve the watch. A tunnel with somebody's mark sprayed over the old ward-lines. You will find it in a day, because your kind know each other on sight: how you stand, what you clock, what you do not ask. Floor to sleep on. Somebody who knows the district. Hands for a job that needs more than two. Nothing is free, though. Free country means we pay for it ourselves. So the crew asks. They want to know everything: who your new friends are, what they carry, who they answer to, what they found down there. They want the thing in the mansion on the hill, the one with the wards and the two guards nobody has ever walked past, and they want it before the new moon. They will ask you to stand up in front of people you like and be the one who says no. And do not get too attached to that party of yours. The crew was here first.",
			),
		),
	Background(
		name="Arcane Mutant",
		abilities=(
			"CON",
			"INT",
			"CHA",
			),
		skills=(
			"Arcana",
			"Perception",
			),
		tool="Gaming_Set",
		origin_feat="Arcane Conduit",
		description=(
			"""Something in you is wrong, and it is the most interesting thing about you. Not lineage. Not study. A change, sometime, somewhere: a wild surge in the womb, a place you should not have stood in, a spark that got into you and never went out. Magic comes to you and does not pass through. You feel it before you see it, the way other people feel a storm coming in their bones: the ward across a doorway, the thing in the next room that is not breathing air, the ring somebody is wearing under a glove. When a spell hits you, part of it stays, and you have learned what to do with what stays. You have studied yourself the way a scholar studies a manuscript, because nobody else could explain you. You carry with you a game that grounds you: cards, dice, or stones. When you focus, you can always tell the result, but never whether you guessed it or caused it. It gives your hands something to do and your power something smaller to fill. Most days it works. Some mornings you find them warm, or the pips have moved, or a card you never owned is sitting on top of the deck."""
			),
		hook=Entry(
			title="What They Want",
			definition="You cannot hide what you are forever, and everyone who finds out wants the same thing: You. A guild wants you tested, measured, and replicated. A temple wants to know whether it can be cured. A collector wants you for display, and you are not sure whether that means alive or dead. Somebody's army wants a walking countermeasure. No one will take no for an answer. But there are others. There have always been others. Whatever made you has happened before: a woman who caught a lightning bolt in her bare hand, a boy his village drowned who walked away over the waves, an elder who looks the same age as you. They are hard to find, because the ones who were easy to find are gone. Find them anyway. They are the only people alive who can tell you what you are turning into, which of the stories about your kind are true, and how to survive your gift. Some will want to teach you. Some will want you stopped before you make things worse for the rest. Either way, you need someone who truly understands.",
			),
		),
	Background(
		name="Bailiff",
		abilities=(
			"STR",
			"DEX",
			"CHA",
			),
		skills=(
			"Intimidation",
			"Perception",
			),
		tool="Forgery_Kit",
		origin_feat="Strong Arm",
		description=(
			"""You served the writ, not the argument. Somebody above you decided who was guilty (a sheriff, a magistrate, a lord, a company with a charter), and you were the one who went and got them. You learned how to find a person who does not want to be found, how to walk into a room so that it goes quiet, and how a document should look, which is also how to make one look right when the file is thin and the arrest is happening anyway. You learned that a man will talk if you stand close enough and say almost nothing. You learned to watch hands. And you learned what nobody says out loud: that up close there is no oversight at all, only whoever is standing there and what they decide to do. What you did with that, and whether you would do it again, is yours to answer."""
			),
		hook=Entry(
			title="The Badge",
			definition="You carry the badge of your office: a shield, a brooch, a seal-ring, a brand, whatever mark your masters used for their own. It carries a very specific power: Authority. Move your coat aside and let a gate guard catch sight of it, and the gate opens. Let a clerk see it and the ledger comes out. Let a room see it and every conversation stops and begins again, more carefully. Most days you keep it hidden. It is worth more when it surprises, and your companions may not know you have it at all. There may be nights you would rather they did not find out. And the Badge was never really yours, but the other way around. Your superiors can call it back if you step out of line, or request a name and expect that person delivered to them, and they will somehow always know you used it, and they may not approve your methods, especially if you go soft. A badge only works while somebody behind it still has the real power to back it up.",
			),
		),
	)


def Register_Forgotten_Realms_Backgrounds(
		**routes,
		) -> tuple[type, ...]:
	return Register_Backgrounds(
		records=RECORDS,
		source_title=SOURCE_TITLE,
		source_url=SOURCE_URL,
		source_locator=SOURCE_LOCATOR,
		**routes,
		)


__all__ = (
	"Register_Forgotten_Realms_Backgrounds",
	)
