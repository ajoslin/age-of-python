from ..util import helpers 
from ..util import logger

logger = logger.Logger('condition')

# Enum of condition types. accessed through eg Types.BringObjectToObject
class Type:
	Blank = 0
	BringObjectToArea = 1
	BringObjectToObject = 2
	OwnObjects = 3
	OwnFewerObjects = 4
	ObjectsInArea = 5
	DestroyObject = 6
	CaptureObject = 7
	AccumulateAttribute = 8
	ResearchTechnology = 9
	Timer = 10
	ObjectSelected = 11
	AISignal = 12
	PlayerDefeated = 13
	ObjectHasTarget = 14
	ObjectVisible = 15
	ObjectNotVisible = 16
	ResearchingTechnology = 17
	UnitsGarrisoned = 18
	DifficultyLevel = 19

class Condition(object):
	cond_type = -1
	check = 0x10 # conditions are this by default. see aokts source
	amount = -1
	resource = -1
	uid_object = -1 #unit id on the map
	uid_location = -1 #unit id on the map
	unit_constant = -1 #number from unit list (eg archer)
	player = -1
	tech = -1
	timer = -1
	unkown = -1
	area_ur_y = -1
	area_ur_x = -1
	area_ll_y = -1
	area_ll_x = -1
	unit_group = -1
	unit_type = -1
	ai_signal = -1

	def write(self, scn_file):
		f = scn_file
		helpers.write_long(f, self.cond_type)
		helpers.write_long(f, self.check)
		helpers.write_long(f, self.amount)
		helpers.write_long(f, self.resources)
		helpers.write_long(f, self.uid_object)
		helpers.write_long(f, self.uid_location)
		helpers.write_long(f, self.unit_const)
		helpers.write_long(f, self.player)
		helpers.write_long(f, self.technology)
		helpers.write_long(f, self.timer)
		helpers.write_long(f, self.unknown)
		helpers.write_long(f, self.area_ur_y)
		helpers.write_long(f, self.area_ur_x)
		helpers.write_long(f, self.area_ll_y)
		helpers.write_long(f, self.area_ll_x)
		helpers.write_long(f, self.unit_group)
		helpers.write_long(f, self.unit_type)
		helpers.write_long(f, self.ai_signal)

	def read(self, scn_file):
		""" Read condition from scenario file """
		f = scn_file # for ease of use
		self.cond_type    = helpers.read_long(f)
		self.check        = helpers.read_long(f)
		self.amount       = helpers.read_long(f)
		self.resources    = helpers.read_long(f)
		self.uid_object   = helpers.read_long(f)
		self.uid_location = helpers.read_long(f)
		self.unit_const   = helpers.read_long(f)
		self.player       = helpers.read_long(f)
		self.technology   = helpers.read_long(f)
		self.timer        = helpers.read_long(f)
		self.unknown      = helpers.read_long(f)
		self.area_ur_y    = helpers.read_long(f)
		self.area_ur_x    = helpers.read_long(f)
		self.area_ll_y    = helpers.read_long(f)
		self.area_ll_x    = helpers.read_long(f)
		self.unit_group   = helpers.read_long(f)
		self.unit_type    = helpers.read_long(f)
		self.ai_signal    = helpers.read_long(f)