import pytest
import filecmp
import os

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def convert_string_to_binary(input_string):
    return int(input_string, 16)

def write_binary_for_each_byte():
    return 0

def test_compare_two_binary_files():
    current_absolute_path = os.path.dirname( os.path.abspath( __file__ ))
    assert filecmp.cmp( current_absolute_path + './question.bin', current_absolute_path +'./answer.bin') == True

def test_string_to_binary():
    input_string = '11'
    assert convert_string_to_binary(input_string) == 0x11

    input_string = '1103'
    assert convert_string_to_binary(input_string) == 0x1103

# def test_write_binary_for_each_byte():
#     assert write_binary_for_each_byte() == 1
