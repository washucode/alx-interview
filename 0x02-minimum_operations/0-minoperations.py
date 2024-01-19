#!/usr/bin/python3

"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file;
 Copy All and Paste.
 Given a number n, write a method that calculates the
 fewest number of operations needed
"""


def minOperations(n):
    """ Calculates the fewest number of operations needed
    """
    if n <= 1:
        return 0

    if n == 1:
        return 1

    def prime_factors(n):
        """ Calculates the prime factors of a number.
            Will help apply Copy All Appropriately.
        """
        factors = []
        for i in range(2, n + 1):
            while n % i == 0:
                factors.append(i)
                n /= i
        if n > 1:
            factors.append(n)
        return factors

    factors = prime_factors(n)
    return int(sum(factors))
