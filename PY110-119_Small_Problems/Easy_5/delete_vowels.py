# P:
#   Input: A list of strings
#   Output: A list of the same string values, but with all vowels (a,e,i,o,u) removed
#   Explicit:
#       Remove vowels from a string
#       Returning a new list
#       In the place of each index, place a string with the vowels removed
# E:
# All of these examples should print True
    # original = ['abcdefghijklmnopqrstuvwxyz']
    # expected = ['bcdfghjklmnpqrstvwxyz']
    # print(remove_vowels(original) == expected)        # True

    # original = ['green', 'YELLOW', 'black', 'white']
    # expected = ['grn', 'YLLW', 'blck', 'wht']
    # print(remove_vowels(original) == expected)        # True

    # original = ['ABC', 'AEIOU', 'XYZ']
    # expected = ['BC', '', 'XYZ']
    # print(remove_vowels(original) == expected)        # True

# D:
#   Strings and lists
# A:
#   1. Create a new empty string
#   2. Create a new empty list
#   3. Iterate over the input list
#   4. At each index of the input list
#       A. Full the empty string with the non-vowel characters of the index string
#       B. Append the new empty string to the current index
#       C. Reset the empty string
#   5. Return the new empty list

def remove_vowels(og_list):
    VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    empty_str = ""
    new_list = []

    for string in og_list:
        for chara in string:
            if chara not in VOWELS:
                empty_str += chara
        new_list.append(empty_str)
        empty_str = ""

    return new_list

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True



# Launchschool
def strip_vowels(string):
    VOWELS = "aeiouAEIOU"
    no_vowels = [char for char in string
                 if char not in VOWELS]
    return ''.join(no_vowels)

def remove_vowels(string_list):
    return [strip_vowels(string) for string in string_list]