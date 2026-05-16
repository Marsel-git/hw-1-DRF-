from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from app.user.models import User
from app.user.seralisers import (
    RegisterSerializer,
    ProfileSerializer,
    LoginSerializer,
    LogoutSerializer,
    PasswordResetSerializer,
)

class RegisterAPI(GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProfileAPI(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class LoginAPI(TokenObtainPairView):
    serializer_class = LoginSerializer

class LogoutAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Успешный выход из системы'}, status=status.HTTP_204_NO_CONTENT)

class PasswordResetAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Пароль успешно изменён'})
   