class Display:
    def __init__(self):
        self.state = True

    def print_game(self, clue, jumper):
        # Print the current game state, including the ground
        print(f"{clue}\n")
        print(f"{jumper}\n")
        self._print_ground()
    
    def _print_ground(self):
        print("^^ ^^ ^ ^")