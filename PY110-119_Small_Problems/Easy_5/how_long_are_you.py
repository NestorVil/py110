# P:
#   Input: A string
#   Output: A list that contains every word from the string, with each word
#           followed by a space and the word's length. If the string is empty or
#           no argument is passed, the function should return an empty list
#   Explicit:
#       Return an empty list if no argument is passed or string is empty
#       List that contains every word, followed by a space and the len of the word
#       Turning a string into a list which length is dependent on how many words are in the string
#       Every pair of word in the string separated by a single space
# E:
# All of these examples should print True
    # words = 'cow sheep chicken'
    # expected_result = ['cow 3', 'sheep 5', 'chicken 7']
    # print(word_lengths(words) == expected_result)        # True

    # words = 'baseball hot dogs and apple pie'
    # expected_result = ['baseball 8', 'hot 3', 'dogs 4',
    #                    'and 3', 'apple 5', 'pie 3']
    # print(word_lengths(words) == expected_result)        # True

    # words = "It ain't easy, is it?"
    # expected_result = ['It 2', "ain't 5", 'easy, 5',
    #                    'is 2', 'it? 3']
    # print(word_lengths(words) == expected_result)        # True

    # big_word = 'Supercalifragilisticexpialidocious'
    # print(word_lengths(big_word) == [f'{big_word} 34'])  # True

    # print(word_lengths('') == [])                        # True
    # print(word_lengths() == [])                          # True
# D: 
#   Strings and lists
# A:
#   1. Split the input_string into a list with each word separated by a space. If the input is empty, just return a new list
#   2. Create a new string
#   3. Determine the length of the word at each iteration of the split string
#   4. Place the word followed by a space and the length of the word into a new list
#   5. Return it

def word_lengths(words=""):
    new_list = []
    if len(words) > 1:
        split_string = words.split()
        for word in split_string:
            word_length = len(word)
            new_list.append(f"{word} {word_length}")
    return new_list

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True

# Launch:
def word_lengths(string=''):
    if not string:
        return []

    return [f"{word} {len(word)}"
            for word in string.split()]