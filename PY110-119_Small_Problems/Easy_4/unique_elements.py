# P:
#   Input: Two list arguments
#   Output: A set that has the unique elements exlusive to the first set

def unique_from_first(list1, list2):
    return set(list1) - set(list2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

# I looked up lesson 1 again. the - for sets is the same as fruits1.difference(fruits2) (with fruits1 and 2 being sets obv)