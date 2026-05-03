from django.urls import path
from . import views

urlpatterns = [
    path('greeting/', views.greeting),
    path('about/', views.about),
    path('contacts/', views.contacts),
]