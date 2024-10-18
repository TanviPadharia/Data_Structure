# INSERTION SORT : The Insertion Sort algorithm uses one part of the array to
# hold the sorted values, and the other part of the array to hold values that are not sorted yet.

# To implement the insertion sort
# 1. An array with values to sort.
# 2. An outer loop that picks a value to be sorted.For an array with n values, this outer loop skips the first
# values and must runs n - 1 times.
# 3.An inner loop that goes through the sorted part of the array to find where to insert the value.
# If the value to be sorted is at index i, the sorted part of the array starts at index 0 and ends index i-1.


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)

for i in range(1, n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i - 1, -1, -1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)
print(f"Insertion sort: {my_array}")

# improved code of insertion sort
# this solve the issue of the time as in the pervious code it used to pop the element from the unsorted array
# to sorted array and in this improvised code the just swap the element and move back the largest element

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1, n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i - 1, -1, -1):
        if my_array[j] > current_value:
            my_array[j + 1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_value

print("Improved insertion sorted array:", my_array)
