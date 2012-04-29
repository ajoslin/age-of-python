from ..util import helpers 
from ..util import logger

logger = logger.Logger('condition')

class Condition(object):
	def __init__(self):
		logger.log("creating new condition")


	def read(self, scn_file):
		""" Read condition from scenario file """

