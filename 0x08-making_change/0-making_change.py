#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet a given amount"""
    if total <= 0:
        return 0
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
