from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View

from payment_app.payment import get_confirmation_url


class PaymentYooKassaView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return redirect(get_confirmation_url())

