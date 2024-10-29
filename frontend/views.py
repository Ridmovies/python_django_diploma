from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View
from rest_framework.request import Request

from basket_app.models import Order
from basket_app.payment import get_confirmation_url


class PaymentYooKassaView(View):
    def get(self, request: HttpRequest, id:int) -> HttpResponse:
        # TODO HARDCODE
        exchange_rate = 90
        order: Order = Order.objects.get(id=id)
        value: str = str(order.totalCost * exchange_rate)
        description: str = f"Order #{id}"
        print(f"{order.totalCost=}")
        return redirect(get_confirmation_url(value, description))


class PaymentSucces(View):
    def get(self, request) -> HttpResponse:
        print(f"{request=}")
        return redirect('http://127.0.0.1:8000/')
