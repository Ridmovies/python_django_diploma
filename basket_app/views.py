from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from basket_app.models import OrderProduct, Basket
from basket_app.serializers import BasketSerializer, OrderProductSerializer
from product_app.models import Product


class BasketView(APIView):
    @extend_schema(tags=["basket"])
    def post(self, request: Request) -> Response:
        print(f"{request.data=}")
        product_id = request.data.get("id", None)
        product = Product.objects.get(id=product_id)
        count = request.data.get("count", None)
        basket: Basket = Basket.objects.get(user=request.user)
        order_product = OrderProduct.objects.create(
            product=product,
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
        # return Response(status=status.HTTP_200_OK)
        # data = [
        #     {
        #         "id": 123,
        #         "category": 55,
        #         "price": 500.67,
        #         "count": 12,
        #         "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
        #         "title": "video card",
        #         "description": "description of the product",
        #         "freeDelivery": True,
        #         "images": [
        #             {
        #                 "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
        #                 "alt": "hello alt",
        #             }
        #         ],
        #         "tags": [
        #             {
        #                 "id": 0,
        #                 "name": "Hello world"
        #             }
        #         ],
        #         "reviews": 5,
        #         "rating": 4.6
        #     },
        #     {
        #         "id": 124,
        #         "category": 55,
        #         "price": 201.675,
        #         "count": 5,
        #         "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
        #         "title": "video card",
        #         "description": "description of the product",
        #         "freeDelivery": True,
        #         "images": [
        #             {
        #                 "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
        #                 "alt": "hello alt",
        #             }
        #         ],
        #         "tags": [
        #             {
        #                 "id": 0,
        #                 "name": "Hello world"
        #             }
        #         ],
        #         "reviews": 5,
        #         "rating": 4.6
        #     }
        # ]
        # return JsonResponse(data, safe=False)


class OrdersListView(APIView):
    @extend_schema(tags=["order"])
    def get(self, request: Request) -> Response:
        # history-order/
        data = [
            {
        "id": 123,
        "createdAt": "2023-05-05 12:12",
        "fullName": "Annoying Orange",
        "email": "no-reply@mail.ru",
        "phone": "88002000600",
        "deliveryType": "free",
        "paymentType": "online",
        "totalCost": 567.8,
        "status": "accepted",
        "city": "Moscow",
        "address": "red square 1",
        "products": [
          {
            "id": 123,
            "category": 55,
            "price": 500.67,
            "count": 12,
            "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
            "title": "video card",
            "description": "description of the product",
            "freeDelivery": True,
            "images": [
              {
                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                "alt": "Image alt string"
              }
            ],
            "tags": [
              {
                "id": 12,
                "name": "Gaming"
              }
            ],
            "reviews": 5,
            "rating": 4.6
          }
        ]
      },
            {
        "id": 123,
        "createdAt": "2023-05-05 12:12",
        "fullName": "Annoying Orange",
        "email": "no-reply@mail.ru",
        "phone": "88002000600",
        "deliveryType": "free",
        "paymentType": "online",
        "totalCost": 567.8,
        "status": "accepted",
        "city": "Moscow",
        "address": "red square 1",
        "products": [
          {
            "id": 123,
            "category": 55,
            "price": 500.67,
            "count": 12,
            "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
            "title": "video card",
            "description": "description of the product",
            "freeDelivery": True,
            "images": [
              {
                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                "alt": "Image alt string"
              }
            ],
            "tags": [
              {
                "id": 12,
                "name": "Gaming"
              }
            ],
            "reviews": 5,
            "rating": 4.6
          }
        ]
      }
        ]
        return JsonResponse(data, safe=False)
