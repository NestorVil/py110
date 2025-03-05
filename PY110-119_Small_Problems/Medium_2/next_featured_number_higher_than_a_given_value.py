# P:
#   Input: A digit
#   Output: Another digit representing the next featured number g reather than the input
#   Explicit:
#       A featured number is an odd number that is a multiple of 7, with all of its digits occuring exactly once each
#       The return digit needs to be both higher than the input and be a featured number
#       Need to get first occurance of number bigger than the featured number, 
#           is a multiple of 7, is odd, and has each digit being unique
#       If no such next featured number, return an error messages (number bigger than 9876543201)
# E:
    # print(next_featured(12) == 21)                  # True
    # print(next_featured(20) == 21)                  # True
    # print(next_featured(21) == 35)                  # True
    # print(next_featured(997) == 1029)               # True
    # print(next_featured(1029) == 1043)              # True
    # print(next_featured(999999) == 1023547)         # True
    # print(next_featured(999999987) == 1023456987)   # True
    # print(next_featured(9876543186) == 9876543201)  # True
    # print(next_featured(9876543200) == 9876543201)  # True

    # error = ("There is no possible number that "
    #          "fulfills those requirements.")
    # print(next_featured(9876543201) == error)       # True
# D:
#   Need a way to count the amount of occurance of a digit in the number
# A:
#   1. Iterate the range of 7 and the largest featured number skipping every 7th step.
#       A. If the number is odd 
#       B. and bigger than the input integer 
#       C. and has unique digits
#           A. Split the digit into a string
#           B. Count the occurance of each digit
#           C. return if no occurance greater than 1
#       D. Return it

def to_odd_multiple_of_7(number):
    number += 1
    while number % 2 == 0 or number % 7 != 0:
        number += 1

    return number

def all_unique(number):
    digits = list(str(number))
    return len(digits) == len(set(digits))

def next_featured(number):
    MAX_FEATURED = 9876543201
    featured_num = to_odd_multiple_of_7(number)

    while featured_num <= MAX_FEATURED:
        if all_unique(featured_num):
            return featured_num

        featured_num += 14

    return "There is no possible number that fulfills those requirements."
        
error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True