from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView

from books.models import Book
from books.models import Author

from openpyxl import Workbook
from datetime import datetime


class Index(TemplateView):
    template_name = 'index.html'


class BookList(ListView):
    queryset = Book.objects.all().select_related('author', 'category')


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


def export_books_to_xlsx(request):
    """
    Downloads all books as Excel file with a single worksheet
    """
    book_queryset = Book.objects.all().select_related('author', 'category')

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename={date}-books.xlsx'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )
    workbook = Workbook()

    # Get active worksheet/tab
    worksheet = workbook.active
    worksheet.title = 'Books'

    # Define the titles for columns
    columns = [
        'Title',
        'Publish_year',
        'Review',
        'Condition',
        'Author',
        'Category',
    ]
    row_num = 1

    # Assign the titles for each cell of the header
    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    # Define the data for each cell in the row
    for book in book_queryset:
        row_num += 1
        row = [
            book.title,
            book.publish_year,
            book.review,
            book.condition,
            book.author.second_name,
            book.category,
        ]

        # Assign the data for each cell of the row
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value

    workbook.save(response)
    return response
