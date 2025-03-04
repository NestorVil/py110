# P:
#   Input: A positive integer
#   Output: The sum of its digits
#   Explicit:
#       Adding each single digit in the whole digit together
# E:
    # print(sum_digits(23) == 5)              # True
    # print(sum_digits(496) == 19)            # True
    # print(sum_digits(123456789) == 45)      # True
# D:
#   Indexing and addition. Integers can't be indexed so need to do something about that
# A:
#   1. Convert the integer into a string
#   2. Iterate over the string
#   3. Split the string into individual characters while turning each back into an integer
#   4. Return the sum of everything in the new split list

def sum_digits(input_int):
    new_list = [int(number) for number in str(input_int)]
    return sum(new_list)
#   or sum([int(number) for number in str(input_int)])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True