# P:
#   Input: Two lists
#   Output: A new list that contains all elements from both input lists, with each element taken in alternation
#   Explicit:
#       Returning new list, one element, then one element again, then next one element ect
#  Will the two input lists always have the same amount of elements?
#  What to do if they don't?
# E:
    # list1 = [1, 2, 3]
    # list2 = ['a', 'b', 'c']
    # expected = [1, "a", 2, "b", 3, "c"]
    # print(interleave(list1, list2) == expected)      # True

#   Look's like here the two lists will always have the same amount of elements the first passed in list goes first
# D:
#   Working with just lists here
# A:
#   1. Combine the two lists together
#   2. Create a new empty list
#   3. Go through the combined list
#   4. Add the elements to the empty list

def interleave(list1, list2):
    zipped_list = list(zip(list1, list2))
    new_list = []
    for couple in zipped_list:
        new_list.extend(couple)
    return new_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True