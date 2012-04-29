from ..util import helpers 
from ..util import logger

logger = logger.Logger('effect')

# Enum of all effect types, accessed eg by Type.ChangeDiplomacy
class Type:
	Blank = 0
	ChangeDiplomacy = 1
	ResearchTechnology = 2
	SendChat = 3
	PlaySound = 4
	SendTribute = 5
	UnlockGate = 6
	LockGate = 7
	ActivateTrigger = 8
	DeactivateTrigger = 9
	AIScriptGoal = 10
	CreateObject = 11
	TaskObject = 12
	DeclareVictory = 13
	KillObject = 14
	RemoveObject = 15
	ChangeView = 16
	Unload = 17
	ChangeOwnership = 18
	Patrol = 19
	DisplayInstructions = 20
	ClearInstructions = 21
	FreezeUnit = 22
	UseAdvancedButtons = 23
	DamageObject = 24
	PlaceFoundation = 25
	ChangeObjectName = 26
	ChangeObjectHP = 27
	ChangeObjectAttack = 28
	StopUnit = 29

class Effect(object):
	eff_type = -1
	check = 0x17 # effects are this by default. see aokts source
	ai_goal = -1
	amount = -1
	resource = -1
	diplomacy = -1
	# num_selected : stored as len(uids)
	uid_location = -1 #this is a unit id on the map
	unit_constant = -1 #this is a number from the unitlist (eg archer)
	player_source = -1
	player_target = -1
	technology = -1
	string_table_id = -1 # unused I think - but still have to have it
	unknown = -1
	display_time = -1
	trigger_index = -1
	location_y = -1
	location_x = -1
	area_ll_y = -1
	area_ll_x = -1
	area_ur_y = -1
	area_ur_x = -1
	unit_group = -1
	unit_type = -1
	panel = -1
	text = ''
	sound = ''
	uids = []

	def __init__(self):
		logger.log("creating new effect")


	def read(self, scn_file):
		"""Read effect from scenario file"""
		f = scn_file # for ease of use
		self.eff_type        = helpers.read_long(f)
		self.check           = helpers.read_long(f)
		self.ai_goal         = helpers.read_long(f)
		self.amount          = helpers.read_long(f)
		self.resource        = helpers.read_long(f)
		self.diplomacy       = helpers.read_long(f)
		uids_len             = helpers.read_long(f)
		self.uid_location    = helpers.read_long(f)
		self.unit_constant   = helpers.read_long(f)
		self.player_source   = helpers.read_long(f)
		self.player_target   = helpers.read_long(f)
		self.technology      = helpers.read_long(f)
		self.string_table_id = helpers.read_long(f)
		self.unknown         = helpers.read_long(f)
		self.display_time    = helpers.read_long(f)
		self.trigger_index   = helpers.read_long(f)
		self.location_y      = helpers.read_long(f)
		self.location_x      = helpers.read_long(f)
		self.area_ll_y       = helpers.read_long(f)
		self.area_ll_x       = helpers.read_long(f)
		self.area_ur_y       = helpers.read_long(f)
		self.area_ur_x       = helpers.read_long(f)
		self.unit_group      = helpers.read_long(f)
		self.unit_type       = helpers.read_long(f)
		self.panel           = helpers.read_long(f)
		self.text            = helpers.read_str(f)
		self.sound           = helpers.read_str(f)
		for i in range(uids_len):
			self.uids.append( helpers.read_long(f) )





