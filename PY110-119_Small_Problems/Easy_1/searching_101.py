# P:
#   Input: asking for 6 numbers
#   Output: a message that describes if the sixth number is in the first five
# E:
    # Enter the 1st number: 25
    # Enter the 2nd number: 15
    # Enter the 3rd number: 20
    # Enter the 4th number: 17
    # Enter the 5th number: 23
    # Enter the last number: 17

    # 17 is in 25,15,20,17,23.
#   Each time the program asks for an input it keeps track of it (2nd...3rd)
#   Last line suggests all the numbers need to be joined by a comma but no space
# D:
#   A list to contain the first five numbers and a way to join them
# A:
#   1. Ask the user for five inputs
#   2, For each input, add each to a list
#   3. Join that list separated by a comma
#   4. Ask user for a sixth input
#   5. Check if that sixth input is in the list of the first five

num_list = []

num1 = input("Please enter the 1st number: ")
num_list.append(num1)
num2 = input("Please enter the 2nd number: ")
num_list.append(num2)
num3 = input("Please enter the 3rd number: ")
num_list.append(num3)
num4 = input("Please enter the 4th number: ")
num_list.append(num4)
num5 = input("Please enter the 5th number: ")
num_list.append(num5)

num_list = ",".join(num_list)

num6 = input("Please ender the last number: ")

if num6 in num_list:
    print(f"{num6} is in {num_list}.")
else:
    print(f"{num6} isn't in {num_list}.")


# I can combine like this: num_list.append(input("Enter the 1st number: "))
# I like this solution:

checklist = []
input_num = ['1st', '2nd', '3rd', '4th', '5th', 'last']

for i in input_num:
    checklist.append(input(f"enter the {i} number: "))

if checklist[5] in checklist[:5]:
    print(f'{checklist[5]} is in {','.join(checklist[:5])}')
else:
    print(f'{checklist[5]} is not in {','.join(checklist[:5])}')