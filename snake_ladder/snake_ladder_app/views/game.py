from snake_ladder.snake_ladder_app.views.board import Board


class Game():
    def __init__(self, player,number_of_players):
        self.limit_of_players = number_of_players
        self.board = Board()
        self.players = [player]

    def has_players(self):
        return len(self.players) != 0

    def has_given_player(self, given_player):
        for player in self.players:
            if(player.name == given_player.name):
                return True
        return False

    def has_place(self):
        return len(self.players) < self.limit_of_players

    def add_player(self, player):
        if self.has_place() and not self.has_given_player(player):
            self.players.append(player)

    


