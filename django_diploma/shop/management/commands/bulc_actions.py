from typing import Sequence

from django.core.management import BaseCommand
from django.contrib.auth.models import User

from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo bulc actions")

        info = [
            ("smartphone 1", 199),
            ("smartphone 2", 199),
            ("smartphone 3", 199),
        ]

        products = [
            Product(name=name, price=price)
            for name, price in info
        ]

        result = Product.objects.bulk_create(products)

        for obj in result:
            print(obj)

        self.stdout.write("Done")
