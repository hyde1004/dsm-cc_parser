import os
import struct

class ExtractData:
    def __init__(self, input_string):
        hex_values = []

        if input_string != None:
            strip_string = ''.join(input_string.split()) # https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string-in-python
            for i in range(0, len(strip_string) - 1, 2):
                hex_value = int(strip_string[i:i+2], 16)
                hex_values.append(hex_value)    

        self.buffer = hex_values

    def set_buffer(self, input_string):
        hex_values = []

        if input_string != None:
            strip_string = ''.join(input_string.split()) # https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string-in-python
            for i in range(0, len(strip_string) - 1, 2):
                hex_value = int(strip_string[i:i+2], 16)
                hex_values.append(hex_value)    

        self.buffer = hex_values

    def write(self, output_file_name):
        with open(os.path.dirname( os.path.abspath( __file__ )) + '/' + output_file_name, 'wb') as bin_file:
            for byte in self.buffer:
                bin_file.write(struct.pack('B', byte)) # https://stackoverflow.com/questions/18367007/python-how-to-write-to-a-binary-file        
    
if __name__ == "__main__":
    dii_raw_string = '''
    1103 1003 878E 5C63 FF00 0FE8 000B 0CFF
    0000 4249 4F50 0100 0000 0000 0969 0478
    94F1 F300 0000 0466 696C 0000 0800 0000
    0000 0009 4900 0000 094D 0000 0949 2354
    6F74 616C 206E 756D 6265 7220 6F66 2061
    7070 6C69 6361 7469 6F6E 7320 746F 2062
    6520 686F 7374 6564 206F 6E20 7468 6520
    706F 7274 616C 0D0A 544F 5441 4C5F 4150
    504C 4943 4154 494F 4E53 203D 2035 0D0A
    0D0A 234D 6178 696D 756D 206E 756D 6265
    7220 6F66 2061 7070 6C69 6361 7469 6F6E
    7320 746F 2062 6520 6469 7370 6C61 7965
    6420 6F6E 2070 6167 650D 0A41 5050 4C49
    4341 5449 4F4E 535F 5045 525F 5041 4745
    203D 2034 0D0A 0D0A 2341 7070 6C69 6361
    7469 6F6E 2043 7963 6C69 630D 0A63 7963
    6C69 6320 3D20 300D 0A0D 0A23 6943 6F6F
    6B69 6E67 0D0A 6E61 6D65 203D 2069 436F
    6F6B 696E 670D 0A75 726C 203D 2064 7662
    3A2F 2F41 432E 3043 2E33 3331 330D 0A66
    6472 5F6E 616D 6520 3D20 6943 6F6F 6B69
    6E67 2E66 6472 0D0A 7472 6961 6C5F 7065
    7269 6F64 203D 200D 0A6E 6F74 5F72 6561
    6368 5F74 696D 656F 7574 203D 2031 320D
    0A6E 6F74 2061 7574 686F 7269 7365 6420
    3D20 546F 2073 7562 7363 7269 6265 2074
    6869 7320 7365 7276 6963 6520 6174 2052
    7334 352F 6D6F 6E74 6820 6769 7665 2061
    206D 6973 7365 6420 6361 6C6C 2061 7420
    3931 3039 3531 3531 3531 2066 726F 6D20
    796F 7572 2072 6567 6973 7465 7265 6420
    6D6F 6269 6C65 206E 756D 6265 722E 2045
    7272 6F72 2043 6F64 653A 2034 0D0A 6E6F
    745F 7265 6163 6861 626C 655F 6572 726F
    725F 7465 7874 203D 2053 6572 7669 6365
    2069 7320 6375 7272 656E 746C 7920 6E6F
    7420 7375 6273 6372 6962 6564 2062 7920
    796F 752E 506C 6561 7365 2063 6F6E 7461
    6374 2063 7573 746F 6D65 7220 6361 7265
    2061 7420 3138 3030 2031 3032 2038 3038
    3020 2874 6F6C 6C20 6672 6565 2920 6F72
    2030 3230 2034 3031 3831 3430 3020 746F
    2061 6464 2074 6869 7320 746F 2079 6F75
    7220 7061 636B 6167 652E 0D0A 0D0A 2369
    4B69 6473 776F 726C 640D 0A6E 616D 6520
    3D20 694B 6964 7377 6F72 6C64 0D0A 7572
    6C20 3D20 6476 623A 2F2F 4143 2E30 422E
    3244 4235 0D0A 6664 725F 6E61 6D65 203D
    2046 756E 446F 6F44 6161 5F50 6F72 7461
    6C2E 6664 720D 0A74 7269 616C 5F70 6572
    696F 6420 3D20 0D0A 6E6F 745F 7265 6163
    685F 7469 6D65 6F75 7420 3D20 3132 0D0A
    6E6F 7420 6175 7468 6F72 6973 6564 203D
    2054 6F20 656E 6162 6C65 2074 6869 7320
    6954 5620 7365 7276 6963 652C 2070 6C65
    6173 6520 6361 6C6C 2031 3231 3530 2028
    746F 6C6C 2066 7265 6520 6672 6F6D 2079
    6F75 7220 6169 7274 656C 206D 6F62 696C
    6529 206F 7220 3138 3030 2031 3032 2038
    3038 3020 2874 6F6C 6C20 6672 6565 292E
    2045 7272 6F72 2043 6F64 653A 2034 0D0A
    6E6F 745F 7265 6163 6861 626C 655F 6572
    726F 725F 7465 7874 203D 2053 6572 7669
    6365 2069 7320 6375 7272 656E 746C 7920
    6E6F 7420 7375 6273 6372 6962 6564 2062
    7920 796F 752E 506C 6561 7365 2063 6F6E
    7461 6374 2063 7573 746F 6D65 7220 6361
    7265 2061 7420 3138 3030 2031 3032 2038
    3038 3020 2874 6F6C 6C20 6672 6565 2920
    6F72 2030 3230 2034 3031 3831 3430 3020
    746F 2061 6464 2074 6869 7320 746F 2079
    6F75 7220 7061 636B 6167 652E 0D0A 0D0A
    2368 656C 700D 0A6E 616D 6520 3D20 6865
    6C70 0D0A 7572 6C20 3D20 6476 623A 2F2F
    4143 2E30 372E 3145 4631 0D0A 6664 725F
    6E61 6D65 203D 2049 4865 6C70 436F 6E74
    726F 6C6C 6572 2E66 6472 0D0A 7472 6961
    6C5F 7065 7269 6F64 203D 200D 0A6E 6F74
    5F72 6561 6368 5F74 696D 656F 7574 203D
    2031 320D 0A6E 6F74 2061 7574 686F 7269
    7365 6420 3D20 546F 2065 6E61 626C 6520
    7468 6973 2069 5456 2073 6572 7669 6365
    2C20 706C 6561 7365 2063 616C 6C20 3132
    3135 3020 2874 6F6C 6C20 6672 6565 2066
    726F 6D20 796F 7572 2061 6972 7465 6C20
    6D6F 6269 6C65 2920 6F72 2031 3830 3020
    3130 3220 3830 3830 2028 746F 6C6C 2066
    7265 6529 2E20 4572 726F 7220 436F 6465
    3A20 340D 0A6E 6F74 5F72 6561 6368 6162
    6C65 5F65 7272 6F72 5F74 6578 7420 3D20
    5365 7276 6963 6520 6973 2063 7572 7265
    6E74 6C79 206E 6F74 2073 7562 7363 7269
    6265 6420 6279 2079 6F75 2E50 6C65 6173
    6520 636F 6E74 6163 7420 6375 7374 6F6D
    6572 2063 6172 6520 6174 2031 3830 3020
    3130 3220 3830 3830 2028 746F 6C6C 2066
    7265 6529 206F 7220 3032 3020 3430 3138
    3134 3030 2074 6F20 6164 6420 7468 6973
    2074 6F20 796F 7572 2070 6163 6B61 6765
    2E0D 0A0D 0A23 694D 7573 6963 5370 6163
    650D 0A6E 616D 6520 3D20 694D 7573 6963
    5370 6163 650D 0A75 726C 203D 2064 7662
    3A2F 2F41 432E 3034 2E32 4639 350D 0A66
    6472 5F6E 616D 6520 3D20 4169 7274 656C
    5F69 4D75 7369 632E 6664 720D 0A74 7269
    616C 5F70 6572 696F 6420 3D20 0D0A 6E6F
    745F 7265 6163 685F 7469 6D65 6F75 7420
    3D20 3130 0D0A 6E6F 7420 6175 7468 6F72
    6973 6564 203D 2054 6F20 7375 6273 6372
    6962 6520 746F 2069 4D75 7369 6353 7061
    6365 2066 6F72 2052 7335 3120 7065 7220
    6D6F 6E74 682C 2047 6976 6520 6D69 7373
    6564 2063 616C 6C20 6F6E 2038 3830 3034
    3838 3030 332E 2045 7272 6F72 2043 6F64
    653A 2034 0D0A 6E6F 745F 7265 6163 6861
    626C 655F 6572 726F 725F 7465 7874 203D
    2053 6572 7669 6365 2069 7320 6375 7272
    656E 746C 7920 6E6F 7420 7375 6273 6372
    6962 6564 2062 7920 796F 752E 506C 6561
    7365 2063 6F6E 7461 6374 2063 7573 746F
    6D65 7220 6361 7265 2061 7420 3138 3030
    2031 3032 2038 3038 3020 2874 6F6C 6C20
    6672 6565 2920 6F72 2030 3230 2034 3031
    3831 3430 3020 746F 2061 6464 2074 6869
    7320 746F 2079 6F75 7220 7061 636B 6167
    652E 0D0A 0D0A 2369 5456 2048 6F6D 650D
    0A6E 616D 6520 3D20 6954 5620 486F 6D65
    0D0A 7572 6C20 3D20 6476 623A 2F2F 4143
    2E30 372E 3145 4530 0D0A 6664 725F 6E61
    6D65 203D 2069 5456 506F 7274 616C 2E66
    6472 0D0A 7472 6961 6C5F 7065 7269 6F64
    203D 200D 0A6E 6F74 5F72 6561 6368 5F74
    696D 656F 7574 3D31 300D 0A6E 6F74 2061
    7574 686F 7269 7365 6420 3D20 546F 2065
    6E61 626C 6520 7468 6973 2069 5456 2073
    6572 7669 6365 2C20 706C 6561 7365 2063
    616C 6C20 3132 3135 3020 2874 6F6C 6C20
    6672 6565 2066 726F 6D20 796F 7572 2061
    6972 7465 6C20 6D6F 6269 6C65 2920 6F72
    2031 3830 3020 3130 3220 3830 3830 2028
    746F 6C6C 2066 7265 6529 2E20 4572 726F
    7220 436F 6465 3A20 340D 0A6E 6F74 5F72
    6561 6368 6162 6C65 5F65 7272 6F72 5F74
    6578 7420 3D20 5365 7276 6963 6520 6973
    2063 7572 7265 6E74 6C79 206E 6F74 2073
    7562 7363 7269 6265 6420 6279 2079 6F75
    2E50 6C65 6173 6520 636F 6E74 6163 7420
    6375 7374 6F6D 6572 2063 6172 6520 6174
    2031 3830 3020 3130 3220 3830 3830 2028
    746F 6C6C 2066 7265 6529 206F 7220 3032
    3020 3430 3138 3134 3030 2074 6F20 6164
    6420 7468 6973 2074 6F20 796F 7572 2070
    6163 6B61 6765 2E42 494F 5001 0000 0000
    0000 B704 80AF F1F3 0000 0004 6669 6C00
    0008 0000 0000 0000 0097 0000 0000 9B00
    0000 9723 4C69 6E6B 204D 6573 7361 6765
    0D0A 6D65 7373 6167 6520 3D20 5072 6573
    7320 6F6B 2074 6F20 6C61 756E 6368 0D0A
    0D0A 2341 7070 5374 6F72 650D 0A6E 616D
    6520 3D20 4170 7053 746F 7265 0D0A 7572
    6C20 3D20 6874 7470 3A2F 2F31 3232 2E31
    3630 2E31 3736 2E33 352F 6169 7274 656C
    2E73 656C 662E 6361 7265 2F76 6965 772F
    696E 6465 782E 7068 700D 0A0D 0A20 0D0A
    0D0A 0D0A 0D0A 0D0A 0D0A 4249 4F50 0100
    0000 0000 009F 04F0 81F1 F300 0000 0466
    696C 0000 0800 0000 0000 0000 7F00 0000
    0083 0000 007F 234C 696E 6B20 4D65 7373
    6167 650D 0A6D 6573 7361 6765 203D 2050
    7265 7373 206F 6B20 746F 206C 6175 6E63
    680D 0A0D 0A23 466C 6F32 476F 0D0A 6E61
    6D65 203D 2046 6C6F 3247 6F0D 0A75 726C
    203D 2068 7474 703A 2F2F 3130 332E 3235
    352E 3231 362E 3335 2F64 7468 2F69 6E64
    6578 2E70 6870 0D0A 200D 0A0D 0A0D 0A0D
    0A0D 0A0D 0A42 494F 5001 0000 0000 000E
    D504 3003 F1F3 0000 0004 6669 6C00 0008
    0000 0000 0000 0EB5 0000 000E B900 000E
    B523 546F 7461 6C20 6E75 6D62 6572 206F
    6620 6170 706C 6963 6174 696F 6E73 2074
    6F20 6265 2068 6F73 7465 6420 6F6E 2074
    6865 2070 6F72 7461 6C0D 0A54 4F54 414C
    5F41 5050 4C49 4341 5449 4F4E 5320 3D20
    370D 0A0D 0A23 4D61 7869 6D75 6D20 6E75
    6D62 6572 206F 6620 6170 706C 6963 6174
    696F 6E73 2074 6F20 6265 2064 6973 706C
    6179 6564 206F 6E20 7061 6765 0D0A 4150
    504C 4943 4154 494F 4E53 5F50 4552 5F50
    4147 4520 3D20 340D 0A0D 0A23 4170 706C
    6963 6174 696F 6E20 4379 636C 6963 0D0A
    6379 636C 6963 203D 2030 0D0A 0D0A 2353
    6E61 6B65 7320 616E 6420 5669 6E65 730D
    0A6E 616D 6520 3D20 536E 616B 6573 2061
    6E64 2056 696E 6573 0D0A 7572 6C20 3D20
    6476 623A 2F2F 4143 2E30 372E 3146 3336
    0D0A 6664 725F 6E61 6D65 203D 2053 6E61
    6B65 416E 644C 6164 6465 722E 6664 720D
    0A74 7269 616C 5F70 6572 696F 6420 3D20
    0D0A 6E6F 745F 7265 6163 685F 7469 6D65
    6F75 743D 3130 0D0A 6E6F 7420 6175 7468
    6F72 6973 6564 203D 2054 6F20 706C 6179
    2053 6E61 6B65 7320 616E 6420 5669 6E65
    7320 616E 6420 3520 6F74 6865 7220 6578
    6369 7469 6E67 2067 616D 6573 2040 206A
    7573 7420 5273 2E20 3531 2070 6D20 7375
    6273 6372 6962 6520 746F 2047 616D 6573
    2050 6C61 7469 6E75 6D20 5061 636B 2E20
    2053 656E 6420 534D 5320 4144 4420 5047
    2074 6F20 3534 3332 352E 2050 7265 7373
    2062 6163 6B20 746F 2063 6C6F 7365 0D0A
    6E6F 745F 7265 6163 6861 626C 655F 6572
    726F 725F 7465 7874 203D 2053 6572 7669
    6365 2069 7320 6375 7272 656E 746C 7920
    6E6F 7420 7375 6273 6372 6962 6564 2062
    7920 796F 752E 506C 6561 7365 2063 6F6E
    7461 6374 2063 7573 746F 6D65 7220 6361
    7265 2061 7420 3138 3030 2031 3032 2038
    3038 3020 2874 6F6C 6C20 6672 6565 2920
    6F72 2030 3230 2034 3031 3831 3430 3020
    746F 2061 6464 2074 6869 7320 746F 2079
    6F75 7220 7061 636B 6167 652E 0D0A 0D0A
    2344 6578 7465 7227 7320 4C61 620D 0A6E
    616D 6520 3D20 4465 7874 6572 2773 204C
    6162 0D0A 7572 6C20 3D20 6476 623A 2F2F
    4143 2E30 372E 3146 3335 0D0A 6664 725F
    6E61 6D65 203D 2041 544C 4465 7874 6572
    734C 6162 6F72 6174 6F72 7933 2E66 6472
    0D0A 7472 6961 6C5F 7065 7269 6F64 203D
    200D 0A6E 6F74 5F72 6561 6368 5F74 696D
    656F 7574 3D31 300D 0A6E 6F74 2061 7574
    686F 7269 7365 6420 3D20 546F 2070 6C61
    7920 4465 7874 6572 2773 204C 6162 2061
    6E64 2035 206F 7468 6572 2065 7863 6974
    696E 6720 6761 6D65 7320 4020 6A75 7374
    2052 732E 2035 3120 706D 2073 7562 7363
    7269 6265 2074 6F20 4761 6D65 7320 506C
    6174 696E 756D 2050 6163 6B2E 2020 5365
    6E64 2053 4D53 2041 4444 2050 4720 746F
    2035 3433 3235 2E20 5072 6573 7320 6261
    636B 2074 6F20 636C 6F73 650D 0A6E 6F74
    5F72 6561 6368 6162 6C65 5F65 7272 6F72
    5F74 6578 7420 3D20 5365 7276 6963 6520
    6973 2063 7572 7265 6E74 6C79 206E 6F74
    2073 7562 7363 7269 6265 6420 6279 2079
    6F75 2E50 6C65 6173 6520 636F 6E74 6163
    7420 6375 7374 6F6D 6572 2063 6172 6520
    6174 2031 3830 3020 3130 3220 3830 3830
    2028 746F 6C6C 2066 7265 6529 206F 7220
    3032 3020 3430 3138 3134 3030 2074 6F20
    6164 6420 7468 6973 2074 6F20 796F 7572
    2070 6163 6B61 6765 2E0D 0A0D 0A23 4D69
    636B 7920 4D61 7463 680D 0A6E 616D 6520
    3D20 4D69 636B 7920 4D61 7463 680D 0A75
    726C 203D 2064 7662 3A2F 2F41 432E 3037
    2E31 4633 370D 0A66 6472 5F6E 616D 6520
    3D20 4D4D 7CB0 B7DD                                              
    '''
    dii = ExtractData(None)
    
    dii.set_buffer(dii_raw_string)
    dii.write('ref_dsm-cc_ddb-module_B-section0.bin')
