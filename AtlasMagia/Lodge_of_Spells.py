# Lodge of Spells
import random

try:
    from AtlasLudus.Map_of_Dice import Dice
    from AtlasActorLudi.Map_of_Scores import PB, Modifier
    from AtlasScriptum.Map_of_Formats import Entry

except ImportError:
    raise

# Consolidated 2024 spell list
SPELL_DATA_2024 = {
    "Acid Splash": {
        "level": 0,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You conjure a glob of corrosive acid that bursts on impact. One or two "
            "creatures you can see within 5 feet of each other must make a Dexterity "
            "save or take 1d6 acid damage (scaling with level)."
        ),
    },
    "Animate Dead": {
        "level": 3,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "10 feet",
        "duration": "Instantaneous",
        "components": "V, S, M (a drop of blood, a piece of flesh, and a pinch of bone dust)",
        "concentration": "",
        "definition": (
            "You raise a corpse or pile of bones as a zombie or skeleton under your "
            "control for 24 hours, commanding up to four undead with higher-slot casts."
        ),
    },
    "Antagonize": {
        "level": 3,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You goad a creature into reckless aggression. On a failed Wisdom save, "
            "the target has disadvantage on attacks against creatures other than you, "
            "and allies have advantage to strike it until the spell ends."
        ),
    },
    "Arcane Eye": {
        "level": 4,
        "school": "Divination",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a bit of bat fur)",
        "concentration": "Concentration",
        "definition": (
            "You create an invisible, floating eye that you can move with your "
            "thoughts, seeing through it in any direction while it scouts out to 30 feet per round."
        ),
    },
    "Ashardalon's Stride": {
        "level": 3,
        "school": "Transmutation",
        "casting_time": "Bonus Action",
        "range": "Self",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "Fiery vitality surges through you. Your speed increases by 20 feet, you "
            "ignore opportunity attacks, and creatures you pass take 1d6 fire damage "
            "(scaling with slot) unless they save."
        ),
    },
    "Aura of Life": {
        "level": 4,
        "school": "Abjuration",
        "casting_time": "Action",
        "range": "Self (30-foot radius)",
        "duration": "Concentration, up to 10 minutes",
        "components": "V",
        "concentration": "Concentration",
        "definition": (
            "You emit a vital aura that grants resistance to necrotic damage, "
            "prevents max hit point reduction, and automatically stabilises allies "
            "in the area who start their turn at 0 hit points."
        ),
    },
    "Aura of Purity": {
        "level": 4,
        "school": "Abjuration",
        "casting_time": "Action",
        "range": "Self (30-foot radius)",
        "duration": "Concentration, up to 10 minutes",
        "components": "V",
        "concentration": "Concentration",
        "definition": (
            "A cleansing aura surrounds you, granting allies advantage on saves "
            "against disease and poison while reducing poison damage in your radius."
        ),
    },
    "Aura of Vitality": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "Self (30-foot radius)",
        "duration": "Concentration, up to 1 minute",
        "components": "V",
        "concentration": "Concentration",
        "definition": (
            "A surge of healing energy pulses from you. As a bonus action while the "
            "spell lasts, you can restore 2d6 hit points to a creature in the aura."
        ),
    },
    "Beacon of Hope": {
        "level": 3,
        "school": "Abjuration",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You bestow hope and resilience on allies, granting advantage on Wisdom "
            "and death saves, plus maximised healing they receive for the duration."
        ),
    },
    "Bestow Curse": {
        "level": 3,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Concentration, up to 1 minute (or longer with higher slots)",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "On a failed Wisdom save, you afflict a creature with a tailored curse, "
            "such as disadvantage on chosen ability checks and saves or wasting its actions."
        ),
    },
    "Blinding Smite": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "Bonus Action",
        "range": "Self",
        "duration": "Concentration, up to 1 minute",
        "components": "V",
        "concentration": "Concentration",
        "definition": (
            "Your next melee weapon hit blazes with radiant force for +3d8 damage, and "
            "the target must save or be blinded until the spell ends."
        ),
    },
    "Booming Blade": {
        "level": 0,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "Self",
        "duration": "1 round",
        "components": "S, M (a melee weapon worth at least 1 sp)",
        "concentration": "",
        "definition": (
            "As part of the spell you make a melee attack. On a hit the target takes "
            "thunder damage if it willingly moves before your next turn, with both the "
            "initial hit and rider scaling by tier."
        ),
    },
    "Catnap": {
        "level": 3,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "10 minutes",
        "components": "S, M (a pinch of sand)",
        "concentration": "",
        "definition": (
            "Up to three willing creatures fall into a magical doze for 10 minutes, "
            "gaining the benefits of a short rest and ending effects that would stop "
            "them from resting when the spell concludes."
        ),
    },
    "Charm Monster": {
        "level": 4,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "1 hour",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You beguile a creature of any type. On a failed Wisdom save it regards you "
            "as a trusted ally for the duration, though it gains advantage if you or your "
            "companions are fighting it."
        ),
    },
    "Clairvoyance": {
        "level": 3,
        "school": "Divination",
        "casting_time": "10 minutes",
        "range": "1 mile",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S, M (a focus worth at least 100 gp)",
        "concentration": "Concentration",
        "definition": (
            "You create an invisible sensor that either sees or hears within range, "
            "located in a familiar place or one you describe."
        ),
    },
    "Cloudkill": {
        "level": 5,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You create a mobile 20-foot-radius fog of poison. Creatures inside take 5d8 "
            "poison damage on a failed Constitution save (half on success) each round as the cloud rolls away from you."
        ),
    },
    "Compulsion": {
        "level": 4,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You sway targets in a radius to dance in place. Creatures that fail a Wisdom "
            "save must use their movement to head in a horizontal direction of your choice on each turn."
        ),
    },
    "Conjure Animals": {
        "level": 3,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You summon fey spirits that take beast forms, creating one or more creatures "
            "whose challenge rating scales with the slot used to aid you."
        ),
    },
    "Conjure Barrage": {
        "level": 3,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "Self (60-foot cone)",
        "duration": "Instantaneous",
        "components": "V, S, M (a ranged weapon worth at least 1 sp)",
        "concentration": "",
        "definition": (
            "You launch a spray of spectral missiles that deals 3d8 damage of the weapon's "
            "type to creatures in a wide cone, Dexterity half."
        ),
    },
    "Conjure Minor Elementals": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "1 minute",
        "range": "90 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You summon elemental spirits that adopt small or medium elemental stat blocks, "
            "with the number and CR scaling by slot level to fight for you."
        ),
    },
    "Conjure Woodland Beings": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "1 minute",
        "range": "60 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (one holly berry per creature summoned)",
        "concentration": "Concentration",
        "definition": (
            "Fey spirits take the form of beasts or fey creatures, with the total CR tied to "
            "the spell slot, and obey your verbal commands for the duration."
        ),
    },
    "Control Water": {
        "level": 4,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "300 feet",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S, M (a drop of water and a pinch of dust)",
        "concentration": "Concentration",
        "definition": (
            "You manipulate a large body of water, creating floods, parting water, reversing "
            "currents, or forming standing waves within a 100-foot cube."
        ),
    },
    "Countercharm": {
        "level": 3,
        "school": "Abjuration",
        "casting_time": "Reaction",
        "range": "60 feet",
        "duration": "Instantaneous",
        "components": "V",
        "concentration": "",
        "definition": (
            "You break an enchantment that would charm or frighten your allies. When a "
            "creature within range makes a save against those conditions, you grant it "
            "advantage and can immediately end such an effect on it."
        ),
    },
    "Crusader's Mantle": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "Self (30-foot radius)",
        "duration": "Concentration, up to 1 minute",
        "components": "V",
        "concentration": "Concentration",
        "definition": (
            "Holy energy radiates from you. Allies in the aura deal an extra 1d4 radiant "
            "damage with weapon attacks while the spell persists."
        ),
    },
    "Daylight": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "1 hour",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You create a 60-foot-radius sphere of bright light that dispels lower-level "
            "darkness. The light can be moved if centred on an object you carry."
        ),
    },
    "Death Ward": {
        "level": 4,
        "school": "Abjuration",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "8 hours",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You protect a creature from death once. The first time it would drop to 0 hit "
            "points, it instead falls to 1, or it ignores an effect that would kill it outright."
        ),
    },
    "Demiplane": {
        "level": 8,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "1 hour",
        "components": "S",
        "concentration": "",
        "definition": (
            "You create a shadowy door leading to a 30-foot cubic extradimensional chamber. "
            "Repeated castings can link multiple chambers for storage or meeting."
        ),
    },
    "Dimension Door": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "500 feet",
        "duration": "Instantaneous",
        "components": "V",
        "concentration": "",
        "definition": (
            "You teleport yourself and one willing creature to any spot within range you can "
            "visualise or describe by distance and direction."
        ),
    },
    "Dispel Magic": {
        "level": 3,
        "school": "Abjuration",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "Choose a creature, object, or effect. Any spell of 3rd level or lower ends, and "
            "higher-level spells require an ability check to dispel."
        ),
    },
    "Divination": {
        "level": 4,
        "school": "Divination",
        "casting_time": "Action",
        "range": "Self",
        "duration": "Instantaneous",
        "components": "V, S, M (incense and a sacrificial offering worth 25 gp)",
        "concentration": "",
        "definition": (
            "You ask a single question about a goal, event, or activity within the next 7 days, "
            "receiving a truthful omen from your deity."
        ),
    },
    "Dominate Beast": {
        "level": 4,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You charm a beast, gaining complete control on subsequent turns if it fails its "
            "Wisdom save. Using higher slots extends the duration."
        ),
    },
    "Dominate Monster": {
        "level": 8,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You seize control of any creature. On a failed save it obeys you, and you can "
            "direct it telepathically, even taking full actions through it while the spell lasts."
        ),
    },
    "Druidcraft": {
        "level": 0,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You tap minor primal magic to create harmless sensory effects, predict the weather, "
            "or coax plant life."
        ),
    },
    "Earthquake": {
        "level": 8,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "500 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S, M (a bit of dirt and clay in a small leather bag)",
        "concentration": "Concentration",
        "definition": (
            "You shake ground in a 100-foot radius, creating difficult terrain, fissures, and "
            "collapsing structures each round the spell persists."
        ),
    },
    "Elemental Bane": {
        "level": 4,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "90 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You strip away a creature's resistance to one damage type and cause it to take an "
            "extra 2d6 of that damage whenever it is hit."
        ),
    },
    "Elemental Weapon": {
        "level": 3,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You imbue a weapon with elemental energy, granting +1 bonus to attack rolls and "
            "1d4 extra damage of a chosen type, improving with higher-level slots."
        ),
    },
    "Encode Thoughts": {
        "level": 0,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "Self",
        "duration": "8 hours",
        "components": "S",
        "concentration": "",
        "definition": (
            "You pull a memory strand from your mind, creating a tangible ribbon of information "
            "that can be read with the appropriate magic."
        ),
    },
    "Enemies Abound": {
        "level": 3,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "A creature you target becomes confused about its allies. On a failed Intelligence save "
            "it cannot distinguish friend from foe and must attack the nearest creature."
        ),
    },
    "Erupting Earth": {
        "level": 3,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Instantaneous",
        "components": "V, S, M (a piece of obsidian)",
        "concentration": "",
        "definition": (
            "You churn a 20-foot cube of ground into jagged debris, dealing 3d12 bludgeoning "
            "damage (Dexterity half) and leaving the area difficult terrain."
        ),
    },
    "Evard's Black Tentacles": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "90 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S, M (a bit of tentacle from a giant octopus)",
        "concentration": "Concentration",
        "definition": (
            "Rubbery tentacles fill a 20-foot square, grappling creatures and dealing 3d6 "
            "bludgeoning damage each round they fail their Dexterity saves."
        ),
    },
    "Fabricate": {
        "level": 4,
        "school": "Transmutation",
        "casting_time": "10 minutes",
        "range": "120 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You convert raw materials into finished goods of the same substance, crafting "
            "large objects or numerous smaller items in seconds."
        ),
    },
    "Fast Friends": {
        "level": 3,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You supernaturally befriend a creature. On a failed Wisdom save it treats you "
            "as a close ally, readily helping you so long as you do not harm it."
        ),
    },
    "Feeblemind": {
        "level": 8,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "150 feet",
        "duration": "Instantaneous",
        "components": "V, S, M (a handful of clay, crystal, glass, or mineral spheres)",
        "concentration": "",
        "definition": (
            "A creature that fails both Intelligence and Charisma saves takes 4d6 psychic damage "
            "and has its intellect and personality shattered until cured."
        ),
    },
    "Feign Death": {
        "level": 3,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "1 hour",
        "components": "V, S, M (a pinch of graveyard dirt)",
        "concentration": "",
        "definition": (
            "You place a willing creature in a cataleptic state indistinguishable from death, "
            "granting resistance to damage but leaving it incapacitated."
        ),
    },
    "Find Greater Steed": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "10 minutes",
        "range": "30 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You summon a spirit steed (such as a griffon or pegasus) that serves as a loyal mount, "
            "sharing spells you cast on yourself."
        ),
    },
    "Fire Storm": {
        "level": 7,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "150 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "Seven 10-foot cubes of roaring flame appear, dealing 7d10 fire damage (Dexterity "
            "half) and igniting unattended objects."
        ),
    },
    "Flame Arrows": {
        "level": 3,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a quiver of arrows or bolts)",
        "concentration": "Concentration",
        "definition": (
            "You kindle ammunition. Each piece fired deals an extra 1d6 fire damage, with the "
            "spell affecting up to 12 missiles."
        ),
    },
    "Foresight": {
        "level": 9,
        "school": "Divination",
        "casting_time": "1 minute",
        "range": "Touch",
        "duration": "8 hours",
        "components": "V, S, M (a hummingbird feather)",
        "concentration": "",
        "definition": (
            "You grant a creature supernatural premonition. It gains advantage on attack rolls, "
            "ability checks, and saves, while attackers have disadvantage against it."
        ),
    },
    "Freedom Of Movement": {
        "level": 4,
        "school": "Abjuration",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "1 hour",
        "components": "V, S, M (a leather strap bound around the arm)",
        "concentration": "",
        "definition": (
            "The target's movement is unhindered. Difficult terrain, restraints, and magical "
            "effects cannot reduce its speed, and it can escape nonmagical restraints automatically."
        ),
    },
    "Freedom of the Waves (HB)": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "Self (15-foot cube)",
        "duration": "Instantaneous",
        "components": "V, S, M (a drop of water)",
        "concentration": "",
        "definition": (
            "A surge of seawater bursts forth. Creatures of your choice take 4d8 cold damage and are "
            "pushed 10 feet, or willing allies gain temporary hit points instead."
        ),
    },
    "Frostbite": {
        "level": 0,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "Chilling wind assails a creature. On a failed Constitution save it takes 1d6 cold damage "
            "(scaling) and has disadvantage on its next weapon attack."
        ),
    },
    "Galder's Speedy Courier": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "10 minutes",
        "range": "10 feet",
        "duration": "Instantaneous",
        "components": "V, S, M (25 gp per casting)",
        "concentration": "",
        "definition": (
            "You summon an invisible courier to deliver a small object or message to a designated "
            "recipient on the same plane within 10 minutes."
        ),
    },
    "Galder's Tower": {
        "level": 3,
        "school": "Conjuration",
        "casting_time": "10 minutes",
        "range": "30 feet",
        "duration": "24 hours",
        "components": "V, S, M (a fragment of stone)",
        "concentration": "",
        "definition": (
            "You raise a two-story magical tower with furnished rooms you choose. The structure "
            "remains for a day unless dismissed."
        ),
    },
    "Gaseous Form": {
        "level": 3,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a bit of gauze and smoke)",
        "concentration": "Concentration",
        "definition": (
            "The target becomes a misty cloud, gaining resistance to nonmagical damage and the ability "
            "to slip through cracks while unable to attack."
        ),
    },
    "Giant Insect": {
        "level": 4,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You transform up to ten centipedes, spiders, wasps, or scorpions into giant versions under "
            "your command for the duration."
        ),
    },
    "Glyph of Warding": {
        "level": 3,
        "school": "Abjuration",
        "casting_time": "1 hour",
        "range": "Touch",
        "duration": "Until dispelled",
        "components": "V, S, M (incense and powdered diamond worth 200 gp)",
        "concentration": "",
        "definition": (
            "You inscribe a ward that triggers an explosive burst or stores a spell of up to 3rd level, "
            "detonating when the trigger condition is met."
        ),
    },
    "Grasping Vine": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "Bonus Action",
        "range": "30 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "A vine sprouts from a surface and lashes at creatures, pulling them 20 feet toward a point "
            "you choose each round."
        ),
    },
    "Gravity Sinkhole": {
        "level": 4,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Instantaneous",
        "components": "V, S, M (a crushed black pearl worth 500 gp)",
        "concentration": "",
        "definition": (
            "You create a 20-foot-radius sphere of crushing gravity. Creatures make Constitution saves or take 5d10 "
            "force damage and are pulled to the centre."
        ),
    },
    "Greater Invisibility": {
        "level": 4,
        "school": "Illusion",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "The target becomes invisible even after attacking or casting spells until the effect ends."
        ),
    },
    "Guardian of Faith": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "8 hours",
        "components": "V",
        "concentration": "",
        "definition": (
            "A Large spectral guardian appears. Hostile creatures in its space take 20 radiant damage unless "
            "they save, and the guardian vanishes after dealing 60 damage total."
        ),
    },
    "Guardian of Nature": {
        "level": 4,
        "school": "Transmutation",
        "casting_time": "Bonus Action",
        "range": "Self",
        "duration": "Concentration, up to 1 minute",
        "components": "V",
        "concentration": "Concentration",
        "definition": (
            "You assume the form of a primal warrior or great tree, gaining movement, damage, and sense boosts "
            "depending on the form chosen."
        ),
    },
    "Guidance": {
        "level": 0,
        "school": "Divination",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You grant a creature a +1d4 bonus to one ability check it makes before the spell ends."
        ),
    },
    "Gust": {
        "level": 0,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You create a small gust of wind to push unattended objects or nudge creatures a few feet."
        ),
    },
    "Heal": {
        "level": 6,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "A surge of healing energy restores 70 hit points to a creature and ends blindness, deafness, and disease."
        ),
    },
    "Heroes’ Feast": {
        "level": 6,
        "school": "Conjuration",
        "casting_time": "10 minutes",
        "range": "30 feet",
        "duration": "24 hours",
        "components": "V, S, M (a bowl worth 1,000 gp)",
        "concentration": "",
        "definition": (
            "You conjure a sumptuous meal for up to twelve creatures, granting immunity to poison and fear, "
            "plus bonus hit points and advantage on Wisdom saves for a day."
        ),
    },
    "Hunger Of Hadar": {
        "level": 3,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "150 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S, M (a pickled octopus tentacle)",
        "concentration": "Concentration",
        "definition": (
            "You open a rift to the Far Realm, creating a 20-foot sphere of biting cold and writhing tendrils that "
            "damage and impede creatures."
        ),
    },
    "Incite Greed": {
        "level": 3,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "A cluster of creatures covet a bauble you present. On failed Wisdom saves they are charmed, "
            "incapacitated, and compelled to move toward the object."
        ),
    },
    "Infestation": {
        "level": 0,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Instantaneous",
        "components": "V, S, M (a living flea)",
        "concentration": "",
        "definition": (
            "You summon biting vermin. On a failed Constitution save the target takes 1d6 poison damage and moves "
            "5 feet in a random direction."
        ),
    },
    "Legend Lore": {
        "level": 5,
        "school": "Divination",
        "casting_time": "10 minutes",
        "range": "Self",
        "duration": "Instantaneous",
        "components": "V, S, M (incense and ivory strips worth 250 gp, consumed)",
        "concentration": "",
        "definition": (
            "You learn significant lore about a person, place, or object, including current tales, "
            "forgotten stories, or secret information."
        ),
    },
    "Leomund's Secret Chest": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "1 action",
        "range": "Touch",
        "duration": "Instantaneous",
        "components": "V, S, M (a rare miniaturized chest worth 5,000 gp)",
        "concentration": "",
        "definition": (
            "You hide a chest on the Ethereal Plane, recalling it with the miniature replica while the spell lasts."
        ),
    },
    "Leomund’s Tiny Hut": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "1 minute",
        "range": "Self (10-foot radius hemisphere)",
        "duration": "8 hours",
        "components": "V, S, M (a small crystal bead)",
        "concentration": "",
        "definition": (
            "You conjure an immobile dome that shelters up to nine Medium creatures, maintaining "
            "comfortable conditions while blocking spells and weather."
        ),
    },
    "Life Transference": {
        "level": 3,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You sacrifice life force, taking 4d8 necrotic damage and healing the target for twice that amount."
        ),
    },
    "Lightning Arrow": {
        "level": 3,
        "school": "Transmutation",
        "casting_time": "Bonus Action",
        "range": "Self",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "Your next ranged weapon attack becomes a bolt of lightning dealing 4d8 lightning damage on a hit and "
            "splashing nearby creatures for half as much."
        ),
    },
    "Lightning Bolt": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "Self (100-foot line)",
        "duration": "Instantaneous",
        "components": "V, S, M (a bit of fur and a rod of amber, crystal, or glass)",
        "concentration": "",
        "definition": (
            "A stroke of lightning blasts out, dealing 8d6 lightning damage to creatures in a line (Dexterity half)."
        ),
    },
    "Locate Creature": {
        "level": 4,
        "school": "Divination",
        "casting_time": "Action",
        "range": "Self",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a bit of fur from a bloodhound)",
        "concentration": "Concentration",
        "definition": (
            "You sense the direction of a familiar creature within 1,000 feet, provided you know its appearance."
        ),
    },
    "Magic Circle": {
        "level": 3,
        "school": "Abjuration",
        "casting_time": "1 minute",
        "range": "10 feet",
        "duration": "1 hour",
        "components": "V, S, M (holy water or powdered silver worth 100 gp)",
        "concentration": "",
        "definition": (
            "You inscribe a 10-foot-radius circle that either keeps extraplanar creatures at bay or traps them within."
        ),
    },
    "Major Image": {
        "level": 3,
        "school": "Illusion",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S, M (a bit of fleece)",
        "concentration": "Concentration",
        "definition": (
            "You create a convincing image with sound, smell, and temperature that you can move within range."
        ),
    },
    "Mass Heal": {
        "level": 9,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You restore up to 700 hit points divided as you choose and end blindness, deafness, and disease on affected creatures."
        ),
    },
    "Mass Polymorph": {
        "level": 9,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a caterpillar cocoon)",
        "concentration": "Concentration",
        "definition": (
            "Up to ten willing creatures transform into beasts of CR 8 or lower, keeping their mental abilities while adopting the new forms."
        ),
    },
    "Mass Suggestion": {
        "level": 6,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "24 hours",
        "components": "V, M (a snake's tongue and either a bit of honeycomb or a drop of sweet oil)",
        "concentration": "",
        "definition": (
            "You influence up to twelve creatures with a reasonable course of activity, lasting a day or longer with higher-level slots."
        ),
    },
    "Maze": {
        "level": 8,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You banish a creature to a labyrinthine demiplane until it escapes by using an action to succeed on an Intelligence check."
        ),
    },
    "Meld into Stone": {
        "level": 3,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "8 hours",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You and your gear merge with a stone surface, allowing you to hear faintly outside but taking damage if the stone is destroyed."
        ),
    },
    "Melf's Minute Meteors": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "1 action",
        "range": "Self",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S, M (niter, sulfur, and pine tar formed into beads)",
        "concentration": "Concentration",
        "definition": (
            "You create six tiny meteors orbiting you, each hurled as a bonus action to explode for 2d6 fire damage in a small radius."
        ),
    },
    "Mold Earth": {
        "level": 0,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Instantaneous or 1 hour",
        "components": "S",
        "concentration": "",
        "definition": (
            "You shape, excavate, or create difficult terrain from earth within a 5-foot cube."
        ),
    },
    "Mordenkainen's Faithful Hound": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "8 hours",
        "components": "V, S, M (a silver whistle, a string of bells, and a piece of bone)",
        "concentration": "",
        "definition": (
            "You summon an invisible guardian hound that attacks intruders and barks to alert you."
        ),
    },
    "Mordenkainen's Magnificent Mansion": {
        "level": 7,
        "school": "Conjuration",
        "casting_time": "1 minute",
        "range": "300 feet",
        "duration": "24 hours",
        "components": "V, S, M (a miniature portal carved from ivory and a small piece of polished marble)",
        "concentration": "",
        "definition": (
            "You conjure a luxurious extradimensional dwelling with food and unseen servants for up to one hundred guests."
        ),
    },
    "Mordenkainen's Private Sanctum": {
        "level": 4,
        "school": "Abjuration",
        "casting_time": "10 minutes",
        "range": "120 feet",
        "duration": "24 hours",
        "components": "V, S, M (a thin sheet of lead, a piece of opaque glass, a wad of cotton, or powdered chrysolite)",
        "concentration": "",
        "definition": (
            "You ward a 100-foot cube against scrying, teleportation, sound, and light as you choose."
        ),
    },
    "Motivational Speech": {
        "level": 3,
        "school": "Enchantment",
        "casting_time": "1 minute",
        "range": "60 feet",
        "duration": "1 hour",
        "components": "V",
        "concentration": "",
        "definition": (
            "Up to five creatures gain 5 temporary hit points and advantage on Wisdom saves, losing the temp HP to gain advantage on an attack."
        ),
    },
    "Otiluke's Resilient Sphere": {
        "level": 4,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S, M (a hemispherical piece of clear crystal)",
        "concentration": "Concentration",
        "definition": (
            "You trap a creature in a weightless, impenetrable sphere. Nothing can pass through it, though the target can breathe."
        ),
    },
    "Otto’s Irresistible Dance": {
        "level": 6,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V",
        "concentration": "Concentration",
        "definition": (
            "You compel a creature to dance uncontrollably. It has disadvantage on Dexterity saves and attack rolls and grants advantage until it saves."
        ),
    },
    "Passwall": {
        "level": 5,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "1 hour",
        "components": "V, S, M (a pinch of sesame seeds)",
        "concentration": "",
        "definition": (
            "You open a passage through wood, plaster, or stone, creating a 5-foot-wide, 8-foot-tall tunnel 20 feet deep."
        ),
    },
    "Power Word Stun": {
        "level": 8,
        "school": "Enchantment",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Instantaneous",
        "components": "V",
        "concentration": "",
        "definition": (
            "You speak a word of power that stuns a creature with 150 hit points or fewer. It remains stunned until it succeeds on a save at the end of each turn."
        ),
    },
    "Power Word: Fortify": {
        "level": 7,
        "school": "Abjuration",
        "casting_time": "Bonus Action",
        "range": "30 feet",
        "duration": "10 minutes",
        "components": "V",
        "concentration": "",
        "definition": (
            "You utter a bolstering word. Up to six creatures gain 50 temporary hit points and advantage on saves against exhaustion for the duration."
        ),
    },
    "Programmed Illusion": {
        "level": 6,
        "school": "Illusion",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Until dispelled",
        "components": "V, S, M (a bit of fleece and jade dust worth 25 gp)",
        "concentration": "",
        "definition": (
            "You craft a complex scene that appears when a trigger condition is met, repeating while the illusion persists."
        ),
    },
    "Protection from Energy": {
        "level": 3,
        "school": "Abjuration",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You grant resistance to acid, cold, fire, lightning, or thunder damage for the duration."
        ),
    },
    "Pulse Wave": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "Self (30-foot cone)",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You unleash a concussive wave, dealing 6d6 force damage (Constitution half) and either pushing or pulling creatures 15 feet."
        ),
    },
    "Raise Dead": {
        "level": 5,
        "school": "Necromancy",
        "casting_time": "1 hour",
        "range": "Touch",
        "duration": "Instantaneous",
        "components": "V, S, M (a diamond worth 500 gp)",
        "concentration": "",
        "definition": (
            "You return a creature that has been dead no longer than 10 days to life with 1 hit point, leaving it temporarily weakened."
        ),
    },
    "Raulothim's Psychic Lance": {
        "level": 4,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Instantaneous",
        "components": "V",
        "concentration": "",
        "definition": (
            "You hurl a psychic spear at a creature you can name or see, dealing 7d6 psychic damage and incapacitating it until your next turn on a failed save."
        ),
    },
    "Resistance": {
        "level": 0,
        "school": "Abjuration",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S, M (a miniature cloak)",
        "concentration": "Concentration",
        "definition": (
            "You bolster a creature, allowing it to add 1d4 to one saving throw before the spell ends."
        ),
    },
    "Revivify": {
        "level": 3,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Instantaneous",
        "components": "V, S, M (a diamond worth 300 gp)",
        "concentration": "",
        "definition": (
            "You restore life to a creature that has died within the last minute, returning it with 1 hit point."
        ),
    },
    "Sapping Sting": {
        "level": 0,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You assault the nervous system. On a failed Constitution save the target takes 1d4 necrotic damage and falls prone."
        ),
    },
    "Seeming": {
        "level": 5,
        "school": "Illusion",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "8 hours",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You change the appearance of any number of creatures you can see, crafting different disguises for each."
        ),
    },
    "Sending": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "Unlimited",
        "duration": "Instantaneous",
        "components": "V, S, M (a short piece of copper wire)",
        "concentration": "",
        "definition": (
            "You send a 25-word telepathic message to a creature you're familiar with. It can reply immediately."
        ),
    },
    "Shadow of Moil": {
        "level": 4,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "Self",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "Shadowy flames wreath you, giving resistance to radiant damage, imposing disadvantage on attacks against you, and scorching foes that strike you."
        ),
    },
    "Shape Water": {
        "level": 0,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Instantaneous or 1 hour",
        "components": "S",
        "concentration": "",
        "definition": (
            "You manipulate up to a 5-foot cube of water, moving it, freezing it, or changing its appearance temporarily."
        ),
    },
    "Shapechange": {
        "level": 9,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "Self",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a jade circlet worth at least 1,500 gp)",
        "concentration": "Concentration",
        "definition": (
            "You assume the form of any creature you've seen of your level or lower, changing into new forms each round as desired."
        ),
    },
    "Shillelagh": {
        "level": 0,
        "school": "Transmutation",
        "casting_time": "Bonus Action",
        "range": "Touch",
        "duration": "1 minute",
        "components": "V, S, M (mistletoe, a shamrock leaf, and a club or quarterstaff)",
        "concentration": "",
        "definition": (
            "You imbue a club or staff with nature's power, making it magical with a d8 damage die and using your spellcasting ability for attack rolls."
        ),
    },
    "Sickening Radiance": {
        "level": 4,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "Dim, greenish light fills a 30-foot radius sphere. Creatures inside take 4d10 radiant damage and suffer exhaustion on failed saves."
        ),
    },
    "Spare the Dying": {
        "level": 0,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You stabilise a creature at 0 hit points, removing the need for death saving throws."
        ),
    },
    "Spirit Guardians": {
        "level": 3,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "Self (15-foot radius)",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S, M (a holy symbol)",
        "concentration": "Concentration",
        "definition": (
            "Spectral guardians swirl around you, halving enemy speed and dealing 3d8 radiant or necrotic damage each round to foes that fail a save."
        ),
    },
    "Spirit Of Death": {
        "level": 4,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You manifest a reaper-like spirit in an open space. It flies 30 feet and reaps a creature, dealing 3d10 necrotic damage (save for half) each round."
        ),
    },
    "Spirit Shroud": {
        "level": 3,
        "school": "Necromancy",
        "casting_time": "Bonus Action",
        "range": "Self",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "You summon spirits that chill your foes. Your attacks deal an extra 1d8 radiant, necrotic, or cold damage, and enemies within 10 feet cannot regain hit points."
        ),
    },
    "Staggering Smite": {
        "level": 4,
        "school": "Evocation",
        "casting_time": "Bonus Action",
        "range": "Self",
        "duration": "Concentration, up to 1 minute",
        "components": "V",
        "concentration": "Concentration",
        "definition": (
            "Your next melee hit deals an extra 4d6 psychic damage, and the target must save or suffer disadvantage on attacks and checks and be unable to take reactions."
        ),
    },
    "Stone Shape": {
        "level": 4,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "Instantaneous",
        "components": "V, S, M (soft clay)",
        "concentration": "",
        "definition": (
            "You form stone into a shape of your choice, creating doors, small passages, or stone tools."
        ),
    },
    "Storm Sphere": {
        "level": 4,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "150 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "A 20-foot-radius whirlwind of magical lightning forms, damaging creatures inside and allowing you to hurl bolts as a bonus action."
        ),
    },
    "Summon Aberration": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "90 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a pickled tentacle and an eyeball in a silver ring)",
        "concentration": "Concentration",
        "definition": (
            "You call forth an aberrant spirit manifesting as a Beholderkin, Slaad, or Star Spawn ally whose strength scales with slot level."
        ),
    },
    "Summon Construct": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "90 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a tiny piece of stone, metal, or clay)",
        "concentration": "Concentration",
        "definition": (
            "You magically assemble a construct ally (clay, metal, or stone form) that fights for you and grows stronger with higher slots."
        ),
    },
    "Summon Fey": {
        "level": 3,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "90 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a gilded flower worth at least 300 gp)",
        "concentration": "Concentration",
        "definition": (
            "You summon a fey spirit manifested as a trickster, fury, or mirthful ally, gaining extra abilities based on the mood you choose."
        ),
    },
    "Summon Undead": {
        "level": 3,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "90 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a gilded skull worth at least 300 gp)",
        "concentration": "Concentration",
        "definition": (
            "You conjure a ghostly, skeletal, or zombie spirit that obeys your commands and scales with slot level."
        ),
    },
    "Symphony Of The Masked": {
        "level": 7,
        "school": "Illusion",
        "casting_time": "1 minute",
        "range": "60 feet",
        "duration": "Concentration, up to 1 hour",
        "components": "V, S, M (a conductor's baton)",
        "concentration": "Concentration",
        "definition": (
            "You orchestrate a haunting performance, charming and enthralling creatures of your choice in a wide radius while you conduct."
        ),
    },
    "Teleport": {
        "level": 7,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "10 feet",
        "duration": "Instantaneous",
        "components": "V",
        "concentration": "",
        "definition": (
            "You and up to eight willing creatures teleport instantly to a destination you know or can describe, with accuracy depending on familiarity."
        ),
    },
    "Thaumaturgy": {
        "level": 0,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "Up to 1 minute",
        "components": "V",
        "concentration": "",
        "definition": (
            "You manifest minor wonders—booming your voice, causing flames to flicker, doors to slam, or the ground to tremble briefly."
        ),
    },
    "Tidal Wave": {
        "level": 3,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Instantaneous",
        "components": "V, S, M (a drop of water)",
        "concentration": "",
        "definition": (
            "You conjure a wave that crashes in a 30-foot line, dealing 4d8 bludgeoning damage (Dexterity half) and knocking creatures prone."
        ),
    },
    "Time Stop": {
        "level": 9,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "Self",
        "duration": "Instantaneous",
        "components": "V",
        "concentration": "",
        "definition": (
            "You briefly stop time, taking 1d4+1 turns in a row while others are frozen, ending if your actions affect a creature or object worn or carried."
        ),
    },
    "Tiny Servant": {
        "level": 3,
        "school": "Transmutation",
        "casting_time": "1 minute",
        "range": "Touch",
        "duration": "8 hours",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You animate up to three Tiny objects that obey your commands and can perform tasks or attack at your direction."
        ),
    },
    "True Seeing": {
        "level": 6,
        "school": "Divination",
        "casting_time": "Action",
        "range": "Touch",
        "duration": "1 hour",
        "components": "V, S, M (an ointment for the eyes worth 25 gp)",
        "concentration": "",
        "definition": (
            "The target gains truesight out to 120 feet, seeing through illusions, transmutations, and into the Ethereal Plane."
        ),
    },
    "Vampiric Touch": {
        "level": 3,
        "school": "Necromancy",
        "casting_time": "Action",
        "range": "Self",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "Your shadow-wreathed hand siphons life. On a hit the target takes 3d6 necrotic damage and you regain half as many hit points."
        ),
    },
    "Vitriolic Sphere": {
        "level": 4,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "150 feet",
        "duration": "Instantaneous",
        "components": "V, S, M (a drop of giant slug bile)",
        "concentration": "",
        "definition": (
            "A glowing bead streaks to a point, exploding into acid that deals 10d4 damage on impact and another 5d4 the next round (Dexterity half)."
        ),
    },
    "Wall of Sand": {
        "level": 3,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "90 feet",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S, M (a handful of sand)",
        "concentration": "Concentration",
        "definition": (
            "A wall of swirling sand blinds creatures passing through and creates difficult terrain, though it does not block movement."
        ),
    },
    "Wall of Water": {
        "level": 3,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Concentration, up to 10 minutes",
        "components": "V, S, M (a drop of water)",
        "concentration": "Concentration",
        "definition": (
            "You create a wall of water that slows movement, extinguishes flames, and hinders ranged weapon attacks passing through."
        ),
    },
    "Water Breathing": {
        "level": 3,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "24 hours",
        "components": "V, S, M (a short reed or piece of straw)",
        "concentration": "",
        "definition": (
            "Up to ten creatures gain the ability to breathe underwater for a full day."
        ),
    },
    "Water Walk": {
        "level": 3,
        "school": "Transmutation",
        "casting_time": "Action",
        "range": "30 feet",
        "duration": "1 hour",
        "components": "V, S, M (a piece of cork)",
        "concentration": "",
        "definition": (
            "Up to ten creatures can move across liquid surfaces as if solid, including lava or mud, for the duration."
        ),
    },
    "Watery Sphere": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "Action",
        "range": "90 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S, M (a droplet of water)",
        "concentration": "Concentration",
        "definition": (
            "You form a 10-foot sphere of water that traps creatures, restraining them on failed Strength saves as you move the orb."
        ),
    },
    "Weird": {
        "level": 9,
        "school": "Illusion",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S",
        "concentration": "Concentration",
        "definition": (
            "Nightmarish visions assail creatures you choose in a 30-foot radius. They take 4d10 psychic damage and gain frightened, repeating saves each round."
        ),
    },
    "Widogast's Vault of Amber (HB)": {
        "level": 4,
        "school": "Conjuration",
        "casting_time": "1 minute",
        "range": "30 feet",
        "duration": "24 hours",
        "components": "V, S, M (a pinch of amber dust)",
        "concentration": "",
        "definition": (
            "You conjure a translucent amber vault with shelves for storing objects and creatures, locking them in stasis until released."
        ),
    },
    "Widogast's Web of Fire (HB)": {
        "level": 4,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "60 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You hurl up to ten fire threads at creatures of your choice, each dealing 1d6 fire damage with overlapping strands burning the same target multiple times."
        ),
    },
    "Wind Walk": {
        "level": 6,
        "school": "Transmutation",
        "casting_time": "1 minute",
        "range": "30 feet",
        "duration": "8 hours",
        "components": "V, S, M (a bit of smoke)",
        "concentration": "",
        "definition": (
            "Up to ten creatures transform into clouds, gaining a flying speed of 300 feet and resistance to nonmagical damage while in gas form."
        ),
    },
    "Wind Wall": {
        "level": 3,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "120 feet",
        "duration": "Concentration, up to 1 minute",
        "components": "V, S, M (a tiny fan and a feather of exotic origin)",
        "concentration": "Concentration",
        "definition": (
            "You create a wall of strong wind that deflects arrows, fog, and gas while dealing 3d8 bludgeoning damage to creatures passing through."
        ),
    },
    "Word of Radiance": {
        "level": 0,
        "school": "Evocation",
        "casting_time": "Action",
        "range": "5 feet",
        "duration": "Instantaneous",
        "components": "V, S",
        "concentration": "",
        "definition": (
            "You utter a divine word, causing radiant energy to flare from you. Each hostile creature you choose within range makes a Constitution save or takes 1d6 radiant damage (scaling)."
        ),
    },
}



def spell_from_data(spell_name: str) -> "Spell":
    """Build a spell instance using the 2024 reference data."""
    data = SPELL_DATA_2024.get(spell_name)
    if not data:
        raise KeyError(f"No spell data found for {spell_name!r}")
    return Spell(
        name=spell_name,
        level=data["level"],
        school=data["school"],
        casting_time=data["casting_time"],
        ranges=data["range"],
        duration=data["duration"],
        components=data["components"],
        concentration=data["concentration"],
        definition=data["definition"],
    )

class Spell:
	def __init__(spell,
				 name="",
				 level=0,
				 school="",
				 casting_time="",
				 ranges = "",
				 duration = "",
				 components = "",
				 concentration = "",
				 definition = ""):
		spell.name =  name
		spell.level = level
		spell.school = school
		spell.casting_time = casting_time
		spell.ranges = ranges
		spell.duration = duration
		spell.components = components
		spell.concentration = concentration
		spell.definition = definition

	def describe(spell):
		desc = spell.string
		return desc

	def __str__(spell):
		desc = ""
		if spell.casting_time:   desc += f"<i>⟨{spell.casting_time}⟩</i><br>"
		if spell.concentration:  desc += f"<i>({spell.concentration}: </i>"
		if spell.duration:       desc += f"<i>({spell.duration})</i>"
		if spell.ranges:         desc += f"<br><i>>{spell.ranges}></i>"
		if spell.components:	 desc += f"<br><i>⦓{spell.components}⦔</i>"
		if spell.level == 0:
			level_text = "<b><p>Cantrip</b></p>"
		else:
			level_text = f"<b><p> Level {spell.level} Spell </b></p>"
		return f"""
		<h4 style="font-family: 'Iglesia' ; font-size:	2.1em;"> {spell.name}</h4>
		{level_text}
		<p>{desc}</p>
		<p>
		{spell.definition }
		</p>
		"""

	@property
	def string(spell):

		name  = f"{spell.name}"
		desc  = f"{spell.school}"
		definition = ""
		if spell.casting_time:   desc += f"({spell.casting_time})"
		if spell.concentration:  desc += f"⟨{spell.concentration}"
		if spell.duration:       desc += f"⟨{spell.duration}⟩"
		if spell.ranges:         desc += f"-{spell.ranges}"
		if spell.definition:     definition += f"\n\t{spell.definition}"
		string = Entry(title=name, definition=definition, description=desc)
		return string






# Cantrips
CANTRIPS = True # Just for ordering information at human reader level
if CANTRIPS:
	Elementalism = 		Spell("Elementalism",
			level=0,
			school="Transmutation",
			casting_time="Action",
			ranges = "30 feet",
			duration = "Instantaneous",
			components = "Verbal, Somatic",
			concentration = "",
			definition = """You exert control over the elements, creating one of the following effects within range.
			<br>
			<b>Beckon Air.</b> You create a breeze strong enough to ripple cloth, stir dust, rustle leaves, and close open doors and shutters, all in a 5-foot Cube. Doors and shutters being held open by someone or something aren't affected.
			<br>
			<b>Beckon Earth.</b> You create a thin shroud of dust or sand that covers surfaces in a 5-foot-square area, or you cause a single word to appear in your handwriting in a patch of dirt or sand.
			<br>
			<b>Beckon Fire.</b> You create a thin cloud of harmless embers and colored, scented smoke in a 5-foot Cube. You choose the color and scent, and the embers can light candles, torches, or lamps in that area. The smoke's scent lingers for 1 minute.
			<br>
			<b>Beckon Water.</b> You create a spray of cool mist that lightly dampens creatures and objects in a 5-foot Cube. Alternatively, you create 1 cup of clean water either in an open container or on a surface, and the water evaporates in 1 minute.
			<br>
			<b>Sculpt Element.</b> You cause dirt, sand, fire, smoke, mist, or water that can fit in a 1-foot Cube to assume a crude shape (such as that of a creature) for 1 hour.
			<br>""")
	StarryWisp = Spell("Starry Wisp",
			level=0,
			school="Evocation",
			casting_time="Action",
			ranges = "60 feet",
			duration = "Instantaneous",
			components = "Verbal, Somatic",
			concentration = "",
			definition = """You launch a mote of light at one creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d8 Radiant damage, and until the end of your next turn, it emits Dim Light in a 10-foot radius and can't benefit from the Invisible condition.
			<br>
			<b>Cantrip Upgrade.</b> The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).
			<br>""")
	EncodeThoughts = spell_from_data("Encode Thoughts")
	Frostbite = spell_from_data("Frostbite")
	Resistance = spell_from_data("Resistance")
	SappingSting = spell_from_data("Sapping Sting")
	ShapeWater = spell_from_data("Shape Water")
	Shillelagh = spell_from_data("Shillelagh")
	WordofRadiance = spell_from_data("Word of Radiance")
	AcidSplash = spell_from_data("Acid Splash")
	MoldEarth = spell_from_data("Mold Earth")
	Firebolt =          Spell("Fire Bolt",           0,
		school="Evocation",
		casting_time="Action",
		ranges = "120 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		definition = """
			You hurl a mote of fire at a creature or an object within range.
			Make a ranged spell attack against the target.
			On a hit, the target takes <b>1d10 Fire damage</b>.
			A flammable object hit by this spell starts burning
			if it isn't being worn or carried.<br>
			<i>Cantrip Upgrade.</i> The damage increases by 1d10 when you reach levels 5 (2d10), 11 (3d10), and 17 (4d10).
			""")
	FireBolt = 			Firebolt
	DancingLights =     Spell("Dancing Lights",     0,
		school="Illusion",
		casting_time="Action",
		ranges = "120 feet",
		duration = "Up to 1 minute",
		components = "Verbal, Somatic, Material (a bit of phosphorus)",
		concentration = "Concentration",
		definition = """
		You create up to four torch-size lights within range, making them appear as torches, lanterns, or glowing orbs that hover for the duration. Alternatively, you combine the four lights into one glowing Medium form that is vaguely humanlike. Whichever form you choose, each light sheds Dim Light in a 10-foot radius.
		<br>
		As a Bonus Action, you can move the lights up to 60 feet to a space within range. A light must be within 20 feet of another light created by this spell, and a light vanishes if it exceeds the spell's range.
		<br>""")
	BoomingBlade = spell_from_data("Booming Blade")
	ChillTouch =        Spell("Chill Touch",        0,
			school	=	"Necromancy",
			casting_time="Action",
			ranges = "Touch",
			duration = "Instantaneous",
			components = "Verbal, Somatic",
			concentration = "",
			definition = """
				Channeling the chill of the grave, make a melee spell
				attack against a target within reach.
				On a hit, the target takes <b>1d10 Necrotic damage</b>,
				and it can't regain Hit Points until the end of
				your next turn.<br>
				<i>Cantrip Upgrade.</i> The damage increases by 1d10 when
				you reach levels 5 (2d10), 11 (3d10), and 17 (4d10).
				""")
	BladeWard =         Spell(name="Blade Ward",
		level=0,
		school="Abjuration",
		casting_time="Action",
		ranges = "Self",
		duration = "Up to 1 minute",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		definition = """
		Whenever a creature makes an attack roll against you before the spell ends, the attacker subtracts <i>1d4</i> from the attack roll.
		<br>""")
	Infestation = spell_from_data("Infestation")
	Gust = spell_from_data("Gust")
	Thaumaturgy = spell_from_data("Thaumaturgy")
	SparetheDying = spell_from_data("Spare the Dying")
	EncodeThoughts = spell_from_data("Encode Thoughts")
	Frostbite = spell_from_data("Frostbite")
	Resistance = spell_from_data("Resistance")
	SappingSting = spell_from_data("Sapping Sting")
	ShapeWater = spell_from_data("Shape Water")
	Shillelagh = spell_from_data("Shillelagh")
	AcidSplash = spell_from_data("Acid Splash")
	Thaumaturgy = spell_from_data("Thaumaturgy")
	Druidcraft = spell_from_data("Druidcraft")
	MoldEarth = spell_from_data("Mold Earth")
	SparetheDying = spell_from_data("Spare the Dying")
	BoomingBlade = spell_from_data("Booming Blade")
	Infestation = spell_from_data("Infestation")
	Gust = spell_from_data("Gust")
	Guidance = spell_from_data("Guidance")
	BoomingBlade =     	Spell("Booming Blade",     	0,
		school="Evocation",
		casting_time="Action",
		ranges = "Self (5-foot radius)",
		duration = "1 round",
		components = "Somatic, Material (a melee weapon worth at least 1 sp)",
		concentration = "Concentration",
		definition = """
		You brandish the weapon used in the spell's casting and make a melee attack with it against one creature within 5 feet of you. On a hit, the target suffers the weapon attack's normal effects and then becomes sheathed in booming energy until the start of your next turn. If the target willingly moves 5 feet or more before then, the target takes <b>1d8 thunder damage</b>, and the spell ends.
		<br>
		This spell's damage increases when you reach certain levels. At 5th level, the melee attack deals an extra <b>1d8 thunder damage</b> to the target on a hit, and the damage the target takes for moving increases to <b>2d8</b>. Both damage rolls increase by <b>1d8</b> at 11th level <b>(2d8 and 3d8)</b> and again at 17th level <b>(3d8 and 4d8)</b>.
		<br>""")
	ControlFlames =     Spell("Control Flames",     0,
			school = "Transmutation",
			casting_time = "Action",
			ranges = "60 feet",
			duration = "Instantaneous or 1 hour.",
			components = "Somatic",
			concentration = "Concentration",
			definition = """
You choose nonmagical flame that you can see within range and that fits within a 5-foot cube. You affect it in one of the following ways:
 <ul style="list-style-type: '🔥'; text-align: left; ">
	<li>You instantaneously expand the flame 5 feet in one direction, provided that wood or other fuel is present in the new location.</li>
	<li>You instantaneously extinguish the flames within the cube.</li>
	<li>You double or halve the area of bright light and dim light cast by the flame, change its color, or both. The change lasts for 1 hour.</li>
	<li>You cause simple shapes—such as the vague form of a creature, an inanimate object, or a location—to appear within the flames and animate as you like. The shapes last for 1 hour.</li>
 </ul>
If you cast this spell multiple times, you can have up to three non-instantaneous effects created by it active at a time, and you can dismiss such an effect as an action.
			<br>""")
	ShockingGrasp =     Spell("Shocking Grasp",   	0,
				school = "Evocation",
				casting_time = "Action",
				ranges = "Touch",
				duration = "Instantaneous.",
				components = "Verbal, Somatic",
				concentration = "",
				definition = """Lightning springs from you to a creature that you try to touch.
				Make a melee spell attack against the target.
				On a hit, the target takes <i>1d8 Lightning damage</i>,
				and it can't make <i>Opportunity Attacks</i>
				until the start of its next turn. <br>
				<b>Cantrip Upgrade.</b> The damage increases by <b>1d8</b> when you reach
				<i>levels 5 (2d8), 11 (3d8), and 17 (4d8).</i> """
				)
	PrimalSavagery =    Spell("Primal Savagery",    0,
		school = "Transmutation",
		casting_time = "Action",
		ranges = "Self",
		duration = "Instantaneous.",
		components = "Somatic",
		concentration = "",
		definition = """
		You channel primal magic to cause your teeth or fingernails to sharpen,
		ready to deliver a corrosive attack.
		Make a <b>melee spell attack</b>
		against one creature within <b>5 feet</b> of you.
		On a hit, the target takes <b>1d10 acid damage</b>.
		After you make the attack, your teeth or fingernails return to normal.
		<br>
		<b>At Higher Levels.</b> The spell’s damage increases by <b>1d10</b>
		when you reach <b>5th level (2d10), 11th level (3d10), and 17th level (4d10)</b>."""
		)
	Thunderclap =		Spell("Thunderclap",    	0,
			school = "Evocation",
			casting_time = "Action",
			ranges = "Self",
			duration = "Instantaneous.",
			components = "Somatic",
			concentration = "",
			definition = """Each creature in a <i>5-foot Emanation</i>
				originating from you must succeed on a
				<i>Constitution saving throw</i>
				or take <b>1d6 Thunder damage</b>.
				The spell's thunderous sound can be heard up to <i>100 feet</i> away.
				<br><b>Cantrip Upgrade.</b> The damage increases by <b>1d6</b>
				when you reach <i>levels 5 (2d6), 11 (3d6), and 17 (4d6)</i>.
				"""
				)
	Mending = 			Spell("Mending",            0,
				school = "Transmutation",
				casting_time = "1 minute",
				ranges = "Touch",
				duration = "Instantaneous",
				components = "Verbal, Somatic, Material (two Lodestones).",
				concentration = "",
				definition = """This spell repairs a single break or tear in an object you touch, such as a broken chain link, two halves of a broken key, a torn cloak, or a leaking wineskin. As long as the break or tear is no larger than 1 foot in any dimension, you mend it, leaving no trace of the former damage.
				<br>This spell can physically repair a magic item, but it can't restore magic to such an object."""
				)
	Message = 			Spell("Message",            0,
					school = "Transmutation",
					casting_time = "Action",
					ranges = "120 feet",
					duration = "1 round",
					components = "Somatic, Material (a copper wire)",
					concentration = "",
					definition = """You point toward a creature within range and whisper a message.
					The target (and only the target) hears the message and can reply in a whisper that only you can hear. <br>
					You can cast this spell through solid objects if you are familiar with the target and know it is beyond the barrier.
					Magical silence; 1 foot of stone, metal, or wood; or a thin sheet of lead blocks the spell."""
					)
	MinorIllusion =     Spell("Minor Illusion",     0,
						school = "Illusion",
						casting_time = "Action",
						ranges = "30 feet",
						duration = "1 minute",
						components = "Somatic, Material (a bit of fleece)",
						concentration = "",
						definition = """You create a sound or an image of an object within range that lasts for the duration. See the descriptions below for the effects of each. The illusion ends if you cast this spell again.<br>
							If a creature takes a Study action to examine the sound or image, the creature can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the illusion becomes faint to the creature.<br>
							<b>Sound.</b> If you create a sound, its volume can range from a whisper to a scream. It can be your voice, someone else's voice, a lion's roar, a beating of drums, or any other sound you choose. The sound continues unabated throughout the duration, or you can make discrete sounds at different times before the spell ends.<br>
							<b>Image.</b> If you create an image of an object—such as a chair, muddy footprints, or a small chest—it must be no larger than a 5-foot Cube. The image can't create sound, light, smell, or any other sensory effect. Physical interaction with the image reveals it to be an illusion, since things can pass through it.
							"""
							)
	PoisonSpray = 		Spell("Poison Spray",   	0,
		school = "Necromancy",
		casting_time = "Action",
		ranges = "30 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
			You spray toxic mist at a creature within range.
			Make a ranged spell attack against the target.
			On a hit, the target takes <b>1d12 Poison damage</b>.<br>
			<i>Cantrip Upgrade.</i> The damage increases by
			1d12 when you reach levels 5 (2d12), 11 (3d12),
			and 17 (4d12).
			"""
			)
	LightningLure =     Spell("Lightning Lure",     0,
		school = "Evocation",
		casting_time = "Action",
		ranges = "Self (15-foot radius)",
		duration = "Instantaneous",
		components = "Verbal",
		concentration = "",
		definition = """
		You create a lash of lightning energy that strikes
		at one creature of your choice that you can see
		within <i>15 feet</i> of you. The target
		must succeed on
		a <i>Strength saving throw</i> or be pulled up
		to <i>10 feet</i>
		in a straight line toward you and then take
		<i>1d8
		lightning damage</i> if it is within 5 feet of you.
		<br>
		This spell's damage increases by 1d8 when you reach
		5th level (2d8), 11th level (3d8), and 17th level
		(4d8).
		"""
		)
	GreenFlameBlade =   Spell("Green Flame Blade",  0,
		school = "Evocation",
		casting_time = "Action",
		ranges = "Self (5-foot radius)",
		duration = "Instantaneous",
		components = "Somatic, Material (a melee weapon worth at least 1 sp)",
		concentration = "",
		definition = """
		You brandish the weapon used in the spell's casting and make a melee attack with it against one creature within 5 feet of you. On a hit, the target suffers the weapon attack's normal effects, and you can cause green fire to leap from the target to a different creature of your choice that you can see within 5 feet of it. The second creature takes fire damage equal to your spellcasting ability modifier.<br>
		This spell's damage increases when you reach certain levels. At 5th level, the melee attack deals an extra 1d8 fire damage to the target on a hit, and the fire damage to the second creature increases to 1d8 + your spellcasting ability modifier. Both damage rolls increase by 1d8 at 11th level (2d8 and 2d8) and 17th level (3d8 and 3d8).
		"""
		)
	MageHand =          Spell("Mage Hand",          0,
		school = "Conjuration",
		casting_time = "Action",
		ranges = "30 feet",
		duration = "1 minute",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
		A spectral, floating hand appears at a point you choose within range. The hand lasts for the duration. The hand vanishes if it is ever more than 30 feet away from you or if you cast this spell again.
		<br>
		When you cast the spell, you can use the hand to manipulate an object, open an unlocked door or container, stow or retrieve an item from an open container, or pour the contents out of a vial.
		<br>
		As a Magic action on your later turns, you can control the hand thus again. As part of that action, you can move the hand up to 30 feet.
		<br>
		The hand can't attack, activate magic items, or carry more than 10 pounds.
		"""
		)
	MagicStone =        Spell("Magic Stone",        0,
		school = "Transmutation",
		casting_time = "Bonus Action",
		ranges = "Touch",
		duration = "1 minute",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
		You touch one to three pebbles and imbue them with magic.
		You or someone else can make a ranged spell attack with
		one of the pebbles by throwing it or hurling it with a
		sling. If thrown, a pebble has a range of 60 feet. If
		someone else attacks with a pebble, that attacker
		adds your spellcasting ability modifier, not the
		attacker's, to the attack roll. On a hit, the
		target takes <b>bludgeoning damage equal to 1d6 + your
		spellcasting ability modifier.</b> Whether the
		attack hits or misses, the spell then ends on the
		stone.
		<br>
		If you cast this spell again, the spell ends on any pebbles still affected
		by your previous casting.
		"""
		)
	Light = Spell("Light",              0,
		school = "Evocation",
		casting_time = "Action",
		ranges = "Touch",
		duration = "1 hour",
		components = "Verbal, Material (a firefly or phosphorescent moss)",
		concentration = "",
		definition = """
		You touch one Large or smaller object that isn't being worn or carried by someone else. Until the spell ends, the object sheds Bright Light in a 20-foot radius and Dim Light for an additional 20 feet. The light can be colored as you like.
		<br>
		Covering the object with something opaque blocks the light. The spell ends if you cast it again.
		"""
		)
	SacredFlame =       Spell("Sacred Flame",       0,
		school = "Evocation",
		casting_time = "Action",
		ranges = "60 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
		Flame-like radiance descends on a creature that you can see within range. The target must succeed on a Dexterity saving throw or take 1d8 Radiant damage. The target gains no benefit from Half Cover or Three-Quarters Cover for this save.
		<br>
		<b>Cantrip Upgrade.</b> The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).
		"""
		)
	SwordBurst =        Spell("Sword Burst",        0,
		school = "Conjuration",
		casting_time = "Action",
		ranges = "Self (5-foot radius)",
		duration = "Instantaneous",
		components = "Verbal",
		concentration = "",
		definition = """
		You create a momentary circle of spectral blades that sweep around you. All other creatures within 5 feet of you must succeed on a Dexterity saving throw or take 1d6 force damage.
		<br>
		This spell's damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).
		"""
		)
	Prestidigitation =  Spell("Prestidigitation", 	0,
		school = "Transmutation",
		casting_time = "Action",
		ranges = "10 feet",
		duration = "1 hour",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
		You create a magical effect within range. Choose the effect from the options below. If you cast this spell multiple times, you can have up to three of its non-instantaneous effects active at a time.
		<ul style="list-style-type: '🪄'; text-align: left; ">
<li> <b> Sensory Effect.</b> You create an instantaneous, harmless sensory effect, such as a shower of sparks, a puff of wind, faint musical notes, or an odd odor.
<li><b> Fire Play.</b> You instantaneously light or snuff out a candle, a torch, or a small campfire.
<li><b> Clean or Soil.</b> You instantaneously clean or soil an object no larger than 1 cubic foot.
<li><b> Minor Sensation.</b> You chill, warm, or flavor up to 1 cubic foot of nonliving material for 1 hour.
<li><b> Magic Mark.</b> You make a color, a small mark, or a symbol appear on an object or a surface for 1 hour.
<li><b> Minor Creation.</b> You create a nonmagical trinket or an illusory image that can fit in your hand. It lasts until the end of your next turn. A trinket can deal no damage and has no monetary worth.
		</ul>
		"""
		)
	TolltheDead =       Spell("Toll the Dead",      0,
		school = "Necromancy",
		casting_time = "Action",
		ranges = "60 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
		You point at one creature you can see within range, and the single chime of a dolorous bell is audible within 10 feet of the target. The target must succeed on a Wisdom saving throw or take 1d8 Necrotic damage. If the target is missing any of its Hit Points, it instead takes 1d12 Necrotic damage.
		<br>
		<b>Cantrip Upgrade.</b> The damage increases by one die when you reach levels 5 (2d8 or 2d12), 11 (3d8 or 3d12), and 17 (4d8 or 4d12).
		"""
		)
	MindSliver =        Spell("Mind Sliver",        0,
		school = "Enchantment",
		casting_time = "Action",
		ranges = "60 feet",
		duration = "Instantaneous",
		components = "Verbal",
		concentration = "",
		definition = """
		You try to temporarily sliver the mind of one creature you can see within range.
		The target must succeed on an <i>Intelligence saving throw</i> or take
		<i>1d6 Psychic damage</i> and subtract 1d4 from the next saving throw
		it makes before the end of your next turn.
		<br>
		<b>Cantrip Upgrade.</b> The damage increases by 1d6 when you reach
		levels 5 (2d6), 11 (3d6), and 17 (4d6).
		"""
		)
	Druidcraft =        Spell("Druidcraft",         0,
		school = "Transmutation",
		casting_time = "Action",
		ranges = "30 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
Whispering to the spirits of nature, you create one of the following effects within range.
<br>
<b>Weather Sensor.</b> You create a Tiny, harmless sensory effect that predicts what the weather will be at your location for the next 24 hours. The effect might manifest as a golden orb for clear skies, a cloud for rain, falling snowflakes for snow, and so on. This effect persists for 1 round.
<br>
<b>Bloom.</b> You instantly make a flower blossom, a seed pod open, or a leaf bud bloom.
<br>
<b>Sensory Effect.</b> You create a harmless sensory effect, such as falling leaves, spectral dancing fairies, a gentle breeze, the sound of an animal, or the faint odor of skunk. The effect must fit in a 5-foot Cube.
<br>
<b>Fire Play.</b> You light or snuff out a candle, a torch, or a campfire.
		"""
		)
	ThornWhip = 		Spell("Thorn Whip",			0,
		school = "Transmutation",
		casting_time = "Action",
		ranges = "30 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic, Material (the stem of a plant with thorns)",
		concentration = "",
		definition = """
You create a vine-like whip covered in thorns that lashes out at your command toward a creature in range. Make a melee spell attack against the target. On a hit, the target takes 1d6 Piercing damage, and if it is Large or smaller, you can pull it up to 10 feet closer to you.
<br>
<b>Cantrip Upgrade.</b> The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).
		"""
		)
	ProduceFlame =      Spell("Produce Flame",  	0,
		school = "Conjuration",
		casting_time = "Bonus action",
		ranges = "Self",
		duration = "10 minutes",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
A flickering flame appears in your hand and remains there for the duration. While there, the flame emits no heat and ignites nothing, and it sheds Bright Light in a 20-foot radius and Dim Light for an additional 20 feet. The spell ends if you cast it again.
<br>
Until the spell ends, you can take a Magic action to hurl fire at a creature or an object within 60 feet of you. Make a ranged spell attack. On a hit, the target takes 1d8 Fire damage.
<br>
Cantrip Upgrade. The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).
		"""
		)
	TrueStrike =        Spell("True Strike",        0,
		school = "Divination",
		casting_time = "Action",
		ranges = "Self",
		duration = "Instantaneous",
		components = "Somatic, Material (a weapon with which you have proficiency and that is worth 1+ CP)",
		concentration = "",
		definition = """
			Guided by a flash of magical insight, you make one attack with the weapon used in the spell's casting. The attack uses your spellcasting ability for the attack and damage rolls instead of using Strength or Dexterity. If the attack deals damage, it can be Radiant damage or the weapon's normal damage type (your choice).
			<br>
			<b>Cantrip Upgrade.</b> Whether you deal Radiant damage or the weapon's normal damage type, the attack deals extra Radiant damage when you reach levels 5 (1d6), 11 (2d6), and 17 (3d6).
			"""
			)
	RayofFrost =        Spell("Ray of Frost", 		0,
		school = "Evocation",
		casting_time = "Action",
		ranges = "60 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
			A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 Cold damage, and its Speed is reduced by 10 feet until the start of your next turn.
			<br>
			<b>Cantrip Upgrade.</b> The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).
			"""
			)
	Friends =           Spell("Friends",            0,
		school = "Enchantment",
		casting_time = "Action",
		ranges = "10 feet",
		duration = "1 minute",
		components = "Somatic, Material (some makeup)",
		concentration = "",
		definition = """
			You magically emanate a sense of friendship toward one creature you can see within range. The target must succeed on a Wisdom saving throw or have the Charmed condition for the duration. The target succeeds automatically if it isn't a Humanoid, if you're fighting it, or if you have cast this spell on it within the past 24 hours.
			<br>
			The spell ends early if the target takes damage or if you make an attack roll, deal damage, or force anyone to make a saving throw. When the spell ends, the target knows it was Charmed by you.
			"""
			)
	CreateBonfire =     Spell("Create Bonfire",     0,
		school = "Conjuration",
		casting_time = "Action",
		ranges = "60 feet",
		duration = "1 minute",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		definition = """
			You create a bonfire on ground that you can see within range. Until the spell ends, the magic bonfire fills a 5-foot cube. Any creature in the bonfire's space when you cast the spell must succeed on a Dexterity saving throw or take 1d8 fire damage. A creature must also make the saving throw when it moves into the bonfire's space for the first time on a turn or ends its turn there.
			<br>
			The bonfire ignites flammable objects in its area that aren't being worn or carried.
			<br>
			The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).
			"""
			)
	EldritchBlast =     Spell("Eldritch Blast",     0,
		school = "Evocation",
		casting_time = "Action",
		ranges = "120 feet",
		components = "Verbal, Somatic",
		duration = "Instantaneous",
		concentration = "",
		definition = """
			You hurl a beam of crackling energy. Make a ranged spell attack against one creature or object in range. On a hit, the target takes 1d10 Force damage.
			<br>
			<b>Cantrip Upgrade.</b> The spell creates two beams at level 5, three beams at level 11, and four beams at level 17. You can direct the beams at the same target or at different ones. Make a separate attack roll for each beam.
			"""
			)
	ViciousMockery =    Spell("Vicious Mockery",    0,
		school = "Enchantment",
		casting_time = "Action",
		ranges = "60 feet",
		components = "Verbal",
		duration = "Instantaneous",
		concentration = "",
		definition = """
You unleash a string of insults laced with subtle enchantments at one creature you can see or hear within range. The target must succeed on a Wisdom saving throw or take 1d6 Psychic damage and have Disadvantage on the next attack roll it makes before the end of its next turn.
<br>
Cantrip Upgrade. The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).
			"""
			)




	# Rewrites

# First Level Spells
LEVEL1 = True
if LEVEL1:
	BurningHands =          Spell("Burning Hands ",1,"Evocation ","1 Action ","Self (15-foot cone) ","Instantaneous ","Verbal, Somatic")
	ChaosBolt =             Spell("Chaos Bolt ",1,"Evocation ","1 Action ","120 feet ","Instantaneous ","Verbal, Somatic")
	ComprehendLanguages = 	Spell("Comprehend Languages",	1,	"Divination",	"1 Action R ",	"Self ",	"1 hour ",	"Verbal, Somatic, Material")
	CreateorDestroyWater = 	Spell("Create or Destroy Water ",1,"Transmutation ","1 Action ","30 feet ","Instantaneous ","Verbal, Somatic, Material")
	DissonantWhispers = 	Spell("Dissonant Whispers ",1,"Enchantment ","1 Action ","60 feet ","Instantaneous ","Verbal")
	DivineFavor =         	Spell("Divine Favor ",1,"Evocation ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal, Somatic")
	EnsnaringStrike =   	Spell("Ensnaring Strike ",1,"Conjuration ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal")
	Entangle =          	Spell("Entangle ",1,"Conjuration ","1 Action ","90 feet ","Concentration, up to 1 minute ","Verbal, Somatic")
	ExpeditiousRetreat =  	Spell("Expeditious Retreat ",
			level=1,
			school="Transmutation",
			casting_time="Bonus Action",
			ranges = "Self",
			duration = "Up to 10 minute",
			components = "Verbal, Somatic",
			concentration = "Concentration",
			definition = """
			You take the <b>Dash action</b>, and until the spell ends, you can take that action again as a <i>Bonus Action</i>.
			<br>""")
	FaerieFire =        	Spell("Faerie Fire ",1,"Evocation ","1 Action ","60 feet ","Concentration, up to 1 minute ","Verbal")
	FindFamiliar =      	Spell("Find Familiar ",1,"Conjuration ","1 Hour R ","10 feet ","Instantaneous ","Verbal, Somatic, Material")
	FrostFingers =  		Spell("Frost Fingers ",1,"Evocation ","1 Action ","Self (15-foot cone) ","Instantaneous ","Verbal, Somatic")
	GiftofAlacrity = 		Spell("Gift of Alacrity ",1,"Divination","1 Minute ","Touch ","8 hours ","Verbal, Somatic")
	Goodberry =         Spell("Goodberry ",1,"Transmutation ","1 Action ","Touch ","Instantaneous ","Verbal, Somatic, Material")
	Grease =            Spell("Grease ",1,"Conjuration ","1 Action ","60 feet ","1 minute ","Verbal, Somatic, Material")
	GuidingBolt = 		Spell("Guiding Bolt ",1,"Evocation ","1 Action ","120 feet ","1 round ","Verbal, Somatic")
	HailofThorns = 		Spell("Hail of Thorns ",1,"Conjuration ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal")
	HellishRebuke =     Spell("Hellish Rebuke ",1,"Evocation ","1 Reaction ","60 feet ","Instantaneous ","Verbal, Somatic")
	HuntersMark =       Spell("Hunter's Mark ",1,"Divination ","1 Bonus Action ","90 feet ","Concentration, up to 1 hour ","Verbal")
	Identify =          Spell("Identify",   1,"Divination ","1 Minute R ","Touch ","Instantaneous ","Verbal, Somatic, Material")
	InflictWounds =     Spell("Inflict Wounds ",1,"Necromancy ","1 Action ","Touch ","Instantaneous ","Verbal, Somatic")
	JimsMagicMissile = 	Spell("Jim's Magic Missile ",1,"Evocation ","1 Action ","120 feet ","Instantaneous ","Verbal, Somatic, Material")
	Jump =              Spell("Jump ",1,"Transmutation ","1 Action ","Touch ","1 minute ","Verbal, Somatic, Material")
	Longstrider = 		Spell("Longstrider ",1,"Transmutation ","1 Action ","Touch ","1 hour ","Verbal, Somatic, Material")
	MagicMissile = 		Spell("Magic Missile ",	1,	"Evocation ",
		"1 Action",	"120 feet",	"Instantaneous",	"Verbal, Somatic",
		definition = """You create three glowing darts of magical force. Each dart strikes a creature of your choice that you can see within range. A dart deals <i>1d4 + 1 Force damage</i> to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several.
		<br>
		<b>Using a Higher-Level Spell Slot.</b> The spell creates one more dart for each spell slot level above 1.""")
	MagnifyGravity = 	Spell("Magnify Gravity ",1,"Transmutation DG ","1 Action ","60 feet ","1 round ","Verbal, Somatic")
	RayofSickness = 	Spell("Ray of Sickness ",1,"Necromancy ","1 Action ","60 feet ","Instantaneous ","Verbal, Somatic")
	SearingSmite =     	Spell("Searing Smite ",1,"Evocation ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal")
	Shield =        	Spell("Shield ",1,"Abjuration ","1 Reaction ","Self ","1 round ","Verbal, Somatic")
	ShieldofFaith = 	Spell("Shield of Faith ",1,"Abjuration ","1 Bonus Action ","60 feet ","Concentration, up to 1 minute ","Verbal, Somatic, Material")
	Sleep =         	Spell("Sleep ",1,"Enchantment ","1 Action ","90 feet ","1 minute ","Verbal, Somatic, Material")
	Snare =         	Spell("Snare ",1,"Abjuration ","1 Minute ","Touch ","Until dispelled or triggered ","Verbal, Somatic, Material")
	CausticBrew =     	Spell("Tasha's Caustic Brew ",1,"Evocation ","1 Action ","Self (30-foot line) ","Concentration, up to 1 minute ","Verbal, Somatic, Material")
	FloatingDisk =     	Spell("Tenser's Floating Disk ",1,"Conjuration ","1 Action R ","30 feet ","1 hour ","Verbal, Somatic, Material")
	ThunderousSmite = 	Spell("Thunderous Smite ",1,"Evocation ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal")
	Thunderwave =     	Spell("Thunderwave ",1,"Evocation ","1 Action ","Self (15-foot cube) ","Instantaneous ","Verbal, Somatic")
	ZephyrStrike =     	Spell("Zephyr Strike ",1,"Transmutation ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal")
	Alarm =                 Spell("Alarm",  1,"Abjuration","1 Minute (R)" ,"30 feet", "8 Hours","Verbal, Somatic, Material")
	ArmorofAgathys =        Spell("Armor of Agathys",   1,"Abjuration", "1 Action" ,"Self", "1 hour ", "Verbal, Somatic, Material")
	Ceremony =              Spell("Ceremony ",        1,"Evocation ","1 Action R ","Touch ","Instantaneous ","Verbal, Somatic, Material")

	AbsorbElements =        	Spell("Absorb Element",	1,"Abjuration","1 Reaction","Self","1 round", "Somatic")
	BeastBond =             	Spell("Beast Bond",   	1,"Divination ","1 Action ","Touch ","Concentration, up to 1 minute ","Verbal, Somatic, Material")
	Catapult =              	Spell("Catapult ",   	1,"Transmutation ","1 Action ","60 feet ","Instantaneous ","Somatic")
	CharmPerson =               Spell("Charm Person",	1,	"Enchantment",
		"1 Action",	"30 feet",	"1 hour",	"Verbal, Somatic",	"",
		definition = """One Humanoid you can see within range makes a <i>Wisdom saving throw</i>. It does so with <i>Advantage</i> if you or your allies are fighting it. On a failed save, the target has the <i>Charmed condition</i> until the spell ends or until you or your allies damage it. The Charmed creature is <i>Friendly</i> to you. When the spell ends, the target knows it was Charmed by you.
<br>
<b>Using a Higher-Level Spell Slot.</b> You can target one additional creature for each spell slot level above 1."""
		)
	CauseFear =             	Spell("Cause Fear ",	1,"Necromancy ","1 Action ","60 feet ","Concentration, up to 1 minute ","Verbal, Somatic")
	EarthTremor =       		Spell("Earth Tremor",	1,"Evocation ","1 Action ","Self (10-foot radius) ","Instantaneous ","Verbal, Somatic")
	Bless =                 	Spell("Bless",         	1,"Enchantment ","1 Action ","30 feet ","Concentration, up to 1 minute ","Verbal, Somatic, Material")
	Sanctuary =     			Spell("Sanctuary",		1,"Abjuration ","1 Bonus Action ","30 feet ","1 minute ","Verbal, Somatic, Material")
	BurningHands =          	Spell("Burning Hands",
		1,	"Evocation",	"1 Action",	"Self (15-foot cone)",	"Instantaneous",
		"Verbal, Somatic", definition = """A thin sheet of flames shoots forth from you. Each creature in a <i>15-foot Cone</i> makes a <i>Dexterity saving throw</i>, taking <i>3d6 Fire damage</i> on a failed save or half as much damage on a successful one.
<br>
Flammable objects in the Cone that aren't being worn or carried start burning.
<br>
<b>Using a Higher-Level Spell Slot.</b> The damage increases by <i>1d6</i> for each spell slot level above 1. """)
	CauseFear =             	Spell("Cause Fear ",1,"Necromancy ","1 Action ","60 feet ","Concentration, up to 1 minute ","Verbal, Somatic")
	ChaosBolt =             	Spell("Chaos Bolt ",	1,"Evocation ","1 Action ","120 feet ","Instantaneous ","Verbal, Somatic")
	ChromaticOrb =          	Spell("Chromatic Orb ",
		level=1,
		school="Evocation",
		casting_time="Action",
		ranges = "90 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic, Material (a diamond worth 50+ GP)",
		concentration = "",
		definition = """You hurl an orb of energy at a target within range. Choose <i>Acid, Cold, Fire, Lightning, Poison, or Thunder</i> for the type of orb you create, and then make a <i>ranged spell attack</i> against the target. On a hit, the target takes <b>3d8 damage</b> of the chosen type. <br>
		If you roll the same number on two or more of the <b>d8</b>s, the orb leaps to a different target of your choice within <i>30 feet</i> of the target. Make an <b>attack roll</b> against the new target, and make a new <b>damage roll</b>. The orb can't leap again unless you cast the spell with a level 2+ spell slot. <br>
		<b>Using a Higher-Level Spell Slot.</b> The damage increases by <i>1d8</i> for each spell slot level above 1. The orb can leap a maximum number of times equal to the level of the slot expended, and a creature can be targeted only once by each casting of this spell."""
		)
	ComprehendLanguages =       Spell("Comprehend Languages ",1,"Divination ","1 Action R ","Self ","1 hour ","Verbal, Somatic, Material")
	CreateorDestroyWater =      Spell("Create or Destroy Water ",1,"Transmutation ","1 Action ","30 feet ","Instantaneous ","Verbal, Somatic, Material")
	DetectMagic =               Spell("Detect Magic",	1, 	"Divination",
		"1 Action or Ritual",	"Self",	"up to 10 minutes",	"Verbal, Somatic",
		"Concentration",
		definition = """For the duration, you sense the presence of magical effects within <i>30 feet</i> of yourself. If you sense such effects, you can take the <i>Magic action</i> to see a faint aura around any visible creature or object in the area that bears the magic, and if an effect was created by a spell, you learn the spell's school of magic. <br>
The spell is blocked by 1 foot of stone, dirt, or wood; 1 inch of metal; or a thin sheet of lead.
"""
		)
	DissonantWhispers =     	Spell("Dissonant Whispers ",1,"Enchantment ","1 Action ","60 feet ","Instantaneous ","Verbal")
	DivineFavor =         	Spell("Divine Favor ",1,"Evocation ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal, Somatic")
	EarthTremor =       Spell("Earth Tremor ",1,"Evocation ","1 Action ","Self (10-foot radius) ","Instantaneous ","Verbal, Somatic")
	EnsnaringStrike =   Spell("Ensnaring Strike ",1,"Conjuration ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal")
	Entangle =          Spell("Entangle ",1,"Conjuration ","1 Action ","90 feet ","Concentration, up to 1 minute ","Verbal, Somatic")
	FaerieFire =        Spell("Faerie Fire ",1,"Evocation ","1 Action ","60 feet ","Concentration, up to 1 minute ","Verbal")
	FindFamiliar =      Spell("Find Familiar ",1,"Conjuration ","1 Hour R ","10 feet ","Instantaneous ","Verbal, Somatic, Material")
	FrostFingers =         Spell("Frost Fingers ",1,"Evocation ","1 Action ","Self (15-foot cone) ","Instantaneous ","Verbal, Somatic")
	GiftofAlacrity = 	Spell("Gift of Alacrity ",
		1,	"Divination",	"1 Minute ",	"Touch ",
		"8 hours ",	"Verbal, Somatic")
	Goodberry =         Spell("Goodberry ",1,"Transmutation ","1 Action ","Touch ","Instantaneous ","Verbal, Somatic, Material")
	Grease =            Spell("Grease ",1,"Conjuration ","1 Action ","60 feet ","1 minute ","Verbal, Somatic, Material")
	GuidingBolt = 		Spell("Guiding Bolt ",1,"Evocation ","1 Action ","120 feet ","1 round ","Verbal, Somatic")
	HailofThorns = 		Spell("Hail of Thorns ",1,"Conjuration ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal")
	HellishRebuke =     Spell("Hellish Rebuke ",1,"Evocation ","1 Reaction ","60 feet ","Instantaneous ","Verbal, Somatic")
	HuntersMark =       Spell("Hunter's Mark ",	1,	"Divination ","1 Bonus Action ","90 feet ","Concentration, up to 1 hour ","Verbal")
	Identify =          Spell("Identify",   1,	"Divination ","1 Minute R ","Touch ","Instantaneous ","Verbal, Somatic, Material")
	InflictWounds =     Spell("Inflict Wounds ",1,"Necromancy ","1 Action ","Touch ","Instantaneous ","Verbal, Somatic")
	JimsMagicMissile = 	Spell("Jim's Magic Missile ",1,"Evocation ","1 Action ","120 feet ","Instantaneous ","Verbal, Somatic, Material")
	Jump =              Spell("Jump ",1,"Transmutation ","1 Action ","Touch ","1 minute ","Verbal, Somatic, Material")
	Longstrider = 		Spell("Longstrider ",1,"Transmutation ","1 Action ","Touch ","1 hour ","Verbal, Somatic, Material")
	MageArmor =         Spell("Mage Armor ",1,"Abjuration ","1 Action ","Touch ","8 hours ","Verbal, Somatic, Material")
	MagnifyGravity = 	Spell("Magnify Gravity ",1,"Transmutation DG ","1 Action ","60 feet ","1 round ","Verbal, Somatic")
	RayofSickness = 	Spell("Ray of Sickness ",1,"Necromancy ","1 Action ","60 feet ","Instantaneous ","Verbal, Somatic")
	Sanctuary =     	Spell("Sanctuary ",1,"Abjuration ","1 Bonus Action ","30 feet ","1 minute ","Verbal, Somatic, Material")
	SearingSmite =     	Spell("Searing Smite ",1,"Evocation ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal")
	Shield =        	Spell("Shield ",
		1,"Abjuration ","1 Reaction ","Self ","1 round ","Verbal, Somatic")
	ShieldofFaith = 	Spell("Shield of Faith ",1,"Abjuration ","1 Bonus Action ","60 feet ","Concentration, up to 1 minute ","Verbal, Somatic, Material")
	Sleep =         	Spell("Sleep ",1,"Enchantment ","1 Action ","90 feet ","1 minute ","Verbal, Somatic, Material")
	Snare =         	Spell("Snare ",1,"Abjuration ","1 Minute ","Touch ","Until dispelled or triggered ","Verbal, Somatic, Material")
	CausticBrew =     	Spell("Tasha's Caustic Brew ",1,"Evocation ","1 Action ","Self (30-foot line) ","Concentration, up to 1 minute ","Verbal, Somatic, Material")
	FloatingDisk =     	Spell("Tenser's Floating Disk ",1,"Conjuration ","1 Action R ","30 feet ","1 hour ","Verbal, Somatic, Material")
	ThunderousSmite = 	Spell("Thunderous Smite ",1,"Evocation ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal")
	Thunderwave =     	Spell("Thunderwave ",1,"Evocation ","1 Action ","Self (15-foot cube) ","Instantaneous ","Verbal, Somatic")
	ZephyrStrike =     	Spell("Zephyr Strike ",1,"Transmutation ","1 Bonus Action ","Self ","Concentration, up to 1 minute ","Verbal")
	Alarm = 			Spell("Alarm",  1,"Abjuration","1 Minute (R)" ,"30 feet", "8 Hours","Verbal, Somatic, Material")
	ArmorofAgathys = 	Spell("Armor of Agathys",   1,"Abjuration", "1 Action" ,"Self", "1 hour ", "Verbal, Somatic, Material")
	Ceremony = 			Spell(	"Ceremony ",        1,		"Evocation",
								"1 Action R",	"Touch",	"Instantaneous",
								"Verbal, Somatic, Material")
	AbsorbElements =        Spell("Absorb Element",    1,  "Abjuration","1 Reaction","Self","1 round", "Somatic")
	BeastBond =             Spell("Beast Bond",        1,	"Divination ","1 Action ","Touch ","Concentration, up to 1 minute ","Verbal, Somatic, Material")
	Bless =                 Spell("Bless ",            1,"Enchantment ","1 Action ","30 feet ","Concentration, up to 1 minute ","Verbal, Somatic, Material")
	Catapult =              Spell("Catapult ",        1,"Transmutation ","1 Action ","60 feet ","Instantaneous ","Somatic")
	DisguiseSelf =              Spell("Disguise Self ",1,"Illusion ","1 Action ","Self ","1 hour ","Verbal, Somatic")
	FalseLife = 	Spell("False Life ",1,"Necromancy ","1 Action ","Self ","Instantaneous","Verbal, Somatic, Material [a drop of alcohol]",
					definition = """You gain <b>2d4 + 4 Temporary Hit Points</b>.
						<br><b>Using a Higher-Level Spell Slot.</b> You gain <i>5 additional Temporary Hit Points</i> for each spell slot level above 1.""")
	ColorSpray = 	Spell("Color Spray ",1,"Illusion ","1 Action ","Self (15-foot cone) ","1 round ","Verbal, Somatic, Material [a pinch of colorful sand]",
		definition = """You launch a dazzling array of flashing, colorful light. Each creature in a <i>15-foot Cone</i> originating from you must succeed on a <i>Constitution saving throw</i> or have the <i>Blinded</i> condition until the end of your next turn."""
		)

	MageArmor = Spell("Mage Armor ",1,"Abjuration ","1 Action ","Touch ","8 hours ","Verbal, Somatic, Material",
		definition = """You touch a willing creature who isn't wearing armor. Until the spell ends, the target's base AC becomes 13 plus its Dexterity modifier. The spell ends early if the target dons armor."""
		)
	CureWounds = Spell("Cure Wounds",	1,"Abjuration ","Action", "Touch ","Instantaneous ","Verbal, Somatic",
		definition = """A creature you touch regains a number of <b>Hit Points</b> equal to <b>2d8 plus your spellcasting ability modifier</b>.
		<b>Using a Higher-Level Spell Slot.</b> The healing increases by <b>2d8 for each spell slot</b> level above 1."""
		)
	UnseenServant = 	Spell("Unseen Servant ",1,"Conjuration","Action or Ritual","60 feet","1 hour ","Verbal, Somatic, Material (a bit of string and of wood)",
		definition = """This spell creates an Invisible, mindless, shapelesSomatic, Materialedium force that performs simple tasks at your command until the spell ends. The servant springs into existence in an unoccupied space on the ground within range. It has AC 10, 1 Hit Point, and a Strength of 2, and it can't attack. If it drops to 0 Hit Points, the spell ends.
			<br>
			Once on each of your turns as a Bonus Action, you can mentally command the servant to move up to 15 feet and interact with an object. The servant can perform simple tasks that a human could do, such as fetching things, cleaning, mending, folding clothes, lighting fires, serving food, and pouring drinks. Once you give the command, the servant performs the task to the best of its ability until it completes the task, then waits for your next command.
			<br>
			If you command the servant to perform a task that would move it more than 60 feet away from you, the spell ends.
			"""
			)
	Hex =               Spell("Hex ",1,"Enchantment ","1 Bonus Action ","90 feet ","1 hour ","Verbal, Somatic, Material(the petrified eye of a newt)",
			concentration = "Concentration",
			definition = """You place a curse on a creature that you can see within range.
			Until the spell ends, you deal an extra 1d6 Necrotic damage to the target whenever you hit it with an attack roll.
			Also, choose one ability when you cast the spell.
			The target has Disadvantage on ability checks made with the chosen ability.
<br>
If the target drops to 0 Hit Points before this spell ends,
you can take a Bonus Action on a later turn to curse a new creature.
<br>
<b>Using a Higher-Level Spell Slot.</b> Your Concentration can last longer with a spell slot of level 2 (up to 4 hours), 3-4 (up to 8 hours), or 5+ (24 hours).
			""")
	DetectPoisonandDisease =    Spell("Detect Poison and Disease",
		level=1,
		school="Divination",
		casting_time="Action or Ritual",
		ranges = "Self",
		duration = "Up to 10 minutes",
		components = "Verbal, Somatic, Material (a yew leaf)",
		concentration = "Concentration",
		definition = """
		For the duration, you sense the location of poisons, poisonous or venomous creatures, and magical contagions within 30 feet of yourself. You sense the kind of poison, creature, or contagion in each case.
		<br>
		The spell is blocked by 1 foot of stone, dirt, or wood; 1 inch of metal; or a thin sheet of lead.
		"""
		)
	FogCloud = Spell("Fog Cloud ",
		level=1,
		school="Conjuration",
		casting_time="Action",
		ranges = "120 feet",
		duration = "1 hour",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		definition = """
		You create a 20-foot-radius Sphere of fog centered on a point within range. The Sphere is Heavily Obscured. It lasts for the duration or until a strong wind (such as one created by Gust of Wind) disperses it.
		<br>
		<b>Using a Higher-Level Spell Slot.</b> The fog's radius increases by 20 feet for each spell slot level above 1.
		"""
		)
	IceKnife = 			Spell("Ice Knife",
		level=1,
		school="Conjuration",
		casting_time="Action",
		ranges = "60 feet",
		duration = "Instantaneous",
		components = "Somatic, Material (a drop of water or a piece of ice)",
		concentration = "Concentration",
		definition = """
		You create a shard of ice and fling it at one creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 Piercing damage. Hit or miss, the shard then explodes. The target and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 2d6 Cold damage.
		<br>
		Using a Higher-Level Spell Slot. The Cold damage increases by 1d6 for each spell slot level above 1.
		"""
		)
	PurifyFoodandDrink = Spell("Purify Food and Drink ",
		level=1,
		school="Transmutation",
		casting_time="Action or Ritual",
		ranges = "10 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		definition = """
		You remove poison and rot from nonmagical food and drink in a 5-foot-radius Sphere centered on a point within range.
		"""
		)
	SpeakwithAnimals = 	Spell("Speak with Animals",
		level=1,
		school="Divination",
		casting_time="Action or Ritual",
		ranges = "Self",
		duration = "10 minutes",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
		For the duration, you can comprehend and verbally communicate with Beasts, and you can use any of the Influence action's skill options with them.
		<br>
		Most Beasts have little to say about topics that don't pertain to survival or companionship, but at minimum, a Beast can give you information about nearby locations and monsters, including whatever it has perceived within the past day.
		"""
		)
	Bane = 	Spell("Bane",
			level=1,
			school="Enchantment",
			casting_time="Action",
			ranges = "30 feet",
			duration = "1 minute",
			components = "Verbal, Somatic, Material (a drop of blood)",
			concentration = "Concentration",
			definition = """
			Up to three creatures of your choice that you can see within range must each make a Charisma saving throw. Whenever a target that fails this save makes an attack roll or a saving throw before the spell ends, the target must subtract 1d4 from the attack roll or save.
			<br>
			Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 1.
			"""
			)
	DistortValue = 	Spell("Distort Value",
					level=1,
					school="Illusion",
					casting_time="1 Minute",
					ranges = "Touch",
					duration = "8 hours",
					components = "Verbal",
					concentration = "Concentration",
					definition = """
Do you need to squeeze a few more gold pieces out of a merchant as you try to sell that weird octopus statue you liberated from the chaos temple? Do you need to downplay the worth of some magical assets when the tax collector stops by? Distort value has you covered.
<br>
You cast this spell on an object no more than 1 foot on a side, doubling the object's perceived value by adding illusory flourishes or polish to it, or reducing its perceived value by half with the help of illusory scratches, dents, and other unsightly features. Anyone examining the object can ascertain its true value with a successful Intelligence (Investigation) check against your spell save DC.
<br>
At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the maximum size of the object increases by 1 foot for each slot level above 1st.
"""					)

	ArmsOfHadar =	Spell("Arms of Hadar",
					level=1,
					school="Conjuration",
					casting_time="Action",
					ranges = "Self",
					duration = "Instantaneous",
					components = "Verbal, Somatic",
					concentration = "Concentration",
					definition = """
					Invoking Hadar, you cause tendrils to erupt from yourself. Each creature in a 10-foot Emanation originating from you makes a Strength saving throw. On a failed save, a target takes 2d6 Necrotic damage and can't take Reactions until the start of its next turn. On a successful save, a target takes half as much damage only.
					<br>
					<b>Using a Higher-Level Spell Slot.</b> The damage increases by 1d6 for each spell slot level above 1.
					""")
	WitchBolt = Spell("Witch Bolt",
				level=1,
				school="Evocation",
				casting_time="Action",
				ranges = "60 feet",
				duration = "1 minute",
				components = "Verbal, Somatic, Material (a twig struck by lightning)",
				concentration = "Concentration",
				definition = """
				A beam of crackling energy lances toward a creature within range, forming a sustained arc of lightning between you and the target. Make a ranged spell attack against it. On a hit, the target takes 2d12 Lightning damage.
				<br>
				On each of your subsequent turns, you can take a Bonus Action to deal 1d12 Lightning damage to the target automatically, even if the first attack missed.
				<br>
				The spell ends if the target is ever outside the spell's range or if it has Total Cover from you.
				<br>
				Using a Higher-Level Spell Slot. The initial damage increases by 1d12 for each spell slot level above 1.
				""")
	ProtectionfromEvilandGood = 	Spell("Protection from Evil and Good",
			level=1,
			school="Abjuration",
			casting_time="Action",
			ranges = "Touch",
			duration = "10 minutes",
			components = "Verbal, Somatic, Material (a flask of Holy Water worth 25+ GP, which the spell consumes)",
			concentration = "Concentration",
			definition = """
			Until the spell ends, one willing creature you touch is protected against creatures that are Aberrations, Celestials, Elementals, Fey, Fiends, or Undead. The protection grants several benefits. Creatures of those types have Disadvantage on attack rolls against the target. The target also can't be possessed by or gain the Charmed or Frightened conditions from them. If the target is already possessed, Charmed, or Frightened by such a creature, the target has Advantage on any new saving throw against the relevant effect.
			""")
	Command = 	Spell("Command",
				level=1,
				school="Enchantment",
				casting_time="Action",
				ranges = "60 feet",
				components = "Verbal",
				duration = "Instantaneous",
				concentration = "",
				definition = """
You speak a one-word command to a creature you can see within range. The target must succeed on a Wisdom saving throw or follow the command on its next turn. Choose the command from these options:
<ul style="list-style-type: '۞'; text-align: left; ">
  <li><b>Approach.</b> The target moves toward you by the shortest and most direct route, ending its turn if it moves within 5 feet of you.</li>
  <li><b>Drop.</b>  The target drops whatever it is holding and then ends its turn.</li>
  <li><b>Flee.</b>  The target spends its turn moving away from you by the fastest available means.</li>
  <li><b>Grovel.</b>  The target has the Prone condition and then ends its turn.</li>
  <li><b>Halt.</b>  On its turn, the target doesn't move and takes no action or Bonus Action.</li>
 </ul>
<b>Using a Higher-Level Spell Slot.</b> You can affect one additional creature for each spell slot level above 1.
				""")
	IllusoryScript = 	Spell("Illusory Script",
		level=1,
		school="Illusion",
		casting_time="1 minute or Ritual",
		ranges = "Touch",
		components = "Somatic, Material (ink worth 10+ GP, which the spell consumes)",
		duration = "10 days",
		concentration = "",
		definition = """
You write on parchment, paper, or another suitable material and imbue it with an illusion that lasts for the duration. To you and any creatures you designate when you cast the spell, the writing appears normal, seems to be written in your hand, and conveys whatever meaning you intended when you wrote the text. To all others, the writing appears as if it were written in an unknown or magical script that is unintelligible. Alternatively, the illusion can alter the meaning, handwriting, and language of the text, though the language must be one you know.
<br>
If the spell is dispelled, the original script and the illusion both disappear.
<br>
A creature that has Truesight can read the hidden message.
			""")
	DetectEvilandGood = Spell("Detect Evil and Good",
			level=1,
			school="Divination",
			casting_time="Action",
			ranges = "Self",
			components = "Verbal, Somatic",
			concentration = "Concentration",
			duration = "10 minutes",
			definition = """
			For the duration, you sense the location of any Aberration, Celestial, Elemental, Fey, Fiend, or Undead within 30 feet of yourself. You also sense whether the Hallow spell is active there and, if so, where.
			<br>
			The spell is blocked by 1 foot of stone, dirt, or wood; 1 inch of metal; or a thin sheet of lead.
			""")
	SilentImage =       Spell("Silent Image" ,
			level=1,
			school="Illusion",
			casting_time="60 feet",
			ranges = "Self",
			components = "Verbal, Somatic, Material (a bit of fleece)",
			duration = "10 minutes",
			concentration = "Concentration",
			definition = """
You create the image of an object, a creature, or some other visible phenomenon that is no larger than a 15-foot Cube. The image appears at a spot within range and lasts for the duration. The image is purely visual; it isn't accompanied by sound, smell, or other sensory effects.
<br>
As a Magic action, you can cause the image to move to any spot within range. As the image changes location, you can alter its appearance so that its movements appear natural for the image. For example, if you create an image of a creature and move it, you can alter the image so that it appears to be walking.
<br>
Physical interaction with the image reveals it to be an illusion, since things can pass through it. A creature that takes a Study action to examine the image can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the creature can see through the image.
			""")
	AnimalFriendship = 	Spell("Animal Friendship",
		level=1,
		school="Enchantment",
		casting_time="Action",
		ranges = "30 feet",
		duration = "24 hours",
		components = "Verbal, Somatic, Material (a morsel of food)",
		concentration = "",
		definition = """
		Target a Beast that you can see within range. The target must succeed on a Wisdom saving throw or have the Charmed condition for the duration. If you or one of your allies deals damage to the target, the spells ends.
		<br>
		Using a Higher-Level Spell Slot. You can target one additional Beast for each spell slot level above 1.
		"""
		)
	FeatherFall =       Spell("Feather Fall",
		level=1,
		school="Transmutation",
		casting_time="Reaction, which you take when you or a creature you can see within 60 feet of you falls",
		ranges = "60 feet",
		duration = "1 minute",
		components = "Verbal, Material (a small feather or piece of down)",
		concentration = "",
		definition = """
		Choose up to five falling creatures within range. A falling creature's rate of descent slows to 60 feet per round until the spell ends. If a creature lands before the spell ends, the creature takes no damage from the fall, and the spell ends for that creature.
		"""
		)
	Heroism = Spell("Heroism",
		level=1,
		school="Enchantment",
		casting_time="Action",
		ranges = "Touch",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		duration = "1 minute",
		definition = """
			A willing creature you touch is imbued with bravery. Until the spell ends, the creature is immune to the Frightened condition and gains Temporary Hit Points equal to your spellcasting ability modifier at the start of each of its turns.
			<br>
			Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 1.
			"""
			)
	HideousLaughter = 	Spell("Tasha's Hideous Laughter",
		level=1,
		school="Enchantment",
		casting_time="Action",
		ranges = "30 feet",
		components = "Verbal, Somatic, Material (a tart and a feather)",
		concentration = "Concentration",
		duration = "1 minute",
		definition = """
One creature of your choice that you can see within range makes a Wisdom saving throw. On a failed save, it has the Prone and Incapacitated conditions for the duration. During that time, it laughs uncontrollably if it's capable of laughter, and it can't end the Prone condition on itself.
<br>
At the end of each of its turns and each time it takes damage, it makes another Wisdom saving throw. The target has Advantage on the save if the save is triggered by damage. On a successful save, the spell ends.
<br>
Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 1.
			"""
			)
	WrathfulSmite = 	Spell("Wrathful Smite",
		level=1,
		school="Necromancy",
		casting_time="Bonus action, which you take immediately after hitting a creature with a Melee weapon or an Unarmed Strike",
		ranges = "Self",
		components = "Verbal",
		concentration = "",
		duration = "1 minute",
		definition = """
The target takes an extra 1d6 Necrotic damage from the attack, and it must succeed on a Wisdom saving throw or have the Frightened condition until the spell ends. At the end of each of its turns, the Frightened target repeats the save, ending the spell on itself on a success.
<br>
Using a Higher-Level Spell Slot. The damage increases by 1d6 for each spell slot level above 1.
			"""	)
	SilveryBarbs =  Spell("Silvery Barbs",
		level=1,
		school="Enchantment",
		casting_time="Reaction, which you take when a creature you can see within 60 feet of yourself succeeds on an attack roll, an ability check, or a saving throw",
		ranges = "60 feet",
		components = "Verbal",
		concentration = "",
		duration = "Instantaneous",
		definition = """
		You magically distract the triggering creature and turn its momentary uncertainty into encouragement for another creature. The triggering creature must reroll the d20 and use the lower roll.
		<br>
		You can then choose a different creature you can see within range (you can choose yourself). The chosen creature has advantage on the next attack roll, ability check, or saving throw it makes within 1 minute. A creature can be empowered by only one use of this spell at a time.
		""")
	CompelledDuel = Spell("Compelled Duel",
		level = 1,
		school = "Enchantment",
		casting_time = "Bonus Action",
		ranges = "30 feet",
		components = "Verbal",
		concentration = "Concentration",
		duration = "1 minute",
		definition = """
		You try to compel a creature into a duel. One creature that you can see within range makes a Wisdom saving throw. On a failed save, the target has Disadvantage on attack rolls against creatures other than you, and it can't willingly move to a space that is more than 30 feet away from you.
<br>
The spell ends if you make an attack roll against a creature other than the target, if you cast a spell on an enemy other than the target, if an ally of yours damages the target, or if you end your turn more than 30 feet away from the target.
		""")
	HealingWord = Spell("Healing Word",
		level = 1,
		school = "Abjuration",
		casting_time = "Bonus Action",
		ranges = "60 feet",
		components = "Verbal",
		concentration = "",
		duration = "Instantaneous",
		definition = """
A creature of your choice that you can see within range regains Hit Points equal to 2d4 plus your spellcasting ability modifier.
<br>
Using a Higher-Level Spell Slot. The healing increases by 2d4 for each spell slot level above 1.
		""")



# Initialize second level spells
LEVEL2 = True
if LEVEL2:
	AirBubble = 		Spell("Air Bubble", 2, "Conjuration", "1 Action", "60 Feet", "24 hours", "Somatic")
	ArcaneLock = 		Spell("Arcane Lock", 2, "Abjuration", "1 Action", "Touch", "Until dispelled", "Verbal, Somatic, Material")
	BlindnessDeafness = Spell("Blindness/Deafness",
		2, "Necromancy", "1 Action", "30 Feet", "1 minute", "Verbal",
		concentration = "",
		definition = """One creature that you can see within range must succeed on a <i>Constitution saving throw</i>, or it has the <i>Blinded</i> or <i>Deafened</i> condition (your choice) for the duration. At the end of each of its turns, the target repeats the save, ending the spell on itself on a success. <br>
		<b>Using a Higher-Level Spell Slot.</b> You can target one additional creature for each spell slot level above 2.
		""")
	Blur = 				Spell("Blur", 2, "Illusion", "1 Action", "Self", "Concentration, up to 1 minute", "Verbal")
	CordonofArrows = 	Spell("Cordon of Arrows",2, "Transmutation", "1 Action", "5 feet", "8 hours", "Verbal, Somatic, Material")
	Darkvision = 		Spell("Darkvision",2, "Transmutation", "1 Action", "Touch", "8 hours", "Verbal, Somatic, Material")
	DragonsBreath = 	Spell("Dragon's Breath",2, "Transmutation", "1 Bonus Action", "Touch", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	DustDevil = 		Spell("Dust Devil", 2, "Conjuration", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	FindSteed = 		Spell("Find Steed", 2, "Conjuration", "10 Minutes", "30 feet", "Instantaneous", "Verbal, Somatic")
	FindTraps = 		Spell("Find Traps",
		2, 	"Divination", 	"1 Action", 	"120 feet", 	"Instantaneous",
		"Verbal, Somatic")
	FlamingSphere = 	Spell("Flaming Sphere",2, "Conjuration", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	FlockofFamiliars = 	Spell("Flock of Familiars",2, "Conjuration", "1 Minute", "Touch", "Concentration, up to 1 hour", "Verbal, Somatic")
	FortunesFavor = 	Spell("Fortune's Favor",2, "Divination", "1 Minute", "60 feet", "1 hour", "Verbal, Somatic, Material")
	GentleRepose = 		Spell("Gentle Repose",2, "Necromancy", "1 Action", "Touch", "10 days", "Verbal, Somatic, Material")
	GiftOfGab = 		Spell("Gift of Gab",2, "Enchantment", "Reaction", "Self", "Instantaneous", "Verbal, Somatic, Material")
	HealingSpirit = 	Spell("Healing Spirit",2, "Conjuration", "1 Bonus Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic")
	ImmovableObject = 	Spell("Immovable Object",2, "Transmutation", "1 Action", "Touch", "1 hour", "Verbal, Somatic, Material")
	GlowingCoin = 			Spell("Jim's Glowing Coin",2, "Enchantment", "1 Action", "60 feet", "1 minute", "Somatic, Material")
	KineticJaunt = 			Spell("Kinetic Jaunt",2, "Transmutation", "1 Bonus Action", "Self", "Concentration, up to 1 minute", "Somatic")
	LocateAnimalsPlants = 	Spell("Locate Animals or Plants",2, "Divination", "1 Action", "Self", "Instantaneous", "Verbal, Somatic, Material")
	LocateObject = 		Spell("Locate Object",2, "Divination", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	MagicMouth = 		Spell("Magic Mouth",2, "Illusion", "1 Minute", "30 feet", "Until dispelled", "Verbal, Somatic, Material")
	EarthenGrasp = 		Spell("Maximillian's Earthen Grasp",2, "Transmutation", "1 Action", "30 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	AcidArrow = 		Spell("Melf's Acid Arrow",2, "Evocation", "1 Action", "90 feet", "Instantaneous", "Verbal, Somatic, Material")
	MindSpike = 		Spell("Mind Spike",2, "Divination", "1 Action", "60 feet", "Concentration, up to 1 hour", "Somatic")
	MistyStep = 		Spell("Misty Step", 2,  "Conjuration", "1 Bonus Action", "Self", "Instantaneous", "Verbal")
	Moonbeam =		 	Spell("Moonbeam", 2,  "Evocation", "1 Action", "120 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Mischief = 			Spell("Nathair's Mischief",  2, "Illusion", "1 Action", "60 feet", "Concentration, up to 1 minute", "Somatic, Material")
	MagicAura = 		Spell("Nystul's Magic Aura", 2,  "Illusion", "1 Action", "Touch", "24 hours", "Verbal, Somatic, Material")
	PrayerOfHealing = 	Spell("Prayer of Healing",  2, "Evocation", "10 Minutes", "30 feet", "Instantaneous", "Verbal")
	ProtectionFromPoison = 	Spell("Protection from Poison", 2,  "Abjuration", "1 Action", "Touch", "1 hour", "Verbal, Somatic")
	Pyrotechnics = 		Spell("Pyrotechnics", 2,  "Transmutation", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic")
	RayOfEnfeeblement = Spell("Ray of Enfeeblement", 2,  "Necromancy", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic")
	BindingIce = 		Spell("Rime's Binding Ice", 2,  "Evocation", "1 Action", "Self (30-foot cone)", "Instantaneous", "Somatic, Material")
	RopeTrick = 		Spell("Rope Trick", 2,  "Transmutation", "1 Action", "Touch", "1 hour", "Verbal, Somatic, Material")
	ShadowBlade = 		Spell("Shadow Blade", 2,  "Illusion", "1 Bonus Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic")
	Skywrite = 			Spell("Skywrite", 2,  "Transmutation", "1 Action", "Sight", "Concentration, up to 1 day", "Verbal, Somatic")
	SnowballStorm = 	Spell("Snilloc's Snowball Storm", 2,  "Evocation", "1 Action", "90 feet", "Instantaneous", "Verbal, Somatic, Material")
	SpiderClimb = 		Spell("Spider Climb", 2,  "Transmutation", "1 Action", "Touch", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	SpikeGrowth = 		Spell("Spike Growth", 2,  "Transmutation", "1 Action", "150 feet", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	SpiritualWeapon = 	Spell("Spiritual Weapon", 2,  "Evocation", "1 Bonus Action", "60 feet", "1 minute", "Verbal, Somatic")
	SummonBeast = 		Spell("Summon Beast", 2,  "Conjuration", "1 Action", "90 feet", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	MindWhip = 			Spell("Tasha's Mind Whip", 2,  "Enchantment", "1 Action", "90 feet", "1 round", "Verbal")
	VortexWarp = 		Spell("Vortex Warp", 2,  "Conjuration", "1 Action", "90 feet", "Instantaneous", "Verbal, Somatic")
	WardingBond = 		Spell("Warding Bond", 2,  "Abjuration", "1 Action", "Touch", "1 hour", "Verbal, Somatic, Material")
	WardingWind = 		Spell("Warding Wind", 2,  "Evocation", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal")
	WarpSense = 		Spell("Warp Sense", 2,  "Divination", "1 Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Web = 				Spell("Web", 2,  "Conjuration", "1 Action", "60 feet", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	WitherBloom = 	Spell("Wither and Bloom", 2,  "Necromancy", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic, Material")
	Wristpocket = 	Spell("Wristpocket", 2,  "Conjuration", "1 Action", "Self", "Concentration, up to 1 hour", "Somatic")
	AlterSelf = 	Spell("Alter Self", 2, "Transmutation", "1 Action", "Self", "Concentration, up to 1 hour", "Verbal, Somatic")
	Barkskin = 		Spell("Barkskin", 2, "Transmutation", "1 Action", "Touch", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	BeastSense = 	Spell("Beast Sense", 2, "Divination", "1 Action", "Touch", "Concentration, up to 1 hour", "Somatic")
	HeatMetal = 		Spell("Heat Metal", 2, "Transmutation", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Earthbind = 			Spell("Earthbind", 2, "Transmutation", "1 Action", "300 feet", "Concentration, up to 1 minute", "Verbal")
	ContinualFlame = 		Spell("Continual Flame", 2, "Evocation", "1 Action", "Touch", "Until dispelled", "Verbal, Somatic, Material")
	FlameBlade = 			Spell("Flame Blade", 2, "Evocation", "1 Bonus Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	Augury = 				Spell("Augury",2,  "Divination", "1 Minute", "Self", "Instantaneous", "Verbal, Somatic, Material")
	DetectThoughts = 		Spell("Detect Thoughts",2,  "Divination", "1 Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	PassWithoutTrace = 		Spell("Pass Without Trace", 2, "Abjuration", "1 Action", "Self", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	LesserRestoration = 	Spell("Lesser Restoration",	2, "Abjuration", "1 Action", "Touch", "Instantaneous", "Verbal, Somatic")
	AirBubble = 			Spell("Air Bubble", 2, "Conjuration", "1 Action", "60 Feet", "24 hours", "Somatic")
	ArcaneLock = 			Spell("Arcane Lock", 2, "Abjuration", "1 Action", "Touch", "Until dispelled", "Verbal, Somatic, Material")
	Blur = 					Spell("Blur", 2, "Illusion", "1 Action", "Self", "Concentration, up to 1 minute", "Verbal")
	BorrowedKnowledge = 	Spell("Borrowed Knowledge", 2, "Divination", "1 Action", "Self", "1 hour", "Verbal, Somatic, Material")
	CordonofArrows = 		Spell("Cordon of Arrows",2,  "Transmutation", "1 Action", "5 feet", "8 hours", "Verbal, Somatic, Material")
	Darkvision = 			Spell("Darkvision", 2, "Transmutation", "1 Action", "Touch", "8 hours", "Verbal, Somatic, Material")
	DragonsBreath = 		Spell("Dragon's Breath", 2, "Transmutation", "1 Bonus Action", "Touch", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	DustDevil = 			Spell("Dust Devil", 2, "Conjuration", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	FindSteed = 			Spell("Find Steed", 2, "Conjuration", "10 Minutes", "30 feet", "Instantaneous", "Verbal, Somatic")
	FindTraps = 			Spell("Find Traps", 2, "Divination", "1 Action", "120 feet", "Instantaneous", "Verbal, Somatic")
	FlamingSphere = 		Spell("Flaming Sphere", 2, "Conjuration", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	FlockofFamiliars = 		Spell("Flock of Familiars", 2, "Conjuration", "1 Minute", "Touch", "Concentration, up to 1 hour", "Verbal, Somatic")
	FortunesFavor = 		Spell("Fortune's Favor", 2, "Divination", "1 Minute", "60 feet", "1 hour", "Verbal, Somatic, Material")
	GentleRepose = 			Spell("Gentle Repose", 2, "Necromancy", "1 Action", "Touch", "10 days", "Verbal, Somatic, Material")
	GiftOfGab = 			Spell("Gift of Gab", 2, "Enchantment", "Reaction", "Self", "Instantaneous", "Verbal, Somatic, Material")
	HealingSpirit = 		Spell("Healing Spirit", 2, "Conjuration", "1 Bonus Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic")
	ImmovableObject = 		Spell("Immovable Object", 2, "Transmutation", "1 Action", "Touch", "1 hour", "Verbal, Somatic, Material")
	GlowingCoin = 			Spell("Jim's Glowing Coin", 2, "Enchantment", "1 Action", "60 feet", "1 minute", "Somatic, Material")
	KineticJaunt = 			Spell("Kinetic Jaunt", 2, "Transmutation", "1 Bonus Action", "Self", "Concentration, up to 1 minute", "Somatic")
	Levitate = 				Spell("Levitate", 2, "Transmutation", "1 Action", "60 feet", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	LocateAnimalsPlants = 	Spell("Locate Animals or Plants", 2, "Divination", "1 Action", "Self", "Instantaneous", "Verbal, Somatic, Material")
	LocateObject = 			Spell("Locate Object", 2, "Divination", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	MagicMouth = 			Spell("Magic Mouth", 2, "Illusion", "1 Minute", "30 feet", "Until dispelled", "Verbal, Somatic, Material")
	EarthenGrasp = 			Spell("Maximillian's Earthen Grasp", 2, "Transmutation", "1 Action", "30 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	AcidArrow = 			Spell("Melf's Acid Arrow",2,  "Evocation", "1 Action", "90 feet", "Instantaneous", "Verbal, Somatic, Material")
	MindSpike = 			Spell("Mind Spike",2,  "Divination", "1 Action", "60 feet", "Concentration, up to 1 hour", "Somatic")
	MistyStep = 			Spell("Misty Step", 2, "Conjuration", "1 Bonus Action", "Self", "Instantaneous", "Verbal")
	Moonbeam = 				Spell("Moonbeam", 2, "Evocation", "1 Action", "120 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Mischief = 				Spell("Nathair's Mischief", 2, "Illusion", "1 Action", "60 feet", "Concentration, up to 1 minute", "Somatic, Material")
	MagicAura = 			Spell("Nystul's Magic Aura",2,  "Illusion", "1 Action", "Touch", "24 hours", "Verbal, Somatic, Material")
	PrayerOfHealing = 		Spell("Prayer of Healing", 2, "Evocation", "10 Minutes", "30 feet", "Instantaneous", "Verbal")
	ProtectionFromPoison = 	Spell("Protection from Poison", 2, "Abjuration", "1 Action", "Touch", "1 hour", "Verbal, Somatic")
	Pyrotechnics = 			Spell("Pyrotechnics",2,  "Transmutation", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic")
	RayOfEnfeeblement = 	Spell("Ray of Enfeeblement", 2, "Necromancy", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic")
	BindingIce = 			Spell("Rime's Binding Ice", 2, "Evocation", "1 Action", "Self (30-foot cone)", "Instantaneous", "Somatic, Material")
	RopeTrick = 			Spell("Rope Trick", 2, "Transmutation", "1 Action", "Touch", "1 hour", "Verbal, Somatic, Material")
	ShadowBlade = 			Spell("Shadow Blade", 2, "Illusion", "1 Bonus Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic")
	Skywrite = 				Spell("Skywrite", 2,  "Transmutation", "1 Action", "Sight", "Concentration, up to 1 day", "Verbal, Somatic")
	SnowballStorm = 		Spell("Snilloc's Snowball Storm", 2,  "Evocation", "1 Action", "90 feet", "Instantaneous", "Verbal, Somatic, Material")
	SpiderClimb = 			Spell("Spider Climb", 2,  "Transmutation", "1 Action", "Touch", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	SpikeGrowth = 			Spell("Spike Growth",  2, "Transmutation", "1 Action", "150 feet", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	SpiritualWeapon = 		Spell("Spiritual Weapon",  2, "Evocation", "1 Bonus Action", "60 feet", "1 minute", "Verbal, Somatic")
	SummonBeast = 			Spell("Summon Beast", 2,  "Conjuration", "1 Action", "90 feet", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	MindWhip = 				Spell("Tasha's Mind Whip",  2, "Enchantment", "1 Action", "90 feet", "1 round", "Verbal")
	VortexWarp = 			Spell("Vortex Warp",  2, "Conjuration", "1 Action", "90 feet", "Instantaneous", "Verbal, Somatic")
	WardingBond = 			Spell("Warding Bond",  2, "Abjuration", "1 Action", "Touch", "1 hour", "Verbal, Somatic, Material")
	WardingWind = 			Spell("Warding Wind",  2, "Evocation", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal")
	WarpSense = 			Spell("Warp Sense",  2, "Divination", "1 Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Web = 					Spell("Web",  2, "Conjuration", "1 Action", "60 feet", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	Wristpocket = 			Spell("Wristpocket",  2, "Conjuration", "1 Action", "Self", "Concentration, up to 1 hour", "Somatic")
	LesserRestoration = 	Spell("Lesser Restoration", 2,  "Abjuration", "1 Action", "Touch", "Instantaneous", "Verbal, Somatic")
	AlterSelf = 			Spell("Alter Self",  2, "Transmutation", "1 Action", "Self", "Concentration, up to 1 hour", "Verbal, Somatic")
	Barkskin = 				Spell("Barkskin", 2,  "Transmutation", "1 Action", "Touch", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	BeastSense = 			Spell("Beast Sense", 2,  "Divination", "1 Action", "Touch", "Concentration, up to 1 hour", "Somatic")
	HeatMetal = 			Spell("Heat Metal",  2, "Transmutation", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Earthbind = 			Spell("Earthbind", 2,  "Transmutation", "1 Action", "300 feet", "Concentration, up to 1 minute", "Verbal")
	ContinualFlame = 		Spell("Continual Flame", 2,  "Evocation", "1 Action", "Touch", "Until dispelled", "Verbal, Somatic, Material")
	AganazzarScorcher = 	Spell("Aganazzar's Scorcher", 2, "Evocation", "1 Action", "30 Feet", "Instantaneous", "Verbal, Somatic, Material")
	FlameBlade = 			Spell("Flame Blade", 2,  "Evocation", "1 Bonus Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	Augury = 				Spell("Augury", 2,  "Divination", "1 Minute", "Self", "Instantaneous", "Verbal, Somatic, Material")
	DetectThoughts = 		Spell("Detect Thoughts", 2,  "Divination", "1 Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	PassWithoutTrace = 		Spell("Pass Without Trace", 2,  "Abjuration", "1 Action", "Self", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	BorrowedKnowledge = 	Spell("Borrowed Knowledge",	2, "Divination", "1 Action", "Self", "1 hour", "Verbal, Somatic, Material")
	ArcaneVigor           = Spell("Arcane Vigor",            2, "Abjuration",  "Bonus Action", "Self",
								"Concentration, up to 1 hour", "Verbal, Somatic")
	MagicWeapon = 			Spell("Magic Weapon",  2, "Transmutation", "1 Bonus Action", "Touch", "Up to 1 hour", "Verbal, Somatic", "Concentration",
					"""You touch a nonmagical weapon. Until the spell ends, that weapon becomes a magic weapon with a <i>+1 bonus to attack rolls and damage rolls</i>.
					<br>The spell ends early if you cast it again.
					<br><b>Using a Higher-Level Spell Slot.</b> The bonus increases to +2 with a level 3-5 spell slot.
					The bonus increases to +3 with a level 6+ spell slot.""")
	CloudofDaggers =	Spell("Cloud of Daggers",2,  "Conjuration", "1 Action", "60 feet", "up to 1 minute", "Verbal, Somatic, Material [a sliver of glass]", "Concentration",
		"""You conjure spinning daggers in a 5-foot Cube centered on a point within range.
		Each creature in that area takes <b>4d4 Slashing damage</b>.
		A creature also takes this damage if it enters the Cube or ends its turn there or if the Cube moves into its space.
		A creature takes this damage only once per turn.
		<br>
		On your later turns, you can take a <i>Magic action</i> to teleport the Cube up to <i>30 feet</i>.
		<br><b>Using a Higher-Level Spell Slot.</b> The damage increases by <b>2d4</b> for each spell slot level above 2.""")
	Levitate =  Spell("Levitate",2, "Transmutation", "1 Action", "60 feet", "up to 10 minutes", "Verbal, Somatic, Material", "Concentration",
		"""
		One creature or loose object of your choice that you can see within range rises vertically up to 20 feet and remains suspended there for the duration. The spell can levitate an object that weighs up to 500 pounds. An unwilling creature that succeeds on a Constitution saving throw is unaffected. <br>
		The target can move only by pushing or pulling against a fixed object or surface within reach (such as a wall or a ceiling), which allows it to move as if it were climbing. You can change the target's altitude by up to 20 feet in either direction on your turn. If you are the target, you can move up or down as part of your move. Otherwise, you can take a Magic action to move the target, which must remain within the spell's range.<br>
		When the spell ends, the target floats gently to the ground if it is still aloft.
		""")
	Aid = Spell("Aid",  2, "Abjuration", "1 Action", "30 Feet", "8 hours", "Verbal, Somatic, Material (a strip of white cloth)", "",
		"""Choose up to three creatures within range. Each target's Hit Point maximum and current Hit Points increase by 5 for the duration. <br>
		<b>Using a Higher-Level Spell Slot.</b> Each target's Hit Points increase by 5 for each spell slot level above 2.
		""")
	EnlargeReduce = Spell("Enlarge/Reduce",
		level=2,
		school="Transmutation",
		casting_time="Action",
		ranges = "30 feet",
		components = "Verbal, Somatic, Material (a pinch of powdered iron)",
		concentration = "Concentration",
		duration = "1 minute",
		definition = """
			You spray a 15-foot cone of spectral cards. Each creature in that area must make a Dexterity saving throw. On a failed save, a creature takes 2d10 force damage and has the blinded condition until the end of its next turn. On a successful save, a creature takes half as much damage only.
			<br>
			<b>At Higher Levels.</b> When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d10 for each slot level above 2nd.
			""")

	SprayOfCards = 			Spell("Spray Of Cards",
		level=2,
		school="Conjuration",
		casting_time="Action",
		ranges = "Self (15-foot cone)",
		duration = "Instantaneous",
		components = "Verbal, Somatic, Material (a deck of cards)",
		concentration = "",
		definition = """
			You spray a 15-foot cone of spectral cards. Each creature in that area must make a Dexterity saving throw. On a failed save, a creature takes 2d10 force damage and has the blinded condition until the end of its next turn. On a successful save, a creature takes half as much damage only.
			<br>
			<b>At Higher Levels.</b> When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d10 for each slot level above 2nd.
			""")
	MirrorImage = 			Spell("Mirror Image",
		level=2,
		school="Illusion",
		casting_time="Action",
		ranges = "Self",
		duration = "1 minute",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
			Three illusory duplicates of yourself appear in your space. Until the spell ends, the duplicates move with you and mimic your actions, shifting position so it's impossible to track which image is real.
			<br>
			Each time a creature hits you with an attack roll during the spell's duration, roll a d6 for each of your remaining duplicates. If any of the d6s rolls a 3 or higher, one of the duplicates is hit instead of you, and the duplicate is destroyed. The duplicates otherwise ignore all other damage and effects. The spell ends when all three duplicates are destroyed.
			<br>
			A creature is unaffected by this spell if it has the Blinded condition, Blindsight, or Truesight.
			""")
	Darkness = 		Spell("Darkness",
			level=2,
			school="Evocation",
			casting_time="Action",
			ranges = "60 feet",
			duration = "10 minutes",
			components = "Verbal, Material (bat fur and a piece of coal)",
			concentration = "Concentration",
			definition = """
For the duration, magical Darkness spreads from a point within range and fills a 15-foot-radius Sphere. Darkvision can't see through it, and nonmagical light can't illuminate it.
<br>
Alternatively, you cast the spell on an object that isn't being worn or carried, causing the Darkness to fill a 15-foot Emanation originating from that object. Covering that object with something opaque, such as a bowl or helm, blocks the Darkness.
<br>
If any of this spell's area overlaps with an area of Bright Light or Dim Light created by a spell of level 2 or lower, that other spell is dispelled.
				""")
	AnimalMessenger = 		Spell("Animal Messenger",
		level=2,
		school="Enchantment",
		casting_time="Action",
		ranges = "30 feet",
		duration = "24 hours",
		components = "Verbal, Somatic, Material (a morsel of food)",
		concentration = "",
		definition = """
A Tiny Beast of your choice that you can see within range must succeed on a Charisma saving throw, or it attempts to deliver a message for you (if the target's Challenge Rating isn't 0, it automatically succeeds). You specify a location you have visited and a recipient who matches a general description, such as "a person dressed in the uniform of the town guard" or "a red-haired dwarf wearing a pointed hat." You also communicate a message of up to twenty-five words. The Beast travels for the duration toward the specified location, covering about 25 miles per 24 hours or 50 miles if the Beast can fly.
<br>
When the Beast arrives, it delivers your message to the creature that you described, mimicking your communication. If the Beast doesn't reach its destination before the spell ends, the message is lost, and the Beast returns to where you cast the spell.
<br>
Using a Higher-Level Spell Slot. The spell's duration increases by 48 hours for each spell slot level above 2.
			""")
	GustOfWind = 			Spell("Gust of Wind", 2,
		school="Evocation",
		casting_time="Action",
		ranges = "Self",
		duration = "1 minute",
		components = "Verbal, Somatic, Material (a legume seed)",
		concentration = "Concentration",
		definition = """
A Line of strong wind 60 feet long and 10 feet wide blasts from you in a direction you choose for the duration. Each creature in the Line must succeed on a Strength saving throw or be pushed 15 feet away from you in a direction following the Line. A creature that ends its turn in the Line must make the same save.
<br>
Any creature in the Line must spend 2 feet of movement for every 1 foot it moves when moving closer to you.
<br>
The gust disperses gas or vapor, and it extinguishes candles and similar unprotected flames in the area. It causes protected flames, such as those of lanterns, to dance wildly and has a 50 percent chance to extinguish them.
<br>
As a Bonus Action on your later turns, you can change the direction in which the Line blasts from you.
			""")
	Invisibility = 			Spell("Invisibility", 2,
		school="Illusion",
		casting_time="Action",
		ranges = "Touch",
		duration = "1 hour",
		components = "Verbal, Somatic, Material (an eyelash in gum arabic)",
		concentration = "Concentration",
		definition = """
A creature you touch has the Invisible condition until the spell ends. The spell ends early immediately after the target makes an attack roll, deals damage, or casts a spell.
<br>
<b>Using a Higher-Level Spell Slot.</b> You can target one additional creature for each spell slot level above 2.
			""")
	PhantasmalForce = 		Spell("Phantasmal Force",2,
		school="Illusion",
		casting_time="Action",
		ranges = "60 feet",
		duration = "1 minute",
		components = "Verbal, Somatic, Material (a bit of fleece)",
		concentration = "Concentration",
		definition = """
You attempt to craft an illusion in the mind of a creature you can see within range. The target makes an Intelligence saving throw. On a failed save, you create a phantasmal object, creature, or other phenomenon that is no larger than a 10-foot Cube and that is perceivable only to the target for the duration. The phantasm includes sound, temperature, and other stimuli.
<br>
The target can take a Study action to examine the phantasm with an Intelligence (Investigation) check against your spell save DC. If the check succeeds, the target realizes that the phantasm is an illusion, and the spell ends.
<br>
While affected by the spell, the target treats the phantasm as if it were real and rationalizes any illogical outcomes from interacting with it. For example, if the target steps through a phantasmal bridge and survives the fall, it believes the bridge exists and something else caused it to fall.
<br>
An affected target can even take damage from the illusion if the phantasm represents a dangerous creature or hazard. On each of your turns, such a phantasm can deal 2d8 Psychic damage to the target if it is in the phantasm's area or within 5 feet of the phantasm. The target perceives the damage as a type appropriate to the illusion.
		""")
	SeeInvisibility = 		Spell("See Invisibility", 2,
		school="Divination",
		casting_time="Action",
		ranges = "Self",
		duration = "1 hour",
		components = "Verbal, Somatic, Material (a pinch of talc)",
		concentration = "",
		definition = """
	For the duration, you see creatures and objects that have the Invisible condition as if they were visible, and you can see into the Ethereal Plane. Creatures and objects there appear ghostly.
	""")
	ScorchingRay = 			Spell("Scorching Ray", 2,
		school="Evocation",
		casting_time="Action",
		ranges = "120 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
You hurl three fiery rays. You can hurl them at one target within range or at several. Make a ranged spell attack for each ray. On a hit, the target takes 2d6 Fire damage.
<br>
Using a Higher-Level Spell Slot. You create one additional ray for each spell slot level above 2.
		""")
	Enthrall = 				Spell("Enthrall", 2,
		school="Enchantment",
		casting_time="Action",
		ranges = "60 feet",
		components = "Verbal, Somatic",
		duration = "1 minute",
		concentration = "",
		definition = """
		You weave a distracting string of words, causing creatures of your choice that you can see within range to make a Wisdom saving throw. Any creature you or your companions are fighting automatically succeeds on this save. On a failed save, a target has a -10 penalty to Wisdom (Perception) checks and Passive Perception until the spell ends.
		""")
	HoldPerson = Spell("Hold Person",
		level=2,
		school="Enchantment",
		casting_time="Action",
		ranges = "60 feet",
		components = "Verbal, Somatic, Material (a straight piece of iron)",
		duration = "1 minute",
		concentration = "Concentration",
		definition = """
		Choose a Humanoid that you can see within range. The target must succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, the target repeats the save, ending the spell on itself on a success.
		""")
	CrownofMadness = 		Spell("Crown of Madness",
			level=2,
			school="Enchantment",
			casting_time="Action",
			ranges = "120 feet",
			components = "Verbal, Somatic",
			concentration = "Concentration",
			duration = "1 minute",
			definition = """
			One creature that you can see within range must succeed on a Wisdom saving throw or have the Charmed condition for the duration. The creature succeeds automatically if it isn't Humanoid.
			<br>
			A spectral crown appears on the Charmed target's head, and it must use its action before moving on each of its turns to make a melee attack against a creature other than itself that you mentally choose. The target can act normally on its turn if you choose no creature or if no creature is within its reach. The target repeats the save at the end of each of its turns, ending the spell on itself on a success.
			<br>
			On your later turns, you must take the Magic action to maintain control of the target, or the spell ends.
			""")
	Silence = Spell("Silence",
		level=2,
		school="Illusion",
		casting_time="Action or Ritual",
		ranges = "120 feet",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		duration = "10 minutes",
		definition = """
			For the duration, no sound can be created within or pass through a 20-foot-radius Sphere centered on a point you choose within range. Any creature or object entirely inside the Sphere has Immunity to Thunder damage, and creatures have the Deafened condition while entirely inside it. Casting a spell that includes a Verbal component is impossible there.
			""")
	Suggestion = Spell("Suggestion",
		level=2,
		school="Enchantment",
		casting_time="Action",
		ranges = "30 feet",
		components = "Verbal, Material (a drop of honey)",
		concentration = "Concentration",
		duration = "8 hours",
		definition = """
		You suggest a course of activity—described in no more than 25 words—to one creature you can see within range that can hear and understand you. The suggestion must sound achievable and not involve anything that would obviously deal damage to the target or its allies. For example, you could say, "Fetch the key to the cult's treasure vault, and give the key to me." Or you could say, "Stop fighting, leave this library peacefully, and don't return."
		<br>
		The target must succeed on a Wisdom saving throw or have the Charmed condition for the duration or until you or your allies deal damage to the target. The Charmed target pursues the suggestion to the best of its ability. The suggested activity can continue for the entire duration, but if the suggested activity can be completed in a shorter time, the spell ends for the target upon completing it.
		""")
	Knock = Spell("Knock",
		level=2,
		school="Transmutation",
		casting_time="Action",
		ranges = "60 feet",
		components = "Verbal",
		concentration = "Concentration",
		duration = "Instantaneous",
		definition = """
		Choose an object that you can see within range. The object can be a door, a box, a chest, a set of manacles, a padlock, or another object that contains a mundane or magical means that prevents access.
		<br>
		A target that is held shut by a mundane lock or that is stuck or barred becomes unlocked, unstuck, or unbarred. If the object has multiple locks, only one of them is unlocked.
		<br>
		If the target is held shut by Arcane Lock, that spell is suppressed for 10 minutes, during which time the target can be opened and closed.
		<br>
		When you cast the spell, a loud knock, audible up to 300 feet away, emanates from the target.
		""")
	ZoneOfTruth = Spell("Zone of Truth",
		level=2,
		school="Enchantment",
		casting_time="Action",
		ranges = "60 feet",
		components = "Verbal, Somatic",
		concentration = "",
		duration = "10 minutes",
		definition = """
			You create a magical zone that guards against deception in a 15-foot-radius Sphere centered on a point within range. Until the spell ends, a creature that enters the spell's area for the first time on a turn or starts its turn there makes a Charisma saving throw. On a failed save, a creature can't speak a deliberate lie while in the radius. You know whether a creature succeeds or fails on this save.
			<br>
			An affected creature is aware of the spell and can avoid answering questions to which it would normally respond with a lie. Such a creature can be evasive yet must be truthful.
			""")
	Shatter = Spell("Shatter",
		level=2,
		school="Evocation",
		casting_time="Action",
		ranges = "60 feet",
		components = "Verbal, Somatic, Material(a chip of mica)",
		concentration = "",
		duration = "Instantaneous",
		definition = """
			A loud noise erupts from a point of your choice within range. Each creature in a 10-foot-radius Sphere centered there makes a Constitution saving throw, taking 3d8 Thunder damage on a failed save or half as much damage on a successful one. A Construct has Disadvantage on the save.
			<br>
			A nonmagical object that isn't being worn or carried also takes the damage if it's in the spell's area.
			<br>
			<b>Using a Higher-Level Spell Slot.</b> The damage increases by 1d8 for each spell slot level above 2.
			""")
	CalmEmotions = Spell("Calm Emotions",
		level=2,
		school="Enchantment",
		casting_time="Action",
		ranges = "60 feet",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		duration = "1 minute",
		definition = """
Each Humanoid in a 20-foot-radius Sphere centered on a point you choose within range must succeed on a Charisma saving throw or be affected by one of the following effects (choose for each creature):
<ul style="list-style-type: '🩶'; text-align: left; ">
<li>	The creature has Immunity to the Charmed and Frightened conditions until the spell ends. If the creature was already Charmed or Frightened, those conditions are suppressed for the duration.
<li>	The creature becomes Indifferent about creatures of your choice that it's Hostile toward. This indifference ends if the target takes damage or witnesses its allies taking damage. When the spell ends, the creature's attitude returns to normal.
</ul>
""")
	EnhanceAbility = Spell("Enhance Ability",
		level=2,
		school="Transmutation",
		casting_time="Action",
		ranges = "Touch",
		components = "Verbal, Somatic, Material (fur or a feather)",
		concentration = "Concentration",
		duration = "1 hour",
		definition = """
You touch a creature and choose Strength, Dexterity, Intelligence, Wisdom, or Charisma. For the duration, the target has Advantage on ability checks using the chosen ability.
<br>
Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 2. You can choose a different ability for each target.
""")
	BrandingSmite = Spell("Branding Smite",
		level=2,
		school="Evocation",
		casting_time="Bonus action",
		ranges = "Self",
		components = "Verbal",
		concentration = "Concentration",
		duration = "1 minute",
		definition = """
The next time you hit a creature with a weapon attack before this spell ends, the weapon gleams with astral radiance as you strike. The attack deals an extra 2d6 radiant damage to the target, which becomes visible if it's invisible, and the target sheds dim light in a 5-foot radius and can't become invisible until the spell ends.
<br>
At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, the extra damage increases by 1d6 for each slot level above 2nd.
""")

GustofWind = GustOfWind
AganazzarsScorcher = AganazzarScorcher
MaximiliansEarthenGrasp = EarthenGrasp
RayofEnfeeblement = RayOfEnfeeblement

# Define third-level spells
LEVEL3 = True
if LEVEL3:
	SpiritGuardians = spell_from_data("Spirit Guardians")
	ProtectionfromEnergy = spell_from_data("Protection from Energy")
	DispelMagic = spell_from_data("Dispel Magic")
	Revivify = spell_from_data("Revivify")
	CrusadersMantle = spell_from_data("Crusader's Mantle")
	TinyHut = spell_from_data("Leomund’s Tiny Hut")
	MajorImage = spell_from_data("Major Image")
	EnemiesAbound = spell_from_data("Enemies Abound")
	GaseousForm = spell_from_data("Gaseous Form")

	BlindingSmite = spell_from_data("Blinding Smite")
	ConjureBarrage = spell_from_data("Conjure Barrage")
	EruptingEarth = spell_from_data("Erupting Earth")
	FastFriends = spell_from_data("Fast Friends")
	FeignDeath = spell_from_data("Feign Death")
	FlameArrows = spell_from_data("Flame Arrows")
	FreedomWaves = spell_from_data("Freedom of the Waves (HB)")
	GaldersTower = spell_from_data("Galder's Tower")
	GlyphWarding = spell_from_data("Glyph of Warding")
	HungerHadar = spell_from_data("Hunger Of Hadar")
	InciteGreed = spell_from_data("Incite Greed")
	LifeTransference = spell_from_data("Life Transference")
	LightningArrow = spell_from_data("Lightning Arrow")
	LightningBolt = spell_from_data("Lightning Bolt")
	MagicCircle = spell_from_data("Magic Circle")
	MeldIntoStone = spell_from_data("Meld into Stone")
	MelfsMinuteMeteors = spell_from_data("Melf's Minute Meteors")
	MotivationalSpeech = spell_from_data("Motivational Speech")
	PulseWave = spell_from_data("Pulse Wave")
	SleetStorm = 	Spell("Sleet Storm", 3,
					school="Conjuration",
					casting_time="Action",
					ranges = "150 feet",
					duration = "Up to 1 minute",
					components = "Verbal, Somatic, Material (a miniature umbrella)",
					concentration = "Concentration",
					definition = """Until the spell ends, sleet falls in a 40-foot-tall, 20-foot-radius Cylinder centered on a point you choose within range. The area is Heavily Obscured, and exposed flames in the area are doused. <br>
					Ground in the Cylinder is Difficult Terrain. When a creature enters the Cylinder for the first time on a turn or starts its turn there, it must succeed on a Dexterity saving throw or have the Prone condition and lose Concentration.""")
	SpiritShroud = spell_from_data("Spirit Shroud")
	SummonFey = spell_from_data("Summon Fey")
	SummonUndead = spell_from_data("Summon Undead")
	TidalWave = spell_from_data("Tidal Wave")
	TinyServant = spell_from_data("Tiny Servant")
	VampiricTouch = spell_from_data("Vampiric Touch")
	WallSand = spell_from_data("Wall of Sand")
	WallWater = spell_from_data("Wall of Water")
	AnimateDead = spell_from_data("Animate Dead")
	AshardalonStride = spell_from_data("Ashardalon's Stride")
	Blink = Spell("Blink", 3,
			school="Transmutation",
			casting_time="Action",
			ranges = "Self",
			duration = "1 minute",
			components = "Verbal, Somatic",
			concentration = "",
			definition = """Roll <i>1d6</i> at the end of each of your turns for the duration. On a roll of <i>4-6</i>, you vanish from your current plane of existence and appear in the <i>Ethereal Plane</i> (the spell ends instantly if you are already on that plane). While on the <i>Ethereal Plane</i>, you can perceive the plane you left, which is cast in shades of gray, but you can't see anything there more than <i>60 feet</i> away. You can affect and be affected only by other creatures on the <i>Ethereal Plane</i>, and creatures on the other plane can't perceive you unless they have a special ability that lets them perceive things on the <i>Ethereal Plane</i>. <br> You return to the other plane at the start of your next turn and when the spell ends if you are on the Ethereal Plane. You return to an unoccupied space of your choice that you can see within <i>10 feet</i> of the space you left. If no unoccupied space is available within that range, you appear in the nearest unoccupied space.""")
	BeaconHope = spell_from_data("Beacon of Hope")
	Clairvoyance = spell_from_data("Clairvoyance")
	AuraVitality = spell_from_data("Aura of Vitality")
	BestowCurse = spell_from_data("Bestow Curse")
	Catnap = spell_from_data("Catnap")
	ConjureAnimals = spell_from_data("Conjure Animals")
	WindWall = spell_from_data("Wind Wall")
	WaterWalk = spell_from_data("Water Walk")
	WaterBreathing = spell_from_data("Water Breathing")
	Sending = spell_from_data("Sending")
	Sending = spell_from_data("Sending")
	CharmMonster = spell_from_data("Charm Monster")
	ElementalWeapon = spell_from_data("Elemental Weapon")
	SpiritGuardians = spell_from_data("Spirit Guardians")
	ProtectionfromEnergy = spell_from_data("Protection from Energy")
	Haste = 	Spell("Haste", 3,
			school="Transmutation",
			casting_time="Action",
			ranges = "30 feet",
			duration = "Up to 1 minute",
			components = "Verbal, Somatic, Material (a shaving of licorice root)",
			concentration = "Concentration",
			definition = """Choose a willing creature that you can see within range.
			Until the spell ends, the target's <b>Speed is doubled</b>, it gains a <b>+2 bonus to Armor Class</b>, it has <b>Advantage on Dexterity saving throws</b>, and it gains an <b>additional action</b> on each of its turns. That action can be used to take only the <b>Attack (one attack only), Dash, Disengage, Hide, or Utilize action</b>.
			<br>
			When the spell ends, the target is <b>Incapacitated</b> and has a <b>Speed of 0</b> until the end of its next turn, as a wave of lethargy washes over it.""")
	Revivify = spell_from_data("Revivify")
	CrusadersMantle = spell_from_data("Crusader's Mantle")
	TinyHut = spell_from_data("Leomund’s Tiny Hut")
	MajorImage = spell_from_data("Major Image")
	EnemiesAbound = spell_from_data("Enemies Abound")
	GaseousForm = spell_from_data("Gaseous Form")

	BlindingSmite = spell_from_data("Blinding Smite")
	ConjureBarrage = spell_from_data("Conjure Barrage")
	EruptingEarth = spell_from_data("Erupting Earth")
	FastFriends = spell_from_data("Fast Friends")
	FeignDeath = spell_from_data("Feign Death")
	FlameArrows = spell_from_data("Flame Arrows")
	FreedomWaves = spell_from_data("Freedom of the Waves (HB)")
	GaldersTower = spell_from_data("Galder's Tower")
	GlyphWarding = spell_from_data("Glyph of Warding")
	HungerHadar = spell_from_data("Hunger Of Hadar")
	InciteGreed = spell_from_data("Incite Greed")
	LifeTransference = spell_from_data("Life Transference")
	LightningArrow = spell_from_data("Lightning Arrow")
	LightningBolt = spell_from_data("Lightning Bolt")
	MagicCircle = spell_from_data("Magic Circle")
	MeldIntoStone = spell_from_data("Meld into Stone")
	MelfsMinuteMeteors = spell_from_data("Melf's Minute Meteors")
	MotivationalSpeech = spell_from_data("Motivational Speech")
	PulseWave = spell_from_data("Pulse Wave")
	SpiritShroud = spell_from_data("Spirit Shroud")
	SummonFey = spell_from_data("Summon Fey")
	SummonUndead = spell_from_data("Summon Undead")
	TidalWave = spell_from_data("Tidal Wave")
	TinyServant = spell_from_data("Tiny Servant")
	WallSand = spell_from_data("Wall of Sand")
	WallWater = spell_from_data("Wall of Water")
	AnimateDead = spell_from_data("Animate Dead")
	Antagonize = spell_from_data("Antagonize")
	AshardalonStride = spell_from_data("Ashardalon's Stride")
	BeaconHope = spell_from_data("Beacon of Hope")
	Clairvoyance = spell_from_data("Clairvoyance")
	AuraVitality = spell_from_data("Aura of Vitality")
	BestowCurse = spell_from_data("Bestow Curse")
	Catnap = spell_from_data("Catnap")
	ConjureAnimals = spell_from_data("Conjure Animals")
	Daylight = spell_from_data("Daylight")
	WindWall = spell_from_data("Wind Wall")
	WaterWalk = spell_from_data("Water Walk")
	WaterBreathing = spell_from_data("Water Breathing")
	DispelMagic = spell_from_data("Dispel Magic")
	CharmMonster = spell_from_data("Charm Monster")
	ElementalWeapon = spell_from_data("Elemental Weapon")
	PhantomSteed = Spell("Phantom Steed", 3,
			school="Illusion",
			casting_time="1 minute or Ritual",
			ranges = "30 feet",
			duration = "1 hour",
			components = "Verbal, Somatic",
			concentration = "",
			definition = """A Large, quasi-real, horselike creature appears on
			the ground in an unoccupied space of your choice within range. You
			decide the creature's appearance, and it is equipped with a saddle,
			bit, and bridle. Any of the equipment created by the spell vanishes
			in a puff of smoke if it is carried more than 10 feet away from the
			steed. <br>
			For the duration, you or a creature you choose can ride the steed.
			The steed uses the Riding Horse stat block, except it has a Speed
			of 100 feet and can travel 13 miles in an hour. When the spell ends,
			the steed gradually fades, giving the rider 1 minute to dismount.
			The spell ends early if the steed takes any damage.""")
	Antagonize = Spell("Antagonize", 3,
			school="Enchantment",
			casting_time="Action",
			ranges = "30 feet",
			duration = "Instantaneous",
			components = "Verbal, Somatic, Material (a playing card depicting a rogue)",
			concentration = "",
			definition = """
			You whisper magical words that antagonize one creature of your
			choice within range.
			The target must make a Wisdom saving throw.
			On a failed save, the target takes 4d4 psychic damage and must
			immediately use its reaction to make a melee attack against another
			creature of your choice that you can see.
			If the target can't make this attack (for example,
			because there is no one within its reach or because its reaction is
			unavailable), the target instead has disadvantage on the next attack
			roll it makes before the start of your next turn.
			On a successful save, the target takes half as much damage only.

			<b>At Higher Levels.</b>
			When you cast this spell using a spell slot of 4th level or higher,
			the damage increases by 1d4 for each slot level above 3rd.
			""")
	Fly = Spell("Fly", 3,
			school="Transmutation",
			casting_time="Action",
			ranges = "Touch",
			duration = "10 minutes",
			components = "Verbal, Somatic, Material (a feather)",
			concentration = "Concentration",
			definition = """
				You touch a willing creature. For the duration, the target gains a Fly Speed of 60 feet and can hover. When the spell ends, the target falls if it is still aloft unless it can stop the fall.
				<br>
				Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 3.
				""")
	SummonLesserDemons = Spell("Summon Lesser Demons", 3,
			school="Conjuration",
			casting_time="Action",
			ranges = "60 feet",
			duration = "1 hour",
			components = "Verbal, Somatic, Material (a vial of blood from a humanoid killed within the past 24 hours)",
			concentration = "Concentration",
			definition = """
				You utter foul words, summoning demons from the chaos of the Abyss. Roll on the following table to determine what appears.
				 <ul style="list-style-type: '🜏'; text-align: left; ">
				 <li>d6	    Demons Summoned
				<li> 1-2	Two demons of challenge rating 1 or lower
				<li> 3-4	Four demons of challenge rating 1/2 or lower
				<li> 5-6	Eight demons of challenge rating 1/4 or lower
				 </ul>

				The DM chooses the demons, such as manes or dretches, and you choose the unoccupied spaces you can see within range where they appear. A summoned demon disappears when it drops to 0 hit points or when the spell ends.

				The demons are hostile to all creatures, including you. Roll initiative for the summoned demons as a group, which has its own turns. The demons pursue and attack the nearest non-demons to the best of their ability.

				As part of casting the spell, you can form a circle on the ground with the blood used as a material component. The circle is large enough to encompass your space. While the spell lasts, the summoned demons can't cross the circle or harm it, and they can't target anyone within it. Using the material component in this manner consumes it when the spell ends.

				At Higher Levels. When you cast this spell using a spell slot of 6th or 7th level, you summon twice as many demons. If you cast it using a spell slot of 8th or 9th level, you summon three times as many demons.
				""")
	AuraofVitality = Spell("Aura of Vitality", 3,
			school="Abjuration",
			casting_time="Action",
			ranges = "Self",
			duration = "Up to 1 minute",
			components = "Verbal",
			concentration = "Concentration",
			definition = """
			An aura radiates from you in a 30-foot Emanation for the duration.
			When you create the aura and at the start of each of your turns
			while it persists, you can restore 2d6 Hit Points to one creature
			in it.
			""")
	SpeakWithPlants = Spell("Speak with Plants", 3,
			school="Transmutation",
			casting_time="Action",
			ranges = "Self",
			duration = "10 minutes",
			components = "Verbal, Somatic",
			concentration = "Concentration",
			definition = """
You imbue plants in an immobile 30-foot Emanation with limited sentience and animation, giving them the ability to communicate with you and follow your simple commands. You can question plants about events in the spell's area within the past day, gaining information about creatures that have passed, weather, and other circumstances.
<br>
You can also turn Difficult Terrain caused by plant growth (such as thickets and undergrowth) into ordinary terrain that lasts for the duration. Or you can turn ordinary terrain where plants are present into Difficult Terrain that lasts for the duration.
<br>
The spell doesn't enable plants to uproot themselves and move about, but they can move their branches, tendrils, and stalks for you.
<br>
If a Plant creature is in the area, you can communicate with it as if you shared a common language.
			""")
	FountofMoonlight = Spell("Fount of Moonlight", 3,
			school="Evocation",
			casting_time="Action",
			ranges = "Self",
			duration = "10 minutes",
			components = "Verbal, Somatic",
			concentration = "Concentration",
			definition = """
A cool light wreathes your body for the duration, emitting Bright Light in a 20-foot radius and Dim Light for an additional 20 feet.
<br>
Until the spell ends, you have Resistance to Radiant damage, and your melee attacks deal an extra 2d6 Radiant damage on a hit.
<br>
In addition, immediately after you take damage from a creature you can see within 60 feet of yourself, you can take a Reaction to force the creature to make a Constitution saving throw. On a failed save, the creature has the Blinded condition until the end of your next turn.
			""")
	Fireball = Spell("Fireball", 3,
		school="Evocation",
		casting_time="Action",
		ranges = "150 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic, Material (a ball of bat guano and sulfur)",
		concentration = "",
		definition = """
		A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 8d6 Fire damage on a failed save or half as much damage on a successful one.
		<br>
		Flammable objects in the area that aren't being worn or carried start burning.
		<br>
		<b>Using a Higher-Level Spell Slot.</b> The damage increases by 1d6 for each spell slot level above 3.
				""")
	Slow = Spell("Slow", 3,
		school="Transmutation",
		casting_time="Action",
		ranges = "120 feet",
		duration = "1 minute",
		components = "Verbal, Somatic, Material (a drop of molasses)",
		concentration = "Concentration",
		definition = """
		You alter time around up to six creatures of your choice in a 40-foot Cube within range. Each target must succeed on a Wisdom saving throw or be affected by this spell for the duration.
		<br>
		An affected target's Speed is halved, it takes a -2 penalty to AC and Dexterity saving throws, and it can't take Reactions. On its turns, it can take either an action or a Bonus Action, not both, and it can make only one attack if it takes the Attack action. If it casts a spell with a Somatic component, there is a 25 percent chance the spell fails as a result of the target making the spell's gestures too slowly.
		<br>
		An affected target repeats the save at the end of each of its turns, ending the spell on itself on a success.
				""")
	RemoveCurse = Spell("Remove Curse", 3,
	school="Abjuration",
	casting_time="Action",
	ranges = "Touch",
	duration = "Instantaneous",
	components = "Verbal, Somatic",
	concentration = "",
	definition = """
At your touch, all curses affecting one creature or object end. If the object is a cursed magic item, its curse remains, but the spell breaks its owner's Attunement to the object so it can be removed or discarded.
				""")
	Fear = 	Spell("Fear", 3,
			school="Illusion",
			casting_time="Action",
			ranges = "Self",
			duration = "1 minute",
			components = "Verbal, Somatic, Material (a white feather)",
			concentration = "Concentration",
			definition = """
Each creature in a 30-foot Cone must succeed on a Wisdom saving throw or drop whatever it is holding and have the Frightened condition for the duration.
<br>
A Frightened creature takes the Dash action and moves away from you by the safest route on each of its turns unless there is nowhere to move. If the creature ends its turn in a space where it doesn't have line of sight to you, the creature makes a Wisdom saving throw. On a successful save, the spell ends on that creature.
				""")
	Tongues = 	Spell("Tongues", 3,
				school="Divination",
				casting_time="Action",
				ranges = "Touch",
				components = "Verbal, Material (a miniature ziggurat)",
				duration = "1 hour",
				concentration = "",
				definition = """
This spell grants the creature you touch the ability to understand any spoken or signed language that it hears or sees. Moreover, when the target communicates by speaking or signing, any creature that knows at least one language can understand it if that creature can hear the speech or see the signing.
					""")
	StinkingCloud = 		Spell("Stinking Cloud", 3,
				school="Conjuration",
				casting_time="Action",
				ranges = "90 feet",
				components = "Verbal, Somatic, Material (a rotten egg)",
				duration = "1 minute",
				concentration = "Concentration",
				definition = """
You create a 20-foot-radius Sphere of yellow, nauseating gas centered on a point within range. The cloud is Heavily Obscured. The cloud lingers in the air for the duration or until a strong wind (such as the one created by Gust of Wind) disperses it.
<br>
Each creature that starts its turn in the Sphere must succeed on a Constitution saving throw or have the Poisoned condition until the end of the current turn. While Poisoned in this way, the creature can't take an action or a Bonus Action.
					""")
	IntellectFortress = Spell("Intellect Fortress", 3,
				school="Abjuration",
				casting_time="Action",
				ranges = "30 feet",
				components = "Verbal",
				duration = "1 hour",
				concentration = "Concentration",
				definition = """
For the duration, you or one willing creature you can see within range has resistance to psychic damage, as well as advantage on Intelligence, Wisdom, and Charisma saving throws.
<br>
At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, you can target one additional creature for each slot level above 3rd. The creatures must be within 30 feet of each other when you target them.
					""")
	SummonShadowspawn = Spell("Summon Shadowspawn", 3,
				school="Conjuration",
				casting_time="Action",
				ranges = "90 feet",
				components = "Verbal, Somatic, Material (tears inside a gem worth at least 300 gp)",
				duration = "1 hour",
				concentration = "Concentration",
				definition = """
You call forth a shadowy spirit. It manifests in an unoccupied space that you can see within range. This corporeal form uses the Shadow Spirit stat block. When you cast the spell, choose an emotion: Fury, Despair, or Fear. The creature resembles a misshapen biped marked by the chosen emotion, which determines certain traits in its stat block. The creature disappears when it drops to 0 hit points or when the spell ends.
<br>
The creature is an ally to you and your companions. In combat, the creature shares your initiative count, but it takes its turn immediately after yours. It obeys your verbal commands (no action required by you). If you don't issue any, it takes the Dodge action and uses its move to avoid danger.
<br>
At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, use the higher level wherever the spell's level appears in the stat block.
					""")
	CreateFoodWater = Spell("Create Food and Water", 3,
		school="Conjuration",
		casting_time="Action",
		ranges = "30 feet",
		components = "Verbal, Somatic",
		duration = "Instantaneous",
		concentration = "",
		definition = """
			You create 45 pounds of food and 30 gallons of fresh water on the ground or in containers within range—both useful in fending off the hazards of malnutrition and dehydration. The food is bland but nourishing and looks like a food of your choice, and the water is clean. The food spoils after 24 hours if uneaten.
			""")
	CallLightning = Spell("Call Lightning", 3,
		school="Conjuration",
		casting_time="Action",
		ranges = "120 feet",
		components = "Verbal, Somatic",
		duration = "10 minutes",
		concentration = "Concentration,",
		definition = """
			A storm cloud appears at a point within range that you can see above yourself. It takes the shape of a Cylinder that is 10 feet tall with a 60-foot radius.
			<br>
			When you cast the spell, choose a point you can see under the cloud. A lightning bolt shoots from the cloud to that point. Each creature within 5 feet of that point makes a Dexterity saving throw, taking 3d10 Lightning damage on a failed save or half as much damage on a successful one.
			<br>
			Until the spell ends, you can take a Magic action to call down lightning in that way again, targeting the same point or a different one.
			<br>
			If you're outdoors in a storm when you cast this spell, the spell gives you control over that storm instead of creating a new one. Under such conditions, the spell's damage increases by 1d10.
			<br>
			<b>Using a Higher-Level Spell Slot.</b> The damage increases by 1d10 for each spell slot level above 3.
			""")
	HypnoticPattern = Spell("Hypnotic Pattern", 3,
		school="Illusion",
		casting_time="Action",
		ranges = "120 feet",
		components = "Somatic, Material(a pinch of confetti)",
		duration = "1 minute",
		concentration = "Concentration",
		definition = """
			Up to six creatures of your choice that you can see within range regain Hit Points equal to 2d4 plus your spellcasting ability modifier.
			<br>
			Using a Higher-Level Spell Slot. The healing increases by 1d4 for each spell slot level above 3.
			"""
			)
	MassHealingWord = Spell("Mass Healing Word", 3,
		school="Abjuration",
		casting_time="Bonus Action",
		ranges = "60 feet",
		components = "Verbal",
		duration = "Instantaneous",
		concentration = "",
		definition = """
			Up to six creatures of your choice that you can see within range regain Hit Points equal to 2d4 plus your spellcasting ability modifier.
			<br>
			<b>Using a Higher-Level Spell Slot.</b> The healing increases by 1d4 for each spell slot level above 3.
			""")
	Nondetection = Spell("Nondetection", 3,
		school="Abjuration",
		casting_time="Action",
		ranges = "Touch",
		components = "Verbal, Somatic, Material (a pinch of diamond dust worth 25+ GP, which the spell consumes)",
		duration = "8 hours",
		concentration = "",
		definition = """
			For the duration, you hide a target that you touch from Divination spells. The target can be a willing creature, or it can be a place or an object no larger than 10 feet in any dimension. The target can't be targeted by any Divination spell or perceived through magical scrying sensors.
			""")
	PlantGrowth = Spell("Plant Growth", 3,
		school="Transmutation",
		casting_time="Action (Overgrowth) or 8 hours (Enrichment)",
		ranges = "150 feet",
		components = "Verbal, Somatic",
		duration = "Instantaneous",
		concentration = "",
		definition = """
			This spell channels vitality into plants. The casting time you use determines whether the spell has the Overgrowth or the Enrichment effect below.
			<ul style="list-style-type: '🪴'; text-align: left; ">
				<li><b>Overgrowth.</b> Choose a point within range. All normal plants in a 100-foot-radius Sphere centered on that point become thick and overgrown. A creature moving through that area must spend 4 feet of movement for every 1 foot it moves. You can exclude one or more areas of any size within the spell's area from being affected.</li>
				<li><b>Enrichment.</b> All plants in a half-mile radius centered on a point within range become enriched for 365 days. The plants yield twice the normal amount of food when harvested. They can benefit from only one Plant Growth per year.</li>
				</ul>
			""")
	SpeakwithDead = Spell("Speak with Dead", 3,
		school="Necromancy",
		casting_time="Action (Overgrowth) or 8 hours (Enrichment)",
		ranges = "10 feet",
		components = "Verbal, Somatic, Material (burning incense)",
		duration = "10 minutes",
		concentration = "",
		definition = """
		You grant the semblance of life to a corpse of your choice within range, allowing it to answer questions you pose. The corpse must have a mouth, and this spell fails if the deceased creature was Undead when it died. The spell also fails if the corpse was the target of this spell within the past 10 days.
		<br>
		Until the spell ends, you can ask the corpse up to five questions. The corpse knows only what it knew in life, including the languages it knew. Answers are usually brief, cryptic, or repetitive, and the corpse is under no compulsion to offer a truthful answer if you are antagonistic toward it or it recognizes you as an enemy. This spell doesn't return the creature's soul to its body, only its animating spirit. Thus, the corpse can't learn new information, doesn't comprehend anything that has happened since it died, and can't speculate about future events.
		""")
	Counterspell =  Spell("Counterspell", 3,
		school="Abjuration",
		casting_time="Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components",
		ranges = "60 feet",
		components = "Somatic",
		duration = "Instantaneous",
		concentration = "",
		definition = """
		You attempt to interrupt a creature in the process of casting a spell. The creature makes a Constitution saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.
		""")
	ThunderStep = Spell("Thunder Step", 3,
		school="Conjuration",
		casting_time="Action",
		ranges = "90 feet",
		components = "Verbal",
		duration = "Instantaneous",
		concentration = "",
		definition = """
You teleport yourself to an unoccupied space you can see within range. Immediately after you disappear, a thunderous boom sounds, and each creature within 10 feet of the space you left must make a Constitution saving throw, taking 3d10 thunder damage on a failed save, or half as much damage on a successful one. The thunder can be heard from up to 300 feet away.
<br>
You can bring along objects as long as their weight doesn't exceed what you can carry. You can also teleport one willing creature of your size or smaller who is carrying gear up to its carrying capacity. The creature must be within 5 feet of you when you cast this spell, and there must be an unoccupied space within 5 feet of your destination space for the creature to appear in; otherwise, the creature is left behind.
<br>
At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d10 for each slot level above 3rd.
		""")


	Revival = Revivify
	BeaconofHope = BeaconHope

# Define fourth-level spells
LEVEL4 = True
if LEVEL4:
	Compulsion = spell_from_data("Compulsion")
	StoneShape = spell_from_data("Stone Shape")
	GraspingVine = spell_from_data("Grasping Vine")
	DeathWard = spell_from_data("Death Ward")
	AuraofPurity = spell_from_data("Aura of Purity")
	SecretChest = spell_from_data("Leomund's Secret Chest")
	PrivateSanctum = spell_from_data("Mordenkainen's Private Sanctum")
	ArcaneEye = spell_from_data("Arcane Eye")
	GreaterInvisibility = spell_from_data("Greater Invisibility")
	CharmMonster = spell_from_data("Charm Monster")
	ShadowofMoil = spell_from_data("Shadow of Moil")
	Confusion = Spell("Confusion", 4,
				school="Enchantment",
				casting_time="Action",
				ranges = "90 feet",
				duration = "Up to 1 minute",
				components = "Verbal, Somatic, Material (three nut shells)",
				concentration = "Concentration",
				definition = """Each creature in a 10-foot-radius Sphere centered on a point you choose within range must succeed on a <b>Wisdom saving throw</b>, or that target can't take <b>Bonus Actions or Reactions</b> and must roll <b>1d10</b> at the start of each of its turns to determine its behavior for that turn, consulting the list below: <br>
 <ul style="list-style-type: '꩜'; text-align: left; ">
 <li> 1	|	The target doesn't take an action, and it uses all its movement to move. Roll 1d4 for the direction: 1, north; 2, east; 3, south; or 4, west. </li>
 <li> 2-6		|	The target doesn't move or take actions. </li>
 <li> 7-8	|	The target doesn't move, and it takes the Attack action to make one melee attack against a random creature within reach. If none are within reach, the target takes no action. </li>
 <li> 9-10		|	The target chooses its behavior. </li>
</ul>
At the end of each of its turns, an affected target repeats the save, ending the spell on itself on a success.
<br>
<b>Using a Higher-Level Spell Slot.</b> The Sphere's radius increases by 5 feet for each spell slot level above 4.""")
	DimensionDoor = spell_from_data("Dimension Door")
	ConjureMinorElementals = spell_from_data("Conjure Minor Elementals")
	ConjureWoodlandBeings = spell_from_data("Conjure Woodland Beings")
	ControlWater = spell_from_data("Control Water")
	Divination = spell_from_data("Divination")
	DominateBeast = spell_from_data("Dominate Beast")
	ElementalBane = spell_from_data("Elemental Bane")
	EvardsBlackTentacles = spell_from_data("Evard's Black Tentacles")
	Fabricate = spell_from_data("Fabricate")
	FindGreaterSteed = spell_from_data("Find Greater Steed")
	GalderSpeedyCourier = spell_from_data("Galder's Speedy Courier")
	GiantInsect = spell_from_data("Giant Insect")
	GravitySinkhole = spell_from_data("Gravity Sinkhole")
	GuardianFaith = spell_from_data("Guardian of Faith")
	IceStorm = Spell("Ice Storm", 4, 'Evocation', 'Action', '300 feet', 'Instantaneous', 'Verbal, Somatic,M (a mitten)', '', """<br>
	Hail falls in a 20-foot-radius, 40-foot-high Cylinder centered on a point within range. Each creature in the Cylinder makes a <b>Dexterity saving throw</b>. A creature takes <i>2d10 Bludgeoning damage</i> and <i>4d6 Cold damage</i> on a failed save or half as much damage on a successful one.
	<br>
	Hailstones turn ground in the Cylinder into Difficult Terrain until the end of your next turn.
	<br>
	<b>Using a Higher-Level Spell Slot.</b> The Bludgeoning damage increases by <i>1d10</i> for each spell slot level above 4.
	<br>""")
	FaithfulHound = spell_from_data("Mordenkainen's Faithful Hound")
	OtilukeResilientSphere = spell_from_data("Otiluke's Resilient Sphere")
	RaulothimPsychicLance = spell_from_data("Raulothim's Psychic Lance")
	SickeningRadiance = spell_from_data("Sickening Radiance")
	SpiritOfDeath = spell_from_data("Spirit Of Death")
	StaggeringSmite = spell_from_data("Staggering Smite")
	SummonAberration = spell_from_data("Summon Aberration")
	SummonConstruct = spell_from_data("Summon Construct")
	VitriolicSphere = spell_from_data("Vitriolic Sphere")
	WidogastVaultAmber = spell_from_data("Widogast's Vault of Amber (HB)")
	WidogastWebofFire = spell_from_data("Widogast's Web of Fire (HB)")
	AuraLife = spell_from_data("Aura of Life")
	LocateCreature = spell_from_data("Locate Creature")
	WaterySphere = spell_from_data("Watery Sphere")
	StormSphere = spell_from_data("Storm Sphere")
	GuardianNature = spell_from_data("Guardian of Nature")
	Compulsion = spell_from_data("Compulsion")
	StoneShape = spell_from_data("Stone Shape")
	FreedomOfMovement = spell_from_data("Freedom Of Movement")
	GraspingVine = spell_from_data("Grasping Vine")
	DeathWard = spell_from_data("Death Ward")
	AuraofPurity = spell_from_data("Aura of Purity")
	SecretChest = spell_from_data("Leomund's Secret Chest")
	PrivateSanctum = spell_from_data("Mordenkainen's Private Sanctum")
	ArcaneEye = spell_from_data("Arcane Eye")
	GreaterInvisibility = spell_from_data("Greater Invisibility")
	CharmMonster = spell_from_data("Charm Monster")
	ShadowofMoil = spell_from_data("Shadow of Moil")
	DimensionDoor = spell_from_data("Dimension Door")
	ConjureMinorElementals = spell_from_data("Conjure Minor Elementals")
	ConjureWoodlandBeings = spell_from_data("Conjure Woodland Beings")
	ControlWater = spell_from_data("Control Water")
	Divination = spell_from_data("Divination")
	DominateBeast = spell_from_data("Dominate Beast")
	ElementalBane = spell_from_data("Elemental Bane")
	EvardsBlackTentacles = spell_from_data("Evard's Black Tentacles")
	Fabricate = spell_from_data("Fabricate")
	FindGreaterSteed = spell_from_data("Find Greater Steed")
	GalderSpeedyCourier = spell_from_data("Galder's Speedy Courier")
	GiantInsect = spell_from_data("Giant Insect")
	GravitySinkhole = spell_from_data("Gravity Sinkhole")
	GuardianFaith = spell_from_data("Guardian of Faith")
	FaithfulHound = spell_from_data("Mordenkainen's Faithful Hound")
	OtilukeResilientSphere = spell_from_data("Otiluke's Resilient Sphere")
	RaulothimPsychicLance = spell_from_data("Raulothim's Psychic Lance")
	SickeningRadiance = spell_from_data("Sickening Radiance")
	SpiritOfDeath = spell_from_data("Spirit Of Death")
	StaggeringSmite = spell_from_data("Staggering Smite")
	SummonAberration = spell_from_data("Summon Aberration")
	SummonConstruct = spell_from_data("Summon Construct")
	VitriolicSphere = spell_from_data("Vitriolic Sphere")
	WidogastVaultAmber = spell_from_data("Widogast's Vault of Amber (HB)")
	WidogastWebofFire = spell_from_data("Widogast's Web of Fire (HB)")
	AuraLife = spell_from_data("Aura of Life")
	LocateCreature = spell_from_data("Locate Creature")
	WaterySphere = spell_from_data("Watery Sphere")
	StormSphere = spell_from_data("Storm Sphere")
	GuardianNature = spell_from_data("Guardian of Nature")
	SummonGreaterDemon = Spell("Summon Greater Demon", 4,
				school="Enchantment",
				casting_time="Action",
				ranges = "90 feet",
				duration = "Up to 1 minute",
				components = "Verbal, Somatic, Material (three nut shells)",
				concentration = "Concentration",
				definition = """
					You utter foul words, summoning one demon from the chaos of the Abyss. You choose the demon's type, which must be one of challenge rating 5 or lower, such as a shadow demon or a barlgura. The demon appears in an unoccupied space you can see within range, and the demon disappears when it drops to 0 hit points or when the spell ends.
					<br>
					Roll initiative for the demon, which has its own turns. When you summon it and on each of your turns thereafter, you can issue a verbal command to it (requiring no action on your part), telling it what it must do on its next turn. If you issue no command, it spends its turn attacking any creature within reach that has attacked it.
					<br>
					At the end of each of the demon's turns, it makes a Charisma saving throw. The demon has disadvantage on this saving throw if you say its true name. On a failed save, the demon continues to obey you. On a successful save, your control of the demon ends for the rest of the duration, and the demon spends its turns pursuing and attacking the nearest non-demons to the best of its ability. If you stop concentrating on the spell before it reaches its full duration, an uncontrolled demon doesn't disappear for 1d6 rounds if it still has hit points.
					<br>
					As part of casting the spell, you can form a circle on the ground with the blood used as a material component. The circle is large enough to encompass your space. While the spell lasts, the summoned demon can't cross the circle or harm it, and it can't target anyone within it. Using the material component in this manner consumes it when the spell ends.
					<br>
					<b>At Higher Levels.</b> When you cast this spell using a spell slot of 5th level or higher, the challenge rating increases by 1 for each slot level above 4th.
					""")
	GateSeal = Spell("Gate Seal", 4,
		school="Abjuration",
		casting_time="1 minute",
		ranges = "60 feet",
		duration = "24 hours",
		components = "Verbal, Somatic, Material (a broken portal key, which the spell consumes)",
		concentration = "",
		definition = """
			You fortify the fabric of the planes in a 30-foot cube you can see within range. Within that area, portals close and can't be opened for the duration. Spells and other effects that allow planar travel or open portals, such as gate or plane shift, fail if used to enter or leave the area. The cube is stationary.
			<br>
			At Higher Levels. When you cast this spell using a spell slot of 6th level or higher, the spell lasts until dispelled.
			""")
	Stoneskin = Spell("Stoneskin", 4,
		school="Transmutation",
		casting_time="Action",
		ranges = "Touch",
		duration = "1 hour",
		components = "Verbal, Somatic, Material (diamond dust worth 100+ GP, which the spell consumes)",
		concentration = "Concentration",
		definition = """
			Until the spell ends, one willing creature you touch has Resistance to Bludgeoning, Piercing, and Slashing damage.
			""")
	FireShield = Spell("Fire Shield", 4,
			school="Evocation",
			casting_time="Action",
			ranges = "Self",
			components = "Verbal, Somatic, Material (a bit of phosphorus or a firefly)",
			duration = "10 minutes",
			concentration = "",
			definition = """
				Wispy flames wreathe your body for the duration, shedding Bright Light in a 10-foot radius and Dim Light for an additional 10 feet.
				<br>
				The flames provide you with a warm shield or a chill shield, as you choose. The warm shield grants you Resistance to Cold damage, and the chill shield grants you Resistance to Fire damage.
				<br>
				In addition, whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame. The attacker takes 2d8 Fire damage from a warm shield or 2d8 Cold damage from a chill shield.
				""")
	WallofFire = Spell("Wall of Fire", 4,
				school="Evocation",
				casting_time="Action",
				ranges = "120 feet",
				components = "Verbal, Somatic, Material (a piece of charcoal)",
				duration = "1 minute",
				concentration = "Concentration",
				definition = """
					You create a wall of fire on a solid surface within range. You can make the wall up to 60 feet long, 20 feet high, and 1 foot thick, or a ringed wall up to 20 feet in diameter, 20 feet high, and 1 foot thick. The wall is opaque and lasts for the duration.
					<br>
					When the wall appears, each creature in its area makes a Dexterity saving throw, taking 5d8 Fire damage on a failed save or half as much damage on a successful one.
					<br>
					One side of the wall, selected by you when you cast this spell, deals 5d8 Fire damage to each creature that ends its turn within 10 feet of that side or inside the wall. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there. The other side of the wall deals no damage.
					""")
	HallucinatoryTerrain = Spell("Hallucinatory Terrain", 4,
		school="Illusion",
		casting_time="10 minutes",
		ranges = "300 feet",
		components = "Verbal, Somatic, Material (a mushroom)",
		duration = "24 hours",
		concentration = "",
		definition = """
		You make natural terrain in a 150-foot Cube in range look, sound, and smell like another sort of natural terrain. Thus, open fields or a road can be made to resemble a swamp, hill, crevasse, or some other difficult or impassable terrain. A pond can be made to seem like a grassy meadow, a precipice like a gentle slope, or a rock-strewn gully like a wide and smooth road. Manufactured structures, equipment, and creatures within the area aren't changed.
		<br>
		The tactile characteristics of the terrain are unchanged, so creatures entering the area are likely to notice the illusion. If the difference isn't obvious by touch, a creature examining the illusion can take the Study action to make an Intelligence (Investigation) check against your spell save DC to disbelieve it. If a creature discerns that the terrain is illusory, the creature sees a vague image superimposed on the real terrain.
		""")
	PhantasmalKiller = Spell("Phantasmal Killer", 4,
		school="Illusion",
		casting_time="Action",
		ranges = "120 feet",
		components = "Verbal, Somatic",
		duration = "1 minute",
		concentration = "Concentration",
		definition = """
		You tap into the nightmares of a creature you can see within range and create an illusion of its deepest fears, visible only to that creature. The target makes a Wisdom saving throw. On a failed save, the target takes 4d10 Psychic damage and has Disadvantage on ability checks and attack rolls for the duration. On a successful save, the target takes half as much damage, and the spell ends.
		<br>
		For the duration, the target makes a Wisdom saving throw at the end of each of its turns. On a failed save, it takes the Psychic damage again. On a successful save, the spell ends.
		<br>
		Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 4.
		""")
	Polymorph = Spell("Polymorph", 4,
		school="Transmutation",
		casting_time="Action",
		ranges = "60 feet",
		components = "Verbal, Somatic, Material (a caterpillar cocoon)",
		duration = "1 hour",
		concentration = "Concentration",
		definition = """
		You attempt to transform a creature that you can see within range into a Beast. The target must succeed on a Wisdom saving throw or shape-shift into Beast form for the duration. That form can be any Beast you choose that has a Challenge Rating equal to or less than the target's (or the target's level if it doesn't have a Challenge Rating). The target's game statistics are replaced by the stat block of the chosen Beast, but the target retains its alignment, personality, creature type, Hit Points, and Hit Point Dice.
		<br>
		The target gains a number of Temporary Hit Points equal to the Hit Points of the Beast form. These Temporary Hit Points vanish if any remain when the spell ends. The spell ends early on the target if it has no Temporary Hit Points left.
		<br>
		The target is limited in the actions it can perform by the anatomy of its new form, and it can't speak or cast spells.
		<br>
		The target's gear melds into the new form. The creature can't use or otherwise benefit from any of that equipment.

		""")
	SummonElemental = Spell("Summon Elemental", 4,
			school="Conjuration",
			casting_time="Action",
			ranges = "90 feet",
			components = "Verbal, Somatic, Material (air, a pebble, ash, and water inside a gold-inlaid vial worth 400+ GP)",
			concentration = "Concentration",
			duration = "1 hour",
			definition = """
			You call forth an Elemental spirit. It manifests in an unoccupied space that you can see within range and uses the Elemental Spirit stat block. When you cast the spell, choose an element: Air, Earth, Fire, or Water. The creature resembles a bipedal form wreathed in the chosen element, which determines certain details in its stat block. The creature disappears when it drops to 0 Hit Points or when the spell ends.
			<br>
			The creature is an ally to you and your allies. In combat, the creature shares your Initiative count, but it takes its turn immediately after yours. It obeys your verbal commands (no action required by you). If you don't issue any, it takes the Dodge action and uses its movement to avoid danger.
			<br>
			Using a Higher-Level Spell Slot. Use the spell slot's level for the spell's level in the stat block.
			""")
	Blight = Spell("Blight", 4,
		school="Necromancy",
		casting_time="Action",
		ranges = "30 feet",
		components = "Verbal, Somatic.",
		concentration = "",
		duration = "Instantaneous",
		definition = """
		A creature that you can see within range makes a Constitution saving throw, taking 8d8 Necrotic damage on a failed save or half as much damage on a successful one.
		A Plant creature automatically fails the save.
		<br>
		Alternatively, target a nonmagical plant that isn't a creature, such as a tree or shrub.
		It doesn't make a save; it simply withers and dies.
		<br>
		<b>Using a Higher-Level Spell Slot.</b> The damage increases by 1d8 for each spell slot level above 4.
		""")
	Banishment = Spell("Banishment", 4,
			school="Abjuration",
			casting_time="Action",
			ranges = "30 feet",
			components = "Verbal, Somatic, Materials (a pentacle)",
			concentration = "Concentration",
			duration = "1 minute",
			definition = """
			One creature that you can see within range must succeed on a Charisma saving throw or be transported to a harmless demiplane for the duration. While there, the target has the Incapacitated condition. When the spell ends, the target reappears in the space it left or in the nearest unoccupied space if that space is occupied.
			<br>
			If the target is an Aberration, a Celestial, an Elemental, a Fey, or a Fiend, the target doesn't return if the spell lasts for 1 minute. The target is instead transported to a random location on a plane (DM's choice) associated with its creature type.
			<br>
			Using a Higher-Level Spell Slot. You can target one additional creature for each spell slot level above 4.
			""")






	FreedomofMovement = FreedomOfMovement
	GuardianofFaith = GuardianFaith

# Define fifth-level spells
LEVEL5 = True
if LEVEL5:
	Passwall = spell_from_data("Passwall")
	RaiseDead = spell_from_data("Raise Dead")
	LegendLore = spell_from_data("Legend Lore")
	Seeming = spell_from_data("Seeming")
	Cloudkill = spell_from_data("Cloudkill")
	AntilifeShell = Spell("Antilife Shell", 5, "Abjuration ", "1 Action ", "Self (10-foot radius) ", "Concentration, up to 1 hour ", "Verbal, Somatic")
	Awaken = Spell("Awaken", 5, "Transmutation ", "8 Hours ", "Touch ", "Instantaneous ", "Verbal, Somatic, Material")
	BigbysHand = Spell("Bigby's Hand", 5, "Evocation ", "1 Action ", "120 feet ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	CircleofPower = Spell("Circle of Power", 5, "Abjuration ", "1 Action ", "Self (30-foot radius) ", "Concentration, up to 10 minutes ", "Verbal")
	Commune = Spell("Commune", 5, "Divination ", "1 Minute R ", "Self ", "1 minute ", "Verbal, Somatic, Material")
	ConjureElemental = Spell("Conjure Elemental", 5, "Conjuration ", "1 Action ", "90 feet ", "Concentration, up to 1 hour ", "Verbal, Somatic, Material")
	ConjureVolley = Spell("Conjure Volley", 5, "Conjuration ", "1 Action ", "150 feet ", "Instantaneous ", "Verbal, Somatic, Material")
	Contagion = Spell("Contagion", 5, "Necromancy ", "1 Action ", "Touch ", "7 days ", "Verbal, Somatic")
	CreateSpelljammingHelm = Spell("Create Spelljamming Helm", 5, "Transmutation ", "1 Action ", "Touch ", "Instantaneous ", "Verbal, Somatic,M")
	Dawn = Spell("Dawn", 5, "Evocation ", "1 Action ", "60 Feet ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	DestructiveWave = Spell("Destructive Wave", 5, "Evocation ", "1 Action ", "Self (30-foot radius) ", "Instantaneous ", "Verbal")
	Dream = Spell("Dream", 5, "Illusion ", "1 Minute ", "Special ", "8 hours ", "Verbal, Somatic, Material")
	Enervation = Spell("Enervation", 5, "Necromancy ", "1 Action ", "60 feet ", "Concentration, up to 1 minute ", "Verbal, Somatic")
	FreedomofWinds = Spell("Freedom of the Winds (HB)", 5, "Abjuration HB ", "1 action ", "Self ", "Concentration up to 10 minutes ", "Verbal, Somatic, Material")
	Hallow = Spell("Hallow", 5, "Evocation ", "24 Hours ", "Touch ", "Until dispelled ", "Verbal, Somatic, Material")
	HoldMonster = Spell("Hold Monster", 5, "Enchantment ", "1 Action ", "90 feet ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	HolyWeapon = Spell("Holy Weapon", 5, "Evocation ", "1 Bonus Action ", "Touch ", "Concentration, up to 1 hour ", "Verbal, Somatic")
	Immolation = Spell("Immolation", 5, "Evocation ", "1 Action ", "90 feet ", "Concentration, up to 1 minute ", "Verbal")
	InfernalCalling = Spell("Infernal Calling", 5, "Conjuration ", "1 Minute ", "90 feet ", "Concentration, up to 1 hour ", "Verbal, Somatic, Material")
	Maelstrom = Spell("Maelstrom", 5, "Evocation ", "1 Action ", "120 feet ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	NegativeEnergyFlood = Spell("Negative Energy Flood", 5, "Necromancy ", "1 Action ", "60 feet ", "Instantaneous ", "Verbal, Material")
	Reincarnate = Spell("Reincarnate", 5, "Transmutation ", "1 Action ", "Touch ", "Instantaneous ", "Verbal, Somatic, Material")
	SkillEmpowerment = Spell("Skill Empowerment", 5, "Transmutation ", "1 Action ", "Touch ", "Concentration, up to 1 hour ", "Verbal, Somatic")
	SteelWindStrike = Spell("Steel Wind Strike", 5, "Conjuration ", "1 Action ", "30 feet ", "Instantaneous ", "Somatic, Material")
	SummonCelestial = Spell("Summon Celestial", 5, "Conjuration ", "1 Action ", "90 feet ", "Concentration, up to 1 hour ", "Verbal, Somatic, Material")
	SummonDraconicSpirit = Spell("Summon Draconic Spirit", 5, "Conjuration ", "1 Action ", "60 feet ", "Concentration, up to 1 hour ", "Verbal, Somatic, Material")
	SwiftQuiver = Spell("Swift Quiver", 5, "Transmutation ", "1 Bonus Action ", "Touch ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	TemporalShunt = Spell("Temporal Shunt", 5, "Transmutation DC ", "1 Reaction ", "120 feet ", "1 round ", "Verbal, Somatic")
	WallForce = Spell("Wall of Force", 5, "Evocation ", "1 Action ", "120 feet ", "Concentration, up to 10 minutes ", "Verbal, Somatic, Material")
	BanishingSmite = Spell("Banishing Smite", 5, "Abjuration ", "1 Bonus Action ", "Self ", "Concentration, up to 1 minute ", "Verbal")
	CommuneNature = Spell("Commune with Nature", 5, "Divination ", "1 Minute R ", "Self ", "Instantaneous ", "Verbal, Somatic")
	WrathNature = Spell("Wrath Of Nature", 5, "Evocation", "1 Action ", "120 feet ", "Concentration, up to 1 minute ", "Verbal, Somatic")
	TreeStride = Spell("Tree Stride", 5, "Conjuration ", "1 Action ", "Self ", "Concentration, up to 1 minute ", "Verbal, Somatic")
	TransmuteRock = Spell("Transmute Rock", 5, "Transmutation ", "1 Action ", "120 feet ", "Instantaneous ", "Verbal, Somatic, Material")
	ControlWinds = Spell("Control Winds", 5, "Transmutation ", "1 Action ", "300 feet ", "Concentration, up to 1 hour ", "Verbal, Somatic")
	DispelEvilandGood = Spell("Dispel Evil and Good", 5, "Abjuration ", "1 Action ", "Self ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	Passwall = spell_from_data("Passwall")
	RaiseDead = spell_from_data("Raise Dead")
	LegendLore = spell_from_data("Legend Lore")
	Seeming = spell_from_data("Seeming")
	Cloudkill = spell_from_data("Cloudkill")
	AntilifeShell = Spell("Antilife Shell", 5, "Abjuration ", "1 Action ", "Self (10-foot radius) ", "Concentration, up to 1 hour ", "Verbal, Somatic")
	Awaken = 		Spell("Awaken", 5, "Transmutation ", "8 Hours ", "Touch ", "Instantaneous ", "Verbal, Somatic, Material")
	BigbysHand = 	Spell("Bigby's Hand", 5, "Evocation ", "1 Action ", "120 feet ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	CircleofPower = Spell("Circle of Power", 5, "Abjuration ", "1 Action ", "Self (30-foot radius) ", "Concentration, up to 10 minutes ", "Verbal")
	Commune = 	Spell("Commune", 5, "Divination ", "1 Minute R ", "Self ", "1 minute ", "Verbal, Somatic, Material")

	ConjureElemental = Spell("Conjure Elemental", 5, "Conjuration ", "1 Action ", "90 feet ", "Concentration, up to 1 hour ", "Verbal, Somatic, Material")
	ConjureVolley = 	Spell("Conjure Volley", 5, "Conjuration ", "1 Action ", "150 feet ", "Instantaneous ", "Verbal, Somatic, Material")
	Contagion = Spell("Contagion", 5, "Necromancy ", "1 Action ", "Touch ", "7 days ", "Verbal, Somatic")
	CreateSpelljammingHelm = Spell("Create Spelljamming Helm", 5, "Transmutation ", "1 Action ", "Touch ", "Instantaneous ", "Verbal, Somatic,M")
	Dawn = Spell("Dawn", 5, "Evocation ", "1 Action ", "60 Feet ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	DestructiveWave = Spell("Destructive Wave", 5, "Evocation ", "1 Action ", "Self (30-foot radius) ", "Instantaneous ", "Verbal")
	Dream = Spell("Dream", 5, "Illusion ", "1 Minute ", "Special ", "8 hours ", "Verbal, Somatic, Material")
	Enervation = Spell("Enervation", 5, "Necromancy ", "1 Action ", "60 feet ", "Concentration, up to 1 minute ", "Verbal, Somatic")
	FreedomofWinds = Spell("Freedom of the Winds (HB)", 5, "Abjuration HB ", "1 action ", "Self ", "Concentration up to 10 minutes ", "Verbal, Somatic, Material")
	Hallow = Spell("Hallow", 5, "Evocation ", "24 Hours ", "Touch ", "Until dispelled ", "Verbal, Somatic, Material")
	HoldMonster = Spell("Hold Monster", 5, "Enchantment ", "1 Action ", "90 feet ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	HolyWeapon = Spell("Holy Weapon", 5, "Evocation ", "1 Bonus Action ", "Touch ", "Concentration, up to 1 hour ", "Verbal, Somatic")
	Immolation = Spell("Immolation", 5, "Evocation ", "1 Action ", "90 feet ", "Concentration, up to 1 minute ", "Verbal")
	InfernalCalling = Spell("Infernal Calling", 5, "Conjuration ", "1 Minute ", "90 feet ", "Concentration, up to 1 hour ", "Verbal, Somatic, Material")
	Maelstrom = 		Spell("Maelstrom", 5, "Evocation ", "1 Action ", "120 feet ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	NegativeEnergyFlood = Spell("Negative Energy Flood", 5, "Necromancy ", "1 Action ", "60 feet ", "Instantaneous ", "Verbal, Material")
	Reincarnate = 		Spell("Reincarnate", 5, "Transmutation ", "1 Action ", "Touch ", "Instantaneous ", "Verbal, Somatic, Material")
	SkillEmpowerment = 	Spell("Skill Empowerment", 5, "Transmutation ", "1 Action ", "Touch ", "Concentration, up to 1 hour ", "Verbal, Somatic")
	SteelWindStrike = 	Spell("Steel Wind Strike", 5, "Conjuration ", "1 Action ", "30 feet ", "Instantaneous ", "Somatic, Material")
	SummonCelestial = 		Spell("Summon Celestial", 5, "Conjuration ", "1 Action ", "90 feet ", "Concentration, up to 1 hour ", "Verbal, Somatic, Material")
	SummonDraconicSpirit = 	Spell("Summon Draconic Spirit", 5, "Conjuration ", "1 Action ", "60 feet ", "Concentration, up to 1 hour ", "Verbal, Somatic, Material")
	SwiftQuiver = 			Spell("Swift Quiver", 5, "Transmutation ", "1 Bonus Action ", "Touch ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	TemporalShunt = 	Spell("Temporal Shunt", 5, "Transmutation DC ", "1 Reaction ", "120 feet ", "1 round ", "Verbal, Somatic")
	WallForce = 		Spell("Wall of Force", 5, "Evocation ", "1 Action ", "120 feet ", "Concentration, up to 10 minutes ", "Verbal, Somatic, Material")
	WallofForce = 		WallForce
	BanishingSmite = 	Spell("Banishing Smite", 5, "Abjuration ", "1 Bonus Action ", "Self ", "Concentration, up to 1 minute ", "Verbal")
	CommuneNature = Spell("Commune with Nature", 5, "Divination ", "1 Minute R ", "Self ", "Instantaneous ", "Verbal, Somatic")
	WrathNature = Spell("Wrath Of Nature", 5, "Evocation", "1 Action ", "120 feet ", "Concentration, up to 1 minute ", "Verbal, Somatic")
	TreeStride = 	Spell("Tree Stride", 5, "Conjuration ", "1 Action ", "Self ", "Concentration, up to 1 minute ", "Verbal, Somatic")
	TransmuteRock = Spell("Transmute Rock", 5, "Transmutation ", "1 Action ", "120 feet ", "Instantaneous ", "Verbal, Somatic, Material")
	ControlWinds = 		Spell("Control Winds", 5, "Transmutation ", "1 Action ", "300 feet ", "Concentration, up to 1 hour ", "Verbal, Somatic")
	DispelEvilandGood = Spell("Dispel Evil and Good", 5, "Abjuration ", "1 Action ", "Self ", "Concentration, up to 1 minute ", "Verbal, Somatic, Material")
	CommuneWithNature = CommuneNature
	JallarziStormofRadiance = Spell("Jallarzi's Storm of Radiance", 5, "Evocation",
									"Action", "120 feet", "Instantaneous", "Verbal, Somatic, Material")
	DanseMacabre = Spell("Danse Macabre", 5,
		school="Necromancy",
		casting_time="Action",
		ranges = "60 feet",
		duration = "1 hour",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		definition = """
Threads of dark power leap from your fingers to pierce up to five Small or Medium corpses you can see within range. Each corpse immediately stands up and becomes undead. You decide whether it is a zombie or a skeleton (the statistics for zombies and skeletons are in the Monster Manual), and it gains a bonus to its attack and damage rolls equal to your spellcasting ability modifier.
<br>
You can use a bonus action to mentally command the creatures you make with this spell, issuing the same command to all of them. To receive the command, a creature must be within 60 feet of you. You decide what action the creatures will take and where they will move during their next turn, or you can issue a general command, such as to guard a chamber or passageway against your foes. If you issue no commands, the creatures do nothing except defend themselves against hostile creatures. Once given an order, the creatures continue to follow it until their task is complete.
<br>
The creatures are under your control until the spell ends, after which they become inanimate once more.
<br>
At Higher Levels. When you cast this spell using a spell slot of 6th level or higher, you animate up to two additional corpses for each slot level above 5th.
			""")
	ContactOtherPlane = Spell("Contact Other Plane", 5,
	school="Divination",
	casting_time="1 minute or Ritual",
	ranges = "Self",
	duration = "1 minute",
	components = "Verbal",
	concentration = "",
	definition = """
You mentally contact a demigod, the spirit of a long-dead sage, or some other knowledgeable entity from another plane.
Contacting this otherworldly intelligence can break your mind.
When you cast this spell, make a DC 15 Intelligence saving throw.
On a successful save, you can ask the entity up to five questions.
You must ask your questions before the spell ends.
The DM answers each question with one word, such as "yes," "no," "maybe," "never," "irrelevant," or "unclear" (if the entity doesn't know the answer to the question).
If a one-word answer would be misleading, the DM might instead offer a short phrase as an answer.
<br>
On a failed save, you take <b>6d6 Psychic damage</b> and have the
<b>Incapacitated</b> condition until you finish a Long Rest.
A Greater Restoration spell cast on you ends this effect.
		""")
	AnimateObjects = Spell("Animate Objects", 5,
	school="Transmutation",
	casting_time="Action",
	ranges = "120 feet",
	duration = "1 minute",
	components = "Verbal, Somatic",
	concentration = "Concentration",
	definition = """
	Objects animate at your command. Choose a number of nonmagical objects within range that aren't being worn or carried, aren't fixed to a surface, and aren't Gargantuan. The maximum number of objects is equal to your spellcasting ability modifier; for this number, a Medium or smaller target counts as one object, a Large target counts as two, and a Huge target counts as three.
	<br>
	Each target animates, sprouts legs, and becomes a Construct that uses the Animated Object stat block; this creature is under your control until the spell ends or until it is reduced to 0 Hit Points. Each creature you make with this spell is an ally to you and your allies. In combat, it shares your Initiative count and takes its turn immediately after yours.
	<br>
	Until the spell ends, you can take a Bonus Action to mentally command any creature you made with this spell if the creature is within 500 feet of you (if you control multiple creatures, you can command any of them at the same time, issuing the same command to each one). If you issue no commands, the creature takes the Dodge action and moves only to avoid harm. When the creature drops to 0 Hit Points, it reverts to its object form, and any remaining damage carries over to that form.
	<br>
	<b>Using a Higher-Level Spell Slot.</b> The creature's Slam damage increases by 1d4 (Medium or smaller), 1d6 (Large), or 1d12 (Huge) for each spell slot level above 5.
	"""
	)
	TeleportationCircle = Spell("Teleportation Circle", 5,
		school="Conjuration",
		casting_time="1 minute",
		ranges = "10 feet",
		duration = "1 round",
		components = "Verbal, Material (rare inks worth 50+ GP, which the spell consumes)",
		concentration = "",
		definition = """
		As you cast the spell, you draw a 5-foot-radius circle on the ground inscribed with sigils that link your location to a permanent teleportation circle of your choice whose sigil sequence you know and that is on the same plane of existence as you. A shimmering portal opens within the circle you drew and remains open until the end of your next turn. Any creature that enters the portal instantly appears within 5 feet of the destination circle or in the nearest unoccupied space if that space is occupied.
		<br>
		Many major temples, guildhalls, and other important places have permanent teleportation circles. Each circle includes a unique sigil sequence—a string of runes arranged in a particular pattern.
		<br>
		When you first gain the ability to cast this spell, you learn the sigil sequences for two destinations on the Material Plane, determined by the DM. You might learn additional sigil sequences during your adventures. You can commit a new sigil sequence to memory after studying it for 1 minute.
		<br>
		You can create a permanent teleportation circle by casting this spell in the same location every day for 365 days.
		"""
		)
	Scrying = Spell("Scrying", 5,
		school="Divination",
		casting_time="10 minutes",
		ranges = "Self",
		duration = "1 round",
		components = "Verbal, Somatic, Material (a focus worth 1,000+ GP, such as a crystal ball, mirror, or water-filled font)",
		concentration = "Concentration",
		definition = """
You can see and hear a creature you choose that is on the same plane of existence as you. The target makes a Wisdom saving throw, which is modified (see the tables below) by how well you know the target and the sort of physical connection you have to it. The target doesn't know what it is making the save against, only that it feels uneasy.
 <table>
  <tr>
	<th>Your Knowledge of the Target Is...</th>
	<th>Save Modifier</th>
  </tr>
  <tr>
	<td>Secondhand (heard of the target)</td>
	<td>+5</td>
  </tr>
  <tr>
	<td>Firsthand (met the target)</td>
	<td>+0</td>
  </tr>
   <tr>
	 <td>Extensive (know the target well)</td>
	 <td>-5</td>
   </tr>
</table>


 <table>
  <tr>
	<th>You Have the Target's...</th>
	<th>Save Modifier</th>
  </tr>
  <tr>
	<td>Picture or other likeness</td>
	<td>-2</td>
  </tr>
  <tr>
	<td>Garment or other possession</td>
	<td>-4</td>
  </tr>
   <tr>
	 <td>Body part, lock of hair, or bit of nail</td>
	 <td>-10</td>
   </tr>
</table>

		On a successful save, the target isn't affected, and you can't use this spell on it again for 24 hours.
		<br>
		On a failed save, the spell creates an Invisible, intangible sensor within 10 feet of the target. You can see and hear through the sensor as if you were there. The sensor moves with the target, remaining within 10 feet of it for the duration. If something can see the sensor, it appears as a luminous orb about the size of your fist.
		<br>
		Instead of targeting a creature, you can target a location you have seen. When you do so, the sensor appears at that location and doesn't move.
		"""
		)
	FarStep = Spell("Far Step",
		level= 5,
		school="Conjuration",
		casting_time="Bonus Action",
		ranges = "Self",
		duration = "1 minute",
		components = "Verbal",
		concentration = "Concentration",
		definition = """
		You teleport up to 60 feet to an unoccupied space you can see. On each of your turns before the spell ends, you can use a bonus action to teleport in this way again.
		""")
	SynapticStatic = 	Spell("Synaptic Static",
		level= 5,
		school="Enchantment",
		casting_time="Action",
		ranges = "120 feet",
		duration = "Instantaneous",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
You cause psychic energy to erupt at a point within range. Each creature in a 20-foot-radius Sphere centered on that point makes an Intelligence saving throw, taking 8d6 Psychic damage on a failed save or half as much damage on a successful one.
<br>
On a failed save, a target also has muddled thoughts for 1 minute. During that time, it subtracts 1d6 from all its attack rolls and ability checks, as well as any Constitution saving throws to maintain Concentration. The target makes an Intelligence saving throw at the end of each of its turns, ending the effect on itself on a success.
		""")
	Geas = Spell("Geas",
		level= 5,
		school="Enchantment",
		casting_time="1 minute",
		ranges = "60 feet",
		components = "Verbal",
		duration = "30 days",
		concentration = "",
		definition = """
			You give a verbal command to a creature that you can see within range, ordering it to carry out some service or refrain from an action or a course of activity as you decide. The target must succeed on a Wisdom saving throw or have the Charmed condition for the duration. The target automatically succeeds if it can't understand your command.
			<br>
			While Charmed, the creature takes 5d10 Psychic damage if it acts in a manner directly counter to your command. It takes this damage no more than once each day.
			<br>
			You can issue any command you choose, short of an activity that would result in certain death. Should you issue a suicidal command, the spell ends.
			<br>
			A Remove Curse, Greater Restoration, or Wish spell ends this spell.
			<br>
			Using a Higher-Level Spell Slot. If you use a level 7 or 8 spell slot, the duration is 365 days. If you use a level 9 spell slot, the spell lasts until it is ended by one of the spells mentioned above.
			""")
	InsectPlague = Spell("Insect Plague",
		level= 5,
		school="Conjuration",
		casting_time="Action",
		ranges = "300 feet",
		components = "Verbal, Somatic, Material (a locust)",
		duration = "10 minutes",
		concentration = "Concentration",
		definition = """
			Swarming locusts fill a 20-foot-radius Sphere centered on a point you choose within range. The Sphere remains for the duration, and its area is Lightly Obscured and Difficult Terrain.
			<br>
			When the swarm appears, each creature in it makes a Constitution saving throw, taking 4d10 Piercing damage on a failed save or half as much damage on a successful one. A creature also makes this save when it enters the spell's area for the first time on a turn or ends its turn there. A creature makes this save only once per turn.
			<br>
			Using a Higher-Level Spell Slot. The damage increases by 1d10 for each spell slot level above 5.
			""")
	PlanarBinding = Spell("Planar Binding",
			level= 5,
			school="Abjuration",
			casting_time="1 hour",
			ranges = "60 feet",
			components = "Verbal, Somatic, Material (a jewel worth 1,000+ GP, which the spell consumes)",
			duration = "24 hours",
			concentration = "",
			definition = """
You attempt to bind a Celestial, an Elemental, a Fey, or a Fiend to your service. The creature must be within range for the entire casting of the spell. (Typically, the creature is first summoned into the center of the inverted version of the Magic Circle spell to trap it while this spell is cast.) At the completion of the casting, the target must succeed on a Charisma saving throw or be bound to serve you for the duration. If the creature was summoned or created by another spell, that spell's duration is extended to match the duration of this spell.
<br>
A bound creature must follow your commands to the best of its ability. You might command the creature to accompany you on an adventure, to guard a location, or to deliver a message. If the creature is Hostile, it strives to twist your commands to achieve its own objectives. If the creature carries out your commands completely before the spell ends, it travels to you to report this fact if you are on the same plane of existence. If you are on a different plane, it returns to the place where you bound it and remains there until the spell ends.
<br>
Using a Higher-Level Spell Slot. The duration increases with a spell slot of level 6 (10 days), 7 (30 days), 8 (180 days), and 9 (366 days).
				""")
	WallLight = 		Spell("Wall of Light",
			level= 5,
			school="Evocation",
			casting_time="Action",
			ranges = "120 feet",
			components = "Verbal, Somatic, Material (a hand mirror)",
			concentration = "Concentration",
			duration = "10 minutes",
			definition = """
A shimmering wall of bright light appears at a point you choose within range. The wall appears in any orientation you choose: horizontally, vertically, or diagonally. It can be free floating, or it can rest on a solid surface. The wall can be up to 60 feet long, 10 feet high, and 5 feet thick. The wall blocks line of sight, but creatures and objects can pass through it. It emits bright light out to 120 feet and dim light for an additional 120 feet.
<br>
When the wall appears, each creature in its area must make a Constitution saving throw. On a failed save, a creature takes 4d8 radiant damage, and it is blinded for 1 minute. On a successful save, it takes half as much damage and isn't blinded. A blinded creature can make a Constitution saving throw at the end of each of its turns, ending the effect on itself on a success.
<br>
A creature that ends its turn in the wall's area takes 4d8 radiant damage.
<br>
Until the spell ends, you can use an action to launch a beam of radiance from the wall at one creature you can see within 60 feet of it. Make a ranged spell attack. On a hit, the target takes 4d8 radiant damage. Whether you hit or miss, reduce the length of the wall by 10 feet. If the wall's length drops to 0 feet, the spell ends.
<br>
At Higher Levels. When you cast this spell using a spell slot of 6th level or higher, the damage increases by 1d8 for each slot level above 5th.
				""")
	Creation = Spell("Creation",
			level= 5,
			school="Illusion",
			casting_time="1 Minute",
			ranges = "30 feet",
			components = "Verbal, Somatic, Material (a paintbrush)",
			concentration = "Concentration",
			duration = "Special",
			definition = """
You pull wisps of shadow material from the Shadowfell to create an object within range. It is either an object of vegetable matter (soft goods, rope, wood, and the like) or mineral matter (stone, crystal, metal, and the like). The object must be no larger than a 5-foot Cube, and the object must be of a form and material that you have seen.
<br>
The spell's duration depends on the object's material, as shown in the Materials table. If the object is composed of multiple materials, use the shortest duration. Using any object created by this spell as another spell's Material component causes the other spell to fail.
 <table>
  <tr>	<th>Material</th>			<th>Duration</th>	</tr>
  <tr>	<td>Vegetable matter</td>	<td>24 hours</td>	</tr>
  <tr>	<td>Stone or crystal</td>	<td>12 hours</td>	</tr>
  <tr>	<td>Precious metals</td>	<td>1 hour</td>		</tr>
  <tr>	<td>Gems</td>				<td>10 minutes</td>	</tr>
  <tr>	<td>Adamantine or mithral</td> <td>1 minute</td>	</tr>
</table>

Using a Higher-Level Spell Slot. The Cube increases by 5 feet for each spell slot level above 5.
				""")
	FlameStrike = 		Spell("Flame Strike",
		level= 5,
		school="Evocation",
		casting_time="Action",
		ranges = "60 feet",
		components = "Verbal, Somatic, Material (a pinch of sulfur)",
		concentration = "",
		duration = "Instantaneous",
		definition = """
		A vertical column of brilliant fire roars down from above. Each creature in a 10-foot-radius, 40-foot-high Cylinder centered on a point within range makes a Dexterity saving throw, taking 5d6 Fire damage and 5d6 Radiant damage on a failed save or half as much damage on a successful one.
		<br>
		Using a Higher-Level Spell Slot. The Fire damage and the Radiant damage increase by 1d6 for each spell slot level above 5.
		""")
	GreaterRestoration = Spell("Greater Restoration",
		level= 5,
		school="Abjuration",
		casting_time="Action",
		ranges = "Touch",
		components = "Verbal, Somatic, Material (diamond dust worth 100+ GP, which the spell consumes)",
		concentration = "",
		duration = "Instantaneous",
		definition = """
You touch a creature and magically remove one of the following effects from it:
<ul style="list-style-type: '💚'; text-align: left; ">
	<li>1 Exhaustion level</li>
	<li>The Charmed or Petrified condition.</li>
	<li>A curse, including the target's Attunement to a cursed magic item.</li>
	<li>Any reduction to one of the target's ability scores</li>
	<li>Any reduction to the target's Hit Point maximum.</li>
	</ul>
	""")
	DominatePerson = Spell("Dominate Person",
			level= 5,
			school="Enchantment",
			casting_time="Action",
			ranges = "60 feet",
			components = "Verbal, Somatic",
			concentration = "",
			duration = "1 minute",
			definition = """
			One Humanoid you can see within range must succeed on a Wisdom saving throw or have the Charmed condition for the duration. The target has Advantage on the save if you or your allies are fighting it. Whenever the target takes damage, it repeats the save, ending the spell on itself on a success.
			<br>
			You have a telepathic link with the Charmed target while the two of you are on the same plane of existence. On your turn, you can use this link to issue commands to the target (no action required), such as "Attack that creature," "Move over there," or "Fetch that object." The target does its best to obey on its turn. If it completes an order and doesn't receive further direction from you, it acts and moves as it likes, focusing on protecting itself.
			<br>
			You can command the target to take a Reaction but must take your own Reaction to do so.
			<br>
			<b>Using a Higher-Level Spell Slot.</b> Your Concentration can last longer with a spell slot of level 6 (up to 10 minutes), 7 (up to 1 hour), or 8+ (up to 8 hours).
			""")
	ModifyMemory = Spell("Modify Memory",
			level= 5,
			school="Enchantment",
			casting_time="Action",
			ranges = "30 feet",
			components = "Verbal, Somatic",
			concentration = "Concentration",
			duration = "1 minute",
			definition = """
				You attempt to reshape another creature's memories. One creature that you can see within range makes a Wisdom saving throw. If you are fighting the creature, it has Advantage on the save. On a failed save, the target has the Charmed condition for the duration. While Charmed in this way, the target also has the Incapacitated condition and is unaware of its surroundings, though it can hear you. If it takes any damage or is targeted by another spell, this spell ends, and no memories are modified.
				<br>
				While this charm lasts, you can affect the target's memory of an event that it experienced within the last 24 hours and that lasted no more than 10 minutes. You can permanently eliminate all memory of the event, allow the target to recall the event with perfect clarity, change its memory of the event's details, or create a memory of some other event.
				<br>
				You must speak to the target to describe how its memories are affected, and it must be able to understand your language for the modified memories to take root. Its mind fills in any gaps in the details of your description. If the spell ends before you finish describing the modified memories, the creature's memory isn't altered. Otherwise, the modified memories take hold when the spell ends.
				<br>
				A modified memory doesn't necessarily affect how a creature behaves, particularly if the memory contradicts the creature's natural inclinations, alignment, or beliefs. An illogical modified memory, such as a false memory of how much the creature enjoyed swimming in acid, is dismissed as a bad dream. The DM might deem a modified memory too nonsensical to affect a creature.
				<br>
				A Remove Curse or Greater Restoration spell cast on the target restores the creature's true memory.
				<br>
				Using a Higher-Level Spell Slot. You can alter the target's memories of an event that took place up to 7 days ago (level 6 spell slot), 30 days ago (level 7 spell slot), 365 days ago (level 8 spell slot), or any time in the creature's past (level 9 spell slot).
				""")
	RarysTelepathicBond = Spell("Rary's Telepathic Bond",
			level= 5,
			school="Divination",
			casting_time="Action or Ritual",
			ranges = "30 feet",
			components = "Verbal, Somatic, Material(two eggs)",
			concentration = "Concentration",
			duration = "1 hour",
			definition = """
			You forge a telepathic link among up to eight willing creatures of your choice within range, psychically linking each creature to all the others for the duration. Creatures that can't communicate in any languages aren't affected by this spell.
			<br>
			Until the spell ends, the targets can communicate telepathically through the bond whether or not they share a language. The communication is possible over any distance, though it can't extend to other planes of existence.
			""")
	MassCureWounds = Spell("Mass Cure Wounds",
				level= 5,
				school="Abjuration",
				casting_time="Action",
				ranges = "60 feet",
				components = "Verbal, Somatic",
				concentration = "",
				duration = "Instantaneous",
				definition = """
				A wave of healing energy washes out from a point you can see within range. Choose up to six creatures in a 30-foot-radius Sphere centered on that point. Each target regains Hit Points equal to 5d8 plus your spellcasting ability modifier.
				<br>
				<b>Using a Higher-Level Spell Slot.</b> The healing increases by 1d8 for each spell slot level above 5.
				""")
	Mislead = Spell("Mislead",
		level= 5,
		school="Illusion",
		casting_time="Action",
		ranges = "Self",
		components = "Somatic",
		concentration = "Concentration",
		duration = "1 hour",
		definition = """
		You gain the Invisible condition at the same time that an illusory double of you appears where you are standing. The double lasts for the duration, but the invisibility ends immediately after you make an attack roll, deal damage, or cast a spell.
		<br>
		As a Magic action, you can move the illusory double up to twice your Speed and make it gesture, speak, and behave in whatever way you choose. It is intangible and invulnerable.
		<br>
		You can see through its eyes and hear through its ears as if you were located where it is.
		""")
	YolandeRegalPresence  = Spell("Yolande's Regal Presence",
		level= 5,
		school="Enchantment",
		casting_time="Action",
		ranges = "Self",
		components = "Verbal, Somatic, Material (a miniature tiara)",
		concentration = "Concentration",
		duration = "1 minute",
		definition = """
			You surround yourself with unearthly majesty in a 10-foot Emanation.
			Whenever the Emanation enters the space of a creature you can see
			and whenever a creature you can see enters the Emanation or ends
			its turn there, you can force that creature to make a Wisdom saving
			throw. On a failed save, the target takes 4d6 Psychic damage and
			has the Prone condition, and you can push it up to 10 feet away.
			On a successful save, the target takes half as much damage only.
			A creature makes this save only once per turn.
			""")
	WallStone = 	Spell("Wall of Stone",
		level= 5,
		school="Evocation",
		casting_time="Action",
		ranges = "120 feet",
		components = "Verbal, Somatic, Material (a cube of granite)",
		concentration = "Concentration",
		duration = "10 minutes",
		definition = """
		A nonmagical wall of solid stone springs into existence at a point you choose within range. The wall is 6 inches thick and is composed of ten 10-foot-by-10-foot panels. Each panel must be contiguous with another panel. Alternatively, you can create 10-foot-by-20-foot panels that are only 3 inches thick.
		<br>
		If the wall cuts through a creature's space when it appears, the creature is pushed to one side of the wall (you choose which side). If a creature would be surrounded on all sides by the wall (or the wall and another solid surface), that creature can make a Dexterity saving throw. On a success, it can use its Reaction to move up to its Speed so that it is no longer enclosed by the wall.
		<br>
		The wall can have any shape you desire, though it can't occupy the same space as a creature or object. The wall doesn't need to be vertical or rest on a firm foundation. It must, however, merge with and be solidly supported by existing stone. Thus, you can use this spell to bridge a chasm or create a ramp.
		<br>
		If you create a span greater than 20 feet in length, you must halve the size of each panel to create supports. You can crudely shape the wall to create battlements and the like.
		<br>
		The wall is an object made of stone that can be damaged and thus breached. Each panel has AC 15 and 30 Hit Points per inch of thickness, and it has Immunity to Poison and Psychic damage. Reducing a panel to 0 Hit Points destroys it and might cause connected panels to collapse at the DM's discretion.
		<br>
		If you maintain your Concentration on this spell for its full duration, the wall becomes permanent and can't be dispelled. Otherwise, the wall disappears when the spell ends.
		""")
	ConeCold = 	Spell("Cone of Cold",
		level= 5,
		school="Evocation",
		casting_time="Action",
		ranges = "Self",
		components = "Verbal, Somatic, Material (a small crystal or glass cone)",
		concentration = "",
		duration = "Instantaneous",
		definition = """
			You unleash a blast of cold air. Each creature in a 60-foot Cone originating from you makes a Constitution saving throw, taking 8d8 Cold damage on a failed save or half as much damage on a successful one. A creature killed by this spell becomes a frozen statue until it thaws.
			<br>
			Using a Higher-Level Spell Slot. The damage increases by 1d8 for each spell slot level above 5.
			""")
	Telekinesis = Spell("Telekinesis",
		level= 5,
		school="Transmutation",
		casting_time="Action",
		ranges = "60 feet",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		duration = "10 minutes",
		definition = """
You gain the ability to move or manipulate creatures or objects by thought.
When you cast the spell and as a Magic action on your later turns
before the spell ends, you can exert your will on one creature or
object that you can see within range, causing the appropriate effect
below. You can affect the same target round after round or choose a
new one at any time. If you switch targets, the prior target is no
longer affected by the spell.
<br>
<b>Creature.</b> You can try to move a Huge or smaller creature. The target must succeed on a Strength saving throw, or you move it up to 30 feet in any direction within the spell's range. Until the end of your next turn, the creature has the Restrained condition, and if you lift it into the air, it is suspended there. It falls at the end of your next turn unless you use this option on it again and it fails the save.
<br>
<b>Object.</b> You can try to move a Huge or smaller object. If the object isn't being worn or carried, you automatically move it up to 30 feet in any direction within the spell's range.
<br>
If the object is worn or carried by a creature, that creature must succeed on a Strength saving throw, or you pull the object away and move it up to 30 feet in any direction within the spell's range.
<br>
You can exert fine control on objects with your telekinetic grip, such as manipulating a simple tool, opening a door or a container, stowing or retrieving an item from an open container, or pouring the contents from a vial.
			""")

# Define sixth-level spells
LEVEL6 = True
if LEVEL6:
	Countercharm = spell_from_data("Countercharm")
	Heal = spell_from_data("Heal")
	IrresistibleDance = spell_from_data("Otto’s Irresistible Dance")
	MassSuggestion = spell_from_data("Mass Suggestion")
	ProgrammedIllusion = spell_from_data("Programmed Illusion")
	TrueSeeing = spell_from_data("True Seeing")
	WindWalk = spell_from_data("Wind Walk")
	BladeBarrier = Spell("Blade Barrier", 6, "Evocation", "1 Action", "90 feet", "Concentration, up to 10 minutes", "Verbal, Somatic")
	BonesEarth = Spell("Bones of the Earth", 6, "Transmutation", "1 Action", "120 feet", "Instantaneous", "Verbal, Somatic")
	BonesofEarth = BonesEarth
	CircleofDeath = Spell("Circle of Death", 6, "Necromancy", "1 Action", "150 feet", "Instantaneous", "Verbal, Somatic, Material")

	ConjureFey = Spell("Conjure Fey", 6, "Conjuration", "1 Action", "90 feet", "Concentration, up to 1 hour", "Verbal, Somatic")
	Contingency = Spell("Contingency", 6, "Evocation", "10 Minutes", "Self", "10 days", "Verbal, Somatic, Material")
	CreateHomunculus = Spell("Create Homunculus", 6, "Transmutation", "1 Hour", "120 feet", "Instantaneous", "Verbal, Somatic, Material")
	CreateUndead = Spell("Create Undead", 6, "Necromancy", "1 Minute", "10 feet", "Instantaneous", "Verbal, Somatic, Material")
	Disintegrate = Spell("Disintegrate", 6, "Transmutation", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic, Material")
	DrawmijInstantSummons = Spell("Drawmij's Instant Summons", 6, "Conjuration", "1 Minute R", "Touch", "Until dispelled", "Verbal, Somatic, Material")
	FizbanPlatinumShield = Spell("Fizban's Platinum Shield", 6, "Abjuration", "1 Bonus Action", "60ft", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Forbiddance = Spell("Forbiddance", 6, "Abjuration", "10 Minutes R", "Touch", "1 day", "Verbal, Somatic, Material")
	GlobeInvulnerability = Spell("Globe of Invulnerability", 6, "Abjuration", "1 Action", "Self (10-foot radius)", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	GlobeofInvulnerability = GlobeInvulnerability
	GravityFissure = Spell("Gravity Fissure", 6, "Evocation DG", "1 Action", "Self (100-foot line)", "Instantaneous", "Verbal, Somatic, Material")
	Harm = Spell("Harm", 6, "Necromancy", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic")
	InvestitureFlame = Spell("Investiture of Flame", 6, "Transmutation", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic")
	InvestitureIce = Spell("Investiture of Ice", 6, "Transmutation", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic")
	InvestitureStone = Spell("Investiture of Stone", 6, "Transmutation", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic")
	MagicJar = Spell("Magic Jar", 6, "Necromancy", "1 Minute", "Self", "Until dispelled", "Verbal, Somatic, Material")
	MentalPrison = Spell("Mental Prison", 6, "Illusion", "1 Action", "60 feet", "Concentration, up to 1 minute", "Somatic")
	MoveEarth = Spell("Move Earth", 6, "Transmutation", "1 Action", "120 feet", "Concentration, up to 2 hours", "Verbal, Somatic, Material")
	OtilukeFreezingSphere = Spell("Otiluke's Freezing Sphere", 6, "Evocation", "1 Action", "300 feet", "Instantaneous", "Verbal, Somatic, Material")
	PlanarAlly = Spell("Planar Ally", 6, "Conjuration", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic")
	PrimordialWard = Spell("Primordial Ward", 6, "Abjuration", "1 Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic")
	Scatter = Spell("Scatter", 6, "Conjuration", "1 Action", "30 feet", "Instantaneous", "Verbal")
	SoulCage = Spell("Soul Cage", 6, "Necromancy", "Special", "60 feet", "8 hours", "Verbal, Somatic, Material")
	SummonFiend = Spell("Summon Fiend", 6, "Conjuration", "1 Action", "90 feet", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	TashaOtherworldlyGuise = Spell("Tasha's Otherworldly Guise", 6, "Transmutation", "1 Bonus Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	TenserTransformation = Spell("Tenser's Transformation", 6, "Transmutation", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	WallIce = Spell("Wall of Ice", 6, "Evocation", "1 Action", "120 feet", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	WidogastTransmogrification = Spell("Widogast's Transmogrification (HB)", 6, "Transmutation", "1 hour", "Touch", "Instantaneous", "Verbal, Somatic, Material")
	WordRecall = Spell("Word of Recall", 6, "Conjuration", "1 Action", "5 feet", "Instantaneous", "Verbal")
	WordofRecall = WordRecall
	ChainLightning = Spell("Chain Lightning", 6, "Evocation", "1 Action", "150 feet", "Instantaneous", "Verbal, Somatic, Material")
	WallThorns = Spell("Wall of Thorns", 6, "Conjuration", "1 Action", "120 feet", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	DruidGrove = Spell("Druid Grove", 6, "Abjuration", "10 Minutes", "Touch", "24 hours", "Verbal, Somatic, Material")
	TransportviaPlants = Spell("Transport via Plants", 6, "Conjuration", "1 Action", "10 feet", "1 round", "Verbal, Somatic")
	Sunbeam = Spell("Sunbeam", 6, "Evocation", "1 Action", "Self (60-foot line)", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Countercharm = spell_from_data("Countercharm")
	HeroesFeast = spell_from_data("Heroes’ Feast")
	Heal = spell_from_data("Heal")
	IrresistibleDance = spell_from_data("Otto’s Irresistible Dance")
	MassSuggestion = spell_from_data("Mass Suggestion")
	ProgrammedIllusion = spell_from_data("Programmed Illusion")
	TrueSeeing = spell_from_data("True Seeing")
	WindWalk = spell_from_data("Wind Walk")
	BladeBarrier = Spell("Blade Barrier", 6, "Evocation", "1 Action", "90 feet", "Concentration, up to 10 minutes", "Verbal, Somatic")
	BonesEarth = Spell("Bones of the Earth", 6, "Transmutation", "1 Action", "120 feet", "Instantaneous", "Verbal, Somatic")
	CircleofDeath = Spell("Circle of Death", 6, "Necromancy", "1 Action", "150 feet", "Instantaneous", "Verbal, Somatic, Material")
	ConjureFey = Spell("Conjure Fey", 6, "Conjuration", "1 Action", "90 feet", "Concentration, up to 1 hour", "Verbal, Somatic")
	Contingency = Spell("Contingency", 6, "Evocation", "10 Minutes", "Self", "10 days", "Verbal, Somatic, Material")
	CreateHomunculus = Spell("Create Homunculus", 6, "Transmutation", "1 Hour", "120 feet", "Instantaneous", "Verbal, Somatic, Material")
	CreateUndead = Spell("Create Undead", 6, "Necromancy", "1 Minute", "10 feet", "Instantaneous", "Verbal, Somatic, Material")
	Disintegrate = Spell("Disintegrate", 6, "Transmutation", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic, Material")
	DrawmijInstantSummons = Spell("Drawmij's Instant Summons", 6, "Conjuration", "1 Minute R", "Touch", "Until dispelled", "Verbal, Somatic, Material")
	FizbanPlatinumShield = Spell("Fizban's Platinum Shield", 6, "Abjuration", "1 Bonus Action", "60ft", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Forbiddance = Spell("Forbiddance", 6, "Abjuration", "10 Minutes R", "Touch", "1 day", "Verbal, Somatic, Material")
	GlobeInvulnerability = Spell("Globe of Invulnerability", 6, "Abjuration", "1 Action", "Self (10-foot radius)", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	GravityFissure = Spell("Gravity Fissure", 6, "Evocation DG", "1 Action", "Self (100-foot line)", "Instantaneous", "Verbal, Somatic, Material")
	Harm = Spell("Harm", 6, "Necromancy", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic")
	InvestitureFlame = Spell("Investiture of Flame", 6, "Transmutation", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic")
	InvestitureofFlame = InvestitureFlame
	InvestitureIce = Spell("Investiture of Ice", 6, "Transmutation", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic")
	InvestitureStone = Spell("Investiture of Stone", 6, "Transmutation", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic")
	MagicJar = Spell("Magic Jar", 6, "Necromancy", "1 Minute", "Self", "Until dispelled", "Verbal, Somatic, Material")
	MentalPrison = Spell("Mental Prison", 6, "Illusion", "1 Action", "60 feet", "Concentration, up to 1 minute", "Somatic")
	MoveEarth = Spell("Move Earth", 6, "Transmutation", "1 Action", "120 feet", "Concentration, up to 2 hours", "Verbal, Somatic, Material")
	OtilukeFreezingSphere = Spell("Otiluke's Freezing Sphere", 6, "Evocation", "1 Action", "300 feet", "Instantaneous", "Verbal, Somatic, Material")
	PlanarAlly = Spell("Planar Ally", 6, "Conjuration", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic")
	PrimordialWard = Spell("Primordial Ward", 6, "Abjuration", "1 Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic")
	Scatter = Spell("Scatter", 6, "Conjuration", "1 Action", "30 feet", "Instantaneous", "Verbal")
	SoulCage = Spell("Soul Cage", 6, "Necromancy", "Special", "60 feet", "8 hours", "Verbal, Somatic, Material")
	SummonFiend = Spell("Summon Fiend", 6, "Conjuration", "1 Action", "90 feet", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	TashaOtherworldlyGuise = Spell("Tasha's Otherworldly Guise", 6, "Transmutation", "1 Bonus Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	TenserTransformation = Spell("Tenser's Transformation", 6, "Transmutation", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	WallIce = Spell("Wall of Ice", 6, "Evocation", "1 Action", "120 feet", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	WidogastTransmogrification = Spell("Widogast's Transmogrification (HB)", 6, "Transmutation", "1 hour", "Touch", "Instantaneous", "Verbal, Somatic, Material")
	WordRecall = Spell("Word of Recall", 6, "Conjuration", "1 Action", "5 feet", "Instantaneous", "Verbal")
	ChainLightning = Spell("Chain Lightning", 6, "Evocation", "1 Action", "150 feet", "Instantaneous", "Verbal, Somatic, Material")
	WallThorns = Spell("Wall of Thorns", 6, "Conjuration", "1 Action", "120 feet", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	DruidGrove = Spell("Druid Grove", 6, "Abjuration", "10 Minutes", "Touch", "24 hours", "Verbal, Somatic, Material")
	TransportviaPlants = Spell("Transport via Plants", 6, "Conjuration", "1 Action", "10 feet", "1 round", "Verbal, Somatic")
	Sunbeam = Spell("Sunbeam", 6, "Evocation", "1 Action", "Self (60-foot line)", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	TashasBubblingCauldron = Spell("Tasha's Bubbling Cauldron", 6, "Conjuration",
								"Action", "5 feet", "Instantaneous", "Verbal, Somatic, Material")


	Enslave = Spell(
		"Enslave",6,
		"Enchantment", "1 Action", "30 feet",
		"Until the caster dies or is on a different plane", "Verbal",
		definition = "The caster targets one creature it can see within 30 ft. of it. The target must succeed on a Wisdom saving throw or be magically charmed by the caster until the caster dies or until it is on a different plane of existence from the target. The charmed target is under the caster's control and can't take reactions, and the caster and the target can communicate telepathically with each other over any distance. Whenever the charmed target takes damage, the target can repeat the saving throw. On a success, the effect ends. No more than once every 24 hours, the target can also repeat the saving throw when it is at least 1 mile away from the caster.")
	FindthePath = Spell("Find the Path",
		level=6,
		school="Divination",
		casting_time="1 Minute",
		ranges = "Self",
		components = "Verbal, Somatic, Material (a set of divination tools—such as cards or runes—worth 100+ GP)",
		concentration = "Concentration",
		duration = "1 day",
		definition = """
		You magically sense the most direct physical route to a location you name. You must be familiar with the location, and the spell fails if you name a destination on another plane of existence, a moving destination (such as a mobile fortress), or an unspecific destination (such as "a green dragon's lair").
		<br>
		For the duration, as long as you are on the same plane of existence as the destination, you know how far it is and in what direction it lies. Whenever you face a choice of paths along the way there, you know which path is the most direct.
		""")
	Eyebite = Spell("Eyebite",
		level=6,
		school="Necromancy",
		casting_time="Action",
		ranges = "Self",
		duration = "1 minute",
		components = "Verbal, Somatic",
		concentration = "Concentration",
		definition = """
		For the duration, your eyes become an inky void. One creature of your choice within 60 feet of you that you can see must succeed on a Wisdom saving throw or be affected by one of the following effects of your choice for the duration.
		<br>
		On each of your turns until the spell ends, you can take a Magic action to target another creature but can't target a creature again if it has succeeded on a save against this casting of the spell.
		<br>
		<b>Asleep.</b> The target has the <i>Unconscious</i> condition. It wakes up if it takes any damage or if another creature takes an action to shake it awake.
		<br>
		<b>Panicked.</b> The target has the <i>Frightened</i> condition. On each of its turns, the Frightened target must take the Dash action and move away from you by the safest and shortest route available. If the target moves to a space at least 60 feet away from you where it can't see you, this effect ends.
		<br>
		<b>Sickened.</b> The target has the <i>Poisoned</i> condition.
			"""
			)
	HeroesFeast = Spell("Heroes' Feast",
		level=6,
		school="Conjuration",
		casting_time="10 Minutes",
		ranges = "Self",
		components = "Verbal, Somatic, Material (a gem-encrusted bowl worth 1,000+ GP, which the spell consumes)",
		concentration = "",
		duration = "Instantaneous",
		definition = """
You conjure a feast that appears on a surface in an unoccupied 10-foot Cube next to you. The feast takes 1 hour to consume and disappears at the end of that time, and the beneficial effects don't set in until this hour is over. Up to twelve creatures can partake of the feast.
<br>
A creature that partakes gains several benefits, which last for 24 hours. The creature has Resistance to Poison damage, and it has Immunity to the Frightened and Poisoned conditions. Its Hit Point maximum also increases by 2d10, and it gains the same number of Hit Points.
		"""
		)
	GuardsandWards = Spell("Guards and Wards",
	level=6,
	school="Abjuration",
	casting_time="1 hour",
	ranges = "Touch",
	components = "Verbal, Somatic, Material (a silver rod worth 10+ GP)",
	concentration = "",
	duration = "24 hours",
	definition = """
	You create a ward that protects up to 2,500 square feet of floor space.
	The warded area can be up to 20 feet tall, and you shape it as one
	50-foot square, one hundred 5-foot squares that are contiguous, or
	twenty-five 10-foot squares that are contiguous.
	<br>
	When you cast this spell, you can specify individuals that are
	unaffected by the spell's effects. You can also specify a password
	that, when spoken aloud within 5 feet of the warded area, makes
	the speaker immune to its effects.
	<br>
	The spell creates the effects below within the warded area.
	Dispel Magic has no effect on Guards and Wards itself, but each
	of the following effects can be dispelled. If all four are
	dispelled, Guards and Wards ends. If you cast the spell every
	day for 365 days on the same area, the spell thereafter lasts
	until all its effects are dispelled.
	<ul style="list-style-type: '🛡️'; text-align: left; ">
	<li><b>Corridors.</b> Fog fills all the warded corridors, making them Heavily Obscured. In addition, at each intersection or branching passage offering a choice of direction, there is a 50 percent chance that a creature other than you believes it is going in the opposite direction from the one it chooses.</li>
	<li><b>Doors.</b> All doors in the warded area are magically locked, as if sealed by the Arcane Lock spell. In addition, you can cover up to ten doors with an illusion to make them appear as plain sections of wall.</li>
	<li><b>Stairs.</b> Webs fill all stairs in the warded area from top to bottom, as in the Web spell. These strands regrow in 10 minutes if they are destroyed while Guards and Wards lasts.</li>
	<b>Other Spell Effect:</b>
	<li>Dancing Lights in four corridors, with a simple program that the lights repeat as long as Guards and Wards lasts.</li>
	<li>Magic Mouth in two locations.</li>
	<li>Stinking Cloud in two locations (the vapors return within 10 minutes if dispersed while Guards and Wards lasts)</li>
	<li>Gust of Wind in one corridor or room (the wind blows continuously while the spell lasts)</li>
	<li>Suggestion in one 5-foot square; any creature that enters that square receives the suggestion mentally</li>
	</ul>

	""")
	ArcaneGate = Spell("Arcane Gate",
	level=6,
	school="Conjuration",
	casting_time="Action",
	ranges = "500 feet",
	components = "Verbal, Somatic",
	concentration = "Concentration",
	duration = "10 minutes",
	definition = """
		You create linked teleportation portals. Choose two Large, unoccupied spaces on the ground that you can see, one space within range and the other one within 10 feet of you. A circular portal opens in each of those spaces and remains for the duration.
		<br>
		The portals are two-dimensional glowing rings filled with mist that blocks sight. They hover inches from the ground and are perpendicular to it.
		<br>
		A portal is open on only one side (you choose which). Anything entering the open side of a portal exits from the open side of the other portal as if the two were adjacent to each other. As a Bonus Action, you can change the facing of the open sides.
		""")
	FleshtoStone = Spell("Flesh to Stone",
		level=6,
		school="Transmutation",
		casting_time="Action",
		ranges = "60 feet",
		components = "Verbal, Somatic, Material (a cockatrice feather)",
		concentration = "Concentration",
		duration = "1 minute",
		definition = """
		You attempt to turn one creature that you can see within range into stone. The target makes a Constitution saving throw. On a failed save, it has the Restrained condition for the duration. On a successful save, its Speed is 0 until the start of your next turn. Constructs automatically succeed on the save.
		<br>
		A Restrained target makes another Constitution saving throw at the end of each of its turns. If it successfully saves against this spell three times, the spell ends. If it fails its saves three times, it is turned to stone and has the Petrified condition for the duration. The successes and failures needn't be consecutive; keep track of both until the target collects three of a kind.
		<br>
		If you maintain your Concentration on this spell for the entire possible duration, the target is Petrified until the condition is ended by Greater Restoration or similar magic.
		""")
	InvestitureWind = Spell("Investiture of Wind",
		level=6,
		school="Transmutation",
		casting_time="Action",
		ranges = "Self",
		components = "Verbal, Somatic.",
		concentration = "Concentration",
		duration = "10 minutes",
		definition = """
		Until the spell ends, wind whirls around you, and you gain the following benefits:
		 <ul style="list-style-type: '🌪️'; text-align: left; ">
			<li>Ranged weapon attacks made against you have disadvantage on the attack roll.</li>
			<li>You gain a flying speed of 60 feet. If you are still flying when the spell ends, you fall, unless you can somehow prevent it.</li>
			<li>You can use your action to create a 15-foot cube of swirling wind centered on a point you can see within 60 feet of you. Each creature in that area must make a Constitution saving throw. A creature takes 2d10 bludgeoning damage on a failed save, or half as much damage on a successful one. If a Large or smaller creature fails the save, that creature is also pushed up to 10 feet away from the center of the cube.</li>
			</ul>
			""")

# Define seventh-level spells
LEVEL7 = True
if LEVEL7:
	PowerWordFortify = spell_from_data("Power Word: Fortify")
	Symphony = spell_from_data("Symphony Of The Masked")
	FireStorm = spell_from_data("Fire Storm")
	Teleport = spell_from_data("Teleport")
	MagnificentMansion = spell_from_data("Mordenkainen's Magnificent Mansion")
	CreateMagen = Spell("Create Magen", 7, "Transmutation", "1 Hour", "Touch", "Instantaneous", "Verbal, Somatic, Material")
	DelayedBlastFireball = Spell("Delayed Blast Fireball", 7, "Evocation", "1 Action", "150 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	DreamOfTheBlueVeil = Spell("Dream of the Blue Veil", 7, "Conjuration", "10 minutes", "20 feet", "6 hours", "Verbal, Somatic, Material")
	FingerDeath = Spell("Finger of Death", 7, "Necromancy", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic")
	FingerofDeath = FingerDeath
	Forcecage = Spell("Forcecage", 7, "Evocation", "1 Action", "100 feet", "1 hour", "Verbal, Somatic, Material")
	MagnificentMansion = Spell("Mordenkainen's Magnificent Mansion", 7, "Conjuration", "1 Minute", "300 feet", "24 hours", "Verbal, Somatic, Material")
	MordenkainenSword = Spell("Mordenkainen's Sword", 7, "Evocation", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	PlaneShift = Spell("Plane Shift", 7, "Conjuration", "1 Action", "Touch", "Instantaneous", "Verbal, Somatic, Material")
	PowerWordPain = Spell("Power Word: Pain", 7, "Enchantment", "1 Action", "60 feet", "Instantaneous", "Verbal")
	ReverseGravity = Spell("Reverse Gravity", 7, "Transmutation", "1 Action", "100 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Sequester = Spell("Sequester", 7, "Transmutation", "1 Action", "Touch", "Until dispelled", "Verbal, Somatic, Material")
	Simulacrum = Spell("Simulacrum", 7, "Illusion", "12 hours", "Touch", "Until dispelled", "Verbal, Somatic, Material")
	Teleport = Spell("Teleport", 7, "Conjuration", "1 Action", "10 feet", "Instantaneous", "Verbal")
	TempleOfTheGods = Spell("Temple of the Gods", 7, "Conjuration", "1 hour", "120 feet", "24 hours", "Verbal, Somatic, Material")
	TetherEssence = Spell("Tether Essence", 7, "Necromancy D", "1 Action", "60 feet", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	DraconicTransformation = Spell("Draconic Transformation", 7, "Transmutation", "1 Bonus Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	ConjureCelestial = Spell("Conjure Celestial", 7, "Conjuration", "1 Minute", "90 feet", "Concentration, up to 1 hour", "Verbal, Somatic")
	Whirlwind = 	Spell("Whirlwind", 7, "Evocation", "1 Action", "300 feet", "Concentration, up to 1 minute", "Verbal, Material")
	Regenerate = Spell("Regenerate", 7, "Transmutation", "1 Minute", "Touch", "1 hour", "Verbal, Somatic, Material")
	CrownofStars = Spell("Crown of Stars", 7, "Evocation", "1 Action", "Self", "1 hour", "Verbal, Somatic")
	DivineWord = Spell("Divine Word", 7, "Evocation", "1 Bonus Action", "30 feet", "Instantaneous", "Verbal")
	Symphony = spell_from_data("Symphony Of The Masked")
	FireStorm = spell_from_data("Fire Storm")
	Teleport = spell_from_data("Teleport")
	MagnificentMansion = spell_from_data("Mordenkainen's Magnificent Mansion")
	CreateMagen = Spell("Create Magen", 7, "Transmutation", "1 Hour", "Touch", "Instantaneous", "Verbal, Somatic, Material")
	DelayedBlastFireball = Spell("Delayed Blast Fireball", 7, "Evocation", "1 Action", "150 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	DreamOfTheBlueVeil = Spell("Dream of the Blue Veil", 7, "Conjuration", "10 minutes", "20 feet", "6 hours", "Verbal, Somatic, Material")
	FingerDeath = Spell("Finger of Death", 7, "Necromancy", "1 Action", "60 feet", "Instantaneous", "Verbal, Somatic")
	Forcecage = Spell("Forcecage", 7, "Evocation", "1 Action", "100 feet", "1 hour", "Verbal, Somatic, Material")
	MagnificentMansion = Spell("Mordenkainen's Magnificent Mansion", 7, "Conjuration", "1 Minute", "300 feet", "24 hours", "Verbal, Somatic, Material")
	MordenkainenSword = Spell("Mordenkainen's Sword", 7, "Evocation", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	PlaneShift = Spell("Plane Shift", 7, "Conjuration", "1 Action", "Touch", "Instantaneous", "Verbal, Somatic, Material")
	PowerWordPain = Spell("Power Word: Pain", 7, "Enchantment", "1 Action", "60 feet", "Instantaneous", "Verbal")
	ProjectImage = Spell("Project Image", 7, "Illusion", "1 Action", "500 Miles", "Concentration, up to 1 day", "Verbal, Somatic, Material")
	ReverseGravity = Spell("Reverse Gravity", 7, "Transmutation", "1 Action", "100 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Sequester = Spell("Sequester", 7, "Transmutation", "1 Action", "Touch", "Until dispelled", "Verbal, Somatic, Material")
	Simulacrum = Spell("Simulacrum", 7, "Illusion", "12 hours", "Touch", "Until dispelled", "Verbal, Somatic, Material")
	Teleport = Spell("Teleport", 7, "Conjuration", "1 Action", "10 feet", "Instantaneous", "Verbal")
	TempleOfTheGods = Spell("Temple of the Gods", 7, "Conjuration", "1 hour", "120 feet", "24 hours", "Verbal, Somatic, Material")
	TetherEssence = Spell("Tether Essence", 7, "Necromancy D", "1 Action", "60 feet", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	DraconicTransformation = Spell("Draconic Transformation", 7, "Transmutation", "1 Bonus Action", "Self", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	ConjureCelestial = Spell("Conjure Celestial", 7, "Conjuration", "1 Minute", "90 feet", "Concentration, up to 1 hour", "Verbal, Somatic")
	Whirlwind = Spell("Whirlwind", 7, "Evocation", "1 Action", "300 feet", "Concentration, up to 1 minute", "Verbal, Material")
	Regenerate = Spell("Regenerate", 7, "Transmutation", "1 Minute", "Touch", "1 hour", "Verbal, Somatic, Material")
	CrownofStars = Spell("Crown of Stars", 7, "Evocation", "1 Action", "Self", "1 hour", "Verbal, Somatic")
	DivineWord = Spell("Divine Word", 7, "Evocation", "1 Bonus Action", "30 feet", "Instantaneous", "Verbal")
	Resurrection = Spell("Resurrection",
		level=7,
		school="Necromancy",
		casting_time="1 Hour",
		ranges = "Touch",
		duration = "Instantaneous",
		components = "Verbal, Somatic, Material(a diamond worth 1,000+ GP, which the spell consumes)",
		concentration = "",
		definition = """
		With a touch, you revive a dead creature that has been dead for no more than a century, didn't die of old age, and wasn't Undead when it died.
		<br>
		The creature returns to life with all its Hit Points. This spell also neutralizes any poisons that affected the creature at the time of death. This spell closes all mortal wounds and restores any missing body parts.
		<br>
		Coming back from the dead is an ordeal. The target takes a -4 penalty to D20 Tests. Every time the target finishes a Long Rest, the penalty is reduced by 1 until it becomes 0.
		<br>
		Casting this spell to revive a creature that has been dead for 365 days or longer taxes you. Until you finish a Long Rest, you can't cast spells again, and you have Disadvantage on D20 Tests.
		""")
	Symbol = Spell("Symbol",
		level=7,
		school="Abjuration",
		casting_time="1 Minute",
		ranges = "Touch",
		duration = "Until dispelled or triggered (powdered diamond worth 1,000+ GP, which the spell consumes)",
		components = "Verbal, Somatic, Material",
		concentration = "",
		definition = """
You inscribe a harmful glyph either on a surface (such as a section of floor or wall) or within an object that can be closed (such as a book or chest). The glyph can cover an area no larger than 10 feet in diameter. If you choose an object, it must remain in place; if it is moved more than 10 feet from where you cast this spell, the glyph is broken, and the spell ends without being triggered.
<br>
The glyph is nearly imperceptible and requires a successful Wisdom (Perception) check against your spell save DC to notice.
<br>
When you inscribe the glyph, you set its trigger and choose which effect the symbol bears: Death, Discord, Fear, Pain, Sleep, or Stunning. Each one is explained below.
<br>
Set the Trigger. You decide what triggers the glyph when you cast the spell. For glyphs inscribed on a surface, common triggers include touching or stepping on the glyph, removing another object covering it, or approaching within a certain distance of it. For glyphs inscribed within an object, common triggers include opening that object or seeing the glyph.
<br>
You can refine the trigger so that only creatures of certain types activate it (for example, the glyph could be set to affect Aberrations). You can also set conditions for creatures that don't trigger the glyph, such as those who say a certain password.
<br>
Once triggered, the glyph glows, filling a 60-foot-radius Sphere with Dim Light for 10 minutes, after which time the spell ends. Each creature in the Sphere when the glyph activates is targeted by its effect, as is a creature that enters the Sphere for the first time on a turn or ends its turn there. A creature is targeted only once per turn.
<br>
Death. Each target makes a Constitution saving throw, taking 10d10 Necrotic damage on a failed save or half as much damage on a successful save.
<br>
Discord. Each target makes a Wisdom saving throw. On a failed save, a target argues with other creatures for 1 minute. During this time, it is incapable of meaningful communication and has Disadvantage on attack rolls and ability checks.
<br>
Fear. Each target must succeed on a Wisdom saving throw or have the Frightened condition for 1 minute. While Frightened, the target must move at least 30 feet away from the glyph on each of its turns, if able.
<br>
Pain. Each target must succeed on a Constitution saving throw or have the Incapacitated condition for 1 minute.
<br>
Sleep. Each target must succeed on a Wisdom saving throw or have the Unconscious condition for 10 minutes. A creature awakens if it takes damage or if someone takes an action to shake it awake.
<br>
Stunning. Each target must succeed on a Wisdom saving throw or have the Stunned condition for 1 minute.
		"""
		)
	Etherealness = Spell("Etherealness",
		level=7,
		school="Conjuration",
		casting_time="Action",
		ranges = "Self",
		duration = "8 hours",
		components = "Verbal, Somatic",
		concentration = "",
		definition = """
		You step into the border regions of the Ethereal Plane, where it overlaps with your current plane. You remain in the Border Ethereal for the duration. During this time, you can move in any direction. If you move up or down, every foot of movement costs an extra foot. You can perceive the plane you left, which looks gray, and you can't see anything there more than 60 feet away.
		<br>
While on the Ethereal Plane, you can affect and be affected only by creatures, objects, and effects on that plane. Creatures that aren't on the Ethereal Plane can't perceive or interact with you unless a feature gives them the ability to do so.
<br>
When the spell ends, you return to the plane you left in the spot that corresponds to your space in the Border Ethereal. If you appear in an occupied space, you are shunted to the nearest unoccupied space and take Force damage equal to twice the number of feet you are moved.
<br>
This spell ends instantly if you cast it while you are on the Ethereal Plane or a plane that doesn't border it, such as one of the Outer Planes.
<br>
<b>Using a Higher-Level Spell Slot.</b> You can target up to three willing creatures (including yourself) for each spell slot level above 7. The creatures must be within 10 feet of you when you cast the spell.
		""")
	ProjectImage = Spell("Project Image",
		level=7,
		school="Illusion",
		casting_time="Action",
		ranges = "500 Miles",
		components = "Verbal, Somatic, Material (a statuette of yourself worth 5+ GP)",
		concentration = "Concentration",
		duration = "1 day",
		definition = """
		You create an illusory copy of yourself that lasts for the duration. The copy can appear at any location within range that you have seen before, regardless of intervening obstacles. The illusion looks and sounds like you, but it is intangible. If the illusion takes any damage, it disappears, and the spell ends.
		<br>
		You can see through the illusion's eyes and hear through its ears as if you were in its space. As a Magic action, you can move it up to 60 feet and make it gesture, speak, and behave in whatever way you choose. It mimics your mannerisms perfectly.
		<br>
		Physical interaction with the image reveals it to be illusory, since things can pass through it. A creature that takes the Study action to examine the image can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the creature can see through the image, and any noise it makes sounds hollow to the creature.
		""")
	PrismaticSpray = Spell("Prismatic Spray",
		level=7,
		school="Evocation",
		casting_time="Action",
		ranges = "Self",
		components = "Verbal, Somatic",
		concentration = "",
		duration = "Instantaneous",
		definition = """
Eight rays of light flash from you in a 60-foot Cone. Each creature in the Cone makes a Dexterity saving throw. For each target, roll 1d8 to determine which color ray affects it, consulting the Prismatic Rays table.
 <table>
  <tr> <th>Prismatic Rays</th> </tr>
  <tr>	<th>1d8</th>		<th>Ray</th>	</tr>
  <tr>	<td>1</td>	<td>🔴 <b>Red.</b> Failed Save: 12d6 Fire damage. Successful Save: Half as much damage.</td>	</tr>
  <tr>	<td>2</td>	<td>🟠 <b>Orange.</b> Failed Save: 12d6 Acid damage. Successful Save: Half as much damage.</td>	</tr>
  <tr>	<td>3</td>	<td>🟡 <b>Yellow.</b> Failed Save: 12d6 Lightning damage. Successful Save: Half as much damage.</td>	</tr>
  <tr>	<td>4</td>	<td>🟢 <b>Green.</b> Failed Save: 12d6 Poison damage. Successful Save: Half as much damage.</td>	</tr>
  <tr>	<td>5</td>	<td>🔵 <b>Blue.</b> Failed Save: 12d6 Cold damage. Successful Save: Half as much damage.</td>	</tr>
  <tr>	<td>6</td>	<td>🟤 <b>Indigo.</b> Failed Save: The target has the Restrained condition and makes a Constitution saving throw at the end of each of its turns. If it successfully saves three times, the condition ends. If it fails three times, it has the Petrified condition until it is freed by an effect like the Greater Restoration spell. The successes and failures needn't be consecutive; keep track of both until the target collects three of a kind.</td>	</tr>
  <tr>	<td>7</td>	<td>🟣 <b>Violet.</b> Failed Save: The target has the Blinded condition and makes a Wisdom saving throw at the start of your next turn. On a successful save, the condition ends. On a failed save, the condition ends, and the creature teleports to another plane of existence (DM's choice).</td>	</tr>
  <tr>	<td>8</td>	<td>⚪️ <b>Special.</b> The target is struck by two rays. Roll twice, rerolling any 8.</td>	</tr>
</table>
		""")
	MirageArcane = Spell("Mirage Arcane",
		level=7,
		school="Illusion",
		casting_time="10 Minutes",
		ranges = "Sight",
		components = "Verbal, Somatic",
		concentration = "",
		duration = "10 days",
		definition = """
		You make terrain in an area up to 1 mile square look, sound, smell, and even feel like some other sort of terrain. Open fields or a road could be made to resemble a swamp, hill, crevasse, or some other rough or impassable terrain. A pond can be made to seem like a grassy meadow, a precipice like a gentle slope, or a rock-strewn gully like a wide and smooth road.
		<br>
Similarly, you can alter the appearance of structures or add them where none are present. The spell doesn't disguise, conceal, or add creatures.
<br>
The illusion includes audible, visual, tactile, and olfactory elements, so it can turn clear ground into Difficult Terrain (or vice versa) or otherwise impede movement through the area. Any piece of the illusory terrain (such as a rock or stick) that is removed from the spell's area disappears immediately.
<br>
Creatures with Truesight can see through the illusion to the terrain's true form; however, all other elements of the illusion remain, so while the creature is aware of the illusion's presence, the creature can still physically interact with the illusion.
		""")

# Define eighth-level spells
LEVEL8 = True
if LEVEL8:
	Foresight = spell_from_data("Foresight")
	Earthquake = spell_from_data("Earthquake")
	DominateMonster = spell_from_data("Dominate Monster")
	PowerWordStun = spell_from_data("Power Word Stun")
	Demiplane = spell_from_data("Demiplane")
	Feeblemind = spell_from_data("Feeblemind")
	Maze = spell_from_data("Maze")
	HorridWilting = Spell("Abi-Dalzim's Horrid Wilting", 8, "Necromancy", "1 Action", "150 feet", "Instantaneous", "Verbal, Somatic, Material")
	AnimalShapes = Spell("Animal Shapes", 8, "Transmutation", "1 Action", "30 feet", "Concentration, up to 24 hours", "Verbal, Somatic")
	AntipathySympathy = Spell("Antipathy/Sympathy", 8, "Enchantment", "1 Hour", "60 feet", "10 Days", "Verbal, Somatic, Material")
	Clone = Spell("Clone", 8, "Necromancy", "1 Hour", "Touch", "Instantaneous", "Verbal, Somatic, Material")
	DarkStar = Spell("Dark Star", 8, "Evocation DG", "1 Action", "150 Feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	IllusoryDragon = Spell("Illusory Dragon", 8, "Illusion", "1 Action", "120 feet", "Concentration, up to 1 minute", "Somatic")
	MaddeningDarkness = Spell("Maddening Darkness", 8, "Evocation", "1 Action", "150 feet", "Concentration, up to 10 minutes", "Verbal, Material")
	MightyFortress = Spell("Mighty Fortress", 8, "Conjuration", "1 Minute", "1 mile", "Instantaneous", "Verbal, Somatic, Material")
	RealityBreak = Spell("Reality Break", 8, "Conjuration DC", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Telepathy = Spell("Telepathy", 8, "Evocation", "1 Action", "Unlimited", "24 hours", "Verbal, Somatic, Material")
	ControlWeather = Spell("Control Weather", 8, "Transmutation", "10 Minutes", "Self (5 mile radius)", "Concentration, Up to 8 hours", "Verbal, Somatic, Material")
	Tsunami = Spell("Tsunami", 8, "Conjuration", "1 Action", "Sight", "Concentration, up to 6 rounds", "Verbal, Somatic")
	Sunburst = Spell("Sunburst", 8, "Evocation", "1 Action", "150 feet", "Instantaneous", "Verbal, Somatic, Material")
	AntimagicField = Spell("Antimagic Field", 8, "Abjuration", "1 Action", "Self (10-foot radius sphere)", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	Foresight = spell_from_data("Foresight")
	Earthquake = spell_from_data("Earthquake")
	DominateMonster = spell_from_data("Dominate Monster")
	PowerWordStun = spell_from_data("Power Word Stun")
	Demiplane = spell_from_data("Demiplane")
	Feeblemind = spell_from_data("Feeblemind")
	Maze = spell_from_data("Maze")
	HorridWilting = Spell("Abi-Dalzim's Horrid Wilting", 8, "Necromancy", "1 Action", "150 feet", "Instantaneous", "Verbal, Somatic, Material")
	AnimalShapes = Spell("Animal Shapes", 8, "Transmutation", "1 Action", "30 feet", "Concentration, up to 24 hours", "Verbal, Somatic")
	AntipathySympathy = Spell("Antipathy/Sympathy", 8, "Enchantment", "1 Hour", "60 feet", "10 Days", "Verbal, Somatic, Material")
	Clone = Spell("Clone", 8, "Necromancy", "1 Hour", "Touch", "Instantaneous", "Verbal, Somatic, Material")
	DarkStar = Spell("Dark Star", 8, "Evocation DG", "1 Action", "150 Feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	IllusoryDragon = Spell("Illusory Dragon", 8, "Illusion", "1 Action", "120 feet", "Concentration, up to 1 minute", "Somatic")
	MightyFortress = Spell("Mighty Fortress", 8, "Conjuration", "1 Minute", "1 mile", "Instantaneous", "Verbal, Somatic, Material")
	RealityBreak = Spell("Reality Break", 8, "Conjuration DC", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Telepathy = Spell("Telepathy", 8, "Evocation", "1 Action", "Unlimited", "24 hours", "Verbal, Somatic, Material")
	ControlWeather = Spell("Control Weather", 8, "Transmutation", "10 Minutes", "Self (5 mile radius)", "Concentration, Up to 8 hours", "Verbal, Somatic, Material")
	Tsunami = Spell("Tsunami", 8, "Conjuration", "1 Action", "Sight", "Concentration, up to 6 rounds", "Verbal, Somatic")
	Sunburst = Spell("Sunburst", 8, "Evocation", "1 Action", "150 feet", "Instantaneous", "Verbal, Somatic, Material")
	AntimagicField = Spell("Antimagic Field", 8, "Abjuration", "1 Action", "Self (10-foot radius sphere)", "Concentration, up to 1 hour", "Verbal, Somatic, Material")
	Befuddlement 	= Spell("Befuddlement",            8, "Enchantment",
								"Action", "150 feet", "Instantaneous", "Verbal, Somatic")

	IncendiaryCloud = Spell("Incendiary Cloud",
			level=8,
			school="Conjuration",
			casting_time="Action",
			ranges = "150 feet",
			duration = "1 minute",
			components = "Verbal, Somatic",
			concentration = "Concentration",
			definition = """
			A swirling cloud of embers and smoke fills a 20-foot-radius Sphere centered on a point within range. The cloud's area is Heavily Obscured. It lasts for the duration or until a strong wind (like that created by Gust of Wind) disperses it.
			<br>
			When the cloud appears, each creature in it makes a Dexterity saving throw, taking 10d8 Fire damage on a failed save or half as much damage on a successful one. A creature must also make this save when the Sphere moves into its space and when it enters the Sphere or ends its turn there. A creature makes this save only once per turn.
			<br>
			The cloud moves 10 feet away from you in a direction you choose at the start of each of your turns.
			"""
			)
	Glibness = Spell("Glibness",
			level=8,
			school="Enchantment",
			casting_time="Action",
			ranges = "Self",
			duration = "1 hour",
			components = "Verbal",
			concentration = "Concentration",
			definition = """
			Until the spell ends, when you make a Charisma check, you can replace the number you roll with a 15. Additionally, no matter what you say, magic that would determine if you are telling the truth indicates that you are being truthful.
			"""
			)
	MindBlank = Spell("Mind Blank",
		level=8,
		school="Abjuration",
		casting_time="Action",
		ranges = "Touch",
		components = "Verbal, Somatic",
		duration = "24 hours",
		concentration = "",
		definition = """
		Until the spell ends, one willing creature you touch has Immunity to Psychic damage and the Charmed condition. The target is also unaffected by anything that would sense its emotions or alignment, read its thoughts, or magically detect its location, and no spell—not even Wish—can gather information about the target, observe it remotely, or control its mind.
		"""
		)
	HolyAura = Spell("Holy Aura",
		level=8,
		school="Abjuration",
		casting_time="Action",
		ranges = "Self",
		components = "Verbal, Somatic, Material (a reliquary worth 1,000+ GP)",
		duration = "1 minute",
		concentration = "Concentration",
		definition = """
For the duration, you emit an aura in a 30-foot Emanation. While in the aura, creatures of your choice have Advantage on all saving throws, and other creatures have Disadvantage on attack rolls against them. In addition, when a Fiend or an Undead hits an affected creature with a melee attack roll, the attacker must succeed on a Constitution saving throw or have the Blinded condition until the end of its next turn.
		"""
		)


# Define ninth-level spells
LEVEL9 = True
if LEVEL9:
	MassPolymorph = spell_from_data("Mass Polymorph")
	Shapechange = spell_from_data("Shapechange")
	MassHeal = spell_from_data("Mass Heal")
	Weird = spell_from_data("Weird")
	TimeStop = spell_from_data("Time Stop")
	Foresight = spell_from_data("Foresight")
	AstralProjection = Spell("Astral Projection", 9, "Evocation", "1 Hour", "10 feet", "Special", "Verbal, Somatic, Material")
	BladeofDisaster = Spell("Blade of Disaster", 9, "Conjuration", "1 Bonus Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic")
	Gate = Spell("Gate", 9, "Conjuration", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Imprisonment = Spell("Imprisonment", 9, "Abjuration", "1 Minute", "30 feet", "Until dispelled", "Verbal, Somatic, Material")
	PowerWordHeal = Spell("Power Word: Heal", 9, "Evocation", "1 Action", "Touch", "Instantaneous", "Verbal, Somatic")
	PowerWordKill = Spell("Power Word: Kill", 9, "Enchantment", "1 Action", "60 feet", "Instantaneous", "Verbal")
	PrismaticWall = Spell("Prismatic Wall", 9, "Abjuration", "1 Action", "60 feet", "10 minutes", "Verbal, Somatic")
	PsychicScream = Spell("Psychic Scream", 9, "Enchantment", "1 Action", "90 feet", "Instantaneous", "Somatic")
	RavenousVoid = Spell("Ravenous Void", 9, "Evocation DG", "1 Action", "1,000 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	TimeRavage = Spell("Time Ravage", 9, "Necromancy DC", "1 Action", "90 feet", "Instantaneous", "Verbal, Somatic, Material")
	TrueResurrection = Spell("True Resurrection", 9, "Necromancy", "1 Hour", "Touch", "Instantaneous", "Verbal, Somatic, Material")
	StormofVengeance = Spell("Storm of Vengeance", 9, "Conjuration", "1 Action", "Sight", "Concentration up to 1 minute", "Verbal, Somatic")
	Invulnerability = Spell("Invulnerability", 9, "Abjuration", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	MassPolymorph = spell_from_data("Mass Polymorph")
	Shapechange = spell_from_data("Shapechange")
	MassHeal = spell_from_data("Mass Heal")
	Weird = spell_from_data("Weird")
	TimeStop = spell_from_data("Time Stop")
	Foresight = spell_from_data("Foresight")
	AstralProjection = Spell("Astral Projection", 9, "Evocation", "1 Hour", "10 feet", "Special", "Verbal, Somatic, Material")
	BladeofDisaster = Spell("Blade of Disaster", 9, "Conjuration", "1 Bonus Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic")
	Gate = Spell("Gate", 9, "Conjuration", "1 Action", "60 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	Imprisonment = Spell("Imprisonment", 9, "Abjuration", "1 Minute", "30 feet", "Until dispelled", "Verbal, Somatic, Material")
	PowerWordHeal = Spell("Power Word: Heal", 9, "Evocation", "1 Action", "Touch", "Instantaneous", "Verbal, Somatic")
	PowerWordKill = Spell("Power Word: Kill", 9, "Enchantment", "1 Action", "60 feet", "Instantaneous", "Verbal")
	PrismaticWall = Spell("Prismatic Wall", 9, "Abjuration", "1 Action", "60 feet", "10 minutes", "Verbal, Somatic")
	PsychicScream = Spell("Psychic Scream", 9, "Enchantment", "1 Action", "90 feet", "Instantaneous", "Somatic")
	RavenousVoid = Spell("Ravenous Void", 9, "Evocation DG", "1 Action", "1,000 feet", "Concentration, up to 1 minute", "Verbal, Somatic, Material")
	TimeRavage = Spell("Time Ravage", 9, "Necromancy DC", "1 Action", "90 feet", "Instantaneous", "Verbal, Somatic, Material")
	TrueResurrection = Spell("True Resurrection", 9, "Necromancy", "1 Hour", "Touch", "Instantaneous", "Verbal, Somatic, Material")
	StormofVengeance = Spell("Storm of Vengeance", 9, "Conjuration", "1 Action", "Sight", "Concentration up to 1 minute", "Verbal, Somatic")
	Invulnerability = Spell("Invulnerability", 9, "Abjuration", "1 Action", "Self", "Concentration, up to 10 minutes", "Verbal, Somatic, Material")
	MeteorSwarm = Spell("Meteor Swarm",
			level= 9,
			school="Evocation",
			casting_time="Action",
			ranges = "1 mile",
			duration = "Instantaneous",
			components = "Verbal, Somatic",
			concentration = "Concentration",
			definition = """
			Blazing orbs of fire plummet to the ground at four different points you can see within range. Each creature in a 40-foot-radius Sphere centered on each of those points makes a Dexterity saving throw. A creature takes 20d6 Fire damage and 20d6 Bludgeoning damage on a failed save or half as much damage on a successful one. A creature in the area of more than one fiery Sphere is affected only once.
			<br>
			A nonmagical object that isn't being worn or carried also takes the damage if it's in the spell's area, and the object starts burning if it's flammable.
			""")
	Wish = 	Spell("Wish",
		level= 9,
		school="Conjuration",
		casting_time="Action",
		ranges = "Self",
		duration = "Instantaneous",
		components = "Verbal",
		concentration = "",
		definition = """
		Wish is the mightiest spell a mortal can cast. By simply speaking aloud, you can alter reality itself.
		<br>
The basic use of this spell is to duplicate any other spell of level 8 or lower. If you use it this way, you don't need to meet any requirements to cast that spell, including costly components. The spell simply takes effect.
<br>
Alternatively, you can create one of the following effects of your choice:
<br>
	<b>Object Creation.</b> You create one object of up to 25,000 GP in value that isn't a magic item. The object can be no more than 300 feet in any dimension, and it appears in an unoccupied space that you can see on the ground.
<br>
	<b>Instant Health.</b> You allow yourself and up to twenty creatures that you can see to regain all Hit Points, and you end all effects on them listed in the Greater Restoration spell.
<br>
	<b>Resistance.</b> You grant up to ten creatures that you can see Resistance to one damage type that you choose. This Resistance is permanent.
<br>
	<b>Spell Immunity.</b> You grant up to ten creatures you can see immunity to a single spell or other magical effect for 8 hours.
<br>
	<b>Sudden Learning.</b> You replace one of your feats with another feat for which you are eligible. You lose all the benefits of the old feat and gain the benefits of the new one. You can't replace a feat that is a prerequisite for any of your other feats or features.
<br>
	<b>Roll Redo.</b> You undo a single recent event by forcing a reroll of any die roll made within the last round (including your last turn). Reality reshapes itself to accommodate the new result. For example, a Wish spell could undo an ally's failed saving throw or a foe's Critical Hit. You can force the reroll to be made with Advantage or Disadvantage, and you choose whether to use the reroll or the original roll.
<br>
	<b>Reshape Reality.</b> You may wish for something not included in any of the other effects. To do so, state your wish to the DM as precisely as possible. The DM has great latitude in ruling what occurs in such an instance; the greater the wish, the greater the likelihood that something goes wrong. This spell might simply fail, the effect you desire might be achieved only in part, or you might suffer an unforeseen consequence as a result of how you worded the wish. For example, wishing that a villain were dead might propel you forward in time to a period when that villain is no longer alive, effectively removing you from the game. Similarly, wishing for a Legendary magic item or an Artifact might instantly transport you to the presence of the item's current owner. If your wish is granted and its effects have consequences for a whole community, region, or world, you are likely to attract powerful foes. If your wish would affect a god, the god's divine servants might instantly intervene to prevent it or to encourage you to craft the wish in a particular way. If your wish would undo the multiverse itself, threaten the City of Sigil, or affect the Lady of Pain in any way, you see an image of her in your mind for a moment; she shakes her head, and your wish fails.
<br>
The stress of casting Wish to produce any effect other than duplicating another spell weakens you. After enduring that stress, each time you cast a spell until you finish a Long Rest, you take 1d10 Necrotic damage per level of that spell. This damage can't be reduced or prevented in any way. In addition, your Strength score becomes 3 for 2d4 days. For each of those days that you spend resting and doing nothing more than light activity, your remaining recovery time decreases by 2 days. Finally, there is a 33 percent chance that you are unable to cast Wish ever again if you suffer this stress.
		""")
	TruePolymorph = Spell("True Polymorph",
			level= 9,
			school="Transmutation",
			casting_time="Action",
			ranges = "30 feet",
			components = "Verbal, Somatic, Material(a drop of mercury, a dollop of gum arabic, and a wisp of smoke)",
			concentration = "Concentration",
			duration = "1 hour",
			definition = """
				Choose one creature or nonmagical object that you can see within range. The creature shape-shifts into a different creature or a nonmagical object, or the object shape-shifts into a creature (the object must be neither worn nor carried). The transformation lasts for the duration or until the target dies or is destroyed, but if you maintain Concentration on this spell for the full duration, the spell lasts until dispelled.
				<br>
				An unwilling creature can make a Wisdom saving throw, and if it succeeds, it isn't affected by this spell.
				<br>
				<b>Creature into Creature.</b> If you turn a creature into another kind of creature, the new form can be any kind you choose that has a Challenge Rating equal to or less than the target's Challenge Rating or level. The target's game statistics are replaced by the stat block of the new form, but it retains its Hit Points, Hit Point Dice, alignment, and personality.
					<br>
					The target gains a number of Temporary Hit Points equal to the Hit Points of the new form. These Temporary Hit Points vanish if any remain when the spell ends. The spell ends early on the target if it has no Temporary Hit Points left.
					<br>
					The target is limited in the actions it can perform by the anatomy of its new form, and it can't speak or cast spells.
					<br>
					The target's gear melds into the new form. The creature can't use or otherwise benefit from any of that equipment.
					<br>
				<b>Object into Creature.</b> You can turn an object into any kind of creature, as long as the creature's size is no larger than the object's size and the creature has a Challenge Rating of 9 or lower. The creature is Friendly to you and your allies. In combat, it takes its turns immediately after yours, and it obeys your commands.
					<br>
					If the spell lasts more than an hour, you no longer control the creature. It might remain Friendly to you, depending on how you have treated it.
					<br>
				<b>Creature into Object.</b> If you turn a creature into an object, it transforms along with whatever it is wearing and carrying into that form, as long as the object's size is no larger than the creature's size. The creature's statistics become those of the object, and the creature has no memory of time spent in this form after the spell ends and it returns to normal.
				""")

LocateAnimalsorPlants = LocateAnimalsPlants
ZoneofTruth = ZoneOfTruth
GlyphofWarding = GlyphWarding
LeomundTinyHut = TinyHut
TelepathicBond = RarysTelepathicBond
RegalPresence = YolandeRegalPresence
SpeakPlants = SpeakWithPlants
SpeakwithPlants = SpeakPlants
WallofStone = WallStone
ConeofCold = ConeCold


class FocusTechnique:
	def __init__(self, name, level, cost, action_type, description):
		self.name = name
		self.level = level
		self.cost = cost
			# Focus Point cost
		self.action_type = action_type
			# e.g. 'Bonus Action'
		self.description = description

	def __str__(self):
		return f"""<h5>{self.name}</h5>
		<h6>Cost: {self.cost} Focus Point{'s' if self.cost != 1 else ''}</h6>
		({self.action_type})<br>
		<span>{self.description}</span>"""

FlurryofBlows = FocusTechnique(
	"Flurry of Blows", 2, 1, "Bonus Action",
	"Expend 1 Focus Point to make two Unarmed Strikes as a Bonus Action."
	)

PatientDefense = FocusTechnique(
	"Patient Defense", 2, 1, "Bonus Action",
	"Take the Disengage action as a Bonus Action. Alternatively, expend 1 Focus Point to take both the Disengage and the Dodge actions as a Bonus Action."
)

StepOfTheWind = FocusTechnique(
	"Step of the Wind", 2, 1, "Bonus Action",
	"Take the Dash action as a Bonus Action. Alternatively, expend 1 Focus Point to take both the Disengage and Dash actions as a Bonus Action, and your jump distance is doubled for the turn."
)

DeflectAttacks = FocusTechnique(
	"Deflect Attacks", 3, 0, "Reaction",
	"When an attack roll hits you and deals bludgeoning, piercing, or slashing damage, take a Reaction to reduce the damage by 1d10 + your Dex mod + Monk level. If reduced to 0, expend 1 Focus Point to redirect force to another creature within range (see full rules)."
)

StunningStrike = FocusTechnique(
	"Stunning Strike", 5, 1, "Special",
	"Once per turn, when you hit with a Monk weapon or Unarmed Strike, expend 1 Focus Point to force a Constitution save. On failure, target is stunned until the start of your next turn."
)

# More techniques if added by subclasses, e.g., Shadow Arts, Elemental Attunement, etc.



TashaHideousLaughter = HideousLaughter

sanctuary = Sanctuary
