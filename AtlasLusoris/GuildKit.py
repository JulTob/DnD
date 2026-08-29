
# Kept: callers outside this module still name it.
WEIGHT_CLASS_FEATURE = WEIGHT_CLASS


def ability_weights(
		char,
		pool=None,
		amount: int = 1,
		) -> dict[str, int]:
	"""
	How much this Character wants each ability raised, as a weight.

	``amount`` is the size of the raise being considered, because parity is
	worth nothing in the abstract: +1 lands an odd score on an even one, and
	+2 lands an even one.  Passing the real amount is what lets a single rule
	replace the old +2/+1 special case.
	"""
	keys = tuple(
		pool
		or (
			"STR",