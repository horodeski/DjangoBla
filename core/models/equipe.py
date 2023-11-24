from django.db import models
from .user import User
from .avaliacao import Avaliacao

class Equipe(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='equipes')
    RATING_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    nota = models.IntegerField(choices=RATING_CHOICES, default='0')
    def __str__(self):
        return self.name