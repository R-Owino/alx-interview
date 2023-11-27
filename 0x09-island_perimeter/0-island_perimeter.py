#!/usr/bin/python3
"""
This module contains a function island_perimeter that returns
the perimeter of the island described in grid
"""

def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid

    Args:
        grid (list): list of integers

    Returns:
        perimeter (int): perimeter of the island described in grid
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] is 1:
                if row is 0 or grid[row - 1][col] is 0:
                    perimeter += 1
                if col is 0 or grid[row][col - 1] is 0:
                    perimeter += 1
                if col is len(grid[row]) - 1 or grid[row][col + 1] is 0:
                    perimeter += 1
                if row is len(grid) - 1 or grid[row + 1][col] is 0:
                    perimeter += 1
    return perimeter
