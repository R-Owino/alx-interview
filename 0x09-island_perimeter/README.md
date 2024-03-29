## Island Perimeter

The problem:
```
Return the perimeter of the island described in grid.
```

Problem instructions:
- The grid is a list of integers where:
    1. 0 = water
    2. 1 = land
- Each cell is a square with a side length of 1
- The cells are connected horizontally and/or vertically only
- The grid is rectangular with its width and height <= 100
- The grid is completely surrounded ny water
- There is just 1 island or nothing
- The island has no "lakes" (water inside not connected to the water outside)

The approach:
- Initialize a variable to keep track of the perimeter.
- Iterate through each cell in the grid; if it is a land cell increment the perimeter tracker by 4.
- For each land cell, check the neighbor cells. If a neighbor is land, decrement by 1; if water or outside the grid boundaries, do nothing.
- Continue the process for all the cells.
- Return the perimeter tracker variable.

Example:
```
remmy@remmy:~/alx-interview/0x09-island_perimeter$ python3 0-main.py 
12
```