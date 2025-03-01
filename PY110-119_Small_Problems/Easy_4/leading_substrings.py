# P:
#   Input: Two string arguments
#   Output: A list of substrings of that string. Each substring should begin with the first letter
#           of that word, and the list should be ordered from shortest to longest
#   Explicit:
#       Returning a list
#       Splitting the input string apart
#       Length of list depending on list of substring
# E:
# All of these examples should print True
    # print(leading_substrings('abc') == ['a', 'ab', 'abc'])
    # print(leading_substrings('a') == ['a'])
    # print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

#   Will always have at least one character long string
# D:
#   Working with lists and strings
# A:
#   1. Create an empty string
#   2. Create an empty list
#   3. Iterate over the input string
#   4. For each iteration, add it to the empty string, then append it to the empty list
#   5. Return the list

def leading_substrings(input_string):
    leading_string = ""
    new_list = []
    for chara in input_string:
        leading_string += chara
        new_list.append(leading_string)
    
    return new_list

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])