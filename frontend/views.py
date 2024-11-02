from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import redirect
from django.views import View
from yookassa.domain.exceptions import BadRequestError

from basket_app.models import Order
from payment_app.payment import get_confirmation_url


class PaymentYooKassaView(View):
    def get(self, request: HttpRequest, id:int) -> HttpResponse:
        # TODO HARDCODE
        exchange_rate = 90
        order: Order = Order.objects.get(id=id)
        value: str = str(order.totalCost * exchange_rate)
        description: str = f"Order #{id}"

        try:
            url = get_confirmation_url(value, description, order_id=id)
            return redirect(url)
        except BadRequestError:
            raise Http404("TEST")






