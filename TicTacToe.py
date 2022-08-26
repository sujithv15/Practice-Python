
def draw_board():
    n = int(input('Enter square size: '))
    x = 0
    while x < n:
        y = 0
        while y < n:
            print(' --- ', end = ' ')
            y += 1
        print('\n')
        y = 0
        while y < n:
            print('|   |', end = ' ')
            y += 1
        print('\n')
        x += 1
    y = 0
    while y < n:
        print(' --- ', end=' ')
        y += 1
    print('\n')

def check_tic_tac_toe(game):
    # create array for possible wins (wins also include when one row has same nonzero value)
    wins = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [0, 1, 2], [2, 1, 0]]
    win_found = False
    winning_player = 0
    # will check if a sublist of game[] has [1, 1, 1,] or [2, 2, 2]
    col_index = 0
    while col_index < 3 and not win_found:
        if game[col_index][0] == game[col_index][1] == game [col_index][2]:
            winning_player = game[col_index][0]
            if winning_player != 0:
                win_found = True
        col_index += 1

    # iterate through list of wins[] if exists in game[] until end of wins[] or if tic tac toe in game[] found
    index_wins = 0
    while index_wins < len(wins) and not win_found:
        # if winner at game[0], game[1], game[2] are possible combinations of winning positions from wins[]
        # essentially will search game[0 - 2][<<elements from each sublist 0 - 2 from wins[]] if they contain
            # the same number, indicating tic tac toe
        if game[0][wins[index_wins][0]] == game[1][wins[index_wins][1]] == game[2][wins[index_wins][2]]:
            winning_player = game[0][wins[index_wins][0]]
            if winning_player != 0:
                win_found = True
        index_wins += 1

    if win_found:
        print('Congratulations player', winning_player, 'is the winner!')
    else:
        print('No winner found.')

def moves_tic_tac_toe(game):
    max_moves = 9
    curr_move = 0
    player = 1

    while curr_move < max_moves:
        space_validated = False
        print('Player,', player, 'is up.')
        player_input = input('Enter row and column. (Format: \'ROW,COL\') ')

        # trying to validate user input!!
        while not space_validated:
            while len(player_input) != 3 or player_input[1] != ',' or player_input[0]\
                    not in ['0', '1', '2'] or player_input[2] not in ['0', '1', '2']:
                player_input = input('Invalid entry. Please make sure response in proper, \'ROW,COL\' '
                                     'format and row/column is within range of Tic Tac Toe baord(0 or 1 or 2): ')

            player_move = player_input.split(',')
            row = int(player_move[0])
            col = int(player_move[1])
            print('Player', player, 'move: ', row, col)

            if game[row][col] == 0:
                space_validated = True
            else:
                player_input = input('That space has already been played! Please choose an open square: ')


        game[row][col] = player


        print(game)

        if player == 1:
            player = 2
        elif player == 2:
            player = 1
        else:
            player = 0
        curr_move += 1
    print(game)