"""lists and exceptions"""


def verify_input(user_input):
    """verifies user input on int or float type and catch an exception

    Args:
        user_input (int, float): user input

    Returns:
        float: user input
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
    """normalizes user input to index-type (int)

    Args:
        index (int): index to normalize

    Returns:
        int: normalized index
    """
    while index < 0 or index > 3:
        if index < 0:
            index *= -1
            print('{} {}'.format('! index normalized:', index))
        if index > 3:
            index = int(round(verify_input(input(
                '! the value must be in range of 0 - 3, repeat input: ')), 0))
    print('{} {}'.format('index of new item:', index))
    return index


nums = [round(verify_input(input('Введите первое число: ')), 1),
        round(verify_input(input('Второе.. ')), 1),
        round(verify_input(input('Ещё одно ')), 1),
        round(verify_input(input('Ну и последнее) ')), 1)]

LIST_TEMPLATE = "\n{} {} {}"
print(LIST_TEMPLATE.format('Текущий список:', nums, '(данные округлены)'))

MOD_LIST_TEMPLATE = "{} {}"
print(MOD_LIST_TEMPLATE.format(
    'Количество элементов в текущем списке:', len(nums)))

print(MOD_LIST_TEMPLATE.format(
    'Сумма элементов текущего списка:', round(sum(nums), 0)))

NEW_INDEX = normalize_index(int(round(verify_input(input(
    '\nВведите индекс нового элемента: ')), 0)))
NEW_NUM = round(verify_input(input('Введите значение нового элемента: ')), 1)

nums.insert(NEW_INDEX, NEW_NUM)

print(LIST_TEMPLATE.format(
    'Новый список:', nums, '(добавленный элемент округлён)'))
print(MOD_LIST_TEMPLATE.format(
    'Количество элементов в новом списке:', len(nums)))
print(MOD_LIST_TEMPLATE.format(
    'Сумма элементов нового списка:', round(sum(nums), 1)))
