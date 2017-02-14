# #!python

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

    buckets = [] * len(arr)
    pass


def main():
    arr = [18, 5, 3, 7, 4, 9, 4, 3, 6]
    counting_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()


