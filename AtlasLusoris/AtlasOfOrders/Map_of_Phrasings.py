"""
Map of Phrasings — the narrative an Order's prose collapses out of.

This is **not** a bag of independent sentences.  It is a story arc, and each
beat is written to arrive after the one before it:

	1. BEFORE      who you were, and what was missing
	2. CONTACT     how they reached you            ("Then …")
	3. NOTICING    the first odd thing you saw     ("You noticed early that …")
	4. TEACHING    the two spheres, and the creeds
	5. UNEASE      the second odd thing            ("That is not the only …")
	6. BELONGING   why you stayed anyway           ("But …")

Two layers of collapse.  The beat pools hold the shape; the ``VOCABULARY``
pools fill words *inside* them, so the same beat never reads the same twice.
A line may nest freely — ``{belonging}`` may itself mention ``{house}`` — and
the resolver keeps going until no braces remain.

Writing rules learned by reading output aloud:

* **Every vocabulary value must survive its worst host sentence.**  A value
  used as a subject has to work as a subject; a value that may be long must
  not sit inside a relative clause, or it garden-paths.
* **Never hang a relative clause on a slot.**  ``{devotion}, which is spoken
  of rarely`` attaches to the wrong noun the moment the devotion is a phrase.
  Start a new sentence instead.
* **No beat may close the paragraph.**  A line like "that is the whole of it"
  ends the story in the first sentence; every beat must hand forward.
* **Pools must be deep.**  Five entries in a slot drawn every time reads as a
  template within three examples.

Slots the Order supplies: ``{organization} {house} {order} {devotion}
{domain_a} {domain_b} {facet_a} {facet_b} {creed_a} {creed_b} {place}
{practice} {relic} {perk} {sacrifice} {goal}``.
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# Nested vocabulary
# ---------------------------------------------------------------------------

VOCABULARY = {
	# Must read as a sentence subject: "… because {kin} never needed them to."
	"kin": (
		"the ones who had been there longest",
		"people who never introduced themselves",
		"the members who taught you",
		"everyone senior to you",
		"the old hands",
		"those who had carried it before you",
		),
	"former_state": (
		"good at something nobody was hiring for",
		"one bad season from becoming a story other people told",
		"clever, and entirely unattached",
		"the sort of person a city loses without noticing",
		"fed, housed, and quietly certain it would not last",
		"someone with a talent and no one to spend it on",
		"competent, and invisible, and increasingly angry about the second part",
		"living off a reputation that had two seasons left in it",
		"halfway to becoming exactly what people had predicted",
		),
	"lack": (
		"nobody to be loyal to",
		"a skill and no one worth using it for",
		"a great deal of time and nothing that wanted any of it",
		"no reason to be in that city rather than another",
		"a name that opened no doors at all",
		"nothing anyone would have missed",
		"no one who would have come looking",
		),
	"contact_event": (
		"someone paid a debt of yours without mentioning it, and waited a month before saying why",
		"a stranger corrected you, precisely, on a thing you had been wrong about for years",
		"you were handed a note with nothing on it but an hour",
		"a job you were doing turned out to have been a test, and you had passed it days earlier",
		"you were invited to help with something small, and the smallness turned out to be the point",
		"someone sat down opposite you and said your grandmother's name",
		"a door you had walked past for years was open, and someone inside was expecting you",
		"you were thanked, by name, for something you had told nobody about",
		"a woman you had never met paid for your supper and asked you one question",
		"they returned something you had lost so long ago you had stopped describing it",
		"you woke up somewhere safe, and the person who had carried you was already gone",
		),
	"good_feeling": (
		"a relief so complete it frightened you",
		"something close to pride, which you had not felt in years",
		"the first quiet you had known since you were a child",
		"the specific comfort of being useful to people who notice",
		"a warmth you have never managed to describe to anyone outside",
		"the particular peace of a door closing behind you",
		"a steadiness you had assumed was for other people",
		"the plain satisfaction of being counted on",
		"something you can only call gratitude, though it is fiercer than that",
		),
	"unease": (
		"a cold thought you fold away and do not open",
		"a question you learned not to ask twice",
		"the arithmetic that only arrives at three in the morning",
		"a doubt you have never once said out loud",
		"the sense of standing on a floor with something under it",
		"a small permanent draught somewhere behind your ribs",
		),
	"reaction": (
		"decided not to pursue it",
		"asked once, and understood from the answer not to ask again",
		"written it down somewhere they will not look",
		"made your peace with it the way you make peace with weather",
		"filed it beside the other things you have chosen not to know",
		"kept your face still and your conclusions to yourself",
		"stopped counting, which was a decision",
		),
	# Must read after "you noticed early that …" and stand alone.
	"odd_detail": (
		"nobody ever states a rule; you are simply corrected, kindly, until you no longer need to be",
		"the newest member is always the one sent to speak to outsiders",
		"there are more keys than doors, and nobody remarks on it",
		"the oldest of them defer, sometimes, to someone who is not in the room",
		"the records go back further than the {house} admits to existing",
		"nobody is ever expelled; they simply stop being mentioned",
		"every member can cook, and no one can explain why that is required",
		"the youngest are told things the middle ranks clearly are not",
		"letters arrive already answered",
		"there is a chair that is never taken, and never pointed out",
		"the accounts are read aloud, and one line is always skipped",
		),
	# Must stand alone as its own sentence; keep {place} out of it.
	"unease_detail": (
		"one room in the house is kept locked, and it is not the archive",
		"twice a year everyone is elsewhere on the same night, and nobody compares notes afterward",
		"you have met four people who left, and all four have prospered, and none will speak of it",
		"they keep {relic}, and it is older than they have any right to be",
		"the accounts balance, which for something this size should not be possible",
		"somebody has been paying for all of this since before the current members were born",
		"there is a name on the oldest roster that is also on the newest",
		"the {house} has never once been raided, in a century of doing this",
		"nobody has ever asked you where you were before, and that is not politeness",
		),
	"belonging": (
		"they came for you when it went wrong, and never asked what you had done",
		"nobody in the {house} has lied to you yet, which you cannot say of anyone else alive",
		"you have a place at a table that was set before you came and will be set after you go",
		"the work is real, and it is yours, and it matters to someone",
		"when you are ill, somebody notices on the first day",
		"they buried your dead properly, at their own expense, and said nothing about it",
		"you have been wrong in front of them, twice, and are still here",
		"there is one person there you would tell anything, and you have",
		),
	}


# ---------------------------------------------------------------------------
# The arc
# ---------------------------------------------------------------------------

BEFORE = (
	"Before the {house}, you were {former_state}, with {lack}.",
	"You were {former_state}, and you had {lack}, and you had stopped calling that unusual.",
	"There was a version of you with {lack}, and no prospect of that changing.",
	"You had {lack}. It had been true long enough to feel like a personality.",
	"For a long time you were {former_state}, and told yourself it suited you.",
	"You were {former_state}. Nobody was coming to fix that.",
	"Whatever else you were, you were {former_state}, and running out of road.",
	)

CONTACT = (
	"Then {contact_event}.",
	"It began without ceremony: {contact_event}.",
	"That was the year {contact_event}.",
	"Then, with no announcement at all, {contact_event}.",
	"You can name the day. {contact_event}.",
	"It started as a small thing. {contact_event}.",
	"You have gone over it many times since: {contact_event}.",
	)

NOTICING = (
	"You noticed early that {odd_detail}. It should have worried you. Instead you found it restful.",
	"You noticed early that {odd_detail}, and that nobody had thought to warn you.",
	"It took a week to see that {odd_detail}. It took a year to stop finding that remarkable.",
	"What struck you first was not the secrecy. It was that {odd_detail}.",
	"They meet at {place}, where {practice}, and within a month you had worked out that {odd_detail}.",
	"Nobody sat you down and explained anything. You simply observed, over one long winter, that {odd_detail}.",
	"The strangeness is not theatrical. It is only that {odd_detail}, and that everyone treats this as ordinary.",
	)

TEACHING = (
	"What {order} keeps is {domain_a}, and also {domain_b}, and it has never offered anyone an explanation. They made you {facet_a}, on the reasoning that {creed_a}. They made you {facet_b} in the same season, because {creed_b}. Behind all of it stands {devotion}. You stopped asking how the halves reconcile once you understood that {kin} had never needed them to.",
	"They are sworn to {domain_a} and to {domain_b}. Both, always, and in that order only because a sentence has to begin somewhere. As {facet_a} you learned that {creed_a}. As {facet_b} you learned that {creed_b}. What they serve, under both, is {devotion}. It is spoken of rarely, and never lightly.",
	"The teaching is {domain_a}. The teaching is also {domain_b}. You were finished as {facet_a}, who holds that {creed_a}, and as {facet_b}, who holds that {creed_b}. All of it is owed to {devotion}, and that much was made plain the first night.",
	"Two words are cut above the door: {domain_a}, and {domain_b}. Nobody living remembers which was cut first. You were raised in the house as {facet_a}, because {creed_a}, and finished as {facet_b}, because {creed_b}. Both roads run back to {devotion}.",
	"They will tell an outsider it is about {domain_a}. They will not mention {domain_b} at all, and you have come to understand that as courtesy rather than deceit. You were taught as {facet_a}, that {creed_a}, and as {facet_b}, that {creed_b}. Under both sits {devotion}. Whatever it is, it is older than the building.",
	)

UNEASE = (
	"And that is not the only strange thing. {unease_detail}. You have {reaction}, and you carry {unease} about it.",
	"That is not the strangest of it. {unease_detail}. When you understood that, it left you with {unease}, and you have {reaction}.",
	"There is more, of course. {unease_detail}. You have {reaction}, which is not the same as being easy about it.",
	"You are not a fool. {unease_detail}. You noticed, and you have {reaction}, and what remains is {unease}.",
	"None of that is the part that keeps you awake. {unease_detail}. You have {reaction}, and left {unease} where it sits.",
	)

BELONGING = (
	"But {belonging}, and every time you watch the {house} do what it can actually do, what you feel is {good_feeling}, and a sharp private gratitude that you stand on this side of it.",
	"But {belonging}. That is worth {unease} at three in the morning, and you have decided so more than once.",
	"And yet {belonging}. What you felt, the night you understood you were one of them, was {good_feeling}.",
	"But {belonging}, and there is no version of your life now in which you hand that back. You would call it {good_feeling}, if you were the sort to say so aloud.",
	"None of that changes what {belonging} means. What you felt, the day they first said your name as one of their own, was {good_feeling}, and it has not worn off.",
	"You have weighed it. On one side, {unease}. On the other, {belonging}. You are still here, and you know exactly why: {good_feeling}.",
	)


DESCRIPTION_ARC = (
	BEFORE,
	CONTACT,
	NOTICING,
	TEACHING,
	UNEASE,
	BELONGING,
	)


# ---------------------------------------------------------------------------
# The hook: one bargain — a pro, a con, and what the con is buying
# ---------------------------------------------------------------------------

HOOK_FORMS = (
	"Wherever the {house} has reach, {perk}. None of that is generosity: {sacrifice}, and one day the whole account will be called in at once, for this: {goal}.",
	"{perk}, which is the part people envy. What they do not see is the other clause: {sacrifice}. You carry it because something older than you needs doing: {goal}.",
	"The bargain is plain, and it was put to you plainly. They give you this: {perk}. They take this: {sacrifice}. And they are keeping you for {goal}.",
	"You will find that {perk}. You will also find that {sacrifice}. That is the price of the first, it was never hidden, and both exist so that somebody can one day {goal}.",
	"{perk}. That is the {house} keeping its word. Keeping yours means this: {sacrifice}. Neither side is doing it for its own sake: {goal}.",
	"There is no ledger, but everyone knows the terms. {perk}. Against that: {sacrifice}. What it is all for is easy to say and hard to do: {goal}.",
	"Ask what membership is worth and they will show you rather than answer: {perk}. Ask what it costs and they will answer at once: {sacrifice}. Ask what it is for, and you get the only thing they are impatient about: {goal}.",
	)


__all__ = (
	"BELONGING",
	"BEFORE",
	"CONTACT",
	"DESCRIPTION_ARC",
	"HOOK_FORMS",
	"NOTICING",
	"TEACHING",
	"UNEASE",
	"VOCABULARY",
	)
