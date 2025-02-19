# P: Understanding the Problem
#  -Establish rules and define the boundaries of the problem
#  -Restate the problem in your own words
#  -Identify problem requirements:
#       -Explicit
#       -Implicit
#  -Identify inputs and outputs
#  -Ask questions/identify unclear information
#  -Spend enough time here. Don't rush

# Will be given an integer input
# The output will be an integer
# Calculate the leftover blocks after conditions have been met
# Think of each integer as a block
# Each lower layer can have more than one block in an upper layer
# Last layer must be single block
# How many upper layers can a single block support?

# Launchschool:
# Explicit Rules:
# - Structures are built with blocks:
#     - Blocks are cubes.
#     - Cubes are six-sided, have square faces, and have equal
#       lengths on all sides.
# - The top layer in the structure consists of a single block.
# - Upper layer blocks must be supported by four lower layer blocks.
# - Lower layer blocks can support more than one upper layer block.
# - Layers are solid structures -- there are no gaps between blocks.
# Implicit:
#   -How do we know whether a layer is valid?
#   -Since we know the first layer is always one block, and that a block in the upper
#       layer needs to be supported by 4 in the lower layer, then the second layer 
#       needs a least 4 blocks
#   -Since a block in a lower layer can support more than 1 block this suggests overlap
#   -Layer 1 (top row): 1 block(1x1)
#   -Layer 2 (middle row): 4 blocks (2x2)
#   -Layer 3 (bottom row): 9 blocks (3x3)
# - Layer number correlates with blocks in a layer:
# - The number of blocks in a layer is layer number * layer number.
# Questions:
# - Is a lower layer valid if it has more blocks than it needs?
# - Will there always be left-over blocks?