from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from app.user.models import User
from app.user.seralisers import RegisterSerializer, ProfileSerializer, LoginSerializer

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