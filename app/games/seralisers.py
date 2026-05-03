from rest_framework import serializers
from .models import Genre, Games

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug']
class GamesSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Games
        fields = ['id', 'title', 'description', 'price', 'release_data',
          'developer', 'rating', 'created_at', 'genre', 'image']
        
        