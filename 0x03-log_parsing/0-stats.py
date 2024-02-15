#!/usr/bin/env python3

"""0. Log parsing"""

import sys


def metrics(lines):

    # initialize size of file
    file_size = 0

    # initialize status codes
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    # initialize count of lines
    count = 0

    for line in lines:
        count += 1
        data = line.split()
        try:
            file_size += int(data[-1])
        except(ValueError):
            pass
        try:
            status_codes[data[-2]] += 1
        except(KeyError):
            pass

    print("File size: {}".format(file_size))

    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    metrics(lines)
