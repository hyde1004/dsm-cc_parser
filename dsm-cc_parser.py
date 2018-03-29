import pytest
import struct

# https://www.devdungeon.com/content/working-binary-data-python

data = []
pos = 0

def read_bytes(num_of_bytes):
    return data[pos:pos+num_of_bytes]

def read_data_from_file(to_be_read_file):
    with open(to_be_read_file, 'rb') as transport_stream:
        return transport_stream.read()

def parse_dsi():
    # parse header
    pass

data = read_data_from_file('tools/ref_dsm-cc_dsi.bin')
parse_dsi()
print(data[0])
print(bytes(data[0:1]))
header = struct.unpack('B', bytes(data[0:1]))[0]
print(header)