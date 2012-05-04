from ..scenario import scenario
from ..scenario import effect
from ..scenario import condition
import unittest
import os
from ..util import logger
import scenario_read_test

scen_dir = os.getcwd()+'/../scens/'
logger = logger.Logger('scenario_write_test')

# Scenario write tests are just like the read tests, 
# except it reads the scen, writes a new version of it,
# then re-reads it to check if it's ok
class TestScenarioWriteSimple(scenario_read_test.TestScenarioReadSimple):
	def setup_class(self):
		logger.log('Beginning test: TestScenarioWriteSimple')
		original_scen = scenario.Scenario()
		original_scen.read(scen_dir+'1trigger.scx')
		original_scen.write(scen_dir+'1trigger_out.scx')
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'1trigger_out.scx')

class TestScenarioWriteEternalBlood(scenario_read_test.TestScenarioReadEternalBlood):
	def setup_class(self):
		logger.log('Beginning test: TestScenarioWriteEternalBlood')
		original_scen = scenario.Scenario()
		original_scen.read(scen_dir+'eternal_blood.scx')
		original_scen.write(scen_dir+'eternal_blood_out.scx')
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'eternal_blood_out.scx')

class TestScenarioWriteStarTD(scenario_read_test.TestScenarioReadStarTD):
	def setup_class(self):
		logger.log('Beginning test: TestScenarioWriteStarTD')
		original_scen = scenario.Scenario()
		original_scen.read(scen_dir+'star_td.scx')
		original_scen.write(scen_dir+'star_td_out.scx')
		self.scenario = scenario.Scenario()
		self.scenario.read(scen_dir+'star_td_out.scx')