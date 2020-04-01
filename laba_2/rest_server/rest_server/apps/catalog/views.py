from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import ComputerGame, Company, Platform, Engine
from .serializers import ComputerGameSerializer


class ComputerGameView(APIView):

    def get(self, request):
        print(ComputerGame._meta.get_fields())
        game = ComputerGame.objects.all()
        serializer = ComputerGameSerializer(game, many=True)
        return Response({"game": serializer.data})

    def post(self, request):
        print(request.META.get('CONTENT_TYPE', '').lower())
        print(request.body)
        game = request.data.get('game')
        serializer = ComputerGameSerializer(data=game)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            game_saved = serializer.save()
        return Response({"success": "Game '{}' created successfully".format(game_saved.name)})

    def put(self, request, pk):
        saved_game = get_object_or_404(ComputerGame.objects.all(), pk=pk)
        data = request.data.get('game')
        serializer = ComputerGameSerializer(instance=saved_game, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            game_saved = serializer.save()
        return Response({
            "success": "Game '{}' updated successfully".format(game_saved.name)
        })

    def delete(self, request, pk):
        game = get_object_or_404(ComputerGame.objects.all(), pk=pk)
        game.delete()
        return Response({
            "message": "Game with id `{}` has been deleted.".format(pk)
        }, status=204)
