"""Separates all letters in a user string with a user character. Can be
improved for cyrillic too"""

from string import ascii_letters


def separate(string, symbol):
    """[separates all letters in a string with user symbol(s)]

    Args:
        string ([str]): [some string]
        symbol ([any type]): [symbol-separator]

    Returns:
        [type]: [string with letters separated by a symbol-separator]
    """
    result = ''
    for index, item in enumerate(string):
        if index == len(string) - 1:
            result += item
            return result
        if item in ascii_letters and string[index + 1] in ascii_letters:
            result += item + symbol
        else:
            result += item
    return result


if __name__ == '__main__':
    SEP_SYMBOL = str(input("Enter splitter symbol(s): "))
    with open("_source/eggs.txt") as f:
        text = f.read()
        print('\n{}\n{}\n'.format(text, separate(text, SEP_SYMBOL)))
