from ..util import helpers 
from ..util import logger
import effect
import condition

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
		self.on = helpers.read_long(f) == 1 # ==1: convert 0/1 to bool
		self.loop = helpers.read_long(f) == 1
		helpers.read_long(f) #unknown
		self.objective = helpers.read_long(f) == 1
		self.obj_order = helpers.read_long(f)

		f.read(4) # skip zeroes data

		self.description = helpers.read_str(f)
		self.name = helpers.read_str(f)

		# Effects
		neffects = helpers.read_long(f)
		# We have to createa  temporary effects array
		# (this is because effect order is in the scn file
		#  after the actual effects for some reason)
		self.effects = [None] * neffects #initialize list with neffects items
		for i in range(neffects):
			e = effect.Effect().read(f)
			effects.append(e)

		# effect display order
		for i in range(neffects):
			self.effects[i].display_order = helpers.read_long(f)

		#Conditions 
		nconds = helpers.read_long(f)
		self.conditions = [None] * nconds
		for i in range(nconds):
			c = condition.Condition().read(f)
			conditions.append(c)

		# condition display order
		for i in range(nconds):
			conditions[i].display_order = helpers.read_long(f)