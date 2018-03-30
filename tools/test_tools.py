import pytest
import filecmp
import struct
import os

def convert_string_to_binary(input_string):
    return int(input_string, 16)

def write_binary_for_each_byte(input_string):
    hex_values = []
    strip_string = ''.join(input_string.split()) # https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string-in-python
    for i in range(0, len(strip_string) - 1, 2):
        hex_value = convert_string_to_binary(strip_string[i:i+2])
        hex_values.append(hex_value)
    
    output_file_name = 'input_string.bin'
    with open(os.path.dirname( os.path.abspath( __file__ )) + '/' + output_file_name, 'wb') as bin_file:
        for byte in hex_values:
            bin_file.write(struct.pack('B', byte)) # https://stackoverflow.com/questions/18367007/python-how-to-write-to-a-binary-file

    return output_file_name

def compare_two_binary_files(to_be_checked, reference):
    current_absolute_path = os.path.dirname( os.path.abspath( __file__ ))
    return filecmp.cmp( current_absolute_path + '/' + to_be_checked, current_absolute_path + '/' + reference)


def get_hex_value(bytes_data, pos, num_of_bytes):
    if num_of_bytes == 1:
        format = '!B'
    elif num_of_bytes == 2:
        format = '!H'
    elif num_of_bytes == 4:
        format = '!I'    
    
    return struct.unpack(format, bytes_data[pos:pos + num_of_bytes])[0]

def test_compare_two_binary_files():
    assert compare_two_binary_files('question.bin', 'answer.bin') == True

def test_string_to_binary():
    input_string = '11'
    assert convert_string_to_binary(input_string) == 0x11

    input_string = '1103'
    assert convert_string_to_binary(input_string) == 0x1103

def test_write_binary_for_each_byte():
    input_string_dsi = '''
    1103 1006 8000 0001 FF00 005B FFFF FFFF  
    FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF 
    0000 0043 0000 0004 7372 6700 0000 0001 
    4953 4F06 0000 002B 0002 4953 4F50 0D87 
    8E5C 6300 0001 0004 D8B4 4708 4953 4F40 
    1201 0000 0016 0000 0A00 0180 0000 0FFF 
    FFFF FF00 0000 0013 FA5A A3             
    '''
    assert compare_two_binary_files(write_binary_for_each_byte(input_string_dsi), 'ref_dsm-cc_dsi.bin')

def test_hex_values():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e]
    input_bytes = bytes(input_numbers)
    assert struct.unpack('!B', input_bytes[0:1])[0] == 0x0a # check one byte
    assert struct.unpack('!H', input_bytes[0:2])[0] == 0x0a0b # check two bytes
    assert struct.unpack('!I', input_bytes[0:4])[0] == 0x0a0b0c0d # check four bytes

    assert struct.unpack('!B', input_bytes[1:2])[0] == 0x0b # check one byte
    assert struct.unpack('!H', input_bytes[1:3])[0] == 0x0b0c # check two bytes
    assert struct.unpack('!I', input_bytes[1:5])[0] == 0x0b0c0d0e # check four bytes
    
    assert get_hex_value(input_bytes, 0, 1) == 0x0a # check one byte
    assert get_hex_value(input_bytes, 0, 2) == 0x0a0b # check two bytes
    assert get_hex_value(input_bytes, 0, 4) == 0x0a0b0c0d # check four bytes

    assert get_hex_value(input_bytes, 1, 1) == 0x0b # check one byte
    assert get_hex_value(input_bytes, 1, 2) == 0x0b0c # check two bytes
    assert get_hex_value(input_bytes, 1, 4) == 0x0b0c0d0e # check four bytes

def test_section():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10]
    section_data = bytes(input_numbers)
    position = 0

    bytes_to_be_read = 1
    assert get_hex_value(section_data, position, bytes_to_be_read) == 0x0a
    position += bytes_to_be_read

    bytes_to_be_read = 2
    assert get_hex_value(section_data, position, bytes_to_be_read) == 0x0b0c
    position += bytes_to_be_read   

    bytes_to_be_read = 4
    assert get_hex_value(section_data, position, bytes_to_be_read) == 0x0d0e0f10
    position += bytes_to_be_read      