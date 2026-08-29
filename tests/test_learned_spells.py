"""Learned spells grow with level and do not reshuffle."""
import os
from AtlasLusoris.Compass_of_Learned_Spells import (
	catalog_keys,
	catalog_spells,
	html_spell_catalog,
	know_spell,
	progressive_learn,
	spell_key,
	spell_mark,
	unique_spells,
	)


class FakeSpell:
	def __init__(self, name, level):
		self.name = name
		self.level = level


def fake_table():
	return {
		0: [FakeSpell(f"Cantrip {i}", 0) for i in range(1, 9)],
		1: [FakeSpell(f"First {i}", 1) for i in range(1, 9)],
		2: [FakeSpell(f"Second {i}", 2) for i in range(1, 9)],
		3: [FakeSpell(f"Third {i}", 3) for i in range(1, 9)],
		}


class FakeCharacter:
	def __init__(self, seed):
		self.seed = seed


def learn_at(level):
	return progressive_learn(
		FakeCharacter(42),
		fake_table(),
		level,
		cantrips_at=lambda lvl: 3 if lvl < 4 else 4,
		known_at=lambda lvl: 4 + lvl,
		slots_at=lambda lvl: (2, 0, 0) if lvl < 3 else (4, 2, 0) if lvl < 5 else (4, 3, 2),
		salt=1,
		)


def test_grows_without_reshuffle():
	low_cantrips, low_known = learn_at(4)
	high_cantrips, high_known = learn_at(5)
	assert {spell_key(spell) for spell in low_cantrips} <= {spell_key(spell) for spell in high_cantrips}
	assert {spell_key(spell) for spell in low_known} <= {spell_key(spell) for spell in high_known}
	assert len(high_known) >= len(low_known)
	assert len(unique_spells(low_known)) == len(low_known)


def test_know_spell_is_separate_from_display():
	class Character:
		spellcaster = None

	character = Character()
	spell = FakeSpell("Speak with Animals", 1)
	gained = know_spell(character, spell)
	assert gained is None
	known = catalog_spells(character.spellcaster)
	assert {spell_key(item) for item in known} == {"Speak with Animals"}
	page = html_spell_catalog(character.spellcaster)
	assert "Speak with Animals" in page
	assert spell_mark(spell) in page


def test_forest_gnome_lineage_knows_without_embedding():
	from AtlasLusoris.Grimoire_of_Features import ForestGnomeLineage

	class Character:
		spellcaster = None
		features = []

	character = Character()
	feat = ForestGnomeLineage()
	feat(character)
	names = {spell_key(spell) for spell in catalog_spells(character.spellcaster)}
	assert "Minor Illusion" in names
	assert "Speak with Animals" in names
	assert "<div class='npc-textbox'>" not in feat.description
	assert "{SpeakwithAnimals}" not in feat.description
	assert str(character.spellcaster.html_catalog()).count("Speak with Animals") >= 1


def test_wildwarden_knows_speak_with_animals_without_embedding():
	from AtlasLusoris.Grimoire_of_Features import Wildwarden

	class Character:
		spellcaster = None
		char_class = "Wizard"
		features = []

	character = Character()
	feat = Wildwarden()
	feat(character)
	names = {spell_key(spell) for spell in catalog_spells(character.spellcaster)}
	assert "Speak with Animals" in names
	assert "<div class='npc-textbox'>" not in feat.description
	assert "See Spells" in feat.description
	assert "Tag Team" in feat.description
	assert str(character.spellcaster.html_catalog()).count("Speak with Animals") >= 1
	assert "Speak with Animals" not in {
		spell_key(spell) for spell in character.spellcaster.spells_known
		}


def test_grant_does_not_consume_a_class_known_slot():
	speak = FakeSpell("Speak with Animals", 1)
	fire = FakeSpell("Fire Bolt", 0)
	shield = FakeSpell("Shield", 1)
	armor = FakeSpell("Mage Armor", 1)

	class Book:
		def __init__(self):
			self.spells_known = [speak, fire]
			self.granted_spells = []
			self.always_prepared = set()
			self.prepared_spells = [speak, fire]
			self.catalog_known = True
			self.spells_available = [speak, fire, shield, armor]

	class Character:
		def __init__(self):
			self.seed = 7
			self.spellcaster = Book()

	character = Character()
	known_before = len(character.spellcaster.spells_known)
	know_spell(character, speak)
	book = character.spellcaster
	granted_names = {spell_key(spell) for spell in book.granted_spells}
	known_names = {spell_key(spell) for spell in book.spells_known}
	assert granted_names == {"Speak with Animals"}
	assert "Speak with Animals" not in known_names
	assert len(book.spells_known) == known_before
	assert {"Speak with Animals", "Fire Bolt"} <= catalog_keys(book)
	know_spell(character, speak)
	assert len([spell for spell in book.granted_spells if spell_key(spell) == "Speak with Animals"]) == 1


def test_progressive_learn_skips_owned_names_without_shrinking_the_budget():
	cantrips, known = progressive_learn(
		FakeCharacter(42),
		fake_table(),
		1,
		cantrips_at=lambda lvl: 3,
		known_at=lambda lvl: 4,
		slots_at=lambda lvl: (2,),
		salt=1,
		skip={"Cantrip 1", "First 1"},
		)
	keys = {spell_key(spell) for spell in cantrips + known}
	assert "Cantrip 1" not in keys
	assert "First 1" not in keys
	assert len(cantrips) == 3
	assert len(known) == 4


if __name__ == "__main__":
	test_grows_without_reshuffle()
	test_know_spell_is_separate_from_display()
	test_forest_gnome_lineage_knows_without_embedding()
	test_wildwarden_knows_speak_with_animals_without_embedding()
	test_grant_does_not_consume_a_class_known_slot()
	test_progressive_learn_skips_owned_names_without_shrinking_the_budget()
	print("progressive_learn: ok", flush=True)
	os._exit(0)
