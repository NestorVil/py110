# D: Data Structures:
#   -Thinking in terms of data structures is an important partt of the problem solving process
#   -Helps reason with data logically
#   -Helps interact with data at the implementation stage
#   -Data structures are closely linked to the algorithm used for your solution


# 1x1
14 # 3 layers 
1  # 1x1
4  # 2x2
9  # 3x3
# Seems like a nested sequence of some kind would work here
# It's a sequence of rows
# [ [1] x 1,
#   [1, 1] x 2,
#   [1, 1, 1] x 3
# ]

# LaunchSchool:
# """
# - Perhaps we can use a nested list to represent the structure?
#     - Each sublist could represent a layer.
# """

# [
#     ['x'],
#     ['x', 'x', 'x', 'x'],
#     ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#       ...
# ]

# Launch school suggests to not be constrained into thinking PEDAC as a linear process and that
# it's okay to move backward and forward between steps.