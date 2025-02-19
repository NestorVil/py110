# E: Examples and Test Cases
#   -Can be used to confirm or refute assumptions
#   -Answer questions and provide implicit requirements
#   -Test cases are written in code and can be run to test your solution
#   -Codify the rules and boundaries of the problem

def sort_by_consonant_count(lst):
    pass


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

# Seems lists/strings will never be empty according to test cases. Should ask interviewer this question.
# Strings can contain single and multiple words
# Some strings can have no adjacent consonants
# Descending order (highest to lowest)

# Launchschool:
# - Do strings always contain multiple words? [No]
#     - Can strings contain a single word? [Yes]
#     - Can strings be empty? [No]
# - Is it possible for a string to contain no adjacent consonants?
#   [Yes]
# - What is meant by "a space between two consonants in adjacent
#   words"? [A consonant that ends one word followed by a consonant
#   that starts a new word are adjacent.]
# - Should the strings be sorted in ascending or descending order?
#   [Descending]
# - Is case important? [No]

#Implicit rules:
# - Strings may contain single or multiple words.
# - Strings may not be empty.
# - Strings may have no adjacent consonants.
# - Strings should be sorted in descending order.
# - Case is not relevant.
# - Single consonants in a string do not affect sort order in
#   comparison to strings with no consonants. Only adjacent
#   consonants affect sort order.