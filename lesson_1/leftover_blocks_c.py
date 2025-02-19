# C: Implementing a Solution in Code:
#   - Translating your solution algorithm into code
#       -Think about our algorithm in the context of the programming language
#           -Features and constraints of the language
#           -Characateristcs of data structures
#           -Bulit in methods or functions
#           -Syntax/ general patterns
#       -Create any test cases
#   - Code with intent


# Implementation Notes:
#- Use a `while` loop?
#     - For the condition, check whether "number of blocks
#       remaining" is greater than or equal to the "number of
#       blocks required".
# - Calculating the blocks for the next layer, use `**` operator?
#     - For example: `(current_layer + 1)**2`.

def calculate_leftover_blocks(blocks):
    remaining_blocks = blocks
    current_layer = 0
    required_blocks = (current_layer + 1)**2
    
    while remaining_blocks >= required_blocks:
        remaining_blocks -= required_blocks
        current_layer += 1
        required_blocks = (current_layer + 1)**2

    return remaining_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0)