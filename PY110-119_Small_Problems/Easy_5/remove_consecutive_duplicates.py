# P:
#   Input: A sequence of integers (list of integers)
#   Output: A list (filtering out instances where the same value occurs successively, retaining only the initial occurance)
# A:
#   1. Make a copy of the input_list
#   2. Remove the first element of the copied list
#   3. Add the removed first element to returning list
#   4. Remove the next element of the copied list
#   5. If the removed element is in the returning list, discard it, otherwise add it
#   6. Return the returning list once the copied list is empty

def unique_sequence(og_list):
    copied_list = og_list[:]
    returning_list = []

    while copied_list:
        popped_element = copied_list.pop(0)
        if popped_element not in returning_list:
            returning_list.append(popped_element)

    return returning_list

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True