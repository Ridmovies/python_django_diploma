from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class BasketView(APIView):
    @extend_schema(tags=["basket"])
    def post(self, request: Request) -> Response:
        print(f"{request.data=}")
        product_id = request.data.get("id", None)
        count = request.data.get("count", None)
        return Response(status=status.HTTP_200_OK)

    @extend_schema(tags=["basket"])
    def get(self, request: Request) -> Response:
        data = {
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
                  "src": "/3.png",
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
        return JsonResponse(data, safe=False)


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
