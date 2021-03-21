"""lists, exceptions"""

from lists_and_exceptions.functions.funcs import verify_input, normalize_index

nums = [round(verify_input(input('Введите первое число: ')), 1),
        round(verify_input(input('Второе.. ')), 1),
        round(verify_input(input('Ещё одно ')), 1),
        round(verify_input(input('Ну и последнее) ')), 1)]

LIST_TEMPLATE = "\n{} {} {}"
print(LIST_TEMPLATE.format('Текущий список:', nums, '(данные округлены)'))

MOD_LIST_TEMPLATE = "{} {}"
print(MOD_LIST_TEMPLATE.format('Количество элементов в текущем списке:',
                               len(nums)))

print(MOD_LIST_TEMPLATE.format('Сумма элементов текущего списка:',
                               round(sum(nums), 0)))

new_index = normalize_index(int(round(verify_input(input('\nВведите индекс '
                                                         'нового элемента: '
                                                         )), 0)))
new_num = round(verify_input(input('Введите значение нового элемента: ')), 1)

nums.insert(new_index, new_num)

print(LIST_TEMPLATE.format('Новый список:', nums, '(добавленный элемент '
                                                  'округлён)'))
print(MOD_LIST_TEMPLATE.format('Количество элементов в новом списке:',
                               len(nums)))
print(MOD_LIST_TEMPLATE.format('Сумма элементов нового списка:',
                               round(sum(nums), 1)))
print('\n Have. a. nice. day.')
