from typing import Sequence

from django.core.management import BaseCommand
from django.contrib.auth.models import User

from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo bulc update")

        result = Product.objects.filter(
            name__contains="smartphone",
        ).update(discount=10)
        print(result)

        self.stdout.write("Done")
