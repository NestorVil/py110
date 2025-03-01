# P:
#   Input: A list of positive integers
#   Output: A string that multiplies all of the integers in the input together, divides the result by the number of entries
#           in the list, and rounded to three decimal places.
#   Explicit:
#       Multiple all elements in a list, 
#       divide that number by the amount of elements in the list, 
#       round it to 3. 
#       Turn it string
# E:# All of these examples should print True
    # print(multiplicative_average([3, 5]) == "7.500")
    # print(multiplicative_average([2, 5, 8]) == "26.667")
    # print(multiplicative_average([2, 5]) == "5.000")
    # print(multiplicative_average([1, 1, 1, 1]) == "0.250")
    # print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

#   In these test cases lists will always have at least 2 elements
# A:
#   1. Count the amount of elements in a list and assign it to variable "amount_of_elements"
#   2. Multiply the amount of numbers in a list and assign it to variable "sum_of_elements"
#   3. Divide "sum_of_elements" by "amount_of_elements" and round it to 3 decimal places
#   4. Turn that number into a string and return it

def multiplicative_average(list1):
    amount_of_elements = len(list1)
    multiple_of_elements = 1
    for num in list1:
        multiple_of_elements *= num
    the_number = multiple_of_elements / amount_of_elements
    return(f"{the_number:.3f}")

# All of these examples should print True
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

# I looked up how to multiply everything in a list and got somethin from the math module
# But idk if they'll yell at me for that since it might be considered method hunting

from math import prod
def multiplicative_average(numbers: list) -> str:
    return f"{prod(numbers) / len(numbers):.3f}"