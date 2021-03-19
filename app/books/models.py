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


class RequestBook(models.Model):

    STATUS_IN_PROGRESS = 10
    STATUS_CONFIRMED = 20
    STATUS_REJECTED = 30
    STATUS_SENT_TO_RECIPIENT = 40
    STATUS_RECIPIENT_RECEIVED_BOOK = 50
    STATUS_SENT_BACK_TO_OWNER = 60
    STATUS_OWNER_RECEIVED_BACK = 70

    REQUEST_STATUSES = (
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_CONFIRMED, 'Confirmed '),
        (STATUS_REJECTED, 'Rejected'),
        (STATUS_SENT_TO_RECIPIENT, 'Sent via mail service'),
        (STATUS_RECIPIENT_RECEIVED_BOOK, 'Received Book'),
        (STATUS_SENT_BACK_TO_OWNER, 'Sent back'),
        (STATUS_OWNER_RECEIVED_BACK, 'Received Book (Final)'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recipient = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(choices=REQUEST_STATUSES)


class Category(models.Model):
    name = models.CharField(max_length=64)


class Log(models.Model):
    path = models.CharField(max_length=512)
    method = models.CharField(max_length=64)
    time = models.PositiveIntegerField()
