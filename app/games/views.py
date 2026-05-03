from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
from app.games.models import Games
from app.games.seralisers import GamesSerializer

class GamesListAPIView(ListAPIView):
    queryset = Games.objects.select_related("genre").all() 
    serializer_class = GamesSerializer
    