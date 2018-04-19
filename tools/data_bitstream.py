import struct

class DataBitstream():
    def __init__(self):
        self.buffer = None
        self.position = 0

    def setData(self, bitstream):
        self.buffer = bytes(bitstream)
        self.position = 0

    def length(self):
        return len(self.buffer)

    def get_bytes(self, bytes_to_be_read):
        if bytes_to_be_read == 1:
            format = '!B'
        elif bytes_to_be_read == 2:
            format = '!H'
        elif bytes_to_be_read == 4:
            format = '!I'    
        else:
            raise NotImplementedError

        converted_value = struct.unpack(format, self.buffer[self.position:self.position + bytes_to_be_read])[0]
        self.position += bytes_to_be_read

        return converted_value        

if __name__ == '__main__':
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10]
    input_bytes = bytes(input_numbers)

    data_partition = DataBitstream()
    data_partition.setData(input_bytes)

    print(data_partition.buffer)    