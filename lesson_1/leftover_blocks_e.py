# E: Examples and Test Cases
#   -Can be used to confirm or refute assumptions
#   -Answer questions and provide implicit requirements
#   -Test cases are written in code and can be run to test your solution
#   -Codify the rules and boundaries of the problem

# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True

14 # 3 layers 
1  # 1x1
4  # 2x2
9  # 3x3
# 1 + 4 + 9 = 14

# These test cases seem to confirm the model we have
# 14 = 3 layers, each layer is squared until it can't be stacked anymore

# Launchschool:
# Unanswered question: Is a lower layer valid if it has more blocks than it needs?
#   No, look at second to last test case
# Unanswered question: Will there always be left-over blocks?
#   No