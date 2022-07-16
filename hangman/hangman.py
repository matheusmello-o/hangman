from time import sleep

class Hangman():
    def __init__(self, secret_word = None, letters_right = [], letters_wrong = [], letters = [], wrong_plays = 0):
        self.secret_word = secret_word
        self.letters = letters
        self.letters_right = letters_right
        self.letters_wrong = letters_wrong
        self.wrong_plays = wrong_plays

    # GETTERS E SETTERS

    def set_secret_word(self, new_word):
        self.secret_word = new_word
    
    def get_secret_word(self):
        return self.secret_word

    def get_letters_right(self):
        return self.letters_right
    
    def set_letters_right(self, letter):
        self.letters_right.append(letter)
     
    def get_letters_wrong(self):
        return self.letters_wrong
    
    def set_letters_wrong(self, letter):
        self.letters_wrong.append(letter)

    def get_letters(self):
        return self.letters

    def set_letters(self, letter):
        self.letters.append(letter)

    def set_wrong_plays(self):
        self.wrong_plays = self.wrong_plays + 1
    
    def get_wrong_plays(self):
        return self.wrong_plays

    # METODOS

    def select_secret_word(self):
        from random import randint
        path = 'words-database/words.txt'
        with open(path, 'rt') as f:
            file = f.readlines()

        random_number = randint(0, len(file)) - 1
        new_word = file[random_number].strip()
        return self.set_secret_word(new_word)

    def play(self):
        if self.get_secret_word() != None:
            guess_letter = input('GIVE ME SOME LETTER: ').strip().lower()
            if guess_letter in self.get_letters():
                print('YOU ALREADY GOT ME THAT ONE')
                sleep(1)
            else:
                self.set_letters(guess_letter)
                self.check_play(guess_letter)
        else:
            print('FIRST YOU NEED TO CREATE A SECRET WORD.')


    def check_play(self, guess_letter):
        secret_word = self.secret_word
        if guess_letter in secret_word:
            print('GOOD ONE')
            self.set_letters_right(guess_letter)
        else:
            print('WRONG ONE.')
            self.set_letters_wrong(guess_letter)
            self.set_wrong_plays()

    def game_won(self):
        return len(set(self.secret_word)) == len(self.get_letters_right())

    def game_lose(self):
        return self.get_wrong_plays() <= 6

    def check_continue_game(self):
        if self.game_won():
            print('GOOD! YOU GOT IT!')
            return False
        elif self.game_lose():
            return True
        else:
            print('\nOH NO, YOU LOSE.')