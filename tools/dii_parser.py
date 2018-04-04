import section
class Dii(section.Section):
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
        self.skip_bytes(bytes)

    def parse_dsmcDownloadDataHeader(self):
        self.get_protocolDiscriminator()
        self.get_dsmccType()
        self.get_messageId()
        self.get_transactionID()
        self.get_reserved()
        self.get_adaptationLength()
        self.get_messageLength()
        self.get_adaptation(self.adaptationLength)

    def get_downloadId(self):
        self.downloadId = self.get_bytes(4)
        return self.downloadId

    def get_blockSize(self):
        self.blockSize = self.get_bytes(2)
        return self.blockSize

    def get_windowSize(self):
        self.windowSize = self.get_bytes(1)
        return self.windowSize

    def get_ackPeriod(self):
        self.ackPeriod = self.get_bytes(1)
        return self.ackPeriod

    def get_tCDownloadWindow(self):
        self.tCDownloadWindow = self.get_bytes(4)
        return self.tCDownloadWindow

    def get_tCDownloadScenario(self):
        self.tCDownloadScenario = self.get_bytes(4)
        return self.tCDownloadScenario

    def get_compatibilityDescriptor(self):
        self.compatibilityDescriptor = self.get_bytes(2)
        return self.compatibilityDescriptor

    def get_numberOfModule(self):
        self.numberOfModule = self.get_bytes(2)
        return self.numberOfModule

    def get_moduleId(self):
        self.moduleId = self.get_bytes(2)
        return self.moduleId

    def get_moduleSize(self):
        self.moduleSize = self.get_bytes(4)
        return self.moduleSize

    def get_moduleVersion(self):
        self.moduleVersion = self.get_bytes(1)
        return self.moduleVersion

    def get_moduleInfoLength(self):
        self.moduleInfoLength = self.get_bytes(1)
        return self.moduleInfoLength

    def get_moduleInfoByte(self, bytes):
        self.skip_bytes(bytes)

    def get_privateDataLength(self):
        self.privateDataLength = self.get_bytes(2)
        return self.privateDataLength

    def get_privateDataByte(self, bytes):
        self.get_block_bytes(bytes)

    class Module:
        def __init__(self):
            self.id = 0
            self.size = 0
            self.version = 0
            self.infoLength = 0
            self.infoByte = None

    def get_moduleInfo(self, numberOfModule):
        self.module = []
        
        for i in range(self.numberOfModule):
            parsed_module = self.Module()
            parsed_module.id = self.get_moduleId()
            parsed_module.size = self.get_moduleSize()
            parsed_module.version = self.get_moduleVersion()
            parsed_module.infoLength = self.get_moduleInfoLength()
            parsed_module.infoByte = self.get_block_bytes(parsed_module.infoLength)

            self.module.append(parsed_module)

            i = i # dummy for pylint warning

    def get_crc(self):
        self.crc = self.get_bytes(4)
        return self.crc

    def parse_body(self):
        self.get_downloadId()
        self.get_blockSize()
        self.get_windowSize()
        self.get_ackPeriod()
        self.get_tCDownloadWindow()
        self.get_tCDownloadScenario()
        self.get_compatibilityDescriptor()
        self.get_numberOfModule()
        self.get_moduleInfo(self.numberOfModule)
        self.get_privateDataLength()
        self.get_privateDataByte(self.privateDataLength)
        self.get_crc()

    def parse(self):
        self.parse_dsmcDownloadDataHeader()
        self.parse_body()

    