#!/usr/bin/python3
"""
This module contains a function rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise

    Args:
        matrix (list of lists) - the 2D matrix to be rotated

    Returns:
        Nothing, the matrix is edited in-place
    """
    # determin the length of the matrix
    n = len(matrix)

    # transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse each row
    for i in range(n):
        matrix[i].reverse()
