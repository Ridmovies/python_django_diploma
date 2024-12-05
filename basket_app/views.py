from datetime import datetime, timedelta

from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from basket_app.models import Basket, Order, OrderProduct
from basket_app.serializers import OrderProductSerializer, OrderSerializer
from basket_app.services import (
    add_product_to_basket,
    add_products_in_order,
    create_new_order,
    get_or_create_basket,
    update_order_info, remove_product_from_basket
)


class BasketView(APIView):
    @extend_schema(tags=["basket"], responses=OrderProductSerializer)
    def get(self, request: Request) -> Response:
        basket: Basket = get_or_create_basket(request)
        products: OrderProduct = OrderProduct.objects.filter(basket=basket)
        serializer = OrderProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(tags=["basket"], responses=OrderProductSerializer)
    def post(self, request: Request) -> Response:
        """ ADD TO CART """
        product_id: int = request.data.get("id", None)
        count: str = request.data.get("count", None)
        basket: Basket = get_or_create_basket(request)
        try:
            product_order = add_product_to_basket(product_id, count, basket)
            serializer = OrderProductSerializer(
                OrderProduct.objects.filter(basket=basket), many=True
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_409_CONFLICT)

    @extend_schema(tags=["basket"], responses=OrderProductSerializer)
    def delete(self, request: Request) -> Response:
        basket: Basket = get_or_create_basket(request)
        remove_product_from_basket(request, basket)
        serializer = OrderProductSerializer(basket.products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrdersListView(APIView):
    @extend_schema(tags=["order"])
    def post(self, request: Request) -> Response:
        """ Оформление заказа """
        basket: Basket = Basket.objects.get(user=request.user)
        # basket: Basket = get_or_create_basket(request)
        # if request.user.is_authenticated:
        #     new_order = create_new_order(request)
        # else:
        #     new_order = create_anonymous_order(request)
        new_order = create_new_order(request)
        add_products_in_order(request, basket, new_order)
        return Response({"orderId": new_order.id}, status=status.HTTP_200_OK)

    @extend_schema(tags=["order"])
    def get(self, request: Request) -> Response:
        order: Order = Order.objects.filter(
            user=request.user, status__isnull=False
        ).order_by("-createdAt")
        serializer = OrderSerializer(order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class OrderDetailView(APIView):
    @extend_schema(tags=["order"], responses=OrderSerializer)
    def post(self, request: Request, id: int) -> Response:
        """ Оплатить """
        order: Order = Order.objects.get(id=id)
        if order.status == "Оплачено":
            return Response(status=status.HTTP_409_CONFLICT)
        update_order_info(request, order)
        # TODO Очищение корзины должно происходить во время подтверждения оплаты
        basket: Basket = Basket.objects.get(user=request.user)
        basket.products.clear()
        return Response({"orderId": order.id})

    @extend_schema(tags=["order"], responses=OrderSerializer)
    def get(self, request: Request, id: int) -> Response:
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=["order"], responses=OrderSerializer)
class OldOrdersListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Order.objects.filter(
        createdAt__lt=datetime.now() - timedelta(days=3), status="Ожидает оплаты"
    )
    serializer_class = OrderSerializer


def clean_old_orders(request) -> HttpResponse:
    """
    Удаление заказов старше одного дня
    """
    Order.objects.filter(
        createdAt__lt=datetime.now() - timedelta(days=1),
        status__in=["Оформление заказа", "Ожидает оплаты"],
    ).delete()
    return HttpResponse('Orders cleaned successfully.', content_type='text/plain')

