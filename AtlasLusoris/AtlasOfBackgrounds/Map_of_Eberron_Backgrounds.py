"""Official 2024-format Background records from Eberron."""

from AtlasLusoris.AtlasOfBackgrounds.OfficialBackgroundsKit import (
	Register_Backgrounds,
	)
from AtlasLusoris.Grimoire_of_Backgrounds import (
	Background,
	)

SOURCE_TITLE = 'Eberron: Forge of the Artificer'
SOURCE_URL = 'https://www.dndbeyond.com/sources/dnd/efota'
SOURCE_LOCATOR = 'Chapter 2: Character Options — Backgrounds'

RECORDS = (
	Background(
		name='Aberrant Mutant',
		description=(
			"""There is a word for what you are: Aberration. 
			
You did not ask for what happened. It came like a crack that broke the life you had. People look at you scared. They are not entirely wrong.

So you learned to hide the signs, and when you couldn't, to leave with nobody daring to move first. You know how to keep it shut. To keep it inside. To never let it out. To never look inside, and never look away either. To not hurt anyone else again. But it always finds a way out. The life of an aberration is to be hunted."""
			),
		abilities=('STR', 'CON', 'CHA',),
		origin_feat='Mutant Aberration',
		skills=('History', 'Intimidation',),
		tools='Disguise_Kit',
		roleplay=(
			'''**Personal Weapon.** They promised a cure. Then they decided you were useful.
Training had rules. You are dangerous. You are property. You do not get to want things. You do not deserve to walk free. A weapon is not allowed friends, because everything a weapon does is hurt, kill, destroy. They were not entirely wrong. That is the worst of it.

You had to leave. They are still looking: patient, well funded, and getting closer. The next hunter is always tracking you down. They will come at you through the people around you. They will come through whoever stands beside you. Your companions are safer not knowing your name, and safest not knowing you at all. 

But... you breathe deeper, and you go where you like, and you stop to smell the roses, and you put your hands in cold streams. You are the one deciding your life. You would always rather be hunted than kept.'''
			),
		),
	Background(
		name='Archaeologist',
		description=(
			"The gold is the least interesting thing in this job.\n\nIt is arithmetic. A gold cup buys you one good year. An accurate account of where that cup stood, what lay around it, which way the body was facing and what was cut above the door, buys you the rest of your life: the next expedition, the letter of introduction, the archive that opens for you and stays shut for everybody else. Loot gets spent. A record will make you the reference.\n\nSo you made yourself into the instrument that carries the record home. You can reach places nobody sensible wants to go, and, far more importantly, get out of them again, which is the part the stories always skip. You have crossed country that kills people who packed badly. You have gone through a window at speed with a lamp in your teeth. You have talked past a border guard in a language you started learning two weeks earlier on the road. You know how a site should be entered so that it can still be read afterwards, and you know when to turn around and leave one, which is a skill nobody has ever thanked you for and the reason you are still alive.\n\nAnd you draw. All of it, every hour: the route in, the elevation, the chamber, the marks on the lintel copied exactly, including the ones you cannot read yet. Half your work happens afterwards by lamplight, with a pen, and it is the half that lasts.\n\nYou are not a scholar who travels. You are a traveller who reads. That difference has kept both sorts of people at arm's length from you your whole life, and you stopped minding a long time ago."
			),
		abilities=('DEX', 'INT', 'WIS',),
		origin_feat='Skilled',
		skills=('History', 'Survival',),
		tools='Cartographer_Tools',
		roleplay=(
			'**A Piece of the Artifact.** It is not you they want. It is what you are carrying. Everyone has heard of the thing: the drowned city, the sealed ark, the grail nobody ever found. All of it is legend, and most of the legend is nonsense. But you, and only you, carry the key to the real one, and it is in your pack: a fragment of a disc cut with the cipher, a map with the place still unmarked but close enough, or a journal you filled yourself over eleven years, corrected, argued with, and useless to anyone who cannot read your hand. That is what opens doors. A patron who would not have given you an hour clears an afternoon. A private collection unseals. A captain agrees to the southern passage in the wrong season. None of them are impressed by you. They have been shown a fragment, they want the rest, and they will pay for the privilege of standing there when it is used. And because it is the thing they want and not you, you are the part of the arrangement that is not necessary. Some are patient and rich. Some have been at it three generations and consider it theirs by inheritance. All of them know the shortest way to the Artifact runs through you: the polite route, or the persuasive one. Either way, you are the one who decides whether it ends in its rightful place, in a museum, or in your own private vault. If you live that long.'
			),
		),
	Background(
		name='Debunker',
		description=(
			"There is always a reasonable explanation.\n\nYou have made a modest living out of that sentence. The lights over the marsh are gas, the bleeding statue is rust and rainwater, and the medium's table lifts because of a very strong left knee.\n\nYou are good at this. Half the work is knowing that a wizard with guano and charcoal is not calling down fire but making powder. The other half is being willing to investigate for six hours to prove it. You have opened a hundred and one cases and closed a hundred, one at a time, and every one of them made the world a little more reasonable. Then there was the other one.\n\nYou did what you always do. You checked the flue, the cellar, the floorboards, the family, the will. You reached up to take the mask off, the way you have a hundred times before, and there was no mask, and your hand kept going.\n\nYou still tell people it is always explainable. It is. But the explanations can keep you awake."
			),
		abilities=('STR', 'INT', 'CHA',),
		origin_feat='Lucky',
		skills=('Investigation', 'Persuasion',),
		tools=(),
		roleplay=(
			'**Fellow Cranks.** You are not alone, exactly. You are alone in any particular town, but there is a loose and quarrelsome web of people like you, and it reaches further than it has any right to. An apothecary with a drawer full of cuttings. A lamplighter who has mapped the three streets where dogs will not walk. A widow with forty years of notes in a hand nobody else can read. A bored clerk in a records office who copies out the strange ones for his own amusement. Most of you have never met. All of you write. Arrive anywhere and you can turn up the local one inside a day, because cranks recognise each other on sight. They will give you everything: what happened, when, who saw it, who is lying about it, and what the constable was paid to write down instead. They have been watching this town for years and not one person has ever asked them a single question about any of it. Ask, and you will not get them to stop. The price is that they are cranks. So are you, and you know exactly what that is worth. Perhaps one letter in twenty is a real observation. The rest is an eclipse, a fox, a grudge against a neighbour, or a lonely person who worked out that a good story brings a visitor. You sort it yourself, and sorting takes time you do not always have. And none of it counts. Not to a magistrate, not to a temple, not to anyone with the power to act. Your evidence is a heap of letters from people the world has already decided are unwell, collected by someone the world has decided the same about. When you are wrong, that is fair enough. When you are right, it is the worst thing about your life.'
			),
		),
	Background(
		name='Inquisitor',
		description=(
			"You have seen what comes through when a seal fails. Nobody who has seen it argues.\n\nThat is the beginning and the end of your faith. Not the singing, not the incense, not the long words. You have stood in a room where something wore a person like a coat and used their mouth to say your name, and you put it down, and the village slept that night because you did. The gods keep a right hand for blessing and a left hand for this. You are the left. You made peace with the arithmetic a long time ago: some things have to be ended, the ending is filthy work, and it falls to somebody.\n\nSo you were taught. Which of the dead walk and which are only grief. Which contracts bind and which are boasting. Which marks cut into a doorframe are a ward and which are an invitation. You knew the seventy-two sealed names before you were old enough to shave.\n\nYou carry your own account as well. You have done penance you will not describe, for a reason you do not say aloud, and something got into you along the way that has not entirely left. You are not a good person. You never claimed to be. You are an instrument, and an instrument does not need to be clean, only sharp.\n\nAnd still. There was a child. Your superior looked at her once and named her, and she burned, and she screamed the whole time in a voice that was hers and nobody else's. Iron blistered her hands, which is in the book. Some people are simply born unable to touch iron, which is in another book. You have read both pages more times than you can count. Your superior had read neither, and said what they always said: send them on, the gods will know their own.\n\nYou still believe. That is the part nobody outside ever understands. You believe, and you keep working, and you do not sleep well."
			),
		abilities=('CON', 'INT', 'CHA',),
		origin_feat='Alert',
		skills=('Insight', 'Investigation',),
		tools='Thieves_Tools',
		roleplay=(
			"**Chapter and Verse.** Any temple with a roof will give you a bed and feed you, and nobody asks how long you intend to stay. That is not hospitality. It is what you are owed, and what they would rather not be caught refusing. You get the room at the end of the corridor, and the door closes a little too quickly behind you. Then, some time after dark, somebody knocks. They always come. The woman whose neighbour has not eaten at his own table since spring. The father whose daughter's window is open every morning and he knows he shut it. The sexton who has counted the graves twice and got two different numbers. Frightened people tell you everything, including what they have never said to their own family, because you are the one person who will not laugh, and because you are the one who was sent to be told. And you can answer them. You were given the whole shelf: the seventy-two sealed names and what each of them wants, the were-bestiary with its notes on silver and rue and the turning of the moon, the tables of which dead rise and which merely lie there, the accounts of every contract anyone survived long enough to record. When a thing has a name, you know the name. When it has a rule, you know the rule. If it was written down anywhere, you can send for it and it will come. Nobody writes in the margin whether any of it is true. The book was made by people who were frightened too, who set down what they believed had worked, and who were not always alive afterwards to correct it. Salt, iron, running water, a name said backwards. Some of it is the gathered wisdom of centuries. Some of it is a rumour copied out so many times it hardened into scripture. You will not learn which is which until you are standing in front of the thing, at night, with the page in your memory and no time to check it."
			),
		),
	)

def Register_Eberron_Backgrounds(
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
	"Register_Eberron_Backgrounds",
	)
