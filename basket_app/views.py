from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse, HttpResponseRedirect
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import Profile
from basket_app.models import OrderProduct, Basket, Order, Payment
from basket_app.serializers import OrderProductSerializer, OrderSerializer, PaymentSerializer
from basket_app.services import get_or_create_basket, cancel_order_product
from product_app.models import Product
from python_django_diploma import settings


class BasketView(APIView):
    @extend_schema(tags=["basket"], responses=OrderProductSerializer)
    def get(self, request: Request) -> Response:
        basket: Basket = get_or_create_basket(request)
        products: OrderProduct = OrderProduct.objects.filter(basket=basket)
        serializer = OrderProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(tags=["basket"])
    def post(self, request: Request) -> Response:
        # ADD TO CART
        product_id = request.data.get("id", None)
        count: str = request.data.get("count", None)
        basket: Basket = get_or_create_basket(request)
        product: Product = Product.objects.get(id=product_id)
        if not (int(count) <= product.count):
            return Response({"message": f"You can order only {product.count}"},
                            status=status.HTTP_409_CONFLICT)

        product_order, created = OrderProduct.objects.get_or_create(
            product_id=product_id,
            basket=basket,
        )
        if created:
            product_order.quantity = count
            product_order.save()
            product.count -= int(count)
            product.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"message": "Product already in basket"},
                            status=status.HTTP_409_CONFLICT)

    @extend_schema(tags=["basket"])
    def delete(self, request: Request) -> Response:
        basket: Basket = Basket.objects.get(user=request.user)
        product_id = request.data.get("id")
        order_product: OrderProduct = OrderProduct.objects.get(
            product_id=product_id,
            basket=basket,
        )
        if order_product:
            cancel_order_product(order_product, product_id)

        return Response(status=status.HTTP_200_OK)


class OrdersListView(APIView):
    @extend_schema(tags=["order"])
    def post(self, request: Request) -> Response:

        # Создание заказа
        basket: Basket = Basket.objects.get(user=request.user)
        # basket: Basket = get_or_create_basket(request)
        new_order: Order = Order.objects.create(user=request.user)
        new_order.totalCost = 0

        profile: Profile = Profile.objects.get(user=request.user)
        new_order.email = profile.email
        new_order.phone = profile.phone
        new_order.fullName = profile.fullName

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
        return Response({"orderId": new_order.id}, status=status.HTTP_200_OK)

    @extend_schema(tags=["order"])
    def get(self, request: Request) -> Response:
        # TODO Clean not active orders
        order: Order = Order.objects.filter(user=request.user, status__isnull=False)
        serializer = OrderSerializer(order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class OrderDetailView(APIView):
    @extend_schema(tags=["order"])
    def post(self, request: Request, id:int) -> Response:
        order = Order.objects.get(id=id)
        if order.status == 'Оплачено':
            return Response(status=status.HTTP_409_CONFLICT)

        data: dict = request.data
        order: Order = Order.objects.get(id=order.id)
        order.fullName = data['fullName']
        order.phone = data.get('phone', None)
        order.email = data['email']
        order.city = data['city']
        order.address = data['address']
        order.status = 'Ожидает оплаты'
        order.totalCost = data['totalCost']

        if not data['paymentType']:
            order.paymentType = 'online'
        else:
            order.paymentType = data['paymentType']

        if data['deliveryType'] == 'express':
            order.deliveryType = data['deliveryType']
        else:
            order.deliveryType = 'standard'

        order.save()
        return JsonResponse({"orderId": order.id})

    @extend_schema(tags=["order"], responses=OrderSerializer)
    def get(self, request: Request, id:int) -> Response:
        order = Order.objects.get(id=id)

        serializer = OrderSerializer(order, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PaymentView(APIView):
    @extend_schema(tags=["payment"])
    def post(self, request: Request, id:int) -> Response:
        basket: Basket = Basket.objects.get(user=request.user)
        order = Order.objects.get(id=id)
        data: dict = request.data
        credit_number = data.get("number", None)
        payment: Payment = Payment.objects.create(**data)
        order.status = 'Ожидает оплаты'
        serializer = PaymentSerializer(payment, many=False)
        if credit_number[-1] != "0":
            # TODO DO validation
            order.status = 'Оплачено'
        elif credit_number[-1] == "0":
            order.status = 'Ошибка оплаты'
        basket.products.clear()
        basket.save()
        order.save()
        return Response(status=status.HTTP_200_OK)



