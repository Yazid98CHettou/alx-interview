#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    data: list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    byte_count = 0

    for a in data:
        if byte_count == 0:
            if a >> 5 == 0b110 or a >> 5 == 0b1110:
                byte_count = 1
            elif a >> 4 == 0b1110:
                byte_count = 2
            elif a >> 3 == 0b11110:
                byte_count = 3
            elif a >> 7 == 0b1:
                return False
        else:
            if a >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
