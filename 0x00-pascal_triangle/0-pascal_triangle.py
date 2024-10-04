#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    lst = []
    if n <= 0:
        return k
    lst = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(lst[i - 1]) - 1):
            curr = k[i - 1]
            temp.append(lst[i - 1][j] + lst[i - 1][j + 1])
        temp.append(1)
        lst.append(temp)
    return lst 
