# radix sort using the stable sorting algorithm - counting sort
# Stable Sorting: Radix Sort relies on a stable sorting algorithm
# (like Counting Sort) to sort the digits. Stability ensures that two equal elements retain their relative order.


myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array: ", myArray)

# empty list set from 0 to 9
radixArray = [[], [], [], [], [], [], [], [], [], []]

maxVal = max(myArray)

# exponent set 1 as unit
exp = 1

while maxVal // exp > 0:  # outer loop to process all the digits units,tens...

    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val // exp) % 10  # calculate the current digit
        radixArray[radixIndex].append(val)

    # rebuilding array

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)

    exp *= 10

print("Sorted array in the radix:", myArray)


# radix sort using the bubble sort as stable sort algorithm


# bubble sort logic
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def radixSortWithBubbleSort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        radixArray = [[], [], [], [], [], [], [], [], [], []]

        for num in arr:
            radixIndex = (num // exp) % 10
            radixArray[radixIndex].append(num)

        for bucket in radixArray:
            bubbleSort(bucket)

        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i += 1
        exp *= 10


myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixSortWithBubbleSort(myArray)
print("Sorted array of radix sort with bubble sort:", myArray)
