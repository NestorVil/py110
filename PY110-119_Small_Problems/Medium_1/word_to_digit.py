# P:
#   Input: A string
#   Output: A string with every occurance of a number word (like zero) converetd to 
#           its corresponding digit character
#   Explicit:
#       Can assume the string does not contain any punctation
#       If a word is a number, convert it to a number
# E:
    # message = 'Please call me at five five five one two three four'
    # print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
    # # Should print True
# D:
#   Strings, digits, lists?
# A:
#   1. Create a numbers list containing "one", "two", "three" ect
#   2. Create a new empty list
#   3. Go over the input_string
#   4. If the word is not a number, simply add it to the list
#   5. If the word is in the numbers list, add the corresponding number
#       A. 
#   6. Join the list and return it


# def matching(word):
#     match word:
#         case "zero":
#             return "0"
#         case "one":
#             return "1"
#         case "two":
#             return "2"
#         case "three":
#             return "3"
#         case "four":
#             return "4"
#         case "five":
#             return "5"
#         case "six":
#             return "6"
#         case "seven":
#             return "7"
#         case "eight":
#             return "8"
#         case "nine":
#             return "9"

# def word_to_digit(sentence):
#     digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
#     split_sentence = sentence.split()
#     new_list = [word 
#                 if word not in digits 
#                 else matching(word) 
#                 for word in split_sentence]

#     return " ".join(new_list)

NUM_WORDS = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}

def word_to_digit(sentence):
    words = sentence.split()
    processed_words = [NUM_WORDS.get(word, word) for word in words]
    print(processed_words)
    return ' '.join(processed_words)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True