# P: Understanding the Problem
#  -Establish rules and define the boundaries of the problem
#  -Restate the problem in your own words
#  -Identify problem requirements:
#       -Explicit
#       -Implicit
#  -Identify inputs and outputs
#  -Ask questions/identify unclear information
#  -Spend enough time here. Don't rush

# Input will be a list of strings
# Iterate over the list of strings, for each element string count the amount of adjacent consonants in each
# Sort the list by strings with the highest amount of adjacent consonants
# If two strings have the same amount of adjacent consonants, have them retain their original order to each other
# Adjacent consonants are if they are next to each other in the same word, or if a space exists between the two
# Output will be that sorted list

# Are we mutating the given list or making a new one?

# Launchschool:
# - Input: list of strings
# - Output: a list of strings sorted according to the highest number
#   of adjacent consonants

#Explicit:
# - If two strings contain the same highest number of adjacent
#   consonants, they should maintain their original relative order.
# - Adjacent consonants:
#     - are next to each other in the same string.
#     - can have a space between them in adjacent
#       words.

#Implicit:
# - Strings may contain more than one words.

#Questions:
# - Do strings always contain multiple words?
#     - Can strings contain a single word?
#     - Can strings be empty?
# - Is it possible for a string to contain no adjacent consonants?
# - What is meant by "a space between two consonants in adjacent
#   words"?
# - Should the strings be sorted in ascending or descending order?
# - Is case important?