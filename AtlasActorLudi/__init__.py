"""AtlasActorLudi — actor statistics: ability scores and modifiers."""

# [restored 2026-08-29 after the working-tree wipe; the uncommitted final was
#  read in-session and is reproduced here from that record.]

from AtlasActorLudi.CharactersKit import Character, Player, NonPlayer
from AtlasActorLudi.GendersKit import (
	Agender,
	Female,
	Find_Gender,
	Gender,
	Gender_Reveal,
	Male,
	)

# Lazy: Map_of_Character_Generation imports Lusoris, which imports CharactersKit.
# Eager import here closes a cycle through BackgroundKit during package load.
def __getattr__(
		name: str,
		):
	if name in {
		"Character_Choices",
		"character_choices",
		"summon_player",
		}:
		from AtlasActorLudi.Map_of_Character_Generation import (
			Character_Choices,
			character_choices,
			summon_player,
			)
		globals().update(
			{
				"Character_Choices": Character_Choices,
				"character_choices": character_choices,
				"summon_player": summon_player,
				}
			)
		return globals()[name]
	raise AttributeError(
		name
		)


def Summon_Player_Character(
		seed: int = -1,
		level: int = 1,
		guild: str = "None",
		origin: str = "None",
		background: str = "None",
		):
	character = Character(seed=seed, level=level)
	Player(character)
	from AtlasLusoris.AbilityScoresKit import AbilityScores
	character.AS = AbilityScores(
		character=character
		)
	return character


if __name__ == "__main__":
	char = Summon_Player_Character(seed=42, level=1)
	print(char)
	print(char.AS.STR, char.AS.DEX)
	print(char.Roll(6))


__all__ = (
	"Character",
	"Agender",
	"Female",
	"Find_Gender",
	"Gender",
	"Gender_Reveal",
	"Male",
	"Player",
	"NonPlayer",
	"Character_Choices",
	"character_choices",
	"summon_player",
	"Summon_Player_Character",
	)
