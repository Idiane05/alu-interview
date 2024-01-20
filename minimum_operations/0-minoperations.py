#!/usr/bin/python3

def minOperations(n):
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
