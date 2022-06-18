"""lists, exceptions"""


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
            index = int(round(verify_input(input(
                '! the value must be in range of 0 - 3, repeat input: ')), 0))
    print('{} {}'.format('index of new item:', index))
    return index


NUMS = [round(verify_input(input('Введите первое число: ')), 1),
        round(verify_input(input('Второе.. ')), 1),
        round(verify_input(input('Ещё одно ')), 1),
        round(verify_input(input('Ну и последнее) ')), 1)]

LIST_TEMPLATE = "\n{} {} {}"
print(LIST_TEMPLATE.format('Текущий список:', NUMS, '(данные округлены)'))

MOD_LIST_TEMPLATE = "{} {}"
print(MOD_LIST_TEMPLATE.format(
    'Количество элементов в текущем списке:', len(NUMS)))

print(MOD_LIST_TEMPLATE.format(
    'Сумма элементов текущего списка:', round(sum(NUMS), 0)))

NEW_INDEX = normalize_index(int(round(verify_input(input(
    '\nВведите индекс нового элемента: ')), 0)))
NEW_NUM = round(verify_input(input('Введите значение нового элемента: ')), 1)

NUMS.insert(NEW_INDEX, NEW_NUM)

print(LIST_TEMPLATE.format(
    'Новый список:', NUMS, '(добавленный элемент округлён)'))
print(MOD_LIST_TEMPLATE.format(
    'Количество элементов в новом списке:', len(NUMS)))
print(MOD_LIST_TEMPLATE.format(
    'Сумма элементов нового списка:', round(sum(NUMS), 1)))
