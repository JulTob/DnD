
from Minion import Initialized, Alert, Inform, Warning, News

try: # to find the Cartography
	from AtlasAlusoris.Grimoire_of_NPC import NPC
	import random

	from AtlasScriptum.Map_of_Formats import Entry
	from AtlasLudus.Map_of_Dice import Dice

	from AtlasInventarium.Grimoire_of_Weapons import Weapon as weapon
	from AtlasLudus.Map_of_Useful_Functions import select1

	from AtlasLudus.Compass_of_Damages 	import MagicDamage, Damage

except ImportError as e:
	Alert("My lord, I couldn't find the cartography for the Lodge of Basic Weapons",e)


class Lodge():
	def __init__(lodge,npc):
		Initialized("You got a new Lodge of Weapons, Master.")
		Warning(
			f"The npc is of type: {type(npc)}")

		# Internal variables to initialize weapons
		Type= npc.Type
		PB = npc.proficiency_bonus
		STR = npc.ability_scores.str_mod
		DEX = npc.ability_scores.dex_mod
		MAG = max(
			npc.ability_scores.cha_mod,
			npc.ability_scores.wis_mod,
			npc.ability_scores.int_mod)
		FIN = max(STR, DEX)
		CON = npc.ability_scores.con_mod

		# Define weapons
		lodge.Fists = 		weapon("Fists",			 Dice(PB-1),"d4", STR,"Bludgeoning")
		lodge.Knuckles = 		weapon("Brass Knuckles", Dice(PB-1),"d4", STR,"Bludgeoning")
		lodge.Club = 			weapon("Club",			 Dice(PB-1),"d4", STR,"Bludgeoning")
		lodge.Dagger = 		weapon("Dagger",		 Dice(PB-1),"d4", FIN,"Piercing","20/60 thrown")
		lodge.GreatClub = 	weapon("GreatClub",		 Dice(PB-1),"d8", STR,"Bludgeoning")
		lodge.Handaxe = 		weapon("Handaxe",		 Dice(PB-1),"d6", STR,"Slashing",'20/60 thrown')
		lodge.Javelin = 		weapon("Javelin",		 Dice(PB-1),"d6", STR,"Piercing",'30/120 thrown')
		lodge.LightHammer = 	weapon("Light Hammer",	 Dice(PB-1),"d4", STR,"Bludgeoning",'20/60 thrown')
		lodge.Mace = 			weapon("Mace",			 Dice(PB-1),"d6", STR,"Bludgeoning")
		lodge.Quarterstaff = 	weapon("Quarterstaff",	 Dice(PB-1),random.choice(['d8','d6']), STR,"Bludgeoning")
		lodge.Sickle = 		weapon("Sickle",		 Dice(PB-1),"d4", STR,"Slashing")
		lodge.Slam = 			weapon("Slam",			 Dice(PB-1),"d4", STR,"Bludgeoning")
		lodge.Spear = 		weapon("Spear",			 Dice(PB-1),random.choice(['d8','d6']), STR,"Piercing",'20/60 thrown')
		lodge.Nunchaku = 		weapon("Nunchaku",		 Dice(PB-1),'d6', STR,"Bludgeoning")

		lodge.SimpleMeleeweapons = [
			lodge.Fists,
			lodge.Knuckles,
			lodge.Club,
			lodge.Dagger,
			lodge.GreatClub,
			lodge.Handaxe,
			lodge.Javelin,
			lodge.LightHammer,
			lodge.Mace,
			lodge.Quarterstaff,
			lodge.Sickle,
			lodge.Slam,
			lodge.Spear,
			lodge.Nunchaku]

		lodge.LightCrossbow = weapon("Light Crossbow",Dice(PB-1),"d8", DEX,"Piercing",'80/320 range','ammunition, loading, two handed')
		lodge.Dart = 			weapon("Dart",			Dice(PB-1),"d4", FIN,"Piercing",'20/60 thrown range', 'finesse')
		lodge.Shortbow = 		weapon("Shortbow",		Dice(PB-1),"d6", DEX,"Piercing",'80/320 range','Ammunition, two handed')
		lodge.Sling = 		weapon("Sling",			Dice(Dice(PB-1)),"d4", DEX,"Bludgeoning",'30/120 range','Ammunition')
		lodge.Rock = 			weapon("Rock",			Dice(PB-1),"d4", DEX,"Bludgeoning",'30/120 range')

		lodge.SimpleRangedweapons = [
			lodge.LightCrossbow,
			lodge.Dart,
			lodge.Shortbow,
			lodge.Sling,
			lodge.Rock]

		lodge.Battleaxe = 	weapon("Battleaxe",	Dice(PB-1),random.choice(['d8','d10']),STR,'Slashing')
		lodge.Flail = 		weapon("Battleaxe",	Dice(PB-1),'d8',STR,'Bludgeoning')
		lodge.Glaive = 		weapon("Glaive",	Dice(PB-1),'d10',STR,'Bludgeoning','reach')
		lodge.Greataxe = 		weapon("Greataxe",	Dice(PB-1),'d12',STR,'Slashing','reach')
		lodge.Greatsword = 	weapon("Greatsword",Dice(PB),'d6',STR,'Slashing')
		lodge.Halberd = 		weapon("Halberd",	Dice(PB-1),'d10',STR,'Slashing','reach')
		lodge.Lance = 		weapon("Lance",		Dice(PB-1),'d12',STR,'Piercing','reach')
		lodge.Longsword = 	weapon("Longsword",	Dice(PB-1),random.choice(['d8','d10']),STR,'Slashing')
		lodge.Maul = 			weapon("Maul",		Dice(PB),'d6',STR,'Bludgeoning')
		lodge.Morningstar = 	weapon("Morningstar",Dice(PB-1),'d8',STR,'Piercing')
		lodge.Pike = 			weapon("Pike",		Dice(PB-1),'d10',STR,'Piercing','reach')
		lodge.Rapier = 		weapon("Rapier",	Dice(PB-1),'d8',FIN,'Piercing')
		lodge.Scimitar = 		weapon("Scimitar",	Dice(PB-1),'d6',FIN,'Slashing','','light')
		lodge.Trident = 		weapon("Trident",	Dice(PB-1),random.choice(['d8','d6']),STR,'Piercing','20/60 thrown')
		lodge.WarPick = 		weapon("War Pick",	Dice(PB-1),'d8',STR,'Piercing')
		lodge.Warhammer = 	weapon("Warhammer",	Dice(PB-1),random.choice(['d8','d10']),STR,'Bludgeoning')
		lodge.Whip = 			weapon("Whip",		Dice(PB-1),'d4',FIN,'Slashing','reach','finesse')

		lodge.MartialMeleeweapons = [
			lodge.Battleaxe,
			lodge.Flail,
			lodge.Glaive,
			lodge.Greataxe,
			lodge.Greatsword,
			lodge.Halberd,
			lodge.Lance,
			lodge.Longsword,
			lodge.Maul,
			lodge.Morningstar,
			lodge.Pike,
			lodge.Rapier,
			lodge.Scimitar,
			lodge.Trident,
			lodge.WarPick,
			lodge.Warhammer,
			lodge.Whip,
			]

		lodge.Blowgun = 			weapon("Blowgun",		1,"", 				DEX,"Piercing",'25/100 range','Ammunition. Loading')
		lodge.HandCrossbow = 		weapon("Hand Crossbow",	Dice(PB-1),"d6", 	DEX,"Piercing",'30/120 range','Ammunition. Light. Loading')
		lodge.HeavyCrossbow = 	weapon("Heavy Crossbow",Dice(PB-1),"d10", 	DEX,"Piercing",'100/400 range','Ammunition. Heavy. Loading. Two Handed')
		lodge.Longbow = 			weapon("Longbow",		Dice(PB-1),"d8", 	DEX,"Piercing",'150/600 range','Ammunition. Heavy. Two Handed')
		lodge.Net = 				weapon("Net",			0,"", 				0,"Special",'5/15 range','Thrown')
		lodge.ThrowingAxe = 		weapon("Throwing Axe",	Dice(PB-1),"d6", 	STR,"Slashing",'20/60 range','Thrown')
		lodge.FlintlockPistol =	weapon("Flintlock Pistol",Dice(PB-1),"d8", 	DEX,"Piercing",'30/90 range','Loading, Jamming: On an attack roll of 1, the gun jams and requires an action to clear before it can be fired again.')
		lodge.Musket = 			weapon("Musket",		Dice(PB-1)+1,"d6", 	DEX,"Piercing",'60/180 range','Loading, Jamming: On an attack roll of 1, the musket jams and requires an action to clear before it can be fired again.')
		lodge.Blunderbuss = 		weapon("Blunderbuss",	Dice(PB)+1,"d6", 	DEX,"Fire",'10/30 range',"Loading, Exploding: On an attack roll of 1, the gun explodes and requires a short rest fixing it before it can be fired again. You don't gain the benefits of that short rest.")

		lodge.MartialRangedweapons = [
			lodge.Blowgun,
			lodge.HandCrossbow,
			lodge.HeavyCrossbow,
			lodge.Longbow,
			lodge.Net,
			lodge.ThrowingAxe,
			lodge.FlintlockPistol,
			lodge.Musket,
			lodge.Blunderbuss,
			]

		lodge.Tail =  weapon("Tail",Dice(PB-1),'d4',STR,'Bludgeoning')

		lodge.Bite = weapon("Bite",Dice(PB-1),
			'd4',
			STR,'Piercing','',
			select1([
				'',
				f"""The target is grappled (escape DC {
					8+STR+PB
					} Strength saving throw). Until this grapple ends, the target is restrained, and {
					npc.title} can't bite another target.<br>""",
				f"The target must succeed a DC {8+STR+PB} Strength saving throw or be knocked prone.<br>",
				]),
			)

		lodge.Claws = weapon("Claws",Dice(PB-1),'d4',STR,'Slashing')

		lodge.Primalweapons = [
			lodge.Tail,
			lodge.Bite,
			lodge.Claws,
			]

		lodge.Firebolt = 	weapon("Firebolt",Dice(PB-1),"d10", MAG, "Fire",'10/30 range')

		lodge.Tentacle = 	weapon("Tentacle",Dice(PB-1),'d4',STR,'Bludgeoning')

		lodge.Breath = 	weapon("Breath Attack",Dice(PB)+1,"d10", MAG, MagicDamage(),'10/30 range')

		lodge.LifeDrain = weapon("Life Drain", Dice(PB)-1, "d4", CON, select1(["Piercing", "Necrotic"]),     properties=(
	        f"The target's hit point maximum is reduced by an amount equal to the damage taken. "
	        f"The undead regains hit points equal to that amount. "
	        f"The reduction lasts until the target finishes a long rest. "
	        f"The target dies if this effect reduces its hit point maximum to 0."
    		))

# Example usage
if __name__ == "__main__":
    lodge = Lodge(NPC())
    print("Available Simple Melee Weapons:")
    for weapon in lodge.SimpleMeleeWeapons:
        print(f"- {weapon.name}")
