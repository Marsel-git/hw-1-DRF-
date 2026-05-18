from django.urls import path

from app.games.views import (
    GamesListAPIView,
    GenreListAPIView,
    GameDetailAPIView,
    GameCreateAPIView,
    GameUpdateAPIView,
    GameDestroyAPIView,
)

urlpatterns = [
    path("list-games", GamesListAPIView.as_view(), name="list-games"),
    path("list-genres", GenreListAPIView.as_view(), name="list-genres"),
    path("list-games/<int:id>", GameDetailAPIView.as_view(), name="detail-games"),
    path("create-game", GameCreateAPIView.as_view(), name="create-game"),
    path("update-game/<int:id>", GameUpdateAPIView.as_view(), name="update-game"),
    path("delete-game/<int:id>", GameDestroyAPIView.as_view(), name="delete-game"),
]
