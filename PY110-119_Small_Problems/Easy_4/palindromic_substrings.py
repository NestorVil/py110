# P:
#   Input: A string
#   Output: A list of all palindromic substrings of the input string
#   Explicit:
#       A palindromic is a word that reads the same forward and backwards
#       The substrings in the returned list should be sorted by their order of appearance
#       Duplicate substrings should be included multiple times
#       Expected to use my previous function
#       Case sensitivity matters
#   Implicit:
#       Always returning a new list
# E:
    # print(palindromes('abcd') == [])                  # True
    # print(palindromes('madam') == ['madam', 'ada'])   # True

    # print(palindromes('hello-madam-did-madam-goodbye') ==
    #                   [
    #                       'll', '-madam-', '-madam-did-madam-',
    #                       'madam', 'madam-did-madam', 'ada',
    #                       'adam-did-mada', 'dam-did-mad',
    #                       'am-did-ma', 'm-did-m', '-did-',
    #                       'did', '-madam-', 'madam', 'ada', 'oo',
    #                   ])    # True

    # print(palindromes('knitting cassettes') ==
    #                   [
    #                       'nittin', 'itti', 'tt', 'ss',
    #                       'settes', 'ette', 'tt',
    #                   ])    # True
# D:
#   Strings, lists, some way to reverse strings
# A:
#   1. Use the previous function to get a list of all torn up substrings in the input string
#   2. For each element in the returned list, check if it's a palindromic
#   3. If it is, and greater than 1 character append it to a new list
#   4. Return the new list


def palindromes(input_string):
    return [substring for substring in substrings(input_string) if substring == substring[::-1] and len(substring) > 1]

def substrings(input_string):
    leading_string = ""
    new_list = []

    for idx in range(len(input_string)):
        for chara in input_string[idx:]:
            leading_string += chara
            new_list.append(leading_string)

        leading_string = ""

    return new_list

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True