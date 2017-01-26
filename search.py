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
    #return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # Binary search iteratively

    # Base cases
    if not array:
        return None

    current_index = int(math.floor(len(array)/2))

    # Iterate through
    while len(array) > 1:

        # Set to middle of array
        index = int(math.floor(len(array)/2))

        # Found item, return
        if item == array[index]:
            return current_index

        # Too low, slice to upper half of array
        if item > array[index]:
            array = array[index:]
            current_index += int(math.floor(len(array)/2))

        # Too high, slice to lower half of array
        elif item < array[index]:
            array = array[:index]
            current_index += int(math.floor(len(array)/2)) - len(array)

    # Last element in array
    if array[0] == item:
        return current_index

    # Did not find
    return None

def binary_search_recursive(array, item, index=None, current_index=None):

    # Empty array
    if not array:
        return

    # Set up indexes
    if current_index is None:
        current_index = int(math.floor(len(array)/2))
    index = int(math.floor(len(array)/2))

    # Last item
    if len(array) == 1:
        if array[0] == item:
            return current_index
        else:
            return None

    # Found item, return
    if item == array[index]:
        return current_index

    # Too low, slice to upper half of array
    if item > array[index]:
        array = array[index:]
        current_index += int(math.floor(len(array)/2))

    # Too high, slice to lower half of array
    elif item < array[index]:
        array = array[:index]
        current_index += int(math.floor(len(array)/2)) - len(array)

    return binary_search_recursive(array, item, index, current_index)

