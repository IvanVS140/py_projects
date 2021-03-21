"""dictionary assistant. converts an arbitrary string into a normalized
dictionary"""

SPAM = "бензин горит температура 35.5678 1 первый 2.1234 2-ой 3.0"  # odd
print('{}\n{}\n'.format('Source string:', SPAM))


def make_dict(string):
    """
converts an arbitrary string into a non-normalized dictionary
    :param string: arbitrary string
    :return: non-normalized dictionary
    """
    new_list = string.split()
    dictionary = {}
    index = 0
    while index < len(new_list) - 1:
        dictionary.update({new_list[index]: new_list[index + 1]})
        index += 2
    if index == len(new_list) - 1:  # if the list has an odd number of
        # elements, then the value of extreme key will be set to None
        dictionary.update({new_list[index]: None})
    return dictionary


def is_digit(string):
    """
checks if a string-type item represented by a digit
    :param string: string-type item to check
    :return: True if a digit, and False if not
    """
    if string is None:
        return False
    if string.isdigit():
        return True
    try:
        float(string)
        return True
    except ValueError:
        return False


def normalize_dict(dictionary):
    """
if the key or its value represented by numbers - converts them into a float
with subsequent rounding
    :param dictionary: non-normalized dictionary
    :return: normalized dictionary
    """
    (key_round, value_round) = (0, 2)  # rounding values. If the key is
    # rounded to "0" characters, then it will be represented by an integer
    normalized_dict = {}
    for key, value in dictionary.items():
        if is_digit(key):
            if key_round == 0:
                new_key = int(round(float(key), 0))
            else:
                new_key = round(float(key), key_round)
        else:
            new_key = key
        if is_digit(value):
            new_value = round(float(value), value_round)
        else:
            new_value = value
        normalized_dict.update({new_key: new_value})
    return normalized_dict


print('{}\n{}'.format('Output:', (normalize_dict(make_dict(SPAM)))))
