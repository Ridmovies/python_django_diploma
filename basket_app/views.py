from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import Profile
from basket_app.models import OrderProduct, Basket, Order, Payment
from basket_app.serializers import BasketSerializer, OrderProductSerializer, OrderSerializer, PaymentSerializer
from product_app.models import Product


class BasketView(APIView):
    @extend_schema(tags=["basket"])
    def post(self, request: Request) -> Response:
        print(f"{request.data=}")
        product_id = request.data.get("id", None)
        count = request.data.get("count", None)
        basket: Basket = Basket.objects.get(user=request.user)

        # TODO FIX ADD to cart
        order_product = OrderProduct.objects.get_or_create(
            product_id=product_id,
            quantity=count,
            basket=basket,
        )
        return Response(status=status.HTTP_200_OK)

    @extend_schema(tags=["basket"], responses=OrderProductSerializer)
    def get(self, request: Request) -> Response:
        basket: Basket = Basket.objects.get(user=request.user)
        products: OrderProduct = OrderProduct.objects.filter(basket=basket)
        serializer = OrderProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(tags=["basket"])
    def delete(self, request: Request) -> Response:
        basket: Basket = Basket.objects.get(user=request.user)
        order: Order = Order.objects.filter(user=request.user)
        product_id = request.data.get("id")
        quantity = request.data.get("count")
        order_product: OrderProduct = OrderProduct.objects.get(
            product_id=product_id,
            quantity=quantity,
            basket=basket,
            # order=order,
        )
        print(order_product)

        if order_product:
            order_product.delete()
        return Response(status=status.HTTP_200_OK)


class OrdersListView(APIView):
    @extend_schema(tags=["order"])
    def post(self, request: Request) -> Response:
        # Создание заказа
        basket: Basket = Basket.objects.get(user=request.user)
        new_order: Order = Order.objects.create(user=request.user)
        new_order.totalCost = 0

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
        order: Order = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class OrderDetailView(APIView):
    @extend_schema(tags=["order"])
    def post(self, request: Request, id:int) -> JsonResponse:
        print("Оформить заказ")
        print(f"{request.data=}")
        order = Order.objects.get(id=id)
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
        profile: Profile = Profile.objects.get(user=request.user)
        order.email = profile.email
        order.phone = profile.phone

        serializer = OrderSerializer(order, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PaymentView(APIView):
    @extend_schema(tags=["payment"])
    def post(self, request: Request, id:int) -> Response:
        order = Order.objects.get(id=id)
        data: dict = request.data
        credit_number = data.get("number", None)
        payment: Payment = Payment.objects.create(**data)
        print(f"{payment=}")
        serializer = PaymentSerializer(payment, many=False)
        # TODO DO validation
        order.status = 'Оплачено'
        order.save()
        return Response(status=status.HTTP_200_OK)



