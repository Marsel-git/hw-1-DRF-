from rest_framework.routers import DefaultRouter
from django.urls import path
from app.user.views import RegisterAPI, ProfileAPI, LoginAPI, LogoutAPI, PasswordResetAPI

router = DefaultRouter()
router.register('register', RegisterAPI, basename='register')
router.register('profile', ProfileAPI, basename='profile')

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('password-reset/', PasswordResetAPI.as_view(), name='password_reset'),
]
urlpatterns += router.urls
