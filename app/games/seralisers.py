from rest_framework import serializers
from .models import Genre, Games

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug']

class GamesSerializer(serializers.ModelSerializer):
    genre_id = serializers.IntegerField(write_only=True, required=False)
    genre = GenreSerializer(read_only=True)
    creator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Games
        fields = ['id', 'title', 'description', 'price', 'release_data',
                  'developer', 'rating', 'created_at', 'updated_at', 'genre', 'genre_id', 'image', 'creator']
        read_only_fields = ['created_at', 'updated_at', 'creator']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Цена не может быть отрицательной')
        return value

    def create(self, validated_data):
        genre_id = validated_data.pop('genre_id', None)
        game = Games.objects.create(**validated_data)
        if genre_id:
            game.genre_id = genre_id
            game.save()
        return game

    def update(self, instance, validated_data):
        genre_id = validated_data.pop('genre_id', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if genre_id:
            instance.genre_id = genre_id
        instance.save()
        return instance
        
        