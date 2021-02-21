from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True, default=None)
    author = models.ForeignKey('books.Author', on_delete=models.SET_NULL, null=True, default=None)
    category = models.ForeignKey('books.Category', on_delete=models.SET_NULL, null=True, default=None)


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=64)
    gender = models.BooleanField(null=True)
    native_language = models.CharField(max_length=32)


class Category(models.Model):
    name = models.CharField(max_length=64)


class Log(models.Model):
    path = models.CharField(max_length=512)
    method = models.CharField(max_length=64)
    time = models.PositiveIntegerField()
