# #!python

from binarysearchtree import BinarySearchTree

def swap(arr, first_index, second_index):
    arr[first_index], arr[second_index] = arr[second_index], arr[first_index]

def bubble_sort(arr):

    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                sorted = False
                swap(arr, i, i+1)

def selection_sort(arr):

    current_index = 0

    for i in range(len(arr)):

        # Find smallest
        new_index = current_index
        for i in range(current_index + 1, len(arr)):
            if arr[i] < arr[new_index]:
                new_index = i

        # Swap smallest and lowest
        swap(arr, current_index, new_index)

        # Increment current index
        current_index += 1

def insertion_sort(arr):

    current_index = 0
    for i in range(len(arr)):
        for j in range(0, current_index):
            if arr[i] < arr[j]:
                arr.insert(j, arr.pop(i))
                break
        current_index += 1

def counting_sort(arr):

    # Find min and max
    min_num = None
    max_num = None
    for num in arr:
        if num < min_num or min_num is None:
            min_num = num
        if num > max_num or max_num is None:
            max_num = num

    # Create a histogram
    histogram = [None] * (max_num - min_num + 1)

    # Add to buckets
    for num in arr:
        if histogram[num - min_num] is None:
            histogram[num - min_num] = (num, 1)
        else:
            histogram[num - min_num] = (num, histogram[num - min_num][1] + 1)

    # Overwrite array
    index = 0
    for item in histogram:
        if item is None:
            continue
        else:
            for num in range(item[1]):
                arr[index] = item[0]
                index += 1

def bucket_sort(arr):

    # Find min and max
    min_num = None
    max_num = None
    for num in arr:
        if num < min_num or min_num is None:
            min_num = num
        if num > max_num or max_num is None:
            max_num = num

    # Create buckets
    place = len(str(max_num))
    num_of_buckets = int(str(max_num)[0]) + 1

    buckets = [[] for _ in range(num_of_buckets)]
    
    # Add to buckets
    for num in arr:
        if len(str(num)) == len(str(max_num)):
            bucket_num = int(str(num)[::-1][place-1])
            buckets[bucket_num].append(num)
        else:
            buckets[0].append(num)

    # Sort all buckets
    for bucket in buckets:
        bubble_sort(bucket)

    # Overwrite array
    index = 0
    for bucket in buckets:
        for item in bucket:
            arr[index] = item
            index += 1

def merge(arr1, arr2):

    new_arr = []

    # Compare and add
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            new_arr.append(arr1.pop(0))
        else:
            new_arr.append(arr2.pop(0))

    # Add rest of elements
    if arr1:
        new_arr.extend(arr1)
    if arr2:
        new_arr.extend(arr2)

    # Return
    return new_arr

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    num = len(arr)//2
    new_list = merge(merge_sort(arr[:num]), merge_sort(arr[num:]))

    return new_list

def tree_sort(arr):

    bst = BinarySearchTree(arr)
    bst_list = bst.in_order_traversal()
    for i in range(len(arr)):
        arr[i] = bst_list[i]

def quick_sort(arr):

    # Return same arr
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr) - 1):


def partition(arr, left, right):

    # Set up pivot
    pivot = ((right - left) // 2) + left

    while arr[left] < pivot:
        left = left + 1
        if left > right:
            swap(arr, left, right)

    while arr[right] > pivot:
        right = right - 1
        if left > right:
            swap(arr: left, right)


def main():

    arr = [58, 25, 3, 7, 4, 9, 4, 3, 6]
    print(merge_sort(arr))
    # print(arr)

if __name__ == '__main__':
    main()


