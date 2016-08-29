from snake_ladder.snake_ladder_app.views.tile import Tile


class Board():
    def __init__(self):
        self.snake_tile_numbers = {31: 14, 37: 17, 78: 39, 92: 35, 99: 7}
        self.ladder_tile_numbers = {5: 25, 10: 29, 22: 41, 28: 55, 44: 95, 70: 89, 79: 81}
        self.tiles = []

    def _generate_snake_tiles(self, number):
        return Tile(number, True, False, self.snake_tile_numbers[number])

    def _generate_ladder_tiles(self, number):
        return Tile(number, False, True, self.ladder_tile_numbers[number])

    def generate_tiles(self):
        for i in range(0,100):
            if(i in self.snake_tile_numbers.keys()):
                tile = self._generate_snake_tiles(i)
            elif(i in self.ladder_tile_numbers.keys()):
                tile = self._generate_ladder_tiles(i)
            else:
                tile = Tile(i, False, False)
            self.tiles.append(tile)





