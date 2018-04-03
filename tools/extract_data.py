import os
import struct

class ExtractData:
    def __init__(self, input_string):
        hex_values = []

        if input_string != None:
            strip_string = ''.join(input_string.split()) # https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string-in-python
            for i in range(0, len(strip_string) - 1, 2):
                hex_value = int(strip_string[i:i+2], 16)
                hex_values.append(hex_value)    

        self.buffer = hex_values

    def set_buffer(self, input_string):
        hex_values = []

        if input_string != None:
            strip_string = ''.join(input_string.split()) # https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string-in-python
            for i in range(0, len(strip_string) - 1, 2):
                hex_value = int(strip_string[i:i+2], 16)
                hex_values.append(hex_value)    

        self.buffer = hex_values

    def write(self, output_file_name):
        with open(os.path.dirname( os.path.abspath( __file__ )) + '/' + output_file_name, 'wb') as bin_file:
            for byte in self.buffer:
                bin_file.write(struct.pack('B', byte)) # https://stackoverflow.com/questions/18367007/python-how-to-write-to-a-binary-file        
    
if __name__ == "__main__":
    dii_raw_string = '''
    1103 1002 8000 000F FF00 006D 878E 5C63
    0FE2 0000 0000 0000 0000 0000 0000 0003
    0000 0000 034C 0D15 FFFF FFFF FFFF FFFF
    FFFF FFFF 0100 0000 1700 0000 0000 0900
    0005 710C 15FF FFFF FFFF FFFF FFFF FFFF
    FF01 0000 0017 0000 0000 000B 0000 2556
    0C15 FFFF FFFF FFFF FFFF FFFF FFFF 0100
    0000 1700 0000 0000 00F4 2B7C 0B       
    '''
    dii = ExtractData(None)
    
    dii.set_buffer(dii_raw_string)
    dii.write('ref_dsm-cc_dii.bin')
