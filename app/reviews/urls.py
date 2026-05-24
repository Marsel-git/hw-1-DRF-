from rest_framework.routers import DefaultRouter

from app.reviews.views import GameReviewViewSet

router = DefaultRouter()
router.register(r'(?P<game_pk>\d+)', GameReviewViewSet, basename='game-reviews')

urlpatterns = router.urls
