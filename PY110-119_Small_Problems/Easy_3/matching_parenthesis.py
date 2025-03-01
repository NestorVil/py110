# P:
#   Input: A string
#   Output a boolean value depending if all paranthesis in the string are properly balanced
#   Explicit:
#   All '(' ')' pairs must have t he same count
# E:
    # print(is_balanced("What (is) this?") == True)        # True
    # print(is_balanced("What is) this?") == False)        # True
    # print(is_balanced("What (is this?") == False)        # True
    # print(is_balanced("((What) (is this))?") == True)    # True
    # print(is_balanced("((What)) (is this))?") == False)  # True
    # print(is_balanced("Hey!") == True)                   # True
    # print(is_balanced(")Hey!(") == False)                # True
    # print(is_balanced("What ((is))) up(") == False)      # True
# D:
#   Strings and boolean values. Need some way to keep count of everything
# A:
#   1. Count "("
#   2. Count ")"
#   3. Return the amount of both

def is_balanced(s):
    parens = 0
    for char in s:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        if parens < 0:
            return False
    return parens == 0


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True