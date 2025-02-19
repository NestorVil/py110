# A: Algorithms:
#   -A logical sequence of steps for accomplishing a task or objective
#   -Closely related to data structures
#   -At first, keep your algorithm abstract and high level
#   -Once have an algorithm that makes sense, can go back to fill in some of the details
#   -Can and should revisit algorithm during implementation step to update it or make implementation notes as you work through some of the steps
#   -(Break down steps and fill in details as needed ^^)
#   Don't worry about efficiency at this stage

# 1. For each string in the input list, determine the highest number
#    of adjacent consonants within that string.
# 2. Sort the input list based on the calculated highest number of
#    consonants from step 1.
# 3. Return the sorted list.


# Pedac process for step 1
# Input: a string
# Output: an integer representing a count of the highest number of
#         adjacent consonants in the string


# - Remove the spaces from the "input string".
# - Initialize a "maximum consonants count" to zero.
# - Initialize an "adjacent consonants string" to an empty string.
# - For each "letter" in the "input string":
#     - If the "letter" is a consonant:
#         - Concatenate it to the "adjacent consonants string".
#     - If the "letter" is a vowel:
#         - If the "adjacent consonants string" has a length
#           greater than the current "maximum consonants count":
#             - If the "adjacent consonants string" has a length
#               greater than 1:
#                 - Set the "maximum consonants count" to the length
#                   of the "adjacent consonants string".

#         - Reset the "adjacent consonants string" to an empty string.

# - Return the "maximum consonants count".