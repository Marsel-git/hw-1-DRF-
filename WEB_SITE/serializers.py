from rest_framework import serializers

class GreetingSerializer(serializers.Serializer):
    message = serializers.CharField()


class AboutSerializer(serializers.Serializer):
    info = serializers.CharField()


class ContactSerializer(serializers.Serializer):
    phone = serializers.CharField()
    email = serializers.EmailField()