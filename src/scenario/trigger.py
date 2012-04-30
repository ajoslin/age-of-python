from ..util import helpers 
from ..util import logger
import effect
import condition
import struct

logger = logger.Logger('trigger')

class Trigger(object):
	conditions = []
	effects = []
	name = ''
	description = ''
	on = False
	loop = False
	objective = False
	obj_order = 0

	def __init__(self):
		logger.log('creating new trigger')

	def read(self, scn_file):
		"""Reads trigger-data from given scn_file"""
		f = scn_file #shorter for ease of use
		self.on = helpers.read_long(f) == 1 # ==1: convert 0 or 1 to bool
		self.loop = helpers.read_long(f) == 1

		f.read(1) #1-char unknown

		# Objective is stored as a 1-byte char.
		# so read it in as an int, just mul it by 4
		self.objective = struct.unpack('<i', f.read(1)*4) == 1
		self.obj_order = helpers.read_long(f)

		f.read(4) # skip zeroes data

		self.description = helpers.read_str(f)
		self.name = helpers.read_str(f)

		# Effects
		neffects = helpers.read_long(f)
		# We have to create a temporary effects array
		# (because effect order is in the scn file after the actual effects)
		effects_tmp = []
		for i in range(neffects):
			e = effect.Effect()
			e.read(f)
			effects_tmp.append(e)

		# effect order. we'll put things in actual self.effects in order
		self.effects = []
		for i in range(neffects):
			order = helpers.read_long(f)
			self.effects.append(effects_tmp[order])

		#Conditions 
		nconds = helpers.read_long(f)
		# Temporary conditions array
		conditions_tmp = []
		for i in range(nconds):
			c = condition.Condition()
			c.read(f)
			conditions_tmp.append(c)

		# condition display order, uses actual self.conditions
		self.conditions = []
		for i in range(nconds):
			order = helpers.read_long(f)
			self.conditions.append(conditions_tmp[order])

	