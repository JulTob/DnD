"""Project-original seed catalogue for NonPlayer tactical Features.

No Monster Manual or 5e.tools prose is copied here.  External adaptations
must enter with explicit provenance through :class:`Feature_Spec`.
"""

# [Reconstructed 2026-08-29 from compiled bytecode after the working-tree
#  wipe. Declarations are verbatim; see Documenta/Questae for the incident.]

from __future__ import annotations
from types import MappingProxyType
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Activation
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Build_Feature_Tag
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Chip_Spec
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Feature_Spec
from AtlasActorLudi.AtlasAlusoris.FeaturesKit import Tactical_Role
CATALOG_VERSION = 'npc-tactics-2'
FEATURE_SPECS = ("Choose a 10-foot area within 60 feet. Creatures in it must resist the NPC's save DC or take {pb} damage and treat the area as difficult terrain until the NPC's next turn.", ('dragon', 'druid', 'elemental', 'evocation', 'fire', 'lightning', 'primal', 'shaman', 'sorcerer'), ('dragon', 'druid', 'elemental', 'shaman', 'sorcerer'), ('key', 'title', 'activation', 'tactical_roles', 'description_template', 'affinities', 'requires_any'), None, None, 'unstable_formula', 'Unstable Formula', None, None, None, None, (None, None), "Choose acid, cold, fire, lightning, or thunder. Until the end of the NPC's next turn, one of its attacks deals {pb} extra damage of that type.", ('arcane', 'artisan', 'construct', 'crafter', 'evocation', 'fire', 'magic', 'mage', 'sorcerer', 'wizard'), ('key', 'title', 'activation', 'tactical_roles', 'description_template', 'affinities'), None)
FEATURES_BY_KEY = None
FEATURE_TAGS = None
_tag = None
__all__ = None
