# P:
#   Input: Two lists as arguments
#   Output: A set that contains the union of the values
#   Explicit:
#       Returning a new set
# E:
    # print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
#   Lists not empty
# D:
#   Lists and sets
# A:
#   Create a new set "union_list" thats the two given lists merged together
#   Turn the "union_set" into a set
#   Return it

def union(list1, list2):
    merged_lists = list1 + list2
    return set(merged_lists)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# Probably more in the spirit of it:

def union(list1, list2):
    return set(list1).union(set(list2))