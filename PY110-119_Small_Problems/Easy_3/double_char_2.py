# P:
#   Input: A string
#   Output: A new string that doubles every consonant in the input string
#   Explicit:
#       Not double vowels, digits, punctuation, or whitespace
#       Still add those characters but just dont double them

def double_consonants(the_string):
    new_string = ""
    for chara in the_string:
        if chara.isalpha() and chara not in ["a", "e", "i", "o", "u"]:
            new_string += chara * 2
        else:
            new_string += chara
    return new_string

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")