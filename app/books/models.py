from django.db import models
from books import model_choises as mch
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True, default=None)
    author = models.ForeignKey('books.Author', on_delete=models.SET_NULL, null=True, default=None)
    category = models.ForeignKey('books.Category', on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=64)
    gender = models.BooleanField(null=True)
    native_language = models.CharField(max_length=32)

    def __str__(self):
        return self.first_name + ' ' + self.second_name


class RequestBook(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recipient = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(choices=mch.REQUEST_STATUSES)

    def __str__(self):
        return self.recipient


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Log(models.Model):
    path = models.CharField(max_length=512)
    method = models.CharField(max_length=64)
    time = models.PositiveIntegerField()
