from typing import Sequence

from django.core.management import BaseCommand
from django.contrib.auth.models import User

from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo select fields")
        # users_info = User.objects.values_list("pk", "username")
        users_info = User.objects.values_list("username", flat=True)
        print(users_info)
        for user_info in users_info:
            print(user_info)

        # product_values = Product.objects.values("pk", "name")
        # for p_value in product_values:
        #     print(p_value)

        self.stdout.write("Done")
