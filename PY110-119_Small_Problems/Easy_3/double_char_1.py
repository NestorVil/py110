# P:
#   Input: A string
#   Output: A new string that doubles every character in the string
# Can strings be empty?
# E:
    # print(repeater('Hello') == "HHeelllloo")              # True
    # print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
    # print(repeater('') == "")                             # True

# Yes
# D:
#   Just working with strings
# A:
#   1. Create a new empty string
#   2. Populate the new empty string with each character multiplied by 2
#   3. Return it

def repeater(the_string):
    new_string = ""
    for chara in the_string:
        new_string += chara * 2
    return new_string


print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

# Can use list comprehension
def repeater(string):
    return ''.join([char * 2 for char in string])