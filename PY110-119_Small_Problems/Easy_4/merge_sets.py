# P:
#   Input: Two lists
#   Output: A new set which is the union of both inputs also converted to sets
# A:
#   1. Add both lists together
#   2. Conver it to a set and return it

def merge_sets(list1, list2):
    return set(list1 + list2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

# Launchschool
def merge_sets(list1, list2):
    return set(list1) | set(list2)