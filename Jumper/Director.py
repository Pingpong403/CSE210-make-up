from Display import Display
from Jumper import Jumper
from Word import Word

class Director:
    def __init__(self):
        self._jumper = Jumper()
        self._word = Word()
        self._display = Display()

    def game_loop(self):
        # Display the clue along with a full jumper
        # Loop:
        # Ask for a letter from a-z
        # Update the jumper and word based on input
        # Display the new word and jumper
        # If out of lives, game over
        pass

    def _update(self, letter):
        # Talk to Word and Jumper and update the clue and the jumper
        # Pass the letter given into check_letter --> True or False
        # Use result to update jumper health
        pass