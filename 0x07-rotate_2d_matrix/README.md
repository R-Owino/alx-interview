## Rotate 2D matrix

The problem:
```
Given an n x n 2D matrix, rotate it 90 degrees clockwise
```

Problem instructions:
- Do not import any module.
- Do not return anything. The matrix must be edited in place.
- Assume the matrix will have 2 dimensions and will not be empty.

The approach:
- I achieved this by performing 2 operations on the matrix:
    * Transpose the matrix - swap the elements at position (0, 1) with those at position (1, 0) for all 0 and 1. This turns rows to columns.
    * Reverse each row - swap the elements at position (0, 1) with those at position (0, n-1-1), where n is the number of columns. This rotates the matrix 90&deg; clockwise.

Example:
Input: `[[1, 2, 3],[4, 5, 6],[7, 8, 9]]`
Output: `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`
