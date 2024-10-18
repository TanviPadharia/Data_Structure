# searching in unstored array


def findElement(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i

    # if key is not found
    return -1


if __name__ == "__main__":
    arr = [2, 34, 17, 6, 40]
    key = 6
    n = len(arr)

    # search elements :
    index = findElement(arr, n, key)
    if index != -1:
        print("Element found at positon: ", str(index + 1))
    else:
        print("Element not found.")

# Time Complexity: O(N)
# Auxiliary Space: O(1)
