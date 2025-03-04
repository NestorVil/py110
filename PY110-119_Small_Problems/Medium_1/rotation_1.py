# P:
#   Input: A list
#   Output: A separate list which moves the first element to the end of the list
#   Explicit:
#       No mutation. Return new list
#       Return an empty list if the input is an empty list
#       Return None if the input is not a list
# E:
# All of these examples should print True

    # print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
    # print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
    # print(rotate_list(['a']) == ['a'])
    # print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
    # print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
    # print(rotate_list([]) == [])

    # # return `None` if the argument is not a list
    # print(rotate_list(None) == None)
    # print(rotate_list(1) == None)

    # # the input list is not mutated
    # lst = [1, 2, 3, 4]
    # print(rotate_list(lst) == [2, 3, 4, 1])
    # print(lst == [1, 2, 3, 4])

#   Everything seems as expected
# D:
#   Lists
# A:
#   1. If the input_list isn't a list, return None
#   2. If the input_list is empty, return an empty list
#   3. Create a copy of the input_list
#   4. Remove the first element of the copied_list, saving it to a variable
#   5. Add the saved_variable to the end of the copied_list
#   6. Return the copied list

def rotate_list(input_list):
    if not isinstance(input_list, list):
        return None
    if input_list == []:
        return input_list
    copied_list = input_list[:]
    popped_element = copied_list.pop(0)
    copied_list.append(popped_element)
    return copied_list

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])