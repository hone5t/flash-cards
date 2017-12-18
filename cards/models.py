from django.db import models
from django.conf import settings

class Card(models.Model):
  front    = models.TextField(max_length=500)
  back     = models.TextField()
  category = models.CharField(max_length=30)
  known    = models.BooleanField()
  owner    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)