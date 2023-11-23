#!/usr/bin/python3
"""
The making change problem:
  This module contains the function makeChange, that solves the
  making change problem dynamically.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the coin denominations available.
        total (int): The total amount needed.

    Returns:
        Fewest number of coins needed to meet total
        if total is 0 or less, return 0
        if total cannot be met by any number of coins, return -1
    """

    if total <= 0:
        return 0

    # sort coins in descending order for optimization
    coins.sort(reverse=True)

    # Create a list to store the fewest number of coins needed to make change
    # for each value from 0 to total
    change = [0] + [float('inf')] * total

    # For each value from 1 to total, determine the fewest number of coins
    # needed to make change
    for i in range(1, total + 1):
        for coin in [c for c in coins if c <= i]:
            change[i] = min(change[i], change[i - coin] + 1)

    # If change[total] is still infinity, then total cannot be met by any
    # number of coins
    if change[total] == float('inf'):
        return -1

    return change[total]
