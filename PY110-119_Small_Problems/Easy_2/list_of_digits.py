# P:
#   Input: A positive integer
#   Output: A list of digits in the number
#   Explicit:
#       Will need to tear up a positive integer and populate each of its numbers into a list
# E:
    # print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
    # print(digit_list(7) == [7])                       # True
    # print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
    # print(digit_list(444) == [4, 4, 4])               # True
# D:
#   Digits into lists
# A:
#   1. Since can't iterate over integers, turn the input integer into a string
#   2. Iterate over that string
#   3. For each iteration turn the number into an integer and put it in a list

def digit_list(the_number):
    stringed = str(the_number)
    return [int(num) for num in stringed]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

# Could've shreded a line
def digit_list(number):
    return [int(digit) for digit in str(number)]