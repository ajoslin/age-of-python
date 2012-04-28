import aoplogger

logger = aoplogger.logger('effect')

class Effect(object):
	def __init__(self):
		logger.log("creating new effect")


	def read(self, scn_file):
		"""Read effect from scenario file"""

