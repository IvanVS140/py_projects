"""used functions"""


def verify_input(user_input):
    """
verify_input
    :param user_input:
    :return:
    """
    while True:
        try:
            user_input = float(user_input)
        except ValueError:
            user_input = input('! This is not a number. Repeat input: ')
            continue
        else:
            return user_input


def normalize_index(index):
    """
normalize_index
    :param index:
    :return:
    """
    while index < 0 or index > 3:
        if index < 0:
            index *= -1
            print('{} {}'.format('! index normalized:', index))
        if index > 3:
            index = int(round(
                verify_input(input('! the value must be in range of 0 - 3, '
                                   'repeat input: ')), 0))
    print('{} {}'.format('index of new item:', index))
    return index
