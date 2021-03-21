"""'rock, paper, scissors' game auto play"""

from random import choice

p1 = 'игрок 1:'
p2 = 'игрок 2:'
game_list = ['камень', 'ножницы', 'бумага']
template = '{} {}\n{} {}\n{}'
while True:
    p1_rand = choice(game_list)
    p2_rand = choice(game_list)
    if p1_rand == p2_rand:
        print(template.format(p1, p1_rand, p2, p2_rand, 'ничья!\n'))
        continue
    if p1_rand == game_list[0] and p2_rand == game_list[1] or \
            p1_rand == game_list[1] and p2_rand == game_list[2] or \
            p1_rand == game_list[2] and p2_rand == game_list[0]:
        print(template.format(p1, p1_rand, p2, p2_rand, 'игрок 1 победил!'))
        break
    print(template.format(p1, p1_rand, p2, p2_rand, 'игрок 2 победил!'))
    break
print('\n Have. a. nice. day.')
