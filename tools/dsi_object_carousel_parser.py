import dsi_parser

class Dsi(dsi_parser.Dsi):
    def __init__(self, bytes_data):
        dsi_parser.Dsi.__init__(self, bytes_data)