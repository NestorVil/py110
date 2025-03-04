# P:
#   Input: A dictionary and a list of keys
#   Output: A new dictionary that only contains the key/value pairs for the specific keys
#   Explicit:
#       Matching the list of keys to the dictionary. Returning a new dictionary
# E:
    # input_dict = {
    #     'red': 1,
    #     'green': 2,
    #     'blue': 3,
    #     'yellow': 4,
    # }

    # keys = ['red', 'blue']
    # expected_dict = {'red': 1, 'blue': 3}
    # print(keep_keys(input_dict, keys) == expected_dict) # True
# D:
#   Working with dictionaries and lists
# A:
#   1. Using the input_list, search if it exists among the keys in the input_dict
#   2. If itt does exist, add it to the new dictionary
#   3. Return that new dictionary


def keep_keys(input_dictionary, input_keys):
    # new_dict = dict()
    # for key, value in input_dictionary.items():
    #     if key in input_keys:
    #         new_dict.setdefault(key, value)

    # return new_dict
    return {key: value for key, value in input_dictionary.items() if key in input_keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

# Launchschool
def keep_keys(my_dict, key_list):
    return {key: my_dict[key]
            for key in key_list
            if key in my_dict}