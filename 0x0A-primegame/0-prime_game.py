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
    def get_prime_count(n):
        if n < 2:
            return 0
        count = 0
        for i in range(2, n + 1):
            if n % i == 0:
                count += 1
        return count

    if not nums or x < 1:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        if i % 2 == 0:
            Maria += get_prime_count(nums[i])
        else:
            Ben += get_prime_count(nums[i])
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
