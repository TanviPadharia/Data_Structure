# pseudocode for buuble sort
# TO implement the bubble sort algorithm:
# 1.An array with values to sort.
# 2.An inner loop that goes through the array and swaps values if the first value is higher than text value.
# This loop must loop through one less value each time it runs.
# 3.An outer loop that controls how many times the inner loop must run.For an array with n values,
# the outer loop must run n-1 times.

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# my_array = [7, 3, 9, 12, 11]
n = len(my_array)
for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

print("Sorted array :", my_array)

# ==============================================================

# Bubble - sort Improvement

# In this case, the array will be sorted after the first run, but the Bubble Sort
# algorithm will continue to run, without swapping elements, and that is not necessary.

# If the algorithm goes through the array one time without swapping any values,
# the array must be finished sorted, and we can stop the algorithm, like this:


arr = [7, 3, 9, 12, 11]

n = len(arr)
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        break
print(f"Sorred array : {arr}")

# The Bubble Sort algorithm loops through every value in the array, comparing it to the value next to it.
# So for an array of n
#  values, there must be n
#  such comparisons in one loop.

# And after one loop, the array is looped through again and again  n
#  times.

# This means there are  n ⋅ n comparisons done in total, so the time complexity for Bubble Sort is:

# O(n2)
