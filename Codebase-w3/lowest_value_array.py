arr = [12, 3, 7, 23, 4, 0]
minVal = arr[0]

for i in arr:
    if i < minVal:
        minVal = i

print("Lowest value:", minVal)
