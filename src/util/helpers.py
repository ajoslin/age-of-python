import struct
import base64
import zlib
import logger

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
	s = ''
	for i in range(length):
		c = struct.unpack('<c', f.read(1))[0]
		if c != '\x00': s += c
	return s

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
	# add a null char at the end
	val += '\x00'
	length = len(val)
	f.write( struct.pack('<l', length) )
	for i in range(length):
		f.write( struct.pack('<c', val[i]) )

def read_char(f):
	return struct.unpack('<c', f.read(1))[0]

# Helper functions for deflate(decompress) and inflate(compress) of a given string
def inflate( b64string ):
    # decoded_data = base64.b64decode( b64string )
    return zlib.decompress( b64string , -15)

def deflate( string_val ):
    zlibbed_str = zlib.compress( string_val )
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( compressed_string )