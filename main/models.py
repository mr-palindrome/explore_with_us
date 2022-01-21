from typing_extensions import Self
from django.db import models


# Create your models here.

class Destination(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price_from = models.IntegerField()
    price_to = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class USER_subs(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)


    def __str__(self):
        return self.name + " - "+ self.email