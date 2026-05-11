import django_filters

from app.games.models import Games

class GamesFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(field_name="genre__slug", lookup_expr="iexact")
    class Meta:
        model = Games
        fields = ["genre"]