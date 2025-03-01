# P:
#   Input: A list
#   Output: A list that contains two elements, both are lists. First half of the og list in the 1st nested, 2nd half in 2nd nested
#   Explicit:
#       If the original list contains odd num of elements, place middle element in the first half
# E:
    # # All of these examples should print True
    # print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
    # print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
    # print(halvsies([5]) == [[5], []])
    # print(halvsies([]) == [[], []])
# D:
#   Lists and nested lists. Will need a way to cut a list in half and round up
# A:
#   1. Make a new variable and have it contain the first half of the input list rounded up
#   2. Make a new variable and have it contain the last half of the input list
#   3. Make a new list and populate it with a nested list of the first two variables
#   4. Return it

import math

def halvsies(full_list):
    half = math.ceil(len(full_list) / 2)
    halfed_list = [full_list[:half], full_list[half:]]

    return halfed_list



print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])