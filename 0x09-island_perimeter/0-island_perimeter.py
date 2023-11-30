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
    # keep track of perimeter
    perimeter = 0

    # iterate thru each cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # if cell is land
            if grid[row][col] == 1:
                perimeter += 4
                # check neighboring cells
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
