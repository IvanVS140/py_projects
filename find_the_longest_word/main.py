"""finds the longest word in a string"""

from find_the_longest_word.functions.funcs import find_longest_word
from string import ascii_letters

with open("../_source/spam.txt") as f:
    text = f.read()
    result = []
    for i in text.split():
        if i[-1] not in ascii_letters:
            i = list(i)
            del i[-1]
            i = ''.join(i)
        result.append(i.lower())
    print(result)

find_longest_word(text)
