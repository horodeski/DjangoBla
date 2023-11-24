from django.db import models
from .user import User
from .hackathon import Hackathon

class Comentario(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='comentarios', on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, related_name='comentarios', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)