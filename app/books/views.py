from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from books.models import Author

# Create your views here.


def books_list(request):

    response_content = ''

    for book in Book.objects.all():
        response_content += f'ID: {book.id}, Author: {book.author} <br/>'

    return HttpResponse(response_content)


def authors_list(request):

    response_content = ''

    for author in Author.objects.all():
        response_content += f'Author name: {author.first_name}, {author.second_name}<br/>'

    return HttpResponse(response_content)