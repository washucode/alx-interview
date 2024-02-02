#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """ Determine if a given data set represents a valid UTF-8 encoding
    Args:
        data: list of integers
    Returns:
        True if data is a valid UTF-8 encoding, else return False
    """

    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit is set or not
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6

    # iterate through the list of integers
    for num in data:
        # if its a continuation byte
        if n_bytes > 0:
            # check if the most significant and least significant bits are set
            if not (num & mask1 and not (num & mask2)):
                return False
            n_bytes -= 1
            continue
        else:
            # determine the number of bytes the UTF-8 Character consists of
            if num & mask1:
                n_bytes = 1
                # check the number of bytes
                while (num << n_bytes) & mask1:
                    n_bytes += 1

                # number of bytes cannot be 4 or more
                if n_bytes == 1 or n_bytes > 4:
                    return False
                n_bytes -= 1
    return n_bytes == 0
