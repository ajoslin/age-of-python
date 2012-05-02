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
		logger.log('Reading scenario. path='+path)

		# open the file
		scn_file = open(path, 'rb')
		logger.log('Opened scenario. length=%d', os.stat(path).st_size)

		# Skip the header
		logger.log('reading header...')
		header_len = skip_header(scn_file);
		# now we have to save the header data for writing later
		f = open(path, 'rb')
		self.header_data = f.read(header_len)
		f.close()

		logger.log('header read. header_len=%d', header_len+4)

		# decompress everything after header
		logger.log('decompressing data...')
		# get decompressed string through zlib
		decompressed_data = helpers.inflate(scn_file.read())
		decompressed_len = len(decompressed_data)
		logger.log('decompression done. decompressed_len=%d', decompressed_len)

		# write decompressed data to a new file, close the old one
		scn_file.close()
		decompr_path = path+'.hex'
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

		# Now we are going to save the before triggers data
		# re-open the decompressed file from start to do this
		# We'll need this data when we write
		f = open(decompr_path, 'rb')
		self.before_triggers_data = f.read(misc_data_len)
		f.close()

		# Now read the triggers
		logger.log('reading triggers...')
		ntriggers = helpers.read_long(decompr_file)
		logger.log('ntriggers=%d', ntriggers)

		# create temporary array for triggers, will fill in self.triggers later
		# with actual trigger order
		triggers_tmp = []
		for i in range(ntriggers):
			t = trigger.Trigger()
			t.read(decompr_file)
			triggers_tmp.append(t)

		# now fill in trigger order
		self.triggers = []
		for i in range(ntriggers):
			order = helpers.read_long(decompr_file)
			self.triggers.append(triggers_tmp[i])

		logger.log('trigger reading done.')
		logger.log('trigger end = %d', decompr_file.tell())

		# Save everything else after triggers to memory
		# For writing
		self.after_triggers_data = decompr_file.read()

		# Close our decompressed data file and remove it
		decompr_file.close()
		os.remove(decompr_path)

	def write(self, path):
		logger.log("Writing scenario to %s", path)
		# write needs the scenario to have been read before
		if self.header_data == None or self.before_triggers_data == None or self.after_triggers_data == None:
			raise Exception("Error in write! Scenario must be read before writing")

		# We have to write all the decompressed data to a file then compress it
		# First write all the data
		decompr_path = path+'.hex'
		decompr_file = open(decompr_path, 'wb')
		decompr_file.write(self.before_triggers_data)

		# Write trigger count
		helpers.write_long(decompr_file, len(self.triggers))
		# Write triggers
		for i in range( len(self.triggers) ):
			self.triggers[i].write(decompr_file)
		# Write trigger order
		for i in range( len(self.triggers) ):
			helpers.write_long(decompr_file, i)

		# Write everything after triggers and close
		decompr_file.write(self.after_triggers_data)
		decompr_file.close()

		# Now read all the data to a string then compress that string
		decompr_file = open(decompr_path, 'rb')
		compressed_data = helpers.deflate( decompr_file.read() )
		# Close and remove .hex, we're done with decompressed data
		decompr_file.close()
		os.remove(decompr_path)

		# Now we just have to write header and compressed data to given path
		scn_file = open(path, 'wb')
		scn_file.write(self.header_data)
		scn_file.write(compressed_data)
		scn_file.close()




# Skips the uncompressed header and returns length of it
def skip_header(f):
	f.read(4) # skip 4-char version header
	header_len = helpers.read_long(f) # length of header
	f.read(header_len)
	return header_len + 8

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
		f.read(4+4+2+2+4) # misc
		bmp_size = helpers.read_long(f)
		f.read(16)
		f.read(bmp_size+1024)
	# logger.log('after bmp=%d', f.tell())
	for i in range(32): f.read( helpers.read_short(f) ) # 32 unknowns
	for i in range(16): f.read( helpers.read_short(f) ) # 16 ai names
	# logger.log('after 16 ai names=%d', f.tell())
	for i in range(16):
		f.read(8)
		ai_len = helpers.read_long(f)
		f.read(ai_len)
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
	# logger.log('mapx,mapy = %d,%d', mapx, mapy)
	f.read( mapx * mapy * 3 ) #mapx*mapy*(id,elv,null)

	f.read(4) #numplayers
	f.read(8*28) #playerdata part 4
	# logger.log('after playerdata part4=%d', f.tell())
	###
	# TODO?: Consider reading these units in and saving them to scenario,
	# then restrict what units user can pick based on it
	###
	for i in range(9): #players 0-8
		count = helpers.read_long(f) #unitcount
		# logger.log('count for player %d = %d', 1+i, count)
		for j in range(count):
			f.read(4+4) #xpos, ypos float
			f.read(4) # unknown long
			f.read(4) #uid long
			f.read(2 + 1) #unknown short + byte
			f.read(4) #rotation float
			f.read(2) #frame short
			f.read(4) #garrison long
			
	# logger.log('after unit data=%d', f.tell())
	f.read(4) #seperator
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
	