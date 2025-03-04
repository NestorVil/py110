# P:
#   Input: A dictionary where both keys and values are unique
#   Output: A dictionary where its keys and values are inverted
#   Question:
#       Idk if I'm mutating the dictionary or returning a new one
#   Explicit:
#       Switching keys and values
# E:
    # print(invert_dict({
    #           'apple': 'fruit',
    #           'broccoli': 'vegetable',
    #           'salmon': 'fish',
    #       }) == {
    #           'fruit': 'apple',
    #           'vegetable': 'broccoli',
    #           'fish': 'salmon',
    #       })  # True

#   I think I'm mutating
# D:
#   Working with dictionaries
# A:
#   1. Go over the dictionary
#   2. For each key I iterate over, switch it with the value in the new dictionary
#   3. Return it

def invert_dict(input_dictionary):
    inverted_dict = dict()
    for key, value in input_dictionary.items():
        inverted_dict.setdefault(value, key)
    
    return inverted_dict

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

# Launchschool:
def invert_dict(my_dict):
    return {value: key for key, value in my_dict.items()}