# P:
#   Input: A string
#   Output: A list of all substrings of the input string, ordered by where in the string the substring begins
# E:
    # expected_result = [
    #     "a", "ab", "abc", "abcd", "abcde",
    #     "b", "bc", "bcd", "bcde",
    #     "c", "cd", "cde",
    #     "d", "de",
    #     "e",
    # ]

    # print(substrings('abcde') == expected_result)  # True
# D:
#   Strings and lists
# A:
#   1. Create an empty string variable
#   2. Create an empty list
#   3. For each character of the input string:
#       A. Add the character to the empty string and append it to the empty list
#   4. Repeat step three, clearing the empty string, and beginning from the first character, leading to the end


def substrings(input_string):
    leading_string = ""
    new_list = []

    for idx in range(len(input_string)):
        for chara in input_string[idx:]:
            leading_string += chara
            new_list.append(leading_string)

        leading_string = ""

    return new_list

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

# Launchschool:
def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    return [
        substring
        for idx in range(len(string))
        for substring in leading_substrings(string[idx:])
    ]