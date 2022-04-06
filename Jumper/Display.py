class Display:
    def __init__(self):
        pass

    def print_game(self, clue, jumper):
        # Print the current game state, including the ground
        print(f"{clue}\n")
        print(f"{jumper}\n")
    
    def _print_ground(self):
        print("^^ ^^ ^ ^")