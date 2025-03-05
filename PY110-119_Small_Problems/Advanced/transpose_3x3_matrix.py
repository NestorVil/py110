# P:
#   Input: A nested list representing a matrix (3 lists, 3 elements each)
#   Output: A new newsted list representing the original input transposed (rows and columes exchanged)
#   Explicit:
#       Can't mutate original input list
#       Get the corresponding element of each list into it's own unique list
#       Combine each unique list into a new giga list
# E:
    # matrix = [
    #     [1, 5, 8],
    #     [4, 7, 2],
    #     [3, 9, 6],
    # ]

    # new_matrix = transpose(matrix)

    # print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
    # print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
# D:
#   Working with nested lists
# A:
#   1. Segment each list of the original matrix 
#   2. Combine those lists again, but in accordance to their corresponding elements
#   3. Place each new list into a new nested list
#   4. Return it

def transpose(matrix):
    one, two, three = matrix
    return [list(row) for row in zip(one, two, three)]

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True