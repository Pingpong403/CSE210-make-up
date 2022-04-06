from random import choice as randchoice
class Word:
    def __init__(self, filename = "words.txt"):
        self._word = self._read_file(filename)
        self._clue = []
        for letter in self._word:
            if letter == " ":
                self._clue.append(" ")
            else:
                self._clue.append("_")

    def _read_file(self, filename):
        # Read the file and return a random word
        words = []
        with open(filename) as f:
            for line in f:
                words.append(line.strip('\n'))
        return randchoice(words)

    def _update_clue(self, letter, i):
        # Replace the clue's underscores with the revealed letters
        self._clue[i] = letter

    def check_letter(self, letter):
        # Return the existance of a letter in the word
        flag = False
        for i in range(len(self._word)):
            if self._word[i].lower() == letter.lower():
                self._update_clue(self._word[i], i)
                flag = True

        return flag

    def get_clue(self):
        # Return the decyphered word
        return ' '.join(self._clue)

    def is_match(self):
        # returns whether the clue matches the word or not
        return self._word == self.get_clue()