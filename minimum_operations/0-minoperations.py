#!/usr/bin/python3
"""
Minimum Operations: 
This script defines a function minOperations to calculate
the fewest number of operations needed to result in exactly n H characters.
"""
import math


def minOperations(n):
    """
    Minimum Operations:
    Calculate the fewest number of operations needed to reach exactly n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations.
    """
    if n <= 1:
        return 0

    operations = 0
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        operations += n

    return operations
