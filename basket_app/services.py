from django.db import transaction
from rest_framework.request import Request

from basket_app.models import Basket, OrderProduct
from product_app.models import Product


def get_or_create_basket(request: Request):
    if request.user.is_authenticated:
        basket: Basket = Basket.objects.get(user=request.user)
        return basket

    elif request.user.is_anonymous:
        basket, _ = Basket.objects.get_or_create(session_key=request.session.session_key)
        return basket


@transaction.atomic
def cancel_order_product(order_product: OrderProduct, product_id: int):
    product: Product = Product.objects.get(id=product_id)
    product.count += int(order_product.quantity)
    product.save()
    order_product.delete()



