import section
class Ddb(section.Section):
    def __init__(self, bytes_data):
        section.Section.__init__(self, bytes_data)

    def get_protocolDiscriminator(self):
        self.protocolDiscriminator = self.get_bytes(1)
        return self.protocolDiscriminator

    def get_dsmccType(self):
        self.dsmccType = self.get_bytes(1)
        return self.dsmccType

    def get_messageId(self):
        self.messageId = self.get_bytes(2)
        return self.messageId

    def get_downloadId(self):
        self.downloadId = self.get_bytes(4)
        return self.downloadId

    def get_reserved(self):
        self.reserved = self.get_bytes(1)
        return self.reserved

    def get_adaptationLength(self):
        self.adaptationLength = self.get_bytes(1)
        return self.adaptationLength

    def get_messageLength(self):
        self.messageLength = self.get_bytes(2)
        return self.messageLength

    def get_adaptation(self, bytes_to_be_read):
        self.adaptation = self.get_block_bytes(bytes_to_be_read)
        return self.adaptation

    def get_moduleId(self):
        self.moduleId = self.get_bytes(2)
        return self.moduleId

    def get_moduleVersion(self):
        self.moduleVersion = self.get_bytes(1)
        return self.moduleVersion

    def get_blockNumber(self):
        self.blockNumber = self.get_bytes(2)
        return self.blockNumber

    def get_blockDataByte(self, bytes_to_be_read):
        self.blockDataByte = self.get_block_bytes(bytes_to_be_read)
        return self.blockDataByte

    def get_crc(self):
        self.crc = self.get_bytes(4)
        return self.crc
    
    def parse_dsmccDownloadDataHeader(self):
        self.get_protocolDiscriminator()
        self.get_dsmccType()
        self.get_messageId()
        self.get_downloadId()
        self.get_reserved()
        self.get_adaptationLength()
        self.get_messageLength()
        self.get_block_bytes(self.adaptationLength)

    def parse_body(self):
        self.get_moduleId()
        self.get_moduleVersion()
        self.get_reserved()
        self.get_blockNumber()
        skip_num_of_bytes = 6 # 2 (moduleId) + 1 (moduleVersion) + 1 (reserved) + 2 (blockNumber)
        self.get_blockDataByte(self.messageLength - skip_num_of_bytes)

    def parse(self):
        self.parse_dsmccDownloadDataHeader()
        self.parse_body()
        self.get_crc()

    def display(self):
        print('-------------------------------')
        print('protocolDisciminator : 0x%02X' % ddb.protocolDiscriminator)
        print('dsmccType : 0x%02X' % ddb.dsmccType)
        print('messageId : 0x%04X' % ddb.messageId)
        print('downloadId : 0x%08X' % ddb.downloadId)
        print('reserved : 0x%02X' % ddb.reserved)
        print('adaptationLength : %02X' % ddb.adaptationLength)
        print('moduleId : 0x%04X' % ddb.moduleId)
        print('moduleVersion : 0x%02X' % ddb.moduleVersion)
        print('blockNumber : 0x%04X' % ddb.blockNumber)
        print('')

if __name__ == '__main__':
    input_files = ['ref_dsm-cc_ddb-module_0.bin', 'ref_dsm-cc_ddb-module_9.bin',
        'ref_dsm-cc_ddb-module_B-section0.bin', 'ref_dsm-cc_ddb-module_B-section1.bin', 'ref_dsm-cc_ddb-module_B-section2.bin']
    
    for input_file in input_files:
        ddb = Ddb(None)
        ddb.read_from_file(input_file)
        ddb.parse()

        print('file name : %s' % input_file)
        ddb.display()





    