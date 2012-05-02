import struct
import base64
import zlib
import logger
import os

logger = logger.Logger('helpers')

### Helper functions for reading from binary
def read_int(f):
	return struct.unpack('<i', f.read(4))[0]

def read_short(f):
	return struct.unpack('<h', f.read(2))[0]

def read_long(f):
	return struct.unpack('<l', f.read(4))[0]

def read_float(f):
	return struct.unpack('<f', f.read(4))[0]

# When reading a genie str, there is a null char at the end
# Python doesn't use null-terminated strings, ignore null chars
def read_str(f):
	length = read_long(f)
	#read the full length, then take out the nullchar at the end
	return f.read(length)[:length-1] 

### Helper functions for writing to binary
def write_int(f, val):
	f.write( struct.pack('<f', val) )

def write_short(f, val):
	f.write( struct.pack('<h', val) )

def write_long(f, val):
	f.write( struct.pack('<l', val) )

def write_float(f, val):
	f.write( struct.pack('<f', val) )

def write_str(f, val):
	# The len will be one longer because we're adding nullchar at end
	f.write( struct.pack('<l', len(val)+1) )
	f.write(val)
	f.write('\x00')

def read_char(f):
	return struct.unpack('<c', f.read(1))[0]

# Helper functions for deflate(decompress) and inflate(compress) of a given string
def inflate(string):
    return zlib.decompress(string, -15)

def deflate( string_val ):
    return zlib.compress( string_val )[2:]