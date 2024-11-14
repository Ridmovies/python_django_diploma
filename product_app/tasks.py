from celery import shared_task
from django.db.models import Avg

from product_app.models import Product, Review


# @shared_task
# def update_product_avg_rating(product_id: int):
#     average_rate = Review.objects.filter(product_id=product_id).aggregate(Avg("rate"))[
#         "rate__avg"
#     ]
#     product: Product = Product.objects.get(id=product_id)
#     product.rating = average_rate
#     product.save()

