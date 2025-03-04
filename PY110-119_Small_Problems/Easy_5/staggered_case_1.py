# P:
#   Input: A string 
#   Output: That string with a staggered capitalization scheme. Every other character, starting from the first
#           should be capitalized and should be followed by a lowercase or non-alphabetic character.
#           Non-alphabetic characters should not be changed, but should be counted as characters for determining
#           when to switch between upper and lower case
#   Explicit:
#       Capitalize first chara
#       Lowercase next chara
#       Keep alternating between this
#       Non-characters like spaces should be counted in the cycle
# E:
    # string = 'I Love Launch School!'
    # result = "I LoVe lAuNcH ScHoOl!"
    # print(staggered_case(string) == result)  # True

    # string = 'ALL_CAPS'
    # result = "AlL_CaPs"
    # print(staggered_case(string) == result)  # True

    # string = 'ignore 77 the 4444 numbers'
    # result = "IgNoRe 77 ThE 4444 nUmBeRs"
    # print(staggered_case(string) == result)  # True

    # print(staggered_case('') == "")          # True

# D:
#   Strings, they aren't mutable so need to do something

# A:
#   1. Create a new empty string
#   2. Iterate over the original string
#   3. Beginning at the first character, capitalize it and add the result to the empty string
#   4. Beginning at the next character, lowercase it and add it the empty string
#   5. If the next character is a space or is a character , uppercase it and add it
#   6. If the next character is a space or is a character, lowercase it and add it
#   7. Keep repeating 5-6 until reach end
#   8. Return the new empty string

def staggered_case(string):
    result = ''
    for idx, char in enumerate(string):
        func = char.upper if idx % 2 == 0 else char.lower
        result += func()

    return result

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

# Student
def staggered_case(s):
    return ''.join([
        char.upper() if idx % 2 == 0 else char.lower()
        for idx, char in enumerate(s)
    ])