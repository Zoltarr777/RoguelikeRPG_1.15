import tcod as libtcod

from game_messages import Message

from game_states import GameStates

from render_functions import RenderOrder

from playsound import playsound

def kill_player(player, constants):
	player.char = constants['corpse_tile']
	player.color = libtcod.white
	player.name = "corpse of " + player.name

	return Message("You died!", libtcod.red), GameStates.PLAYER_DEAD
	playsound('sounds/dead.m4a', block=False)

def kill_monster(monster, player, constants):
	print("\nEntered kill_monster function in death_functions\n")
	print("\n" + "Monster Name: " + monster.name + "\n")
	name_check = "corpse of "

	if monster.name == "Floor Trap":
		death_message = Message("The {0} deactivates!".format(monster.name.capitalize()), libtcod.red)
		monster.char = constants['floor_tile']
		monster.color = libtcod.white
		monster.blocks = False
		monster.fighter = None
		monster.ai = None
		monster.name = "Exploded Trap"
		monster.render_order = RenderOrder.CORPSE

	elif name_check in monster.name:
		death_message = Message(" ", libtcod.black)

	else:
		print("\nEntered death section\n")
		death_message = Message("You killed the {0} and take {1} gold!".format(monster.name.capitalize(), monster.fighter.gold), libtcod.red)
		playsound('sounds/dead.m4a', block=False)

		player.fighter.gold += monster.fighter.gold

		if monster.name == "Slime":
			monster.char = constants['slime_corpse_tile']
		elif monster.name == "Baby Slime":
			monster.char = constants['baby_slime_corpse_tile']
		elif monster.name == "Skeleton":
			monster.char = constants['skeleton_corpse_tile']
		else:
			monster.char = constants['corpse_tile']

		monster.color = libtcod.white
		monster.blocks = False
		monster.fighter = None
		print("\nRemoved figher status\n")
		monster.ai = None
		monster.name = "corpse of " + monster.name
		monster.render_order = RenderOrder.CORPSE

	return death_message

