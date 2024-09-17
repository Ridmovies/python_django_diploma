from django.core.management import BaseCommand

from shop.models import Product


class Command(BaseCommand):
    """
    Create products
    """

    def handle(self, *args, **options):
        self.stdout.write("Create products")
        products_data = [
            {"title": "smartphone 1", "price": 200},
            {"title": "smartphone 2", "price": 300}
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(**product_data)
            self.stdout.write(f"Created product {product.title}")

        self.stdout.write(self.style.SUCCESS("SUCCESS"))
