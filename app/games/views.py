from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.
from app.games.models import Games,Genre
from app.games.seralisers import GamesSerializer, GenreSerializer


from app.filters import GamesFilter
from app.paginations import GamePagination



class GamesListAPIView(ListAPIView):
    queryset = Games.objects.select_related("genre").all() 
    serializer_class = GamesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["tittle"]
    filterset_class = GamesFilter
    pagination_class = GamePagination

class GameDetailAPIView(RetrieveAPIView):
    queryset = Games.objects.select_related("genre")
    serializer_class = GamesSerializer
    lookup_field = "id"
class GenreListAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
