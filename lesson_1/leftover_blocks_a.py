# A: Algorithms:
#   -A logical sequence of steps for accomplishing a task or objective
#   -Closely related to data structures
#   -At first, keep your algorithm abstract and high level
#   -Once have an algorithm that makes sense, can go back to fill in some of the details
#   -Can and should revisit algorithm during implementation step to update it or make implementation
#        notes as you work through some of the steps
#   -(Break down steps and fill in details as needed ^^)
#   Don't worry about efficiency at this stage

# Will be given an integer like 6 (which returns 1 leftover block), or 14 (returns 0)
# Will need to segment that number to fit the criteria
# Calculate the leftover blocks after conditions have been met

# 1. Create an empty 'rows' list to hold all the empty rows
# 2. If the given integer is greater than 0, populate the first row with one of its elements
# 3. Take away an amount from the integer for each row that gets populated
# 4. Check if theres enough in the integer to populate the next row (2x2...3x3...4x4...)
# 5. Populate that row by taking away from the integer
# 6. If step 5 isn't possible, return the remaining integer

# Launchschool:
# 1. Start with:
#      - The "number of blocks remaining" is equal to the input.
#      - The "current layer number" is layer 0.

# 2. Calculate the "current layer number" for the next layer by
#    adding 1 to the "current layer number".

# 3. Using the new "current layer number", calculate the "number of
#    blocks required in this layer" by multiplying the "current
#    layer number" by itself.

# 4. Determine whether the "number of blocks remaining" is greater
#    than or equal to the "number of blocks required in this layer".
#      - If there are enough blocks:
#          - Subtract the "number of blocks required in this layer"
#            from the "number of blocks remaining".
#          - Go to step 2.
#      - If there aren't enough blocks:
#          - Return the "number of blocks remaining".