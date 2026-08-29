def Build_Weapon(
		*,
		name: str,
		damage: str,
		damage_type: str = "Bludgeoning",
		category: str = "Simple",
		reach: str = "Melee",
		mastery: str = "",
		properties: tuple[str, ...] = (),
		value: float = 0,
		weight: float = 0,
		description: str = "",
		grants: dict[str, int] | None = None,
		attack_with: str = "",
		) -> Item:
	"""Craft a weapon. ``category`` gates proficiency, ``mastery`` its property.

	``category="Firearm"`` tags ``Firearm`` instead of the plain ``Weapon`` —
	Firearm IS-A Weapon (Tag inheritance), so ``item in Weapon`` still holds,
	but a Martial-proficient character does not get firearms for free.

	``attack_with`` names the ability this weapon attacks with when it is NOT
	the usual Strength/Dexterity rule — "Intelligence", "Wisdom", "Charisma".
	Julio (2026-08-05): "for magic users it would make sense to have some
	weapons that attack with int/wis/cha, to make them more usable… It should
	be clearly described in the description which one is using." So it is
	stored as a field and printed in the blurb, never left to prose alone.
	"""
	tags: list[type[Tag]] = [
			Firearm
			if category == "Firearm"
			else Weapon,
			]
	tags.append(
			Simple
			if category == "Simple"
			else Martial
			)
	tags.append(
			Ranged
			if reach == "Ranged"
			else Melee
			)

	item = Build_Item(
			name=name,
			value=value,
			weight=weight,
			description=description,
			grants=grants,
			tags=tuple(
					tags
					),
			)
	item.damage = damage
	item.damage_type = damage_type
	item.category = category
	item.reach = reach
	item.mastery = mastery
	item.attack_with = attack_with
	item.properties = tuple(
			properties
			)
	return item


# ---------------------------------------------------------------------------
# Owning, equipping, selling
# ---------------------------------------------------------------------------