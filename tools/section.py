import struct

class Section:
    def __init__(self, bytes_data):
        self.position = 0
        self.buffer = bytes_data
        if self.buffer == None:
            self.length = 0
        else:
            self.length = len(self.buffer)

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

    def read_from_file(self, file_to_be_read):
        with open(file_to_be_read, 'rb') as transport_stream:
            raw_data = transport_stream.read()

        self.buffer = bytes(raw_data)
        self.length = len(self.buffer)

    def skip_bytes(self, bytes_to_be_skipped):
        self.position += bytes_to_be_skipped