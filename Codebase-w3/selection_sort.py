# SELECTION SORT : The Selection Sort algorithm finds the lowest value in an array
# and moves it to the front of the array.

# To implement the selection sort
# 1.An array with values to sort.
# 2.An inner loop that goes through the array, find the lowest value and moves it to the front of the array
# this loop must loop through one less value each times it runs
# 3.An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop
# must loop run n-1 times


my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("Sorted selection sort array:", my_array)


# In the above slection sort code the lowest value was removed and then inserted which cause the
# extra time becuase of shift the other another backwards and to this problem solution is swapping the values
# instead removing, instering and shifing
# here is the code :

my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("Sorted improved selection sort :", my_array)


# Calculating the time taken
import timeit


# Original Selection Sort with pop() and insert()
def selection_sort_original():
    my_array = [64, 34, 25, 5, 22, 11, 90, 12]
    n = len(my_array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        min_value = my_array.pop(min_index)
        my_array.insert(i, min_value)


# Improved Selection Sort with swapping
def selection_sort_improved():
    my_array = [64, 34, 25, 5, 22, 11, 90, 12]
    n = len(my_array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        my_array[i], my_array[min_index] = my_array[min_index], my_array[i]


# Time both versions using timeit
original_time = timeit.timeit(selection_sort_original, number=1000)
improved_time = timeit.timeit(selection_sort_improved, number=1000)

print("Time taken by original selection sort: {:.6f} seconds".format(original_time))
print("Time taken by improved selection sort: {:.6f} seconds".format(improved_time))
