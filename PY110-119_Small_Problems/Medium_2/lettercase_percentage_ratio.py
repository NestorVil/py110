# P:
#   Input: A string
#   Output: A dictionary that contains: the percentage of characters in the string that are lowercase
#                                     # the percentage of characters that are uppercase letters
#                                       the percentage of characters that are neither
#           All three percentages should be returned as strings represented as '0.00' to '100.00' 
#                                                                            each value roudned to two decimal points
# Explicit:
#   String will always contain one character
#   Returning a dictionary
#   The dictionary should have 'uppercase': percentage, 'lowercase': percentage, 'neither': percentage'
#   # The key, values should both be strings, the values should be rounded by 2
# E:
    # expected_result = {
    #     'lowercase': "50.00",
    #     'uppercase': "10.00",
    #     'neither': "40.00",
    # }
    # print(letter_percentages('abCdef 123') == expected_result)

    # expected_result = {
    #     'lowercase': "37.50",
    #     'uppercase': "37.50",
    #     'neither': "25.00",
    # }
    # print(letter_percentages('AbCd +Ef') == expected_result)

    # expected_result = {
    #     'lowercase': "0.00",
    #     'uppercase': "0.00",
    #     'neither': "100.00",
    # }
    # print(letter_percentages('123') == expected_result)
# D:
#   Dicionaries, strings, some way to get percentages
# A:
#   1. Create an empty dictionary to match lowercase, uppercase, and neither
#   2. Find the length of the input string and save it as a number variable
#   3. Find the amount of characters in the input string are lowercase and save it as number variable
#   4. Find the amount of characters in the input string are uppercase and save it as a number variable
#   5. Count and save the rest of the characters as a number variable
#   6. Divide the length of the input string by each variable create in steps 3-5 and assign each to the dictionary, rounded
#       A. Turn each into a string
#   7. Return the dictionary

def letter_percentages(input_string):
    len_of_string = len(input_string)
    uppercase = 0
    lowercase = 0
    rest = 0
    for chara in input_string:
        if chara.isupper():
            uppercase += 1
        elif chara.islower():
            lowercase += 1
        else:
            rest += 1

    uppercase /= len_of_string
    lowercase /= len_of_string
    rest /= len_of_string

    return {"lowercase": f"{lowercase * 100:.2f}",
            "uppercase": f"{uppercase * 100:.2f}",
            "neither": f"{rest * 100:.2f}"}

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

# Launchschool:
def percentage(count, total_count):
    return f'{(count / total_count) * 100:.2f}'

def letter_percentages(string):
    total_chars = len(string)
    lowercase_count = 0
    uppercase_count = 0
    neither_count = 0

    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        else:
            neither_count += 1

    return {
        'lowercase': percentage(lowercase_count, total_chars),
        'uppercase': percentage(uppercase_count, total_chars),
        'neither':   percentage(neither_count, total_chars),
    }