from ..scenario import scenario
from ..scenario import effect
from ..scenario import condition
import unittest
import os
from ..util import logger

logger = logger.Logger('scenario_test')
scen_dir = os.getcwd()+'/../scens/'

# Test of a simple scenario with 1 trigger and 1 effect and 1 condition
class TestScenarioSimple(object):
	def setup_class(self):
		logger.log('Beginning test: TestScenarioSimple')
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'1trigger.scx')

	def test_triggers_len(self):
		assert len(self.scenario.triggers) == 1, 'Incorrect triggers count'

	def test_trigger_attr_loop(self):
		assert self.scenario.triggers[0].loop == False, 'Loop was read wrong'

	def test_trigger_effect_attr_type(self):
		assert self.scenario.triggers[0].effects[0].eff_type == effect.Type.Blank, 'Effect type was read wrong'

	def test_trigger_conds_len(self):
		assert self.scenario.triggers[0].conditions[0].cond_type == condition.Type.Blank, 'Condition type was read wrong'

# Test of loading eternal blood scenario
class TestScenarioEternalBlood(object):
	def setup_class(self):
		logger.log('Beginning test: TestScenarioEternalBlood')
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'eternal_blood.scx')

	def test_triggers_len(self):
		assert len(self.scenario.triggers) == 2017, 'Trigger count is not 2017'

	def test_trigger_1(self):
		"""Test the second trigger in eternal blood"""
		trigger = self.scenario.triggers[1]
		assert trigger.name == 'PL1 KFC-', 'Name is wrong'

		assert len(trigger.conditions) == 1, 'Conditions len is wrong'
		assert trigger.conditions[0].cond_type == condition.Type.AccumulateAttribute, 'Cond0 type is not AccumulateAttribute'
		assert trigger.conditions[0].amount == 5, 'Cond0 Amount is not 5'
		assert trigger.conditions[0].player == 1, 'Cond0 player is not 1'

		assert len(trigger.effects) == 3, 'Effects len is wrong'
		assert triggers.effects[2].eff_type == effect.Type.CreateObject, 'Effect0 type is not CreateObject'
		assert triggers.effects[2].unit_constant == 601, 'Effect0 unit constant is not flag B'
		assert triggers.effects[2].player == 1, 'Effect0 player is wrong'


if __name__ == '__main__':
	unittest.main()