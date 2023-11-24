from django.db import models
from .user_equipe import User_Equipe

class Equipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User_Equipe, related_name='equipes')
    
    def __str__(self):
        return self.name