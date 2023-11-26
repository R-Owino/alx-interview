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
    # Initialize dp array with total+1 as we can't have more coins than total+1
    dp = [total + 1] * (total + 1)

    # When total is 0, 0 coins are needed
    dp[0] = 0

    # Loop through all totals from 1 to total
    for i in range(1, total + 1):
        # For each coin value
        for j in range(len(coins)):
            # If the coin value is less than or equal to the total
            if coins[j] <= i:
                # Update the dp value for this total
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    # If the dp value for total is still total+1,
    # then we can't make the total with the coins
    if dp[total] == total + 1:
        return -1

    # Return the dp value for total
    return dp[total]
