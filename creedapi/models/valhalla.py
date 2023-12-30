from django.db import models

class Valhalla(models.Model):
    location = models.CharField(max_length=255)
