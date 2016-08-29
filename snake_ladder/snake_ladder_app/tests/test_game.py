from snake_ladder.snake_ladder_app.views.game import Game
from snake_ladder.snake_ladder_app.views.player import Player

def test_game_has_players_should_return_true_if_player_is_there_when_game_started():
    bunty = Player("bunty")
    game = Game(bunty, 2)
    assert game.has_players()

def test_game_has_place_should_return_true_if_other_player_can_still_join_the_game():
    bunty = Player("bunty")
    game = Game(bunty, 2)
    assert game.has_place()

def test_game_has_given_player_should_return_true_if_given_player_is_already_a_member_of_game():
    bunty = Player("bunty")
    game = Game(bunty, 2)
    assert game.has_given_player(bunty)

def test_game_add_player_should_add_given_player_to_game():
    bunty = Player("bunty")
    game = Game(bunty, 2)
    assert game.has_given_player(bunty)
    game.add_player(Player("pinky"))
    assert not game.has_place()