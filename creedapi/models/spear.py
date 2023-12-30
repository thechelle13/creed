
from django.db import models
from .game import Game
from .weapon import Weapon

class Spear(models.Model):
    label = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
