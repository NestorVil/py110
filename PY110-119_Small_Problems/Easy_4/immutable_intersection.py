# P:
#   Input: Two lists
#   Output: A frozenset that is the common elements of the two lists
# A:
#   1. Convert first list into a frozen set
#   2. Convert 2nd list into a frozen set
#   3. Assign their common elements to a new set and return it

def intersection(list1, list2):
    set1 = frozenset(list1)
    set2 = frozenset(list2)
    common_element = set1 & set2
    return common_element

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True