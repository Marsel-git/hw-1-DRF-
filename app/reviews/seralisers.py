from rest_framework import serializers

from app.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'game',
            'author',
            'score',
            'comment',
            'created_at',
        ]
        read_only_fields = ['id', 'author', 'game', 'created_at']

    def validate_score(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError('Оценка должна быть от 0 до 10')
        return value
