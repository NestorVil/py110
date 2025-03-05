# P:
#   Input: Three separate numbers (representing the three sides of a triangle)
#   Output: A string ("equilateral" if all sides same, "isosceles" if only 2 same, "scalene" if none same)
#   Explicit:
#       Comparing the three side digits
#       The sum of the lengths of the two shortest sides must be greater than the length of the longest side
#       Every side must have a length greater than 0
# E:
    # print(triangle(3, 3, 3) == "equilateral")  # True
    # print(triangle(3, 3, 1.5) == "isosceles")  # True
    # print(triangle(3, 4, 5) == "scalene")      # True
    # print(triangle(0, 3, 3) == "invalid")      # True
    # print(triangle(3, 1, 1) == "invalid")      # True
# D:
#   Seems like I'm match casing 
# A:
#   1. If any of the sides is 0, return "invalid"
#   2. If the sum of the two shortest sides isn't more than the longest, return "invalid"
#   1. If the three sides match, return "equilateral"
#   2. If only two sides match, return "isosceles"
#   3. Else, return "scalene"

def triangle(side1, side2, side3):
    if side1 == 0 or side2 == 0 or side3 == 0:
        return "invalid"
    
    all_sides = [side1, side2, side3]
    max_side = max(all_sides)
    the_element = all_sides.index(max_side)
    max_side = all_sides.pop(the_element)

    if sum(all_sides) < max_side:
        return "invalid"

    if side1 == side2 == side3:
        return "equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"
    else:
        return "scalene"
    
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

# Otherstudent
def triangle(side1, side2, side3):
    sorted_sides = sorted([side1, side2, side3])
    valid_side_ratio = sum(sorted_sides[:2]) > sorted_sides[2]

    if (not side1 or not side2 or not side3) or not valid_side_ratio:
        return 'invalid'
    if side1 == side2 == side3:
        return 'equilateral'
    if side1 != side2 != side3:
        return 'scalene'
    else:
        return 'isosceles'