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
        clue = self._word.get_clue()
        graphic = self._jumper.get_graphic()
        self._display.print_game(clue, graphic)
        # Loop:
        while True:
            # Ask for a letter from a-z
            letter_guess = input("Guess a letter [a-z]: ")
            # Update the jumper and word based on input
            self._update(letter_guess)
            # Display the new word and jumper
            clue = self._word.get_clue()
            graphic = self._jumper.get_graphic()
            self._display.print_game(clue, graphic)
            # If out of lives, game over
            if self._jumper.is_alive():
                if not "_" in clue:
                    print("Winner!")
                    break
            else:
                break

    def _update(self, letter):
        # Talk to Word and Jumper and update the clue and the jumper
        # Pass the letter given into check_letter --> True or False
        # Use result to update jumper health
        correct = self._word.check_letter(letter)
        if correct:
            pass
        else:
            self._jumper.lose_health()