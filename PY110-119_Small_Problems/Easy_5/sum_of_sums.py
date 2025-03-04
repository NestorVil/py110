# P:
#   Input: A list of numbers
#   Output: The sum of each leading subsequence in that list
#   Explicit:
#       The list always contains at least one number
#       It's possible for inputs to only have 1 number
# E:
    # print(sum_of_sums([3, 5, 2]) == 21)               # True
    # # (3) + (3 + 5) + (3 + 5 + 2) --> 21

    # print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
    # # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

    # print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
    # # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

    # print(sum_of_sums([4]) == 4)                      # True

# D:
#   Lists
# A:
#   1. Create a list where each element is 


def sum_of_sums(numbers):
    total_sum = 0
    running_sum = 0
    for num in numbers:
        running_sum += num
        total_sum += running_sum

    return total_sum


print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True



def sum_of_sums(lst: list):
    return sum([sum(lst[:i]) for i in range(1, len(lst) + 1)])
