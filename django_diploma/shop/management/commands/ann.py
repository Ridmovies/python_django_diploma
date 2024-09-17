
from django.core.management import BaseCommand


from shopapp.models import Product, Order
from django.db.models import Avg, Max, Min, Count, Sum


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start demo aggregate")

        orders = Order.objects.annotate(
            total=Sum("products__price", default=0),
            products_count=Count("products"),
        )

        for order in orders:
            print(
                f"Order #{order.id} "
                f"with {order.products_count} "
                f"Total {order.total}"
            )
        self.stdout.write("Done")
