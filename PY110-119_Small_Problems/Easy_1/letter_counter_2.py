# P:
#   Same as last time but exluding non-letter words when determining word size
#   How to exlude non-letter words?
#   Input: A string of words separated by whitespace
#   Output: A list of those words but without any apostophes, punctation marks, ect.
# E:
#   "What's up doc?" will be [whats, up, doc]
# D:
#   For now lists
# A:
#   1. Accept the string
#   2. Iterate over each character of the string
#   3. If the character is not an apostrophe or a punctation mark, add it to a new string
#   4. If the character encountered is a space or we reach the end, add the new string to a new element and reset the new string
#   5. Do steps 4 and 5 until we reach the end of the og string

def remove_non_letters(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char

    return result

def word_sizes(words):
    words_list = words.split()
    counts = {}

    for word in words_list:
        clean_word = remove_non_letters(word)

        clean_word_size = len(clean_word)
        if clean_word_size == 0:
            continue

        if clean_word_size not in counts:
            counts[clean_word_size] = 0

        counts[clean_word_size] += 1

    return counts

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# Ye
def word_sizes(string):
    hashmap = {}

    for word in string.split():
        clean = ''.join(char for char in word if char.isalpha())
        print(clean)
        length = len(clean)
        hashmap[length] = hashmap.get(length, 0) + 1

    return hashmap