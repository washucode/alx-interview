#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Prime Game"""
    if x < 1 or not nums:
        return None
    n = max(nums)
    primes = [0] * (n + 1)
    for i in range(2, n + 1):
        primes[i] = primes[i - 1]
        if is_prime(i):
            primes[i] += 1
    wins = 0
    for n in nums:
        wins += primes[n] % 2 == 1
    return "Maria" if wins * 2 > len(nums) else "Ben"
