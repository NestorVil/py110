# P:
#   Input: Two lists, each a list of numbers
#   Output: A new list that contains the product of each pair of numbers from the arguments that have the same index
#   Explicit:
#       Multiple two numers of the same index together and populate the new list with that number at that index
# Will the two input lists always have the same amount?
# E:
    # list1 = [3, 5, 7]
    # list2 = [9, 10, 11]
    # print(multiply_list(list1, list2) == [27, 50, 77])  # True

#   Look's like they will
# D:
#   Working with lists, will need to multiply stuff
# A:
#   1. Create a new list that contains the appropiate indexed elements of the two lists
#   2. Multiple the two elements of that combined list together
#   3. Create a new empty list
#   4. Add the multiple of the two elements to the new empty list

def multiply_list(list1, list2):
    combined_list = list(zip(list1, list2))
    new_list = []
    for element in combined_list:
        new_num = element[0] * element[1]
        new_list.append(new_num)
    return new_list

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# Launchschool:
def multiply_list(numbers1, numbers2):
    return [a * b for a, b in zip(numbers1, numbers2)]

# Otherstudent:
def multiply_list(list1, list2):
    zipped = zip(list1, list2)

    return [ pair[0] * pair[1] for pair in zipped ]