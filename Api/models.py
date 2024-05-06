from django.db import models
from django import forms
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


# Create your models here.
