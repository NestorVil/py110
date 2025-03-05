# P:
#   Input: A list
#   Output: A sorted list
#   Explicit:
#       Need to use a merge sort
#       A merge sort first breaks down the input list into halves until the innermost lists contain exactly one element
#       Then those individual elements are combined in pairs in proper ascending order
#       Need to halve the list into nested lists and those nested lists into further nested lists until single element
#       As working way up, combine them in assorted order
# E:
# All of these examples should print True
    # print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
    # print(merge_sort([5, 3]) == [3, 5])
    # print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
    # print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

    # original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
    #             'Kim', 'Bonnie']
    # expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
    #             'Sue', 'Tyler']
    # print(merge_sort(original) == expected)

    # original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
    #             43, 5, 25, 35, 18, 46]
    # expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
    #             35, 37, 43, 46, 51, 54]
    # print(merge_sort(original) == expected)
# D:
#   Lists and nested lists
# A:
#   1. Find the half way point of the initial_list and save it to a variable half_way
#   2. Index up into that half way point, placing it in a new list, and from halfway point onward, place in new list
#   3. For each individual list, do step 2 until can't divide any longer
#   4. Looking at the first half
#   5. Looking at the first half again
#   6. Repeat step 5 until reached a nested list of two lists
#   7. Pass both as arguments to previous function
#   8. Repeat 6-7 for second nested list
#   9. Go upward until finished merge sort and return it

# Launchschools solution
def merge_sort(lst):
    if len(lst) == 1:
        return lst

    sub_list1 = lst[:len(lst) // 2]
    sub_list2 = lst[len(lst) // 2:]

    sub_list1 = merge_sort(sub_list1)
    sub_list2 = merge_sort(sub_list2)

    return merge(sub_list1, sub_list2)