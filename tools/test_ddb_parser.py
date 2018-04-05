import pytest
import ddb_parser

def test_dii_parser_init():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10]
    input_bytes = bytes(input_numbers)
    ddb = ddb_parser.Ddb(input_bytes)

    assert ddb.get_bytes(1) == 0x0a
    assert ddb.position == 1

    assert ddb.get_bytes(2) == 0x0b0c
    assert ddb.position == 3

    assert ddb.get_bytes(4) == 0x0d0e0f10
    assert ddb.position == 7

def test_read_dsi_data_from_file():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')

    assert ddb.buffer[0] == 0x11
    assert ddb.buffer[1] == 0x03

    assert ddb.length == 0x0362
    assert len(ddb.buffer) == 0x0362

def test_get_protocolDiscriminator():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  

    assert ddb.get_protocolDiscriminator() == 0x11  

def test_get_dsmccType():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()

    assert ddb.get_dsmccType() == 0x03   

def test_get_messageId():  
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()

    assert ddb.get_messageId() == 0x1003  

def test_get_downloadId():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()
    ddb.get_messageId()

    assert ddb.get_downloadId() == 0x878E5C63  

def test_get_reserved():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()
    ddb.get_messageId()
    ddb.get_downloadId()

    assert ddb.get_reserved() == 0xFF

def test_get_adaptationLength():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()
    ddb.get_messageId()
    ddb.get_downloadId()
    ddb.get_reserved()

    assert ddb.get_adaptationLength() == 0x00

def test_get_messageLength():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()
    ddb.get_messageId()
    ddb.get_downloadId()
    ddb.get_reserved()    
    ddb.get_adaptationLength()

    assert ddb.get_messageLength() == 0x0352

def test_get_adaptation():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()
    ddb.get_messageId()
    ddb.get_downloadId()
    ddb.get_reserved()    
    adaptationLength = ddb.get_adaptationLength()
    ddb.get_messageLength()

    ddb.get_adaptation(adaptationLength)

    assert ddb.position == 0x000C

def test_get_moduleId():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()
    ddb.get_messageId()
    ddb.get_downloadId()
    ddb.get_reserved()    
    adaptationLength = ddb.get_adaptationLength()
    ddb.get_messageLength()
    ddb.get_adaptation(adaptationLength)    

    assert ddb.get_moduleId() == 0x0000

def test_get_moduleVersion():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()
    ddb.get_messageId()
    ddb.get_downloadId()
    ddb.get_reserved()    
    adaptationLength = ddb.get_adaptationLength()
    ddb.get_messageLength()
    ddb.get_adaptation(adaptationLength)    

    ddb.get_moduleId()
    assert ddb.get_moduleVersion() == 0x0D    

# reserved following moduleVersion
# def test_get_reserved():
#     pass

def test_get_blockNumber():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()
    ddb.get_messageId()
    ddb.get_downloadId()
    ddb.get_reserved()    
    adaptationLength = ddb.get_adaptationLength()
    ddb.get_messageLength()
    ddb.get_adaptation(adaptationLength)    

    ddb.get_moduleId()
    ddb.get_moduleVersion()
    ddb.get_reserved()
    assert ddb.get_blockNumber() == 0x0000

def test_get_blockDataByte():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()
    ddb.get_messageId()
    ddb.get_downloadId()
    ddb.get_reserved()    
    adaptationLength = ddb.get_adaptationLength()
    messageLength = ddb.get_messageLength()
    ddb.get_adaptation(adaptationLength)    

    start_of_body = ddb.position
    ddb.get_moduleId()
    ddb.get_moduleVersion()
    ddb.get_reserved()
    ddb.get_blockNumber()
    consumed_bytes = ddb.position - start_of_body
    
    ddb.get_blockDataByte(messageLength - consumed_bytes)
    assert ddb.position == 0x035E

def test_get_crc():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')  
    ddb.get_protocolDiscriminator()
    ddb.get_dsmccType()
    ddb.get_messageId()
    ddb.get_downloadId()
    ddb.get_reserved()    
    adaptationLength = ddb.get_adaptationLength()
    messageLength = ddb.get_messageLength()
    ddb.get_adaptation(adaptationLength)    

    start_of_body = ddb.position
    ddb.get_moduleId()
    ddb.get_moduleVersion()
    ddb.get_reserved()
    ddb.get_blockNumber()
    consumed_bytes = ddb.position - start_of_body
    ddb.get_blockDataByte(messageLength - consumed_bytes)

    assert ddb.get_crc() == 0xEDCB2BD5        

def test_parse_dsmccDownloadDataHeader():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')

    ddb.parse_dsmccDownloadDataHeader()
    assert ddb.position == 0x000C 

def test_parse_body():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin')

    ddb.parse_dsmccDownloadDataHeader()
    ddb.parse_body()

    assert ddb.moduleVersion == 0x0D

def test_parse():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_0.bin') 

    ddb.parse()

    assert ddb.moduleVersion == 0x0D   
    assert ddb.crc == 0xEDCB2BD5

def test_parse_ddb_module_B_section0_file():
    ddb = ddb_parser.Ddb(None)
    ddb.read_from_file('ref_dsm-cc_ddb-module_B-section0.bin') 
    ddb.parse()
    assert ddb.moduleId == 0x0B
    

