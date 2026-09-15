"""
Paladin Specializations, and the voice of the sworn.

One axis, and a Character carries one point on it: the Oath is what was sworn
*to*. There is no second axis here, and the absence is the argument. The
Warlock has a Casting Variant because a pact can answer to something other
than the person who made it. An oath cannot. It answers to the one who said
it, which is why the Guild casts on Charisma, and why nothing in these five
texts names a god.

The Guild paragraph is seated here rather than arriving from the vault, the
way the Cleric's does from Map_of_Cleric_Prayers. Mechanics stay on the Tags;
only voice lives in this module.
"""

from AtlasLusoris.GuildKit import Build_Specialization
from AtlasLusoris.GuildKit import Describe_Layer
from AtlasLusoris.GuildKit import Paladin


def _with_oath(
		paragraph: str,
		):
	"""
	The Oath paragraph with the recited oath beneath it.

	The recital is drawn once, when the Oath Spells lesson applies at level
	3, and recorded on the Character; this only reads the record. Below
	level 3 no oath has been sworn and the paragraph stands alone.
	"""
	def describe(
			character,
			) -> str:
		from AtlasLusoris.AtlasOfTraining.Map_of_Paladin_Oaths import Oath_Entry

		recital = Oath_Entry(
				character
				)
		if not recital:
			return paragraph

		return f"{paragraph}\n\n{recital}"

	return describe


# The core fantasy is **a principle held**. The oath is that principle said
# out loud, and the Character keeps it because it is theirs, not because
# anyone is listening. Documenta/Canon/Mythos/Paladin.md records the register
# and names what it must not borrow. Three neighbours are close enough to
# collide with, and each is kept out on purpose:
#
#   the Cleric    "watched over", a hand held out before you reached for it
#   the Fighter   "nobody gave you this", the yard at dawn
#   the Barbarian rage, which is emotion turned inward; the chant
#
# The Paladin is will turned outward: the will to change the world, or the
# kingdom, or one corrupt court. No celestial and no fiend stands behind the
# text, because the Character knows of none. Right makes might: the power is
# downstream of the principle, and of nothing else.
#
# **The register is the political romantic.** A Knight's tale in storybook
# aesthetic, not storybook structure; the civic speech that asks who holds
# power and answers with a person standing still. No hedging. No origin: the
# text never says what the Character saw or lost, because that story belongs
# to the player (death of the author). No rule is explained ahead of the
# rules that print it. The archetype is the paragon who acts: the activist,
# never the static protagonist.
#
# **The device is the oath recited.** The class text never quotes it. Each
# Oath paragraph below is followed by the Character's own oath, drawn by
# Map_of_Paladin_Oaths in that Oath's poets, one line by species and one by
# background, set in roman, one line each.
#
# **Alignment-independence**, completing the set the Warlock kit opened. The
# Fiend buys it with toxicity rather than malice, the Celestial with
# instrumentality, the Archfey with spectacle, the Great Old One with
# indifference. The Paladin buys it with **bindingness rather than virtue**:
# Honor, Justice and Hope are names the Character gives the dream, not
# virtues the sheet awards them, and the 2024 Oaths are alignment-free. A
# Lawful Evil Devotion Paladin is a good vassal with a bad lord, and the text
# has to fit them as well as it fits the knight in white.
#
# **Sworn and forsworn.** *Warlock* is Old English *wǣrloga*, the oath-breaker;
# in the setting's own vocabulary a Paladin who breaks the oath becomes one.
# Never say so on a sheet. It governs only how the two Guild texts end: the
# Warlock's on the terms, this one on the stand.
PALADIN_DESCRIPTION = (
	"Ask who holds power in this world and many will point you to a crown. "
	"Some will point to a temple, to a vault, or to an army camp. They are "
	"wrong. You are the standing proof of it. Power is held by whoever will "
	"stand for something true. Whoever believes. Whoever acts. Your oath is "
	"true, so you are mighty.\n\n"
	"They tell you to move. They call you a dreamer. You are. You dreamed a "
	"world that does not yet exist. This world needs it. Call it Honor. Call "
	"it Justice. Call it Hope. You will manifest your dream. So you went and "
	"stood in the one place it would have to begin: here and now. And here "
	"and now you act. You will bring forth a new world. You know what "
	"happens if you move. Justice will fall. The walls of civilization will "
	"fall. Those standing behind you will fall. Your honor will fall. So you "
	"stand, shield ready. You won't move. They will."
	)


# The four Oaths are ordered here by what they swore *to*, and the ordering is
# the argument: a way of being, a world, an audience, a debt. Each text ends on
# its own cost rather than its own power, because the rules already print the
# power and the sheet has nowhere else to say what it took.
#
# The oldest oath, and the only one with no enemy, which is why it cannot be
# finished and why its cost is simply the next morning. Sacred Weapon sheds
# light *while you fight*: the sworn one cannot bear to work where nobody can
# see what they are doing, and that reading is the rules', not ours. Aura of
# Devotion says nobody near you can be Charmed, so the closing line is the
# feature restated as a fact about the person rather than a radius.
DEVOTION_DESCRIPTION = (
	"The oldest oath, and the hardest, because it has no enemy. You swore "
	"to nothing that can be killed. You swore to a way of being: honest "
	"when a lie would save you, brave where nobody would know you ran, "
	"kind when kindness is expensive.\n\n"
	"So there is no finishing it. There is only this morning, and the "
	"next, and whether the thing you said is still true in the way you "
	"stand. Your blade gives light while you fight. You could not bear to "
	"fight where nobody can see what you are doing.\n\n"
	"People near you cannot be talked into being someone else. You have "
	"never once been talked out of this."
	)
Devotion = Build_Specialization(
	guild=Paladin,
	name="Devotion",
	module=__name__,
	extends=_with_oath(
		DEVOTION_DESCRIPTION
		),
	heading="Oath of Devotion",
	)

# Sworn to what was here first, which puts this oath *older than gods* and is
# the one place the Guild touches the Druid's seat without taking it: the Druid
# is lent its membership and keeps it by attention, while this is a word given
# once to the same green. Undying Sentinel hands over agelessness nobody asked
# for, so the middle paragraph takes the gift and the third names the watch it
# bought. The closing image is the Guild's whole thesis in one sentence: the
# oath is outward, and a light is only worth keeping if it is kept for others.
ANCIENTS_DESCRIPTION = (
	"You swore to what was here first. The green that comes back. The "
	"light that returns after the longest night. The laugh in the dark. "
	"Gods are newer than that, and you did not swear to gods.\n\n"
	"The old things keep their side. Vines answer you. New magic breaks "
	"against the people you stand beside, because what you serve was here "
	"before spells were. And the old things do not age, so neither, quite, "
	"do you. That was not asked for. It came with the word.\n\n"
	"There will be a night when the light is nearly gone and you are what "
	"is left of it. That is the oath. Kindle it, shelter it, and do not "
	"let it go out in you."
	)
Ancients = Build_Specialization(
	guild=Paladin,
	name="Ancients",
	module=__name__,
	extends=_with_oath(
		ANCIENTS_DESCRIPTION
		),
	heading="Oath of the Ancients",
	)

# Sworn to be worth telling, which is the one Oath whose failure mode is
# inside the vow rather than outside it. Inspiring Smite gives the Temporary
# Hit Points to *other people*, so the story feeds whoever watched it, and the
# middle paragraph is that rule read back as a fantasy. Living Legend is
# "whether true or exaggerated" in the rulebook's own words, which is the
# knight errant of the Iberian novel arriving as a level 20 feature.
#
# The closing line is a horn that was not blown, from the founding poem of the
# whole Guild. It is never named and the poem is never cited, because the
# unquoted sentence rule covers borrowed sentences too: a reader who knows it
# hears it, and a reader who does not still hears a warning.
GLORY_DESCRIPTION = (
	"Others swore to a cause. You swore to be worth the telling.\n\n"
	"Not to win. Winning is a fact, and facts are forgotten. You swore "
	"that when they tell it afterwards, it will be worth their breath: "
	"the leap that should have failed, the line held past sense, the deed "
	"that made the people watching it braver. When you strike, the ones "
	"around you stand straighter. That is the story feeding on itself, "
	"and you are the story.\n\n"
	"The danger was always that you would prefer the telling to the deed. "
	"You know the sound of a horn not blown. You will not be that story."
	)
Glory = Build_Specialization(
	guild=Paladin,
	name="Glory",
	module=__name__,
	extends=_with_oath(
		GLORY_DESCRIPTION
		),
	heading="Oath of Glory",
	)

# Sworn *against*, and the only Oath whose object is a debt rather than a good.
# The register has to hold it at a distance from the Barbarian: rage is hot and
# runs out, and this is cold and does not, so the second paragraph says so in
# as many words. Vow of Enmity transfers when the target drops, which is a
# ledger rather than a grudge, and the text takes the rule at its word.
#
# Mercy is left standing on purpose. The Oath is alignment-free and the most
# obvious way to break that is to write the Vengeance text as a villain's; so
# mercy is not forbidden here, only unpromised, which is a harder and truer
# thing and keeps the avenger of a burnt village on the same page as the
# tyrant. The wings at 20 are the rules', and on a Tiefling they are the
# setting's own theology reversed for an hour by a vow.
VENGEANCE_DESCRIPTION = (
	"You swore against. Everything else in the oath is instrument.\n\n"
	"Somewhere there was a wrong big enough that a life is the right size "
	"of answer, and you gave the life. Not in fury. Fury runs out. This is "
	"a ledger, and you are the hand that closes it: the vow named on one "
	"enemy, and when that one falls, carried unspent to the next. They "
	"cannot run. You have made sure of that. They cannot swing without an "
	"answer.\n\n"
	"Mercy is not forbidden to you. It is simply not what you promised, "
	"and you do not promise twice. One day the wings come, and you find "
	"out what the wrong made of you."
	)
Vengeance = Build_Specialization(
	guild=Paladin,
	name="Vengeance",
	module=__name__,
	extends=_with_oath(
		VENGEANCE_DESCRIPTION
		),
	heading="Oath of Vengeance",
	)

# The fifth Oath. Its mechanics are the Heroes of Faerun elemental subclass;
# its lore is ours, because an oath to a genie is a pact and a pact is the
# Warlock's seat. Sworn to Creation itself, as settled with Julio: a small
# demiurge, will so strong it shapes the world, the four elements as the stuff
# everything is made of. It winks at the Wizard's True Names without breaking
# them: the Wizard writes and knows what writing cannot hold; this one speaks,
# unwritten, and the world yields a little. Neither holds a True Name. Its
# cost is the demiurge's: everything you make you answer for, and cannot
# unmake. Register: Lorca, Neruda's elemental odes, Scheherazade. This
# paragraph is the first full draft, for Julio's review.
CREATION_DESCRIPTION = (
	"You swore to nothing that exists. You swore to what is not yet, and to "
	"being the reason it comes. Others hold a truth, or a wood, or a wrong, "
	"or a song. You hold the four elements the way a poet holds a language "
	"he has not finished learning, and you speak it anyway, and it answers.\n\n"
	"Earth rises where you say. Fire goes where you send it. There is a line "
	"around you that nothing you have named can cross, and steel bends going "
	"through the field of your will. None of this was lent, and none of it "
	"was bought. It is what happens when a will is pointed at the world and "
	"does not look away.\n\n"
	"The cost is the maker's. Everything you make, you answer for, and you "
	"cannot unmake it. A city is a creation. So is a wall, and so are the "
	"people on the wrong side of it. One day you will look at a thing you "
	"called into being and not be able to call it back, and that is the day "
	"you find out what you swore."
	)
Creation = Build_Specialization(
	guild=Paladin,
	name="Creation",
	module=__name__,
	extends=_with_oath(
		CREATION_DESCRIPTION
		),
	heading="Oath of Creation",
	)


SPECIALIZATIONS = (
	Ancients,
	Devotion,
	Glory,
	Creation,
	Vengeance,
	)


def bind_paladin_voice(
		guild,
		) -> None:
	"""
	Seat the Guild paragraph on a Tag the vaulted kit built without one.

	Does not re-declare Specializations: those carry their own ``extends``
	from the calls above. This replaces the empty ``Describe`` layer only,
	which is the same repair ``bind_cleric_voice`` makes for the Cleric.
	"""
	guild.DESCRIPTION = PALADIN_DESCRIPTION
	guild.Describe = Describe_Layer(
		PALADIN_DESCRIPTION,
		extend=True,
		heading=None,
		)


bind_paladin_voice(
	guild=Paladin,
	)
