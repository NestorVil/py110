# P:
#   Input: Two digits, a digit number, and the last count
#   Output: A new integer, moving the first of the digits you want to
#           rotate to the end and shift the remaining digits to the left
#   Explicit:
#       Returning a new integer
#       Accepting two arguments, long number, single digit
#       Count the long number backwards by the amount the single digit specifies
#       When reaching the count, move that digit to the end
#   Implicit:
#       Idk if arguments can be empty
# E:
    # print(rotate_rightmost_digits(735291, 2) == 735219)  # True
    # print(rotate_rightmost_digits(735291, 3) == 735912)  # True
    # print(rotate_rightmost_digits(735291, 1) == 735291)  # True
    # print(rotate_rightmost_digits(735291, 4) == 732915)  # True
    # print(rotate_rightmost_digits(735291, 5) == 752913)  # True
    # print(rotate_rightmost_digits(735291, 6) == 352917)  # True
    # print(rotate_rightmost_digits(1200, 3) == 1002)      # True

#   I don't think arguments can be empty
# D:
#   Integers can't be indexed and are immutable
#   Maybe work with strings and lists?
# A:
#   1. Turn the number into a string
#   2. Turn the numer_string into a list
#   3. Access the element of that list by the count digit
#   4. Gain and remove that digit
#   5. Add it to the end of the number string
#   6. Join the string and turn it into a number
#   7. Return it

def rotate_rightmost_digits(number, count):
    number_string = list(str(number))
    popped_digit = number_string.pop(-count)
    number_string.append(popped_digit)
    number_string = "".join(number_string)
    return int(number_string)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True