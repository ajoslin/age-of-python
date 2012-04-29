from ..scenario import scenario
import unittest
import os

scen_dir = os.getcwd()+'/../scens/'

class TestScenarioSimple(object):
	def setup_class(self):
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'1trigger.scx')

	def test_triggers(self):
		assert len(self.scenario.triggers) == 1, 'Incorrect triggers count'

	def test_trigger_effects(self):
		assert len(self.scenario.triggers[0].effects) == 1, 'Incorrect effect count'

	def test_trigger_conds(self):
		assert len(self.scenario.triggers[0].effects) == 1, 'Incorrect condition count'


if __name__ == '__main__':
	unittest.main()