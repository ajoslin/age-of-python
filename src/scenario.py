import os
import aoplogger
import zlib
import trigger
import helpers

# Instantiate logger object, and let it know it'll
# be scenario module creating the log entries
logger = aoplogger.logger('scenario')

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
		decompressed_data = zlib.decompress(scn_file.read())
		decompressed_len = len(decompressed_data)
		logger.log('decompression done. decompressed_len=%d', decompressed_len)

		# write decompressed data to a new file, close the old one
		scn_file.close()
		decompr_path = path+'.decompr.hex'
		logger.log('writing decompressed data to %s', decompr_path)
		decompr_file = open(decompr_path, 'wb')
		decompr_file.write(decompressed_data)
		# move back to beginning of file after writing the data
		logger.log('writing done')
		scn_file.seek(0, os.SEEK_SET)
		# send skip_misc_data the decompressed data
		misc_data_len = skip_misc_data(decompressed)
		logger.log('misc data skipped. misc_data_len=%d', misc_data_len)

		# Now read the triggers
		logger.log('reading triggers...')
		ntriggers = helpers.read_long(f)
		logger.log('numtriggers=%d', ntriggers)

		for i in range(ntriggers):
			t = trigger.Trigger().read(f)
			self.triggers.append(t)

# Skips the header 
def skip_header(f):
	f.read(4) # skip header version str
	header_len = helpers.read_long(f)
	header = f.read(header_len)
	return 4+8+header_len

# Skips all the data before triggers
# if you want in-depth info about scenario structure, check out 
# digit's aokts or jatayu's trigedit source.
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
	f.read(8+8+2) #sizex of bmp + sizey of bmp + unknown
	if hasbmp!=0:
		f.read(20) # misc
		f.read( 16+1024+helpers.read_long(f) ) #skip bmp
	for i in range(32+16): f.read( helpers.read_short(f) ) # 32 unknowns, 16 ai names
	for i in range(16): f.read ( 8+helpers.read_long(f) ) # 16 ai files
	f.read(16) # 16 ai types
	f.read(4) # random seperator
	# resources for each player: gold/wood/food/stone/porex/unknown
	for i in range(16): f.read(6*8) 
	f.read(4*8) # victory stuff
	f.read(12) # mode/score/time
	f.read(64+30*64+64+30*64+64+20*64+8+4) #tech stuff
	f.read(16*4+4+8+4) # starting age, unkn, camera pos, aitype
	f.read( helpers.read_long(f) * helpers.read_long(f) * 3 ) #mapx*mapy*(id,elv,null)
	f.read(8+8*28) #numplayers, playerdata part 4
	for i in range(8): #players 0-8
		count = helpers.read_long(f) #unitcount
		for j in range(count):
			f.read(4+4+4+4+2+1+4+2+8) # unit log
	f.read(4) #seperator
	for i in range(8): #player data 3
		f.read( helpers.read_short(f) ) #playername
		f.read(8+4+1) #cameras/unk/alliedvictory
		f.read( 5*helpers.read_short(f) ) #diplomacies
		f.read(4) #color
		f.read( helpers.read_float(f)*4 ) #??? pldata
		f.read(9+4) #ending long
	f.read(8) #constant
	f.read(1) # skip first byte of trigger-data
	return f.tell() #return how many bytes we skipped
