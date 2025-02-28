# P:
#   Input: a list of numbers
#   Output: a list with the same number of elemends, but with each element being the running total from the og list
#   Questions:
#       Will it be the same list, or a new list?
#       Can input list be empty?
#   Explicit Requirements:
#       Add previous element number to the next element number
# E:
    # print(running_total([2, 5, 13]) == [2, 7, 20])    # True
    # print(running_total([14, 11, 7, 15, 20])
    #       == [14, 25, 32, 47, 67])                    # True
    # print(running_total([3]) == [3])                  # True
    # print(running_total([]) == [])                    # True

#   Lists can be empty
#   Looks like theyre new lists
# D:
#   Working with two lists
#   [2, 5, 13] will be [element0, elementprevious + elementcurretn]
# A:
#   1. Create new variable "element_value" and assign it to 0
#   2. Create a new empty list "running_list"
#   3. Iterate over the input list
#   4. For each iteration, add to the "element_value"
#   5. For each iteration, append "element_value" to "running_list"
#   6. Do all of this if the input list isn't empty

def running_total(list):
    element_value = 0
    empty_list = [ ]
    for element in list:
        element_value += element
        empty_list.append(element_value)
    return empty_list



print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True