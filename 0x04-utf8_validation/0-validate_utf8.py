#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    number_bytes = 0

    task_1 = 1 << 7
    task_2 = 1 << 6

    for i in data:

        task_byte = 1 << 7

        if number_bytes == 0:

            while task_byte & i:
                number_bytes += 1
                task_byte = task_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & task_1 and not (i & task_2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
