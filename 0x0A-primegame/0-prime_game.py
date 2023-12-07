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
    # check if a number is a prime
    def isPrime(n):
        """
        Checks if a number is a prime

        Args:
            n (int): number to check

        Returns:
            bool: True if n is a prime, False otherwise
        """
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    # count prime numbers upto n
    def countPrimes(n):
        """
        Counts the number of prime numbers up to n

        Args:
            n (int): the upper limit

        Returns:
            int: the count of prime numbers
        """
        count = 0
        for num in range(2, n):
            if isPrime(num):
                count += 1
        return count

    # play the game for each round and count wins
    winner = None
    for i in range(x):
        if countPrimes(nums[i]) % 2 == 0:
            winner = "Maria"
        else:
            winner = "Ben"
    return winner

    # determine overall winner
    if winner == "Maria":
        return "Maria"
    else:
        return "Ben"
    return None
