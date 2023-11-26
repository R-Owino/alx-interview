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
    # If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # If there are no coins available, the total cannot be met
    if not coins:
        return -1

    # Sort coins in descending order for optimization
    coins.sort(reverse=True)

    # Initialize the count of coins needed
    num_coins = 0

    # Iterate through each coin denomination
    for coin in coins:
        # If the total is already met, exit the loop
        if total <= 0:
            break

        # Calculate the number of coins needed for the current denomination
        num_coins += total // coin

        # Update the remaining total after using the current denomination
        total %= coin

    # If the total is not completely covered by coins, return -1
    if total != 0:
        return -1

    # Return the total number of coins needed
    return num_coins
