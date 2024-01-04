from django.db import models

class Weapon(models.Model):
    label = models.CharField(max_length=255)
