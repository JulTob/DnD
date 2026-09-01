"""Project-original seed catalogue for NonPlayer tactical Features.

No Monster Manual or 5e.tools prose is copied here.  External adaptations
must enter with explicit provenance through :class:`Feature_Spec`.
"""

from __future__ import annotations

from types import MappingProxyType

from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Activation
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Build_Feature_Tag
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Chip_Spec
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Feature_Spec
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Tactical_Role


CATALOG_VERSION = "npc-tactics-2"

FEATURE_SPECS = (
		Feature_Spec(
				key="steady_anchor",
				title="Steady Anchor",
				activation=Activation.TRAIT,
				tactical_roles=(
						Tactical_Role.DEFENSE,
						),
				description_template="When an effect would push, pull, or knock this NPC down, it adds {pb} to the check or save made to resist that movement.",
				affinities=(
						"construct",
						"giant",
						"guardian",
						"knight",
						"soldier",
						),
				chips=(
						Chip_Spec(
								key="stability",
								label="Stability",
								value_template="+{pb}",
								icon="⚓",
								),
						),
				),
		Feature_Spec(
				key="coordinated_pressure",
				title="Coordinated Pressure",
				activation=Activation.TRAIT,
				tactical_roles=(
						Tactical_Role.OFFENSE,
						Tactical_Role.COMMAND,
						),
				description_template="Once each round after this NPC hits a creature, the next ally to hit that creature before this NPC's next turn deals {pb} extra damage.",
				affinities=(
						"bard",
						"fighter",
						"hunter",
						"mentor",
						"soldier",
						"spy",
						),
				),
		Feature_Spec(
				key="driving_break",
				title="Driving Break",
				activation=Activation.ACTION,
				tactical_roles=(
						Tactical_Role.OFFENSE,
						Tactical_Role.CONTROL,
						),
				description_template="After moving at least 10 feet in a straight line, this NPC makes one attack. On a hit, the target must resist the NPC's save DC or move 10 feet in the same direction.",
				affinities=(
						"barbarian",
						"berserker",
						"dragon",
						"fighter",
						"giant",
						"warrior",
						),
				),
		Feature_Spec(
				key="binding_arc",
				title="Binding Arc",
				activation=Activation.ACTION,
				tactical_roles=(
						Tactical_Role.CONTROL,
						),
				description_template="Choose a creature within 30 feet. It must resist the NPC's save DC or its speed is reduced by 10 feet until the end of its next turn.",
				affinities=(
						"druid",
						"primal",
						"plant",
						"shaman",
						"witch",
						),
				),
		Feature_Spec(
				key="thought_static",
				title="Thought Static",
				activation=Activation.ACTION,
				tactical_roles=(
						Tactical_Role.DISRUPTION,
						),
				description_template="One creature within 60 feet must resist the NPC's save DC. On a failure, it subtracts {pb} from its next concentration check before the end of its next turn.",
				affinities=(
						"aberration",
						"arcane",
						"mage",
						"occult",
						"spellcaster",
						"warlock",
						"witch",
						"wizard",
						),
				requires_any=(
						"aberration",
						"arcane",
						"mage",
						"occult",
						"spellcaster",
						"warlock",
						"witch",
						"wizard",
						),
				),
		Feature_Spec(
				key="rally_vector",
				title="Rally Vector",
				activation=Activation.ACTION,
				tactical_roles=(
						Tactical_Role.SUPPORT,
						Tactical_Role.COMMAND,
						),
				description_template="Choose up to {pb} allies who can hear this NPC. Each chosen ally may move 5 feet without spending its reaction.",
				affinities=(
						"bard",
						"cleric",
						"divine",
						"hero",
						"mentor",
						"noble",
						"paladin",
						"priest",
						),
				),
		Feature_Spec(
				key="veil_stride",
				title="Veil Stride",
				activation=Activation.BONUS_ACTION,
				tactical_roles=(
						Tactical_Role.MOBILITY,
						),
				description_template="This NPC moves up to 10 feet to an unoccupied space it can see. This movement ignores creatures and does not trigger reactions.",
				affinities=(
						"fey",
						"fiend",
						"ninja",
						"rogue",
						"spy",
						"trickster",
						"occult",
						"warlock",
						),
				),
		Feature_Spec(
				key="hold_the_angle",
				title="Hold the Angle",
				activation=Activation.BONUS_ACTION,
				tactical_roles=(
						Tactical_Role.DEFENSE,
						Tactical_Role.COMMAND,
						),
				description_template="Choose an adjacent ally. Until the start of this NPC's next turn, the first attack against that ally is reduced by {pb}.",
				affinities=(
						"fighter",
						"guardian",
						"knight",
						"paladin",
						"soldier",
						),
				),
		Feature_Spec(
				key="field_patch",
				title="Field Patch",
				activation=Activation.BONUS_ACTION,
				tactical_roles=(
						Tactical_Role.SUSTAIN,
						Tactical_Role.SUPPORT,
						),
				description_template="A creature within reach regains {pb} hit points. A creature can benefit from Field Patch only once per encounter.",
				affinities=(
						"artisan",
						"crafter",
						"doctor",
						"healer",
						"hermit",
						"priest",
						),
				),
		Feature_Spec(
				key="guarding_intercept",
				title="Guarding Intercept",
				activation=Activation.REACTION,
				tactical_roles=(
						Tactical_Role.DEFENSE,
						Tactical_Role.SUPPORT,
						),
				description_template="When an ally within 5 feet takes damage, this NPC reduces that damage by {pb} and may exchange places with the ally.",
				affinities=(
						"fighter",
						"guardian",
						"knight",
						"paladin",
						"soldier",
						),
				uniqueness_group="protective_reaction",
				),
		Feature_Spec(
				key="counterstep",
				title="Counterstep",
				activation=Activation.REACTION,
				tactical_roles=(
						Tactical_Role.MOBILITY,
						),
				description_template="When a creature misses this NPC with an attack, the NPC moves up to {pb} × 5 feet without triggering a reaction from that creature.",
				affinities=(
						"artist",
						"bard",
						"ninja",
						"rogue",
						"spy",
						"trickster",
						),
				),
		Feature_Spec(
				key="predatory_focus",
				title="Predatory Focus",
				activation=Activation.ACTION,
				tactical_roles=(
						Tactical_Role.OFFENSE,
						),
				description_template="Choose one visible creature. Until the end of this NPC's next turn, its first hit against that target deals {pb} extra damage.",
				affinities=(
						"beast",
						"dragon",
						"hunter",
						"ranger",
						"vampire",
						),
				),
		Feature_Spec(
				key="prepared_escape",
				title="Prepared Escape",
				activation=Activation.BONUS_ACTION,
				tactical_roles=(
						Tactical_Role.MOBILITY,
						Tactical_Role.UTILITY,
						),
				description_template="The NPC uses a previously identified route, cover, or distraction. It may Dash or Disengage, but must end the movement farther from its nearest enemy.",
				affinities=(
						"bandit",
						"criminal",
						"pirate",
						"traveler",
						"wayfarer",
						),
				),
		Feature_Spec(
				key="tactical_appraisal",
				title="Tactical Appraisal",
				activation=Activation.ACTION,
				tactical_roles=(
						Tactical_Role.UTILITY,
						Tactical_Role.SUPPORT,
						),
				description_template="Study one visible creature. The NPC learns whether one chosen defense, save, or movement speed is higher, lower, or equal to its own.",
				affinities=(
						"expert",
						"mage",
						"mentor",
						"sage",
						"scholar",
						"scribe",
						"wizard",
						),
				),
		Feature_Spec(
				key="last_reserve",
				title="Last Reserve",
				activation=Activation.REACTION,
				tactical_roles=(
						Tactical_Role.DEFENSE,
						Tactical_Role.SUSTAIN,
						),
				description_template="When damage would reduce this NPC below half its hit points, it gains {pb} temporary hit points. It can do so once per encounter.",
				affinities=(
						"barbarian",
						"berserker",
						"commoner",
						"hero",
						"warrior",
						),
				uniqueness_group="protective_reaction",
				),
		Feature_Spec(
				key="elemental_pressure",
				title="Elemental Pressure",
				activation=Activation.ACTION,
				tactical_roles=(
						Tactical_Role.OFFENSE,
						Tactical_Role.CONTROL,
						),
				description_template="Choose a 10-foot area within 60 feet. Creatures in it must resist the NPC's save DC or take {pb} damage and treat the area as difficult terrain until the NPC's next turn.",
				affinities=(
						"dragon",
						"druid",
						"elemental",
						"evocation",
						"fire",
						"lightning",
						"primal",
						"shaman",
						"sorcerer",
						),
				requires_any=(
						"dragon",
						"druid",
						"elemental",
						"shaman",
						"sorcerer",
						),
				),
		Feature_Spec(
				key="unstable_formula",
				title="Unstable Formula",
				activation=Activation.ACTION,
				tactical_roles=(
						Tactical_Role.OFFENSE,
						Tactical_Role.UTILITY,
						),
				description_template="Choose acid, cold, fire, lightning, or thunder. Until the end of the NPC's next turn, one of its attacks deals {pb} extra damage of that type.",
				affinities=(
						"arcane",
						"artisan",
						"construct",
						"crafter",
						"evocation",
						"fire",
						"magic",
						"mage",
						"sorcerer",
						"wizard",
						),
				),
		)

FEATURES_BY_KEY = MappingProxyType(
		{
				spec.key: spec
				for spec in FEATURE_SPECS
				}
		)

if len(FEATURES_BY_KEY) != len(FEATURE_SPECS):
	raise ValueError(
			"NonPlayer tactical Feature keys must be unique."
			)

FEATURE_TAGS = MappingProxyType(
		{
				spec.key: Build_Feature_Tag(
						spec
						)
				for spec in FEATURE_SPECS
				}
		)

for _tag in FEATURE_TAGS.values():
	globals()[
			_tag.__name__
			] = _tag

__all__ = (
		"CATALOG_VERSION",
		"FEATURES_BY_KEY",
		"FEATURE_SPECS",
		"FEATURE_TAGS",
		) + tuple(
		tag.__name__
		for tag in FEATURE_TAGS.values()
		)
