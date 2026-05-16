from django.urls import path

from app.library.views import PurchaseGameAPI

purchase_view = PurchaseGameAPI.as_view({
    'post': 'create'
})

urlpatterns = [
    path("purchase-game/<int:game_id>/", purchase_view, name="purchase-game"),
]
