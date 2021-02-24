import random
from datetime import datetime
from django.core.management.base import BaseCommand
from books.models import Book, Author
from faker import Faker


class Command(BaseCommand):
    help = 'Generate Random Books Data'  # noqa

    def add_arguments(self, parser):
        parser.add_argument('qty', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        book_list = []

        for _ in range(options['qty']):
            author = Author.objects.order_by('?').last()
            title = fake.word().capitalize()
            publish_year = random.randint(0, datetime.now().year)
            review = fake.text()
            condition = random.randint(1, 5)

            book_list.append(Book(
                author=author,
                title=title,
                publish_year=publish_year,
                review=review,
                condition=condition
            ))
        Book.objects.bulk_create(book_list)
