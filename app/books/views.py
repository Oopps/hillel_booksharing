from django.http import HttpResponseRedirect
from django.shortcuts import render

from books.models import Book
from books.models import Author
from books.forms import BookForm, AuthorForm


# Create your views here.


def books_list(request):

    context = {
        'books_list': Book.objects.all()
    }

    return render(request, 'books_list.html', context=context)


def books_create(request):

    form_data = request.GET

    if form_data:
        form = BookForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book/list/')
    else:
        form = BookForm()

    context = {
        "message": 'Book create',
        "form": form,
    }
    return render(request, 'books_create.html', context=context)


def authors_list(request):

    context = {
        'authors_list': Author.objects.all()
    }

    return render(request, 'authors_list.html', context=context)


def authors_create(request):

    form_data = request.GET

    if form_data:
        form = AuthorForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book/author/list/')
    else:
        form = AuthorForm()

    context = {
        "message": 'Author create',
        "form": form,
    }
    return render(request, 'authors_create.html', context=context)
