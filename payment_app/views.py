from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from basket_app.models import Order
from payment_app.payment import get_payment_info


class PaymentNotification(APIView):
    @extend_schema(
        tags=["payment"],
        summary="Подтверждение платежа",
        description="Проверка ответа от YooKassa, если succeeded меняем статус заказа на оплачено",
        # parameters=[
        #     OpenApiParameter(
        #         name='payment_id',
        #         type=str,
        #         location=OpenApiParameter.PATH,
        #         required=True,
        #         description="ID платежа для подтверждения.",
        #     ),
        # ],
    )
    def post(self, request: Request, payment_id: str) -> Response:
        """ Проверка ответа от YooKassa, если succeeded меняем статус заказа на оплачено """
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
#             order.status = 'Оплачено'
#         elif credit_number[-1] == "0":
#             order.status = 'Ошибка оплаты'
#         basket.products.clear()
#         basket.save()
#         order.save()
#         return Response(status=status.HTTP_200_OK)
