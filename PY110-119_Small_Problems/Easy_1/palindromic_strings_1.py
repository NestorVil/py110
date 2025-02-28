# P:
#   Input: A string
#   Output: A boolean value depending on if the inputt is a palindromic (reads same forwards and backwards)
#   Case matters, all characters matter
#   Can inputs be empty? 
# E:
# All of these examples should print True
    # print(is_palindrome('madam') == True)
    # print(is_palindrome('356653') == True)
    # print(is_palindrome('356635') == False)

    # # case matters
    # print(is_palindrome('Madam') == False)

    # # all characters matter
    # print(is_palindrome("madam i'm adam") == False)

#   Looks like strings will never be empty
# D:
#   A way to reverse strings and check them
#   String indexing?
# A:
#   1. Create new variable "backwards_string" and assign it backwards value of the input string
#   2. Check both variables for equality
#   3. Return True if they are equal, False otherwise

def is_palindrome(string):
    backwards_string = string[::-1]
    return string == backwards_string

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)