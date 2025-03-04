# P
#   Input: A string consisting of numbers and codewords
#   Output: Printing a number that matches the order of the code inputted
#   Explicit:
#       When something is popped or multiplied ect, it's always the latest number
#       Look at the codewords
#       There's a register and a stack
#       Initialize both the register and the stack to 0 and [] respectively
# E:
    # minilang('PRINT')
    # # 0

    # minilang('5 PUSH 3 MULT PRINT')
    # # 15

    # minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
    # # 5
    # # 3
    # # 8

    # minilang('5 PUSH POP PRINT')
    # # 5

    # minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
    # # 5
    # # 10
    # # 4
    # # 7

    # minilang('3 PUSH PUSH 7 DIV MULT PRINT')
    # # 6

    # minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
    # # 12

    # minilang('-3 PUSH 5 SUB PRINT')
    # # 8

    # minilang('6 PUSH')
    # # (nothing is printed)
# D:
#   Match-case statement, lists, and numbers
# A:
#   1. Initialize stack to an empty list
#   2. Initialize register to 0
#   3. Create a match caste statement
#       A. If matces n, add to the register
#       B. If matches PUSH, push the current register value onto the stack
#       C. ect
#   4. Split the input string into a list
#   5. Starting at the first index, of the split string, make it match any of the cases

def minilang(command):
    stack = []
    register = 0
    split_command = command.split(" ")
    for step in split_command:
        match step:
            case step if step.isdigit() or step[0] == "-":
                register = int(step)
            case "PUSH":
                stack.append(register)
            case "ADD":
                popped = stack.pop()
                register += popped
            case 'SUB':
                popped = stack.pop()
                register -= popped
            case "MULT":
                popped = stack.pop()
                register *= popped
            case "DIV":
                popped = stack.pop()
                register //= popped
            case "REMAINDER":
                popped = stack.pop()
                register %= popped
            case "POP":
                popped = stack.pop()
                register = popped
            case "PRINT":
                print(register)

minilang('5 PUSH 3 MULT PRINT')
15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)
                
