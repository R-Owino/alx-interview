#!/usr/bin/python3
'''
This module contains a method `validUTF8`
'''


def validUTF8(data):
    '''
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data (list): data to validate

    Return:
        True if data is a valid UTF-8 encoding, else return False
    '''

    # checks if the given byte is a valid UTF-8 continuation byte
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    # Tracks the number of remaining continuation bytes to expect
    remaining_bytes = 0

    for byte in data:
        if remaining_bytes > 0:
            if not is_continuation(byte):
                return False
            remaining_bytes -= 1
        else:
            if (byte & 0b10000000) == 0:
                remaining_bytes = 0
            elif (byte & 0b11100000) == 0b11000000:
                remaining_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                remaining_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                remaining_bytes = 3
            else:
                return False

    return remaining_bytes == 0
