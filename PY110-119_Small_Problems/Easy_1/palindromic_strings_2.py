# P:
#   Input: a string
#   Output: A boolean value depending if the string is a palindromic (reads same forwards and backwards)
#   Explicit Requirements:
#       Case does not matter
#       Should ignore all non-alphanumeric characters
#   Implicit:
#       It seems the function I wrote last time would be helpful for this
#   Questions:
#       I assume there aren't any empty strings again
# E:
    # print(is_real_palindrome('madam') == True)           # True
    # print(is_real_palindrome('356653') == True)          # True
    # print(is_real_palindrome('356635') == False)         # True
    # print(is_real_palindrome('356a653') == True)         # True
    # print(is_real_palindrome('123ab321') == False)       # True

    # # case doesn't matter
    # print(is_real_palindrome('Madam') == True)           # True

    # # only alphanumerics matter
    # print(is_real_palindrome("Madam, I'm Adam") == True) # True

#   Ye
# D:
#   Working with strings which are immutable
#   I assume I'll need to create new strings that are the inputted strings but without alphanumeric
# A:
#   1. Create a new empty string "stripped_string"
#   2. For each character in the old string check if it's an alphanumeric character 
#   3. If it is, make the character lowercase add it to stripped string with
#   4. Check if this new stripped string is a palindromic
#   5. If it is, then check if they are without caring for case

def is_real_palindrome(string):
    stripped_string = ""
    for chara in string:
        if chara.isalnum():
            stripped_string += chara.casefold()
    return is_palindrome(stripped_string)




def is_palindrome(string):
    return string == string[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# I like this solution:
def is_real_palindrome(input):
    clean = ''.join((char for char in input if char.isalnum()))
    return clean.casefold() == clean[::-1].casefold()