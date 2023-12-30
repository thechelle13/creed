
from django.db import models

class Game(models.Model):
    label = models.CharField(max_length=255)