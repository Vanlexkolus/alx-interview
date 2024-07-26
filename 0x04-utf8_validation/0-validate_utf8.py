#!/usr/bin/python3
"""
Thsi is there because of the ALX Checker
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers where each integer
        represents a byte (8 least significant bits).

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """


    num_bytes = 0

    for num in data:
        byte = num & 0xFF  # Only consider the last 8 bits
        
        if num_bytes == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
