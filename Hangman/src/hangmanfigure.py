class HangmanFigure(object):
    """
    Class to define the Hangman Image.
    Displays the current Hangman and the gallows.
    Used by the Hangman class.

    """

    # variable to store the images for the hangman
    figures = [""" -----\n|\n|\n|\n|\n|\n---""",
               """ -----\n|   |\n|  ( )\n|\n|\n|\n ---\n""",
               """ -----\n|   |\n|  ( )\n|   |\n|   |\n|\n ---\n""",
               """ -----\n|   |\n|  ( )\n|  \|\n|   |\n|\n ---\n""",
               """ -----\n|   |\n|  ( )\n|  \|/\n|   |\n|\n ---\n""",
               """ -----\n|   |\n|  ( )\n|  \|/\n|   |\n|  /\n ---\n""",
               """ -----\n|   |\n|  ( )\n|  \|/\n|   |\n|  / \\\n ---\n"""]

    def __init__(self):
        """
        Constructor - Assigns current figure to the empty gallows

        """
        self.current_figure = self.figures[0]

    def print_current_hangman(self):
        """
        Method to print the current HangmanFigure image

        """
        print self.current_figure

    def update_figure(self, new):
        """
        Method to update the gallows

        """
        self.current_figure = self.figures[new]
