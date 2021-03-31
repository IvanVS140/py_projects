"""finds the longest word in a string"""

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
    for i in result:
        print("{} - {}".format(i, len(i)))
    print("\nThe longest word is: {}\n".format(max(result, key=len)))
