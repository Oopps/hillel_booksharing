import random
from django.core.management.base import BaseCommand
from books.models import Author
from faker import Faker


class Command(BaseCommand):
    help = 'Generate Random Authors Data'  # noqa

    def add_arguments(self, parser):
        parser.add_argument('qty', type=int)

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(options['qty']):
            first_name = fake.first_name()
            second_name = fake.last_name()
            country = fake.country()
            gender = random.choice([True, False])
            native_language = country

            Author.objects.create(
                first_name=first_name,
                second_name=second_name,
                country=country,
                gender=gender,
                native_language=native_language

            )
