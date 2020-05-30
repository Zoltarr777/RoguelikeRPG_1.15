import tcod as libtcod

from game_messages import Message
from entity import Entity

class Burn:
	def __init__(self, damage, turns, owner):
		self.damage = damage
		self.turns = turns
		self.owner = owner

	def update(self):
		results = []

		if self.turns == 0:
			self.owner.fighter.status = None
			results.append({'message': Message("The {0} is no longer burned!".format(self.owner.name.capitalize()), libtcod.orange)})
		else:
			results.append({'message': Message("The {0} takes {1} burn damage!".format(self.owner.name.capitalize(), str(self.damage), str(self.turns)), libtcod.orange)})
			results.extend(self.owner.fighter.take_damage(self.damage))
			self.turns -= 1

		return results

class Poison:
	def __init__(self, damage, turns, owner):
		self.damage = damage
		self.turns = turns
		self.owner = owner

	def update(self):
		results = []

		if self.turns == 0:
			self.owner.fighter.status = None
			results.append({'message': Message("The {0} is no longer poisoned!".format(self.owner.name.capitalize()), libtcod.orange)})
		else:
			results.append({'message': Message("The {0} takes {1} poison damage!".format(self.owner.name.capitalize(), str(self.damage), str(self.turns)), libtcod.orange)})
			results.extend(self.owner.fighter.take_damage(self.damage))
			self.turns -= 1

		return results


