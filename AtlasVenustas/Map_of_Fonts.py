"""
Map_of_Fonts — which face each class's spellcasting section title wears.

A lookup, not a Tag: this is presentation flavor (which font a class's header
renders in), not a domain axis a Character composes onto its identity — it
lives in Venustas, the presentation Atlas, as a plain key -> value record.
Add a class here to give it its own voice; nothing else changes.

Scoped to the section TITLE only ("Wizard Spellcasting", "Warlock Pact
Magic"...). Spell names and the sub-headers inside stay on the lighter
--font-script face — a whole page of gothic display type reads as noise.
"""

DEFAULT_TITLE_FONT = "'Manufacturing Consent', var(--font-header)"

TITLE_FONTS = {
	"Warlock": "'UnifrakturMaguntia', var(--font-header)",
}


def title_font(class_name: str) -> str:
	"""CSS font-family value for `class_name`'s spellcasting section title."""
	return TITLE_FONTS.get(class_name, DEFAULT_TITLE_FONT)


if __name__ == "__main__":
	assert title_font("Warlock") == "'UnifrakturMaguntia', var(--font-header)"
	assert title_font("Wizard") == DEFAULT_TITLE_FONT
	assert title_font("SomeFutureClass") == DEFAULT_TITLE_FONT
	print("Map_of_Fonts: self-test passed.")
