# COUNTING SORT: this algorithm sorts an array by counting the number of times each value occurs.
# it works with only non-negative numbers

# To implement the counting sort
# 1. An array with values to sort.
# 2. Receives an array of integers
# 3. To keep the count of the values
# 4. Count and removes values, by incrementing element in the array
# 5. Recreate the array by using the counting array, so that the element appear in the right order.


def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr


unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
print(f"unsorted Array : {unsortedArr}")
sortedArr = counting_sort(unsortedArr)
print(f"Sorted array using counting sort : {sortedArr}")
