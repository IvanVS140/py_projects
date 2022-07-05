"""a 'Rock, Raper, Scissors' auto-play game"""

from random import randint

P1 = 'Player 1'
P2 = 'Player 2'
game_list = ['rock', 'scissors', 'paper']
TEMPLATE = '{}: {}\n{}: {}\n\n{}\n'
while True:
    p1_rand = randint(0, 2)
    p2_rand = randint(0, 2)
    # print(p1_rand, p2_rand)
    if p1_rand == p2_rand:
        print(TEMPLATE.format(P1, game_list[p1_rand],
                              P2, game_list[p2_rand],
                              'draw..'))
        continue
    if p1_rand - p2_rand == -1 or p1_rand - p2_rand == 2:
        print(TEMPLATE.format(P1, game_list[p1_rand],
                              P2, game_list[p2_rand],
                              P1 + ' wins!'))
        break
    print(TEMPLATE.format(P1, game_list[p1_rand],
                          P2, game_list[p2_rand],
                          P2 + ' wins!'))
    break
