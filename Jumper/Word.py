import random

class Word:
    def __init__(self, filename = "words.txt"):
        self._word = self._read_file(filename)
        self._clue = []
        for _ in self._word:
            self._clue.append("_")

    def _read_file(self, filename):
        # Read the file and pick a random word
        # Overwrite _word
        return ""

    def _update_clue(self):
        # Replace the clue's underscores with the revealed letters
        pass

    def check_letter(self, letter):
        # Return the existance of a letter in the word
        pass

    def get_clue(self):
        # Return the decyphered word
        pass