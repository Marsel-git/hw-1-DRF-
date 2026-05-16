from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.library.models import Library
from app.games.models import Games
from app.library.seralisers import LibrarySerializer

class PurchaseGameAPI(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LibrarySerializer
    permission_classes = (IsAuthenticated,)
    
    def create(self, request, *args, **kwargs):
        game_id = kwargs.get('game_id')

        game = Games.objects.filter(id=game_id)
        if not game.exists():
            return Response({"error": "Игра не найдена"}, status=status.HTTP_404_NOT_FOUND)
        aready_bought = Library.objects.filter(user=request.user, game=game.exists())
        if aready_bought:
            return Response({"error": "Вы уже купили эту игру"}, status=status.HTTP_400_BAD_REQUEST)
        Library = Library.objects.create(user=request.user, game=game)
        return Response({"message": "Игра успешно куплена"}, status=status.HTTP_201_CREATED)