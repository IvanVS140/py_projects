"""Separates all letters in a user string with a user character. Can be
improved for cyrillic too"""

from string import ascii_letters


# pure
def separate(string, char):
    """
separates all letters in a string with characters
    :param string:
    :param char:
    :return:
    """
    index = 0
    result = ''
    while index < len(string) - 1:
        if string[index] in ascii_letters and string[index + 1] \
                in ascii_letters:
            result += string[index] + char
        else:
            result += string[index]
        index += 1
    result += string[index]
    return result


with open("../_source/eggs.txt") as f:
    text = f.read()

print('{}\n{}\n\n   {}\n'.format(text, separate(text, "."),
                                 "Have. a. nice. day."))


# by enumerate, more elegant i think
def separate(string, char):
    """
separates all letters in a string with characters
    :param string:
    :param char:
    :return:
    """
    result = ''
    for index, item in enumerate(string):
        if index == len(string) - 1:
            result += item
            return result
        if item in ascii_letters and string[index + 1] in ascii_letters:
            result += item + char
        else:
            result += item
    return result


if __name__ == '__main__':
    with open("../_source/eggs.txt") as f:
        text = f.read()
        print('{}\n{}\n\n   {}'.format(text, separate(text, "."),
                                       "Have. a. nice. day."))
