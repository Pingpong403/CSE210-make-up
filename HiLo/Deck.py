from random import randint
class Deck:
    def __init__(self):
        self.state = True
    
    def draw(self):
        return randint(1, 13)