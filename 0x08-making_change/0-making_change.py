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
    if not coins:
        return -1
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total %= coin
    if total != 0:
        return -1
    return num_coins
