class Jumper:
    def __init__(self):
        self._graphic = []
        self._health = 6

    def _create_graphic(self):
        # Load a new jumper into _graphic based on health
        pass

    def _delete_line(self):
        # Delete the top line of the jumper
        pass

    def lose_health(self):
        # decreasing the jumpers health
        pass

    def get_graphic(self):
        # Return the current graphic as a string
        pass

    def is_alive(self):
        # returns alive state of jumper
        return self._health != 0