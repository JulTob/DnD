"""
Learned spells stay put as a character levels up.

The sheet ± buttons reuse the same seed. Spell picks must not reshuffle:
each new level only adds spells. A dedicated RNG (not the main character
RNG) is used so other random rolls cannot steal the sequence.
"""
import random as stdlib_random

CLASS_SALT = {
	"Wizard": 1,
	"Druid": 2,
	"Ranger": 3,
	"Sorcerer": 4,
	"Warlock": 5,
	"Eldritch Knight": 6,
	"Arcane Trickster": 7,
	"Paladin": 8,
	"Bard": 9,
	"Cleric": 10,
	"Monk": 11,
	}


def spell_level(spell):
	try:
		return int(getattr(spell, "level", 0) or 0)
	except (TypeError, ValueError):
		return 0


def spell_key(spell):
	return str(getattr(spell, "name", "")).strip()


def unique_spells(spells):
	seen = set()
	out = []
	for spell in spells or []:
		if spell is None:
			continue
		key = spell_key(spell)
		if not key or key in seen:
			continue
		seen.add(key)
		out.append(spell)
	return out


def spell_mark(spell, prepared=True):
	level = spell_level(spell)
	name = spell_key(spell)
	if prepared:
		return f"【{level}】{name}"
	return f"〖{level}〗{name}"


def caster_rng(character, salt=0):
	try:
		seed = int(getattr(character, "seed", 0) or 0)
	except (TypeError, ValueError):
		seed = 0
	return stdlib_random.Random((seed << 16) ^ int(salt))


def pick_new(pool, n, rng, already):
	candidates = [
		spell for spell in unique_spells(pool)
		if spell_key(spell) not in already
		]
	rng.shuffle(candidates)
	return candidates[:max(0, n)]


def max_slot_from(slots):
	if isinstance(slots, dict):
		levels = [lvl for lvl, n in slots.items() if n]
		return max(levels) if levels else 0
	if isinstance(slots, (tuple, list)):
		levels = [i + 1 for i, n in enumerate(slots) if n]
		return max(levels) if levels else 0
	return 0


def stats_at_level(caster, lvl, key):
	"""Read a caster table row for a walked level without leaving the live level changed."""
	previous = getattr(caster, "level", 1)
	caster.level = min(max(int(lvl), 1), 20)
	try:
		return caster.get_stats(key)
	finally:
		caster.level = previous


def progressive_learn(
		character,
		table,
		level,
		cantrips_at,
		known_at,
		slots_at,
		salt=1,
		always=None,
		):
	"""
	Walk levels 1..level. At each step, only add the newly granted
	cantrips and leveled spells. Prefer the newly unlocked slot level.
	"""
	rng = caster_rng(character, salt)
	cantrips = []
	known = []
	already = set()
	for spell in unique_spells(always):
		if spell_level(spell) == 0:
			cantrips.append(spell)
		else:
			known.append(spell)
		already.add(spell_key(spell))
	table = table or {}
	for lvl in range(1, max(1, int(level)) + 1):
		n_cantrips = cantrips_at(lvl)
		n_known = known_at(lvl)
		max_slot = max_slot_from(slots_at(lvl))
		if n_cantrips > len(cantrips):
			added = pick_new(table.get(0, []), n_cantrips - len(cantrips), rng, already)
			cantrips.extend(added)
			already.update(spell_key(spell) for spell in added)
		if n_known > len(known):
			need = n_known - len(known)
			added = []
			if max_slot >= 1:
				added = pick_new(table.get(max_slot, []), need, rng, already)
			if len(added) < need:
				pool = []
				for slot in range(1, max_slot + 1):
					pool.extend(table.get(slot, []))
				added.extend(pick_new(pool, need - len(added), rng, already))
			known.extend(added)
			already.update(spell_key(spell) for spell in added)
	return cantrips, known


def finish_learning(caster, cantrips, known, prepared_count=None):
	"""Store a growing known list. Prepared is a stable prefix, never reshuffled."""
	if getattr(caster, "granted_spells", None) is None:
		caster.granted_spells = []
	if getattr(caster, "always_prepared", None) is None:
		caster.always_prepared = set()
	cantrips = unique_spells(cantrips)
	known = unique_spells(known)
	caster.spells_known = unique_spells(list(cantrips) + list(known))
	if prepared_count is None:
		caster.prepared_spells = list(caster.spells_known)
	else:
		caster.prepared_spells = unique_spells(list(cantrips) + list(known)[:max(0, int(prepared_count))])
	return caster.spells_known


def grant_spell(character, spell, always_prepared=True):
	"""Attach a feature-granted spell to the sheet catalog. Does not replace learned spells."""
	if spell is None or character is None:
		return
	caster = getattr(character, "spellcaster", None)
	if caster is None:
		return
	if getattr(caster, "granted_spells", None) is None:
		caster.granted_spells = []
	if getattr(caster, "always_prepared", None) is None:
		caster.always_prepared = set()
	key = spell_key(spell)
	if not key:
		return
	have = {spell_key(item) for item in catalog_spells(caster)}
	if key not in have:
		caster.granted_spells.append(spell)
	if always_prepared:
		caster.always_prepared.add(key)


def catalog_spells(caster):
	granted = list(getattr(caster, "granted_spells", []) or [])
	if getattr(caster, "catalog_known", True):
		known = list(getattr(caster, "spells_known", []) or [])
		return unique_spells(known + granted)
	return unique_spells(granted)


def prepared_keys(caster):
	prepared = getattr(caster, "prepared_spells", None)
	if prepared is None:
		keys = {spell_key(spell) for spell in getattr(caster, "spells_known", []) or []}
	else:
		keys = {spell_key(spell) for spell in prepared}
	keys |= set(getattr(caster, "always_prepared", set()) or [])
	return keys


def html_spell_index(caster, bullet="🪄"):
	spells = catalog_spells(caster)
	spells.sort(key=lambda spell: (spell_level(spell), spell_key(spell)))
	prepared = prepared_keys(caster)
	items = []
	for spell in spells:
		is_prepared = spell_key(spell) in prepared or spell_level(spell) == 0
		items.append(f"<li>{spell_mark(spell, prepared=is_prepared)}</li>")
	if not items:
		return ""
	return f"""<ul style="list-style-type: '{bullet}'; text-align: left; font-family: 'Iglesia'">{"".join(items)}</ul>"""


def html_spell_catalog(caster):
	"""Full writeups, one block each, at the end of the sheet."""
	spells = catalog_spells(caster)
	spells.sort(key=lambda spell: (spell_level(spell), spell_key(spell)))
	if not spells:
		return ""
	prepared = prepared_keys(caster)
	blocks = [
		"""<div class="npc-textbox" style="grid-column: 1 / -1;">
			<h1 style="font-family: 'Iglesia'; font-size: 2.4em;">Spells</h1>
			<p>【prepared / always available】 &nbsp; 〖written or granted, not prepared】</p>
			</div>"""
		]
	for spell in spells:
		is_prepared = spell_key(spell) in prepared or spell_level(spell) == 0
		blocks.append(
			f"""<div class="npc-textbox">{spell_mark(spell, prepared=is_prepared)}<br>{spell}</div>"""
			)
	return "".join(blocks)


def pick_magic_initiate(character, list_name):
	from AtlasLusoris.Grimoire_of_Spellcasters import SPELL_LISTS
	table = SPELL_LISTS.get(list_name) or {}
	if not any(table.values()):
		table = SPELL_LISTS.get("Wizard", {})
	cantrips, leveled = progressive_learn(
		character,
		table,
		level=1,
		cantrips_at=lambda lvl: 2,
		known_at=lambda lvl: 1,
		slots_at=lambda lvl: (1,),
		salt=0x1A1 ^ CLASS_SALT.get(list_name, 0),
		)
	return unique_spells(cantrips + leveled)


def names_line(spells, prepared=True):
	return ", ".join(spell_mark(spell, prepared=prepared) for spell in unique_spells(spells))
