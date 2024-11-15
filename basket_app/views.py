from datetime import datetime, timedelta

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
    cancel_order_product,
    create_new_order,
    get_or_create_basket,
    update_order_info,
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
        product_id = request.data.get("id")
        order_product: OrderProduct = OrderProduct.objects.get(
            product_id=product_id,
            basket=basket,
        )
        if order_product:
            cancel_order_product(order_product, product_id)

        serializer = OrderProductSerializer(basket.products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrdersListView(APIView):
    @extend_schema(tags=["order"])
    def post(self, request: Request) -> Response:
        # Создание заказа
        basket: Basket = Basket.objects.get(user=request.user)
        new_order = create_new_order(request)
        add_products_in_order(request, basket, new_order)
        return Response({"orderId": new_order.id}, status=status.HTTP_200_OK)

    @extend_schema(tags=["order"])
    def get(self, request: Request) -> Response:
        # TODO Clean not active orders
        order: Order = Order.objects.filter(
            user=request.user, status__isnull=False
        ).order_by("-createdAt")
        serializer = OrderSerializer(order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class OrderDetailView(APIView):
    @extend_schema(tags=["order"], responses=OrderSerializer)
    def post(self, request: Request, id: int) -> Response:
        order: Order = Order.objects.get(id=id)
        if order.status == "Оплачено":
            return Response(status=status.HTTP_409_CONFLICT)
        update_order_info(request, order)
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
