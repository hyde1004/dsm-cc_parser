import pytest
import section

def test_section_init():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e]
    input_bytes = bytes(input_numbers)
    dsi = section.Section(input_bytes)

    assert dsi.buffer[0] == 0x0a # 1st value
    assert dsi.buffer[1] == 0x0b # 2nd value
    assert dsi.buffer[2] == 0x0c # 3rd value

def test_section_read_one_byte():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e]
    input_bytes = bytes(input_numbers)
    dsi = section.Section(input_bytes)    

    assert dsi.get_bytes(1) == 0x0a # 1st value
    assert dsi.position == 1 # new position

    assert dsi.get_bytes(1) == 0x0b # 2nd value
    assert dsi.position == 2 # new position

    assert dsi.get_bytes(1) == 0x0c # 3rd value
    assert dsi.position == 3 # new position

def test_section_read_two_bytes():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e]
    input_bytes = bytes(input_numbers)
    dsi = section.Section(input_bytes)   

    assert dsi.get_bytes(2) == 0x0a0b # read two bytes
    assert dsi.position == 2

    assert dsi.get_bytes(2) == 0x0c0d # read two bytes
    assert dsi.position == 4

def test_section_read_four_bytes():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e]
    input_bytes = bytes(input_numbers)
    dsi = section.Section(input_bytes)

    assert dsi.get_bytes(4) == 0x0a0b0c0d
    assert dsi.position == 4   

def test_section_read_random():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x010]
    input_bytes = bytes(input_numbers)
    dsi = section.Section(input_bytes)   

    assert dsi.get_bytes(1) == 0x0a
    assert dsi.position == 1

    assert dsi.get_bytes(2) == 0x0b0c
    assert dsi.position == 3

    assert dsi.get_bytes(4) == 0x0d0e0f10
    assert dsi.position == 7 
    
def test_section_read_from_file():
    dsi = section.Section(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')

    assert dsi.buffer[0] == 0x11
    assert dsi.buffer[1] == 0x03
    assert len(dsi.buffer) == 0x6B # length
    assert dsi.length == 0x6B # length