from django.db import models

# Create your models here.

class Datamodel(models.Model):
    name = models.CharField(max_length=50)
    last = models.CharField(max_length=50)