from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View

from basket_app.models import Order
from payment_app.payment import get_confirmation_url


class PaymentYooKassaView(View):
    def get(self, request: HttpRequest, id:int) -> HttpResponse:
        # TODO HARDCODE
        exchange_rate = 90
        order: Order = Order.objects.get(id=id)
        value: str = str(order.totalCost * exchange_rate)
        description: str = f"Order #{id}"
        return redirect(get_confirmation_url(value, description, order_id=id))

