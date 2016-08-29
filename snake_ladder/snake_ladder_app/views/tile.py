class Tile():
    def __init__(self, position, is_snake, is_ladder, destination=None):
        self.position = position
        self.snake = is_snake
        self.ladder = is_ladder
        self.destination = destination

    def is_snake(self):
        return self.snake == True

    def is_ladder(self):
        return self.ladder == True

    def is_safe(self):
        return self.ladder == False and self.snake == False

    def increment_position(self, number):
        return self.position + number

    def decrement_position(self, number):
        return self.position - number

