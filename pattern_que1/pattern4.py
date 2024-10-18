"""
pattern2

        *
       **
      ***
     ****
    *****

"""

rows = 5


# for i in range(0, rows):
#     for j in range(i, rows):
#         print("*", end=" ")
#     print()


for i in range(0, rows):
    for j in range(0, rows):
        if j <= rows - 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
