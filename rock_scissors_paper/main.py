"""a 'Rock, Raper, Scissors' auto-play game"""

from random import choice

P1 = 'Player 1'
P2 = 'Player 2'
game_list = ['rock', 'scissors', 'paper']
TEMPLATE = '{}: {}\n{}: {}\n\n{}\n'
while True:
    p1_rand = choice(game_list)
    p2_rand = choice(game_list)
    if p1_rand == p2_rand:
        print(TEMPLATE.format(P1, p1_rand, P2, p2_rand, 'draw..'))
        continue
    elif p1_rand == game_list[0] and p2_rand == game_list[1] or \
            p1_rand == game_list[1] and p2_rand == game_list[2] or \
            p1_rand == game_list[2] and p2_rand == game_list[0]:
        print(TEMPLATE.format(P1, p1_rand, P2, p2_rand, P1 + ' wins!'))
        break
    else:
        print(TEMPLATE.format(P1, p1_rand, P2, p2_rand, P2 + ' wins!'))
    break
