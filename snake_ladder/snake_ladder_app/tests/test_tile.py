from snake_ladder.snake_ladder_app.views.tile import Tile


def test_given_the_tile_is_snake_is_snake_should_return_true():
    tile = Tile(True, False)
    assert tile.is_snake()


def test_given_the_tile_is_ladder_is_ladder_should_return_true():
    tile = Tile(False, True)
    assert tile.is_ladder()


def test_given_the_tile_is_not_ladder_nor_snake_is_safe_should_return_true():
    tile = Tile(False, False)
    assert tile.is_safe()

def test_given_the_tile_position_should_be_0():
    tile = Tile(False, False)
    assert tile.position == {"x": 0, "y": 0}


def test_given_the_tile_I_should_be_able_to_increment_the_position():
    tile = Tile(False, False)
    tile.increment_position(6)
    assert tile.position == {"x": 0, "y": 6}

def test_given_the_tile_I_should_be_able_to_decrement_the_position():
    tile = Tile(False, False)
    tile.increment_position(10)
    tile.decrement_position(6)
    assert tile.position == {"x": 0, "y": 4}
