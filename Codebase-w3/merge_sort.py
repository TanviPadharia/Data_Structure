# merge sort without recursion


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def mergeSort(arr):
    step = 1
    length = len(arr)

    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i : i + step]
            right = arr[i + step : i + 2 * step]

            merged = merge(left, right)

            # placing merged array back into original error
            for j, val in enumerate(merged):
                arr[i + j] = val

        step *= 2
    return arr


unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)


# merge sort using recursion


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft, sortedRight)


unsorted_Arr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = merge_sort(unsorted_Arr)
print("Sorted array with recursion:", sortedArr)
