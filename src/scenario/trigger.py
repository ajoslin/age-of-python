from ..util import helpers 
from ..util import logger
import effect
import condition
import struct
import os

logger = logger.Logger('trigger')

class Trigger(object):
	_conditions = []
	_effects = []
	_name = ''
	_description = ''
	_on = False
	_loop = False
	_objective = False
	_obj_order = -1

	def write(self, scn_file):
		f = scn_file #short for ease of use
		init = f.tell()
		helpers.write_long(f, self._on)
		helpers.write_long(f, self._loop)
		f.write( struct.pack('<c', '0') ) # write unknown
		f.write( struct.pack('<?', self._objective) ) #objective is bool
		helpers.write_long(f, self._obj_order)

		# write 4 bytes of zeroes
		for i in range(4): f.write( struct.pack('<c', '0') ) 

		helpers.write_str(f, self._description)
		helpers.write_str(f, self._name)

		# Write effects
		helpers.write_long(f, len(self._effects))
		for e in self._effects:
			e.write(f)
		# Write effect order
		for i in range( len(self._effects) ):
			helpers.write_long(f, i)

		# Write conds
		helpers.write_long(f, len(self._conditions))
		for c in self._conditions:
			c.write(f)
		# Write condition order
		for i in range( len(self._conditions) ):
			helpers.write_long(f, i)


	def read(self, scn_file):
		"""Reads trigger-data from given scn_file"""
		f = scn_file #shorter for ease of use
		self._on = helpers.read_long(f) == 1 # ==1: convert 0 or 1 to bool
		self._loop = helpers.read_long(f) == 1

		f.read(1) #1-char unknown

		# Objective is stored as a 1-byte char.
		# so read it in as an int, just mul it by 4
		self._objective = struct.unpack('<i', f.read(1)*4) == 1
		self._obj_order = helpers.read_long(f)

		f.read(4) # skip zeroes data

		self._description = helpers.read_str(f)
		self._name = helpers.read_str(f)

		# Effects
		neffects = helpers.read_long(f)
		# We have to create a temporary effects array
		# (because effect order is in the scn file after the actual effects)
		effects_tmp = []
		for i in range(neffects):
			e = effect.Effect()
			e.read(f)
			effects_tmp.append(e)

		# effect order. we'll put things in actual self._effects in order
		self._effects = []
		for i in range(neffects):
			order = helpers.read_long(f)
			self._effects.append(effects_tmp[order])

		#Conditions 
		nconds = helpers.read_long(f)
		# Temporary conditions array
		conditions_tmp = []
		for i in range(nconds):
			c = condition.Condition()
			c.read(f)
			conditions_tmp.append(c)

		# condition display order, uses actual self._conditions
		self._conditions = []
		for i in range(nconds):
			order = helpers.read_long(f)
			self._conditions.append(conditions_tmp[order])


	