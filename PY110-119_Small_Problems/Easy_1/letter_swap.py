# P:
#   Input: A string of words separated by spaces
#   Output: A string that swaps the first and last letter of every word
#   Explicit:
#       Every word contains at least one letter
#       The string will contain at least one word
#       Each string contains nothing but words and spaces
# E:
    # print(swap('Oh what a wonderful day it is')
    #       == "hO thaw a londerfuw yad ti si")  # True
    # print(swap('Abcde') == "ebcdA")            # True
    # print(swap('a') == "a")                    # True
#   Ye
# D:
#   Strings. They're immutable
# A:
#   1. Create a new list "list_of_words" and populate it with each word of the given string
#   2. For each element in "list_of_words" swap the case of the first and last letter
#   3. Join the "list_of_words" into a new variable string "new_string" and return it

def swap(given_string):
    list_of_words = given_string.split()
    for idx, word in enumerate(list_of_words):
        if len(word) == 1:
            new_word = word
        else:
            new_word = word[-1] + word[1:-1] + word[0]

        list_of_words[idx] = new_word

    return " ".join(list_of_words)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True