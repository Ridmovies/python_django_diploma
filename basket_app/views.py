from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from basket_app.models import OrderProduct, Basket, Order
from basket_app.serializers import BasketSerializer, OrderProductSerializer, OrderSerializer
from product_app.models import Product


class BasketView(APIView):
    @extend_schema(tags=["basket"])
    def post(self, request: Request) -> Response:
        print(f"{request.data=}")
        product_id = request.data.get("id", None)
        count = request.data.get("count", None)
        basket: Basket = Basket.objects.get(user=request.user)
        order_product = OrderProduct.objects.create(
            product_id=product_id,
            quantity=count,
            basket=basket,
        )
        return Response(status=status.HTTP_200_OK)

    @extend_schema(tags=["basket"], responses=OrderProductSerializer)
    def get(self, request: Request) -> Response:
        basket: Basket = Basket.objects.get(user=request.user)
        products: OrderProduct = OrderProduct.objects.all()
        serializer = OrderProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(tags=["basket"])
    def delete(self, request: Request) -> Response:
        product_id = request.data.get("id")
        quantity = request.data.get("count")
        order_product: OrderProduct = OrderProduct.objects.get(
            product_id=product_id,
            quantity=quantity,
        )

        if order_product:
            order_product.delete()
        return Response(status=status.HTTP_200_OK)


class OrdersListView(APIView):
    @extend_schema(tags=["order"])
    def post(self, request: Request) -> Response:
        # Создание заказа
        basket: Basket = Basket.objects.get(user=request.user)
        new_order: Order = Order.objects.create()
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
        order: Order = Order.objects.all()
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
        order.phone = data['phone']
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
        print("order get 11111111111111")
        print(f"{request.data=}")
        order = Order.objects.get(id=id)
        # TODO Hardcore
        order.email = "test@email.com"

        serializer = OrderSerializer(order, many=False)
        # data = {
        #     "id": 123,
        #     "createdAt": "2023-05-05 12:12",
        #     "fullName": "Annoying Orange",
        #     "email": "no-reply@mail.ru",
        #     "phone": "88002000600",
        #     "deliveryType": "free",
        #     "paymentType": "online",
        #     "totalCost": 567.8,
        #     "status": "accepted",
        #     "city": "Moscow",
        #     "address": "red square 1",
        #     "products": [
        #         {
        #             "id": 123,
        #             "category": 55,
        #             "price": 500.67,
        #             "count": 12,
        #             "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
        #             "title": "video card",
        #             "description": "description of the product",
        #             "freeDelivery": True,
        #             "images": [
        #                 {
        #                     "src": "/3.png",
        #                     "alt": "Image alt string"
        #                 }
        #             ],
        #             "tags": [
        #                 {
        #                     "id": 12,
        #                     "name": "Gaming"
        #                 }
        #             ],
        #             "reviews": 5,
        #             "rating": 4.6
        #         }
        #     ]
        # }
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        # return JsonResponse(data=data, safe=True)


class PaymentView(APIView):
    @extend_schema(tags=["payment"])
    def post(self, request: Request, id:int) -> Response:
        return Response(status=status.HTTP_200_OK)
