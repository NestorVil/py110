# P:
#   Input: Two lists of integers of the same length
#   Output: A new list where each element is the product of the corresponding elements from the list lists
#   Explicit:
#       Multiplying two corresponding elements of a list together
#       Creating a new list and adding the multiplication result to it
# E:
    # list_a = [1, 2, 3]
    # list_b = [4, 5, 6]
    # print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

#   [1 * 4, 2 * 5, 3 * 6]
# A:
#   1. Combine the two lists at matching elements
#   2. Multiply the matching elements together
#   3. Put the result of the multiplication into a new list and return it

def multiply_items(list1, list2):
    return [list_num_1 * list_num_2 for list_num_1, list_num_2 in zip(list1, list2)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# This other guy did this
def multiply_items(list1, list2):
    return [list1[idx] * list2[idx] for idx in range(len(list1))]