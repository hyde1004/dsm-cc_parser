import pytest
import dsi_object_carousel_parser

def test_init():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10]
    input_bytes = bytes(input_numbers)
    dsi = dsi_object_carousel_parser.Dsi(input_bytes)

    assert dsi.get_bytes(1) == 0x0a
    assert dsi.position == 1

    assert dsi.get_bytes(2) == 0x0b0c
    assert dsi.position == 3

    assert dsi.get_bytes(4) == 0x0d0e0f10
    assert dsi.position == 7 

def test_parse():
    dsi = dsi_object_carousel_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')
    dsi.parse()
    assert dsi.position == 0x67

    assert dsi.protocolDiscriminator == 0x11
    assert dsi.dsmccType == 0x03
    assert dsi.messageId == 0x1006
    assert dsi.transactionID == 0x80000001
    assert dsi.reserved == 0xFF
    assert dsi.adaptationLength == 0x00

    assert dsi.compatibilityDescriptor == 0x0000
    assert dsi.privateDataLength == 0x0043