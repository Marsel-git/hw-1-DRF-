from rest_framework import serializers
from app.library.models import Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = {'id' ,'game', 'purchased_at'}