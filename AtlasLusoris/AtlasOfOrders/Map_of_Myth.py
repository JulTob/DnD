"""
Map of Myth — the Order's story, told in the project's Myth idiom.

Built for ``Charts_of_The_Monomyth.render``: a flat dict of tokens, where a
value may be a plain string or a list of ``(conds, text)`` rows.  ``render``
filters rows through ``If(host, conds)``, picks one, and **stores it back**,
so a token that appears twice reads the same both times.

The host is the Order itself, which answers ``in`` for its tradition, its two
domains, their facets, and its organization.  That is what makes the gating
work::

	("the Veil",  "They taught you to be unremarkable first, unremembered second.")
	("Primal",    "Nothing was written down. You were walked to it, twice.")
	("",          "…the ungated line, eligible for anyone…")

**Theme by imagery, not by label.**  A sentence gated on ``the Forge`` should
smell of heat and iron without using the word "Forge"; one gated on ``the
Veil`` should be about not being seen.  Naming the domain is the weakest way
to convey it, so the named rows are few and the flavoured rows are many.

Naming convention, inherited from ``Map_of_Stories``:

	Capitalized  a whole sentence — concatenates safely
	lowercase    a word or short noun phrase — must fit its host grammar
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Words — short, and safe in any host sentence
# ---------------------------------------------------------------------------

WORDS = {
	# What you were already good at when they found you.  Gated, so a Forge
	# initiate was good at something a Forge order would notice.
	"good_at": [
		("the Forge", "fixing what other people threw away"),
		("the Forge", "seeing how a thing had been put together"),
		("Home", "feeding more people than you had food for"),
		("Home", "making strangers comfortable in a room"),
		("the Hunt", "finding what everyone else had given up on"),
		("the Hunt", "reading ground nobody else thought held anything"),
		("Mercy", "staying calm with blood on your hands"),
		("Mercy", "sitting with people nobody else would sit with"),
		("the Veil", "not being remembered"),
		("the Veil", "being wherever nobody was looking"),
		("the Road", "arriving when you said you would"),
		("the Road", "knowing a way through"),
		("the Word", "reading what was not meant for you"),
		("the Word", "remembering exactly who said what"),
		("the Storm", "being outside when everyone else came in"),
		("the Storm", "knowing an hour early what the sky meant"),
		("the Shield", "standing in front of things"),
		("the Shield", "being the one who did not run"),
		("the Wall", "opening what was supposed to stay shut"),
		("the Wall", "noticing what had been moved"),
		("the Eye", "seeing the thing everyone had walked past"),
		("the Eye", "knowing when you were being lied to"),
		("the Beast", "calming animals nobody else could touch"),
		("the Beast", "being trusted by things that trust nothing"),
		("", "work nobody wanted to pay for"),
		],
	"lost_thing": [
		("the Forge", "a tool of your father's"),
		("Home", "a bowl from a house that no longer stands"),
		("the Hunt", "a knife you had carried since you were twelve"),
		("Mercy", "a ring taken off someone you could not save"),
		("the Veil", "a name you had stopped using"),
		("the Road", "a map you drew as a child"),
		("the Word", "a letter you never got to answer"),
		("the Storm", "a whistle from a boat that went down"),
		("the Shield", "your first commission, and the man who gave it"),
		("the Wall", "a key to somewhere you can no longer picture"),
		("the Eye", "a lens you ground yourself"),
		("the Beast", "a collar with no animal left to wear it"),
		("", "something small you had stopped describing to people"),
		],
	"craft_matter": [
		("the Forge", "the temper of a blade"),
		("Home", "how long a debt of bread lasts"),
		("the Hunt", "how old a print was"),
		("Mercy", "which of two wounds kills first"),
		("the Veil", "how a lie is built"),
		("the Road", "which crossing was safe that season"),
		("the Word", "who had actually written it"),
		("the Storm", "what the swell meant"),
		("the Shield", "where a line breaks"),
		("the Wall", "how the lock had been picked"),
		("the Eye", "what had been left out"),
		("the Beast", "what the herd was afraid of"),
		("", "a matter of your trade"),
		],
	}


# ---------------------------------------------------------------------------
# Sentences — the arc
# ---------------------------------------------------------------------------

BEFORE = [
	("", "You were good at {good_at}, but nobody was hiring. No one was waiting for you either."),
	("", "You were good at {good_at}, and it had never once been enough."),
	("", "Before them you were good at {good_at} and useful to no one in particular, and you had stopped calling that unusual."),
	("", "There was a year when you were good at {good_at} and there was nobody who would have noticed if you stopped."),
	("", "You had a trade, {good_at}, and a city that had no use for it, and no one at home to say otherwise."),
	]

CONTACT = [
	("", "Then someone returned {lost_thing} to you, and would not explain how they had it."),
	("", "Then a stranger corrected you, precisely, about {craft_matter}, and was right."),
	("", "Then you were handed a note with nothing on it but an hour."),
	("", "It began smaller than you would like to admit: someone paid a debt of yours, and waited a month before saying why."),
	("", "You can name the day. A door you had walked past for years stood open, and the person inside was expecting you."),
	("Divine", "They came to you at a funeral, which you later understood was not a coincidence."),
	("Arcane", "You were set a problem, casually, by someone who already knew you could solve it."),
	("Primal", "Someone walked you out of the town without explaining, and you went."),
	]

NOTICING = [
	("", "You noticed early that nobody ever states a rule here. You are simply corrected, kindly, until you no longer need correcting."),
	("", "You noticed early that the newest member is always the one sent to speak to outsiders."),
	("", "It took a week to see that letters arrive already answered. It took a year to stop finding that remarkable."),
	("", "There is a chair that is never taken and never pointed out, and nobody has ever explained it to you."),
	("Arcane", "Everything is written twice and one copy is burned, and you have never been told which copy you hold."),
	("Divine", "The calendar governs everything, including things a calendar has no business governing."),
	("Primal", "Nothing is written down at all. You were walked to it, twice, and expected to have understood."),
	("the Veil", "You have never seen two of them in the same room, and you have started to wonder whether that is deliberate."),
	("the Wall", "There are more keys than there are doors, and nobody remarks on it."),
	("the Word", "The oldest records are in a hand that also appears in the newest."),
	("the Eye", "You are being watched inside the house as carefully as outside it, and nobody pretends otherwise."),
	("the Beast", "The animals here are too calm, and they were calm before you arrived."),
	("the Forge", "Every one of them can make something with their hands, whatever else they do."),
	("Home", "Nobody arrives hungry twice."),
	("the Hunt", "Nothing that is put down here is ever lost, including people."),
	("the Storm", "They go out when everyone else comes in, and they take it personally when someone drowns."),
	("Mercy", "Nobody here flinches at anything, and you have decided not to ask what taught them that."),
	("the Road", "Half of them are always elsewhere, and the other half know exactly where."),
	("the Shield", "They stand up when a stranger enters, all of them, without appearing to have agreed on it."),
	]

TEACHING = [
	("", "What they made of you took two shapes. As {facet_a} you learned that {creed_a}. As {facet_b} you learned that {creed_b}. They have never reconciled the two aloud, and neither have you. Under both sits {devotion}, spoken of rarely and never lightly."),
	("", "They taught you as {facet_a}, on the grounds that {creed_a}. In the same season they taught you as {facet_b}, because {creed_b}. Nobody has ever presented these as a contradiction. Behind them stands {devotion}."),
	("", "Two things were put into you, and not in any order. {facet_a}: {creed_a}. {facet_b}: {creed_b}. What they are both for is {devotion}, and that much was made plain the first night."),
	("", "You were finished as {facet_a}, who holds that {creed_a}, and as {facet_b}, who holds that {creed_b}. An outsider would call that two orders. It is one, and it answers to {devotion}."),
	]

UNEASE = [
	("", "And that is not the only strange thing. The accounts balance, which for something this size should not be possible. You have {reaction}."),
	("", "That is not the strangest of it. Somebody has been paying for all of this since before the current members were born, and nobody will say who. You have {reaction}."),
	("", "You are not a fool. You have met four people who left, and all four have prospered, and not one will speak of it. You have {reaction}."),
	("", "None of it is the part that keeps you awake. One room is kept locked, and it is not the archive. You have {reaction}."),
	("", "Nobody ever asked you where you were before. That is not politeness, and you know it is not. You have {reaction}."),
	("", "They keep {relic}, and it is older than they have any right to be. You have {reaction}."),
	]

BELONGING = [
	("", "But they came for you when it went wrong and never asked what you had done, and every time you watch them work you feel {good_feeling}."),
	("", "But there is a place at their table that was set before you arrived and will be set after you are gone. What you felt, the first time they said your name as one of their own, was {good_feeling}."),
	("", "But nobody there has lied to you yet, which you cannot say of anyone else alive. Set against {unease}, that has been enough."),
	("", "But when you are ill, somebody notices on the first day. You would call it {good_feeling}, if you were the sort to say so aloud."),
	("", "But they buried your dead properly, at their own expense, and said nothing about it afterward. That bought them {unease} and more."),
	("", "And yet you have been wrong in front of them twice and are still here. What that gave you was {good_feeling}, and it has not worn off."),
	]

FEELING = {
	"good_feeling": [
		("", "a relief so complete it frightened you"),
		("", "something close to pride, which you had not felt in years"),
		("", "the first quiet you had known since you were a child"),
		("", "the plain satisfaction of being counted on"),
		("", "a steadiness you had assumed was meant for other people"),
		("", "something you can only call gratitude, though it runs fiercer than that"),
		],
	"unease": [
		("", "a cold thought you fold away and do not open"),
		("", "a question you learned not to ask twice"),
		("", "a doubt you have never once said out loud"),
		("", "the sense of standing on a floor with something beneath it"),
		("", "a small permanent draught somewhere behind your ribs"),
		],
	"reaction": [
		("", "decided not to pursue it"),
		("", "asked once, and understood from the answer not to ask again"),
		("", "written it down somewhere they will not look"),
		("", "made your peace with it the way you make peace with weather"),
		("", "kept your face still and your conclusions to yourself"),
		],
	}


# ---------------------------------------------------------------------------
# The hook — one bargain
# ---------------------------------------------------------------------------

HOOK = [
	("", "Wherever the {house} has reach, {perk}. None of that is generosity: {sacrifice}. And one day the whole account is called in at once, for this: {goal}."),
	("", "{perk}, which is the part people envy. What they do not see is the other clause: {sacrifice}. You carry it because something older than you needs doing: {goal}."),
	("", "Ask what membership is worth and they show you rather than answer: {perk}. Ask what it costs and they answer at once: {sacrifice}. Ask what it is all for, and you get the only thing they are impatient about: {goal}."),
	("", "The bargain was put to you plainly. They give you this: {perk}. They take this: {sacrifice}. And they are keeping you for {goal}."),
	]


SCRIPT = "{Before} {Contact} {Noticing} {Teaching} {Unease} {Belonging}"


def Myth(
		order,
		) -> dict:
	"""Build the token table for one Order, ready for ``render``."""
	table = {
		"Script": SCRIPT,
		"Hook": HOOK,
		"Before": BEFORE,
		"Contact": CONTACT,
		"Noticing": NOTICING,
		"Teaching": TEACHING,
		"Unease": UNEASE,
		"Belonging": BELONGING,
		# Order-supplied literals
		"house": order.organization.lower(),
		"organization": order.organization,
		"order": f"the {order.name}",
		"devotion": order.devotion,
		"domain_a": order.domains[0].name,
		"domain_b": order.domains[1].name,
		"facet_a": order.facets[0].name,
		"facet_b": order.facets[1].name,
		"creed_a": order.facets[0].creed,
		"creed_b": order.facets[1].creed,
		"place": order.place,
		"practice": order.practice,
		"relic": order.relic,
		"perk": order.perk,
		"sacrifice": order.sacrifice,
		"goal": order.goal,
		}
	table.update(
		WORDS
		)
	table.update(
		FEELING
		)

	return table


__all__ = (
	"Myth",
	"SCRIPT",
	)
