import struct
import base64
import zlib

### Helper functions for reading from binary
def read_int(f):
	return struct.unpack('<i', f.read(4))[0]

def read_short(f):
	return struct.unpack('<h', f.read(2))[0]

def read_long(f):
	return struct.unpack('<l', f.read(4))[0]

def read_float(f):
	return struct.unpack('<f', f.read(4))[0]

def read_str(f):
	length = read_long(f)
	return struct.unpack('<s', f.read(length))[0]

# Helper functions for deflate(decompress) and inflate(compress) of a given string
def inflate( b64string ):
    # decoded_data = base64.b64decode( b64string )
    return zlib.decompress( b64string , -15)

def deflate( string_val ):
    zlibbed_str = zlib.compress( string_val )
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( compressed_string )