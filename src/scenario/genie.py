from ..util import helpers
from ..util import logger

logger = logger.Logger('genie')

## LOCATION
# area is just two of these
class Location(object):
	x = -1
	y = -1
	def __init__(self, x, y):
		if x is not None: self.x = x
		if y is not None: self.y = y

	# Genie locations are (y,x)
	def write(self, scn_file):
		helpers.write_long(scn_file, self.y)
		helpers.write_long(scn_file, self.x)

	def read(self, scn_file):
		self.y = helpers.read_long(scn_file)
		self.x = helpers.read_long(scn_file)

## PAIRS
# string identifiers for numbered things
class Pairs(object):
	_pairs = {}
	_default_value = -1

	# if is string, it's fine.
	# if is number, do reverse lookup to find string
	def __init__(self, key_or_val):
		self.set(key_or_val)

	# set key using a key or a value
	def set(self, key_or_val):
		# If it's an int, convert it to a correct key
		if key_or_val != None and not isinstance(key_or_val, basestring):
			for item in self._pairs.items():
				key = item[0]
				value = item[1]
				print key+': '+str(value)
				if value == key_or_val:
					key_or_val = key
					
		self._key = key_or_val

	def value(self):
		if self._key in self._pairs:
			return self._pairs[self._key]
		return self._default_value

	def key(self):
		return self._key

	def write(self, scn_file):
		helpers.write_long( scn_file, self.value() )

	def read(self, scn_file):
		self.set( helpers.read_long(scn_file) )

class ConditionType(Pairs):
	_pairs = {
		'Blank': 0,
		'BringObjectToArea': 1,
		'BringObjectToObject': 2,
		'OwnObjects': 3,
		'OwnFewerObjects': 4,
		'ObjectsInArea': 5,
		'DestroyObject': 6,
		'CaptureObject': 7,
		'AccumulateAttribute': 8,
		'ResearchTechnology': 9,
		'Timer': 10,
		'ObjectSelected': 11,
		'AISignal': 12,
		'PlayerDefeated': 13,
		'ObjectHasTarget': 14,
		'ObjectVisible': 15,
		'ObjectNotVisible': 16,
		'ResearchingTechnology': 17,
		'UnitsGarrisoned': 18,
		'DifficultyLevel': 19
	}
	_default_value = 0

class EffectType(Pairs):
	_pairs = {
		'Blank': 0,
		'ChangeDiplomacy': 1,
		'ResearchTechnology': 2,
		'SendChat': 3,
		'PlaySound': 4,
		'SendTribute': 5,
		'UnlockGate': 6,
		'LockGate': 7,
		'ActivateTrigger': 8,
		'DeactivateTrigger': 9,
		'AIScriptGoal': 10,
		'CreateObject': 11,
		'TaskObject': 12,
		'DeclareVictory': 13,
		'KillObject': 14,
		'RemoveObject': 15,
		'ChangeView': 16,
		'Unload': 17,
		'ChangeOwnership': 18,
		'Patrol': 19,
		'DisplayInstructions': 20,
		'ClearInstructions': 21,
		'FreezeUnit': 22,
		'UseAdvancedButtons': 23,
		'DamageObject': 24,
		'PlaceFoundation': 25,
		'ChangeObjectName': 26,
		'ChangeObjectHP': 27,
		'ChangeObjectAttack': 28,
		'StopUnit': 29
	}
	_default_value = 0


class Resource(Pairs):
	_pairs = {
		'food': 0, 
		'wood': 1, 
		'stone': 2, 
		'gold': 3, 
		'population limit': 4, 
		'relics': 7, 
		'population': 11,
		'kills': 20, 
		'technologies': 21,
		'villager population': 37,
		'military population': 40,
		'conversions': 41,
		'razings': 43,
		'kill ratio': 44
	}


class Diplomacy(Pairs):
	_pairs = {
		'ally': 0,
		'neutral': 1,
		'enemy': 2
	}
	

class UnitType(Pairs):
	_pairs = {
		'none': -1,
		'other': 1,
		'building': 2,
		'civilian': 3,
		'military': 4
	}

class UnitGroup(Pairs):
	_pairs = {
		'sheep': 0,
		'trade boat': 1,
		'monk with relic': 2,
		'horse': 3,
		'trade cart': 4,
		'cavalry archer': 5,
		'packed siege units': 6,
		'relic': 7,
		'farm': 8,
		'walls': 9,
		'raider': 10,
		'building': 11,
		'spearman': 12,
		'boarding boat': 13,
		'map decoration': 14,
		'tower': 15,
		'fishing boat': 16,
		'dolphin': 17,
		'hand cannoneer': 18,
		'phalanx': 19,
		'pikeman': 20,
		'two-handed swordsman': 21,
		'cavalry': 22,
		'scorpion': 23,
		'sea fish': 24,
		'other': 25,
		'conquistador': 26,
		'unpacked siege units': 27,
		'civilian': 28,
		'ore mine': 29,
		'prey animal': 30,
		'berry bush': 31,
		'shore fish': 32,
		'artifact': 33,
		'cavalry raider': 34,
		'petard': 35,
		'stone mine': 36,
		'gold mine': 37,
		'cliff': 38,
		'king': 39,
		'resource': 40,
		'piles': 41,
		'siege weapon': 42,
		'tree': 43,
		'transport boat': 44,
		'archer': 45,
		'flags': 46,
		'scout cavalry': 47,
		'war boat': 48,
		'gates': 49,
		'soldier': 50,
		'predator animal': 51,
		'priest': 52,
		'birds': 53
	}