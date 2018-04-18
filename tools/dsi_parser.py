import section

class Dsi(section.Section):
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

    def get_transactionID(self):
        self.transactionID = self.get_bytes(4)
        return self.transactionID
    
    def get_reserved(self):
        self.reserved = self.get_bytes(1)
        return self.reserved

    def get_adaptationLength(self):
        self.adaptationLength = self.get_bytes(1)
        return self.adaptationLength

    def get_messageLength(self):
        self.messageLength = self.get_bytes(2)
        return self.messageLength

    def get_adaptation(self, bytes):
        self.adaptation = self.get_block_bytes(bytes)

    def parse(self):
        self.parse_dsmccMessageHeader()
        self.parse_body()

    def parse_body(self):
        self.get_serverId()
        self.get_compatibilityDescriptor()
        self.get_privateDataLength()
        self.get_privateData()

    def parse_dsmccMessageHeader(self):
        self.get_protocolDiscriminator()
        self.get_dsmccType()
        self.get_messageId()
        self.get_transactionID()
        self.get_reserved()
        self.get_adaptationLength()
        self.get_messageLength()

    def display_dsmccMessageHeader(self):
        print('---------------------------')
        print('protocolDiscriminator : 0x%02X' % self.protocolDiscriminator)
        print('dsmccType : 0x%02X' % self.dsmccType)
        print('messageId : 0x%02X' % self.messageId)
        print('transactionID : 0x%02X' % self.transactionID)
        print('reserved : 0x%02X' % self.reserved)
        print('adaptationLength : 0x%02X' % self.adaptationLength)
        
    def get_serverId(self):
        self.serverId = self.get_block_bytes(20)

    def get_compatibilityDescriptor(self):
        self.compatibilityDescriptor = self.get_bytes(2)
        return self.compatibilityDescriptor

    def get_privateDataLength(self):
        self.privateDataLength = self.get_bytes(2)
        return self.privateDataLength

    def get_privateData(self):
        self.privateData = self.get_block_bytes(self.privateDataLength)

    def display_dsi_info(self):
        print('serverID : ')
        print('')

    def display(self):
        self.display_dsmccMessageHeader()
        self.display_dsi_info()

if __name__ == '__main__':
    dsi = Dsi(None)
    dsi.read_from_file('ref_dsm-cc_dsi.bin')
    dsi.parse()
    dsi.display()