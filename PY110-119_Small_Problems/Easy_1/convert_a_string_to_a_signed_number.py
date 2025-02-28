# P:
#   Input: A string of digits that may have a leading + or - sign
#   Output: The oppropiate number as an integer corresponding to said sign, positive if no sign
#   Explicit:
#       + Sign means positive
#       - Sign means negative
#       No sign means positive
#   Implicit:
#       Previous function may be required
# E:
    # print(string_to_signed_integer("4321") == 4321)  # True
    # print(string_to_signed_integer("-570") == -570)  # True
    # print(string_to_signed_integer("+100") == 100)   # True

#   No strings empty
# D:
#   Dictionary where each digit corresponds with value like last time
# A:
#   1. If the first digit of the string has a + or -, make the program ignore it
#   2. Procede as normal otherwise
#   3. At the end, check if the first digit has a + or -
#   4. Multiply it by negative if it's negative
#   5. Return the new value

def string_to_signed_integer(string_number):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    value = 0
    for char in string_number:
        if char.isalnum():
            value = (10 * value) + DIGITS[char]

    if string_number[0] == "-":
        value *= -1
    return value

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True