from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=6,
    )
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'email', 'username', 'avatar', 'balance', 'created_at']

class LoginSerializer(TokenObtainPairSerializer):
        username_field = User.EMAIL_FIELD
        def validate(self, attrs):
            credentials = {
                'email': attrs.get('email'),
                'password': attrs.get('password')
            }
            user = authenticate(**credentials)
            if user is None:
                raise serializers.ValidationError('Неверный email или пароль')
            data = super().validate(attrs)

            data['user'] = {
                'id': user.id,
                'email': user.email,
                'username': user.username,
            }
            return data
        