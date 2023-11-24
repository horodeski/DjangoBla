from django.db import models
from .user import User

class Hackathon(models.Model):
    CAMPI_CHOICES = [
        ('AL', 'Abelardo Luz '),
        ('AR', 'Araquari'),
        ('BL', 'Blumenau'),
        ('BR', 'Brusque'),
        ('CA', 'Camboriú'),
        ('CO', 'Concórdia'),
        ('FR', 'Fraiburgo '),
        ('IB', 'Ibirama'),
        ('LU', 'Luzerna'),
        ('RS', 'Rio do Sul '),
        ('CA', 'Camboriú'),
        ('SR', 'Santa Rosa do Sul'),
        ('SB', 'São Bento do Sul'),
        ('SF', 'São Francisco do Sul'),
        ('SO', 'Sombrio '),
        ('VI', 'Videira'),
    ]
    theme = models.CharField(max_length=255)
    year = models.DateField()
    location = models.CharField(max_length=2, choices=CAMPI_CHOICES)
    
    def __str__(self):
        return self.name