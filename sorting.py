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

        end = True
        for j in range(0, current_index):
            if arr[i] < arr[j]:
                arr.insert(j, arr.pop(i))
                end = False
                break
        if end:
            arr.insert(current_index, arr.pop(i))
        current_index += 1


def main():
    arr = [700, 1, 5, 3, 7, 4, 9, 4, 3, 700]
    insertion_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()


