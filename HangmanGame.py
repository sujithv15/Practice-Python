import random

def play_hangman():
    # open file and put each word in list then pick a randon number to select random element in list
    with open('sowpods.txt', 'r') as sowpods:
        lines = sowpods.readlines()
        rand_int = random.randint(0, len(lines))

    # removes \n char and puts chars of string seperated into list
    clue_word = list(lines[rand_int].strip().lower())
    print(clue_word)

    # create empty char lists for word with current guessed letters and list for wrong letters
    current_word_guessed = []
    wrong_letters = []
    guessed_letters = []
    word_solved = False
    input_validated = False
    # creates empty word represented by underscore for current word's not guessed chars
    for letter in range(len(clue_word)):
        current_word_guessed.append('_')

    user_guess_letter = input('Guess your first letter! ').lower()

    while not word_solved:

        while not input_validated:
            # validate length == 1 and is letter
            while len(user_guess_letter) != 1 or not user_guess_letter.isalpha():
                user_guess_letter = input('Follow instructions bitch, guess a letter: ').lower()
            # once input format validated, validate if letter already guessed
            if user_guess_letter in wrong_letters:
                print(user_guess_letter, 'was already played! Idiot')
                user_guess_letter = '_'
            else:
                input_validated = True

        # loop through clue word array
        letter_count = int(0)
        for i in range(len(clue_word)):

            # if char matched with user_guess_letter, then current_word_guessed at that index will have the
            # underscore replaced with the letter
            if user_guess_letter == clue_word[i]:
                current_word_guessed[i] = user_guess_letter
                letter_count += 1
        if letter_count == 1:
            print("There is 1", user_guess_letter)
        if letter_count > 1:
            print('There are', letter_count, user_guess_letter, '\'s.')

        if user_guess_letter not in clue_word:
            if user_guess_letter not in wrong_letters:
                wrong_letters.append(user_guess_letter)
            print('Sorry, no \'', user_guess_letter, '\' in word')
            print('Guessed letters:', wrong_letters)

        if clue_word == current_word_guessed:
            word_solved = True
            print('Solved word:', current_word_guessed)
        else:
            print_current = ''
            for i in range(len(current_word_guessed)):
                print_current = print_current + current_word_guessed[i]
            print('Current word:', print_current)
            user_guess_letter = input('Enter the next letter you want to guess: ').lower()
            input_validated = False


