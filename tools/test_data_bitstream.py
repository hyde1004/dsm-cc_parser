import pytest
import data_bitstream

def test_init():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10]
    input_bytes = bytes(input_numbers)

    data_partition = data_bitstream.DataBitstream()
    data_partition.setData(input_bytes)

    assert data_partition.buffer[0] == 0x0a
    assert data_partition.buffer[1] == 0x0b

def test_length():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10]
    input_bytes = bytes(input_numbers)

    data_partition = data_bitstream.DataBitstream()
    data_partition.setData(input_bytes)

    assert data_partition.length() == len(input_numbers)

def test_read_bytes():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10]
    input_bytes = bytes(input_numbers)

    data_partition = data_bitstream.DataBitstream()
    data_partition.setData(input_bytes)

    assert data_partition.position == 0   

    assert data_partition.get_bytes(1) == 0x0a
    assert data_partition.position == 1

    assert data_partition.get_bytes(2) == 0x0b0c
    assert data_partition.position == 3