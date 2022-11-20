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
    if n <= 1:
        return 0
    else:
        h_counter = 1
        operations = 1
        copy_size = 1

        while h_counter != n:
            if ((n % h_counter) == 0) and (h_counter != 1):
                copy_size = h_counter
                h_counter += copy_size
                operations += 2
            else:
                h_counter += copy_size
                operations += 1

    return operations
