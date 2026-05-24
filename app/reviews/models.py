from django.db import models

from app.games.models import Games
from app.user.models import User


class Review(models.Model):
    game = models.ForeignKey(
        Games,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Игра'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Оценка'
    )
    comment = models.TextField(
        blank=True,
        verbose_name='Комментарий'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    def __str__(self):
        return f'{self.game.title} ({self.score})'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
        