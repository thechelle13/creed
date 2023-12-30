from django.db import models
from .game import Game
from .creedUser import CreedUser

class Character(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    level = models.IntegerField()
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=200)  # Add this line with a default value
    creed_user = models.OneToOneField(CreedUser, on_delete=models.CASCADE, related_name='character')