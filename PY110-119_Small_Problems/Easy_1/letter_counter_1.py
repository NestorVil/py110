# P:
#   Input: A string consisting of zero or more space-separated words
#   Output: A dictionary that shows the number of words of different sizes
#   Explicit:
#       Words consist of any sequence of non-space characters
#   Implicit:
#       I assume stuff like periods count as a length of a word
# E:
# All of these examples should print True
    # string = 'Four score and seven.'
    # print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

    # string = 'Hey diddle diddle, the cat and the fiddle!'
    # print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

    # string = 'Humpty Dumpty sat on a wall'
    # print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

    # string = "What's up doc?"
    # print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

    # print(word_sizes('') == {})

#   Strings can be empty and should still return an empty list
#   Stuff like punctation count as part of the word
# D:
#   Working with dictionaries
# A:
#   1. Create an empty ditionary "word_count"
#   2. Split the string into a list separate by an empty space
#   3. For the length of each element in the new list, count how long the element is
#   4. Add the length of the word to the dictionary

def word_sizes(string):
    word_count = {}

    for word in string.split():
        length = len(word)
        word_count[length] = word_count.get(length, 0) + 1

    return word_count

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})