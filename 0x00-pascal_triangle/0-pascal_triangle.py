#!/usr/bin/python3
"""
Function that returns a list of lists of integers representing the
Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Returns list of lists rep'n Pascal's Triangle

    Args:
        n(int): input number of rows
    """

    if n <= 0:
        return []

    pascal_triangle = [[1]]

    while len(pascal_triangle) < n:
        last_row = pascal_triangle[-1]
        new_row = [1]

        for i in range(1, len(last_row)):
            new_row.append(last_row[i - 1] + last_row[i])

        new_row.append(1)
        pascal_triangle.append(new_row)

    return pascal_triangle
