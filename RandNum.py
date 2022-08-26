
def guess_rand_num():
    rand_number = random.randint(1, 9)
    user_guess = int(input('Hello player. Guess the random number 1-9 inclusive'))
    win = True
    if user_guess == rand_number:
        print('Congrats genius, the random number was ', rand_number, "!")

    while user_guess != rand_number:
        user_quit = input('Bro just give up?(Y/N)')
        if user_quit == 'y' or user_quit == 'Y':
            user_guess = rand_number
            win = False
            break

        while user_guess > rand_number:
            if user_guess > 9:
                user_guess = int(input('1-9 idiot. Guess again: '))
            else:
                user_guess = int(input('Too high bro. Guess again: '))

        while user_guess < rand_number:
            if user_guess < 1:
                user_guess = int(input('1-9 idiot. Guess again: '))
            else:
                user_guess = int(input('Bro too low. Guess again: '))



    if not win:
        print('Bro you\'re a quitter. GTFO')
    else:
        print('Good job genius, the random number was ', rand_number, '!')