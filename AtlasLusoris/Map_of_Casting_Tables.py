"""2024 PHB spellcasting columns, one table per class.

Lists of spells stay in Grimoire_of_Spellcasters. These rows are only
cantrips, prepared counts, and slots. Same shape, class as the key —
so a new caster is a table, not a new get_stats method.
"""

# Full casters share this slot column except Druid from 18 up.
_FULL_SLOTS = {
	1:  (2, 0, 0, 0, 0, 0, 0, 0, 0),
	2:  (3, 0, 0, 0, 0, 0, 0, 0, 0),
	3:  (4, 2, 0, 0, 0, 0, 0, 0, 0),
	4:  (4, 3, 0, 0, 0, 0, 0, 0, 0),
	5:  (4, 3, 2, 0, 0, 0, 0, 0, 0),
	6:  (4, 3, 3, 0, 0, 0, 0, 0, 0),
	7:  (4, 3, 3, 1, 0, 0, 0, 0, 0),
	8:  (4, 3, 3, 2, 0, 0, 0, 0, 0),
	9:  (4, 3, 3, 3, 1, 0, 0, 0, 0),
	10: (4, 3, 3, 3, 2, 0, 0, 0, 0),
	11: (4, 3, 3, 3, 2, 1, 0, 0, 0),
	12: (4, 3, 3, 3, 2, 1, 0, 0, 0),
	13: (4, 3, 3, 3, 2, 1, 1, 0, 0),
	14: (4, 3, 3, 3, 2, 1, 1, 0, 0),
	15: (4, 3, 3, 3, 2, 1, 1, 1, 0),
	16: (4, 3, 3, 3, 2, 1, 1, 1, 0),
	17: (4, 3, 3, 3, 2, 1, 1, 1, 1),
	18: (4, 3, 3, 3, 3, 1, 1, 1, 1),
	19: (4, 3, 3, 3, 3, 2, 1, 1, 1),
	20: (4, 3, 3, 3, 3, 2, 2, 1, 1),
	}

# Druid 18–20: two 5th-level slots, not three; 18 has one 6th, 20 has two 6th.
_DRUID_SLOTS = dict(_FULL_SLOTS)
_DRUID_SLOTS[18] = (4, 3, 3, 3, 2, 1, 1, 1, 1)
_DRUID_SLOTS[19] = (4, 3, 3, 3, 2, 1, 1, 1, 1)
_DRUID_SLOTS[20] = (4, 3, 3, 3, 2, 2, 1, 1, 1)


def _full(cantrips, prepared, slots=_FULL_SLOTS):
	return {
		lvl: {
			"cantrips": cantrips[lvl],
			"prepared": prepared[lvl],
			"slots": slots[lvl],
			}
		for lvl in range(1, 21)
		}


# Wizard: 3 cantrips, +1 at 4 and 10. Prepared 4…25.
_WIZARD_CANTRIPS = {lvl: 3 if lvl < 4 else 4 if lvl < 10 else 5 for lvl in range(1, 21)}
_WIZARD_PREPARED = {
	1: 4, 2: 5, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 14, 10: 15,
	11: 16, 12: 16, 13: 17, 14: 18, 15: 19, 16: 21, 17: 22, 18: 23, 19: 24, 20: 25,
	}

# Sorcerer: 4 cantrips, +1 at 4 and 10. Prepared starts at 2.
_SORCERER_CANTRIPS = {lvl: 4 if lvl < 4 else 5 if lvl < 10 else 6 for lvl in range(1, 21)}
_SORCERER_PREPARED = {
	1: 2, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 14, 10: 15,
	11: 16, 12: 16, 13: 17, 14: 17, 15: 18, 16: 18, 17: 19, 18: 20, 19: 21, 20: 22,
	}

# Druid: 2 cantrips, +1 at 4 and 10. Prepared 4…22.
_DRUID_CANTRIPS = {lvl: 2 if lvl < 4 else 3 if lvl < 10 else 4 for lvl in range(1, 21)}
_DRUID_PREPARED = {
	1: 4, 2: 5, 3: 6, 4: 7, 5: 9, 6: 10, 7: 11, 8: 12, 9: 14, 10: 15,
	11: 16, 12: 16, 13: 17, 14: 17, 15: 18, 16: 18, 17: 19, 18: 20, 19: 21, 20: 22,
	}

CASTING = {
	"Wizard": _full(_WIZARD_CANTRIPS, _WIZARD_PREPARED),
	"Sorcerer": _full(_SORCERER_CANTRIPS, _SORCERER_PREPARED),
	"Druid": _full(_DRUID_CANTRIPS, _DRUID_PREPARED, _DRUID_SLOTS),
	"Ranger": {
		1:  {"prepared": 2,  "slots": (2, 0, 0, 0, 0)},
		2:  {"prepared": 3,  "slots": (2, 0, 0, 0, 0)},
		3:  {"prepared": 4,  "slots": (3, 0, 0, 0, 0)},
		4:  {"prepared": 5,  "slots": (3, 0, 0, 0, 0)},
		5:  {"prepared": 6,  "slots": (4, 2, 0, 0, 0)},
		6:  {"prepared": 6,  "slots": (4, 2, 0, 0, 0)},
		7:  {"prepared": 7,  "slots": (4, 3, 0, 0, 0)},
		8:  {"prepared": 7,  "slots": (4, 3, 0, 0, 0)},
		9:  {"prepared": 8,  "slots": (4, 3, 2, 0, 0)},
		10: {"prepared": 8,  "slots": (4, 3, 2, 0, 0)},
		11: {"prepared": 10, "slots": (4, 3, 3, 0, 0)},
		12: {"prepared": 10, "slots": (4, 3, 3, 0, 0)},
		13: {"prepared": 11, "slots": (4, 3, 3, 1, 0)},
		14: {"prepared": 11, "slots": (4, 3, 3, 1, 0)},
		15: {"prepared": 12, "slots": (4, 3, 3, 2, 0)},
		16: {"prepared": 12, "slots": (4, 3, 3, 2, 0)},
		17: {"prepared": 14, "slots": (4, 3, 3, 3, 1)},
		18: {"prepared": 14, "slots": (4, 3, 3, 3, 1)},
		19: {"prepared": 15, "slots": (4, 3, 3, 3, 2)},
		20: {"prepared": 15, "slots": (4, 3, 3, 3, 2)},
		},
	"Warlock": {
		1:  {"cantrips": 2, "prepared": 2,  "slots": 1, "slot_level": 1},
		2:  {"cantrips": 2, "prepared": 3,  "slots": 2, "slot_level": 1},
		3:  {"cantrips": 2, "prepared": 4,  "slots": 2, "slot_level": 2},
		4:  {"cantrips": 3, "prepared": 5,  "slots": 2, "slot_level": 2},
		5:  {"cantrips": 3, "prepared": 6,  "slots": 2, "slot_level": 3},
		6:  {"cantrips": 3, "prepared": 7,  "slots": 2, "slot_level": 3},
		7:  {"cantrips": 3, "prepared": 8,  "slots": 2, "slot_level": 4},
		8:  {"cantrips": 3, "prepared": 9,  "slots": 2, "slot_level": 4},
		9:  {"cantrips": 3, "prepared": 10, "slots": 2, "slot_level": 5},
		10: {"cantrips": 4, "prepared": 10, "slots": 2, "slot_level": 5},
		11: {"cantrips": 4, "prepared": 11, "slots": 3, "slot_level": 5},
		12: {"cantrips": 4, "prepared": 11, "slots": 3, "slot_level": 5},
		13: {"cantrips": 4, "prepared": 12, "slots": 3, "slot_level": 5},
		14: {"cantrips": 4, "prepared": 12, "slots": 3, "slot_level": 5},
		15: {"cantrips": 4, "prepared": 13, "slots": 3, "slot_level": 5},
		16: {"cantrips": 4, "prepared": 13, "slots": 3, "slot_level": 5},
		17: {"cantrips": 4, "prepared": 14, "slots": 4, "slot_level": 5},
		18: {"cantrips": 4, "prepared": 14, "slots": 4, "slot_level": 5},
		19: {"cantrips": 4, "prepared": 15, "slots": 4, "slot_level": 5},
		20: {"cantrips": 4, "prepared": 15, "slots": 4, "slot_level": 5},
		},
	}

# Empty class lists inherit another list until tagged per-spell lists exist.
LIST_FALLBACK = {
	"Sorcerer": "Wizard",
	}


def casting_row(class_name, level):
	table = CASTING.get(class_name) or {}
	lvl = min(max(int(level or 1), 1), 20)
	return table.get(lvl) or table.get(20) or {}


def slots_as_map(slots):
	if isinstance(slots, dict):
		return {lvl: n for lvl, n in slots.items() if n}
	if isinstance(slots, (tuple, list)):
		return {i + 1: n for i, n in enumerate(slots) if n}
	return {}
