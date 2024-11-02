from django.db import transaction
from rest_framework.request import Request

from auth_app.models import Profile
from basket_app.models import Basket, OrderProduct, Order
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


def update_order_info(request: Request, order: Order) -> None:
    data: dict = request.data
    print(f"{data=}")
    order.status = 'Ожидает оплаты'
    order.fullName = data['fullName']
    order.phone = data.get('phone', None)
    order.email = data['email']
    order.city = data['city']
    order.address = data['address']
    order.totalCost = data['totalCost']
    order.paymentType = data.get('paymentType') or 'online'
    order.deliveryType = data.get('deliveryType') or 'standard'
    order.save()


def create_new_order(request: Request):
    new_order: Order = Order.objects.create(user=request.user)
    new_order.totalCost = 0
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
        product_price: float = Product.objects.get(id=product_id).price
        products_cost: float = product_price * quantity
        new_order.totalCost += products_cost
        new_order.save()
