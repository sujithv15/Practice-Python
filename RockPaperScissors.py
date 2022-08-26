
def rock_paper_scissors():
    moves = {1 : 'Rock', 2 : 'Paper', 3 : 'Scissor'}
    player_move = int(input('Rock, paper, scissors, Shoot!\n1. Rock\n2. Paper\n3. Scissors\nPlayer move: '))
    cpu_move = random.randint(1, 4)
    print('Player move: ', moves[player_move], player_move)
    print('CPU move: ', moves[cpu_move], cpu_move)

    result = 0
    if player_move == cpu_move:
        result = 0
    elif player_move == 1 and cpu_move == 3:
            result = 1
    elif player_move == 2 and cpu_move == 1:
            result = 1
    elif player_move == 3 and cpu_move == 2:
            result = 1
    else:
        result = -1
    if result == 0:
        print('Tie')
    elif result == -1:
        print('You Lose')
    else:
        print('You Win!')