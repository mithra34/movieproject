from django.db import models

# Create your models here.
from django.http import HttpResponse


class movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()

    year=models.IntegerField()
    img = models.ImageField(upload_to='pics')
def __str__(self):
    return self.name
