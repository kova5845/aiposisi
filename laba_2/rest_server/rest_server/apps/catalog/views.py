from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ComputerGame, Company, Platform, Engine
from .serializers import ComputerGameSerializer

class ComputerGameView(APIView):

    def get(self, request):
        game = ComputerGame.objects.all()
        serializer = ComputerGameSerializer(game, many=True)
        return Response({"game": serializer.data})

    def post(self, request):
        game = request.data.get('game')
        serializer = ComputerGameSerializer(data=game)
        if serializer.is_valid(raise_exception=True):
            game_saved = serializer.save()
        return Response({"success": "Game '{}' created successfully".format(game_saved.name)})
