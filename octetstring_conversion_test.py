# -*- coding: UTF-8 -*-

"""
HexByteConversion

Convert a byte string to it's hex representation for output or visa versa.

ByteToHex converts byte string "\xFF\xFE\x00\x01" to the string "FF FE 00 01"
HexToByte converts string "FF FE 00 01" to the byte string "\xFF\xFE\x00\x01"
"""


def ByteToHex(byteStr):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """

    # Uses list comprehension which is a fractionally faster implementation than
    # the alternative, more readable, implementation below
    #
    #    hex = []
    #    for aChar in byteStr:
    #        hex.append( "%02X " % ord( aChar ) )
    #
    #    return ''.join( hex ).strip()

    return ''.join(["%02X " % ord(x) for x in byteStr]).strip()


def HexToByte(hexStr):
    """
    Convert a string hex byte values into a byte string. The Hex Byte values may
    or may not be space separated.
    """
    # The list comprehension implementation is fractionally slower in this case
    #
    #    hexStr = ''.join( hexStr.split(" ") )
    #    return ''.join( ["%c" % chr( int ( hexStr[i:i+2],16 ) ) \
    #                                   for i in range(0, len( hexStr ), 2) ] )

    bt = []
    hexStr = ''.join(hexStr.split(" "))

    for i in range(0, len(hexStr), 2):
        bt.append(chr(int(hexStr[i:i + 2], 16)))

    return ''.join(bt)
    

if __name__ == "__main__":
    # Functionality speed was tested for Python 2.7
    # Additional tests required for Python 3.6

    # Test data - different formats but equivalent data
    __hexStr1 = "FFFFFF5F8121070C0000FFFFFFFF5F8129010B"
    __hexStr2 = "FF FF FF 5F 81 21 07 0C 00 00 FF FF FF FF 5F 81 29 01 0B"
    __byteStr = "\xFF\xFF\xFF\x5F\x81\x21\x07\x0C\x00\x00\xFF\xFF\xFF\xFF\x5F\x81\x29\x01\x0B"

    print("\nHex To Byte and Byte To Hex Conversion")

    print("Test 1 - ByteToHex - Passed: ", ByteToHex(__byteStr))
    print("Test 2 - HexToByte - Passed: ", HexToByte(__hexStr1))
    print("Test 3 - HexToByte - Passed: ", HexToByte(__hexStr2))

    # turn a non-space separated hex string into a space separated hex string!
    print("Test 4 - Combined  - Passed: ",  ByteToHex(HexToByte(__hexStr1)))
