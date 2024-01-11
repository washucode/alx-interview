#!/usr/bin/python3
""" Pascal Triangle"""


def pascal_triangle(n):
    """ummary for pascal_triangle

    Args:
        n ([integer]): [number of rows or height of triangle]

    Returns:
        [array of arrays]: [pascal triangle]
    """
    triangle = []
    for h_index in range(n):
        row = [1]

        for w in range(1, h_index):
            row.append(triangle[h_index-1][w-1] + triangle[h_index-1][w])
        if h_index > 0:
            row.append(1)
        triangle.append(row)

    return triangle
