#!python

import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    """iteratively return the index of the item or None if not found"""
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index
    return None


def linear_search_recursive(array, item, index=0):
    """recursively return the index of the item or None if not found"""
    # No item
    if index >= len(array):
        return None

    # Found item
    if array[index] == item:
        return index

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    #return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    """iteratively return the index of the item with binary search or None if not found"""
    lower_index = 0
    upper_index = len(array) - 1

    while lower_index <= upper_index:

        middle_index = (lower_index + upper_index) // 2 # // is int division

        if array[middle_index] == item:
            return middle_index
        elif array[middle_index] > item:
            upper_index = middle_index - 1
        elif array[middle_index] < item:
            lower_index = middle_index + 1

    # Did not find
    return None


def binary_search_recursive(array, item, lower_index=None, upper_index=None):
    """iteratively return the index of the item with binary search or None if not found"""
    if lower_index is None or upper_index is None:
        lower_index = 0
        upper_index = len(array) - 1

    # None found
    if lower_index > upper_index:
        return None

    # Create middle index
    middle_index = (lower_index + upper_index) // 2

    # Do checks
    if array[middle_index] == item:
        return middle_index
    elif array[middle_index] > item:
        return binary_search_recursive(array, item, lower_index, middle_index - 1)
    elif array[middle_index] < item:
        return binary_search_recursive(array, item, middle_index + 1, upper_index)

