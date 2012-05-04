from ..scenario import condition

class Condition(condition.Condition):
	def __init__(self,
		type = None,
		amount = -1,
		resource = None,
		uid_object = -1,
		uid_location = -1,
		unit_constant = -1,
		player_source = -1,
		technology = -1,
		timer = -1,
		area_upper = None,
		area_lower = None,
		unit_group = None,
		unit_type = None,
		ai_signal = -1
	):
		self.type(type)
		self.amount(amount)
		self.resource(resource)
		self.uid_object(uid_object)
		self.unit_constant(unit_constant)
		self.player_source(player_source)
		self.technology(technology)
		self.timer(timer)
		self.area_upper(area_upper)
		self.area_lower(area_lower)
		self.unit_group(unit_group)
		self.unit_type(unit_type)
		self.ai_signal(ai_signal)

	def type(self, type):
		self._type = type

	def amount(self, amount):
		self._amount = amount

	def resource(self, resource):
		self._resource.set(resource)

	def uid_object(self, uid_object):
		self._uid_object = uid_object

	def uid_location(self, uid_location):
		self._uid_location = uid_location

	def unit_constant(self, unit_constant):
		self._unit_constant = unit_constant)

	def player_source(self, player_source):
		self._player_source = player_source

	def technology(self, technology):
		self._technology = technology

	def timer(self, timer):
		self._timer = timer

	def area_upper(self, loc):
		if loc is not None:
			self._area_upper.x = loc[0]
			self._area_upper.y = loc[1]

	def area_lower(self, loc):
		loc is not None:
			self._area_lower.x = loc[0]
			self._area_lower.y = loc[1]

	def unit_group(self, unit_group):
		self._unit_group.set(unit_group)

	def unit_type(self, unit_type):
		self._unit_type.set(unit_type)

	def ai_signal(self, ai_signal):
		self._ai_signal = ai_signal

class Blank(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(Blank, self).__init__(self, *ordered_args, **keyed_args)
		self.type('Blank')
		
class BringObjectToArea(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(BringObjectToArea, self).__init__(self, *ordered_args, **keyed_args)
		self.type('BringObjectToArea')
		
class BringObjectToObject(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(BringObjectToObject, self).__init__(self, *ordered_args, **keyed_args)
		self.type('BringObjectToObject')
		
class OwnObjects(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(OwnObjects, self).__init__(self, *ordered_args, **keyed_args)
		self.type('OwnObjects')
		
class OwnFewerObjects(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(OwnFewerObjects, self).__init__(self, *ordered_args, **keyed_args)
		self.type('OwnFewerObjects')
		
class ObjectsInArea(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(ObjectsInArea, self).__init__(self, *ordered_args, **keyed_args)
		self.type('ObjectsInArea')
		
class DestroyObject(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(DestroyObject, self).__init__(self, *ordered_args, **keyed_args)
		self.type('DestroyObject')
		
class CaptureObject(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(CaptureObject, self).__init__(self, *ordered_args, **keyed_args)
		self.type('CaptureObject')
		
class AccumulateAttribute(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(AccumulateAttribute, self).__init__(self, *ordered_args, **keyed_args)
		self.type('AccumulateAttribute')
		
class ResearchTechnology(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(ResearchTechnology, self).__init__(self, *ordered_args, **keyed_args)
		self.type('ResearchTechnology')
		
class Timer(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(Timer, self).__init__(self, *ordered_args, **keyed_args)
		self.type('Timer')
		
class ObjectSelected(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(ObjectSelected, self).__init__(self, *ordered_args, **keyed_args)
		self.type('ObjectSelected')
		
class AISignal(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(AISignal, self).__init__(self, *ordered_args, **keyed_args)
		self.type('AISignal')
		
class PlayerDefeated(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(PlayerDefeated, self).__init__(self, *ordered_args, **keyed_args)
		self.type('PlayerDefeated')
		
class ObjectHasTarget(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(ObjectHasTarget, self).__init__(self, *ordered_args, **keyed_args)
		self.type('ObjectHasTarget')
		
class ObjectVisible(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(ObjectVisible, self).__init__(self, *ordered_args, **keyed_args)
		self.type('ObjectVisible')
		
class ObjectNotVisible(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(ObjectNotVisible, self).__init__(self, *ordered_args, **keyed_args)
		self.type('ObjectNotVisible')
		
class ResearchingTechnology(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(ResearchingTechnology, self).__init__(self, *ordered_args, **keyed_args)
		self.type('ResearchingTechnology')
		
class UnitsGarrisoned(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(UnitsGarrisoned, self).__init__(self, *ordered_args, **keyed_args)
		self.type('UnitsGarrisoned')
		
class DifficultyLevel(Condition):
	def __init__(self, *ordered_args, **keyed_args):
		super(DifficultyLevel, self).__init__(self, *ordered_args, **keyed_args)
		self.type('DifficultyLevel')
		
