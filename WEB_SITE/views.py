from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import GreetingSerializer, AboutSerializer, ContactSerializer
@api_view(['GET'])
def greeting(request):
    data = {"message": "Привет! Добро пожаловать на наш сайт игр Steam!"}
    serializer = GreetingSerializer(data)
    return Response(serializer.data)


@api_view(['GET'])
def about(request):
    data = {"info": "Мы занимаемся разработкой приложеня для магазина игр Steam!"}
    serializer = AboutSerializer(data)
    return Response(serializer.data)


@api_view(['GET'])
def contacts(request):
    data = {
        "phone": "+996 700 00 00 00",
        "email": "example@mail.com"
    }
    serializer = ContactSerializer(data)
    return Response(serializer.data)