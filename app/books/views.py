from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book
from books.models import Author
from books.forms import BookForm, AuthorForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def books_list(request):

    context = {
        'books_list': Book.objects.all()
    }

    return render(request, 'books_list.html', context=context)


def books_create(request):

    form_data = request.POST

    if request.method == 'POST':
        form = BookForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    elif request.method == 'GET':
        form = BookForm()

    context = {
        "message": 'Book create',
        "form": form,
    }
    return render(request, 'books_create.html', context=context)


def book_update(request, pk):

    instance = get_object_or_404(Book, pk=pk)

    form_data = request.POST

    if request.method == 'POST':
        form = BookForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    elif request.method == 'GET':
        form = BookForm(instance=instance)

    context = {
        "message": 'Book update ',
        "form": form,
    }
    return render(request, 'books_create.html', context=context)


def book_delete(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    instance.delete()
    return redirect('book-list')


def authors_list(request):

    context = {
        'authors_list': Author.objects.all()
    }

    return render(request, 'authors_list.html', context=context)


def authors_create(request):

    form_data = request.POST

    if request.method == 'POST':
        form = AuthorForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    elif request.method == 'GET':
        form = AuthorForm()

    context = {
        "message": 'Author create',
        "form": form,
    }
    return render(request, 'authors_create.html', context=context)


def author_update(request, pk):

    instance = get_object_or_404(Author, pk=pk)

    form_data = request.POST

    if request.method == 'POST':
        form = AuthorForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    elif request.method == 'GET':
        form = AuthorForm(instance=instance)

    context = {
        "message": 'Author update',
        "form": form,
    }
    return render(request, 'authors_create.html', context=context)


def author_delete(request, pk):
    instance = get_object_or_404(Author, pk=pk)
    instance.delete()
    return redirect('author-list')
