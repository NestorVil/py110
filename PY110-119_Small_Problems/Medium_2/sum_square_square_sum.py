# P:
#   Input: A positive integer representing a count
#   Output: An integer representing the difference between (the square of the sum of every number
#           leading up to the count integer) and (the sum of the squares leading up to the count integer)
#   Explicit:
#       Looks like this count = 3 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
#       Need to get every number leading up to and including the count integer
#       After doing that need to (sum of all)**2 - (sum of all with each num**2)
# E:
    # print(sum_square_difference(3) == 22)          # True
    # # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

    # print(sum_square_difference(10) == 2640)       # True
    # print(sum_square_difference(1) == 0)           # True
    # print(sum_square_difference(100) == 25164150)  # True
# D:
#   Probably need a list to get every number up to and including the count integer
# A:
#   1. Get every number leading up to and including the count input integer
#   2. Create a sum_square variable and have it capture the sum of the leading_up variable squared
#   3. Create a square_sum variable and have it capture:
#       A. For every number in the leading_up variable
#           A. Square root it
#   4. Subtract sum_square to square-sum and return it

def sum_square_difference(count_input):
    every_number = [num for num in range(count_input + 1)]

    sum_square = sum(every_number)**2
    square_sum = sum([num**2 for num in every_number])

    return sum_square - square_sum

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True