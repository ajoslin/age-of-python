import os
import struct
import aoplogger
import zlib

# Instantiate logger object, and let it know it'll
# be scenario module creating the log entries
logger = aoplogger.logger('scenario')

class Scenario(object):

	def __init__(self, path):
		"""Create a scenario from given path"""
		logger.log('Creating new scenario. path='+path)

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
		# get decompressed string
		decompressed_data = zlib.decompress(scn_file.read(), 13)
		decompressed_len = len(decompressed_data)
		decompr_path = path+'.decompr.hex'
		logger.log('decompression done. decompressed_len=%d', decompressed_len)
		# write it to a new file, close the old one
		logger.log('writing decompressed data to %s', decompr_path)
		scn_file.close()
		decompr_file = open(decompr_path, 'wb')
		decompr_file.write(decompressed_data)
		# move back to beginning of file after writing the data
		logger.log('writing done')
		scn_file.seek(0, os.SEEK_SET)
		# send skip_misc_data the decompressed data
		misc_data_len = skip_misc_data(decompressed)
		logger.log('misc data skipped. misc_data_len=%d', misc_data_len)

		logger.log('reading triggers...')
		ntriggers = long(f.read(8))
		logger.log('numtriggers=%d', ntriggers)

def _read_int(f):
	return struct.unpack('<i', f.read(4))[0]

def _read_short(f):
	return struct.unpack('<h', f.read(2))[0]

def _read_long(f):
	return struct.unpack('<l', f.read(4))[0]

def _read_float(f):
	return struct.unpack('<f', f.read(4))[0]

def skip_header(f):
	f.read(4) # skip header version str
	header_len = _read_long(f)
	header = f.read(header_len)
	return 4+8+header_len

# if you want in-depth log about scenario structure, check out 
# aokts or trigedit source. these comments skip a lot
def skip_misc_data(f):
	f.read(4433) # CHeader
	f.read( 24+int(f.read(2)) ) # name
	f.read( int(f.read(2)) ) # instructions
	f.read( int(f.read(2)) ) # hints
	f.read( int(f.read(2)) ) # victory
	f.read( int(f.read(2)) ) # defeat
	f.read( int(f.read(2)) ) # history
	f.read( int(f.read(2)) ) # scouts
	f.read( int(f.read(2)) ) # pg_cinem
	f.read( int(f.read(2)) ) # vict_cinem
	f.read( int(f.read(2)) ) # lost_cinem
	f.read( int(f.read(2)) ) # background_cinem
	hasbmp = long(f.read(8)) # bool stored as long, hasbmp?
	f.read(8+8+2) #sizex of bmp + sizey of bmp + unknown
	if hasbmp!=0:
		f.read(20) # misc
		f.read( 16+1024+long(f.read(8)) ) #skip bmp
	for i in range(32+16): f.read( int(f.read(2)) ) # 32 unknowns, 16 ai names
	for i in range(16): f.read ( 8+long(f.read(8)) ) # 16 ai files
	f.read(16) # 16 ai types
	f.read(4) # random seperator
	# resources for each player: gold/wood/food/stone/porex/unknown
	for i in range(16): f.read(6*8) 
	f.read(4*8) # victory stuff
	f.read(12) # mode/score/time
	f.read(64+30*64+64+30*64+64+20*64+8+4) #tech stuff
	f.read(16*4+4+8+4) # starting age, unkn, camera pos, aitype
	f.read( long(f.read(8)) * long(f.read(8)) * 3 ) #mapx*mapy*(id,elv,null)
	f.read(8+8*28) #numplayers, playerdata part 4
	for i in range(8): #players 0-8
		count = long(f.read(8)) #unitcount
		for j in range(count):
			f.read(4+4+4+4+2+1+4+2+8) # unit log
	f.read(4) #seperator
	for i in range(8): #player data 3
		f.read( int(f.read(2)) ) #playername
		f.read(8+4+1) #cameras/unk/alliedvictory
		f.read( 5*int(f.read(2)) ) #diplomacies
		f.read(4) #color
		f.read( int(f.read(4))*4 ) #??? pldata
		f.read(9+4) #ending long
	f.read(8) #constant
	f.read(1)
	return f.tell()
