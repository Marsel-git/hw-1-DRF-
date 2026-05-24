from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from app.games.models import Games
from app.reviews.models import Review
from app.reviews.seralisers import ReviewSerializer


class GameReviewViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_game(self):
        return get_object_or_404(Games, pk=self.kwargs.get('game_pk'))

    def get_queryset(self):
        return self.queryset.filter(game_id=self.kwargs.get('game_pk'))

    def perform_create(self, serializer):
        serializer.save(
            game=self.get_game(),
            author=self.request.user if self.request.user.is_authenticated else None,
        )

    @action(detail=False, methods=['post'], url_path='review')
    def review(self, request, game_pk=None):
        return self.create(request)

    @action(detail=False, methods=['get'], url_path='reviews')
    def reviews(self, request, game_pk=None):
        return self.list(request)
