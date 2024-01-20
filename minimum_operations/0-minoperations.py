#!/usr/bin/python3

"""
This script defines a function minOperations to calculate
the fewest number of operations needed to result in exactly n H characters.
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to reach exactly n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations.
    """
    if n <= 1:
        return 0

    result = float('inf')
    for i in range(2, n + 1):
        if n % i == 0:
            operations = minOperations(n // i) + i
            result = min(result, operations)

    return result

# Example usage
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
