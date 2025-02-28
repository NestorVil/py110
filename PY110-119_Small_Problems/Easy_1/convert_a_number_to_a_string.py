# P:
#   Input: A non-negative integer value (0, 2, ect)
#   Output: A string rerpesenting that integer
#   Explicit:
#       Can't use str()
#       Always positive
#   Implcit:
#       Assuming never empty
# E:
    # print(integer_to_string(4321) == "4321")              # True
    # print(integer_to_string(0) == "0")                    # True
    # print(integer_to_string(5000) == "5000")              # True
    # print(integer_to_string(1234567890) == "1234567890")  # True

# D:
#   Divmod function can be indexed. Can use dictionary with associated values
# A:
#   1. Create a dictionary 'digits' with the key being a number and the value corresponding
#   2. 

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        print(number)
        result = DIGITS[remainder] + result

    return result or '0'

integer_to_string(4321)