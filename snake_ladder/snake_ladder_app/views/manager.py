from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from game import Game


class Manager(APIView):
    def __init__(self):
        self.game = None
        self.all_games = []

    def generate_cookie(self, player_name):
        return 'player_'+ player_name + '_in_game_No._'+str(len(self.all_games))


    def post(self, request):
        self.game = Game(request.data['username'], int(request.data['no_of_players']))
        self.all_games.append(self.game)
        response = HttpResponse(status.HTTP_201_CREATED)
        cookie = self.generate_cookie(request.data['username'])
        response.set_signed_cookie(key='name', value=cookie)
        print response.cookies.get('name')
        return response

