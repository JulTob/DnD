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
from AtlasActorLudi.Map_of_Character_Generation import (
	Character_Choices,
	character_choices,
	summon_player,
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
