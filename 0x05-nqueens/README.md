## N queens

- The N queens puzzle is a [backtracking](https://en.wikipedia.org/wiki/Backtracking) technique challenge of placing N non-attacking queens on an N×N chessboard.

<p>The idea is to place queens one by one in different columns, starting from the leftmost column. When we place a queen in a column, we check for clashes with already placed queens. In the current column, if we find a row for which there is no clash, we mark this row and column as part of the solution. If we do not find such a row due to clashes, then we backtrack and return false.</p>

Approach instructions:
- Usage: nqueens N
	* If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
- where N must be an integer greater or equal to 4
	* If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
	* If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
- The program should print every possible solution to the problem
	- One solution per line
	- You don’t have to print the solutions in a specific order
- You are only allowed to import the sys module

Sample output:
remmy@remmy:~/alx-interview/0x05-nqueens# ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
remmy@remmy:~/alx-interview/0x05-nqueens# ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
remmy@remmy:~/alx-interview/0x05-nqueens# ./0-nqueens.py 3
N must be at least 4
