from hangmanfigure import HangmanFigure
from random import randint
from sys import argv


class Hangman(object):
    """
    Class to represent Hangman Game.

    """

    def __init__(self, filename):
        self.hangman_word = self.get_word(filename)        # Assign random hangman word from file
        self.word_guess = list("_ " * len(self.hangman_word))   # Creates blank spaces for word guess
        self.hangman_figure = HangmanFigure()               # Creates new Hangman Figure for display
        self.guessed_letters = []  # Letters Guessed
        self.guess_num = 0  # Number of Current Guesses

    def get_word(self, filename):
        """
        Method to read potential Hangman words into a list

        Args:
            filename: name of the file containing potential Hangman words

        Returns:
            word that we will be using for our Hangman game

        """
        with open(filename, "r") as f:
            content = f.readlines()
        print content
        # Get the word for the Hangman game and create a new game
        word = content[randint(0, len(content) - 1)].strip()
        return word

    def check_letter_guess(self, letter):
        """
        Method to check if the letter the user guessed is in the Hangman word
        Also sets any occurrences of the letter in variable 'word_guess'

        Args:
            letter: letter that the user guessed

        Returns:
            True if letter was in word and false otherwise

        Check to see if the user's guess is in the word
        Also sets the current user guess to the new guess
        """

        char_in_word = False
        if letter not in self.hangman_word:
            return False
        else:
            for i in range(0, len(self.hangman_word)):
                if letter == self.hangman_word[i]:
                    self.word_guess[i * 2] = letter
        return True

    def game_loop(self):
        """
        Method to serve as the round loop for a game of Hangman.

        """
        while self.guess_num <= 5:

            # Print out the hangman figure, word guess, and letters guessed
            self.hangman_figure.print_current_hangman()
            self.print_current_word_guess()
            self.print_letters_guessed()

            # Get and check user input
            letter_guess = raw_input("Enter a letter that has not already been guessed: ")
            while letter_guess in self.guessed_letters or not letter_guess.isalpha() or len(letter_guess) != 1:
                if letter_guess in self.guessed_letters:
                    letter_guess = raw_input("That letter has already been guessed.  Try again! ")
                elif not letter_guess.isalpha():
                    letter_guess = raw_input("That is not a letter! Try again! ")
                elif len(letter_guess) != 1:
                    letter_guess = raw_input("Please enter a single alphabetic character! ")
                break

            # Add guessed letter to list and see if it is in word
            self.guessed_letters.append(letter_guess)
            letter_in_the_word = self.check_letter_guess(letter_guess)
            if letter_in_the_word:
                print 'Great guess!  {} is in the word!'.format(letter_guess)
            else:
                print 'Too bad!  {} is not in the word!'.format(letter_guess)
                self.guess_num += 1
                self.hangman_figure.update_figure(self.guess_num)

            # Check if the user has won
            if '_' not in self.word_guess:
                print "Congratulations!  You won!"
                break

        # User lost
        else:
            print 'Aww, too bad!  Better luck next time!'

    def print_letters_guessed(self):
        """
        Method to print the letters the user has guessed in the current game of hangman

        """
        print "Letters Guessed: ",
        for i in self.guessed_letters:
            print i,
        print

    def print_current_word_guess(self):
        """
        Method to print the word as it has been guessed by the user

        """
        print ''.join(self.word_guess)
        print '\n\n'


def main(args):
    hangman = Hangman(args[1])
    hangman.game_loop()

main(argv)