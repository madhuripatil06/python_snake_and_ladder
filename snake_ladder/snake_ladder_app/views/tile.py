class Tile():
    def __init__(self, is_snake, is_ladder):
        self.position = {"x": 0, "y": 0}
        self.snake = is_snake
        self.ladder = is_ladder

    def is_snake(self):
        return self.snake == True

    def is_ladder(self):
        return self.ladder == True

    def is_safe(self):
        return self.ladder == False and self.snake == False

    def _add_position(self, number):
        position = str(self.position["x"]) + ""+ str(self.position["y"])
        position = int(position) + number
        self.position["x"] = position/10
        self.position["y"] = position - (self.position["x"] * 10)

    def increment_position(self, number):
        self._add_position(number)

    def _decrement_position(self, number):
        position = str(self.position["x"]) + ""+ str(self.position["y"])
        position = int(position) - number
        self.position["x"] = position/10
        self.position["y"] = position - (self.position["x"] * 10)

    def decrement_position(self, number):
        self._decrement_position(number)

