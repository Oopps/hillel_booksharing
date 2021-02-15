from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView

from books.models import Book
from books.models import Author


# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'


class BookList(ListView):
    queryset = Book.objects.all()


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    success_url = reverse_lazy('book-list')
    fields = (
        'author',
        'title',
        'publish_year',
        'review',
        'condition',
    )


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    success_url = reverse_lazy('book-list')
    fields = (
        'author',
        'title',
        'publish_year',
        'review',
        'condition',
    )


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')


class AuthorList(ListView):
    queryset = Author.objects.all()


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    success_url = reverse_lazy('author-list')
    fields = (
        'first_name',
        'second_name',
        'date_of_birth',
        'date_of_death',
        'country',
        'gender',
        'native_language',
    )


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    success_url = reverse_lazy('author-list')
    fields = (
        'first_name',
        'second_name',
        'date_of_birth',
        'date_of_death',
        'country',
        'gender',
        'native_language',
    )


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
