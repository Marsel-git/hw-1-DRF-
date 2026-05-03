from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(
        max_length=155,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        unique=True
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Games(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Название'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Цена'
    )
    release_data = models.DateField(
        null=True, 
        blank=True,
        verbose_name='Дата Выхода'
    )
    developer = models.CharField(
        max_length=155,
        blank=True,
        verbose_name='Создатели'
    )
    rating = models.FloatField(
        default=0.0,
        verbose_name='Рейтинг'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL,
        null=True,
        related_name='games'
    )
    image = models.ImageField(
        upload_to='covers/', 
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-created_at']
