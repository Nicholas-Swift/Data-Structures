#!python

import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):

    # Base case
    if array[index] == item:
        return index

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # Binary search iteratively

    # Base cases
    if not array:
        return None
    
    

    # Iterate through
    while len(array) > 1:

        # Set to middle of array
        index = int(math.floor(len(array)/2))

        # Found item, return
        if item == array[index]:
            return item

        # Too low, slice to upper half of array
        if item > array[index]:
            array = array[index:]

        # Too high, slice to lower half of array
        elif item < array[index]:
            array = array[:index]

        print(array)

    # if len(array) == 1 and item == array[0]:
    #     return item

    # Did not find
    return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
