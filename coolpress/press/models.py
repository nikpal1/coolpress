from django.db import models

# Create your models here.
class Category(models.Model):
    label = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
