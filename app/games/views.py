from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from app.games.models import Games, Genre
from app.games.seralisers import GamesSerializer, GenreSerializer
from app.filters import GamesFilter
from app.paginations import GamePagination
from app.games.permissions import IsCreatorOrAdmin


class GamesListAPIView(ListAPIView):
    queryset = Games.objects.select_related("genre").all()
    serializer_class = GamesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["title"]
    filterset_class = GamesFilter
    pagination_class = GamePagination
    permission_classes = [AllowAny]


class GameDetailAPIView(RetrieveAPIView):
    queryset = Games.objects.select_related("genre")
    serializer_class = GamesSerializer
    lookup_field = "id"
    permission_classes = [AllowAny]


class GameCreateAPIView(CreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GameUpdateAPIView(UpdateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated, IsCreatorOrAdmin]


class GameDestroyAPIView(DestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated, IsCreatorOrAdmin]


class GenreListAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]
