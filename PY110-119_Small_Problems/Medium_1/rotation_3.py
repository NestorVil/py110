#   Input: An integer
#   Output: An integer rotated by its length amount
#   Explicit:
#       Starting at the first number, move it to the end
#       Starting at the next number, move it to the end
#       Repeat this sequence by the total length of the digit
# E:
    # print(max_rotation(735291) == 321579)          # True
    # print(max_rotation(3) == 3)                    # True
    # print(max_rotation(35) == 53)                  # True
    # print(max_rotation(8703529146) == 7321609845)  # True

    # # Note that the final sequence here is `015`. The leading
    # # zero gets dropped, though, since we're working with
    # # an integer.
    # print(max_rotation(105) == 15)                 # True

# D: Integers are immutable, need something else
# A:
#   1. Determine how long the number is
#   2. Starting at the length of the number, begin rotating
#   3. Keep going until we reach the end

def rotate_rightmost_digits(number, count):
    number_string = list(str(number))
    popped_digit = number_string.pop(-count)
    number_string.append(popped_digit)
    number_string = "".join(number_string)
    #print(number_string)
    return int(number_string)

def max_rotation(number):
    length = len(str(number))
    for rotation in range(length, 0, -1):
        number = rotate_rightmost_digits(number, rotation)
    
    return number

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True