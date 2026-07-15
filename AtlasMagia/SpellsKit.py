'''
SpellsKit — the TOP implementation of the Spell class and its Tags.

XKit per Canon/Conventions.md: this module OWNS the Spell class and every
Tag that may be applied to one. Lodge_of_Spells stays what its name says —
a curated registry of Spell instances — and imports Spell from here.
(QST-0031.1; TagKit is the pinned upstream, see Canon/TagKit-Doctrine.md.)

The three Tag families, each rooted on Spell_Tag (whose Precondition
restricts every spell Tag to Spell targets — TagPreconditionError and a
full rollback on anything else):

	School     — the eight canonical schools of magic. Exclusive: a spell
	             bears exactly one (enforced by School.Single_School).
	Tradition  — Arcane / Divine / Primal (the One D&D playtest grouping,
	             adopted deliberately as a project choice, not core rules).
	             NOT exclusive: Cure Wounds is Divine and Primal at once.
	Spell_List — "this spell appears on X's list", one Tag per caster
	             class/subclass the codebase deals spells to. Not exclusive.

Membership reads as TagKit intends:
	Evocation(fireball)              # tag it (atomic; no-op if already)
	fireball in Evocation            # IS-check
	fireball in School               # any school at all
	for spell in Wizard_List: ...    # the live registry, for free
	"evocation" in fireball          # string probe, case-insensitive
'''

from TagKit import Tag, Pre

try:
	from AtlasScriptum.Map_of_Formats import Entry
except ImportError:
	raise


"""		Spell class    """
class Spell:
	# Roots for TagPaths()/Outline() trimming on tagged spells.
	TAG_ROOTS = ()  # filled after the Tag families are declared below

	def __init__(spell,
				 name="",
				 level=0,
				 school="",
				 casting_time="",
				 ranges = "",
				 duration = "",
				 components = "",
				 concentration = "",
				 definition = ""):
		spell.name =  name
		spell.level = level
		spell.school = school
		spell.casting_time = casting_time
		spell.ranges = ranges
		spell.duration = duration
		spell.components = components
		spell.concentration = concentration
		spell.definition = definition

	def describe(spell):
		desc = spell.string
		return desc

	def __str__(spell):
		desc = ""
		if spell.casting_time:   desc += f"<i>⟨{spell.casting_time}⟩</i><br>"
		if spell.concentration:  desc += f"<i>({spell.concentration}: </i>"
		if spell.duration:       desc += f"<i>({spell.duration})</i>"
		if spell.ranges:         desc += f"<br><i>>{spell.ranges}></i>"
		if spell.components:	 desc += f"<br><i>⦓{spell.components}⦔</i>"
		if spell.level == 0:
			level_text = "<b><p>Cantrip</b></p>"
		else:
			level_text = f"<b><p> Level {spell.level} Spell </b></p>"
		return f"""
		<h4 class="spell-title"> {spell.name}</h4>
		{level_text}
		<p class="spell-meta">{desc}</p>
		<p>
		{spell.definition }
		</p>
		"""

	@property
	def string(spell):

		name  = f"{spell.name}"
		desc  = f"{spell.school}"
		definition = ""
		if spell.casting_time:   desc += f"({spell.casting_time})"
		if spell.concentration:  desc += f"⟨{spell.concentration}"
		if spell.duration:       desc += f"⟨{spell.duration}⟩"
		if spell.ranges:         desc += f"-{spell.ranges}"
		if spell.definition:     definition += f"\n\t{spell.definition}"
		string = Entry(title=name, definition=definition, description=desc)
		return string


"""		The root: every spell Tag is exclusive to Spell targets    """
class Spell_Tag(Tag):
	NAME = "Spell Tag"
	DESCRIPTION = "Root of every Tag a Spell may bear. Only Spell targets."
	ABSTRACT = True

	@Pre
	def Spell_Only(agent):
		#-- the contract, not a hand-rolled assert: failure raises
		#-- TagPreconditionError and rolls the whole application back
		return isinstance(agent, Spell)


"""		Schools of magic — exactly one per spell    """
class School(Spell_Tag):
	NAME = "School"
	DESCRIPTION = "One of the eight schools of magic. A spell bears exactly one."
	ABSTRACT = True

	@Pre
	def Single_School(agent):
		#-- runs with the candidate school already active, so a second
		#-- school counts 2 and the application rolls back
		count = sum(1 for school in SCHOOLS.values() if agent in school)
		return count <= 1


class Abjuration(School):
	NAME = "Abjuration"
	DESCRIPTION = "Wards and protection: shields, banishments, dispels."

class Conjuration(School):
	NAME = "Conjuration"
	DESCRIPTION = "Summoning and transportation: creatures, objects, teleports."

class Divination(School):
	NAME = "Divination"
	DESCRIPTION = "Revelation: scrying, foresight, detection."

class Enchantment(School):
	NAME = "Enchantment"
	DESCRIPTION = "Minds bent: charms, compulsions, sleep."

class Evocation(School):
	NAME = "Evocation"
	DESCRIPTION = "Raw energy shaped: fire, lightning, radiant bolts."

class Illusion(School):
	NAME = "Illusion"
	DESCRIPTION = "Deceived senses: images, sounds, phantasms."

class Necromancy(School):
	NAME = "Necromancy"
	DESCRIPTION = "Life and death bartered: drains, undeath, false life."

class Transmutation(School):
	NAME = "Transmutation"
	DESCRIPTION = "Matter reshaped: polymorphs, hastes, stone to mud."


# Canonical name -> School Tag. The one lookup table for normalizing the
# Lodge's raw school strings (QST-0031.3 strips whitespace and the
# Wildemount dunamancy suffixes D/DC/DG before consulting this).
SCHOOLS = {
	"Abjuration":    Abjuration,
	"Conjuration":   Conjuration,
	"Divination":    Divination,
	"Enchantment":   Enchantment,
	"Evocation":     Evocation,
	"Illusion":      Illusion,
	"Necromancy":    Necromancy,
	"Transmutation": Transmutation,
	}


"""		Casting traditions — Arcane / Divine / Primal (One D&D playtest)    """
class Tradition(Spell_Tag):
	NAME = "Tradition"
	DESCRIPTION = (
		"Arcane, Divine, or Primal — the One D&D playtest's grouping, "
		"adopted as a project choice (UA, not core). A spell may bear "
		"more than one: Cure Wounds is Divine and Primal."
		)
	ABSTRACT = True


class Arcane(Tradition):
	NAME = "Arcane"
	DESCRIPTION = "The studied and innate lists: Bard, Sorcerer, Warlock, Wizard."

class Divine(Tradition):
	NAME = "Divine"
	DESCRIPTION = "The granted lists: Cleric, Paladin."

class Primal(Tradition):
	NAME = "Primal"
	DESCRIPTION = "The natural lists: Druid, Ranger."


TRADITIONS = {
	"Arcane": Arcane,
	"Divine": Divine,
	"Primal": Primal,
	}


"""		Class spell lists — who may learn it    """
class Spell_List(Spell_Tag):
	NAME = "Spell List"
	DESCRIPTION = "The spell appears on this class's (or subclass's) list."
	ABSTRACT = True


class Bard_List(Spell_List):
	NAME = "Bard"
	DESCRIPTION = "On the Bard spell list."

class Cleric_List(Spell_List):
	NAME = "Cleric"
	DESCRIPTION = "On the Cleric spell list."

class Druid_List(Spell_List):
	NAME = "Druid"
	DESCRIPTION = "On the Druid spell list."

class Paladin_List(Spell_List):
	NAME = "Paladin"
	DESCRIPTION = "On the Paladin spell list."

class Ranger_List(Spell_List):
	NAME = "Ranger"
	DESCRIPTION = "On the Ranger spell list."

class Sorcerer_List(Spell_List):
	NAME = "Sorcerer"
	DESCRIPTION = "On the Sorcerer spell list."

class Warlock_List(Spell_List):
	NAME = "Warlock"
	DESCRIPTION = "On the Warlock spell list."

class Wizard_List(Spell_List):
	NAME = "Wizard"
	DESCRIPTION = "On the Wizard spell list."

class Eldritch_Knight_List(Spell_List):
	NAME = "Eldritch Knight"
	DESCRIPTION = "On the Eldritch Knight (Fighter) subclass list."

class Arcane_Trickster_List(Spell_List):
	NAME = "Arcane Trickster"
	DESCRIPTION = "On the Arcane Trickster (Rogue) subclass list."


# Class-list name -> Tag, keyed exactly as Grimoire_of_Spellcasters'
# SPELL_LISTS speaks today, so QST-0031.3's migration is a dict walk.
SPELL_LISTS_TAGS = {
	"Bard":             Bard_List,
	"Cleric":           Cleric_List,
	"Druid":            Druid_List,
	"Paladin":          Paladin_List,
	"Ranger":           Ranger_List,
	"Sorcerer":         Sorcerer_List,
	"Warlock":          Warlock_List,
	"Wizard":           Wizard_List,
	"Eldritch Knight":  Eldritch_Knight_List,
	"Arcane Trickster": Arcane_Trickster_List,
	}

# Which lists each tradition covers (the UA mapping, for QST-0031.3 to
# derive a spell's Tradition from its class lists).
TRADITION_OF_LIST = {
	"Bard":             Arcane,
	"Sorcerer":         Arcane,
	"Warlock":          Arcane,
	"Wizard":           Arcane,
	"Eldritch Knight":  Arcane,
	"Arcane Trickster": Arcane,
	"Cleric":           Divine,
	"Paladin":          Divine,
	"Druid":            Primal,
	"Ranger":           Primal,
	}


Spell.TAG_ROOTS = (Spell_Tag,)


if __name__ == "__main__":
	# Self-test / usage demo. Run:  python AtlasMagia/SpellsKit.py
	from TagKit import TagPreconditionError

	bolt = Spell(name="Test Bolt", level=1, school="Evocation", definition="zap")

	# 1) Tagging and membership, root included
	Evocation(bolt)
	assert bolt in Evocation, "tagged spell must be in its school"
	assert bolt in School, "school membership must climb to the family root"
	assert bolt in Spell_Tag, "…and to the kit root"
	assert isinstance(bolt, Spell), "the host class survives tagging"

	# 2) More axes compose on the same target
	Arcane(bolt)
	Wizard_List(bolt)
	Sorcerer_List(bolt)
	assert bolt in Arcane and bolt in Wizard_List and bolt in Sorcerer_List

	# 3) The registry, for free
	assert any(s is bolt for s in Evocation), "Field iteration finds the spell"
	assert any(s is bolt for s in Spell_List), "…on every family it bears"

	# 4) String probe (Tagged mixin)
	assert "evocation" in bolt and "wizard" in bolt

	# 5) Contract: only Spell targets
	class NotASpell:
		pass

	try:
		Evocation(NotASpell())
	except TagPreconditionError:
		pass
	else:
		raise AssertionError("a non-Spell must be rejected by Spell_Only")

	# 6) Contract: one school per spell (atomic rollback)
	try:
		Necromancy(bolt)
	except TagPreconditionError:
		pass
	else:
		raise AssertionError("a second school must be rejected")
	assert bolt in Evocation and bolt not in Necromancy, "rollback must hold"

	# 7) Labels speak D&D, not Python
	assert Wizard_List.Label() == "Wizard"
	assert Eldritch_Knight_List.Label() == "Eldritch Knight"

	print("SpellsKit self-test passed.")
