from django.db import models

# Create your models here.
from django.db.models import ProtectedError


class Book(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=64)
    gender = models.BooleanField(null=True)
    native_language = models.CharField(max_length=32)

    def delete(self, **kwargs):
        raise ProtectedError('This model can not be deleted')


class Log(models.Model):
    path = models.CharField(max_length=512)
    method = models.CharField(max_length=64)
    time = models.PositiveIntegerField()
