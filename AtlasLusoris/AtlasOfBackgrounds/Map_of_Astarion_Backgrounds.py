"""Official 2024-format Background records from Astarion's sourcebook."""

from AtlasLusoris.AtlasOfBackgrounds.OfficialBackgroundsKit import (
	Register_Backgrounds,
	)
from AtlasLusoris.Grimoire_of_Backgrounds import (
	Background,
	)

SOURCE_TITLE = "Astarion's Book of Hungers"
SOURCE_URL = 'https://www.dndbeyond.com/sources/dnd/aboh'
SOURCE_LOCATOR = 'Character Options — Backgrounds'

RECORDS = (
	Background(
		name='Gambler',
		description=(
			'Gambling has nothing to do with luck.\n\nLuck is what the mark calls it later, when he is explaining himself to his wife. You were counting. You were watching his hands, his collar, and the exact second he stopped enjoying himself. You can tell three beats early when a man is about to double down.\n\nThe cards still turn. They always turn. That is when the second trade starts, and the second trade is people. You get staked. You get forgiven. You get dealt back in by men who swore last time was the last time, because you were charming about it, and because they want to see how this one ends.\n\nYou have been rich. Twice in one night you have been nothing. You stood up smiling both times. Standing up smiling is the job. The cards were never the job.'
			),
		abilities=('DEX', 'INT', 'CHA',),
		origin_feat='On a Roll',
		skills=('Deception', 'Persuasion',),
		tools='Gaming_Set',
		roleplay=(
			"**Markers.** Credit finds you. Walk into any town with a back room and somebody will stake you on your face alone, because your face is good and everybody has heard something. You owe them big. Somewhere in a drawer there is paper with your name on it and a number that has never once got smaller. And markers get called. Never in coin. Coin is what people ask for when they have no imagination. There is a thing wants fetching out of somewhere unpleasant. A name wants carrying where it should not go. An evening's work nobody will admit to paying for. There is a job with your name on it, and you will take it, because of what happens to the ones who do not, and because you have never in your life left a table before it was finished."
			),
		),
	Background(
		name='Servant',
		description=(
			'Power can last only in a strong dynasty. Your masters held power for as long as there was a country to rule. And that power is always hungry.\n\nYou served, and listened. When your survival depends on their tastes, you listen: a difficult year. Insufficient body. Charming, but it will not keep. Something young and red, and frankly wasted on the occasion. You stood at the sideboard with the decanter and learned the entire register: what travels, what wants laying down, what improves with keeping and what merely goes on. Nobody was ever crude. Not once did anyone say a mean word to you. They discussed the guest list the way one discusses a cellar, and they were delighted, and they were generous with their compliments, and you poured.\n\nYou were just old enough. The terms were generous: a bed, a wage, and the word of a great house, which is worth more than either. They paid you to keep you. And you supplied, and filled their cups. Not cruelty. Arithmetic. Survival.\n\nEvery night you prepared a banquet for the guests. Every night you cleaned up after. But the stench and stains of iron and wine rarely vanish. You knew where the silver was hidden, and the guests left generous tips. You were not brave enough to free the world of their tyranny. But you were brave enough to say enough. You ran away. It was easy. Too easy.\n\nYou got out. But then you heard it all again, coming from inside you. “Dear, my cup is empty... and I am thirsty.”'
			),
		abilities=('STR', 'CON', 'CHA',),
		origin_feat='Cupbearer',
		skills=('Persuasion', 'Stealth',),
		tools='Cook_Utensils',
		roleplay=(
			'**Indentured.** You are out. You think so. You want to. Whether you were released, or merely reassigned, is a question you have decided not to hold up to the light. But the masters still have a hold on you. The channel did not close. The debt was never settled. And yet they allow this. A letter reached you, and with it the signet of the house, yours to use in their name: it opens doors that were never going to open, closes others for good, and teaches everyone who sees it something about you that you would rather they did not know. Instructions came with it. They said they were happy for you, happy you had found your calling. But it arrived in a tavern you had not known you would stop at, in a room with the door shut, and it was lying on top of you. The message was clear. They still own you. They will allow this, and it is not something you can get out of your head. You still receive orders. Follow the instructions, they say, and you will buy your freedom. And if you do not... well. You had better, darling.'
			),
		),
	Background(
		name='Exorcist',
		description=(
			"It is always the same job, whatever they called it in the letter.\n\nA demon. A devil. A thing from under the sea. A spore. A bite. A very persuasive man with a book. Every one of them wants the same thing: for somebody to stop being a separate person and start being part of something... bigger. You have spent your working life on the other side of that argument, and you have noticed, with some interest, that the procedure is much the same whether it is a fiend or a philosophy.\n\nYou don't need to be devout. You use what works, and what works is always liturgical: salt, iron, running water, the right words in the right order, which you do not even have to mean. You have tested all of it. Half the book was wrong. You kept the half that wasn't, and you charge for it."
			),
		abilities=('DEX', 'CON', 'WIS',),
		origin_feat='Hard to Hold',
		skills=('Insight', 'Religion',),
		tools='Woodworker_Tools',
		roleplay=(
			'**House Calls.** You are in the book. Not a holy book, the other kind: the one behind the bar, the one the parish clerk keeps, the list of people you send for when something has gone wrong in a house and nobody wants to say what. Word travels in a very particular way, which is quietly, and it travels far. So there is always work, and you set the rate. A family that has spent three months pretending nothing is happening will pay up on the day they stop pretending. You get let into houses that would never open for a magistrate, and told things that would never be said to a priest, because you are neither, and because you have already seen worse. But most things like this do not think one at a time. Whatever you cut out of a person had somewhere it belonged, and it went back, and now knows your face and your rate. Every job you finish makes the list of creatures that hate you longer. They always grab you. You have been held by a great many things. You have never yet stayed held. And you are aware that this is a record and not a guarantee.'
			),
		),
	)

def Register_Astarion_Backgrounds(
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
	"Register_Astarion_Backgrounds",
	)
