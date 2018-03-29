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
