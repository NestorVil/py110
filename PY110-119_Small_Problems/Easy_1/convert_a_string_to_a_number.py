# P:
#   Input: A string of digits
#   Output: The appropiate number as an integer
#   Explicit:
#       Can't use int()
#       All characters are numeric
# E:
# D:
# A:
#   1. Initialize a "ones" variable and initialize it to 0
#   2. Initialize a "tens" variable and initialize it to 0
#   3. Initialize a  "hundreds" variable and initialize it to 0
#   4. Initialiaze a "thousands" varuable and initialize it to 0
#   5. Split the string into a list of individual numbers
#   6. Iterate through that list
#   7. Each time we iterate, return the associated integer of the number
#   8. Join the new list and return it


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