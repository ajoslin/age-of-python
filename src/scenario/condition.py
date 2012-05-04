from ..util import helpers 
from ..util import logger
import genie

logger = logger.Logger('condition')

class Condition(object):
	_cond_type = None
	_check = 0x10 # conditions are this by default. see aokts source
	_amount = -1
	_resource = None
	_uid_object = -1 #unit id on the map
	_uid_location = -1 #unit id on the map
	_unit_constant = -1 #number from unit list (eg archer)
	_player_source = -1
	_technology = -1
	_timer = -1
	_unknown = -1
	_area_upper = None
	_area_lower = None
	_unit_group = None
	_unit_type = None
	_ai_signal = -1

	def __init__(self):
		self._cond_type = genie.ConditionType(None)
		self._resource = genie.Resource(None)
		self._area_upper = genie.Location(-1, -1)
		self._area_lower = genie.Location(-1, -1)
		self._unit_group = genie.UnitGroup(None)
		self._unit_type = genie.UnitType(None)

	def write(self, scn_file):
		f = scn_file
		helpers.write_long(f, self._cond_type.value())
		helpers.write_long(f, self._check)
		helpers.write_long(f, self._amount)
		helpers.write_long(f, self._resource.value())
		helpers.write_long(f, self._uid_object)
		helpers.write_long(f, self._uid_location)
		helpers.write_long(f, self._unit_const)
		helpers.write_long(f, self._player_source)
		helpers.write_long(f, self._technology)
		helpers.write_long(f, self._timer)
		helpers.write_long(f, self._unknown)
		helpers.write_long(f, self._area_upper.y)
		helpers.write_long(f, self._area_upper.x)
		helpers.write_long(f, self._area_lower.y)
		helpers.write_long(f, self._area_lower.x)
		helpers.write_long(f, self._unit_group.value())
		helpers.write_long(f, self._unit_type.value())
		helpers.write_long(f, self._ai_signal)

	def read(self, scn_file):
		""" Read condition from scenario file """
		f = scn_file # for ease of use
		self._cond_type.set( helpers.read_long(f) )
		self._check        = helpers.read_long(f)
		self._amount       = helpers.read_long(f)
		self._resource.set( helpers.read_long(f) )
		self._uid_object   = helpers.read_long(f)
		self._uid_location = helpers.read_long(f)
		self._unit_const   = helpers.read_long(f)
		self._player_source= helpers.read_long(f)
		self._technology   = helpers.read_long(f)
		self._timer        = helpers.read_long(f)
		self._unknown      = helpers.read_long(f)
		self._area_upper.y = helpers.read_long(f)
		self._area_upper.x = helpers.read_long(f)
		self._area_lower.y = helpers.read_long(f)
		self._area_lower.x = helpers.read_long(f)
		self._unit_group.set( helpers.read_long(f) )
		self._unit_type.set( (helpers.read_long(f)) )
		self._ai_signal    = helpers.read_long(f)