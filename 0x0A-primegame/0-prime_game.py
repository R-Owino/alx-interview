#!/usr/bin/python3
"""
This module contains a function `isWinner` that returns the winner of a game
"""


def isWinner(x, nums):
    """
    Takes in 2 args to get the winner of the game

    Args:
        x (int): number of rounds
        nums (list): list of numbers

    Returns:
        str: name of the winner
    """
    # count prime numbers upto n
    def countPrimes(n):
        """
        Counts the number of prime numbers up to n

        Args:
            n (int): the upper limit

        Returns:
            int: the count of prime numbers
        """
        sieve = [True] * (n+1)
        sieve[0:2] = [False, False]  # 0 and 1 are not prime
        for current in range(2, int(n**0.5) + 1):
            if sieve[current]:  # current is prime
                for multiple in range(current*current, n+1, current):
                    sieve[multiple] = False
        return sum(sieve)

    # Check for edge cases
    if not nums or x < 1:
        return None

    # Play the game for each round and count wins
    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        primes = countPrimes(nums[i])
        if primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
