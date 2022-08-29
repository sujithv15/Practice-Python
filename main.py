import TicTacToe
import GenFibSeq
import RandNum
import ReadWriteFiles
import RockPaperScissors
import CowsAndBulls
import HangmanGame

def main():
    user_input = int(input('Pick an excercise\n1. Random Number\n2. Generate Fibonacci Sequence\n3. Files\n'
                           '4. Rock Paper Scissors\n5. Cows and Bulls\n6. Tic Tac Toe\n7. Hangman\n'))
    match user_input:
        case 1:
            RandNum
        case 2:
            GenFibSeq
        case 3:
            ReadWriteFiles
        case 4:
            RockPaperScissors
        case 5:
            CowsAndBulls
        case 6:
            TicTacToe.tictactoe_menu()
        case 7:
            HangmanGame.play_hangman()
        case _:
            print("Later bitch")

main()
