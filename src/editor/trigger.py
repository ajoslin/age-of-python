from ..scenario import trigger

class Trigger(trigger.Trigger):

	# User can fully define a trigger in constructor or use methods.
	def __init__(self, 
		name='New Trigger', 
		description='',
		on=False,
		loop=True,
		objective=None,
		effects=[],
		conditions=[]
	):
		self.name(name)
		self.description(description)
		self.on(on)
		self.loop(loop)
		self.objective(objective)
		self.order(order)

	def name(self, name):
		self._name=name

	def description(self, desc):
		self._description=desc

	def on(self, on):
		self._on=on

	def loop(self, loop):
		self._loop=loop

	# User will just type None or a number for objective
	# if he types none, we count objective as false
	# if he types a number, we count objective as true and
	# that as the objective order.
	def objective(self, obj_order):
		if obj_order is None:
			self._objective = False
			self._obj_order = 0
		else:
			self._objective = True
			self._obj_order = obj_order

	def effect(self, effect):
		self._effects.append(effect)

	def condition(self, cond):
		self._conditions.append(cond)