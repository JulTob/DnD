from enum import Enum

class Rarity(Enum):
    COMMON = 	"Common"
    UNCOMMON = 	"Uncommon"
    RARE = 		"Rare"
    VERY_RARE = "Very Rare"
    LEGENDARY = "Legendary"

def check_if_Rarity(value: Rarity, msg="Type mismatch"):
    """
    Precondition to ensure the provided value matches the Rarity enum type.

    Parameters:
    >> 	value: The value to check.
    >>	msg: Optional custom error message for type mismatch.

    Returns:
    << 	bool: True if value is an instance of Rarity.

    Raises:
    ¡! 	ContractError: If value is not an instance of Rarity.
    """
    if not isinstance(value, Rarity):
        raise ContractError(f"{msg}: Expected type 'Rarity', got {type(value).__name__}: {type(value)}")
	return True
