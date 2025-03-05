# P:
#   Input: Three integers representing the three angles of a triangle in degrees
#   Output: A string depending on a condition
#   Explicit:
#       The three digits need to add up to 180 degrees to be valid
#       Each digit needs to be greater than 0 to be valid
#       Return "Right" if one angle exactly 90
#       Return "Acute" if all three angles less than 90 individually
#       Return "Obtuse" if one angle is greater than 90
# E:
    # print(triangle(60, 70, 50) == "acute")      # True
    # print(triangle(30, 90, 60) == "right")      # True
    # print(triangle(120, 50, 10) == "obtuse")    # True
    # print(triangle(0, 90, 90) == "invalid")     # True
    # print(triangle(50, 50, 50) == "invalid")    # True
# D:
#   Digits and strings and a list
# A:
#   1. If one of the digits is 0, it's invalid
#   2. If the sum of all the digits isn't 180, it's invalid
#   3. Going over the list of digits
#   4. If one is 90, return right
#   5. If none are greater than 90, return acute
#   6. If one angle is greater than 90, return obtuse

def triangle(side1, side2, side3):
    angles = [side1, side2, side3]

    if 0 in angles or (sum(angles) != 180):
        return "invalid"
    
    if 90 in angles:
        return "right"
    
    if side1 < 90 and side2 < 90 and side3 < 90:
        return "acute"
    
    if side1 > 90 or side2 > 90 or side3 > 90:
       return "obtuse"
    
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

# I like this other students
def triangle(*angles):
    if 0 in angles or sum(angles) != 180:
        return 'invalid'
    elif all(angle < 90 for angle in angles):
        return 'acute'
    elif any(angle == 90 for angle in angles):
        return 'right'
    else:
        return 'obtuse'