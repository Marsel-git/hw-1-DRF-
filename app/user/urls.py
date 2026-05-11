from rest_framework.routers import DefaultRouter
from django.urls import path
from app.user.views import RegisterAPI, ProfileAPI, LoginAPI
router = DefaultRouter()
router.register('register', RegisterAPI, basename='register')
router.register('profile', ProfileAPI, basename='profile')

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
]
urlpatterns += router.urls
