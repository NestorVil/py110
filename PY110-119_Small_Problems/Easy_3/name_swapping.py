# P:
#   Input: A string consisting of a first name, a space, and a last name
#   Output: A new string consisting of the last name, a comma, a space, and the first name
# E:
    # print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
# D:
# Strings, lists
# A:
#   1. Split string into two names
#   2. Reverse the new list
#   3. Join the list with a comma space
#   4. Return it

def swap_name(full_name):
    name_as_list = full_name.split()
    name_as_list.reverse()
    return ", ".join(name_as_list)

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name("Joe Roberts"))