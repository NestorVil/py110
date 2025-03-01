# P:
#   Input: aN INTEGER
#   Output: A list containing all integers between 1 and the argument(inclusive) in ascending order:
# I assume that means the integer will always begin at 1 at least
# E:
    # print(sequence(5) == [1, 2, 3, 4, 5])   # True
    # print(sequence(3) == [1, 2, 3])         # True
    # print(sequence(1) == [1])               # True
# D:
#   Integers and lists
# A:
#   Turn the integer input into a range
#   Iterate over that range
#   For each iteration (starting at 0 and ending in the num + 1) add the number to a new list
#   Return the new list

def sequence(input_integer):
    return [num for num in range(1, input_integer + 1)]

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True