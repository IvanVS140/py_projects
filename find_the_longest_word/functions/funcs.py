"""used functions"""

from string import ascii_letters
# from collections import Counter


def count_letters_in_words(text):
    """
counts all letters in words and finds maximum value
    :param text:
    :return max_chars:
    """
    index = 0
    letter_counter = 0
    result = []
    while index < len(text):
        if text[index] in ascii_letters:
            letter_counter += 1
        else:
            if letter_counter == 0:
                index += 1
                continue
            result.append(letter_counter)
            letter_counter = 0
        index += 1
    result.append(letter_counter)
    print(result)
    print('{} {}{}'.format('[макс. значение:', max(result), ']'))
    print('{} {}{}'.format('[количество повторений макс. значения:',
                           result.count(max(result)), ']'))
    return result


def calculate_word(text, max_chars):
    """
calculates the longest word
    :param text:
    :param max_chars:
    :return longest word:
    """
    index = 0
    result = ''
    while index < len(text):
        if text[index] in ascii_letters and all(c in ascii_letters for c in text[index:index + max_chars]):
                result += text[index:index + max_chars]
                print('{} {}{}'.format('[самое длинное слово:', result, ']'))
                return result
        index += 1


def find_longest_word(text):
    """
connects two functions
    :rtype: object
    :param text:
    """
    calculate_word(text, max(count_letters_in_words(text)))
    print('\n    have. a. nice. day.')
