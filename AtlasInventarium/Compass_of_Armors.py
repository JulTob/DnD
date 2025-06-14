from enum import Enum

class ArmorType(Enum):
    UNARMORED = "Unarmored"
    LIGHT = 	"Light"
    MEDIUM = 	"Medium"
    HEAVY = 	"Heavy"

def check_if_ArmorType(value: ArmorType, msg: str = "Type mismatch") -> bool:
    """
    Precondition to ensure the provided value matches the ArmorType enum type.

    Parameters:
    >> 	<value>: The value to check.
    >> 	<msg>: Optional custom error message for type mismatch.

    Returns:
    << 	[bool]: (True) if value is an instance of [ArmorType].

    Raises:
    ¡! 	ContractError: If value is not an instance of [ArmorType].
    """
    if not isinstance(value, ArmorType):
        raise ContractError(f"{msg}: Expected type 'ArmorType', got {type(value).__name__}: {type(value)}")
    return True
