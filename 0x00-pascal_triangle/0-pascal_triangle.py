#!/usr/bin/python3
"""
0-pascal_triangle returns an array of array
each sub-array represents a row in the pascal triangle
representation of the number passed in as an argument.
"""


def factorial(n):
    """
    Calculate the factorial
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def combination(n, r):
    """
    Calculate nCr ie n combination r
    """
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


def generate_row(n):
    """
    Generates and returns row i of the pascal's triangle
    """
    array = [1]
    if n == 2:
        array.append(1)
    elif n > 2:
        array += compute_coefficients(n - 1) + [1]
    return array


def compute_coefficients(n):
    """
    Generates and returns the row i of the pascal's triangle as an array
    """
    array = []
    stop_index = int((n / 2) + 1) if ((n % 2) == 0) else int(((n + 1) / 2) + 1)
    for i in range(1, stop_index):
        array.append(combination(n, i))

    reversed = array[::-1]

    result = array + reversed[1:] if n % 2 == 0 else array + reversed[2:]
    return result


def pascal_triangle(n):
    """
    Generates the entire pascal's triangle of an as an array of arrays
    """
    result = [""]

    if n >= 1:
        for i in range(1, n + 1):
            result.append(generate_row(i))
        result = result[1:]

    return result
