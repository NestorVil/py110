# P:
#   Input:  A list of integers
#   Output: The average of all integers in the list rounded down
#   Explicit:
#       Never empty list, always positive integers
#       To calculate average of a list of numbers, add them all up and then divide by the amount of numbers (2+5+8)/3
# E:
    # print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
    # print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
    # print(average([7]) == 7)                          # True

# D:
#   Working with lists and whole numbers (integers)
# A:
#   1. Add all the numbers in the list together "sum_of_list"
#   2. Divide "sum_of_list" by the amount of elements in that list
#   3. Round down and return it

def average(list1):
    sum_of_list  = sum(list1)
    return (sum_of_list // len(list1))

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

# I could've cut out line 20 and do somehting like sum(list1) // len(list1)