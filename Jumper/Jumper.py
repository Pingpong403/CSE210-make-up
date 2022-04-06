class Jumper:
    def __init__(self):
        self._graphic = []
        self._health = 6
        self._create_graphic()

    def _create_graphic(self):
        # Load a new jumper into _graphic based on health
        full_graphic = [" ___", "/___\\", "\   /", " \ /", "  O", " /|\\", " / \\"]
        dead_graphic = ["  x", " /|\\", " / \\"]
        if self._health >= 3:
            self._graphic = full_graphic[6 - self._health:7]
        else:
            self._graphic = dead_graphic

    def lose_health(self):
        # Decrease the jumpers health
        self._health -= 1
        self._create_graphic()

    def get_graphic(self):
        # Return the current graphic as a string
        return "\n".join(self._graphic)

    def is_alive(self):
        # returns alive state of jumper
        return self._health != 2