"""
# # # #
# # # #
# # # #
# # # #
"""
for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()

"""
#
# #
# # #
# # # #
"""
for i in range(4):
    # +1 is for element 0 otherwise it start with 1
    for j in range(i+1):
        print("# ",end="")
    print()

"""
# # # #
# # #
# #
#
"""
for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")

"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
k = 0
rows = 5
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()