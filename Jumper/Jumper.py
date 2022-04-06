class Jumper:
    def __init__(self):
        self._graphic = []
        self._health = 6

    def _create_graphic(self):
        # Load a new jumper into _graphic based on health
        full_graphic = [" ___", "/___\\", "\   /", " \ /", "  O", " /|\\", " / \\"]
        dead_graphic = ["  x", " /|\\", " / \\"]
        if self._health >= 3:
            for _ in range(self._health + 1):
                self._graphic.append(full_graphic[-1])
        else:
            for _ in range(3):
                self._graphic.append(dead_graphic[-1])

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