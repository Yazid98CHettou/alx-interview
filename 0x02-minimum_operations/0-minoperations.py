#!/usr/bin/python3
"""
Minimum Operations
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n
write a method that calculates the fewest number
of operations needed to result in exactly n H
characters in the file.
Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9
H => Copy All => Paste => HH => Paste =>HHH =>
Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
"""
def minOperations(n):
    """
    Function minOperations
    Returns an integer
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result
