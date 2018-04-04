import pytest
import dii_parser

def test_dii_parser_init():
    input_numbers = [0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x010]
    input_bytes = bytes(input_numbers)
    dii = dii_parser.Dii(input_bytes)

    assert dii.get_bytes(1) == 0x0a
    assert dii.position == 1

    assert dii.get_bytes(2) == 0x0b0c
    assert dii.position == 3

    assert dii.get_bytes(4) == 0x0d0e0f10
    assert dii.position == 7

def test_read_dsi_data_from_file():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    assert dii.buffer[0] == 0x11
    assert dii.buffer[1] == 0x03
    assert len(dii.buffer) == 0x7D
    assert dii.length == 0x7D

def test_get_protocolDiscriminator():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    assert dii.position == 0x00
    assert dii.get_protocolDiscriminator() == 0x11

def test_get_dsmccType():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    dii.get_protocolDiscriminator()
    
    assert dii.position == 0x01
    assert dii.get_dsmccType() == 0x03

def test_get_messageId():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    dii.get_protocolDiscriminator()
    dii.get_dsmccType()

    assert dii.get_messageId() == 0x1002

def test_get_transactionID():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    dii.get_protocolDiscriminator()
    dii.get_dsmccType()
    dii.get_messageId()

    assert dii.get_transactionID() == 0x8000000F

def test_get_reserved():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    dii.get_protocolDiscriminator()
    dii.get_dsmccType()
    dii.get_messageId()
    dii.get_transactionID() 

    assert dii.get_reserved() == 0xFF

def test_get_adaptationLength():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    dii.get_protocolDiscriminator()
    dii.get_dsmccType()
    dii.get_messageId()
    dii.get_transactionID() 
    dii.get_reserved()

    assert dii.get_adaptationLength() == 0x00

def test_get_messageLength():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    dii.get_protocolDiscriminator()
    dii.get_dsmccType()
    dii.get_messageId()
    dii.get_transactionID() 
    dii.get_reserved()
    dii.get_adaptationLength()

    assert dii.get_messageLength() == 0x006D

def test_get_adaptation():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    dii.get_protocolDiscriminator()
    dii.get_dsmccType()
    dii.get_messageId()
    dii.get_transactionID() 
    dii.get_reserved()
    bytes = dii.get_adaptationLength()
    dii.get_messageLength()

    dii.get_adaptation(bytes)
    assert dii.position == 0x0C

def test_dsmcDownloadDataHeader():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()

    assert dii.protocolDiscriminator == 0x11
    assert dii.dsmccType == 0x03
    assert dii.messageId == 0x1002
    assert dii.transactionID == 0x8000000F
    assert dii.reserved == 0xFF
    assert dii.adaptationLength == 0x00
    assert dii.messageLength == 0x006D

    assert dii.position == 0x0C

def test_get_downloadId():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()

    assert dii.get_downloadId() == 0x878E5C63

def test_get_blockSize():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()

    assert dii.get_blockSize() == 0x0FE2 

def test_get_windowSize():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()

    assert dii.get_windowSize() == 0x00

def test_get_ackPeriod():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()

    assert dii.get_ackPeriod() == 0x00

def test_get_tCDownloadWindow():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()

    assert dii.get_tCDownloadWindow() == 0x00000000

def test_get_tCDownloadScenario():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()

    assert dii.get_tCDownloadScenario() == 0x00000000

def test_get_compatiblityDescriptor():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()

    assert dii.get_compatibilityDescriptor() == 0x0000

def test_get_numberOfModules():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()
    dii.get_compatibilityDescriptor()

    assert dii.get_numberOfModules() == 0x03

def test_get_moduleId():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()
    dii.get_compatibilityDescriptor()
    dii.get_numberOfModules()

    assert dii.get_moduleId() == 0x0000  

def test_get_moduleSize():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()
    dii.get_compatibilityDescriptor()
    dii.get_numberOfModules()
    dii.get_moduleId()
    assert dii.get_moduleSize() == 0x0000034C

def test_get_moduleVersion():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()
    dii.get_compatibilityDescriptor()
    dii.get_numberOfModules()
    dii.get_moduleId()
    dii.get_moduleSize()
    assert dii.get_moduleVersion() == 0x0D

def test_get_moduleInfoLength():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()
    dii.get_compatibilityDescriptor()
    dii.get_numberOfModules()
    dii.get_moduleId()
    dii.get_moduleSize()
    dii.get_moduleVersion()

    assert dii.get_moduleInfoLength() == 0x15    

def test_get_moduleInfoByte():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()
    dii.get_compatibilityDescriptor()
    dii.get_numberOfModules()
    dii.get_moduleId()
    dii.get_moduleSize()
    dii.get_moduleVersion()
    dii.get_moduleInfoLength()

    dii.get_moduleInfoByte(dii.moduleInfoLength)
    assert dii.position == 0x3D    

def test_get_moduleInfo():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()
    dii.get_compatibilityDescriptor()
    dii.get_numberOfModules()

    dii.get_moduleInfo(dii.numberOfModules)

    # 1'st module
    assert dii.module[0].id == 0x0000
    assert dii.module[0].size == 0x0000034C
    assert dii.module[0].version == 0x0D
    assert dii.module[0].infoLength == 0x15

    # 2'nd module
    assert dii.module[1].id == 0x0009
    assert dii.module[1].size == 0x00000571
    assert dii.module[1].version == 0x0C
    assert dii.module[1].infoLength == 0x15   

    # 3rd module
    assert dii.module[2].id == 0x000B
    assert dii.module[2].size == 0x00002556
    assert dii.module[2].version == 0x0C
    assert dii.module[2].infoLength == 0x15    

def test_get_privateDataLength():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()
    dii.get_compatibilityDescriptor()
    dii.get_numberOfModules()
    dii.get_moduleInfo(dii.numberOfModules)

    assert dii.get_privateDataLength() == 0x0000

def test_get_privateDataByte():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()
    dii.get_compatibilityDescriptor()
    dii.get_numberOfModules()
    dii.get_moduleInfo(dii.numberOfModules)
    dii.get_privateDataLength()

    dii.get_privateDataByte(dii.privateDataLength) 
    assert dii.position == 0x79

def test_get_crc():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')
    dii.parse_dsmcDownloadDataHeader()
    dii.get_downloadId()
    dii.get_blockSize()
    dii.get_windowSize()
    dii.get_ackPeriod()
    dii.get_tCDownloadWindow()
    dii.get_tCDownloadScenario()
    dii.get_compatibilityDescriptor()
    dii.get_numberOfModules()
    dii.get_moduleInfo(dii.numberOfModules)
    dii.get_privateDataLength()
    dii.get_privateDataByte(dii.privateDataLength)     

    assert dii.get_crc() == 0xF42B7C0B

def test_body():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    dii.parse_dsmcDownloadDataHeader()
    dii.parse_body()
    
    assert dii.crc == 0xF42B7C0B

def test_parse():
    dii = dii_parser.Dii(None)
    dii.read_from_file('ref_dsm-cc_dii.bin')

    dii.parse()
    assert dii.crc == 0xF42B7C0B
