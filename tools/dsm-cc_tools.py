import struct
raw_data = '1103100680000001FF00005BFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000004300000004737267000000000149534F060000002B000249534F500D878E5C630000010004D8B4470849534F4012010000001600000A00018000000FFFFFFFFF0000000013FA5AA3'

with open('binary.bin', 'wb') as out:
  for chars in range(0, len(raw_data) - 1, 2):
    out.write(struct.pack('=B', int(raw_data[chars:chars+2], 16)))
