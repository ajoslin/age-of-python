from ..util import helpers 
from ..util import logger
import genie

logger = logger.Logger('effect')

class Effect(object):
	_eff_type = None
	_check = 0x17 # effects are this by default. see aokts source
	_ai_goal = -1
	_amount = -1
	_resource = None
	_diplomacy = None
	# _num_selected stored as len(uids)
	_uid_location = -1 #this is a unit id on the map
	_unit_constant = -1 #this is a number from the unitlist (eg archer)
	_player_source = -1
	_player_target = -1
	_technology = -1
	_string_table_id = -1 # unused I think - but still have to have it
	_unknown = -1
	_display_time = -1
	_trigger = -1
	_location = None
	_area_upper = None
	_area_lower = None
	_unit_group = None
	_unit_type = None
	_panel = -1
	_text = ''
	_sound = ''
	_uids = []

	def __init__(self):
		self._eff_type = genie.EffectType(None)
		self._resource = genie.Resource(None)
		self._diplomacy = genie.Diplomacy(None)
		self._location = genie.Location(-1, -1)
		self._area_upper = genie.Location(-1, -1)
		self._area_lower = genie.Location(-1, -1)
		self._unit_group = genie.UnitGroup(None)
		self._unit_type = genie.UnitType(None)

	def write(self, scn_file):
		f = scn_file # for ease of use
		helpers.write_long(f, self._eff_type.value())
		helpers.write_long(f, self._check)
		helpers.write_long(f, self._ai_goal)
		helpers.write_long(f, self._amount)
		helpers.write_long(f, self._resource.value())
		helpers.write_long(f, self._diplomacy.value())
		helpers.write_long(f, len(self._uids))
		helpers.write_long(f, self._uid_location)
		helpers.write_long(f, self._unit_constant)
		helpers.write_long(f, self._player_source)
		helpers.write_long(f, self._player_target)
		helpers.write_long(f, self._technology)
		helpers.write_long(f, self._string_table_id)
		helpers.write_long(f, self._unknown)
		helpers.write_long(f, self._display_time)
		helpers.write_long(f, self._trigger)
		helpers.write_long(f, self._location.y)
		helpers.write_long(f, self._location.x)
		helpers.write_long(f, self._area_upper.y)
		helpers.write_long(f, self._area_upper.x)
		helpers.write_long(f, self._area_lower.y)
		helpers.write_long(f, self._area_lower.x)
		helpers.write_long(f, self._unit_group.value())
		helpers.write_long(f, self._unit_type.value())
		helpers.write_long(f, self._panel)
		helpers.write_str(f,  self._text)
		helpers.write_str(f,  self._sound)
		for i in range( len(self._uids) ):
			helpers.write_long(f, self._uids[i])

	def read(self, scn_file):
		"""Read effect from scenario file"""
		f = scn_file # for ease of use
		self._eff_type.set( helpers.read_long(f) )
		self._check = helpers.read_long(f)
		self._ai_goal = helpers.read_long(f)
		self._amount = helpers.read_long(f)
		self._resource.set( helpers.read_long(f) )
		self._diplomacy.set( helpers.read_long(f) )
		uids_len = helpers.read_long(f)
		self._uid_location = helpers.read_long(f)
		self._unit_constant = helpers.read_long(f)
		self._player_source = helpers.read_long(f)
		self._player_target = helpers.read_long(f)
		self._technology = helpers.read_long(f)
		self._string_table_id = helpers.read_long(f)
		self._unknown = helpers.read_long(f)
		self._display_time = helpers.read_long(f)
		self._trigger = helpers.read_long(f)
		self._location.y = helpers.read_long(f)
		self._location.x = helpers.read_long(f)
		self._area_upper.y = helpers.read_long(f)
		self._area_upper.x = helpers.read_long(f)
		self._area_lower.y = helpers.read_long(f)
		self._area_lower.x = helpers.read_long(f)
		self._unit_group.set( helpers.read_long(f) )
		self._unit_type.set( helpers.read_long(f) )
		self._panel = helpers.read_long(f)
		self._text = helpers.read_str(f)
		self._sound = helpers.read_str(f)
		for i in range(uids_len):
			self._uids.append( helpers.read_long(f) )





