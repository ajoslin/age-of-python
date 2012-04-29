from ..util import helpers 
from ..util import logger

logger = logger.Logger('effect')

class Effect(object):
	def __init__(self):
		logger.log("creating new effect")


	def read(self, scn_file):
		"""Read effect from scenario file"""

