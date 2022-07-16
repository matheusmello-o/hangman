import os
import sys
sys.path.append('hangman/')
import hangman

os.system('cls' if os.name == 'nt' else 'clear')

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

game = hangman.Hangman()
game.select_secret_word()

def letras(lista):
    lista = list(lista)
    return print(' '.join(lista))

def display_word(secret_word, right_letters):
    secret_word = list(secret_word)
    display = [letter if letter in right_letters else '_' for letter in secret_word]
    return ' '.join(display)

def main():
    while game.check_continue_game() == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(board[game.get_wrong_plays()])
        
        print('')
        print(display_word(game.get_secret_word(), game.get_letters_right()))

        print('')
        print('Letters Right: ')
        letras(game.get_letters_right())

        print('')
        print('Letters Wrong: ')
        letras(game.get_letters_wrong())

        print('')
        game.play()

if __name__ == '__main__':
    main()