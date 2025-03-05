# P:
#   Input: Two sorted lists
#   Output: A new list that contains all the elements from both input lists in ascending sorted order
#   Explicited:
#       CANNOT USE ANY SOLUTION THAT LETS MOE SORT
#       Need to return a new list
#       Has to be in ascending order (lowest to highest)
# E:
# All of these examples should print True
    # print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
    # print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
    # print(merge([], [1, 4, 5]) == [1, 4, 5])
    # print(merge([1, 4, 5], []) == [1, 4, 5])

    # names1 = ['Alice', 'Kim', 'Pete', 'Sue']
    # names2 = ['Bonnie', 'Rachel', 'Tyler']
    # names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
    #                   'Rachel', 'Sue', 'Tyler']
    # print(merge(names1, names2) == names_expected)

#   LISTS CAN BE EMPTY
# D:
#   Working with lists, need to find a way to get the minimum of a list
# A:
#   1. Add the two lists together to "big_list"
#   2. So long as big_list is not empty
#       A. find the lowest amount and assign it to lowest_element
#       B. Find at what place that lowest element occurs in the list
#       C. Pop the associated element and assign it to lowest_element
#       D. Append lowest_element to a new list
#   3. Return the new list

def merge(list1, list2):
    big_list = list1 + list2
    returning_list = []
    while big_list:
        lowest_element = min(big_list)
        index_position = big_list.index(lowest_element)
        lowest_element = big_list.pop(index_position)
        returning_list.append(lowest_element)
    
    return returning_list

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)