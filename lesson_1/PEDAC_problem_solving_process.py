# The PEDAC Process
# P: Understand the Problem
# E: Examples and Test Cases
# D: Data Structures
# A: Algorithms
# C: Implementing a Solution in Code

# P: Understanding the Problem
#  -Establish rules and define the boundaries of the problem
#  -Restate the problem in your own words
#  -Identify problem requirements:
#       -Explicit
#       -Implicit
#  -Identify inputs and outputs
#  -Ask questions/identify unclear information
#  -Spend enough time here. Don't rush

# Example: 
#   "Given a string, produce a new string with every other word removed"
#   Explicit requirements:
#       -Input: String
#       -Output: new string
#       -Remove every other word from input string

#   -Questions:
#       -What do we mean by "every other word?"
#       -What is a word in this context?
#       -Should we delete all the odd words, or all of the even words?

# E: Examples and Test Cases
#   -Can be used to confirm or refute assumptions
#   -Answer questions and provide implicit requirements
#   -Test cases are written in code and can be run to test your solution
#   -Codify the rules and boundaries of the problem

# D: Data Structures:
#   -Thinking in terms of data structures is an important partt of the problem solving process
#   -Helps reason with data logically
#   -Helps interact with data at the implementation stage
#   -Data structures are closely linked to the algorithm used for your solution

# A: Algorithms:
#   -A logical sequence of steps for accomplishing a task or objective
#   -Closely related to data structures
#   -At first, keep your algorithm abstract and high level
#   -Once have an algorithm that makes sense, can go back to fill in some of the details
#   -Can and should revisit algorithm during implementation step to update it or make implementation notes as you work through some of the steps
#   -(Break down steps and fill in details as needed ^^)
#   Don't worry about efficiency at this stage

# C: Implementing a Solution in Code:
#   - Translating your solution algorithm into code
#       -Think about our algorithm in the context of the programming language
#           -Features and constraints of the language
#           -Characateristcs of data structures
#           -Bulit in methods or functions
#           -Syntax/ general patterns
#       -Create any test cases
#   - Code with intent

# Example:
# Imagine a sequence of consecutive even integers beginning with two. The integers are grouped in rows,
# with the first row containing one integer, the second row two integers, the third row three
# integers, and so on. Given an integer representing the number of a particular row, return an
# integer representing the sum of all the integers in that row
# P: 
#   Input: Integer representing the number of a particular row
#   Output: Integer representing the sum of all integers in that row

#   -Explicit:
#       -Sequence of integers
#       -Sequence begins with 2
#       -Integers are consecutive
#       -Integers are even
#       -Sequence is grouped into rows
#       -Each row is incrementally larger than the last: 1, 2, 3, ...
#   -Implicit:
#       -Row 1 has 1 element, row 2 has 2 elements, ect
#   -Sequence:
#       -2
#       -4, 6
#       -8, 10, 12
#       -14, 16, 18, 20
# E:
#   (Imagine these were provided)
#   Row number: 1 -> Sum of integers in row: 2
#   Row number: 2 -> Sum of integers in row: 10
#   Row number: 4 -> Sum of integers in row: 68
#   (These examples confirm our sequence assumptions while not adding anything not assumed)

# D:
#   (The way we already explored problem already suggests a particular strucutre we can use here)
#   (Can start by making notes of our understanding of the structure)
#   -Sequence of rows
#   -Order of rows is important
#   -Rows contain integers
#   -Order of integers is important
#   (With all of this, a nested list seems like it'd work)
#   [
#       [2],
#       [4, 6],
#       [8, 10, 12],
#       [14, 16, 18, 20],
#       ...
#   ]
#   (Looking at this structure, because rows ordered, given the number of a particular row,
#   can access the index for that row and sum  its elements)(ex: input 4 then reference 4th row in list then sum its elements)

# A:
#   -1. Create an empty 'rows' list to hold all of our rows
#   -2. Create a 'row list and add it to the overall 'rows' list
#   -3. Repeat step 2 until all the necessary rows have been created
#       - A. All the rows have been created when the length of the 'rows' list is equal to the input
#   -4. Sum the final row
#   -5. Return the sum
#   (Since this is abstract, some steps like 2 may need further detail. Sometimes may be helpful
#    to use the PEDAC process for an individual step)
# Step 2 PEDAC:
#   Rules:
#       -Row is a list
#       -List contains integers
#       -Integers are consecutive even numbers
#       -Integers in each row form part of a larger overall sequence
#       -Rows are of different lengths
#       -Input:
#           -Length of the row
#           -The starting integer
#       -Output: The row itself ---> [8, 10, 12]
#   Examples:
#       -start: 2, length: 1 --> [2]
#       -start: 4, length: 2 --> [4, 6]
#       -start: 8, length: 3 --> [8, 10, 12]
#   Data Structure: List
#   Algorithm:
#       -1. Create an empty 'row' list to contain the integers
#       -2. Add the starting integer
#       -3. Increment the starting integer by 2 to get the next integer in the sequence
#       -4. Rpeat steps 2 & 3 until the list has reached the correct length
#       -5. Return the 'row list



# Calculating the start integer:
# Rule: First integer of row == last integer of preceding row + 2
# Algorithm:
#   -Get the last row of the rows list
#   -Get the last integer from that row
#   -add 2 to that integer


# C:
def sum_even_number_row(row_number):
    rows = []
    start_integer = 2
    for row_length in range(1, row_number + 1):
        row = create_row(start_integer, row_length)
        rows.append(row)
        start_integer = row[-1] + 2
    return sum(rows[-1])

def create_row(start_integer, row_length):
    row = []
    current_integer = start_integer
    while len(row) < row_length:
        row.append(current_integer)
        current_integer += 2
    return row


print(sum_even_number_row(1) == 2)
print(sum_even_number_row(2) == 10)
print(sum_even_number_row(4) == 68)

# print(create_row(2, 1) == [2])
# print(create_row(4, 2) == [4, 6])
# print(create_row(8, 3) == [8, 10, 12])

# Final Thoughts:
#   -Not a completely linear process
#   -Be prepared to move back and forth between steps
#   -Refer back to your notes
#   -Switch from implementation mode back to abstract problem solving mode when necessary
#   -Don't try to problem solve at the code level
#   -My approach will likely evolve over time