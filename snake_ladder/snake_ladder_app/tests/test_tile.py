from snake_ladder.snake_ladder_app.views.tile import Tile

def test_given_the_tile_is_snake_is_snake_should_return_true():
    tile = Tile(00, True, False)
    assert tile.is_snake()

def test_given_the_tile_is_ladder_is_ladder_should_return_true():
    tile = Tile(00, False, True)
    assert tile.is_ladder()

def test_given_the_tile_is_not_ladder_nor_snake_is_safe_should_return_true():
    tile = Tile(00, False, False)
    assert tile.is_safe()

def test_given_the_tile_position_should_be_0():
    tile = Tile(00, False, False)
    assert tile.position == 00

def test_given_the_tile_I_should_be_able_to_increment_the_position():
    tile = Tile(00, False, False)
    position = tile.increment_position(6)
    assert position == 06

def test_given_the_tile_I_should_be_able_to_decrement_the_position():
    tile = Tile(10, False, False)
    position = tile.decrement_position(6)
    assert position == 04
