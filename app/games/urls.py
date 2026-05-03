from django.urls import path

from app.games.views import GamesListAPIView

urlpatterns = [
    path("list-games", GamesListAPIView.as_view(), name="list-games")
]
