from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    img_url = models.CharField(max_length=30)
    