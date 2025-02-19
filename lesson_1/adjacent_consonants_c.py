# C: Implementing a Solution in Code:
#   - Translating your solution algorithm into code
#       -Think about our algorithm in the context of the programming language
#           -Features and constraints of the language
#           -Characateristcs of data structures
#           -Bulit in methods or functions
#           -Syntax/ general patterns
#       -Create any test cases
#   - Code with intent

# Implementation Notes for counting constants:
# - Use `string.split` combined with `string.join` to remove the
#   spaces from the input string.
# - Perhaps use a `for` loop to iterate through the string?
# - Use the `in` keyword to check whether a string of consonants
#   includes the letter for that iteration.

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings

def count_max_adjacent_consonants(string):
    string = ''.join(string.split(' '))
    max_consonant_count = 0
    adjacent_consonants = ''

    for letter in string:
        if letter in 'bcdfghjklmnpqrstvwxyz':
            adjacent_consonants += letter
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)
        else:
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)

            adjacent_consonants = ''

    return max_consonant_count

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# Expected: ['dddaa', 'ccaa', 'aa', 'baa']
# Actual:   ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# Expected: ['salt pan', 'can can', 'batman', 'toucan']
# Actual:   ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# Expected: ['bar', 'car', 'far', 'jar']
# Actual:   ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# Expected: ['month', 'day', 'week', 'year']
# Actual:   ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# Expected: ['xxxx', 'xxxb', 'xxxa']
# Actual:   ['xxxx', 'xxxb', 'xxxa']