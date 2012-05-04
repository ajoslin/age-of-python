from ..scenario import scenario
from ..scenario import effect
from ..scenario import condition
import unittest
import os
from ..util import logger

logger = logger.Logger('scenario_read_test')
scen_dir = os.getcwd()+'/../scens/'

# Test of a simple scenario with 1 trigger and 1 effect and 1 condition
class TestScenarioReadSimple(object):
	def setup_class(self):
		logger.log('Beginning test: TestScenarioReadSimple')
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'1trigger.scx')

	def test_triggers_len(self):
		assert len(self.scenario.triggers) == 1

	def test_trigger_attr_loop(self):
		assert self.scenario.triggers[0]._loop == False

	def test_trigger_cond_effect_type(self):
		triggers = self.scenario.triggers
		assert triggers[0]._effects[0]._eff_type.key() == 'Blank'
		assert triggers[0]._conditions[0]._cond_type.key() == 'Blank'

# Test of loading eternal blood scenario
class TestScenarioReadEternalBlood(object):
	def setup_class(self):
		logger.log('Beginning test: TestScenarioReadEternalBlood')
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'eternal_blood.scx')

	def test_triggers_len(self):
		assert len(self.scenario.triggers) == 2017

	def test_trigger_1(self):
		"""Test the second trigger in eternal blood"""
		trigger = self.scenario.triggers[1]
		# have to add nullchar when testing string equality because
		# genie reads in a null char for all strings
		assert trigger._name == 'PL1 KFC-'

		assert len(trigger._conditions) == 1
		assert trigger._conditions[0]._cond_type.key() == 'AccumulateAttribute'
		assert trigger._conditions[0]._amount == 5
		assert trigger._conditions[0]._player_source == 1

		assert len(trigger._effects) == 3
		assert trigger._effects[2]._eff_type.key() == 'CreateObject'
		assert trigger._effects[2]._unit_constant == 601
		assert trigger._effects[2]._player_source == 1

# Test loading of star td scenario
class TestScenarioReadStarTD(object):
	def setup_class(self):
		logger.log('Beginning test: TestScenarioReadStarTD')
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'star_td.scx')

	def test_triggers_len(self):
		assert len(self.scenario.triggers) == 469

	def test_trigger_last_attrs(self):
		trigger = self.scenario.triggers[468]

		assert trigger._name == 'Stop towers on resource isles'
		assert trigger._loop == True
		assert trigger._on == True
		assert len(trigger._conditions) == 0
		assert len(trigger._effects) == 8
		assert trigger._effects[2]._eff_type.key() == 'KillObject'
		assert trigger._effects[2]._player_source == 3

if __name__ == '__main__':
	unittest.main()