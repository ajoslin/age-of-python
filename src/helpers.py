import struct

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
	return struct.unpack('<s', f.read(length))