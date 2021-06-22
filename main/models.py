from django.db import models


# Create your models here.
from django.forms import forms


class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.title
