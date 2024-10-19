# QUICKSORT : Quicksort algorithm takes an array of values, chooses one of
# the values as the 'pivot' element, and moves the other values so that lower values are on the left of the
# pivot element, and higher values are on the right of it.


# To implement the quick sort
# 1. An array with values to sort.
# 2. An pivot values is taken and all the values that are higher moves to right vice-versa
# values that are lower moves to left from the pivot values and then pivot changes
# 3. An partition method that receives a sub-array, moves values around, swaps the pivot
# element into the sub-array and returns the index where the next split in sub-arrays happens.


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)


# The recursion part of the Quicksort algorithm is actually a reason why the average sorting
# scenario is so fast, because for good picks of the pivot element, the array will be split
# in half somewhat evenly each time the algorithm calls itself. So the number of recursive
# calls do not double, even if the number of values n double.

# The worst case scenario for Quicksort is O(n2). This is when the pivot element is either
# the highest or lowest value in every sub-array, which leads to a lot of recursive calls.
# With our implementation above, this happens when the array is already sorted.

# But on average, the time complexity for Quicksort is actually just O(nlogn),
# which is a lot better than for the previous sorting algorithms we have looked at.
# That is why Quicksort is so popular.
