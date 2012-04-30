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
		assert len(self.scenario.triggers) == 1

	def test_trigger_attr_loop(self):
		assert self.scenario.triggers[0].loop == False

	def test_trigger_cond_effect_type(self):
		triggers = self.scenario.triggers
		assert triggers[0].effects[0].eff_type == effect.Type.Blank
		assert triggers[0].conditions[0].cond_type == condition.Type.Blank

# Test of loading eternal blood scenario
class TestScenarioEternalBlood(object):
	def setup_class(self):
		logger.log('Beginning test: TestScenarioEternalBlood')
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'eternal_blood.scx')

	def test_triggers_len(self):
		assert len(self.scenario.triggers) == 2017

	def test_trigger_1(self):
		"""Test the second trigger in eternal blood"""
		trigger = self.scenario.triggers[1]
		# have to add nullchar when testing string equality because
		# genie reads in a null char for all strings
		assert trigger.name == 'PL1 KFC-'

		assert len(trigger.conditions) == 1
		assert trigger.conditions[0].cond_type == condition.Type.AccumulateAttribute
		assert trigger.conditions[0].amount == 5
		assert trigger.conditions[0].player == 1

		assert len(trigger.effects) == 3
		assert trigger.effects[2].eff_type == effect.Type.CreateObject
		assert trigger.effects[2].unit_constant == 601
		assert trigger.effects[2].player_source == 1

# Test loading of star td scenario
class TestScenarioStarTowerDefense(object):
	def setup_class(self):
		logger.log('Beginning test: TestScenarioStarTowerDefense')
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'star_td.scx')

	def test_triggers_len(self):
		assert len(self.scenario.triggers) == 469

	def test_trigger_last_attrs(self):
		trigger = self.scenario.triggers[468]

		assert trigger.name == 'Stop towers on resource isles'
		assert trigger.loop == True
		assert trigger.on == True
		assert len(trigger.conditions) == 0
		assert len(trigger.effects) == 8
		assert trigger.effects[2].eff_type == effect.Type.KillObject
		assert trigger.effects[2].player_source == 3

if __name__ == '__main__':
	unittest.main()