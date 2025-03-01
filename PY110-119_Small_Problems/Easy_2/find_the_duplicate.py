# P:
#   Input: An unordered list with the info that one value in the list occurs twice
#   Output: Which value occurs twice
#   Explicit:
#       May assume that the input list will always have exactly one duplicate value
# E:
    # print(find_dup([1, 5, 3, 1]) == 1) # True
    # print(find_dup([
    #                   18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
    #                   38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
    #                   14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
    #                   78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
    #                   89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
    #                   41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
    #                   55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
    #                   85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
    #                   40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
    #                    7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
    #               ]) == 73)       # True

#   Only one example but lists arent empty. Confirmed how lists will always have one duplicate value
# D:
#   Will be working with lists and returning an integer here
# A:
#   1. Create a new varible "multiple_occurance"
#   2. Go through the list and count each number
#   3. If the count of an element is greater than 1, assign it to "multiple_occurance"
#   4. Return it

def find_dup(the_list):
    #multiple_occurance = 0
    for element in the_list:
        if the_list.count(element) > 1:
            multiple_occurance = element
            break
    return multiple_occurance

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True

# Still works if I don't initialize the variable 
# Can use list comprehension too
def find_dup(lst):
    dups = [element for element in lst if lst.count(element) == 2]
    return dups[0]