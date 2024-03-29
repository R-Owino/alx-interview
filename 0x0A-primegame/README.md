## Prime Game

The problem:
```
Maria and Ben are playing a game. 
Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. 
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.
```

Problem instructions:
- Assume n and x will not be larger than 10000
- Return name of the player that won most rounds
- Return `None` if winner cannot be determined

### Example:
- x = 3, nums = [4, 5, 1]

First round: 4
- Maria picks 2 and removes 2, 4, leaving 1, 3
- Ben picks 3 and removes 3, leaving 1
- Ben wins because there are no prime numbers left for Maria to choose

Second round: 5
- Maria picks 2 and removes 2, 4, leaving 1, 3, 5
- Ben picks 3 and removes 3, leaving 1, 5
- Maria picks 5 and removes 5, leaving 1
- Maria wins because there are no prime numbers left for Ben to choose

Third round: 1
- Ben wins because there are no prime numbers for Maria to choose

**Result: Ben has the most wins**

### The approach:
1. Prime Sieve: First, generate all prime numbers up to `n`.

2. Game Play: Maria and Ben take turns to pick a prime number and remove that number and its multiples. The player who cannot make a move loses the game.

3. Optimal Strategy: Since both players play optimally, they would always choose the smallest available prime number. This is because choosing a larger prime number would potentially leave more options for the opponent in the next turn.

4. Determine the Winner: If the number of primes is even, Ben wins, because Maria will be forced to pick the last prime number. If the number of primes is odd, Maria wins, because she can always mirror Ben’s moves and ensure she picks the last prime number.


### Running the code:
```
remmy@remmy:~/alx-interview/0x0A-primegame$ python3 0-main.py 
Winner: Ben
```