import os
import gzip
import trigger
from ..util import helpers 
from ..util import logger

# Instantiate logger object, and let it know it'll
# be scenario module creating the log entries
logger = logger.Logger('scenario')

class Scenario(object):

	triggers = []

	def __init__(self):
		logger.log('Creating new scenario')

	def read(self, path):
		"""Reads from given path"""
		"""Steps:"""
		"""1. Open scenario, skip the header (header is uncompressed)"""
		"""2. Decompress everything after the header (rest of scn data)"""
		"""3. Skip all the data through to triggers"""
		logger.log('Reading scenario. path='+path)

		# open the file
		scn_file = open(path, 'rb')
		scn_len = os.stat(path).st_size
		logger.log('Opened scenario. length=%d', scn_len)

		# skip uncompressed header string
		logger.log('skipping header...')
		header_len = skip_header(scn_file)
		logger.log('header skipped. header_len=%d', header_len)

		# decompress everything after header
		logger.log('decompressing data...')
		# get decompressed string through zlib
		decompressed_data = helpers.inflate(scn_file.read())
		decompressed_len = len(decompressed_data)
		logger.log('decompression done. decompressed_len=%d', decompressed_len)

		# write decompressed data to a new file, close the old one
		scn_file.close()
		decompr_path = path+'.decompr.hex'
		logger.log('writing decompressed data to %s', decompr_path)
		decompr_file = open(decompr_path, 'wb')
		decompr_file.write(decompressed_data)
		decompr_file.close()
		logger.log('writing done')

		# re-open decompressed data file for reading
		decompr_file = open(decompr_path, 'rb')

		# send skip_misc_data the decompressed data
		logger.log('skipping misc data...')
		misc_data_len = skip_misc_data(decompr_file)
		logger.log('misc data skipped. misc_data_len=%d', misc_data_len)

		# Now read the triggers
		logger.log('reading triggers...')
		ntriggers = helpers.read_long(decompr_file)
		logger.log('numtriggers=%d', ntriggers)

		for i in range(ntriggers):
			t = trigger.trigger().read(decompr_file)
			self.triggers.append(t)



# Skips the header 
def skip_header(f):
	f.read(4) # skip header version str
	header_len = helpers.read_long(f)
	header = f.read(header_len)
	return 8+header_len

# Skips all the data before triggers
# Note: if you want in-depth info about scenario structure, check out 
# digit's aokts source or jatayu's trigedit source.
# these comments are cursory and only tell you a tiny bit
def skip_misc_data(f):
	f.read(4433) # CHeader
	f.read( 24+helpers.read_short(f) ) # name
	f.read( helpers.read_short(f) ) # instructions
	f.read( helpers.read_short(f) ) # hints
	f.read( helpers.read_short(f) ) # victory
	f.read( helpers.read_short(f) ) # defeat
	f.read( helpers.read_short(f) ) # history
	f.read( helpers.read_short(f) ) # scouts
	f.read( helpers.read_short(f) ) # pg_cinem
	f.read( helpers.read_short(f) ) # vict_cinem
	f.read( helpers.read_short(f) ) # lost_cinem
	f.read( helpers.read_short(f) ) # background_cinem
	hasbmp = helpers.read_long(f) # bool stored as long, hasbmp?
	f.read(4+4+2) #sizex of bmp + sizey of bmp + unknown
	if hasbmp!=0:
		f.read(20) # misc
		f.read( 16+1024+helpers.read_long(f) ) #skip bmp
	for i in range(32): f.read( helpers.read_short(f) ) # 32 unknowns
	for i in range(16): f.read( helpers.read_short(f) ) # 16 ai names
	for i in range(16): f.read( 8+helpers.read_long(f) ) # 16 ai files
	f.read(16) # 16 ai types
	f.read(4) # random seperator
	# resources for each player: long gold/wood/food/stone/porex/unknown
	for i in range(16): f.read(6*4) 
	f.read(4*8) # victory stuff
	f.read(12) # mode/score/time
	f.read(16*16*4) # diplo: 16x16 longs
	f.read(11520+4) #random bytes + seperator
	f.read(64) #16 long allied victories
	f.read(64) # 16 longs num disabled techs
	f.read(64*30) #16*30 longs disabled techs
	f.read(64) #num disabled units 16 longs
	f.read(64*30) #disabled units 16*30 longs
	f.read(64) #num disabled buildings
	f.read(64*20) #disabled buildings
	f.read(12) #null longs and all techs
	f.read(16*4) # starting age,
	f.read(4*4) # unkn, camerax, cameray, aitype
	mapx = helpers.read_long(f)
	mapy = helpers.read_long(f)
	logger.log('mapx,mapy = %d,%d', mapx, mapy)
	f.read( mapx * mapy * 3 ) #mapx*mapy*(id,elv,null)

	f.read(4) #numplayers
	f.read(8*28) #playerdata part 4
	for i in range(8): #players 0-8
		count = helpers.read_long(f) #unitcount
		for j in range(count):
			f.read(4+4+4+4+2+1+4+2+4) # unit info
	f.read(8) #seperator
	for i in range(8): #player data 3
		f.read( helpers.read_short(f) ) #playername
		f.read(8+4+1) #cameras/unk/alliedvictory
		diplolen = helpers.read_short(f)
		f.read( 5*diplolen ) #diplomacies
		f.read(4) #color
		f.read( int(helpers.read_float(f))*4 ) #??? pldata
		f.read(9+4) #9 nulls and ending long
	f.read(8) #constant
	f.read(1) # skip first byte of trigger-data
	return f.tell() #return how many bytes we skipped
