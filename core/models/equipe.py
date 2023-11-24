from django.db import models
from .user import User

class Equipe(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='equipes')
    
    def __str__(self):
        return self.name