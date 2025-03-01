# P:
#   Input: Two integers as arguments. First a count, 2nd a starting number of a sequence
#   Output: A list containing the same number of elements as the count argument, the value of each
#           element should be multiple of the starting (5, 2) == [2, 4, 6, 8, 10]
# Explicit:
#   Creating a list, count, number*current index number
# E:
    # print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
    # print(sequence(4, -7) == [-7, -14, -21, -28])     # True
    # print(sequence(3, 0) == [0, 0, 0])                # True
    # print(sequence(0, 1000000) == [])                 # True
# D:
#   Lists
# A:
#   1. Using the first input integer, turn it into a range
#   2. For each iteration of that range, times the current iteration by the second input integer
#   3. Put both into a list
#   4. Return the list

def sequence(count, starting_number):
    return [num * starting_number for num in range(1, count + 1)]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True