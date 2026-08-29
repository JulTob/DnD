"""Official 2024-format Background records from Lorwyn."""

from AtlasLusoris.AtlasOfBackgrounds.OfficialBackgroundsKit import (
	Register_Backgrounds,
	)
from AtlasLusoris.Grimoire_of_Backgrounds import (
	Background,
	)

SOURCE_TITLE = 'Lorwyn: First Light'
SOURCE_URL = 'https://www.dndbeyond.com/sources/dnd/lfl'
SOURCE_LOCATOR = 'Chapter 1: Lorwyn-Shadowmoor Origins — Backgrounds'

RECORDS = (
	Background(
		name='Destined',
		description=(
			'You are destined for greatness. You know it.\n\nYou were told. A sprite told you, or your loving brother did, or an old woman by the road who knew your name before you gave it. There is a court somewhere missing an heir. A crown that fits only you. A prophecy with a gap exactly your shape.\n\nSo you left. Obviously you left. A destiny does not come to a village and knock; you go out and meet it, cheerfully, at considerable expense. You are strong, you are healthy, you can walk further than anyone else in the party, and you glow. An actual aura of light surrounds you on command! That is irrefutable proof that you are destined by a star. Nobody has ever proved otherwise, and you have noticed that people stop laughing about it the moment the dark closes in and you are the only one confident enough to face it.'
			),
		abilities=('STR', 'CON', 'WIS',),
		origin_feat='Aurora',
		skills=('Athletics', 'Nature',),
		tools='Cartographer_Tools',
		roleplay=(
			'**Born Under a Star.** Things arrive. A ring in the gutter. A key with no door. A letter addressed to a place you happen to be going. Signs of the road you must take. And people run into you in the street. They always have. A woman who has lost something, a man who owes something, a boy who has run from something, and every one of them looks at you and says a version of the same sentence: you are the one who can help me. They are usually right, which you take as further evidence, and you say yes before they have finished asking. You say yes every time. That is the cost, though you would never call it one. The stars always reward you for doing the right thing, marking your path. Every stranger is the prophecy and every errand is the road to your great destiny, so you cannot tell the one that matters from the forty that do not, and you have never once left a town by the road you meant to. Everything happens for a reason.'
			),
		),
	Background(
		name='Fated',
		description=(
			"You are cursed. You know it.\n\nEverybody agrees. A gnome told you, or your mean brother did, or an old woman by the road who knew your name before you gave it. You break things. Not carelessly, and not always by touching them: a rope you did not tie gives way, a bridge holds for four people and not for you, milk spoils as you touch the glass.\n\nThen you heard the rumour: you were promised to a witch, or a demonic entity, or a dark god. It is coming for you. In the meantime everything near you goes slightly wrong, and that is undeniable proof. You took that rather well, because there is a freedom in a settled account: nothing you do can make it worse, so you may as well do as you like. If you fall, you roll over and jump back up. If you break a mirror, you make a new one even fancier. It's not so bad all the time. You may jinx something every day, so you have learned to aim it at the bad guys. Because your fate is set, why not go out there and see the world? If a witch is going to sacrifice you, it will have to find you first, and with luck you will cheat it by dying in a dungeon instead. Who knows? Let's find out."
			),
		abilities=('DEX', 'INT', 'CHA',),
		origin_feat='Jinx',
		skills=('Acrobatics', 'Deception',),
		tools='Glassblower_Tools',
		roleplay=(
			'**Star-Crossed.** Things arrive. A ring in the gutter. A key with no door. A letter addressed to a place you happen to be going. Marks of a fate you share. And people run into you in the street. They always have. A woman who has lost something, a man who owes something, a boy who has run from something, and every one of them looks at you and says a version of the same sentence: you are the only one who can help me. They mean that exactly as it sounds. They have asked everybody else first. You say yes every time. That is the cost, and you know precisely what it is. The stars always punish you for refusing, marking your path. There is nobody coming after you and no second person to ask. And the ones who find you found you because they are as unlucky as you are, and misery loves company.'
			),
		),
	)

def Register_Lorwyn_Backgrounds(
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
	"Register_Lorwyn_Backgrounds",
	)
