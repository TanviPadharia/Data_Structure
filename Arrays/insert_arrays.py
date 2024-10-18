# insert the element at the end


def insertEnd(arr, element):
    arr.append(element)


if __name__ == "__main__":
    arr = [12, 12, 25, 40, 59, 88]
    key = 2

    print("Before intresecting :")
    print(arr)

    # arrat after inseringr element
    insertEnd(arr, key)
    print("array instargram")
    print(arr)


# Time Complexity: O(1)
# Auxiliary Space: O(1)


# inserting at any position
