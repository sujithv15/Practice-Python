def cows_and_bulls():
    #// random number and turn to list
    rand_num = random.randint(1000, 9999)
    rand_num_in_list = list(str(rand_num))

    user_guess = 0
    user_guess_in_list = []
    cow_bull_list = ['x', 'x', 'x', 'x']
    cow_count = 0
    bull_count = 0
    num_found = False

    user_guess = input('Please guess the four digit number, press \'0\' to quit')

    if (user_guess == 'q'):
        print('Quitter ass nigga')


    print('<<Random: ', rand_num, '>>')
    print('<<User: ', user_guess, '>>')

    while user_guess != '0' and num_found == False:
        if int(user_guess) == int(rand_num):
            print('Congrats, you win!')
            num_found = True

        user_guess_in_list = list(str(user_guess))
        print(user_guess, user_guess_in_list)
        print(rand_num, rand_num_in_list)

        for i in range(len(rand_num_in_list)):
            if user_guess_in_list[i] == rand_num_in_list[i]:
                cow_bull_list[i] = 'cow'
                cow_count += 1
            elif user_guess_in_list[i] in rand_num_in_list:
                cow_bull_list[i] = 'bull'
                bull_count += 1
            else:
                cow_bull_list[i] = 'x'

        print(cow_bull_list)
        print('Cow totals: ', cow_count, '\nBull totals: ', bull_count)
        if not num_found:
            user_guess = input('Keep guessing or press 0 to quit')
            if int(user_guess) == 0:
                print('Boy bye')