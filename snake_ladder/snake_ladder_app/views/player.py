import random

class Player():
    def __init__(self, name):
        self.name = name
        self.id =  self.generate_id()
        self.position = 00

    def generate_id(self):
        return random.randrange(0, 10000, 1)
