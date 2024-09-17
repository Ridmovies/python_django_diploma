from typing import Sequence

from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.db.models import Avg, Max, Min, Count

from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo aggregate")

        result = Product.objects.aggregate(
            Avg("price"),
            Max("price"),
            min_price=Min("price"),
            count=Count("price"),
        )

        print(result)
        self.stdout.write("Done")
