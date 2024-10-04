#!/usr/bin/python3
"""
0. Pascal's Triangle
"""
def pascal_triangle(n):
    lst = []
    if n > 0:
        for i in range(1, n + 1):
            lvl = []
            x = 1
            for j in range(1, i + 1):
                lvl.append(C)
                x = x * (i - j) // j
            lst.append(level)
    return lst
