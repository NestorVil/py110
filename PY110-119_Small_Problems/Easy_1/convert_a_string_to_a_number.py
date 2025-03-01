# P:
#   Input: A string of digits
#   Output: The appropiate number as an integer
#   Explicit:
#       Can't use int()
#       All characters are numeric
# E:
# D:
# A:
#   1. Split the string into a list of individual numbers
#   2. Iterate through that list
#   3. Each time we iterate, return the associated integer of the number
#   4. Join the new list and return it


def check(number):
    match number:
        case "0":
            return 0
        case "1":
            return 1
        case "2":
            return 2
        case "3":
            return 3
        case "4":
            return 4
        case "5":
            return 5
        case "6":
            return 6
        case "7":
            return 7
        case "8":
            return 8
        case "9":
            return 9


def string_to_integer(string_number):
    split_string_number = list(string_number)
    real_integers = []

    for number in split_string_number:
        new_number = check(number)
        real_integers.append(new_number)

    print(real_integers)
    return " ".join(real_integers)

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

# NVM can't join non strings lol

def string_to_integer(string_number):
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
        value = (10 * value) + DIGITS[char]

    return value