from Deck import Deck

class Director:
    def __init__(self):
        self._score = 300
    def update_score(self, points):
        self._score += points
    def game_loop(self):
        deck = Deck()
        while True:
            # Current card is displayed - Card :: Draw()
            card1 = deck.draw()
            print(f'The card is: {card1}')
            # Player guesses hi/lo
            hilo = input('Higher or lower? [h/l]: ')
            # The next card is displayed - Card :: Draw()
            card2 = deck.draw()
            print(f'The card is: {card2}')
            # If correct, +100 pt, if wrong, -75 pt
            if card1 < card2 and hilo == 'h':
                points = 100
            elif card1 > card2 and hilo == 'l':
                points = 100
            else:
                points = -75
            self.update_score(points)
            print(f'Your score is: {self._score}')
            # If game over, exit
            if self.game_over():
                print('You lost!')
                break
            else:
                again = input('Play again? [y/n]: ')
                if again == 'y':
                    pass
                else:
                    break
    def game_over(self):
        if self._score <= 0:
            return True
        else:
            return False