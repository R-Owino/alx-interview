## Making Change

The problem:
```
Given a pile of coins of different values, determine the fewest 
number of coins needed to meet a given amount total.
```

- Assumptions: There is an infinite number of each denomination of coin in the list.
- The solution should be optimal, i.e. lower complexity.

The approach:
- There are 2 ways to solve this problem:

1. Recursion
- Consider 2 possibilities at each step: either include a coin in the solution or exclude it.
:thumbsdown: Using recursion results into an exponential time complexity and might not be efficient for large inputs.

2. Dynamic Programming
- This is a way better option to optimize the program. It avoids 
redundant work by storing and reusing solutions to subproblems
\* The solution is faster due to optimized subproblem solving and memoization.

- While both approaches are powerful for solving complex problems, dynamic programming is more efficient and that's what I used to solve this problem.

#### Sample output
0-main.py contains the driving function. Run it like so:
`python3 0-main.py`

The output should look like:
```
remmy@remmy:~/alx-interview/0x08-making_change$ python3 0-main.py 
7
-1
```
