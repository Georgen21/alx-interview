#!/usr/bin/python3
"""
This module defines a function that calculates the fewest number of 
operations needed to result in exactly n H characters in a given file
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in 
    exactly n H characters in a given file.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The fewest number of operations needed.

    Raises:
        TypeError: If n is not an integer or is less than or equal to 1.
    """
    if not isinstance(n, int) or n <= 1:
        raise TypeError("n must be a positive integer greater than 1")

    summation = []

    divisor = 2
    while n > 1:
        while n % divisor == 0:
            summation.append(divisor)
            n //= divisor
        divisor += 1

    return sum(summation)
