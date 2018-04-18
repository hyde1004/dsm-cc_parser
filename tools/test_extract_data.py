import pytest
import extract_data
import os
import filecmp

def test_extract_data_init():
    input_string_dsi = '''
    1103 1006 8000 0001 FF00 005B FFFF FFFF  
    FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF 
    0000 0043 0000 0004 7372 6700 0000 0001 
    4953 4F06 0000 002B 0002 4953 4F50 0D87 
    8E5C 6300 0001 0004 D8B4 4708 4953 4F40 
    1201 0000 0016 0000 0A00 0180 0000 0FFF 
    FFFF FF00 0000 0013 FA5A A3             
    '''
    dsi_data = extract_data.ExtractData(input_string_dsi)
    assert dsi_data.buffer[0] == 0x11
    assert dsi_data.buffer[1] == 0x03
    assert dsi_data.buffer[2] == 0x10

    dsi_data = extract_data.ExtractData(None)
    dsi_data.set_buffer(input_string_dsi)
    assert dsi_data.buffer[0] == 0x11
    assert dsi_data.buffer[1] == 0x03
    assert dsi_data.buffer[2] == 0x10

@pytest.mark.skip(reason='no need to write file test any more')
def test_write_to_file():
    input_string_dsi = '''
    1103 1006 8000 0001 FF00 005B FFFF FFFF  
    FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFF 
    0000 0043 0000 0004 7372 6700 0000 0001 
    4953 4F06 0000 002B 0002 4953 4F50 0D87 
    8E5C 6300 0001 0004 D8B4 4708 4953 4F40 
    1201 0000 0016 0000 0A00 0180 0000 0FFF 
    FFFF FF00 0000 0013 FA5A A3             
    '''
    dsi_data = extract_data.ExtractData(input_string_dsi)
    dsi_data.write('test.dat')
    
    current_absolute_path = os.path.dirname( os.path.abspath( __file__ ))
    assert filecmp.cmp( current_absolute_path + '/' + 'test.dat', current_absolute_path + '/' + 'ref_dsm-cc_dsi.bin') == True 
    