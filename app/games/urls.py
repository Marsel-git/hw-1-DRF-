from django.urls import path

from app.games.views import GamesListAPIView, GenreListAPIView , GameDetailAPIView

urlpatterns = [
    path("list-games", GamesListAPIView.as_view(), name="list-games"),
    path("list-genres", GenreListAPIView.as_view(), name="list-genres"),
    path("list-games/<int:id>", GameDetailAPIView.as_view(), name="detail-games"),
]
