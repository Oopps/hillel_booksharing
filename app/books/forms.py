from django import forms

from books.models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'author',
            'title',
            'publish_year',
            'review',
            'condition',
            'cover',
         )


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            'first_name',
            'second_name',
            'date_of_birth',
            'date_of_death',
            'country',
            'gender',
            'native_language',
         )
