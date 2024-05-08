#!/usr/bin/python3
"""
This module defines a function that calculates the fewest number of 
operations needed to result in exactly n H characters in the a given file.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to result in 
    exactly n H characters in a given file.
    """
    if type(n) is not int or n <= 1:
        return 0
    factor = []

    divisor = 2
    while (n % divisor) == 0 and (n // divisor) != 1:
        factor.append(divisor)
        n = n // divisor
    divisor = 3
    while n > divisor:
        while (n % divisor) == 0 and (n // divisor) != 1:
            factor.append(divisor)
            n = n // divisor
        divisor += 2
    factor.append(n)

    return sum(factor)
