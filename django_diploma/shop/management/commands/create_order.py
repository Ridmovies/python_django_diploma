from typing import Sequence

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from shopapp.models import Order, Product


class Command(BaseCommand):
    """
    Create order
    """

    @transaction.atomic
    def handle(self, *args, **options):
        # with transaction.atomic():
        #     ...
        self.stdout.write("Create order")
        user = User.objects.get(username="root")
        # products: Sequence[Product] = Product.objects.defer("description", "price", "created_at").all()
        products: Sequence[Product] = Product.objects.only("id").all()
        order, created = Order.objects.get_or_create(
            delivery_address="test address",
            promocode="prom5",
            user=user,
        )
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(f"Created order {order}")
