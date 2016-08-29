from snake_ladder.snake_ladder_app.views.board import Board


def test_board_generate_tiles_should_generate_tiles_with_snake_tiles_and_ladder_tiles():
    board = Board()
    board.generate_tiles()
    assert len(board.tiles) == 100

def filter_for_snake(tile):
    if(tile.is_snake()):
        return tile

def test_board_generate_tiles_should_generate_tiles_with_5_snake_tiles():
    board = Board()
    board.generate_tiles()
    snake_tiles = filter(filter_for_snake, board.tiles)
    assert len(snake_tiles) == 5

def filter_for_ladder(tile):
    if(tile.is_ladder()):
        return tile

def test_board_generate_tiles_should_generate_tiles_with_6_ladder_tiles():
    board = Board()
    board.generate_tiles()
    snake_tiles = filter(filter_for_ladder, board.tiles)
    assert len(snake_tiles) == 7