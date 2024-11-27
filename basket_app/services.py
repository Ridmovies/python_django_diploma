from _decimal import ROUND_HALF_UP
from django.db import transaction
from rest_framework.request import Request
from decimal import Decimal

from auth_app.models import Profile
from basket_app.models import Basket, Order, OrderProduct
from product_app.models import Product


def get_or_create_basket(request: Request):
    if request.user.is_authenticated:
        basket: Basket = Basket.objects.get(user=request.user)
        return basket

    elif request.user.is_anonymous:
        # Сохранение сессии перед использованием сессионного ключа
        request.session.modified = True
        request.session.save()

        basket, _ = Basket.objects.get_or_create(
            session_key=request.session.session_key
        )
        return basket


def add_product_to_basket(product_id, count, basket):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise ValueError(f"Product with ID {product_id} does not exist.")

    if int(count) > product.count:
        message = f"You can order only {product.count} products."
        raise Exception(message)

    product_order, created = OrderProduct.objects.get_or_create(
        product_id=product.id, basket=basket
    )

    if created:
        product_order.quantity = count
        product_order.save()
        product.count -= int(count)
        product.save()
    else:
        raise RuntimeError("Product already in basket")

    return product_order


@transaction.atomic
def cancel_order_product(order_product: OrderProduct, product_id: int):
    product: Product = Product.objects.get(id=product_id)
    product.count += int(order_product.quantity)
    product.save()
    order_product.delete()


def update_order_info(request: Request, order: Order) -> None:
    data: dict = request.data
    order.status = "Ожидает оплаты"
    order.fullName = data["fullName"]
    order.phone = data.get("phone", None)
    order.email = data["email"]
    order.city = data["city"]
    order.address = data["address"]
    order.totalCost = data["totalCost"]
    order.paymentType = data.get("paymentType") or "online"
    order.deliveryType = data.get("deliveryType") or "standard"
    order.save()


def create_new_order(request: Request):
    new_order: Order = Order.objects.create(user=request.user)
    new_order.totalCost = Decimal(0)
    profile: Profile = Profile.objects.get(user=request.user)
    new_order.email = profile.email
    new_order.phone = profile.phone
    new_order.fullName = profile.fullName
    new_order.save()
    return new_order


def add_products_in_order(request: Request, basket: Basket, new_order: Order):
    for product in request.data:
        product_id = product.get("id")
        quantity = product.get("count")
        order_product: OrderProduct = OrderProduct.objects.create(
            product_id=product_id,
            quantity=quantity,
            basket=basket,
            order=new_order,
        )
        new_order.products.add(order_product)
        # Calculate Order's totalCost
        # Фронт сам считает totalCost
        product_price: Decimal = Product.objects.get(id=product_id).price
        products_cost: Decimal = product_price * quantity
        new_order.totalCost += products_cost.quantize(
            Decimal('.01'),
            rounding=ROUND_HALF_UP
        )
        new_order.save()
