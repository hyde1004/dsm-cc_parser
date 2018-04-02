import pytest
import dsi_parser

def test_dsi_init():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x010]
    input_bytes = bytes(input_numbers)
    dsi = dsi_parser.Dsi(input_bytes)

    assert dsi.get_bytes(1) == 0x0a
    assert dsi.position == 1

    assert dsi.get_bytes(2) == 0x0b0c
    assert dsi.position == 3

    assert dsi.get_bytes(4) == 0x0d0e0f10
    assert dsi.position == 7 

def test_read_dsi_data_from_file():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')

    assert dsi.buffer[0] == 0x11
    assert dsi.buffer[1] == 0x03
    assert len(dsi.buffer) == 0x6B # length
    assert dsi.length == 0x6B # length

def test_get_protocolDiscriminator():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')

    assert dsi.position == 0x00
    assert dsi.get_protocolDiscriminator() == 0x11

def test_get_dsmccType():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')

    dsi.get_protocolDiscriminator() 

    assert dsi.position == 0x01
    assert dsi.get_dsmccType() == 0x03 # Download message



def test_get_messageId():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')

    dsi.get_protocolDiscriminator() 
    dsi.get_dsmccType()
    
    assert dsi.position == 0x02
    assert dsi.get_messageId() == 0x1006 # DownloadServerInitiate

def test_get_transactionID():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')

    dsi.get_protocolDiscriminator() 
    dsi.get_dsmccType()
    dsi.get_messageId()

    assert dsi.position == 0x04
    assert dsi.get_transactionID() == 0x80000001 # transactionID

def test_get_reserved():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')

    dsi.get_protocolDiscriminator() 
    dsi.get_dsmccType()
    dsi.get_messageId()    
    dsi.get_transactionID()
    
    assert dsi.position == 0x08
    assert dsi.get_reserved() == 0xFF  

def test_get_adaptationLength():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')

    dsi.get_protocolDiscriminator() 
    dsi.get_dsmccType()
    dsi.get_messageId()    
    dsi.get_transactionID()
    dsi.get_reserved()

    assert dsi.position == 0x09
    assert dsi.get_adaptationLength() == 0x00  

def test_get_messageLength():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')

    dsi.get_protocolDiscriminator() 
    dsi.get_dsmccType()
    dsi.get_messageId()    
    dsi.get_transactionID()
    dsi.get_reserved()
    dsi.get_adaptationLength()

    assert dsi.position == 0x0A
    assert dsi.get_messageLength() == 0x005B   

def test_get_adaptation():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')

    dsi.get_protocolDiscriminator() 
    dsi.get_dsmccType()
    dsi.get_messageId()    
    dsi.get_transactionID()
    dsi.get_reserved()
    adaptation_length = dsi.get_adaptationLength()
    dsi.get_adaptation(adaptation_length)
#    assert dsi.position == 0x0A

def test_dsmcDownloadDataHeader():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')
    dsi.parse_dsmcDownloadDataHeader()
    assert dsi.protocolDiscriminator == 0x11
    assert dsi.dsmccType == 0x03
    assert dsi.messageId == 0x1006
    assert dsi.transactionID == 0x80000001
    assert dsi.reserved == 0xFF
    assert dsi.adaptationLength == 0x00

    assert dsi.position == 0x0c
    #assert dsi.display_dsmcDownloadDataHeader() == True

def test_get_serverId():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')
    dsi.parse_dsmcDownloadDataHeader()   

    old_position = dsi.position
    dsi.get_serverId() # 20 bytes
    assert dsi.position == old_position + 20
    assert dsi.position == 0x20

def test_get_compatibilityDescriptor():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')
    dsi.parse_dsmcDownloadDataHeader()   

    dsi.get_serverId()
    assert dsi.position == 0x20
    assert dsi.get_compatibilityDescriptor() == 0x0000
    
def test_get_privateDataLength():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')
    dsi.parse_dsmcDownloadDataHeader()   
    dsi.get_serverId()
    dsi.get_compatibilityDescriptor()

    assert dsi.position == 0x22
    assert dsi.get_privateDataLength() == 0x0043


def test_parse():
    dsi = dsi_parser.Dsi(None)
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

def test_get_crc():
    dsi = dsi_parser.Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')
    dsi.parse_dsmcDownloadDataHeader()   
    dsi.get_serverId()
    dsi.get_compatibilityDescriptor()
    dsi.get_privateDataLength()
    dsi.get_privateData()

    assert dsi.position == 0x67
    assert dsi.get_bytes(4) == 0x13FA5AA3

