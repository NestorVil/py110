# P:
#   Input: A list of integers between 0 and 19
#   Output: A lost of those integers sorted based on the english word of each number
#   Explicit:
#       A sorted list
#       The sorting will correspond to the enligh word of the number
# E:
    # input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    #               10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    # expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
    #                    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

    # print(alphabetic_number_sort(input_list) == expected_result)
    # # Prints True
# D:
#   Could use a really long dictionary or something to keep track of a number and number(english)
#   Could also use a match case statement
# A:
#   1. For each number, make a corresponding named number associated with it
#   2. Sort the inputt list by what I did in step 1

def matching(num):
    match num:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"
        case 6:
            return "six"
        case 7:
            return "seven"
        case 8:
            return "eight"
        case 9:
            return "nine"
        case 10:
            return "ten"
        case 11:
            return "eleven"
        case 12:
            return "twelve"
        case 13:
            return "thirteen"
        case 14:
            return "fourteen"
        case 15:
            return "fifteen"
        case 16:
            return "sixteen"
        case 17:
            return "seventeen"
        case 18:
            return "eighteen"
        case 19:
            return "ninteen"
        
def alphabetic_number_sort(list1):
    return sorted(list1, key=matching)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

# Launchschool
NUMBER_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                'twelve', 'thirteen', 'fourteen', 'fifteen',
                'sixteen', 'seventeen', 'eighteen', 'nineteen']

def word_for_number(num):
    return NUMBER_WORDS[num]

def alphabetic_number_sort(numbers):
    return sorted(numbers, key=word_for_number)