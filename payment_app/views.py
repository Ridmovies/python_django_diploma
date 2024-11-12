from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from basket_app.models import Order
from payment_app.payment import get_payment_confirm, get_payment_info, get_payments_list


class PaymentListView(APIView):
    @extend_schema(tags=["payment"])
    def get(self, request: Request) -> Response:
        payments_list = get_payments_list()
        return Response(status=status.HTTP_200_OK)


class PaymentNotification(APIView):
    @extend_schema(tags=["payment"])
    def post(self, request: Request, payment_id: str) -> Response:
        payment_info = get_payment_info(payment_id)
        order_id = payment_info.metadata.get("orderId")
        order = Order.objects.get(id=order_id)
        if payment_info.status == "succeeded":
            order.status = "Оплачено"
            order.save()
        else:
            order.status = payment_info.status
            order.save()
        return Response(status=status.HTTP_200_OK)


class PaymentInfoView(APIView):
    @extend_schema(tags=["payment"])
    def get(self, request: Request, payment_id: str) -> Response:
        payment_info = get_payment_info(payment_id)
        print(f"{payment_info.status=}")
        print(f"{payment_info.description=}")
        return Response(status=status.HTTP_200_OK)


class PaymentConfirmView(APIView):
    @extend_schema(tags=["payment"])
    def post(self, request: Request, payment_id: str) -> Response:
        get_payment_confirm(payment_id)
        payment_info = get_payment_info(payment_id)
        if payment_info.status == "succeeded":
            order_id = payment_info.metadata.get("orderId")
            order = Order.objects.get(id=order_id)
            order.status = "Оплачено"
            order.save()
        return Response(status=status.HTTP_200_OK)


# class PaymentView(APIView):
#     @extend_schema(tags=["payment"])
#     def post(self, request: Request, id:int) -> Response:
#         basket: Basket = Basket.objects.get(user=request.user)
#         order = Order.objects.get(id=id)
#         data: dict = request.data
#         credit_number = data.get("number", None)
#         payment: Payment = Payment.objects.create(**data)
#         order.status = 'Ожидает оплаты'
#         serializer = PaymentSerializer(payment, many=False)
#         if credit_number[-1] != "0":
#             # TODO DO validation
#             order.status = 'Оплачено'
#         elif credit_number[-1] == "0":
#             order.status = 'Ошибка оплаты'
#         basket.products.clear()
#         basket.save()
#         order.save()
#         return Response(status=status.HTTP_200_OK)
