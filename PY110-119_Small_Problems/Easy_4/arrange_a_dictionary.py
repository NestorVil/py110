# P:
#   Input: A dictionary
#   Output: It's key's sorted by the values associated with each key
#   Explicit:
#       Doing some sorting
#   Implicit?:
#       Looking at the example test case, I assume they want me to return something like a list of the keys
#       Going from lowest to highest
# D:
#      Lists?
# A:
#   1. Create a new list consisting of just the keys of the dictionary
#   2. Return it

def sort_key(item):
    return item[1]

def order_by_value(d):
    sorted_items = sorted(d.items(), key=sort_key)
    return [key for key, value in sorted_items]

# Student solution
def order_by_value(dictionary):
    return sorted(list(dictionary.keys()), key=dictionary.get)