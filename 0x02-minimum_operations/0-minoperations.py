#!/usr/bin/python3
"""
0-minoperations.py has a method minOperations(n)
that returns the total number of minimum steps
needed to arrive at n H characters using only
Copy All and Paste operations.
"""


def minOperations(n):
    """
    Returns minimum steps needed to arrive
    at n H characters.
    """
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        copy_size = 1
        operations = 1
        counter = n - 1

        while counter > 0:
            if (n - (copy_size * 2)) == 0:
                counter = 0
                operations += 1
            elif (n % (copy_size * 2) == 0):
                counter -= copy_size
                copy_size *= 2
                operations += 2
            else:
                counter -= copy_size
                operations += 1

    return operations

