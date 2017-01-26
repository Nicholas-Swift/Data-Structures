#!python

import unittest


def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    #return factorial_recursive(n)
    return factorial_iterative(n)


def factorial_iterative(n):

    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))

    # check if n is one of the base cases
    elif n == 0 or n == 1:
        return 1

    # Create number (start with 1 rather than 0)
    num = 1

    # For loop through all numbers up to n
    for i in range(1, n):
        num += num * i

    # Return num
    return num


def factorial_recursive(n):

    # check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('factorial is undefined for n = {}'.format(n))

    # check if n is one of the base cases
    elif n == 0 or n == 1:
        return 1

    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)
