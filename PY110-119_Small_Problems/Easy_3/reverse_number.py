# P:
#   Input: A positive integer
#   Output: It's digits reversed
# E:
    # print(reverse_number(12345) == 54321)   # True
    # print(reverse_number(12213) == 31221)   # True
    # print(reverse_number(456) == 654)       # True
    # print(reverse_number(1) == 1)           # True
    # print(reverse_number(12000) == 21)      # True
# D:
#   Can use strings and lists again
# A:
#   1. Turn the input integer into a string
#   2. Turn that string into a list
#   3. Reverse the list
#   4. Join the list
#   5. Return it

def reverse_number(number):
    new_list = list(str(number))
    new_list.reverse()
    new_string = "".join(new_list)
    return int(new_string)

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True