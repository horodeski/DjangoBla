from django.db import models

from .user import User


class Avaliacao(models.Model):
    RATING_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    nota = models.IntegerField(choices=RATING_CHOICES, default='Null')
    avaliador = models.ForeignKey(User, related_name='avaliacoes', on_delete=models.CASCADE)