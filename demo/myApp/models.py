from django.db import models

# Create your models here.

class TodoITem(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)