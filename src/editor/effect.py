from ..scenario import effect

class Effect(effect.Effect):
	def __init__(self,
		type = 0,
		ai_goal = -1,
		amount = -1,
		resource = None,
		diplomacy = None,
		uid_location = None,
		unit_constant = None,
		player_source = -1,
		player_target = -1,
		technology = -1,
		display_time = -1,
		trigger = -1,
		location = None,
		area_upper = None,
		area_lower = None,
		unit_group = None,
		unit_type = None,
		panel = -1,
		text = '',
		sound = '',
		uids = [],
	): 
		self.type(type)
		self.ai_goal(ai_goal)
		self.amount(amount)
		self.resource(resource)
		self.diplomacy(diplomacy)
		self.uid_location(uid_location)
		self.unit_constant(unit_constant)
		self.player_source(player_source)
		self.player_target(player_target)
		self.technology(technology)
		self.display_time(display_time)
		self.trigger(trigger)
		self.location(location)
		self.area_upper(area_upper)
		self.area_lower(area_lower)
		self.unit_group(unit_group)
		self.unit_type(unit_type)
		self.panel(panel)
		self.text(text)
		self.sound(sound)
		self.uids(uids)

		def type(self, type):
			self._eff_type.set(type)

		def ai_goal(self, ai_goal):
			self._ai_goal = ai_goal

		def amount(self, amount):
			self._amount = amount

		def resource(self, resource):
			self._resource.set(resource)

		def diplomacy(self, diplomacy):
			self._diplomacy.set(diplomacy)

		def uid_location(self, uid_location):
			self._uid_location = uid_location

		def unit_constant(self, unit_constant):
			self._unit_constant = unit_constant

		def player_source(self, player_source):
			self._player_source = player_source

		def player_target(self, player_target):
			self._player_target = player_target

		def technology(self, technology):
			self._technology = technology

		def display_time(self, display_time):
			self._display_time = display_time

		def trigger(self, trigger):
			self._trigger = trigger

		def location(self, location):
			if location is not None:
				self._location.x = location[0]
				self._location.y = location[1]

		def area_upper(self, area_upper):
			if area_upper is not None:
				self._area_upper.x = area_upper[0]
				self._area_upper.y = area_upper[1]

		def area_lower(self, area_lower):
			if area_lower is not None:
				self._area_lower.x = area_lower[0]
				self._area_lower.y = area_lower[1]

		def unit_group(self, unit_group):
			self._unit_group.set(unit_group)

		def unit_type(self, unit_type):
			self._unit_type.set(unit_type)

		def panel(self, panel):
			self._panel = panel

		def text(self, text):
			self._text = text

		def sound(self, sound):
			self._sound = sound

		def uids(self, uids):
			if uids is not None:
				self._uids = uids

class Blank(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(Blank, self).__init__(*ordered_args, **keyed_args)
		self.type('Blank')

class ChangeDiplomacy(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(ChangeDiplomacy, self).__init__(*ordered_args, **keyed_args)
		self.type('ChangeDiplomacy')

class ResearchTechnology(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(ResearchTechnology, self).__init__(*ordered_args, **keyed_args)
		self.type('ResearchTechnology')

class SendChat(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(SendChat, self).__init__(*ordered_args, **keyed_args)
		self.type('SendChat')

class PlaySound(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(PlaySound, self).__init__(*ordered_args, **keyed_args)
		self.type('PlaySound')

class SendTribute(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(SendTribute, self).__init__(*ordered_args, **keyed_args)
		self.type('SendTribute')

class UnlockGate(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(UnlockGate, self).__init__(*ordered_args, **keyed_args)
		self.type('UnlockGate')

class LockGate(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(LockGate, self).__init__(*ordered_args, **keyed_args)
		self.type('LockGate')

class ActivateTrigger(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(ActivateTrigger, self).__init__(*ordered_args, **keyed_args)
		self.type('ActivateTrigger')

class DeactivateTrigger(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(DeactivateTrigger, self).__init__(*ordered_args, **keyed_args)
		self.type('DeactivateTrigger')

class AIScriptGoal(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(AIScriptGoal, self).__init__(*ordered_args, **keyed_args)
		self.type('AIScriptGoal')

class CreateObject(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(CreateObject, self).__init__(*ordered_args, **keyed_args)
		self.type('CreateObject')

class TaskObject(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(TaskObject, self).__init__(*ordered_args, **keyed_args)
		self.type('TaskObject')

class DeclareVictory(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(DeclareVictory, self).__init__(*ordered_args, **keyed_args)
		self.type('DeclareVictory')

class KillObject(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(KillObject, self).__init__(*ordered_args, **keyed_args)
		self.type('KillObject')

class RemoveObject(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(RemoveObject, self).__init__(*ordered_args, **keyed_args)
		self.type('RemoveObject')

class ChangeView(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(ChangeView, self).__init__(*ordered_args, **keyed_args)
		self.type('ChangeView')

class Unload(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(Unload, self).__init__(*ordered_args, **keyed_args)
		self.type('Unload')

class ChangeOwnership(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(ChangeOwnership, self).__init__(*ordered_args, **keyed_args)
		self.type('ChangeOwnership')

class Patrol(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(Patrol, self).__init__(*ordered_args, **keyed_args)
		self.type('Patrol')

class DisplayInstructions(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(DisplayInstructions, self).__init__(*ordered_args, **keyed_args)
		self.type('DisplayInstructions')

class ClearInstructions(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(ClearInstructions, self).__init__(*ordered_args, **keyed_args)
		self.type('ClearInstructions')

class FreezeUnit(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(FreezeUnit, self).__init__(*ordered_args, **keyed_args)
		self.type('FreezeUnit')

class UseAdvancedButtons(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(UseAdvancedButtons, self).__init__(*ordered_args, **keyed_args)
		self.type('UseAdvancedButtons')

class DamageObject(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(DamageObject, self).__init__(*ordered_args, **keyed_args)
		self.type('DamageObject')

class PlaceFoundation(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(PlaceFoundation, self).__init__(*ordered_args, **keyed_args)
		self.type('PlaceFoundation')

class ChangeObjectName(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(ChangeObjectName, self).__init__(*ordered_args, **keyed_args)
		self.type('ChangeObjectName')

class ChangeObjectHP(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(ChangeObjectHP, self).__init__(*ordered_args, **keyed_args)
		self.type('ChangeObjectHP')

class ChangeObjectAttack(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(ChangeObjectAttack, self).__init__(*ordered_args, **keyed_args)
		self.type('ChangeObjectAttack')

class StopUnit(Effect):
	def __init__(self, *ordered_args, **keyed_args):
		super(StopUnit, self).__init__(*ordered_args, **keyed_args)
		self.type('StopUnit')

