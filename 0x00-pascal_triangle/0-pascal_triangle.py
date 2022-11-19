#!/usr/bin/python3
"""
0-pascal_triangle returns an array of array
each sub-array represents a row in the pascal triangle
representation of the number passed in as an argument.
"""


def pascal_triangle(n):
    """
    Generates the entire pascal's triangle of an as an array of arrays
    """
    result = []

    for i in range(n):
        row = [1]
        result.append(row)
        for j in range(1, i):
            next_coefficient = result[i - 1][j - 1] + result[i - 1][j]
            row.append(next_coefficient)
        if i >= 1:
            row.append(1)

    return result if n > 0 else []
