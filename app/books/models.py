from django.db import models

# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(default=None)
    country = models.CharField(max_length=64)
    gender = models.CharField(max_length=16)
    native_language = models.CharField(max_length=32)
