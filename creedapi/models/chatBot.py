
from django.db import models


class ChatBot(models.Model):
    content = models.CharField(max_length=255)
    